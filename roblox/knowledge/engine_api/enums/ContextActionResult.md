---
name: ContextActionResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes whether a contextual action should sink or pass input events."
---

# ContextActionResult

Describes whether a contextual action should sink or pass input events.

**Type:** enum

## Description

`ContextActionResult` controls the behavior of multiple bound actions. It
gives the option of controlling whether or not a bound action should sink or
pass the input event, meaning other things (including other bound actions) can
process it.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Sink` | 0 | If `functionToBind` from [ContextActionService:BindAction()](/docs/reference/engine/classes/ContextActionService.md) returns [ContextActionResult.Sink](/docs/reference/engine/enums/ContextActionResult.md), the input event will stop at that function and no other bound actions under it will be processed. This is the default behavior if `functionToBind` does not return anything or yields in any way. |
| `Pass` | 1 | If `functionToBind` from [ContextActionService:BindAction()](/docs/reference/engine/classes/ContextActionService.md) returns [ContextActionResult.Pass](/docs/reference/engine/enums/ContextActionResult.md), the input event is considered to have not been handled by `functionToBind` and will continue being passed to actions bound to the same input type. |