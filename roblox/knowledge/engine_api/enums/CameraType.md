---
name: CameraType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the camera behavior mode if using the default PlayerScripts."
---

# CameraType

Describes the camera behavior mode if using the default PlayerScripts.

**Type:** enum

## Description

The CameraType Enum is used in [Camera.CameraType](/docs/reference/engine/classes/Camera.md) to set the behavior
of the Camera object.

Attach, Watch, Track, and Follow all require a valid
[Camera.CameraSubject](/docs/reference/engine/classes/Camera.md) to work properly.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Fixed` | 0 | Camera is stationary. |
| `Attach` | 1 | Camera moves with the subject at a fixed offset and will rotate as the subject rotates. |
| `Watch` | 2 | Camera is stationary but will rotate to keep the subject in the center of the screen. |
| `Track` | 3 | Camera moves with the subject but does not rotate automatically. |
| `Follow` | 4 | Camera moves with the subject and rotates to keep the subject in the center. |
| `Custom` | 5 | Default mode used by Roblox core scripts. |
| `Scriptable` | 6 | No default behavior. Used when developers need to script custom behavior. |
| `Orbital` | 7 | The camera has a fixed Y position, but can be rotated around the player. |