---
name: ScreenshotCaptureResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the result of a screenshot capture initiated by CaptureService:TakeScreenshotCaptureAsync()."
---

# ScreenshotCaptureResult

Describes the result of a screenshot capture initiated by
[CaptureService:TakeScreenshotCaptureAsync()](/docs/reference/engine/classes/CaptureService.md).

**Type:** enum

## Description

The ScreenshotCaptureResult enum describes the result of a screenshot capture
initiated through [CaptureService:TakeScreenshotCaptureAsync()](/docs/reference/engine/classes/CaptureService.md). It is
passed as the first argument to the `onCaptureReady` callback.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Success` | 0 | The screenshot capture completed successfully. |
| `OtherError` | 1 | The screenshot capture failed due to an unspecified error. |
| `NoDeviceSupport` | 2 | The device does not support screenshot captures. |
| `NoSpaceOnDevice` | 3 | The device does not have enough storage space to save the screenshot capture. |