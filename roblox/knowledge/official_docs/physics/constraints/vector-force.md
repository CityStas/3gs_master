---
title: "VectorForce"
url: /docs/en-us/physics/constraints/vector-force
last_updated: 2026-10-30T19:55:46Z
description: "The VectorForce constraint applies constant linear force on an assembly."
---

# VectorForce

> **Info:** For an overview on creating, visualizing, and simulating mover constraints, including `Class.VectorForce`, see [mover constraints](/docs/en-us/physics/mover-constraints.md). Also see [Roblox units](/docs/en-us/physics/units.md) to understand how Roblox units compare to metric units.

The `Class.VectorForce` constraint applies constant linear force on an assembly. The direction and strength of the force is determined by a `Datatype.Vector3` and can be relative to an attachment on the part, another attachment, or the world coordinate system.

> **Warning:** Because the `Class.VectorForce` constraint applies **constant** force and acceleration, very high speeds may result if no other forces are involved. If you want to maintain a more steady velocity over time, use a [LinearVelocity](/docs/en-us/physics/constraints/linear-velocity.md) constraint. Alternatively, if you only need **initial** velocity, set the `Class.BasePart.AssemblyLinearVelocity|AssemblyLinearVelocity` property directly on the assembly.
## Force location

By default, force is applied to the assembly at the location of `Class.Constraint.Attachment0|Attachment0`. Thus, if its center of mass is not aligned with the direction/point of force, torque will be applied as well. If desired, force can be focused at the center of mass by toggling on `Class.VectorForce.ApplyAtCenterOfMass|ApplyAtCenterOfMass`.

_ApplyAtCenterOfMass = **false**_

_ApplyAtCenterOfMass = **true**_

## Relativity

By default, force is applied relative to `Class.Constraint.Attachment0|Attachment0`. If the parent assembly rotates, the force will change direction to match the adjusted orientation of the attachment; visualize this behavior in how the thruster of a rocket pushes it forward, regardless of the rocket's rotation.

If `Class.VectorForce.RelativeTo|RelativeTo` is set to **World**, force will be applied in world coordinates, independent of the parent or attachment orientations; visualize this behavior as a directional force like the wind blowing against an object.

If `Class.VectorForce.RelativeTo|RelativeTo` is set to **Attachment1**, force will be applied relative to `Class.Constraint.Attachment1|Attachment1` and, if the attachment rotates, the force will change to match its orientation.

_RelativeTo = **Attachment0**_

_RelativeTo = **World**_
