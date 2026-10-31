---
name: ActionType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the outcome of a game action, such as winning, losing, or drawing."
---

# ActionType

Describes the outcome of a game action, such as winning, losing, or drawing.

**Type:** enum

## Description

Legacy enum historically used with the player-points and badge-award system to
classify game results. No current engine API property or method accepts or
returns this enum; it remains in the Luau reflection system for backward
compatibility.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Nothing` | 0 | No specific game action occurred. |
| `Pause` | 1 | The game or round was paused. |
| `Lose` | 2 | The player lost the game or round. |
| `Draw` | 3 | The game or round ended in a draw with no winner. |
| `Win` | 4 | The player won the game or round. |