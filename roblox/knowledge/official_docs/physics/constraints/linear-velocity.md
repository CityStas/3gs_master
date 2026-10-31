---
title: "LinearVelocity"
url: /docs/en-us/physics/constraints/linear-velocity
last_updated: 2026-10-30T19:55:46Z
description: "The LinearVelocity constraint applies force on an assembly to maintain a constant velocity along a 3D vector, line, or 2D plane."
---

# LinearVelocity

> **Info:** For an overview on creating, visualizing, and simulating mover constraints, including `Class.LinearVelocity`, see [mover constraints](/docs/en-us/physics/mover-constraints.md). Also see [Roblox units](/docs/en-us/physics/units.md) to understand how Roblox units compare to metric units.

A `Class.LinearVelocity` constraint applies force on an assembly to maintain a constant velocity. It can be set to apply force along a `Datatype.Vector3`, line, or 2D plane.

> **Warning:** The `Class.LinearVelocity` constraint applies a force that attempts to maintain a **constant** linear velocity. If you want to control the amount of force applied, use a [VectorForce](/docs/en-us/physics/constraints/vector-force.md) constraint. Alternatively, if you only need **initial** linear velocity, set the `Class.BasePart.AssemblyLinearVelocity|AssemblyLinearVelocity` property directly on the assembly.
## Relativity

Application of velocity can be controlled through the constraint's `Class.LinearVelocity.RelativeTo|RelativeTo` property. If set to `Enum.ActuatorRelativeTo|World`, force will be applied in world coordinates, independent of the parent or attachment orientations. If set to `Enum.ActuatorRelativeTo|Attachment0` or `Enum.ActuatorRelativeTo|Attachment1`, force will be applied relative to `Class.Constraint.Attachment0|Attachment0` or `Class.Constraint.Attachment1|Attachment1` respectively.

_RelativeTo = **World**_

_RelativeTo = **Attachment0**_
