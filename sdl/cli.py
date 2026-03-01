"""
SDL Toolkit CLI.

Usage:
    sdl validate <file.parquet> --dataset ais:DailyBroadcasts --vocab vocab/ --desc desc/
    sdl validate <broadcast.parquet> --dataset ais:DailyBroadcasts --companion <index.parquet> --companion-dataset ais:DailyIndex
    sdl describe <vocab_dir> <desc_dir>
    sdl info <file.parquet>
"""

from __future__ import annotations

from pathlib import Path

import click

from sdl.engine import ValidationEngine
from sdl.graph import SDLGraph
from sdl.model import ComputationalProfile, ValidationResult


def _load_graph(
    vocab_paths: tuple[str, ...],
    desc_paths: tuple[str, ...],
) -> SDLGraph:
    """Load vocabulary and description files into an SDLGraph."""
    graph = SDLGraph()
    for p in vocab_paths:
        path = Path(p)
        if path.is_dir():
            graph.load_directory(path)
        else:
            graph.load(path)
    for p in desc_paths:
        path = Path(p)
        if path.is_dir():
            graph.load_directory(path)
        else:
            graph.load(path)
    return graph


@click.group()
def main() -> None:
    """SDL Toolkit — Structural Data Language for data lakes."""
    pass


@main.command()
@click.argument("file_path", type=click.Path(exists=True))
@click.option(
    "--dataset", "-d",
    required=True,
    help="SDL dataset URI (e.g. ais:DailyBroadcasts)",
)
@click.option(
    "--vocab", "-v",
    multiple=True,
    required=True,
    help="Path to vocabulary .ttl file or directory",
)
@click.option(
    "--desc",
    multiple=True,
    required=True,
    help="Path to description .ttl file or directory",
)
@click.option(
    "--companion", "-c",
    type=click.Path(exists=True),
    default=None,
    help="Path to companion file (e.g. index file)",
)
@click.option(
    "--companion-dataset",
    default=None,
    help="SDL dataset URI for the companion file",
)
@click.option(
    "--max-level",
    type=click.Choice(["schema", "values", "scan", "sequential"]),
    default="sequential",
    help="Maximum validation depth",
)
@click.option("--turtle", is_flag=True, help="Output attestations as Turtle")
@click.option("--verbose", is_flag=True, help="Print progress")
def validate(
    file_path: str,
    dataset: str,
    vocab: tuple[str, ...],
    desc: tuple[str, ...],
    companion: str | None,
    companion_dataset: str | None,
    max_level: str,
    turtle: bool,
    verbose: bool,
) -> None:
    """Validate a Parquet file against its SDL description."""
    level_map = {
        "schema": ComputationalProfile.SCHEMA_CHECK,
        "values": ComputationalProfile.PER_VALUE,
        "scan": ComputationalProfile.FULL_SCAN,
        "sequential": ComputationalProfile.SEQUENTIAL_SCAN,
    }

    graph = _load_graph(vocab, desc)
    engine = ValidationEngine(graph)

    attestations = engine.validate_file(
        Path(file_path),
        dataset,
        companion_path=Path(companion) if companion else None,
        companion_dataset_uri=companion_dataset,
        max_profile=level_map[max_level],
        verbose=verbose,
    )

    # Summary
    passes = sum(1 for a in attestations if a.result == ValidationResult.PASS)
    fails = sum(1 for a in attestations if a.result == ValidationResult.FAIL)
    warns = sum(1 for a in attestations if a.result == ValidationResult.WARN)
    errors = sum(1 for a in attestations if a.result == ValidationResult.ERROR)

    click.echo(f"\n{'=' * 72}")
    click.echo(
        f"  {passes} passed  {fails} failed  {warns} warnings  {errors} errors"
    )
    click.echo(f"{'=' * 72}\n")

    for a in attestations:
        click.echo(a.summary_line())
        if a.result != ValidationResult.PASS:
            for line in a.details.split("\n"):
                click.echo(f"      {line}")

    if turtle:
        click.echo("\n# --- Attestation Triples ---")
        click.echo("@prefix sdl: <http://example.org/sdl#> .")
        click.echo("@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .")
        click.echo()
        for a in attestations:
            click.echo(a.to_turtle())

    # Exit code: non-zero if any failures
    if fails > 0 or errors > 0:
        raise SystemExit(1)


