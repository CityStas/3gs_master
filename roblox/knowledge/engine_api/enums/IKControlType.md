---
name: IKControlType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used on IKControl to specify their Type, to change their behavior."
---

# IKControlType

Used on [IKControl](/docs/reference/engine/classes/IKControl.md) to specify their [Type](/docs/reference/engine/classes/IKControl.md), to
change their behavior.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Transform` | 0 | It is a full 6-DoF constraint. Aligns the [EndEffector](/docs/reference/engine/classes/IKControl.md) [CFrame](/docs/reference/engine/datatypes/CFrame.md) to that of the [Target](/docs/reference/engine/classes/IKControl.md). It is the default value. |
| `Position` | 1 | Aligns the [EndEffector](/docs/reference/engine/classes/IKControl.md) position to that of the [Target](/docs/reference/engine/classes/IKControl.md) . |
| `Rotation` | 2 | Aligns the [EndEffector](/docs/reference/engine/classes/IKControl.md) rotation to that of the [Target](/docs/reference/engine/classes/IKControl.md). |
| `LookAt` | 3 | Moves and orients the whole chain to make the forward axis on the [EndEffector](/docs/reference/engine/classes/IKControl.md) point at a position in the world specified by [Target](/docs/reference/engine/classes/IKControl.md). |