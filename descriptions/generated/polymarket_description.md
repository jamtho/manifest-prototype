# Polymarket Dataset Description

*Generated from `polymarket_description.ttl` — do not edit.*

## Datasets

| Dataset | Row Semantics | Schema | Partitioning | Format |
|---------|---------------|--------|--------------|--------|
| Gamma Market Snapshots | sdl:SnapshotRow | sdl:InferredSchema | — | Parquet |
| Gamma Event Snapshots | sdl:SnapshotRow | sdl:InferredSchema | — | Parquet |
| CLOB Price Snapshots | sdl:SnapshotRow | sdl:InferredSchema | — | Parquet |
| CLOB Orderbook Snapshots | sdl:SnapshotRow | sdl:InferredSchema | — | Parquet |
| Trade Events | sdl:EventRow | sdl:InferredSchema | — | Parquet |
| Token Holder Snapshots | sdl:SnapshotRow | sdl:InferredSchema | — | Parquet |
| Gamma Tags | — | — | — | Parquet |
| Gamma Series | — | — | — | Parquet |
| Gamma Sports | — | — | — | Parquet |

---

## Gamma Market Snapshots

**URI:** `pm:MarketSnapshots`
  
**Row semantics:** sdl:SnapshotRow
  
**Schema:** sdl:InferredSchema
  
**Path template:** `data/parquet/{stream}/dt={date}/hour={hour}.parquet`
  
**Entity key:** `id`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `_fetched_at` | sdl:Double | pm:FetchTimestamp | no |
| `_source` | sdl:Varchar | pm:DataSourceLabel | no |
| `active` | sdl:Varchar |  | yes |
| `bestAsk` | sdl:Double | pm:Probability | yes |
| `bestBid` | sdl:Double | pm:Probability | yes |
| `category` | sdl:Varchar | pm:MarketCategory | yes |
| `clobTokenIds` | sdl:Varchar | pm:JSONArray | yes |
| `closed` | sdl:Varchar |  | yes |
| `competitive` | sdl:Double | pm:CompetitivenessScore | yes |
| `conditionId` | sdl:Varchar | pm:ConditionId | yes |
| `createdAt` | sdl:Varchar | pm:ISOTimestamp | yes |
| `description` | sdl:Varchar |  | yes |
| `enableOrderBook` | sdl:Varchar |  | yes |
| `endDate` | sdl:Varchar | pm:ISOTimestamp | yes |
| `id` | sdl:Varchar | pm:MarketId | no |
| `image` | sdl:Varchar |  | yes |
| `lastTradePrice` | sdl:Double | pm:Probability | yes |
| `liquidity` | sdl:Varchar |  | yes |
| `liquidityNum` | sdl:Double | pm:USDAmount | yes |
| `negRisk` | sdl:Varchar |  | yes |
| `oneDayPriceChange` | sdl:Double | pm:PriceChange | yes |
| `oneWeekPriceChange` | sdl:Double | pm:PriceChange | yes |
| `outcomePrices` | sdl:Varchar | pm:JSONArray | yes |
| `outcomes` | sdl:Varchar | pm:JSONArray | yes |
| `question` | sdl:Varchar |  | yes |
| `rewardsMaxSpread` | sdl:Double |  | yes |
| `rewardsMinSize` | sdl:Double |  | yes |
| `slug` | sdl:Varchar | pm:Slug | yes |
| `spread` | sdl:Double | pm:PriceSpread | yes |
| `startDate` | sdl:Varchar | pm:ISOTimestamp | yes |
| `updatedAt` | sdl:Varchar | pm:ISOTimestamp | yes |
| `volume` | sdl:Varchar |  | yes |
| `volume1mo` | sdl:Double | pm:USDAmount | yes |
| `volume1wk` | sdl:Double | pm:USDAmount | yes |
| `volume1yr` | sdl:Double | pm:USDAmount | yes |
| `volume24hr` | sdl:Double | pm:USDAmount | yes |
| `volumeNum` | sdl:Double | pm:USDAmount | yes |

### Derivations

| Derived Column | Source Columns | Function | Properties |
|----------------|----------------|----------|------------|
| `_fetched_at` |  | pm:FetcherTimestampInjection | sdl:Deterministic |
| `_source` |  | pm:FetcherSourceInjection | sdl:Deterministic |
| `spread` | `bestAsk`, `bestBid` | pm:SpreadFromBidAsk | sdl:Deterministic, sdl:Invertible |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | Parquet schemas are inferred by Polars from JSON, not declared. The schema.py file in the fetcher defines type hints but they are NOT applied during compaction. Columns may appear or disappear depending on API response changes. Types may vary between hourly files if Polars infers differently from different data batches. Datasets declare sdl:schemaStability sdl:InferredSchema to signal this. |
| moderate | Snapshot datasets (markets, events, prices, holders) contain the same entity polled multiple times per hour. Within a single hourly file, the same market/event/token may appear multiple times with slightly different values. No deduplication is performed by the compactor. |
| minor | Several columns store structured data as JSON strings rather than native Parquet nested types: outcomes, outcomePrices, clobTokenIds (in markets), bids/asks (in books), holders (in holders), markets/tags (in events). This happens because the compactor does not parse these fields into structured columns. |

