---
name: CameraMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used to set Player.CameraMode to determine when first person and third person cameras should be used."
---

# CameraMode

Used to set [Player.CameraMode](/docs/reference/engine/classes/Player.md) to determine when first person and third
person cameras should be used.

**Type:** enum

## Description

The **CameraMode** enum is used to set [Player.CameraMode](/docs/reference/engine/classes/Player.md) to determine
when first person and third person cameras should be used.

#### Third Person

In the default third person mode ([Classic](/docs/reference/engine/enums/CameraMode.md)), the character
can be seen in the camera. While in this mode, the default behavior is:

- Players can right-click and drag (mouse), tap and drag (mobile), use the
  secondary thumbstick (gamepad), or press the left/right arrows (keyboard) to
  rotate the camera around their character.
- When a player moves their character, it faces in the corresponding movement
  direction.
- Players can zoom in and out freely, even to first person on full zoom in.

#### First Person

In first person mode ([LockFirstPerson](/docs/reference/engine/enums/CameraMode.md)), the player's camera
is zoomed all the way in. Unless there is a visible GUI present with the
[GuiButton.Modal](/docs/reference/engine/classes/GuiButton.md) property set to `true`, moving the mouse, tap-dragging
on mobile, or using the secondary thumbstick on a gamepad will rotate the
camera around the character.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Classic` | 0 | Third person camera which can be zoomed into first person. |
| `LockFirstPerson` | 1 | Exclusively first person camera. |