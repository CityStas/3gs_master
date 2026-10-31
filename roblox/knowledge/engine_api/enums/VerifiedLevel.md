---
name: VerifiedLevel
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the level of player verification required by Player:IsVerified()."
---

# VerifiedLevel

Specifies the level of player verification required by
[Player:IsVerified()](/docs/reference/engine/classes/Player.md).

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Low` | 0 | Requires the player to meet the low verification level or higher. This is the default value for [Player:IsVerified()](/docs/reference/engine/classes/Player.md). |
| `High` | 1 | Requires the player to meet the high verification level. |