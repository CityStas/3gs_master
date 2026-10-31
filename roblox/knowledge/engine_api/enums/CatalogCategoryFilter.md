---
name: CatalogCategoryFilter
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Filters Avatar Shop catalog search results by a predefined category such as Featured, Premium, or Recommended."
---

# CatalogCategoryFilter

Filters Avatar Shop catalog search results by a predefined category such as
Featured, Premium, or Recommended.

**Type:** enum

## Description

Used with [CatalogSearchParams.CategoryFilter](/docs/reference/engine/datatypes/CatalogSearchParams.md) to narrow Avatar Shop
catalog search results by category when calling
[AvatarEditorService:SearchCatalogAsync()](/docs/reference/engine/classes/AvatarEditorService.md). Defaults to
[CatalogCategoryFilter.None](/docs/reference/engine/enums/CatalogCategoryFilter.md), which applies no category filter and
returns items from all categories.

To filter by collectible items (Limited and Limited Unique), use
[SalesTypeFilter.Collectibles](/docs/reference/engine/enums/SalesTypeFilter.md) via
[CatalogSearchParams.SalesTypeFilter](/docs/reference/engine/datatypes/CatalogSearchParams.md) instead of the deprecated
[CatalogCategoryFilter.Collectibles](/docs/reference/engine/enums/CatalogCategoryFilter.md) value.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 1 | No category filter is applied; returns items from all categories. This is the default value of [CatalogSearchParams.CategoryFilter](/docs/reference/engine/datatypes/CatalogSearchParams.md). |
| `Featured` | 2 | Returns only items editorially featured in the Avatar Shop catalog. |
| `Collectibles` | 3 | Deprecated. Previously filtered for collectible items; use [SalesTypeFilter.Collectibles](/docs/reference/engine/enums/SalesTypeFilter.md) via [CatalogSearchParams.SalesTypeFilter](/docs/reference/engine/datatypes/CatalogSearchParams.md) instead. |
| `CommunityCreations` | 4 | Returns only items created by community developers. |
| `Premium` | 5 | Returns only items available to Roblox Premium subscribers. |
| `Recommended` | 6 | Returns only items recommended by the catalog for the current user. |