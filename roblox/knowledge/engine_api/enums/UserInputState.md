---
name: UserInputState
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "This enum describes the state of an input that is currently or was recently performed."
---

# UserInputState

This enum describes the state of an input that is currently or was recently
performed.

**Type:** enum

## Description

The `UserInputState` enum describes the state of an input that is currently or
was recently performed. It is used by the [InputObject.UserInputState](/docs/reference/engine/classes/InputObject.md)
property of the same name, as well as various [UserInputService](/docs/reference/engine/classes/UserInputService.md) and
[GuiObject](/docs/reference/engine/classes/GuiObject.md) events.

Depending on the [UserInputType](/docs/reference/engine/enums/UserInputType.md), input may follow states differently:

- Simple button and key presses generally follow a simple `Begin` to `End`
  flow. Analog gamepad trigger buttons are similar to button presses but will
  use `Change` as the trigger pressure changes.
- Mouse movement generally follows `Begin` (mouse-over) to `Change` (mouse
  movement) to `End` (mouse-leave).
- Touch input behaves somewhat similarly to mouse movement. `Begin` and `End`
  occur when the user starts or ends touching the screen, respectively. The
  same [InputObject](/docs/reference/engine/classes/InputObject.md) is used for the same touch point.
- Gamepad thumbstick controls will cause `Change` to occur each frame the
  position changes.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Begin` | 0 | Occurs when an [InputObject](/docs/reference/engine/classes/InputObject.md) starts to interact with the experience. For example, a mouse button down, a key down, or when the player begins touching the screen. |
| `Change` | 1 | Occurs each frame an [InputObject](/docs/reference/engine/classes/InputObject.md) has already begun interacting with the experience and part of its state is changing. For example, movement of the mouse position, a gamepad thumbstick movement, an analog gamepad trigger button change, or screen touch point change. |
| `End` | 2 | Occurs when an [InputObject](/docs/reference/engine/classes/InputObject.md) finishes interacting with the experience. For example, a mouse button up, a key up, or when the player stops touching the screen. |
| `Cancel` | 3 | A special circumstance state that indicates this input is no longer relevant, particularly with [ContextActionService](/docs/reference/engine/classes/ContextActionService.md). For example, binding two action-handling functions will cause the first to `Cancel` if an input was already in-progress when the second was bound. |
| `None` | 4 | A state that should never be seen in an experience; essentially just marks the end of the enum. |