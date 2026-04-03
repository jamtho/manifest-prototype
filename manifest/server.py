"""Manifest MCP server — expose dataset metadata and DuckDB query tools."""

from __future__ import annotations

import csv
import io
import re
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from dataclasses import dataclass, field
from pathlib import Path

import duckdb
from mcp.server.fastmcp import FastMCP, Context
from rdflib import Graph

from manifest.graph import ManifestGraph, MNF, RDF, _str
from manifest.cli import _render_description, _load_graph


@dataclass
class AppContext:
    graph: ManifestGraph
    db: duckdb.DuckDBPyConnection
    views: dict[str, str] = field(default_factory=dict)  # view_name -> dataset_uri
    docs: dict[str, str] = field(default_factory=dict)  # domain_name -> markdown


def _template_to_glob(template: str) -> str:
    """Convert a partition path template to a glob pattern.

    Placeholders that occupy an entire path segment (e.g. '{stream}') become
    '**' to match multiple directory levels.  Inline placeholders (e.g.
    'ais-{date}.parquet') become '*'.
    """
    def _replace(m: re.Match) -> str:
        # Check if the placeholder is the entire segment
        start, end = m.start(), m.end()
        seg_start = template.rfind("/", 0, start) + 1
        seg_end = template.find("/", end)
        if seg_end == -1:
            seg_end = len(template)
        if seg_start == start and seg_end == end:
            return "**"
        return "*"

    return re.sub(r"\{[^}]+\}", _replace, template)


def _label_to_view_name(label: str) -> str:
    """Sanitize a dataset label to a valid SQL identifier.

    E.g. 'AIS Daily Broadcast Positions' -> 'ais_daily_broadcast_positions'
    """
    name = label.lower().strip()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    name = name.strip("_")
    return name


def _register_views(
    db: duckdb.DuckDBPyConnection,
    graph: ManifestGraph,
    data_roots: list[Path],
) -> dict[str, str]:
    """Register DuckDB views for datasets that have matching files under data roots.

    Returns a mapping of view_name -> dataset_uri for successfully registered views.
    """
    views: dict[str, str] = {}

    for ds_uri in graph.list_datasets():
        ds = graph.get_dataset(ds_uri)
        if not ds.partition_path_template:
            continue

        glob_pattern = _template_to_glob(ds.partition_path_template)
        view_name = _label_to_view_name(ds.label)

        # Try each data root until we find one with matching files
        for root in data_roots:
            full_glob = root / glob_pattern
            matches = list(root.glob(glob_pattern))
            if matches:
                # Use forward slashes for DuckDB compatibility
                glob_path = str(full_glob).replace("\\", "/")
                sql = (
                    f"CREATE VIEW {view_name} AS "
                    f"SELECT * FROM read_parquet('{glob_path}', "
                    f"hive_partitioning=true)"
                )
                db.execute(sql)
                views[view_name] = ds_uri
                break

    return views


