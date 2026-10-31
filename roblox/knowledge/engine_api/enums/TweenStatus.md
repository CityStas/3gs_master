---
name: TweenStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The completion status of a GuiObject tween function."
---

# TweenStatus

The completion status of a [GuiObject](/docs/reference/engine/classes/GuiObject.md) tween function.

**Type:** enum

## Description

Describes the completion status of a [GuiObject](/docs/reference/engine/classes/GuiObject.md) tween function.

Passed as an argument to the callback function provided to
[GuiObject:TweenPosition()](/docs/reference/engine/classes/GuiObject.md), [GuiObject:TweenSize()](/docs/reference/engine/classes/GuiObject.md), and
[GuiObject:TweenSizeAndPosition()](/docs/reference/engine/classes/GuiObject.md).

Not to be confused for [PlaybackState](/docs/reference/engine/enums/PlaybackState.md) which is used with
[TweenService](/docs/reference/engine/classes/TweenService.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Canceled` | 0 | The tween was cancelled before completion. |
| `Completed` | 1 | The Tween has successfully completed. |