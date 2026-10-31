---
name: VRControllerModelMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether and how the player's VR hand controller models are rendered in an experience."
---

# VRControllerModelMode

Controls whether and how the player's VR hand controller models are rendered
in an experience.

**Type:** enum

## Description

`VRControllerModelMode` is used by the [VRService.ControllerModels](/docs/reference/engine/classes/VRService.md)
property to determine how the 3D models representing a VR player's hand
controllers are displayed.

The default value of [VRService.ControllerModels](/docs/reference/engine/classes/VRService.md) is
[Transparent](/docs/reference/engine/enums/VRControllerModelMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Disabled` | 0 | The player's VR hand controller models are not rendered. |
| `Transparent` | 1 | The player's VR hand controller models are rendered with transparency. |