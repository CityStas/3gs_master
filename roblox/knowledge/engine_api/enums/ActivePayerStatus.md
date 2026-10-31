---
name: ActivePayerStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes a player's payer status bucket for the current experience."
---

# ActivePayerStatus

Describes a player's payer status bucket for the current experience.

**Type:** enum

## Description

The `ActivePayerStatus` enum describes a player's payer status bucket for the
current experience.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 0 | Segment data is unavailable. |
| `Never` | 1 | The player has not made a qualifying purchase in the experience. |
| `Lapsed` | 2 | The player has previously spent in the experience but is not currently an active payer. |
| `Casual50Percent` | 3 | The player is in the casual payer bucket for the experience. |
| `Intermediate35Percent` | 4 | The player is in the intermediate payer bucket for the experience. |
| `Top15Percent` | 5 | The player is in the top payer bucket for the experience. |