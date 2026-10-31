---
name: AgeCheckStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates whether a player has completed age verification."
---

# AgeCheckStatus

Indicates whether a player has completed age verification.

**Type:** enum

## Description

Result of a player's age verification check. Used by
[Player.AgeChecked](/docs/reference/engine/classes/Player.md), which defaults to [AgeCheckStatus.Unchecked](/docs/reference/engine/enums/AgeCheckStatus.md)
and transitions to [AgeCheckStatus.Checked](/docs/reference/engine/enums/AgeCheckStatus.md) when the player completes the
age verification flow from [Player:PromptAgeCheck()](/docs/reference/engine/classes/Player.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unchecked` | 0 | The player has not yet completed age verification. |
| `Checked` | 1 | The player has successfully completed age verification. |