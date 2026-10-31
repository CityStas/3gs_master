---
name: DevComputerMovementMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Sets the movement mode of players who are playing on computers."
---

# DevComputerMovementMode

Sets the movement mode of players who are playing on computers.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `UserChoice` | 0 | Allows players to choose their desired control scheme from the in-experience menu. This is the default movement mode. |
| `KeyboardMouse` | 1 | The player's character will be controlled using the keyboard and mouse. |
| `ClickToMove` | 2 | Players can only move through the experience by clicking a target location. The player's character will automatically jump when reaching a surmountable obstacle/gap while moving to the click destination. |
| `Scriptable` | 3 | Disables all default controls and allows you to script your own control scheme. |