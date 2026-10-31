---
name: IKCollisionsMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls which parts in the workspace participate in collision resolution when WorldRoot:IKMoveTo() drives a part toward a target CFrame."
---

# IKCollisionsMode

Controls which parts in the workspace participate in collision resolution when
[WorldRoot:IKMoveTo()](/docs/reference/engine/classes/WorldRoot.md) drives a part toward a target [CFrame](/docs/reference/engine/datatypes/CFrame.md).

**Type:** enum

## Description

Controls which parts in the workspace participate in collision resolution when
[WorldRoot:IKMoveTo()](/docs/reference/engine/classes/WorldRoot.md) drives a part toward a target [CFrame](/docs/reference/engine/datatypes/CFrame.md)
via inverse kinematics.

The three [IKCollisionsMode](/docs/reference/engine/enums/IKCollisionsMode.md) values offer a spectrum of collision
fidelity. [IKCollisionsMode.NoCollisions](/docs/reference/engine/enums/IKCollisionsMode.md) ignores the rest of the
workspace and moves only the mechanism being dragged (fastest, most
permissive). [IKCollisionsMode.OtherMechanismsAnchored](/docs/reference/engine/enums/IKCollisionsMode.md) keeps the dragged
mechanism physically correct against the scene but treats other objects as
immovable anchors. [IKCollisionsMode.IncludeContactedMechanisms](/docs/reference/engine/enums/IKCollisionsMode.md) lets the
dragged mechanism push unanchored objects, so the entire contacted set
participates in resolution.

[WorldRoot:IKMoveTo()](/docs/reference/engine/classes/WorldRoot.md) defaults to
[IKCollisionsMode.OtherMechanismsAnchored](/docs/reference/engine/enums/IKCollisionsMode.md) when no collisions mode is
supplied.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `NoCollisions` | 0 | Only the part and any parts directly joined to it via joints/[constraints](/docs/reference/engine/classes/Constraint.md) will be involved in the resolution; everything else in the workspace will be treated as though it doesn't exist. |
| `OtherMechanismsAnchored` | 1 | Only the part and any parts directly joined to it via joints/[constraints](/docs/reference/engine/classes/Constraint.md) will be moved during resolution, but they will collide with other objects in the workspace. |
| `IncludeContactedMechanisms` | 2 | The part, any parts directly joined to it via joints/[constraints](/docs/reference/engine/classes/Constraint.md), and any parts which it comes into contact with during the solve will be moved during the resolution. That is, the moved parts will be allowed to "push" other unanchored parts in the workspace out of the way in order to get to the target position. |