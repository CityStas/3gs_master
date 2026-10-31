---
name: CaptureType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates whether a capture is a screenshot or a video recording."
---

# CaptureType

Indicates whether a capture is a screenshot or a video recording.

**Type:** enum

## Description

Indicates whether a capture is a screenshot or a video recording.
[CaptureService](/docs/reference/engine/classes/CaptureService.md) passes this value in
[CaptureService.CaptureBegan](/docs/reference/engine/classes/CaptureService.md) and [CaptureService.CaptureEnded](/docs/reference/engine/classes/CaptureService.md),
and accepts an array of [CaptureType](/docs/reference/engine/enums/CaptureType.md) values as the `captureTypeFilters`
argument of [CaptureService:ReadCapturesFromGalleryAsync()](/docs/reference/engine/classes/CaptureService.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Screenshot` | 1 | The capture is a screenshot image. |
| `Video` | 2 | The capture is a video recording. |