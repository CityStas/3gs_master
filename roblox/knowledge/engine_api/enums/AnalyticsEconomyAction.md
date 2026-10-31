---
name: AnalyticsEconomyAction
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the type of economic transaction in AnalyticsService:FireInGameEconomyEvent()."
---

# AnalyticsEconomyAction

Describes the type of economic transaction in
[AnalyticsService:FireInGameEconomyEvent()](/docs/reference/engine/classes/AnalyticsService.md).

**Type:** enum

## Description

This enum is used as an argument in
[AnalyticsService:FireInGameEconomyEvent()](/docs/reference/engine/classes/AnalyticsService.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Default action. Used for an undefined Action. |
| `Acquire` | 1 | Indicates the acquisition of an in game resource. For example, a player acquires virtual currency by completing a specific in game task. |
| `Spend` | 2 | Indicates the spending or loss of an in game resource. For example, a player spends virtual currency to acquire a new item. |