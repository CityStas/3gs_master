---
name: GameAvatarType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Value indicating which type of avatar an experience uses."
---

# GameAvatarType

Value indicating which type of avatar an experience uses.

**Type:** enum

## Description

The value of this Enum indicates which type of avatar an experience uses. Some
experiences may specify explicitly R6/R15, while some will allow the player's
choice of avatar to be used.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `R6` | 0 | The R6 character rig. |
| `R15` | 1 | The R15 character rig. |
| `PlayerChoice` | 2 | The rig (either R6 or [R15](/docs/en-us/avatar/character-bodies/specifications.md#rigging) determined by a player's character settings set on the website in the 'Edit Avatar' page. |