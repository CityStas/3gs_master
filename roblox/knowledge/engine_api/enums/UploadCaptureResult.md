---
name: UploadCaptureResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the outcome of a CaptureService:UploadCaptureAsync() call."
---

# UploadCaptureResult

Describes the outcome of a [CaptureService:UploadCaptureAsync()](/docs/reference/engine/classes/CaptureService.md) call.

**Type:** enum

## Description

Represents the result of uploading a capture to the asset system.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Success` | 0 | The capture was successfully uploaded and registered as an asset. |
| `NeedPermission` | 1 | The experience has not been granted developer gallery read and upload permission, so the capture cannot be uploaded. |
| `CaptureModerated` | 2 | The capture was rejected by Roblox content moderation and cannot be uploaded. |
| `CaptureNotInGallery` | 3 | The capture no longer exists in the user's gallery and cannot be uploaded. |
| `IneligibleCapture` | 4 | The capture is not eligible for upload to this experience, either because it is a permanent system capture or the experience permissions grant was rejected. |
| `UploadQuotaReached` | 5 | The user has reached their daily capture upload quota and the upload was not completed. |
| `UploadPending` | 6 | The upload is still in progress and the asset has not yet been assigned an ID; poll [CaptureService:CheckUploadCaptureStatusAsync()](/docs/reference/engine/classes/CaptureService.md) again to check for completion. |
| `UploadFailed` | 7 | The upload completed but a backend processing error occurred, so the capture was not saved as an asset. |