---
name: SortDirection
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether results are ordered from lowest to highest or from highest to lowest."
---

# SortDirection

Controls whether results are ordered from lowest to highest or from highest to
lowest.

**Type:** enum

## Description

Controls the ordering direction of results returned by APIs that support
sorted retrieval, such as [DataStore:ListVersionsAsync()](/docs/reference/engine/classes/DataStore.md) and
[MemoryStoreSortedMap:GetRangeAsync()](/docs/reference/engine/classes/MemoryStoreSortedMap.md). Pass
[SortDirection.Ascending](/docs/reference/engine/enums/SortDirection.md) to receive items ordered from lowest to highest
(or oldest to newest), and [SortDirection.Descending](/docs/reference/engine/enums/SortDirection.md) to receive them
from highest to lowest (or newest to oldest).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Ascending` | 0 | Orders results from lowest to highest value, or from oldest to newest entry. |
| `Descending` | 1 | Orders results from highest to lowest value, or from newest to oldest entry. |