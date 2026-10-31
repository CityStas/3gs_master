---
name: VelocityConstraintMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The velocity constraint mode property controls how the linear velocity of the attachment(s) is constrained."
---

# VelocityConstraintMode

The velocity constraint mode property controls how the linear velocity of the
attachment(s) is constrained.

**Type:** enum

## Description

The velocity constraint mode sets how the attachment velocity is constrained.
The velocity can be constrained to a line, a plane or a vector. See each mode
for more details.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Line` | 0 | The velocity component in the direction of the line is constrained to the specified value. The line direction is based on the [RelativeTo](/docs/reference/engine/classes/LinearVelocity.md) property:  - [Attachment0](/docs/reference/engine/enums/ActuatorRelativeTo.md) - The line direction is the   primary axis of [Attachment0](/docs/reference/engine/classes/Constraint.md). - [Attachment1](/docs/reference/engine/enums/ActuatorRelativeTo.md) - The line direction is the   primary axis of [Attachment1](/docs/reference/engine/classes/Constraint.md). - [World](/docs/reference/engine/enums/ActuatorRelativeTo.md) - The line direction must be specified. |
| `Plane` | 1 | The velocity components in the plane are constrained to the specified values. The plane tangents are based on the [RelativeTo](/docs/reference/engine/classes/LinearVelocity.md) property:  - [Attachment0](/docs/reference/engine/enums/ActuatorRelativeTo.md) - The plane tangents are the two   axes of [Attachment0](/docs/reference/engine/classes/Constraint.md). - [Attachment1](/docs/reference/engine/enums/ActuatorRelativeTo.md) - The plane tangents are the two   axes of [Attachment1](/docs/reference/engine/classes/Constraint.md). - [World](/docs/reference/engine/enums/ActuatorRelativeTo.md) - The two plane tangents must be   specified |
| `Vector` | 2 | The velocity components must be equal to the vector components specified. The coordinate system of the vector is based on the [RelativeTo](/docs/reference/engine/classes/LinearVelocity.md) property:  - [Attachment0](/docs/reference/engine/enums/ActuatorRelativeTo.md) - The vector components are in the   coordinate system defined by the axes of   [Attachment0](/docs/reference/engine/classes/Constraint.md). - [Attachment1](/docs/reference/engine/enums/ActuatorRelativeTo.md) - The vector components are in the   coordinate system defined by the axes of   [Attachment1](/docs/reference/engine/classes/Constraint.md). - [World](/docs/reference/engine/enums/ActuatorRelativeTo.md) - The coordinate system is in the world   and the vector components must be specified. |