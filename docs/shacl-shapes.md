# SHACL Shapes for Manifest Descriptions

*2026-04-03*

Manifest descriptions are RDF graphs: Turtle files that assert structural metadata about datasets. Until now, the contract for what makes a description *well-formed* has been implicit — spread across the vocabulary comments, the Python graph loader's query assumptions, and the existing domain descriptions used as templates. A missing `mnf:columnName` on a Column, or a `mnf:valueRange` attached directly to a Column instead of its SemanticType, would only surface as a `None` at runtime.

`vocabularies/mnf_shapes.ttl` makes that contract explicit using [SHACL](https://www.w3.org/TR/shacl/) (Shapes Constraint Language). It validates *descriptions themselves* — before any data file is touched.

## Why SHACL, and why here

Manifest already has a clear separation between description and verification: the RDF graph records what is *asserted*; the validation engine checks whether *data files* conform to those assertions. SHACL adds a third layer: checking whether the *assertions themselves* are structurally sound. The layers are:

```
  mnf_shapes.ttl          "Is this description well-formed?"
       │                   (SHACL — runs on the RDF graph)
       ▼
  mnf_core.ttl +          "What does this description say?"
  *_description.ttl        (vocabulary + domain assertions)
       │
       ▼
  validation engine        "Does this data match its description?"
                           (Python — runs on Parquet files)
```

This fits the project's design principles directly. Description and verification are decoupled, and SHACL validates the description layer without conflating it with the data layer.

The practical motivation is authoring safety. Someone writing a new domain description needs to get dozens of structural details right: every Column needs a `columnName` and `physicalType`, every OrderingKey needs a `keyDirection` from a specific enum, every AggregatedColumn needs a `targetColumn` and `aggregationFunction`. Getting one wrong currently means a confusing Python traceback later. SHACL makes the feedback immediate and specific.

## What the shapes cover

There are 22 shapes covering every class in the vocabulary. Each shape encodes the structural expectations that `graph.py` relies on when querying the graph, plus additional well-formedness constraints that prevent common authoring mistakes.

### Core data model

**DatasetShape** requires a label and at least one column. Constrains `rowSemantics` to the `{EventRow, SnapshotRow, AggregateRow}` enum and `schemaStability` to `{FixedSchema, InferredSchema, VariableSchema}`. Allows multiple `entityKey` values for composite keys (e.g. Polymarket holders keyed by `condition_id` + `token`). At most one physical layout, partition scheme, and provenance.

**ColumnShape** requires exactly one `columnName` (string) and exactly one `physicalType` (must be an instance of `mnf:PhysicalType`). Optional `semanticType` (at most one), `nullable` (boolean if present), and `embeddedStructure` (validated as a nested shape).

**SemanticTypeShape** requires a label. Optional `requiredPhysicalType` (must be a PhysicalType instance), `valueRange` (validated nested — see below), `unit` (string), and `hasAllowedValues` (validated nested).

### Nested structures

Several vocabulary patterns use blank nodes for inline structures. The shapes validate these via `sh:node`, which checks the blank node's properties even when it has no explicit `rdf:type`.

**ValueRangeShape** requires at least one bound to be declared (via `sh:or` across `minInclusive`, `maxInclusive`, `minExclusive`, `maxExclusive`). Each bound is limited to at most one value. Bound values are deliberately not type-constrained because Turtle integer literals like `100000000` parse as `xsd:integer`, while decimal literals like `0.0` parse as `xsd:decimal` — both are valid.

**AllowedValuesShape** requires at least one `allowedValue` string.

**EmbeddedStructureShape** requires both `embeddedFormat` (must be a `DataEncodingFormat` instance) and `embeddedElementType` (string describing the inner type, e.g. `"array<string>"`).

**AggregatedColumnShape** requires `targetColumn`, at least one `aggregationSourceColumn`, and `aggregationFunction`. Optional `withinGroupOrdering` for order-dependent aggregations. This shape has no `sh:targetClass` because aggregated columns in the existing descriptions are inline blank nodes without explicit `rdf:type` — the shape is applied via `sh:node` on the `AggregationRelationship`.

### Physical layout

**PhysicalLayoutShape** requires exactly one `fileFormat` (must be a FileFormat instance). Optional row ordering (validated nested).

**RowOrderingShape** requires at least one ordering key.

**OrderingKeyShape** requires `keyColumn` (an IRI), `keyDirection` (must be `Ascending` or `Descending`), and `keyPrecedence` (integer). Optional `orderingSemantic` (must be an OrderingSemanticType instance).

### Partitioning

**PartitionSchemeShape** requires a `pathTemplate` string.

**CompositePartitionSchemeShape** (subclass of PartitionScheme) additionally requires at least one partition level.

**PartitionLevelShape** requires `levelPrecedence` (integer), `levelColumn` (string), and `levelGranularity` (must be a TemporalGranularity instance).

### Column groups

**ColumnGroupShape** requires `groupSemanticType` and at least two `groupMember` IRIs. A group with fewer than two members is structurally meaningless.

### Derivations and aggregations

**DerivationShape** requires `derivedColumn` and `derivationFunction`. The `sourceColumn` property is optional (not required) because injection-style derivations — such as a fetcher-injected `_fetched_at` timestamp — have no source column in the data.

**AggregationRelationshipShape** requires `sourceDataset`, `targetDataset`, at least one `groupByColumn`, and at least one `hasAggregatedColumn` (each validated via AggregatedColumnShape).

### Cross-dataset relationships

**ForeignKeyShape** requires `foreignKeyFrom` and `foreignKeyTo` (both column IRIs). Optional `referentialIntegrity` constrained to `{StrictIntegrity, EventualIntegrity, PartialIntegrity}`.

**SameEntityShape** requires a label and at least two `identifyingColumn` IRIs (the whole point is linking columns across datasets).

### Provenance and deficiencies

**ProvenanceShape** requires at least one of `source` (URI) or `sourceDescription` (string), via `sh:or`.

**TransformationShape** requires both `transformationType` and `transformationDescription` (both strings).

**KnownDeficiencyShape** requires `deficiencyDescription` (string) and `severity` (constrained to `{Minor, Moderate, Severe}`). Optional `impact` string.

### Verification attestations

**VerificationAttestationShape** requires `verificationResult` (constrained to `{Pass, Fail, Partial, Error}`) and `verificationTime` (xsd:dateTime). This validates attestations produced by the engine and written back to the graph.

## What the shapes don't cover

Some structural expectations are conditional — they depend on the value of another property. The main case: datasets with `rowSemantics` of `SnapshotRow` should declare `entityKey` and `snapshotTimestamp`. Encoding this in SHACL would require `sh:sparql` (a SPARQL-based constraint), which is a step up in complexity. The shapes document this expectation in a comment instead.

The shapes also don't validate:

- **Domain-specific semantics.** Whether a semantic type's value range makes physical sense, whether derivation functions are implemented, or whether column names match across foreign key relationships — these are domain concerns, not structural ones.
- **Data-level constraints.** Whether actual data values fall within declared ranges, whether rows are correctly ordered, or whether aggregations are consistent. That's the engine's job.
- **Vocabulary-level validity.** The shapes validate *descriptions against the vocabulary*, not the vocabulary itself. They assume `mnf_core.ttl` is correct.

## SHACL features used

The shapes use a small, well-documented subset of SHACL:

| Feature | Purpose | Example in shapes |
|---------|---------|-------------------|
| `sh:property` | Declare expected properties on a class | Every shape |
| `sh:minCount` / `sh:maxCount` | Cardinality constraints | Column must have exactly one columnName |
| `sh:datatype` | Literal type checking | columnName must be xsd:string |
| `sh:class` | Instance-of checking | physicalType must be a PhysicalType |
| `sh:in` | Enumeration constraint | keyDirection must be Ascending or Descending |
| `sh:node` | Nested shape validation | valueRange blank nodes validated inline |
| `sh:nodeKind` | IRI vs literal vs blank node | hasColumn values must be IRIs |
| `sh:or` | Disjunction | ValueRange needs at least one bound; Provenance needs source or description |
| `sh:message` | Human-readable error messages | Attached to most constraints |

No SPARQL-based constraints (`sh:sparql`), no property paths beyond simple predicates, no advanced features like `sh:qualifiedValueShape` or `sh:closed`. Anyone who can read Turtle can read these shapes.

## Running validation

### With pyshacl (Python)

```python
from pyshacl import validate
from rdflib import Graph

# Load the data graph: vocabulary + description(s)
data = Graph()
data.parse("vocabularies/mnf_core.ttl")
data.parse("descriptions/ais_description.ttl")

# Load the shapes graph
shapes = Graph()
shapes.parse("vocabularies/mnf_shapes.ttl")

conforms, report_graph, report_text = validate(data, shacl_graph=shapes)
if not conforms:
    print(report_text)
```

### Validating all descriptions at once

```python
data = Graph()
data.parse("vocabularies/mnf_core.ttl")
data.parse("descriptions/ais_description.ttl")
data.parse("descriptions/polymarket_description.ttl")
data.parse("descriptions/foursquare_description.ttl")

shapes = Graph()
shapes.parse("vocabularies/mnf_shapes.ttl")

conforms, _, report_text = validate(data, shacl_graph=shapes)
```

### What violation reports look like

A missing `columnName` on a Column would produce:

```
Constraint Violation in MinCountConstraintComponent:
    Severity: sh:Violation
    Source Shape: [ sh:message "Column must have exactly one columnName (string)." ; ... ]
    Focus Node: ais:bc_mmsi
    Result Path: mnf:columnName
    Message: Column must have exactly one columnName (string).
```

The report identifies the exact node, the missing property, and includes the human-readable message from the shape.

## Design decisions

**Shapes live alongside the vocabulary, not the descriptions.** `mnf_shapes.ttl` is in `vocabularies/` because it defines the structural contract of the vocabulary itself. It doesn't belong with any particular domain description.

**`entityKey` allows multiple values.** The initial shape constrained this to `maxCount 1`, but the Polymarket holders dataset has a composite entity key (`condition_id` + `token`). The shape was relaxed to allow multiple values, matching the vocabulary's design intent.

**`sourceColumn` on Derivation is optional.** The Polymarket description has injection-style derivations where a column is added by external tooling (e.g. the fetcher injects `_fetched_at`), with no source column in the data. Requiring `sourceColumn` would force these legitimate derivations to be described differently.

**Value range bounds are not type-constrained.** The vocabulary declares `rdfs:range xsd:decimal` for bound properties, but Turtle integer literals (`100000000`) parse as `xsd:integer`, not `xsd:decimal`. Constraining the shapes to `sh:datatype xsd:decimal` would reject values that are semantically correct. The shapes validate structure (at most one of each bound) without imposing a specific numeric type.

**Conditional expectations are documented, not enforced.** "Snapshot datasets should have `entityKey` and `snapshotTimestamp`" is noted in a comment on DatasetShape. Encoding this as a SHACL constraint would require `sh:sparql`, a significant complexity increase for a single rule. If more conditional rules accumulate, upgrading to `sh:sparql` would be warranted.

## Validation results against existing descriptions

When run against all three domain descriptions:

| Description | Result | Notes |
|------------|--------|-------|
| AIS | Pass | All 1,231 triples conform |
| Foursquare | Pass | All 935 triples conform |
| Polymarket | 3 violations | `pm:Tags`, `pm:Series`, `pm:Sports` — reference datasets with columns listed in comments but not formalized as `mnf:Column` instances |

The three Polymarket violations are genuine: these datasets are intentionally brief stubs. The shapes correctly flag them as structurally incomplete. Formalizing their columns would resolve the violations.
