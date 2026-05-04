# Manifest Vocabulary Evolution: Lessons from Polymarket

*2026-03-04 (1 of 2)*

How modelling a prediction-market data store surfaced gaps in the original Manifest vocabulary, and the extensions that resolved them.

## Background

Manifest was initially designed around a single domain: NOAA AIS maritime data. AIS data has clean properties that made it a natural starting point — stable schemas, clear temporal ordering, well-defined aggregation relationships, and a single partition dimension (daily). The vocabulary that emerged was sufficient for that domain.

To test whether Manifest generalises, we modelled a fundamentally different domain: [Polymarket](https://polymarket.com) prediction-market data collected by a custom fetcher. This data has:

- **Snapshot semantics** (the same market polled repeatedly, not distinct events)
- **Schemas inferred from JSON** by Polars, not declared upfront
- **Structured data encoded as strings** (JSON arrays in Varchar columns)
- **Two-level Hive partitioning** (date + hour)
- **Cross-dataset referential relationships** (markets, trades, holders linked by condition IDs)
- **Variable-type columns** (a "price" column that's sometimes a float, sometimes an error object)

The exercise surfaced 10 vocabulary gaps. Seven required new vocabulary terms; three were adequately handled by existing mechanisms.

## The 10 Gaps

### Gap 1: Snapshot Semantics

**Problem.** AIS data is event-like: each row is a distinct position broadcast. Polymarket's market snapshots repeat the same entity (identified by market ID) across every hourly file. Manifest had no way to declare "this column is the entity key and rows are temporal snapshots."

Without this, a consumer has no machine-readable signal that the dataset needs deduplication by entity key, or that grouping by market ID across time is the expected access pattern.

**Resolution.** Added `mnf:entityKey` — a property on `mnf:Dataset` pointing to the column(s) that identify the repeated entity.

```turtle
# Before: only a comment
pm:MarketSnapshots a mnf:Dataset ;
    rdfs:comment "...keyed by market ID..." .

# After: formal declaration
pm:MarketSnapshots a mnf:Dataset ;
    mnf:entityKey pm:mkt_id .
```

Composite entity keys (e.g. holders keyed by condition_id + token) use multiple `mnf:entityKey` properties.

**Vocabulary addition:** `mnf:entityKey` (Section 12 of `mnf_core.ttl`)

---

### Gap 2: Enum / Categorical Constraints

**Problem.** `mnf:valueRange` only supports numeric bounds (`minInclusive`, `maxInclusive`, etc.). Polymarket has columns constrained to string enumerations — trade side must be `"BUY"` or `"SELL"`, market category must be one of a known set. There was no way to express this.

**Resolution.** Added `mnf:AllowedValues` class and `mnf:allowedValue` property, linked from a semantic type via `mnf:hasAllowedValues`.

```turtle
pm:TradeSide a mnf:SemanticType ;
    mnf:requiredPhysicalType mnf:Varchar ;
    mnf:hasAllowedValues [
        a mnf:AllowedValues ;
        mnf:allowedValue "BUY" ;
        mnf:allowedValue "SELL"
    ] .
```

For open-ended categoricals (like market category), the allowed values set can include a comment noting it's non-exhaustive.

**Vocabulary addition:** `mnf:AllowedValues`, `mnf:hasAllowedValues`, `mnf:allowedValue` (Section 11)

---

### Gap 3: Structured Data in String Columns

**Problem.** Several Polymarket columns store JSON arrays as Varchar strings — outcomes (`["Yes","No"]`), orderbook bids/asks (`[{"price":"0.50","size":"100"},...]`), nested holder objects. Manifest could declare the physical type as Varchar but had no way to describe what was *inside* the string.

This matters because a consumer needs to know these aren't just text — they require JSON parsing, and the inner structure has its own schema.

**Resolution.** Added `mnf:embeddedStructure` property on columns, pointing to an `mnf:EmbeddedStructure` that declares the encoding format and inner element type.

```turtle
pm:ob_bids a mnf:Column ;
    mnf:physicalType mnf:Varchar ;
    mnf:semanticType pm:JSONArray ;
    mnf:embeddedStructure [
        a mnf:EmbeddedStructure ;
        mnf:embeddedFormat "json" ;
        mnf:embeddedElementType "array<{price: string, size: string}>"
    ] .
```

This also addresses **Gap 8** (nested/repeated fields) — the `embeddedElementType` can describe arbitrary nesting.

**Vocabulary addition:** `mnf:embeddedStructure`, `mnf:EmbeddedStructure`, `mnf:embeddedFormat`, `mnf:embeddedElementType` (Section 13)

---

### Gap 4: Multi-Level Partitioning

**Problem.** AIS data uses single-dimension partitioning: one file per date. Polymarket uses two-level Hive partitioning: `dt=YYYY-MM-DD/hour=HH`. Manifest's `PartitionScheme` had a single `partitionColumn` and `partitionGranularity` — no way to express the second level.

The `pathTemplate` property captured the structure textually, but there was no formal way to declare two independent partition dimensions.

**Resolution.** Added `mnf:CompositePartitionScheme` (subclass of `mnf:PartitionScheme`) with `mnf:PartitionLevel` nodes, each having a `levelPrecedence`, `levelColumn`, and `levelGranularity`.

```turtle
pm:hourly_hive_partition a mnf:CompositePartitionScheme ;
    mnf:pathTemplate "data/parquet/{stream}/dt={date}/hour={hour}.parquet" ;
    mnf:hasPartitionLevel [
        a mnf:PartitionLevel ;
        mnf:levelPrecedence 1 ;
        mnf:levelColumn "dt" ;
        mnf:levelGranularity "daily"
    ] ;
    mnf:hasPartitionLevel [
        a mnf:PartitionLevel ;
        mnf:levelPrecedence 2 ;
        mnf:levelColumn "hour" ;
        mnf:levelGranularity "hourly"
    ] .
```

Because `CompositePartitionScheme` is a subclass of `PartitionScheme`, existing `mnf:partitionedBy` links work unchanged.

**Vocabulary addition:** `mnf:CompositePartitionScheme`, `mnf:PartitionLevel`, `mnf:hasPartitionLevel`, `mnf:levelPrecedence`, `mnf:levelColumn`, `mnf:levelGranularity` (Section 14)

---

### Gap 5: Foreign Key / Referential Relationships

**Problem.** Polymarket's datasets are linked by shared identifiers: trades reference markets via `conditionId`, holders reference markets the same way, orderbooks reference markets via `market`. Manifest had `mnf:companionOf` for co-partitioned datasets, but no concept for general referential links between datasets that are partitioned independently.

**Resolution.** Added `mnf:ForeignKey` class with `mnf:foreignKeyFrom` and `mnf:foreignKeyTo` properties, plus `mnf:referentialIntegrity` to declare the expected integrity level.

```turtle
pm:fk_trades_to_markets a mnf:ForeignKey ;
    mnf:foreignKeyFrom pm:tr_condition_id ;
    mnf:foreignKeyTo pm:mkt_condition_id ;
    mnf:referentialIntegrity "partial" ;
    rdfs:comment """Partial: some trades reference resolved markets
        no longer in active snapshots.""" .
```

The `referentialIntegrity` property acknowledges real-world data: strict (every FK resolves), eventual (may temporarily be missing), or partial (some values never resolve).

**Vocabulary addition:** `mnf:ForeignKey`, `mnf:foreignKeyFrom`, `mnf:foreignKeyTo`, `mnf:referentialIntegrity` (Section 15)

---

### Gap 6: Variable-Type Columns

**Problem.** The `price` column in `clob/prices` can be a float (the actual price) or an error object string (when the API returns an error). Since Polars infers types per batch, the same column might be Float64 in one hourly file and Varchar in another.

**Resolution.** No new vocabulary was needed. The existing `mnf:acceptablePhysicalType` partially covers this (allowing multiple valid types for a semantic type), and the specific data quality issue is documented via `mnf:KnownDeficiency`. This gap is more of a data quality problem than a vocabulary problem — Manifest correctly describes the *intended* type, and the deficiency documents the reality.

---

### Gap 7: Non-Semantic Row Ordering

**Problem.** AIS data has meaningful row ordering (MMSI clustering for index efficiency, timestamp ordering within each cluster). Polymarket's files have no meaningful ordering — rows arrive in poll order.

**Resolution.** No new vocabulary was needed. Manifest already handles this gracefully: simply omit `mnf:hasRowOrdering` from the `PhysicalLayout`. The absence of an ordering declaration correctly communicates that rows have no guaranteed or meaningful order.

---

### Gap 8: Nested / Repeated Fields

**Problem.** Holders contain arrays of holder objects; events contain nested market arrays. Manifest couldn't describe column-level nesting beyond list types.

**Resolution.** Addressed by the same `mnf:embeddedStructure` mechanism from Gap 3. The `embeddedElementType` property can describe arbitrary nesting:

```turtle
pm:hld_holders a mnf:Column ;
    mnf:physicalType mnf:Varchar ;
    mnf:embeddedStructure [
        a mnf:EmbeddedStructure ;
        mnf:embeddedFormat "json" ;
        mnf:embeddedElementType "array<{proxyWallet: string, name: string, amount: float, ...}>"
    ] .
```

---

### Gap 9: Schema Stability

**Problem.** AIS data has a stable, declared schema. Polymarket's Parquet schemas are entirely Polars-inferred — `schema.py` definitions exist in the fetcher but are *not applied* during compaction. Columns may appear or disappear depending on what the API returns in each batch. Manifest assumed schemas were fixed.

**Resolution.** Added `mnf:schemaStability` property with three levels: `FixedSchema`, `InferredSchema`, and `VariableSchema`.

```turtle
pm:MarketSnapshots a mnf:Dataset ;
    mnf:schemaStability mnf:InferredSchema .
```

This gives consumers a machine-readable signal about how much to trust the declared column list. `InferredSchema` means "these columns are typical but may vary between files."

**Vocabulary addition:** `mnf:schemaStability`, `mnf:SchemaStabilityLevel`, `mnf:FixedSchema`, `mnf:InferredSchema`, `mnf:VariableSchema` (Section 16)

---

### Gap 10: Cross-Dataset Entity Identity

**Problem.** The condition ID in `gamma/markets` is the same logical entity referenced by `conditionId` in trades, `condition_id` in holders, and `market` in orderbooks. These columns live in different datasets with different names. Manifest had no way to declare "these columns across datasets identify the same entity." This is different from `companionOf` (co-partitioning) and `ForeignKey` (directional reference) — it's a symmetric identity assertion.

**Resolution.** Added `mnf:SameEntity` class with `mnf:identifyingColumn` linking all the participating columns.

```turtle
pm:same_entity_condition_id a mnf:SameEntity ;
    rdfs:label "Condition ID identifies the same market across datasets" ;
    mnf:identifyingColumn pm:mkt_condition_id ;
    mnf:identifyingColumn pm:tr_condition_id ;
    mnf:identifyingColumn pm:hld_condition_id ;
    mnf:identifyingColumn pm:ob_market .
```

This is a symmetric, non-directional assertion — all four columns refer to the same entity. A query planner or data integration tool can use this to know that joining on any pair is valid.

**Vocabulary addition:** `mnf:SameEntity`, `mnf:identifyingColumn` (Section 17)

---

## Summary of Vocabulary Changes

| Section | Gap | New Terms | Type |
|---------|-----|-----------|------|
| 11 | Enum constraints | `AllowedValues`, `hasAllowedValues`, `allowedValue` | Class + properties |
| 12 | Snapshot semantics | `entityKey` | Property |
| 13 | Embedded structure | `embeddedStructure`, `EmbeddedStructure`, `embeddedFormat`, `embeddedElementType` | Class + properties |
| 14 | Multi-level partitioning | `CompositePartitionScheme`, `PartitionLevel`, `hasPartitionLevel`, `levelPrecedence`, `levelColumn`, `levelGranularity` | Classes + properties |
| 15 | Foreign keys | `ForeignKey`, `foreignKeyFrom`, `foreignKeyTo`, `referentialIntegrity` | Class + properties |
| 16 | Schema stability | `schemaStability`, `SchemaStabilityLevel`, `FixedSchema`, `InferredSchema`, `VariableSchema` | Class + property + instances |
| 17 | Entity identity | `SameEntity`, `identifyingColumn` | Class + property |

**Backward compatibility.** All additions are purely additive. Existing AIS descriptions require no changes. The `CompositePartitionScheme` subclasses `PartitionScheme`, so `partitionedBy` links work without modification.

## Reflections

The original README noted: *"The core vocabulary should not need to change for new domains. If it does, that's a signal that something belongs in the core that was missed."* The Polymarket exercise proved this exactly right — every gap we found was genuinely domain-independent:

- Entity keys apply to any snapshot/polling system (IoT sensors, API crawlers, price feeds)
- Enum constraints apply to any categorical data
- Embedded structure applies to any JSON-in-string column (common in data lakes)
- Multi-level partitioning is standard in Hive-style data stores
- Foreign keys are a universal relational concept
- Schema stability is relevant to any inferred-schema data pipeline
- Cross-dataset entity identity is fundamental to data integration

None of these are Polymarket-specific. The vocabulary was incomplete, not wrongly designed.

---

## Round 2: keystone + dw MySQL databases

Two MySQL databases — `keystone` (OpenStack identity service) and `dw` (MIT institutional data warehouse), sourced from the BEAVER benchmark dumps — brought a different shape than the existing Parquet-shaped descriptions: live RDBMS storage, anonymisation as a first-class fact, soft and polymorphic FKs, sentinel-string-as-NULL, parallel/duplicate tables, and roughly 100 datasets in a single description (vs 2–9 in the AIS / Polymarket / Foursquare descriptions). The description was written first using workarounds, with 29 inline `[BVT-K-GAP-N]` tags pointing at limits in the core vocabulary. This first round of evolution then addressed five of them — chosen for SQL-correctness impact and additive simplicity.

### GAP-A — File formats beyond Parquet/CSV/ORC

The original `mnf:FileFormat` enumerated only `Parquet`, `CSV`, and `ORC`. The keystone and dw datasets are accessed via a live MySQL connection (`mysql://{db}/{table}`), with no file at all. Other domains in the same release also had JSON, JSONL, and plain-text artefacts.

**Resolution.** Extended `mnf:FileFormat` with a set of additive individuals covering both text-based files and live-RDBMS tables:

```turtle
mnf:JSON      a mnf:FileFormat .  # one JSON value per file
mnf:JSONL     a mnf:FileFormat .  # newline-delimited
mnf:NDJSON    a mnf:FileFormat .  # synonym for JSONL
mnf:PlainText a mnf:FileFormat .
mnf:Markdown  a mnf:FileFormat .
mnf:MySQLTable      a mnf:FileFormat .
mnf:PostgreSQLTable a mnf:FileFormat .
mnf:SQLiteTable     a mnf:FileFormat .
```

The keystone+dw description's `bvtk:MySQLTable` placeholder was deleted in favour of `mnf:MySQLTable`. The same RDBMS set works for any other live-database description (Postgres warehouses, SQLite analytical stores).

### GAP-1/2 — Row-count snapshots and empty-table markers

The investigations behind the keystone+dw description carried specific row counts ("user has 944 rows", "fclt_rooms_hist has 5,042,544 rows") that matter for query planning, but the only place to put them was inside `rdfs:comment`. Empty-but-schema-present tables (`federated_user`, the four federation tables) likewise had only a `KnownDeficiency` saying "empty in this dump" — no first-class flag.

**Resolution.** Added `mnf:rowCountSnapshot` (xsd:integer) on `Dataset`. It's a snapshot — not a guaranteed invariant — and may drift as the upstream changes; the property is optional and may be omitted for streaming or unbounded datasets where a count is meaningless. Empty tables collapse to `mnf:rowCountSnapshot 0`, eliminating the need for a separate empty marker.

```turtle
ks:user a mnf:Dataset ;
    mnf:rowCountSnapshot 944 .

ks:federated_user a mnf:Dataset ;
    mnf:rowCountSnapshot 0 ;
    mnf:hasKnownDeficiency ks:deficiency_empty_federation .
```

All keystone and rich-described dw datasets are annotated; the schema-stub dw tables carry it where the count is known (zero for the empty tables). SHACL validates the property as `xsd:integer >= 0` with at most one occurrence.

### GAP-4 — Soft (un-declared) foreign keys

`mnf:ForeignKey` couldn't distinguish FKs declared and enforced in upstream DDL from FKs that exist by convention but aren't enforced. This matters: for soft FKs the consumer needs to know whether to trust the join. The keystone schema mixes declared and soft (e.g. `assignment.role_id` is soft, every value happens to resolve), and the dw schema has *no* declared FKs at all — every relationship is soft. Several soft FKs have empirically partial integrity (one orphaned `credential.user_id`, eleven orphaned `trust.project_id`, etc.).

**Resolution.** Added `mnf:declared` (xsd:boolean) on `ForeignKey`. Absence of the property is treated as `true` — the existing Parquet-shaped descriptions don't need updating. Set to `false` for soft FKs:

```turtle
ks:fk_credential_user a mnf:ForeignKey ;
    mnf:declared false ;
    mnf:foreignKeyFrom ks:credential_user_id ;
    mnf:foreignKeyTo ks:user_id ;
    mnf:referentialIntegrity mnf:PartialIntegrity .
```

The `mnf:referentialIntegrity` property already captured the *empirical* situation; `mnf:declared` captures the *upstream contract*. They're orthogonal.

### GAP-22 — Disjoint identifier namespaces

The single most consequential gap. `dw` has two independent MIT_ID anonymisations: Namespace A in `employee_directory`, `subject_offered.RESPONSIBLE_FACULTY_MIT_ID`, `moira_list_detail.MOIRA_LIST_MEMBER_MIT_ID` etc., and Namespace B in `se_person`, `hr_faculty_roster`, `warehouse_users`. Same logical person, different anonymised IDs in each upstream system. Joining across the two on MIT_ID returns *zero rows* — silent and convincing.

A SQL author looking only at the schema and a `mnf:SameEntity` declaration can't tell. The previous workaround was to declare two separate semantic types (`dw:MITID_NamespaceA`, `dw:MITID_NamespaceB`) with prose comments warning against cross-joins. Better than nothing, but it relied on the consumer reading and remembering the comment.

**Resolution.** Added `mnf:identifierNamespace` (xsd:string) on `SemanticType`:

```turtle
dw:MITID_NamespaceA a mnf:SemanticType ;
    mnf:identifierNamespace "dw/mit_id/A" .

dw:MITID_NamespaceB a mnf:SemanticType ;
    mnf:identifierNamespace "dw/mit_id/B" .
```

Now the disjointness is machine-detectable: a SPARQL query for "which semantic types share a namespace?" answers correctly, and a consumer that includes the description can be told to refuse equality joins between columns whose semantic types have differing namespaces.

The same machinery handles any case where two columns look mergeable but aren't — separate anonymisations of the same logical population, identifiers minted by different generators that happen to share a shape, etc.

### GAP-25 — Case convention on join keys

The same Kerberos username appears uppercase in `dw.person_auth_area.USER_NAME`, lowercase in `dw.roles_fin_pa.USERNAME` and `dw.moira_list_detail.MOIRA_LIST_MEMBER`, and proper-case-with-uppercase-shadow in `dw.employee_directory.KRB_NAME` / `KRB_NAME_UPPERCASE`. A direct equality join silently returns partial results.

`mnf:SameEntity` was already telling the consumer "these columns identify the same person", but not "you'll need `UPPER()` on at least one side."

**Resolution.** Added `mnf:caseConvention` on `Column` with three named individuals — `mnf:UpperCase`, `mnf:LowerCase`, `mnf:MixedCase`. The KRB_NAME columns are now annotated:

```turtle
dw:paa_user_name a mnf:Column ;
    mnf:columnName "USER_NAME" ;
    mnf:caseConvention mnf:UpperCase .

dw:rfp_username a mnf:Column ;
    mnf:columnName "USERNAME" ;
    mnf:caseConvention mnf:LowerCase .
```

A consumer can detect the conflict and apply normalisation; SHACL validates the value is one of the three individuals.

### What's queued

The remaining high-priority gaps surfaced by this modelling round:

| Gap | Edit | Why deferred |
|-----|------|--------------|
| GAP-19 | `mnf:Database` class with `hasDataset` and cluster taxonomy | Architectural; reshapes how the DW catalogue is modelled. |
| GAP-L | `mnf_common.ttl` with shared semantic types (`UUIDHex32`, `Sha256Hex`, `MySQLBoolean`, `JSONInString`, `ISOTimestamp`, `USDAmount`) | Pure refactor; touches every existing description. |
| GAP-3 | `mnf:PolymorphicForeignKey` with discriminator + variants | Larger structural change. |
| GAP-5 | `mnf:sentinelValue` for in-band absence markers like `'<<null>>'` | Useful but lower frequency than 22/25. |

### Summary of round-1 changes

| Gap | New Terms | Backward-compat |
|-----|-----------|----|
| GAP-A   | `JSON`, `JSONL`, `NDJSON`, `PlainText`, `Markdown`, `MySQLTable`, `PostgreSQLTable`, `SQLiteTable` (FileFormat individuals) | Yes (additive) |
| GAP-1/2 | `rowCountSnapshot` (property on Dataset) | Yes (additive, optional) |
| GAP-4   | `declared` (boolean property on ForeignKey) | Yes (default true if absent) |
| GAP-22  | `identifierNamespace` (property on SemanticType) | Yes (additive, optional) |
| GAP-25  | `caseConvention` property + `UpperCase` / `LowerCase` / `MixedCase` individuals | Yes (additive, optional) |

All five additions are purely additive. No existing description requires updating; new descriptions can adopt them incrementally.
