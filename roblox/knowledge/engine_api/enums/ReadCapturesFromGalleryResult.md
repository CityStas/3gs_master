---
name: ReadCapturesFromGalleryResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the outcome of a CaptureService:ReadCapturesFromGalleryAsync() call."
---

# ReadCapturesFromGalleryResult

Describes the outcome of a
[CaptureService:ReadCapturesFromGalleryAsync()](/docs/reference/engine/classes/CaptureService.md) call.

**Type:** enum

## Description

Represents the result of reading captures from a user's gallery.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Success` | 0 | The read operation completed successfully and capture data has been returned. |
| `NeedPermission` | 1 | The read operation failed because the experience has not been granted permission to access the user's capture gallery. |