---

## Gamma Event Snapshots

**URI:** `pm:EventSnapshots`
  
**Row semantics:** sdl:SnapshotRow
  
**Schema:** sdl:InferredSchema
  
**Path template:** `data/parquet/{stream}/dt={date}/hour={hour}.parquet`
  
**Entity key:** `id`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `_fetched_at` | sdl:Double | pm:FetchTimestamp | no |
| `_source` | sdl:Varchar | pm:DataSourceLabel | no |
| `active` | sdl:Varchar |  | yes |
| `closed` | sdl:Varchar |  | yes |
| `commentCount` | sdl:Double |  | yes |
| `competitive` | sdl:Double | pm:CompetitivenessScore | yes |
| `description` | sdl:Varchar |  | yes |
| `endDate` | sdl:Varchar | pm:ISOTimestamp | yes |
| `id` | sdl:Varchar | pm:EventId | no |
| `liquidity` | sdl:Double | pm:USDAmount | yes |
| `markets` | sdl:Varchar |  | yes |
| `negRisk` | sdl:Varchar |  | yes |
| `openInterest` | sdl:Double |  | yes |
| `slug` | sdl:Varchar | pm:Slug | yes |
| `startDate` | sdl:Varchar | pm:ISOTimestamp | yes |
| `tags` | sdl:Varchar | pm:JSONArray | yes |
| `title` | sdl:Varchar |  | yes |
| `volume` | sdl:Double | pm:USDAmount | yes |
| `volume24hr` | sdl:Double | pm:USDAmount | yes |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | Parquet schemas are inferred by Polars from JSON, not declared. The schema.py file in the fetcher defines type hints but they are NOT applied during compaction. Columns may appear or disappear depending on API response changes. Types may vary between hourly files if Polars infers differently from different data batches. Datasets declare sdl:schemaStability sdl:InferredSchema to signal this. |
| moderate | Snapshot datasets (markets, events, prices, holders) contain the same entity polled multiple times per hour. Within a single hourly file, the same market/event/token may appear multiple times with slightly different values. No deduplication is performed by the compactor. |

---

## CLOB Price Snapshots

**URI:** `pm:PriceSnapshots`
  
**Row semantics:** sdl:SnapshotRow
  
**Schema:** sdl:InferredSchema
  
**Path template:** `data/parquet/{stream}/dt={date}/hour={hour}.parquet`
  
**Entity key:** `token_id`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `_fetched_at` | sdl:Double | pm:FetchTimestamp | no |
| `_source` | sdl:Varchar | pm:DataSourceLabel | no |
| `midpoint` | sdl:Varchar |  | yes |
| `price` | sdl:Varchar |  | yes |
| `token_id` | sdl:Varchar | pm:CLOBTokenId | no |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | Parquet schemas are inferred by Polars from JSON, not declared. The schema.py file in the fetcher defines type hints but they are NOT applied during compaction. Columns may appear or disappear depending on API response changes. Types may vary between hourly files if Polars infers differently from different data batches. Datasets declare sdl:schemaStability sdl:InferredSchema to signal this. |
| moderate | The 'price' column in clob/prices may contain either a float value (the actual price) or an error object string when the CLOB API returns an error for a specific token. Since the compactor uses ignore_errors=True, these error responses are silently mixed in with valid data. |

---

## CLOB Orderbook Snapshots

**URI:** `pm:OrderbookSnapshots`
  
**Row semantics:** sdl:SnapshotRow
  
**Schema:** sdl:InferredSchema
  
**Path template:** `data/parquet/{stream}/dt={date}/hour={hour}.parquet`
  
**Entity key:** `asset_id`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `_fetched_at` | sdl:Double | pm:FetchTimestamp | no |
| `_source` | sdl:Varchar | pm:DataSourceLabel | no |
| `asks` | sdl:Varchar | pm:JSONArray | yes |
| `asset_id` | sdl:Varchar | pm:CLOBTokenId | no |
| `bids` | sdl:Varchar | pm:JSONArray | yes |
| `hash` | sdl:Varchar |  | yes |
| `last_trade_price` | sdl:Varchar |  | yes |
| `market` | sdl:Varchar | pm:ConditionId | yes |
| `min_order_size` | sdl:Varchar |  | yes |
| `neg_risk` | sdl:Varchar |  | yes |
| `tick_size` | sdl:Varchar |  | yes |
| `timestamp` | sdl:Varchar |  | yes |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | Parquet schemas are inferred by Polars from JSON, not declared. The schema.py file in the fetcher defines type hints but they are NOT applied during compaction. Columns may appear or disappear depending on API response changes. Types may vary between hourly files if Polars infers differently from different data batches. Datasets declare sdl:schemaStability sdl:InferredSchema to signal this. |
| minor | Several columns store structured data as JSON strings rather than native Parquet nested types: outcomes, outcomePrices, clobTokenIds (in markets), bids/asks (in books), holders (in holders), markets/tags (in events). This happens because the compactor does not parse these fields into structured columns. |

