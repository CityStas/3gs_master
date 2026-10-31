---
title: "AngularVelocity"
url: /docs/en-us/physics/constraints/angular-velocity
last_updated: 2026-10-30T19:55:46Z
description: "The AngularVelocity constraint applies torque on an assembly to maintain a constant angular velocity."
---

# AngularVelocity

> **Info:** For an overview on creating, visualizing, and simulating mover constraints, including `Class.AngularVelocity`, see [mover constraints](/docs/en-us/physics/mover-constraints.md). Also see [Roblox units](/docs/en-us/physics/units.md) to understand how Roblox units compare to metric units.

An `Class.AngularVelocity` constraint applies torque on an assembly to maintain a constant angular velocity.

> **Warning:** The `Class.AngularVelocity` constraint applies torque that attempts to maintain a **constant** angular velocity. If you want to control the amount of torque applied, use a [Torque](/docs/en-us/physics/constraints/torque.md) constraint. Alternatively, if you only need **initial** angular velocity, set the `Class.BasePart.AssemblyAngularVelocity|AssemblyAngularVelocity` method directly on the assembly.
## Relativity

Application of velocity can be controlled through the constraint's `Class.AngularVelocity.RelativeTo|RelativeTo` property. If set to `Enum.ActuatorRelativeTo|World`, the angular velocity vector is used as is. If set to `Enum.ActuatorRelativeTo|Attachment1` and the constraint's `Class.Constraint.Attachment1|Attachment1` property is set to another attachment, the angular velocity will be affected by that of the other attachment as seen by how the upper-left red part's velocity affects the attached blue part's velocity.

_RelativeTo = **World**_

_RelativeTo = **Attachment1**_

> **Info:** Setting `Class.AngularVelocity.RelativeTo|RelativeTo` to `Enum.ActuatorRelativeTo|Attachment1` also exposes the `Class.AngularVelocity.ReactionTorqueEnabled|ReactionTorqueEnabled` property.
