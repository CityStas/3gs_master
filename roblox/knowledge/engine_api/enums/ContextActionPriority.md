---
name: ContextActionPriority
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the priority of a context action."
---

# ContextActionPriority

Describes the priority of a context action.

**Type:** enum

## Description

`ContextActionPriority` specifies the relative priority of an action bound via
[ContextActionService:BindActionAtPriority()](/docs/reference/engine/classes/ContextActionService.md). When multiple actions are
bound to the same input, [ContextActionService](/docs/reference/engine/classes/ContextActionService.md) invokes them in
descending priority order — the action with the highest priority value runs
first and may sink the input before lower-priority actions receive it. The
three named levels map to the integer values `Low = 1000`, `Medium = 2000`,
and `High = 3000`; arbitrary integers are also accepted by
`BindActionAtPriority`. `Medium` is the default priority used by
[ContextActionService:BindAction()](/docs/reference/engine/classes/ContextActionService.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Low` | 1000 | The lowest named priority level (value 1000); an action at this level is invoked after `High` and `Medium` actions bound to the same input. |
| `Medium` | 2000 | The default priority level (value 2000); used automatically by [ContextActionService:BindAction()](/docs/reference/engine/classes/ContextActionService.md) and falls between `High` and `Low` in processing order. |
| `High` | 3000 | The highest named priority level (value 3000); an action at this level is invoked before `Medium` and `Low` actions bound to the same input. |