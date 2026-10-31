---
name: TrackerType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the type of motion tracking that an `RTAnimationTracker` performs."
---

# TrackerType

Specifies the type of motion tracking that an `RTAnimationTracker` performs.

**Type:** enum

## Description

`TrackerType` controls which tracking modality the `RTAnimationTracker` uses
to generate real-time animation data. Changing the `TrackerType` property
shuts down the current tracking engine and reinitializes with the newly
selected type.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | No tracking type is selected; the tracking engine does not initialize, and attempting to start tracking with this type set raises `TrackerError.UnsupportedDevice`. |
| `Face` | 1 | Enables face tracking from a connected video device (and optionally audio) to produce FACS blendshape weights and head-orientation data each step. |
| `UpperBody` | 2 | Reserved for upper-body motion tracking. Setting this type raises `TrackerError.UnsupportedDevice` on initialization. |