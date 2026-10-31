---
name: DataStoreRequestType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates the type of data store request being made."
---

# DataStoreRequestType

Indicates the type of data store request being made.

**Type:** enum

## Description

Categorizes data store operations for use with
[DataStoreService:GetRequestBudgetForRequestType()](/docs/reference/engine/classes/DataStoreService.md), which returns the
remaining per-server request budget for a given category.

The enum contains two sets of values. The **legacy** values (`GetAsync`,
`SetIncrementAsync`, `UpdateAsync`, `GetSortedAsync`,
`SetIncrementSortedAsync`, `OnUpdate`, `ListAsync`, `GetVersionAsync`, and
`RemoveVersionAsync`) should not be used. The **modern** values
(`StandardRead`, `StandardWrite`, `StandardList`, `StandardRemove`,
`OrderedRead`, `OrderedWrite`, `OrderedList`, and `OrderedRemove`) correspond
to the newer [DataStore](/docs/reference/engine/classes/DataStore.md) and [OrderedDataStore](/docs/reference/engine/classes/OrderedDataStore.md) API families that
use universe-level and per-server limits.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `GetAsync` | 0 | Refers to [GetAsync()](/docs/reference/engine/classes/GlobalDataStore.md) and the read of [UpdateAsync()](/docs/reference/engine/classes/GlobalDataStore.md). |
| `SetIncrementAsync` | 1 | Refers to [SetAsync()](/docs/reference/engine/classes/DataStore.md), [IncrementAsync()](/docs/reference/engine/classes/DataStore.md), [RemoveAsync()](/docs/reference/engine/classes/DataStore.md), and the write of [UpdateAsync()](/docs/reference/engine/classes/DataStore.md) when it returns a non-`nil` value. |
| `UpdateAsync` | 2 | Refers to [UpdateAsync()](/docs/reference/engine/classes/GlobalDataStore.md). |
| `GetSortedAsync` | 3 | Refers to [GetSortedAsync()](/docs/reference/engine/classes/OrderedDataStore.md). |
| `SetIncrementSortedAsync` | 4 | Refers to [SetAsync()](/docs/reference/engine/classes/OrderedDataStore.md) [IncrementAsync()](/docs/reference/engine/classes/OrderedDataStore.md), [RemoveAsync()](/docs/reference/engine/classes/OrderedDataStore.md), and the write of [UpdateAsync()](/docs/reference/engine/classes/OrderedDataStore.md) while using an [OrderedDataStore](/docs/reference/engine/classes/OrderedDataStore.md). |
| `OnUpdate` | 5 | Refers to [OnUpdate()](/docs/reference/engine/classes/GlobalDataStore.md). |
| `ListAsync` | 6 | Refers to [ListKeysAsync()](/docs/reference/engine/classes/DataStore.md) and [ListVersionsAsync()](/docs/reference/engine/classes/DataStore.md). |
| `GetVersionAsync` | 7 | Refers to [GetVersionAsync()](/docs/reference/engine/classes/DataStore.md). |
| `RemoveVersionAsync` | 8 | Refers to [RemoveVersionAsync()](/docs/reference/engine/classes/DataStore.md). |
| `StandardRead` | 9 | Refers to [GetAsync()](/docs/reference/engine/classes/DataStore.md), [GetVersionAsync()](/docs/reference/engine/classes/DataStore.md), [GetVersionAtTimeAsync()](/docs/reference/engine/classes/DataStore.md), and the read of [UpdateAsync()](/docs/reference/engine/classes/DataStore.md) for [DataStore](/docs/reference/engine/classes/DataStore.md). |
| `StandardWrite` | 10 | Refers to [SetAsync()](/docs/reference/engine/classes/DataStore.md), [IncrementAsync()](/docs/reference/engine/classes/DataStore.md), and the write of [UpdateAsync()](/docs/reference/engine/classes/DataStore.md) for [DataStore](/docs/reference/engine/classes/DataStore.md). |
| `StandardList` | 11 | Refers to [ListDataStoresAsync()](/docs/reference/engine/classes/DataStoreService.md), and [ListKeysAsync()](/docs/reference/engine/classes/DataStore.md) and [ListVersionsAsync()](/docs/reference/engine/classes/DataStore.md) for [DataStore](/docs/reference/engine/classes/DataStore.md). |
| `StandardRemove` | 12 | Refers to [RemoveAsync()](/docs/reference/engine/classes/DataStore.md) for [DataStore](/docs/reference/engine/classes/DataStore.md). |
| `OrderedRead` | 13 | Refers to [GetAsync()](/docs/reference/engine/classes/OrderedDataStore.md) and the read of [UpdateAsync()](/docs/reference/engine/classes/OrderedDataStore.md) for [OrderedDataStore](/docs/reference/engine/classes/OrderedDataStore.md). |
| `OrderedWrite` | 14 | Refers to [SetAsync()](/docs/reference/engine/classes/OrderedDataStore.md), [IncrementAsync()](/docs/reference/engine/classes/OrderedDataStore.md), and the write of [UpdateAsync()](/docs/reference/engine/classes/OrderedDataStore.md) for [OrderedDataStore](/docs/reference/engine/classes/OrderedDataStore.md). |
| `OrderedList` | 15 | Refers to [GetSortedAsync()](/docs/reference/engine/classes/OrderedDataStore.md) for [OrderedDataStore](/docs/reference/engine/classes/OrderedDataStore.md). GetRequestBudgetForRequestType()`with this enum will return`0`. |
| `OrderedRemove` | 16 | Refers to [RemoveAsync()](/docs/reference/engine/classes/OrderedDataStore.md) for [OrderedDataStore](/docs/reference/engine/classes/OrderedDataStore.md). |