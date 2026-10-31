---
name: TrackerFaceTrackingStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the current state of face tracking for the device camera used by `FaceAnimatorService`."
---

# TrackerFaceTrackingStatus

Describes the current state of face tracking for the device camera used by
`FaceAnimatorService`.

**Type:** enum

## Description

Describes the current state of face tracking as reported by the device camera
tracker. Surfaced through `FaceTrackingStatusEnum`, which defaults to
[TrackerFaceTrackingStatus.FaceTrackingUninitialized](/docs/reference/engine/enums/TrackerFaceTrackingStatus.md) until the tracker
starts running.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `FaceTrackingSuccess` | 0 | Face tracking is active and a face is being tracked successfully. |
| `FaceTrackingNoFaceFound` | 1 | The tracker is running but no face has been detected in the camera feed. |
| `FaceTrackingUnknown` | 2 | The face tracking state is indeterminate or could not be mapped to a known status. |
| `FaceTrackingLost` | 3 | Face tracking was previously active but the face has been lost from the camera feed. |
| `FaceTrackingHasTrackingError` | 4 | Face tracking is active but has encountered an error that prevents reliable pose estimation. |
| `FaceTrackingIsOccluded` | 5 | A face is detected but is partially or fully occluded, reducing tracking reliability. |
| `FaceTrackingUninitialized` | 6 | Face tracking has not yet been initialized; this is the default state before the tracker starts. |