---
name: TeleportResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the result of a teleport."
---

# TeleportResult

Describes the result of a teleport.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Success` | 0 | The teleport was successful. |
| `Failure` | 1 | The teleport failed for an unknown reason. |
| `GameNotFound` | 2 | The game that this player attempted to teleport to could not be found. |
| `GameEnded` | 3 | The game that this player attempted to teleport to has ended. |
| `GameFull` | 4 | The game that this player attempted to teleport to is full. |
| `Unauthorized` | 5 | The player is not authorized to complete this teleport. |
| `Flooded` | 6 | Too many teleport requests have been made recently. |
| `IsTeleporting` | 7 | The player is currently being teleported. |