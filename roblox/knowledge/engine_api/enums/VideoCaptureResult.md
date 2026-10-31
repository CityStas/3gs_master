---
name: VideoCaptureResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates whether a video capture session ended successfully or the reason it was interrupted."
---

# VideoCaptureResult

Indicates whether a video capture session ended successfully or the reason it
was interrupted.

**Type:** enum

## Description

Passed as the `result` argument of `UserVideoCaptureFailed` when a video
capture session ends. [VideoCaptureResult.Success](/docs/reference/engine/enums/VideoCaptureResult.md) means the capture
completed normally; other values identify why recording stopped.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Success` | 0 | Video capture ended normally without any errors. |
| `OtherError` | 1 | Video capture stopped due to an unspecified internal error. |
| `ScreenSizeChanged` | 2 | Video capture was interrupted because the screen dimensions changed while recording was in progress. |
| `TimeLimitReached` | 3 | Video capture was stopped automatically because the maximum allowed recording duration was reached. |