---
name: PlayerExitReason
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "An enum that specifies the reason for **Players.PlayerRemoving** signal."
---

# PlayerExitReason

An enum that specifies the reason for **Players.PlayerRemoving** signal.

**Type:** enum

## Description

Second argument in [Players.PlayerRemoving](/docs/reference/engine/classes/Players.md). Helps identify whether a
kick was caused by the Roblox platform or the Creator.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 0 | Catch-all for all other disconnect reasons. |
| `PlatformKick` | 1 | User was kicked by Roblox systems, such as being blocked while in a Private Server. |
| `CreatorKick` | 2 | Creator called **Player:Kick()** |