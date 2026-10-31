---
name: CreatorTypeFilter
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies which creator type to include when filtering catalog search results in CatalogSearchParams."
---

# CreatorTypeFilter

Specifies which creator type to include when filtering catalog search results
in [CatalogSearchParams](/docs/reference/engine/datatypes/CatalogSearchParams.md).

**Type:** enum

## Description

Specifies which creator type to include when filtering catalog search results.
Used with the [CatalogSearchParams.CreatorType](/docs/reference/engine/datatypes/CatalogSearchParams.md) property to narrow
results to items made by individual users, groups, or any creator. The default
value of [CatalogSearchParams.CreatorType](/docs/reference/engine/datatypes/CatalogSearchParams.md) is
[CreatorTypeFilter.All](/docs/reference/engine/enums/CreatorTypeFilter.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `User` | 0 | Limits catalog search results to items created by individual users. |
| `Group` | 1 | Limits catalog search results to items created by groups. |
| `All` | 2 | Includes items from all creator types; no filtering by creator is applied. |