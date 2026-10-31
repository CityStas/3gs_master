---
title: "AlignOrientation"
url: /docs/en-us/physics/constraints/align-orientation
last_updated: 2026-10-30T19:55:46Z
description: "The AlignOrientation constraint applies torque to align two attachments, or to align one attachment with a goal orientation."
---

# AlignOrientation

> **Info:** For an overview on creating, visualizing, and simulating mover constraints, including `Class.AlignOrientation`, see [mover constraints](/docs/en-us/physics/mover-constraints.md). Also see [Roblox units](/docs/en-us/physics/units.md) to understand how Roblox units compare to metric units.

The `Class.AlignOrientation` constraint applies torque to align two attachments, or to align one attachment with a goal orientation. As indicated by the name, it only affects the **orientation** of the attachments, not their position (to align attachments **positionally**, see [AlignPosition](/docs/en-us/physics/constraints/align-position.md)).

> **Warning:** By default, the constraint only applies torque to `Class.Constraint.Attachment0|Attachment0`, although this behavior can be controlled through the constraint's [reactionary torque](#reactionary-torque).
## Affected axes

The axes affected by torque are controlled through the constraint's `Class.AlignOrientation.AlignType|AlignType` property. When set to `Enum.AlignType.AllAxes|AllAxes` (default), the constraint will apply torque about all 3 axes to achieve alignment. When set to `Enum.AlignType.PrimaryAxisParallel|PrimaryAxisParallel`, `Enum.AlignType.PrimaryAxisPerpendicular|PrimaryAxisPerpendicular`, or `Enum.AlignType.PrimaryAxisLookAt|PrimaryAxisLookAt`, torque will only occur when the **primary** axes become misaligned.

## Torque magnitude

You can configure the `Class.AlignOrientation` constraint to apply the maximum torque that constraints allow through the `Class.AlignOrientation.RigidityEnabled|RigidityEnabled` property. When `true`, the physics solver reacts as quickly as possible to complete the alignment. When `false`, the torque is determined by `Class.AlignOrientation.MaxTorque|MaxTorque`, `Class.AlignOrientation.MaxAngularVelocity|MaxAngularVelocity`, and `Class.AlignOrientation.Responsiveness|Responsiveness`.

## Reactionary torque

By default, the constraint only applies torque to `Class.Constraint.Attachment0|Attachment0` while `Class.Constraint.Attachment1|Attachment1` remains unaffected. If desired, torque can be applied to **both** attachments in **equal and opposite directions** by enabling `Class.AlignOrientation.ReactionTorqueEnabled|ReactionTorqueEnabled`.

## Attachment mode

The `Class.AlignOrientation.Mode|Mode` property specifies whether the constraint uses **one** or **two** attachments in calculating its goal. By default, this is `Enum.OrientationAlignmentMode.TwoAttachment|TwoAttachment`, meaning that the constraint attempts to match the orientation of `Class.Constraint.Attachment0|Attachment0` with the orientation of `Class.Constraint.Attachment1|Attachment1`, disregarding `Class.AlignOrientation.CFrame|CFrame`, `Class.AlignOrientation.PrimaryAxis|PrimaryAxis`, and `Class.AlignOrientation.SecondaryAxis|SecondaryAxis`.

If set to `Enum.OrientationAlignmentMode.OneAttachment|OneAttachment`, the constraint disregards `Class.Constraint.Attachment1|Attachment1` and attempts to match the orientation of `Class.Constraint.Attachment0|Attachment0` with the orientation of `Class.AlignOrientation.CFrame|CFrame`, or match the attachment's `Class.Attachment.Axis|Axis` and `Class.Attachment.SecondaryAxis|SecondaryAxis` with the constraint's `Class.AlignOrientation.PrimaryAxis|PrimaryAxis` and `Class.AlignOrientation.SecondaryAxis|SecondaryAxis` properties respectively.
