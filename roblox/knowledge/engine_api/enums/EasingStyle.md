---
name: EasingStyle
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Enum used with TweenInfo.new to control the motion of a Tween."
---

# EasingStyle

Enum used with [TweenInfo.new](/docs/reference/engine/datatypes/TweenInfo.md) to control the motion of a
[Tween](/docs/reference/engine/classes/Tween.md).

**Type:** enum

## Description

These enum values are passed to [TweenInfo.new()](/docs/reference/engine/datatypes/TweenInfo.md) to
control the motion of a [Tween](/docs/reference/engine/classes/Tween.md). The following graphs reflect easing
styles for [Enum.EasingDirection.In](/docs/reference/engine/enums/EasingDirection.md). For graphs
reflecting [Enum.EasingDirection.Out](/docs/reference/engine/enums/EasingDirection.md) and
[Enum.EasingDirection.InOut](/docs/reference/engine/enums/EasingDirection.md), see
[UI&nbsp;Animations](/docs/en-us/ui/animation.md#style).

![Graphs of EasingStyle variations with an 'In' EasingDirection.](/assets/engine-api/enums/EasingStyle/Easing-Styles-In.png)

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Linear` | 0 | Moves at a constant speed. |
| `Sine` | 1 | Speed is determined by a sine wave for a gentle easing motion. |
| `Back` | 2 | Slightly overshoots the target, then backs into place. |
| `Quad` | 3 | Similar to `Sine` but with a slightly sharper curve based on quadratic interpolation. |
| `Quart` | 4 | Similar to `Cubic` but with an even sharper curve based on quartic interpolation. |
| `Quint` | 5 | Similar to `Quart` but with an even sharper curve based on quintic interpolation. |
| `Bounce` | 6 | Bounces backwards multiple times after reaching the target, before eventually settling. |
| `Elastic` | 7 | Moves as if attached to a rubber band, overshooting the target several times. |
| `Exponential` | 8 | The sharpest curve based on exponential interpolation. |
| `Circular` | 9 | Follows a circular arc, such that acceleration is more sudden and deceleration more gradual versus `Quint` or `Exponential`. |
| `Cubic` | 10 | Similar to `Quad` but with a slightly sharper curve based on cubic interpolation. |