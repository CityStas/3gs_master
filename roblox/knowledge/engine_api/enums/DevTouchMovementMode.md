---
name: DevTouchMovementMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Overrides the movement mode of players who are playing on touch-enabled devices."
---

# DevTouchMovementMode

Overrides the movement mode of players who are playing on touch-enabled
devices.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `UserChoice` | 0 | Allows players to choose their desired control scheme from the in-experience menu. This is the default movement mode. |
| `Thumbstick` | 1 |  |
| `DPad` | 2 |  |
| `Thumbpad` | 3 |  |
| `ClickToMove` | 4 | The player's character will attempt to move to a location in the world when the player taps a location. |
| `Scriptable` | 5 | The player's character will not respond to default controls; any character movement must be defined in custom scripts. |
| `DynamicThumbstick` | 6 | The player's character is controlled with a virtual thumbstick that appears when they touch the lower portion of the screen. Jumping is controlled with a separate button. |