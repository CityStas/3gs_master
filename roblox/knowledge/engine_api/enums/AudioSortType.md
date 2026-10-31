---
name: AudioSortType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The ordering of audio search results."
---

# AudioSortType

The ordering of audio search results.

**Type:** enum

## Description

The ordering of audio search results, used by
[AudioSearchParams.SortType](/docs/reference/engine/classes/AudioSearchParams.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Relevance` | 1 | Orders results by relevance to the search keyword. |
| `MostUsed` | 2 | Orders results from most used to least used. |
| `Trending` | 3 | Orders results from most trending to least trending. |
| `RecentlyCreated` | 4 | Orders results from newest to oldest. |
| `ShortestToLongest` | 5 | Orders results by duration, from shortest to longest. |
| `LongestToShortest` | 6 | Orders results by duration, from longest to shortest. |