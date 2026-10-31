---
name: AnalyticsProgressionType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the player's progression status in a level-progression event logged by AnalyticsService:LogProgressionEvent()."
---

# AnalyticsProgressionType

Specifies the player's progression status in a level-progression event logged
by [AnalyticsService:LogProgressionEvent()](/docs/reference/engine/classes/AnalyticsService.md).

**Type:** enum

## Description

Passed as the `status` argument to
[AnalyticsService:LogProgressionEvent()](/docs/reference/engine/classes/AnalyticsService.md) to indicate whether a player is
starting, completing, or failing a level attempt. The convenience methods
[AnalyticsService:LogProgressionStartEvent()](/docs/reference/engine/classes/AnalyticsService.md),
[AnalyticsService:LogProgressionCompleteEvent()](/docs/reference/engine/classes/AnalyticsService.md), and
[AnalyticsService:LogProgressionFailEvent()](/docs/reference/engine/classes/AnalyticsService.md) set this value
automatically; use [Custom](/docs/reference/engine/enums/AnalyticsProgressionType.md) for
progression events that fall outside the standard lifecycle.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Custom` | 0 | A custom progression status for events outside the standard start/fail/complete lifecycle. |
| `Start` | 1 | The player started the level attempt. |
| `Fail` | 2 | The player failed the level attempt. |
| `Complete` | 3 | The player completed the level successfully. |