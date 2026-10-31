---
title: "AlignPosition"
url: /docs/en-us/physics/constraints/align-position
last_updated: 2026-10-30T19:55:46Z
description: "The AlignPosition constraint applies force to move two attachments together, or to move one attachment to a goal position."
---

# AlignPosition

> **Info:** For an overview on creating, visualizing, and simulating mover constraints, including `Class.AlignPosition`, see [mover constraints](/docs/en-us/physics/mover-constraints.md). Also see [Roblox units](/docs/en-us/physics/units.md) to understand how Roblox units compare to metric units.

An `Class.AlignPosition` constraint applies force to move two attachments together, or to move one attachment to a goal position. As indicated by the name, it only affects the **position** of the attachments, not their orientation (to align attachments by **orientation**, see [AlignOrientation](/docs/en-us/physics/constraints/align-orientation.md)).

> **Warning:** By default, the constraint only applies force to `Class.Constraint.Attachment0|Attachment0`, although this behavior can be controlled through the constraint's [reactionary force](#reactionary-force).
## Force location

By default, force is applied to the parent of `Class.Constraint.Attachment0|Attachment0` at that attachment's location, meaning that if the parent's center of mass is not aligned with the direction of the force, torque will be applied as well as force. Alternatively, force can be applied to the parents' center of mass by toggling on `Class.AlignPosition.ApplyAtCenterOfMass|ApplyAtCenterOfMass`.

## Force magnitude

You can configure the `Class.AlignPosition` constraint to apply the maximum force that constraints allow through the `Class.AlignPosition.RigidityEnabled|RigidityEnabled` property. When `true`, the physics solver reacts as quickly as possible to complete the alignment. When `false`, the force is determined by `Class.AlignPosition.MaxForce|MaxForce`, `Class.AlignPosition.MaxVelocity|MaxVelocity`, and `Class.AlignPosition.Responsiveness|Responsiveness`.

## Reactionary force

By default, the constraint only applies force to `Class.Constraint.Attachment0|Attachment0` while `Class.Constraint.Attachment1|Attachment1` remains unaffected. If desired, force can be applied to **both** attachments in **equal and opposite directions** by enabling `Class.AlignPosition.ReactionForceEnabled|ReactionForceEnabled`.

## Attachment mode

The `Class.AlignPosition.Mode|Mode` property specifies whether the constraint uses **one** or **two** attachments in calculating its goal. By default, this is `Enum.PositionAlignmentMode.TwoAttachment|TwoAttachment`, meaning that the constraint disregards `Class.AlignPosition.Position|Position` and attempts to move `Class.Constraint.Attachment0|Attachment0` to the position of `Class.Constraint.Attachment1|Attachment1`. If set to `Enum.PositionAlignmentMode.OneAttachment|OneAttachment`, the constraint disregards `Class.Constraint.Attachment1|Attachment1` and attempts to move `Class.Constraint.Attachment0|Attachment0` to `Class.AlignPosition.Position|Position`.
