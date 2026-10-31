---
name: AnalyticsProgressionStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "This enum is used as an argument in AnalyticsService:FirePlayerProgressionEvent() to describe the status of progression."
---

# AnalyticsProgressionStatus

This enum is used as an argument in
[AnalyticsService:FirePlayerProgressionEvent()](/docs/reference/engine/classes/AnalyticsService.md) to describe the status
of progression.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Default status. Used for an undefined status. |
| `Begin` | 1 | Indicates the beginning of progression. |
| `Complete` | 2 | Indicates the progression completed. |
| `Abandon` | 3 | Indicates the progression abandoned. |
| `Fail` | 4 | Indicates the progression failed. |