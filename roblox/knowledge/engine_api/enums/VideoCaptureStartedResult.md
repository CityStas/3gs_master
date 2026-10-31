---
name: VideoCaptureStartedResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the outcome of a video capture start request made through CaptureService."
---

# VideoCaptureStartedResult

Describes the outcome of a video capture start request made through
[CaptureService](/docs/reference/engine/classes/CaptureService.md).

**Type:** enum

## Description

Describes the outcome of a video capture start request initiated via
[CaptureService:StartVideoCaptureAsync()](/docs/reference/engine/classes/CaptureService.md). The value is returned
directly by that method and is also surfaced through the
`UserVideoCaptureStartFailed` event when the result is not
[VideoCaptureStartedResult.Success](/docs/reference/engine/enums/VideoCaptureStartedResult.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Success` | 0 | Video capture started successfully. |
| `OtherError` | 1 | Video capture failed due to an unspecified internal error. |
| `CapturingAlready` | 2 | A video capture session is already in progress and a new one cannot be started. |
| `NoDeviceSupport` | 3 | The device does not have the required capture capabilities. |
| `NoSpaceOnDevice` | 4 | The device does not have sufficient storage space available to begin capturing video. |