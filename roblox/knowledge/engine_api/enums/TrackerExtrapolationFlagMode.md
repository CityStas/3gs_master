---
name: TrackerExtrapolationFlagMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls how the face-tracking pipeline extrapolates animation data between camera frames on the `TrackerLodController`."
---

# TrackerExtrapolationFlagMode

Controls how the face-tracking pipeline extrapolates animation data between
camera frames on the `TrackerLodController`.

**Type:** enum

## Description

Controls how the face-tracking pipeline extrapolates animation data between
camera frames. This mode is set via `VideoExtrapolationMode` on
`TrackerLodController` and determines whether the tracker infers intermediate
facial poses and FACS (Facial Action Coding System) blend-shape values when
the camera delivers frames at a lower rate than the animation update rate.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `ForceDisabled` | 0 | Disables all extrapolation so that facial animation updates only when a new camera frame is processed. |
| `ExtrapolateFacsAndPose` | 1 | Extrapolates both FACS blend-shape values and head-pose data between camera frames. |
| `ExtrapolateFacsOnly` | 2 | Extrapolates only FACS blend-shape values between camera frames, leaving head-pose data unchanged. |
| `Auto` | 3 | Lets the `TrackerLodController` automatically select the extrapolation strategy based on current performance conditions. |