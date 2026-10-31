---
name: CatalogSearchParams
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Stores parameters used in catalog searches via AvatarEditorService:SearchCatalogAsync()."
---

# CatalogSearchParams

Stores parameters used in catalog searches via
[AvatarEditorService:SearchCatalogAsync()](/docs/reference/engine/classes/AvatarEditorService.md).

**Type:** datatype

## Description

The [CatalogSearchParams](/docs/reference/engine/datatypes/CatalogSearchParams.md) data type stores the parameters of a
catalog search via [AvatarEditorService:SearchCatalogAsync()](/docs/reference/engine/classes/AvatarEditorService.md).

When accessing the value of the [CatalogSearchParams.BundleTypes](/docs/reference/engine/datatypes/CatalogSearchParams.md) or
[CatalogSearchParams.AssetTypes](/docs/reference/engine/datatypes/CatalogSearchParams.md) property the returned table will be
read-only to avoid confusion when not directly accessing the
[CatalogSearchParams](/docs/reference/engine/datatypes/CatalogSearchParams.md) instance.

For example, you can use these properties as follows:

```lua
local params = CatalogSearchParams.new()
params.SearchKeyword = "Test"
params.MinPrice = 5000
params.MaxPrice = 10000
params.BundleTypes = {Enum.BundleType.Animations, Enum.BundleType.BodyParts}

local types = params.BundleTypes
for _, val in types do
  print(val)
end
-- table.insert(types, Enum.BundleType.Animations) -- This would not work because the table is read only
```

## Properties

### CatalogSearchParams.SearchKeyword

**Type:** `string`

The keyword to search for catalog results with.

### CatalogSearchParams.MinPrice

**Type:** `number`

The minimum item price to search for.

*Default: 0*

### CatalogSearchParams.MaxPrice

**Type:** `number`

The maximum item price to search for.

*Default: 2147483647*

### CatalogSearchParams.SortType

**Type:** `CatalogSortType`

The order in which to sort the results, represented by a
[CatalogSortType](/docs/reference/engine/enums/CatalogSortType.md).

*Default: Enum.CatalogSortType.Relevance*

### CatalogSearchParams.SortAggregation

**Type:** `Enum.CatalogSortAggregation`

The time period to use to aggregate the sort results by, represented by a
[CatalogSortAggregation](/docs/reference/engine/enums/CatalogSortAggregation.md). This only applies when the sort type is
[CatalogSortType.MostFavorited](/docs/reference/engine/enums/CatalogSortType.md) or
[CatalogSortType.BestSelling](/docs/reference/engine/enums/CatalogSortType.md). It does not apply for other sort
types.

*Default: Enum.CatalogSortAggregation.AllTime*

### CatalogSearchParams.CategoryFilter

**Type:** `CatalogCategoryFilter`

The category to filter the search by, represented by a
[CatalogCategoryFilter](/docs/reference/engine/enums/CatalogCategoryFilter.md).

*Default: Enum.CatalogCategoryFilter.None*

### CatalogSearchParams.SalesTypeFilter

**Type:** `Enum.SalesTypeFilter`

The sales type to filter the search by, represented by a
[SalesTypeFilter](/docs/reference/engine/enums/SalesTypeFilter.md). Use [SalesTypeFilter.TimedOptions](/docs/reference/engine/enums/SalesTypeFilter.md) to return
only items that have timed options available.

*Default: Enum.SalesTypeFilter.All*

### CatalogSearchParams.BundleTypes

**Type:** `Array<BundleType>`

An array containing [BundleType](/docs/reference/engine/enums/BundleType.md) values to filter the search by.

*Default: {}*

### CatalogSearchParams.AssetTypes

**Type:** `Array<AvatarAssetType>`

An array containing [AvatarAssetType](/docs/reference/engine/enums/AvatarAssetType.md) values to filter the search by.

### CatalogSearchParams.IncludeOffSale

**Type:** `bool`

Whether off sale items should be included in the results.

*Default: false*

### CatalogSearchParams.CreatorName

**Type:** `string`

Search for items with the given creator name. Specify whether to search
users, groups, or both with [CatalogSearchParams.CreatorType](/docs/reference/engine/datatypes/CatalogSearchParams.md).

### CatalogSearchParams.CreatorType

**Type:** `Enum.CreatorTypeFilter`

Search for items created by the given creator type. When unspecified, it
defaults to returning creations from both [CreatorTypeFilter.User](/docs/reference/engine/enums/CreatorTypeFilter.md)
and [CreatorTypeFilter.Group](/docs/reference/engine/enums/CreatorTypeFilter.md). Searching by
[CatalogSearchParams.CreatorId](/docs/reference/engine/datatypes/CatalogSearchParams.md) with [CreatorTypeFilter.All](/docs/reference/engine/enums/CreatorTypeFilter.md)
results in a HTTP 400 Bad Request error.

*Default: Enum.CreatorTypeFilter.All*

### CatalogSearchParams.CreatorId

**Type:** `number`

Search for items created by the single creator ID. Specify user or group
with [CatalogSearchParams.CreatorType](/docs/reference/engine/datatypes/CatalogSearchParams.md). Searching by creator ID
**and** creator name is not supported; specify one, not both.

*Default: 0*

### CatalogSearchParams.Limit

**Type:** `number`

Specifies the number of items to return. Accepts `10`, `28`, `30`, `60`,
and `120`. Defaults to `30`.