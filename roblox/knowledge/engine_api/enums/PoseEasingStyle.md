---
name: PoseEasingStyle
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the interpolation curve used when blending between keyframe Poses in a KeyframeSequence."
---

# PoseEasingStyle

Specifies the interpolation curve used when blending between keyframe
[Poses](/docs/reference/engine/classes/Pose.md) in a [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md).

**Type:** enum

## Description

Controls how a [Pose](/docs/reference/engine/classes/Pose.md) transitions from one keyframe to the next in a
[KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md). The value is set via the [Pose.EasingStyle](/docs/reference/engine/classes/Pose.md)
property, which defaults to [PoseEasingStyle.Linear](/docs/reference/engine/enums/PoseEasingStyle.md). For asymmetric
styles such as [PoseEasingStyle.Elastic](/docs/reference/engine/enums/PoseEasingStyle.md), [PoseEasingStyle.Bounce](/docs/reference/engine/enums/PoseEasingStyle.md),
and [PoseEasingStyle.CubicV2](/docs/reference/engine/enums/PoseEasingStyle.md), the direction of the curve is further
controlled by [PoseEasingDirection](/docs/reference/engine/enums/PoseEasingDirection.md). [PoseEasingStyle.Cubic](/docs/reference/engine/enums/PoseEasingStyle.md) is a
legacy alias with a known direction-reversal bug between the Animation Editor
and runtime; use [PoseEasingStyle.CubicV2](/docs/reference/engine/enums/PoseEasingStyle.md) for all new work.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Linear` | 0 | Poses interpolate linearly between keyframes. |
| `Constant` | 1 | Poses do not interpolate but snap to the keyframe indicated by the [PoseEasingDirection](/docs/reference/engine/enums/PoseEasingDirection.md). |
| `Elastic` | 2 | Pose interpolation overshoots like an elastic curve. |
| `Cubic` | 3 | Deprecated - Use [PoseEasingStyle.CubicV2](/docs/reference/engine/enums/PoseEasingStyle.md). Pose interpolation is a cubic curve between keyframes based on the [PoseEasingDirection](/docs/reference/engine/enums/PoseEasingDirection.md). |
| `Bounce` | 4 | Pose interpolation produces a bounce-like effect between keyframes. |
| `CubicV2` | 5 | Pose interpolation is a cubic curve between keyframes based on [PoseEasingDirection](/docs/reference/engine/enums/PoseEasingDirection.md). |