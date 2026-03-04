# AIS Dataset Description

*Generated from `ais_description.ttl` — do not edit.*

## Datasets

| Dataset | Row Semantics | Schema | Partitioning | Format |
|---------|---------------|--------|--------------|--------|
| AIS Daily Broadcast Positions | sdl:EventRow | sdl:FixedSchema | daily | Parquet |
| AIS Daily Vessel Index | sdl:AggregateRow | sdl:FixedSchema | daily | Parquet |

---

## AIS Daily Broadcast Positions

**URI:** `ais:DailyBroadcasts`
  
**Row semantics:** sdl:EventRow
  
**Schema:** sdl:FixedSchema
  
**Path template:** `broadcasts/{year}/ais-{date}.parquet`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `base_date_time` | sdl:Varchar | ais:AISRawTimestampString | yes |
| `call_sign` | sdl:Varchar | ais:CallSign | yes |
| `cargo` | sdl:Integer | ais:CargoTypeCode | yes |
| `cog` | sdl:Double | ais:CourseOverGround | yes |
| `date` | sdl:Date | ais:PartitionDate | yes |
| `draft` | sdl:Double | ais:VesselDraft | yes |
| `geometry` | sdl:Blob | ais:WKBPoint | yes |
| `h3_res15` | sdl:UBigInt | ais:H3Resolution15 | yes |
| `heading` | sdl:Double | ais:TrueHeading | yes |
| `imo` | sdl:Varchar | ais:IMONumber | yes |
| `latitude` | sdl:Double | ais:WGS84Latitude | yes |
| `length` | sdl:Double | ais:VesselLength | yes |
| `longitude` | sdl:Double | ais:WGS84Longitude | yes |
| `mmsi` | sdl:Integer | ais:MMSI | yes |
| `sog` | sdl:Double | ais:SpeedOverGround | yes |
| `status` | sdl:Integer | ais:NavigationalStatus | yes |
| `timestamp` | sdl:TimestampTZ | ais:AISTimestamp | yes |
| `transceiver` | sdl:Varchar | ais:TransceiverClass | yes |
| `vessel_name` | sdl:Varchar | ais:VesselName | yes |
| `vessel_type` | sdl:Integer | ais:VesselTypeCode | yes |
| `width` | sdl:Double | ais:VesselWidth | yes |

### Ordering

| # | Column | Direction | Semantic |
|---|--------|-----------|----------|
| 1 | `mmsi` | ascending | sdl:ClusteringForIndex |
| 2 | `timestamp` | ascending | sdl:MeaningfulSequence |

### Derivations

| Derived Column | Source Columns | Function | Properties |
|----------------|----------------|----------|------------|
| `timestamp` | `base_date_time` | ais:ParseTimestamp | sdl:Deterministic, sdl:Invertible |
| `geometry` | `latitude`, `longitude` | ais:PointFromWGS84 | sdl:Deterministic, sdl:Invertible |
| `h3_res15` | `latitude`, `longitude` | ais:H3IndexFromWGS84Res15 | sdl:Deterministic, sdl:Lossy |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | Temporal gaps exist within vessel trajectories due to NOAA's undocumented downsampling. Trajectory-based analyses (distance, speed) may be inaccurate for affected segments. |
| minor | Static vessel data is denormalized into position rows. A vessel's name/IMO/dimensions may appear differently across rows due to broadcast timing and the merge process. |
| moderate | MMSI does not reliably identify a single vessel. Known issues: MMSI reuse between vessels, multiple vessels sharing an MMSI simultaneously, default/test MMSIs, and spoofing. |

---

## AIS Daily Vessel Index

**URI:** `ais:DailyIndex`
  
**Row semantics:** sdl:AggregateRow
  
**Schema:** sdl:FixedSchema
  
