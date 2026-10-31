---
name: ExperienceActivationStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes whether a player is new, active, lapsed, or reactivated in the current experience."
---

# ExperienceActivationStatus

Describes whether a player is new, active, lapsed, or reactivated in the
current experience.

**Type:** enum

## Description

The `ExperienceActivationStatus` enum describes a player's activity status in
the current experience, based on the last 30 days.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 0 | Segment data is unavailable. |
| `New` | 1 | The player first played the experience within the last 30 days. |
| `Active` | 2 | The player played the experience in the last 30 days and is not `New` or `Reactivated`. |
| `Lapsed` | 3 | The player has not played the experience in the last 30 days. |
| `Reactivated` | 4 | The player returned to the experience within the last 30 days after being `Lapsed`. |