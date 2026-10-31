---
name: ControlMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The ControlMode Enum sets how the player is controlled."
---

# ControlMode

The ControlMode Enum sets how the player is controlled.

**Type:** enum

## Description

The ControlMode Enum sets how the player is controlled.

Note that shift-lock related APIs are in the process of being deprecated, so
it's recommended to use [UserInputService.MouseBehavior](/docs/reference/engine/classes/UserInputService.md) instead to lock
the mouse.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Classic` | 0 | Allows the camera to be moved by clicking and dragging with the right mouse button. |
| `MouseLockSwitch` | 1 | Similar to classic, but allows the player to toggle mouse locking, causing the camera to rotate as the player moves the mouse (without holding down a button). |