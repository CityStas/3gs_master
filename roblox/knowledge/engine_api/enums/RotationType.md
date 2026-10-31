---
name: RotationType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls how a player character's body rotation is determined — relative to the camera direction or relative to the movement direction."
---

# RotationType

Controls how a player character's body rotation is determined — relative to
the camera direction or relative to the movement direction.

**Type:** enum

## Description

`RotationType` is used by [UserGameSettings.RotationType](/docs/reference/engine/classes/UserGameSettings.md) to specify how
the local player's character orients its body. With
[RotationType.MovementRelative](/docs/reference/engine/enums/RotationType.md) (the default), the character turns to
face whichever direction it is moving. With
[RotationType.CameraRelative](/docs/reference/engine/enums/RotationType.md), the character's body continuously aligns
with the camera's look direction, enabling first-person-style aiming where the
character faces wherever the player is looking regardless of movement
direction.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `MovementRelative` | 0 | The character's body rotation follows the direction of movement. |
| `CameraRelative` | 1 | The character's body rotation continuously follows the camera's look direction. |