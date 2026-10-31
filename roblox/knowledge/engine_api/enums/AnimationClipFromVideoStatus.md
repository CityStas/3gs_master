---
name: AnimationClipFromVideoStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates the current status or final outcome of a video-to-animation conversion started by AssetService:PromptImportAnimationClipFromVideoAsync()."
---

# AnimationClipFromVideoStatus

Indicates the current status or final outcome of a video-to-animation
conversion started by
[AssetService:PromptImportAnimationClipFromVideoAsync()](/docs/reference/engine/classes/AssetService.md).

**Type:** enum

## Description

Describes the status of a video-to-animation conversion initiated by
[AssetService:PromptImportAnimationClipFromVideoAsync()](/docs/reference/engine/classes/AssetService.md). Values in this
enum are reported both as progress updates through the method's
`progressCallback` and as the final outcome in the returned tuple.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Initializing` | 0 | The video-to-animation job is being set up on the server. |
| `Pending` | 1 | The job has been queued on the server and is waiting for processing resources to become available. |
| `Processing` | 2 | The server is actively analyzing the video and extracting motion-capture data to generate the animation clip. |
| `ErrorGeneric` | 4 | The server-side video processing encountered an unspecified error. |
| `Success` | 6 | The video was successfully converted into an [AnimationClip](/docs/reference/engine/classes/AnimationClip.md), which is returned as the second element of the result tuple. |
| `ErrorVideoTooLong` | 7 | Processing failed because the uploaded video exceeds the maximum allowed duration (15 seconds). |
| `ErrorNoPersonDetected` | 8 | Processing failed because no person could be detected in the video; the video must show a person fully in frame, facing the camera. |
| `ErrorVideoUnstable` | 9 | Processing failed because the video is too shaky for reliable motion capture; a more stable recording is required. |
| `Timeout` | 10 | Processing could not be completed in time, typically due to high request volume on the video processing backend. |
| `Cancelled` | 11 | The player declined the consent prompt or provided no input, so the video upload was not started. |
| `ErrorMultiplePeople` | 12 | Processing failed because more than one person was detected in the video; the video must contain a single person fully in frame. |
| `ErrorUploadingVideo` | 2001 | The client-side video upload failed before the video reached the processing backend. |