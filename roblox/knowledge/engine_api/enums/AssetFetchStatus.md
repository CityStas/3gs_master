---
name: AssetFetchStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the download state of an asset requested through ContentProvider."
---

# AssetFetchStatus

Describes the download state of an asset requested through
[ContentProvider](/docs/reference/engine/classes/ContentProvider.md).

**Type:** enum

## Description

Describes the download state of an asset requested through
[ContentProvider](/docs/reference/engine/classes/ContentProvider.md). Every content ID has exactly one status at any given
time, transitioning from [AssetFetchStatus.None](/docs/reference/engine/enums/AssetFetchStatus.md) (never requested) to
[AssetFetchStatus.Loading](/docs/reference/engine/enums/AssetFetchStatus.md) (fetch in progress) and finally to a terminal
state of [AssetFetchStatus.Success](/docs/reference/engine/enums/AssetFetchStatus.md), [AssetFetchStatus.Failure](/docs/reference/engine/enums/AssetFetchStatus.md), or
[AssetFetchStatus.TimedOut](/docs/reference/engine/enums/AssetFetchStatus.md).

Query the current status with [ContentProvider:GetAssetFetchStatus()](/docs/reference/engine/classes/ContentProvider.md)
and listen for transitions with
[ContentProvider:GetAssetFetchStatusChangedSignal()](/docs/reference/engine/classes/ContentProvider.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Success` | 0 | The asset loaded successfully. |
| `Failure` | 1 | The asset failed to load successfully. Subsequent attempts are likely to fail; there may be something wrong with the [Content](/docs/reference/engine/datatypes/Content.md) string. |
| `None` | 2 | The engine has no information about this asset. The engine never tried to load it. |
| `Loading` | 3 | The engine is in the middle of trying to load this asset. |
| `TimedOut` | 4 | The engine tried to load this asset but timed out. Future attempts to load may succeed. |