**Path template:** `broadcasts/{year}/ais-{date}.parquet`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `call_signs` | sdl:VarcharList |  | yes |
| `cargos` | sdl:IntegerList |  | yes |
| `centroid_lat` | sdl:Double | ais:WGS84Latitude | yes |
| `centroid_lon` | sdl:Double | ais:WGS84Longitude | yes |
| `date` | sdl:Date | ais:PartitionDate | yes |
| `distance_m` | sdl:Double | ais:DistanceMetres | yes |
| `drafts` | sdl:DoubleList |  | yes |
| `duration_s` | sdl:Double | ais:DurationSeconds | yes |
| `first_timestamp` | sdl:TimestampTZ | ais:AISTimestamp | yes |
| `h3_cell_count` | sdl:BigInt |  | yes |
| `imos` | sdl:VarcharList |  | yes |
| `last_timestamp` | sdl:TimestampTZ | ais:AISTimestamp | yes |
| `lengths` | sdl:DoubleList |  | yes |
| `max_inter_msg_speed_ms` | sdl:Double | ais:SpeedMetresPerSecond | yes |
| `max_lat` | sdl:Double | ais:WGS84Latitude | yes |
| `max_lon` | sdl:Double | ais:WGS84Longitude | yes |
| `message_count` | sdl:BigInt | ais:MessageCount | yes |
| `min_lat` | sdl:Double | ais:WGS84Latitude | yes |
| `min_lon` | sdl:Double | ais:WGS84Longitude | yes |
| `mmsi` | sdl:Integer | ais:MMSI | yes |
| `sog_max` | sdl:Double | ais:SpeedOverGround | yes |
| `sog_mean` | sdl:Double | ais:SpeedOverGround | yes |
| `sog_min` | sdl:Double | ais:SpeedOverGround | yes |
| `status_codes` | sdl:IntegerList |  | yes |
| `transceiver_classes` | sdl:VarcharList |  | yes |
| `vessel_names` | sdl:VarcharList |  | yes |
| `vessel_types` | sdl:IntegerList |  | yes |
| `widths` | sdl:DoubleList |  | yes |

## Cross-Dataset Relationships

### Aggregation

**ais:DailyBroadcasts** → **ais:DailyIndex** (grouped by `mmsi`)

| Target Column | Source Column(s) | Function |
|---------------|------------------|----------|
| `message_count` | `mmsi` | COUNT |
| `first_timestamp` | `timestamp` | MIN |
| `last_timestamp` | `timestamp` | MAX |
| `vessel_names` | `vessel_name` | LIST of DISTINCT values |
| `imos` | `imo` | LIST of DISTINCT values |
| `call_signs` | `call_sign` | LIST of DISTINCT values |
| `vessel_types` | `vessel_type` | LIST of DISTINCT values |
| `cargos` | `cargo` | LIST of DISTINCT values |
| `lengths` | `length` | LIST of DISTINCT values |
| `widths` | `width` | LIST of DISTINCT values |
| `drafts` | `draft` | LIST of DISTINCT values |
| `transceiver_classes` | `transceiver` | LIST of DISTINCT values |
| `status_codes` | `status` | LIST of DISTINCT values |
| `min_lat` | `latitude` | MIN |
| `max_lat` | `latitude` | MAX |
| `min_lon` | `longitude` | MIN |
| `max_lon` | `longitude` | MAX |
| `centroid_lat` | `latitude` | MEAN / AVG |
| `centroid_lon` | `longitude` | MEAN / AVG |
| `sog_min` | `sog` | MIN |
| `sog_max` | `sog` | MAX |
| `sog_mean` | `sog` | MEAN / AVG |
| `h3_cell_count` | `h3_res15` | COUNT DISTINCT |
| `duration_s` | `timestamp` | Duration between min and max timestamps |
| `distance_m` | `latitude`, `longitude` | Haversine distance from first to last position |
| `max_inter_msg_speed_ms` | `latitude`, `longitude`, `timestamp` | Maximum implied speed between consecutive messages |

---

## Notes for AI Agents

This section explains SDL concepts used in the tables above, to help you write correct queries against this data.

**Row semantics** determine how to interpret rows:

- **Event rows** (`sdl:EventRow`) — each row is an independent event or observation. No deduplication needed.
- **Aggregate rows** (`sdl:AggregateRow`) — each row summarises a group of source rows. Check the Aggregation table for how columns relate to the source dataset.

**Schema stability** affects query robustness:

- **Fixed** (`sdl:FixedSchema`) — all files have identical columns and types. Query without defensive casting.

**Row ordering** — files with declared ordering are physically sorted by the listed keys. DuckDB can exploit this for merge joins and ordered aggregations. The semantic column distinguishes keys that carry meaning (e.g. a time series) from keys used purely for index clustering.

**Aggregations** — the target dataset's columns are computed from the source dataset. Don't recompute what already exists in the aggregate table. The Function column shows exactly how each target column is derived.

**Known deficiencies** — documented data quality issues that may affect query correctness. Read these before writing queries that involve aggregation, deduplication, or cross-file joins.

**Notation** — `sdl:` prefixed terms are SDL vocabulary concepts. Domain-specific prefixes (e.g. `ais:`, `pm:`) identify semantic types and domain entities. Physical types like `sdl:Varchar`, `sdl:Double`, `sdl:Integer` map directly to DuckDB/Parquet types.

