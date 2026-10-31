---
name: ActuatorRelativeTo
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the coordinate frame in which a mover constraint's directional properties are expressed."
---

# ActuatorRelativeTo

Determines the coordinate frame in which a mover constraint's directional
properties are expressed.

**Type:** enum

## Description

Determines the coordinate frame in which a mover constraint's directional
properties — such as force, velocity, or torque vectors — are interpreted.
Used by the [VectorForce.RelativeTo](/docs/reference/engine/classes/VectorForce.md), [LinearVelocity.RelativeTo](/docs/reference/engine/classes/LinearVelocity.md),
[Torque.RelativeTo](/docs/reference/engine/classes/Torque.md), and [AngularVelocity.RelativeTo](/docs/reference/engine/classes/AngularVelocity.md) properties,
as well as [AlignPosition.ForceRelativeTo](/docs/reference/engine/classes/AlignPosition.md). When set to
[Attachment0](/docs/reference/engine/enums/ActuatorRelativeTo.md) or
[Attachment1](/docs/reference/engine/enums/ActuatorRelativeTo.md), the direction rotates with the
referenced attachment's orientation; when set to
[World](/docs/reference/engine/enums/ActuatorRelativeTo.md), it remains fixed in world space.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Attachment0` | 0 | The directional property is interpreted in the local coordinate frame of [Attachment0](/docs/reference/engine/classes/Constraint.md), rotating with its parent part. |
| `Attachment1` | 1 | The directional property is interpreted in the local coordinate frame of [Attachment1](/docs/reference/engine/classes/Constraint.md), rotating with its parent part. |
| `World` | 2 | The directional property is interpreted in world-space coordinates, remaining constant regardless of part orientation. |