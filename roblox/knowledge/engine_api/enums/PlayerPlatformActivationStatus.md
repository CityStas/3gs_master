---
name: PlayerPlatformActivationStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes whether a player is new, active, lapsed, or reactivated on Roblox."
---

# PlayerPlatformActivationStatus

Describes whether a player is new, active, lapsed, or reactivated on Roblox.

**Type:** enum

## Description

The `PlayerPlatformActivationStatus` enum describes a player's platform-wide
activity status on Roblox, based on the last 60 days.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 0 | Segment data is unavailable. |
| `New` | 1 | The player signed up for Roblox within the last 60 days. |
| `Active` | 2 | The player played on Roblox in the last 60 days and is not `New` or `Reactivated`. |
| `Lapsed` | 3 | The player has not played on Roblox in the last 60 days. |
| `Reactivated` | 4 | The player returned to Roblox within the last 60 days after being `Lapsed`. |