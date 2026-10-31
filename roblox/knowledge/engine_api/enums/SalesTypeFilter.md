---
name: SalesTypeFilter
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Filters catalog search results by sales type."
---

# SalesTypeFilter

Filters catalog search results by sales type.

**Type:** enum

## Description

The [SalesTypeFilter](/docs/reference/engine/enums/SalesTypeFilter.md) enum is used with
[CatalogSearchParams.SalesTypeFilter](/docs/reference/engine/datatypes/CatalogSearchParams.md) to filter catalog search
results by their sales type when calling
[AvatarEditorService:SearchCatalogAsync()](/docs/reference/engine/classes/AvatarEditorService.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `All` | 1 | Returns all items regardless of sales type. |
| `Collectibles` | 2 | Returns only collectible items (Limited and Limited Unique). |
| `Premium` | 3 | Returns only items with Premium pricing. |
| `TimedOptions` | 4 | Returns only items that have timed options available. |