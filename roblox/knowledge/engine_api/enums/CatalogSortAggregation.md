---
name: CatalogSortAggregation
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the time window over which catalog items are aggregated when sorting CatalogSearchParams results."
---

# CatalogSortAggregation

Specifies the time window over which catalog items are aggregated when sorting
[CatalogSearchParams](/docs/reference/engine/datatypes/CatalogSearchParams.md) results.

**Type:** enum

## Description

Specifies the time window used to aggregate catalog item data when sorting
search results via [CatalogSearchParams.SortAggregation](/docs/reference/engine/datatypes/CatalogSearchParams.md). The
selected period determines which sales, popularity, or relevance signals are
counted toward the sort order. [CatalogSortAggregation.AllTime](/docs/reference/engine/enums/CatalogSortAggregation.md) is the
default.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Past12Hours` | 1 | Aggregates catalog data from the past 12 hours when sorting search results. |
| `PastDay` | 2 | Aggregates catalog data from the past day when sorting search results. |
| `Past3Days` | 3 | Aggregates catalog data from the past 3 days when sorting search results. |
| `PastWeek` | 4 | Aggregates catalog data from the past week when sorting search results. |
| `PastMonth` | 5 | Aggregates catalog data from the past month when sorting search results. |
| `AllTime` | 6 | Aggregates catalog data across all time when sorting search results. |