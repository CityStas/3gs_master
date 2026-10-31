---
name: PreferredInput
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "This enum is used with UserInputService.PreferredInput to indicate the primary input type a player is likely using."
---

# PreferredInput

This enum is used with [UserInputService.PreferredInput](/docs/reference/engine/classes/UserInputService.md) to indicate the
primary input type a player is likely using.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `KeyboardAndMouse` | 0 | The player has connected or most recently interacted with a keyboard or mouse. |
| `Gamepad` | 1 | The player has connected or most recently interacted with a gamepad. |
| `Touch` | 2 | The player's device has touch capability and no other input method is available or was recently interacted with. |
| `MicroGamepad` | 3 | The player has connected or most recently interacted with a gamepad without a thumbstick (for example, a TV remote or another limited-input gamepad), and no standard gamepad is currently connected. |