---
name: PlaybackState
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the current state of a Tween in its Tween.PlaybackState property."
---

# PlaybackState

Describes the current state of a [Tween](/docs/reference/engine/classes/Tween.md) in its
[Tween.PlaybackState](/docs/reference/engine/classes/Tween.md) property.

**Type:** enum

## Description

Describes the current playback state of a [Tween](/docs/reference/engine/classes/Tween.md), accessible via its
[TweenBase.PlaybackState](/docs/reference/engine/classes/TweenBase.md) property. The state advances through a defined
lifecycle: a newly created tween begins in `Begin`; calling
[TweenBase:Play()](/docs/reference/engine/classes/TweenBase.md) moves it to `Delayed` (when
[TweenInfo.DelayTime](/docs/reference/engine/datatypes/TweenInfo.md) is greater than `0`) or directly to `Playing`;
from `Playing` the tween can be suspended (`Paused`), stopped early
(`Cancelled`), or reach its natural end (`Completed`). The
[TweenBase.Completed](/docs/reference/engine/classes/TweenBase.md) event fires when the state transitions to either
`Completed` or `Cancelled`.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Begin` | 0 | The tween has been created, but has yet to be played. After exiting this state, the tween never enters it again. |
| `Delayed` | 1 | The tween is waiting for the duration specified in its [TweenInfo.DelayTime](/docs/reference/engine/datatypes/TweenInfo.md). After the delay elapses, the tween plays. |
| `Playing` | 2 | The tween is currently in progress. |
| `Paused` | 3 | The tween is paused in the middle of playing. |
| `Completed` | 4 | The tween completed successfully. |
| `Cancelled` | 5 | The tween was cancelled before completion. |