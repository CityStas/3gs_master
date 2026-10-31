---
name: PlayerPlatformSpenderStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes a player's platform-wide spender status bucket."
---

# PlayerPlatformSpenderStatus

Describes a player's platform-wide spender status bucket.

**Type:** enum

## Description

The `PlayerPlatformSpenderStatus` enum describes a player's platform-wide
spender status bucket.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 0 | Segment data is unavailable. |
| `Active` | 1 | The player is an active platform spender. |
| `OtherPayer` | 2 | The player is not an active platform spender, including players who have never spent. |