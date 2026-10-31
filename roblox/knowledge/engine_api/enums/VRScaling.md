---
name: VRScaling
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether VRService automatically adjusts the perceived scale of the world in VR to match the player's avatar size."
---

# VRScaling

Controls whether [VRService](/docs/reference/engine/classes/VRService.md) automatically adjusts the perceived scale
of the world in VR to match the player's avatar size.

**Type:** enum

## Description

`VRScaling` is used by the [VRService.AutomaticScaling](/docs/reference/engine/classes/VRService.md) property to
determine how the engine scales the player's view in VR. When set to
[VRScaling.World](/docs/reference/engine/enums/VRScaling.md), the engine automatically adjusts
[Camera.HeadScale](/docs/reference/engine/classes/Camera.md) so that the scale of the world matches the player's
avatar height, preserving immersion when avatars differ in size. When set to
[VRScaling.Off](/docs/reference/engine/enums/VRScaling.md), no automatic adjustment is made and you can set
[Camera.HeadScale](/docs/reference/engine/classes/Camera.md) manually to control the perceived world scale.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `World` | 0 | Adjusts [Camera.HeadScale](/docs/reference/engine/classes/Camera.md) so that the world in VR is seen from the avatar's perspective. |
| `Off` | 1 | Disables VR automatic scaling; set [Camera.HeadScale](/docs/reference/engine/classes/Camera.md) manually if needed. |