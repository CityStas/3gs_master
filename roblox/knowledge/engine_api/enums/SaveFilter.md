---
name: SaveFilter
last_updated: 2026-10-30T19:55:54Z
type: enum
tags:
  - Deprecated
summary: "Used by DataModel.SavePlace to determine the type of save operation This enum determines which aspects of the current place are saved, based on the following options."
---

# SaveFilter

Used by [DataModel.SavePlace](/docs/reference/engine/classes/DataModel.md) to determine the type of save operation
This enum determines which aspects of the current place are saved, based on
the following options.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `SaveWorld` | 0 | Saves only the world-related data. |
| `SaveGame` | 1 | Saves only the game-related data. |
| `SaveAll` | 2 | Saves all data, including both world and game-related information. |