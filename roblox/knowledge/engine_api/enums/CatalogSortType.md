---
name: CatalogSortType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the sort order for catalog search results returned by AvatarEditorService:SearchCatalogAsync()."
---

# CatalogSortType

Specifies the sort order for catalog search results returned by
[AvatarEditorService:SearchCatalogAsync()](/docs/reference/engine/classes/AvatarEditorService.md).

**Type:** enum

## Description

[CatalogSortType](/docs/reference/engine/enums/CatalogSortType.md) specifies how catalog search results are ordered when
using [AvatarEditorService:SearchCatalogAsync()](/docs/reference/engine/classes/AvatarEditorService.md). Set this on a
[CatalogSearchParams](/docs/reference/engine/datatypes/CatalogSearchParams.md) object via its `SortType` property, which
defaults to [CatalogSortType.Relevance](/docs/reference/engine/enums/CatalogSortType.md).

For [CatalogSortType.Bestselling](/docs/reference/engine/enums/CatalogSortType.md) and
[CatalogSortType.MostFavorited](/docs/reference/engine/enums/CatalogSortType.md), the time window used to aggregate the
sort metric is controlled by [CatalogSearchParams.SortAggregation](/docs/reference/engine/datatypes/CatalogSearchParams.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Relevance` | 1 | Sorts catalog results by relevance to the search keyword or other query parameters. |
| `PriceHighToLow` | 2 | Sorts catalog results from the highest price to the lowest price. |
| `PriceLowToHigh` | 3 | Sorts catalog results from the lowest price to the highest price. |
| `MostFavorited` | 5 | Sorts catalog results by the number of times items have been favorited, with most-favorited items listed first. |
| `RecentlyCreated` | 6 | Sorts catalog results by creation date, with the most recently created items listed first. |
| `Bestselling` | 7 | Sorts catalog results by total sales, with best-selling items listed first. |