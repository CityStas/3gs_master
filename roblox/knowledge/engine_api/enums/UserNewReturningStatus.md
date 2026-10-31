---
name: UserNewReturningStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes whether a player is new to the current experience or has played it before."
---

# UserNewReturningStatus

Describes whether a player is new to the current experience or has played it
before.

**Type:** enum

## Description

The `UserNewReturningStatus` enum describes whether a player is new to the
current experience or has played it before.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 0 | Segment data is unavailable. |
| `New` | 1 | The player is playing the experience for the first time. |
| `Returning` | 2 | The player has played the experience before. |