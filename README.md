# Manifest Toolkit

**Manifest** — formal semantics for data, sitting in the practical gap between schemas and ontologies.

## The problem

Data formats like Parquet tell you column names and physical types. Everything else — what the values mean, how datasets relate to each other, why the rows are ordered that way, what's known to be broken — lives in people's heads, scattered documentation, and Slack threads. That implicit knowledge is where integration bugs, silent data quality failures, and misinterpretation come from.

This matters more now than it used to. LLMs are increasingly writing SQL, building analyses, and making decisions from data. They see column names and types, but they're blind to the structural context that prevents misuse: that this is a snapshot dataset requiring deduplication, that this column's values are constrained to an enum, that these two datasets share an entity key under different column names, that the data has known gaps you shouldn't smooth over.

## What Manifest does

Manifest makes that implicit knowledge explicit, machine-readable, and queryable. It's an RDF vocabulary for expressing structural metadata about data — the things that are true about your data beyond what the storage format captures:

- **Semantic types with constraints** — not just "this is a DOUBLE" but "this is a WGS84 latitude in degrees, range [-90, 90]", or "this is a trade side, one of {BUY, SELL}"
- **Cross-dataset relationships** — foreign keys with integrity levels, shared entity identifiers across datasets with different column names, aggregation dependencies that the system can verify
- **Physical layout as a first-class concern** — row ordering that distinguishes "sorted for index efficiency" from "sorted because it's a meaningful temporal sequence", partition schemes that map to file paths
- **Row semantics** — whether each row is an independent event, a point-in-time snapshot of a recurring entity (requiring deduplication), or an aggregate summary
- **Known deficiencies** — formal declarations of where reality falls short of the ideal. That AIS data has undocumented gaps. That Polymarket schemas are inferred from JSON and may vary between files. Knowing what NOT to assume prevents more bugs than knowing what to assume.
- **Derivations and provenance** — which columns are computed from which others, what transformations were applied upstream

All of this is expressed as RDF in Turtle files, queryable via SPARQL, composable across domains, and directly consumable by LLMs through the built-in MCP server. See the [generated dataset tables](descriptions/generated/) for a readable view of what's described.

## Design principles

Manifest sits between a schema and a full ontology — formal enough to be machine-readable, lightweight enough that you can describe a new domain in a single Turtle file.

- **Description and verification are decoupled.** The graph records what is asserted about data; validators are external tools whose results are recorded as attestations. The descriptions are useful on their own — for documentation, for LLM context, for integration planning — even if you never run a validator.
- **Combinators over opaque leaves.** The system reasons about structure generically; domain-specific semantics live in extensible leaf terms identified by URI. Adding a new semantic type doesn't require changing the core vocabulary.
- **Physical and logical are both first-class.** Storage layout (ordering, partitioning, file format) carries semantic weight and is formally described alongside logical structure.
- **Cost-aware execution.** Validators declare their computational profile so the engine runs cheapest checks first — Parquet metadata before column scans, column scans before full-file reads.

## Quick Start

```bash
# Install (editable, from the repo root)
uv sync  # or: pip install -e .

# See what the Manifest graph describes (no data needed)
mnf describe --vocab vocabularies/ --desc descriptions/

# Generate browsable markdown tables from the descriptions
mnf generate-docs --vocab vocabularies/ --desc descriptions/ --out descriptions/generated/

# Instant schema check — catches type mismatches from Parquet metadata alone
mnf validate path/to/ais-2025-01-01.parquet \
    --dataset ais:DailyBroadcasts \
    --vocab vocabularies/ --desc descriptions/ \
    --max-level schema

# Full validation — value ranges, ordering, monotonicity
mnf validate path/to/ais-2025-01-01.parquet \
    --dataset ais:DailyBroadcasts \
    --vocab vocabularies/ --desc descriptions/ \
    --verbose

# Inspect a Parquet file's raw metadata
mnf info path/to/data.parquet
```

## MCP Server

