---
name: CreateContentResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates the result of a AssetService:CreateDataModelContentAsync() call."
---

# CreateContentResult

Indicates the result of a [AssetService:CreateDataModelContentAsync()](/docs/reference/engine/classes/AssetService.md)
call.

**Type:** enum

## Description

Returned as the first value in the tuple from
[AssetService:CreateDataModelContentAsync()](/docs/reference/engine/classes/AssetService.md), which creates a
`DataModel`-scoped runtime content object at runtime. A value of
[Success](/docs/reference/engine/enums/CreateContentResult.md) means the content was created and
stored successfully; any other value describes why the operation failed.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Success` | 1 | The content object was created and stored successfully. |
| `PermissionDenied` | 2 | The user does not have the required permissions to perform this operation. |
| `UploadFailed` | 3 | Asset failed to upload. |
| `StorageLimitExceeded` | 4 | The storage budget limit for [DataModel](/docs/reference/engine/classes/DataModel.md)-scoped content was exceeded. |
| `Unknown` | 5 | An unknown error occurred. |