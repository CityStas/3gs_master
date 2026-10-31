---
name: DialogBehaviorType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether multiple people can use this dialog, or only one person at a time can use it."
---

# DialogBehaviorType

Controls whether multiple people can use this dialog, or only one person at a
time can use it.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `SinglePlayer` | 0 | Only one player can interact with this dialog at a time. The conversation between the player and dialog can be seen by all players. |
| `MultiplePlayers` | 1 | Multiple players can simultaneously interact with this dialog. The conversation between the player and the dialog cannot be seen by other players. |