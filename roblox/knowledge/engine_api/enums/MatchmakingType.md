---
name: MatchmakingType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used with DataModel.MatchmakingType to represent how players in the server are handled by matchmaking."
---

# MatchmakingType

Used with [DataModel.MatchmakingType](/docs/reference/engine/classes/DataModel.md) to represent how players in the
server are handled by matchmaking.

**Type:** enum

## Description

This enum is used with [DataModel.MatchmakingType](/docs/reference/engine/classes/DataModel.md) to represent how
players in the server are handled by matchmaking.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 1 | Includes desktop, mobile, cross-play enabled players, etc. |
| `XboxOnly` | 2 | Xbox players with cross-play disabled. |
| `PlayStationOnly` | 3 | PlayStation players with cross-play disabled. |