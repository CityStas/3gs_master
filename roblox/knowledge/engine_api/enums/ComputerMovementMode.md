---
name: ComputerMovementMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The computer movement type in-use by the client."
---

# ComputerMovementMode

The computer movement type in-use by the client.

**Type:** enum

## Description

Describes the movement control scheme currently active for the local player on
a computer. This value is read from
[UserGameSettings.ComputerMovementMode](/docs/reference/engine/classes/UserGameSettings.md) and reflects the scheme in use
at runtime, whether chosen by the player or enforced by the developer via
[StarterPlayer.DevComputerMovementMode](/docs/reference/engine/classes/StarterPlayer.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | The movement mode has not been explicitly set and behaves identically to `KeyboardMouse`. |
| `KeyboardMouse` | 1 | The player moves their character using keyboard keys and steers the camera with the mouse. |
| `ClickToMove` | 2 | The player moves their character by clicking a destination in the game world; the character automatically navigates there and jumps over surmountable obstacles. |