@main.command()
@click.option(
    "--vocab", "-v",
    multiple=True,
    required=True,
    help="Path to vocabulary .ttl file or directory",
)
@click.option(
    "--desc",
    multiple=True,
    required=True,
    help="Path to description .ttl file or directory",
)
def describe(vocab: tuple[str, ...], desc: tuple[str, ...]) -> None:
    """Show a summary of datasets described in the SDL graph."""
    graph = _load_graph(vocab, desc)

    for ds_uri in graph.list_datasets():
        ds = graph.get_dataset(ds_uri)
        click.echo(f"\n{'=' * 60}")
        click.echo(f"Dataset: {ds.label}")
        click.echo(f"URI:     {ds.uri}")
        click.echo(f"Format:  {ds.file_format}")

        if ds.partition_path_template:
            click.echo(f"Path:    {ds.partition_path_template}")
        if ds.partition_granularity:
            click.echo(f"Partitioned: {ds.partition_granularity}")

        click.echo(f"\nColumns ({len(ds.columns)}):")
        for col in sorted(ds.columns, key=lambda c: c.name):
            sem = f"  [{col.semantic_type}]" if col.semantic_type else ""
            click.echo(f"  {col.name:24s} {col.physical_type:16s}{sem}")

        if ds.ordering_keys:
            keys = sorted(ds.ordering_keys, key=lambda k: k.precedence)
            click.echo(f"\nRow ordering:")
            for k in keys:
                click.echo(
                    f"  {k.precedence}. {k.column_name} {k.direction} "
                    f"({k.semantic})"
                )

        derivations = graph.get_derivations(ds_uri)
        if derivations:
            click.echo(f"\nDerivations:")
            for d in derivations:
                props = ", ".join(d.properties) if d.properties else ""
                click.echo(
                    f"  {d.derived_column} <- {d.source_columns} "
                    f"via {d.function_uri} [{props}]"
                )

        deficiencies = graph.get_known_deficiencies(ds_uri)
        if deficiencies:
            click.echo(f"\nKnown deficiencies:")
            for d in deficiencies:
                click.echo(f"  [{d['severity']}] {d['description'][:80]}...")

        companions = graph.get_companions(ds_uri)
        if companions:
            click.echo(f"\nCompanions: {', '.join(companions)}")

    # Show aggregation relationships
    for ds_uri in graph.list_datasets():
        aggs = graph.get_aggregations(ds_uri)
        for agg in aggs:
            click.echo(f"\n{'=' * 60}")
            click.echo(f"Aggregation: {agg.source_dataset} -> {agg.target_dataset}")
            click.echo(f"Group by: {agg.group_by_column}")
            click.echo(f"Columns ({len(agg.aggregated_columns)}):")
            for ac in agg.aggregated_columns:
                order = f" (ordered by {ac.within_group_ordering})" if ac.within_group_ordering else ""
                click.echo(
                    f"  {ac.target_column:24s} = "
                    f"{ac.function_uri}({', '.join(ac.source_columns)})"
                    f"{order}"
                )


@main.command()
@click.argument("file_path", type=click.Path(exists=True))
def info(file_path: str) -> None:
    """Show Parquet file metadata (for quick inspection)."""
    import pyarrow.parquet as pq

    pf = pq.ParquetFile(file_path)
    meta = pf.metadata
    schema = pf.schema_arrow

    click.echo(f"File: {file_path}")
    click.echo(f"Rows: {meta.num_rows:,}")
    click.echo(f"Row groups: {meta.num_row_groups}")
    click.echo(f"Columns: {meta.num_columns}")
    click.echo(f"Created by: {meta.created_by}")
    click.echo(f"Format version: {meta.format_version}")
    click.echo()

    click.echo("Schema:")
    for i in range(len(schema)):
        f = schema.field(i)
        click.echo(f"  {f.name:24s} {str(f.type):30s} nullable={f.nullable}")

    if meta.num_row_groups > 0:
        click.echo(f"\nRow group 0 (of {meta.num_row_groups}):")
        rg = meta.row_group(0)
        click.echo(f"  Rows: {rg.num_rows:,}")
        for j in range(rg.num_columns):
            col = rg.column(j)
            click.echo(
                f"  {col.path_in_schema:24s} "
                f"compressed={col.total_compressed_size:>10,} "
                f"uncompressed={col.total_uncompressed_size:>10,}"
            )


if __name__ == "__main__":
    main()
