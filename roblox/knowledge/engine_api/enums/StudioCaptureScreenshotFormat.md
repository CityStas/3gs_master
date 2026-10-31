---
name: StudioCaptureScreenshotFormat
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the pixel format of the image buffer stored in a StudioScreenshotCapture object."
---

# StudioCaptureScreenshotFormat

Specifies the pixel format of the image buffer stored in a
[StudioScreenshotCapture](/docs/reference/engine/classes/StudioScreenshotCapture.md) object.

**Type:** enum

## Description

Specifies the pixel format used when
[StudioCaptureService:CaptureScreenshot()](/docs/reference/engine/classes/StudioCaptureService.md) stores the captured image.
Pass this value as the `Format` key in the options table to
[StudioCaptureService:CaptureScreenshot()](/docs/reference/engine/classes/StudioCaptureService.md); it is then reflected as the
read-only [StudioScreenshotCapture.BufferFormat](/docs/reference/engine/classes/StudioScreenshotCapture.md) property. When `Format`
is omitted, the capture defaults to
[StudioCaptureScreenshotFormat.RGBA8](/docs/reference/engine/enums/StudioCaptureScreenshotFormat.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `RGBA8` | 0 | The buffer contains raw, uncompressed RGBA pixel data with 8 bits per channel (4 bytes per pixel). |
| `PNG` | 1 | The buffer contains a complete PNG-encoded image. |