---

## Trade Events

**URI:** `pm:Trades`
  
**Row semantics:** sdl:EventRow
  
**Schema:** sdl:InferredSchema
  
**Path template:** `data/parquet/{stream}/dt={date}/hour={hour}.parquet`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `_fetched_at` | sdl:Double | pm:FetchTimestamp | no |
| `_source` | sdl:Varchar | pm:DataSourceLabel | no |
| `asset` | sdl:Varchar | pm:CLOBTokenId | yes |
| `bio` | sdl:Varchar |  | yes |
| `conditionId` | sdl:Varchar | pm:ConditionId | yes |
| `eventSlug` | sdl:Varchar | pm:Slug | yes |
| `icon` | sdl:Varchar |  | yes |
| `name` | sdl:Varchar |  | yes |
| `outcome` | sdl:Varchar |  | yes |
| `outcomeIndex` | sdl:Double | pm:OutcomeIndex | yes |
| `price` | sdl:Double | pm:Probability | yes |
| `profileImage` | sdl:Varchar |  | yes |
| `proxyWallet` | sdl:Varchar | pm:ProxyWallet | yes |
| `pseudonym` | sdl:Varchar |  | yes |
| `side` | sdl:Varchar | pm:TradeSide | yes |
| `size` | sdl:Double | pm:TradeSize | yes |
| `slug` | sdl:Varchar | pm:Slug | yes |
| `timestamp` | sdl:Double |  | yes |
| `title` | sdl:Varchar |  | yes |
| `transactionHash` | sdl:Varchar | pm:TransactionHash | yes |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | Parquet schemas are inferred by Polars from JSON, not declared. The schema.py file in the fetcher defines type hints but they are NOT applied during compaction. Columns may appear or disappear depending on API response changes. Types may vary between hourly files if Polars infers differently from different data batches. Datasets declare sdl:schemaStability sdl:InferredSchema to signal this. |
| moderate | The trades dataset may contain duplicate trades across consecutive polls if the same trade appears in multiple API responses. The fetcher polls the most recent 100 trades every 60 seconds, so overlapping windows produce duplicates. |

---

## Token Holder Snapshots

**URI:** `pm:HolderSnapshots`
  
**Row semantics:** sdl:SnapshotRow
  
**Schema:** sdl:InferredSchema
  
**Path template:** `data/parquet/{stream}/dt={date}/hour={hour}.parquet`
  
**Entity key:** `condition_id`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `_fetched_at` | sdl:Double | pm:FetchTimestamp | no |
| `_source` | sdl:Varchar | pm:DataSourceLabel | no |
| `condition_id` | sdl:Varchar | pm:ConditionId | no |
| `holders` | sdl:Varchar |  | yes |
| `token` | sdl:Varchar | pm:CLOBTokenId | no |

### Derivations

| Derived Column | Source Columns | Function | Properties |
|----------------|----------------|----------|------------|
| `condition_id` |  | pm:FetcherConditionIdEnrichment | sdl:Deterministic |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | Parquet schemas are inferred by Polars from JSON, not declared. The schema.py file in the fetcher defines type hints but they are NOT applied during compaction. Columns may appear or disappear depending on API response changes. Types may vary between hourly files if Polars infers differently from different data batches. Datasets declare sdl:schemaStability sdl:InferredSchema to signal this. |
| moderate | Snapshot datasets (markets, events, prices, holders) contain the same entity polled multiple times per hour. Within a single hourly file, the same market/event/token may appear multiple times with slightly different values. No deduplication is performed by the compactor. |

---

## Gamma Tags

**URI:** `pm:Tags`
  
**Path template:** `data/parquet/{stream}/dt={date}/hour={hour}.parquet`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|

---

## Gamma Series

**URI:** `pm:Series`
  
**Path template:** `data/parquet/{stream}/dt={date}/hour={hour}.parquet`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|

---

## Gamma Sports

**URI:** `pm:Sports`
  
**Path template:** `data/parquet/{stream}/dt={date}/hour={hour}.parquet`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|

## Cross-Dataset Relationships

### Foreign Keys

| Relationship | From | To | Integrity |
|-------------|------|-----|-----------|
| Trades → Markets (via conditionId) | `conditionId` | `conditionId` | sdl:PartialIntegrity |
| Trades → Prices (via asset/token_id) | `asset` | `token_id` | sdl:PartialIntegrity |
| Holders → Markets (via condition_id) | `condition_id` | `conditionId` | sdl:PartialIntegrity |
| Books → Markets (via market/conditionId) | `market` | `conditionId` | sdl:PartialIntegrity |

### Same Entity

| Identity | Columns |
|----------|---------|
| Condition ID identifies the same market across datasets | `conditionId`, `conditionId`, `condition_id`, `market` |
| CLOB token ID identifies the same token across datasets | `token_id`, `asset_id`, `asset`, `token` |

