---
name: CreateAssetResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates the outcome of a call to AssetService:CreateAssetAsync() or AssetService:CreateAssetVersionAsync()."
---

# CreateAssetResult

Indicates the outcome of a call to [AssetService:CreateAssetAsync()](/docs/reference/engine/classes/AssetService.md) or
[AssetService:CreateAssetVersionAsync()](/docs/reference/engine/classes/AssetService.md).

**Type:** enum

## Description

[CreateAssetResult](/docs/reference/engine/enums/CreateAssetResult.md) is returned as the first element of the tuple from
[AssetService:CreateAssetAsync()](/docs/reference/engine/classes/AssetService.md) and
[AssetService:CreateAssetVersionAsync()](/docs/reference/engine/classes/AssetService.md). It indicates whether the asset
was created or updated successfully, or why the operation failed. On success,
the second tuple element is the new asset ID (for `CreateAssetAsync`) or the
new version number (for `CreateAssetVersionAsync`); on failure, the second
element is a string with additional diagnostic information.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Success` | 1 | The asset was created or updated successfully. |
| `PermissionDenied` | 2 | The caller does not have permission to create or update an asset in the target inventory. |
| `UploadFailed` | 3 | The upload request to the Roblox asset service failed for a reason other than a permission error. |
| `Unknown` | 4 | An unexpected error occurred and the operation could not complete. |