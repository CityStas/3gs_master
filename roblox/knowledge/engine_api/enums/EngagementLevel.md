---
name: EngagementLevel
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes how many days a player played the current experience in the last 7 days, represented as a bucket."
---

# EngagementLevel

Describes how many days a player played the current experience in the last 7
days, represented as a bucket.

**Type:** enum

## Description

The `EngagementLevel` enum describes how many days a player played the current
experience in the last 7 days, represented as a bucket.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 0 | Segment data is unavailable. |
| `Inactive` | 1 | The player did not play the experience in the last 7 days. |
| `Low` | 2 | The player played the experience on 1 of the last 7 days. |
| `Medium` | 3 | The player played the experience on 2 or 3 of the last 7 days. |
| `High` | 4 | The player played the experience on 4 to 7 of the last 7 days. |