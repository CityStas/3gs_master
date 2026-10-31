---
name: TweenInfo
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Stores parameters for Tweens."
---

# TweenInfo

Stores parameters for [Tweens](/docs/reference/engine/classes/Tween.md).

**Type:** datatype

## Description

The [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) data type stores parameters for
[TweenService:Create()](/docs/reference/engine/classes/TweenService.md) to specify the behavior of the tween. The
properties of a [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) cannot be written to after its creation.

## Constructors

### TweenInfo.new

**Signature:** `TweenInfo.new(time?: number, easingStyle?: EasingStyle, easingDirection?: EasingDirection, repeatCount?: number, reverses?: bool, delayTime?: number)`

Creates a new [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) from the provided parameters. This
constructor raises an error if `easingStyle` is [EasingStyle.Bezier](/docs/reference/engine/enums/EasingStyle.md)
or [EasingStyle.Spring](/docs/reference/engine/enums/EasingStyle.md).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `time` | `number` | `1` | Duration for the tween, in seconds. |
| `easingStyle` | `EasingStyle` | `Enum.EasingStyle.Quad` | Easing style for the tween. |
| `easingDirection` | `EasingDirection` | `Enum.EasingDirection.Out` | The direction in which the tween executes. |
| `repeatCount` | `number` | `0` | Number of times the tween should repeat. `-1` repeats indefinitely. |
| `reverses` | `bool` | `false` | Whether the tween should reverse to the starting values once it reaches its targets. |
| `delayTime` | `number` | `0` | Time of delay until the tween begins, in seconds. |

## Properties

### TweenInfo.EasingDirection

**Type:** `EasingDirection`

The direction in which the tween executes.

### TweenInfo.Time

**Type:** `number`

Duration of the tween, in seconds.

### TweenInfo.DelayTime

**Type:** `number`

Time of delay until the tween begins, in seconds.

### TweenInfo.RepeatCount

**Type:** `number`

Number of times the tween repeats. `-1` indicates indefinite repetition.

### TweenInfo.EasingStyle

**Type:** `EasingStyle`

The style in which the tween executes.

### TweenInfo.Reverses

**Type:** `bool`

Whether or not the tween interpolates in reverse tween once the initial
tween completes.