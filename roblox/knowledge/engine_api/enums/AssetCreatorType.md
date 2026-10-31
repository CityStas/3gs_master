---
name: AssetCreatorType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates whether an asset is owned by an individual user or a group."
---

# AssetCreatorType

Indicates whether an asset is owned by an individual user or a group.

**Type:** enum

## Description

Indicates whether an asset is owned by an individual user or a group. Used as
the `CreatorType` field in the request parameters of
[AssetService:CreateAssetAsync()](/docs/reference/engine/classes/AssetService.md) and
[AssetService:CreateAssetVersionAsync()](/docs/reference/engine/classes/AssetService.md) to specify the type of entity
that will own the resulting asset. When set to [AssetCreatorType.User](/docs/reference/engine/enums/AssetCreatorType.md),
the accompanying `CreatorId` is interpreted as a user ID; when set to
[AssetCreatorType.Group](/docs/reference/engine/enums/AssetCreatorType.md), it is interpreted as a group ID.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `User` | 0 | The asset is owned by an individual user; the accompanying creator ID is a user ID. |
| `Group` | 1 | The asset is owned by a group; the accompanying creator ID is a group ID. |