Manifest includes an [MCP](https://modelcontextprotocol.io/) server that exposes dataset metadata to AI agents. It supports two modes:

- **SQL advisor** — the agent reads the Manifest metadata (vocabulary, descriptions, relationships) and uses it to write correct DuckDB SQL for the client to execute on their own connection (e.g. DuckDB on S3). This is the primary use case.
- **Query execution** — with `--data`, the server also registers DuckDB views from local Parquet files and can execute queries directly.

```bash
# SQL advisor mode — metadata only, no data access needed
mnf serve --vocab vocabularies/ --desc descriptions/

# With data — also registers DuckDB views for server-side query execution
mnf serve --vocab vocabularies/ --desc descriptions/ \
    --data /data/ais/ --data /data/polymarket/
```

The project includes an `.mcp.json` that configures the server for Claude Code:

```bash
# Start a Claude Code session in the project directory — the MCP server starts automatically
claude
```

### How it works

On startup the server:
1. Loads the Manifest graph from vocabulary and description files
2. Loads raw Turtle content for vocabulary and description resources
3. Pre-renders markdown documentation for each description file
4. If `--data` is provided: creates an in-memory DuckDB connection, converts partition path templates to globs, and registers views for datasets with matching files

### Resources

The server exposes the Manifest metadata in two formats — rendered markdown documentation and raw RDF Turtle. The markdown is human-friendly; the Turtle gives the agent full access to everything in the graph.

| URI | Description |
|-----|-------------|
| `manifest://vocabulary` | The core Manifest vocabulary as raw Turtle (RDF). Defines all classes, properties, and named individuals. Read this to understand what the properties in description files mean. |
| `manifest://description/{domain}` | A domain description as raw Turtle (RDF). Full dataset metadata: columns, types, layout, partitioning, ordering, derivations, relationships, deficiencies, provenance. |
| `manifest://docs/{domain}` | Pre-rendered markdown documentation for a domain. Includes schemas, semantic types, ordering, relationships, deficiencies, and agent notes. |

### Tools

| Tool | Parameters | Description |
|------|------------|-------------|
| `list_datasets` | — | Returns available datasets with view names, column counts, row counts, and documentation resource URIs. |
| `setup_views` | `s3_prefix: str` | Generates `CREATE VIEW` statements for all datasets, combining the S3 prefix with each dataset's path template. For client-side DuckDB connected to S3. |
| `sparql` | `query: str` | Executes a SPARQL query against the loaded Manifest graph. Standard prefixes (mnf:, ais:, pm:, etc.) are injected automatically. Returns results as a markdown table. |
| `query` | `sql: str`, `format: str` | Executes a DuckDB SQL query against registered views (requires `--data`). Format is `"markdown"` (default, 100 row limit) or `"csv"` (denser, 500 row limit). Truncated results include a per-column statistical summary of the full result set. |

### Typical agent workflow

**SQL advisor** (client has own DuckDB, e.g. on S3):
1. Call `list_datasets()` to discover available datasets
2. Read `manifest://description/{domain}` for the full RDF metadata — columns, types, partitioning, relationships, known deficiencies
3. Call `setup_views(s3_prefix)` to get `CREATE VIEW` statements; execute them on the client's DuckDB
4. Use `sparql(query)` to drill into specific metadata (e.g. foreign keys, value ranges) when needed
5. Write correct SQL using the metadata context; the client executes it

**Server-side query execution** (server has data access via `--data`):
1. Call `list_datasets()` to discover what's available
2. Read `manifest://docs/{domain}` for schema context
3. Write SQL against the view names and call `query(sql)`

### Client configuration

The server uses stdio transport. To configure it for Claude Code, add to `.mcp.json`:

```json
{
  "mcpServers": {
    "manifest": {
      "command": "uv",
      "args": [
        "run", "--directory", "/path/to/manifest-toolkit",
        "mnf", "serve",
        "--vocab", "vocabularies/",
        "--desc", "descriptions/"
      ]
    }
  }
}
```

## Python API

```python
from pathlib import Path
from manifest import ManifestGraph, ValidationEngine

# Load the graph — vocabulary + one or more domain descriptions
graph = ManifestGraph()
graph.load("vocabularies/mnf_core.ttl")
graph.load("descriptions/ais_description.ttl")
graph.load("descriptions/polymarket_description.ttl")

# Inspect what's described — works across domains at once
for ds_uri in graph.list_datasets():
    ds = graph.get_dataset(ds_uri)
    print(f"{ds.label}: {len(ds.columns)} columns")

# Validate a file against its description
engine = ValidationEngine(graph)
attestations = engine.validate_file(
    Path("data/gamma-markets/hour=00.parquet"),
    "pm:MarketSnapshots",
    verbose=True,
)
for a in attestations:
    print(a.summary_line())

# Explore metadata — semantic types, derivations, cross-dataset links
st = graph.get_semantic_type("ais:MMSI")
print(f"MMSI requires: {st.required_physical_type}, range: [{st.min_inclusive}, {st.max_inclusive}]")

derivations = graph.get_derivations("pm:MarketSnapshots")   # spread <- bestAsk, bestBid
aggregations = graph.get_aggregations("ais:DailyIndex")     # broadcasts -> index
deficiencies = graph.get_known_deficiencies("pm:MarketSnapshots")
```

## Validation

### Levels

Validators run in cost order, cheapest first:

| Level | Profile | What it checks | Data read |
|-------|---------|---------------|-----------|
| 0 | `SCHEMA_CHECK` | Physical types, column presence | Parquet footer only |
| 1 | `PER_VALUE` | Value ranges from semantic types | Column scan |
| 2 | `FULL_SCAN` | Constant columns, partition keys | Full file |
| 3 | `SEQUENTIAL_SCAN` | Row ordering, within-group monotonicity | Ordered scan |
| — | `FULL_SCAN` | Aggregation consistency (with companion) | Both files |

Use `--max-level schema` for instant type-mismatch detection.

### Description validation (SHACL)

The validation engine checks *data files* against descriptions. But what checks the *descriptions themselves*? `vocabularies/mnf_shapes.ttl` provides [SHACL](https://www.w3.org/TR/shacl/) shapes that validate the structure of Manifest description graphs — catching missing required properties, wrong value types, and malformed nested structures before any data is touched.

```python
from pyshacl import validate
from rdflib import Graph

data = Graph()
data.parse("vocabularies/mnf_core.ttl")
data.parse("descriptions/ais_description.ttl")

shapes = Graph()
shapes.parse("vocabularies/mnf_shapes.ttl")

conforms, report_graph, report_text = validate(data, shacl_graph=shapes)
if not conforms:
    print(report_text)
```

22 shapes cover every class in the vocabulary. See [`docs/shacl-shapes.md`](docs/shacl-shapes.md) for full details.

## Adding a New Domain

1. Define semantic types for your domain in a new `.ttl` file in `descriptions/`
2. Describe your datasets: columns, physical types, semantic types
3. Declare relationships: derivations, aggregations, ordering, foreign keys, provenance
4. Use vocabulary terms for richer metadata:
   - `entityKey` + `snapshotTimestamp` for snapshot data
   - `AllowedValues` for categorical constraints
   - `embeddedStructure` for JSON-in-string columns
   - `ForeignKey` and `SameEntity` for cross-dataset links
   - `schemaStability` for inferred/variable schemas
   - `CompositePartitionScheme` for multi-level partitioning
5. Validate the description with SHACL (`pyshacl`) to catch structural errors early
6. Run `mnf validate` — standard checks (schema, ranges, ordering) work automatically
7. For domain-specific constraints, implement validators and register via `ValidatorRegistry`

The core vocabulary was extended once — when modelling Polymarket data surfaced 7 domain-independent gaps. All additions were backward-compatible. See [`docs/vocabulary-evolution.md`](docs/vocabulary-evolution.md) for the full story.

## Domain Examples

Manifest ships with three Parquet-shaped domain descriptions that together exercise the core vocabulary:

| | AIS Maritime Data | Polymarket Prediction Markets | Foursquare Places |
|-|-------------------|-------------------------------|-------------------|
| **File** | `ais_description.ttl` | `polymarket_description.ttl` | `foursquare_description.ttl` |
| **Datasets** | 2 (broadcasts + index) | 9 (6 core + 3 reference) | 3 (places + detailed + categories) |
| **Row semantics** | Events (each row = one broadcast) | Snapshots (same entity repeated) | Snapshots (periodic bulk release) |
| **Ordering** | Meaningful (MMSI + timestamp) | None (poll arrival order) | None |
| **Partitioning** | Single-level (daily) | Two-level (date + hour) | Sharded (non-partitioned) |
| **Schema** | Fixed (declared) | Inferred (Polars from JSON) | Fixed |
| **Cross-dataset links** | Aggregation (broadcasts -> index) | Foreign keys + entity identity | Foreign key (places -> categories) |
| **Key patterns** | Ordering semantics, aggregation, column groups | Entity keys, embedded JSON, allowed values, composite partitions | Sharded files, struct types, list-to-scalar FK |

A fourth description, `beaver_description.ttl`, covers two MySQL databases — `keystone` (OpenStack identity service from CSAIL Stata's deployment, heavily anonymised) and `dw` (MIT's institutional data warehouse, real campus data). The data is sourced from the dumps released as part of the [BEAVER text-to-SQL benchmark](https://peterbaile.github.io/beaver/), but the description is general-purpose: it captures structural facts (anonymisation namespaces, soft FKs, sentinel values, parallel-table conventions, case conventions, etc.) that any consumer writing SQL against these databases would benefit from, without leaking information about any particular benchmark question set. It's intended as LLM context for SQL generation, not for the validation engine, and is the kind of description the project's MCP server is built to serve. The description stress-tests the vocabulary into territory the original Parquet-shaped domains didn't cover — soft and polymorphic foreign keys, multi-namespace anonymisation (where joining on what looks like the same identifier silently returns zero rows), sentinel-string-as-NULL, parallel/duplicate tables, SCD-2 history, MySQL reserved-word table names. Inline `[BVT-K-GAP-N]` tags against the inventory in [`docs/vocabulary-evolution.md`](docs/vocabulary-evolution.md) flag where modelling hit the vocabulary's limits; round 1 of evolution resolved five of those (file formats, row counts, soft-FK marker, identifier namespaces, case conventions).

Coverage detail: keystone is fully described (17 populated tables + 4 schema-only federation tables). All 97 dw tables are present — most as rich descriptions, the rest as schema-only stubs in a "PART 3 (continued): DW — schema stubs" section near the end of the file. The stubs (lookup / history / mirror tables) carry only column names and types; they're a clearly-marked extension point for upgrade as further investigations land.

## Structure

```
manifest-toolkit/
├── manifest/                 # Python package
│   ├── model.py              # Core data types (Attestation, ColumnInfo, etc.)
│   ├── graph.py              # Manifest graph loader and query layer (rdflib)
│   ├── engine.py             # Graph-driven validation orchestrator
│   ├── registry.py           # Extensible validator registry
│   ├── cli.py                # Click CLI
│   ├── server.py             # MCP server (FastMCP)
│   └── validators/           # Built-in validators
│       ├── schema.py         #   Physical type checks (Parquet metadata only)
│       ├── values.py         #   Value range checks (DuckDB scan)
│       ├── ordering.py       #   Row ordering + monotonicity (DuckDB)
│       └── aggregation.py    #   Index/summary consistency (DuckDB)
├── vocabularies/             # Core Manifest vocabulary (domain-independent)
│   ├── mnf_core.ttl
│   └── mnf_shapes.ttl        # SHACL shapes for description validation
├── descriptions/             # Domain-specific descriptions
│   ├── ais_description.ttl           # NOAA AIS maritime data
│   ├── polymarket_description.ttl    # Polymarket prediction-market data
│   ├── foursquare_description.ttl    # Foursquare Open Source Places data
│   ├── beaver_description.ttl        # keystone (OpenStack) + dw (MIT data warehouse) MySQL databases
│   └── generated/                    # Markdown tables (regenerate with mnf generate-docs)
├── tests/
│   └── test_server.py               # MCP server helper tests
├── docs/
│   ├── vocabulary-evolution.md       # How the Polymarket domain drove vocabulary extensions
│   └── shacl-shapes.md              # SHACL shapes: goals, design decisions, usage
├── .mcp.json                         # MCP server config for Claude Code
├── pyproject.toml
└── README.md
```

## Current State and Limitations

This is a v0.1 prototype. It works end-to-end against real data, but there are important things to know:

**The engine is graph-driven but not yet fully generic.** It reads the Manifest graph to discover columns, semantic types, ordering keys, and aggregation relationships, and dispatches built-in validators automatically. However, the combinator-based constraint model (`mnf:Grouped` / `mnf:Ordered` / `mnf:innerConstraint` chains) is not yet walked generically — the engine recognises specific patterns rather than interpreting arbitrary combinator trees. Making that fully generic is the natural next evolution.

**The validator registry exists but isn't wired into the engine yet.** `ValidatorRegistry` is the extension point for domain-specific validators (e.g. a custom H3 derivation checker, or the `MaxConsecutiveImpliedSpeed` sequential aggregation). Currently the engine dispatches directly to built-in validators.

**Standard aggregations are verified automatically; custom ones are skipped.** The aggregation validator handles `MIN`, `MAX`, `MEAN`, `COUNT`, `COUNT DISTINCT`, and `DISTINCT LIST`. Sequential/windowed aggregations need domain-specific validators.

**Validators are tied to local Parquet files.** The validators use `pyarrow` for schema inspection and `duckdb` for data queries on local files. S3 support is straightforward but isn't parameterised yet. The MCP server's SQL advisor workflow works with remote data (the client runs the queries), but the validation engine currently requires local files.

**New vocabulary terms don't yet have validators.** `AllowedValues`, `entityKey`, `embeddedStructure`, `ForeignKey`, `schemaStability`, `SameEntity`, and `CompositePartitionScheme` are fully expressible in the graph and immediately useful for documentation and LLM consumption, but the engine doesn't yet check them against data.

## Dependencies

- `rdflib >= 7.0` — RDF graph loading and SPARQL
- `duckdb >= 1.0` — efficient Parquet scanning for validation queries and MCP server
- `pyarrow >= 15.0` — Parquet schema inspection
- `click >= 8.0` — CLI
- `mcp >= 1.0` — Model Context Protocol server

Requires Python >= 3.12. Optional: `h3` (for H3 derivation validation), `pytest` (for tests).

## Tests

```bash
uv run --extra dev pytest
```

Tests cover the MCP server helpers: path template globbing, markdown/CSV formatting, DuckDB query summarisation, SPARQL queries, and setup_views logic.
