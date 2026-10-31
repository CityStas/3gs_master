---
name: TrackerError
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Status and error codes reported by the face-tracking subsystem through the `TrackerError` events on `RTAnimationTracker` and `FaceAnimatorService`."
---

# TrackerError

Status and error codes reported by the face-tracking subsystem through the
`TrackerError` events on `RTAnimationTracker` and `FaceAnimatorService`.

**Type:** enum

## Description

Passed to `TrackerError` handlers on `RTAnimationTracker` and
`FaceAnimatorService` to indicate why face tracking failed or stopped.
[TrackerError.Ok](/docs/reference/engine/enums/TrackerError.md) is a clean state; other values cover initialization,
service availability, video input, or audio input failures.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Ok` | 0 | No error; the tracker is operating normally. |
| `NoService` | 1 | A required engine service was unavailable when the tracker attempted to connect. |
| `InitFailed` | 2 | The tracker failed to create or initialize its tracking session. |
| `NoVideo` | 3 | Video input is unavailable because no camera device was found or the camera was disconnected. |
| `VideoError` | 4 | A generic video error occurred during face-tracking camera input processing. |
| `VideoNoPermission` | 5 | The user denied camera permission required for video-based face tracking. |
| `VideoUnsupported` | 6 | Video-based face tracking is not supported on this device or platform. |
| `NoAudio` | 7 | Audio input is unavailable because `SoundService` could not be found or connected. |
| `AudioError` | 8 | A generic audio error occurred during face-tracking audio input processing. |
| `AudioNoPermission` | 9 | The user denied microphone permission required for audio-based face tracking. |
| `UnsupportedDevice` | 10 | The current device or platform does not support face tracking. |