---
title: "Torque"
url: /docs/en-us/physics/constraints/torque
last_updated: 2026-10-30T19:55:46Z
description: "The Torque constraint applies constant torque on an assembly from its center of mass."
---

# Torque

> **Info:** For an overview on creating, visualizing, and simulating mover constraints, including `Class.Torque`, see [mover constraints](/docs/en-us/physics/mover-constraints.md). Also see [Roblox units](/docs/en-us/physics/units.md) to understand how Roblox units compare to metric units.

A `Class.Torque` constraint applies constant torque on an assembly from its center of mass.

> **Warning:** Because the `Class.Torque` constraint applies **constant** torque and angular acceleration, very high speeds may result if no other forces are involved. If you want to maintain a more steady velocity over time, use an [AngularVelocity](/docs/en-us/physics/constraints/angular-velocity.md) constraint. Alternatively, if you only need **initial** velocity, set the `Class.BasePart.AssemblyAngularVelocity|AssemblyAngularVelocity` property directly on the assembly.
## Relativity

By default, torque is applied relative to `Class.Constraint.Attachment0|Attachment0`. If the parent assembly rotates, the torque will change direction to match the adjusted orientation of the attachment.

If `Class.Torque.RelativeTo|RelativeTo` is set to **World**, torque will be applied in world coordinates, independent of the parent or attachment orientations.

If `Class.Torque.RelativeTo|RelativeTo` is set to **Attachment1**, torque will be applied relative to `Class.Constraint.Attachment1|Attachment1` and, if the attachment rotates, change to match its orientation.

_RelativeTo = **Attachment0**_

_RelativeTo = **World**_
