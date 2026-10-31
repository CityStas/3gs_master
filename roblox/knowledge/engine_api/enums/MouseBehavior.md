---
name: MouseBehavior
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Sets the user's mouse behavior."
---

# MouseBehavior

Sets the user's mouse behavior.

**Type:** enum

## Description

Used with the [UserInputService.MouseBehavior](/docs/reference/engine/classes/UserInputService.md) property of
[UserInputService](/docs/reference/engine/classes/UserInputService.md) to set how the user's mouse behaves.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | The mouse moves freely around the user's screen. |
| `LockCenter` | 1 | The mouse is locked and cannot move from the center of the user's screen. |
| `LockCurrentPosition` | 2 | The mouse is locked and cannot move from its current position on the user's screen at the time of locking. |