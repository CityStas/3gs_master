---
name: AnalyticsLogLevel
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the severity level of an analytics log event passed to AnalyticsService:FireLogEvent()."
---

# AnalyticsLogLevel

Specifies the severity level of an analytics log event passed to
[AnalyticsService:FireLogEvent()](/docs/reference/engine/classes/AnalyticsService.md).

**Type:** enum

## Description

This enum is used as an argument in [AnalyticsService:FireLogEvent()](/docs/reference/engine/classes/AnalyticsService.md) to
describe the error severity level.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Trace` | 0 | Trace is the noisiest level, rarely (if ever) enabled for a production app. |
| `Debug` | 1 | Used for debugging. |
| `Information` | 2 | Used for general informational messages that highlight progress or state changes during normal operation. |
| `Warning` | 3 | Used for warning. |
| `Error` | 4 | When functionality is unavailable or expectations broken. |
| `Fatal` | 5 | The most critical level, Fatal events demand immediate attention. |