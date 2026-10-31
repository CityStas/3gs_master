---
name: AnimationNodeBlendMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies how an AnimationNodeType.OneShotNode combines its one-shot pose with its base pose."
---

# AnimationNodeBlendMode

Specifies how an [AnimationNodeType.OneShotNode](/docs/reference/engine/enums/AnimationNodeType.md) combines its one-shot
pose with its base pose.

**Type:** enum

## Description

Used by the [AnimationNodeType.OneShotNode](/docs/reference/engine/enums/AnimationNodeType.md) to choose the blend operation
applied to its one-shot input as it layers over the base input. Mirrors the
behavior of the [AnimationNodeType.OverNode](/docs/reference/engine/enums/AnimationNodeType.md),
[AnimationNodeType.AddNode](/docs/reference/engine/enums/AnimationNodeType.md), and [AnimationNodeType.SubtractNode](/docs/reference/engine/enums/AnimationNodeType.md)
nodes.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Over` | 0 | Composites the one-shot pose on top of the base pose, replacing it by the current blend weight. |
| `Add` | 1 | Adds the one-shot pose to the base pose as an additive layer scaled by the current blend weight. |
| `Subtract` | 2 | Subtracts the one-shot pose from the base pose scaled by the current blend weight. |