def _render_docs(
    graph: ManifestGraph,
    desc_paths: list[str],
) -> dict[str, str]:
    """Pre-render markdown docs for each description file.

    Returns a mapping of domain_name -> markdown content.
    """
    docs: dict[str, str] = {}

    desc_files: list[Path] = []
    for p in desc_paths:
        path = Path(p)
        if path.is_dir():
            desc_files.extend(sorted(path.glob("*.ttl")))
        else:
            desc_files.append(path)

    for desc_file in desc_files:
        tmp = Graph()
        tmp.parse(str(desc_file), format="turtle")
        ds_uris = [_str(s) for s in tmp.subjects(RDF.type, MNF.Dataset)]
        if not ds_uris:
            continue

        # Domain name from filename: 'ais_description.ttl' -> 'ais'
        domain = desc_file.stem.replace("_description", "")
        md = _render_description(graph, ds_uris, desc_file.name)
        docs[domain] = md

    return docs


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Initialize ManifestGraph, DuckDB, and register views on startup."""
    config = server._custom_config

    graph = _load_graph(
        tuple(config["vocab_paths"]),
        tuple(config["desc_paths"]),
    )

    db = duckdb.connect(":memory:")

    data_roots = [Path(p) for p in config.get("data_paths") or []]
    views = _register_views(db, graph, data_roots) if data_roots else {}

    docs = _render_docs(graph, config["desc_paths"])

    ctx = AppContext(graph=graph, db=db, views=views, docs=docs)
    try:
        yield ctx
    finally:
        db.close()


def _format_markdown_table(columns: list[str], rows: list[tuple]) -> str:
    """Format rows as a markdown table."""
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for row in rows:
        cells = [str(v) if v is not None else "NULL" for v in row]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def _format_csv(columns: list[str], rows: list[tuple]) -> str:
    """Format rows as CSV text."""
    buf = io.StringIO(newline="")
    writer = csv.writer(buf)
    writer.writerow(columns)
    for row in rows:
        writer.writerow("" if v is None else v for v in row)
    # csv module writes \r\n per RFC 4180; strip for MCP text responses
    return buf.getvalue().replace("\r\n", "\n").rstrip("\n")


def _summarise_query(db: duckdb.DuckDBPyConnection, sql: str) -> str:
    """Return a compact statistical summary of the full query result.

    Uses DuckDB's SUMMARIZE to compute per-column stats (type, min, max,
    approx unique, avg, null%) over the complete result set.
    """
    try:
        result = db.execute(f"SUMMARIZE ({sql})")
        summary_cols = [desc[0] for desc in result.description]
        summary_rows = result.fetchall()
    except duckdb.Error:
        return ""

    if not summary_rows:
        return ""

    # Pick the most useful columns for a compact summary
    want = ["column_name", "column_type", "min", "max",
            "approx_unique", "avg", "count", "null_percentage"]
    indices = []
    headers = []
    for col in want:
        if col in summary_cols:
            indices.append(summary_cols.index(col))
            headers.append(col)

    if not indices:
        return ""

    lines = [
        "\n**Full result summary:**",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in summary_rows:
        cells = [str(row[i]) if row[i] is not None else "" for i in indices]
        lines.append("| " + " | ".join(cells) + " |")

    return "\n".join(lines)


def create_server(
    vocab_paths: list[str],
    desc_paths: list[str],
    data_paths: list[str] | None = None,
) -> FastMCP:
    """Create and configure the Manifest MCP server."""
    mcp = FastMCP(
        "Manifest",
        lifespan=app_lifespan,
    )
    mcp._custom_config = {
        "vocab_paths": vocab_paths,
        "desc_paths": desc_paths,
        "data_paths": data_paths or [],
    }

    @mcp.resource("manifest://docs/{domain}")
    def get_docs(domain: str) -> str:
        """Get markdown documentation for a dataset domain.

        Returns the full dataset description including schemas, semantic types,
        ordering, relationships, and deficiencies — everything needed to write
        correct queries.
        """
        app: AppContext = mcp.get_context().request_context.lifespan_context
        md = app.docs.get(domain)
        if md is None:
            available = ", ".join(sorted(app.docs.keys())) or "(none)"
            return f"Unknown domain '{domain}'. Available: {available}"
        return md

    @mcp.tool()
    def query(sql: str, format: str = "markdown", ctx: Context = None) -> str:
        """Execute a DuckDB SQL query against registered dataset views.

        Use list_datasets() first to discover available views and read
        manifest://docs/{domain} resources for schema details before querying.

        Args:
            sql: The SQL query to execute.
            format: Response format — "markdown" (default, 100 row limit) or
                "csv" (denser, 500 row limit). Both formats append a statistical
                summary when the result is truncated.
        """
        app: AppContext = ctx.request_context.lifespan_context
        if not app.views:
            return (
                "No data configured. Start the server with --data to "
                "register dataset views for querying."
            )

        if format not in ("markdown", "csv"):
            return f"Unknown format '{format}'. Use 'markdown' or 'csv'."

        row_limit = 100 if format == "markdown" else 500

        try:
            result = app.db.execute(sql)
            columns = [desc[0] for desc in result.description]
            rows = result.fetchmany(row_limit)
        except duckdb.Error as e:
            return f"Query error: {e}"

        if not rows:
            return "Query returned no results."

        try:
            total = app.db.execute(
                f"SELECT count(*) FROM ({sql})"
            ).fetchone()[0]
        except duckdb.Error:
            total = len(rows)

        truncated = total > row_limit

        # Format rows
        if format == "csv":
            output = _format_csv(columns, rows)
        else:
            output = _format_markdown_table(columns, rows)

        if truncated:
            output += f"\n\n*Showing {len(rows):,} of {total:,} rows.*\n"
            output += _summarise_query(app.db, sql)

        return output

    @mcp.tool()
    def list_datasets(ctx: Context) -> str:
        """List available datasets with their view names, row counts, and column counts.

        Use this for discovery before querying.
        """
        app: AppContext = ctx.request_context.lifespan_context
        graph = app.graph

        lines: list[str] = []
        lines.append("| Dataset | View Name | Columns | Rows | Data |")
        lines.append("|---------|-----------|---------|------|------|")

        for ds_uri in graph.list_datasets():
            ds = graph.get_dataset(ds_uri)
            view_name = _label_to_view_name(ds.label)
            col_count = len(ds.columns)

            if view_name in app.views:
                try:
                    row_count = app.db.execute(
                        f"SELECT count(*) FROM {view_name}"
                    ).fetchone()[0]
                    rows_str = f"{row_count:,}"
                except duckdb.Error:
                    rows_str = "error"
                data_str = "yes"
            else:
                rows_str = "—"
                data_str = "no"

            lines.append(
                f"| {ds.label} | `{view_name}` | {col_count} "
                f"| {rows_str} | {data_str} |"
            )

        # Available docs
        if app.docs:
            lines.append("")
            lines.append("**Documentation resources:**")
            for domain in sorted(app.docs.keys()):
                lines.append(f"- `manifest://docs/{domain}`")

        return "\n".join(lines)

    return mcp
