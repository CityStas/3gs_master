---
title: "Hinge"
url: /docs/en-us/physics/constraints/hinge
last_updated: 2026-10-30T19:55:46Z
description: "HingeConstraint allows its two attachments to rotate about one axis, with optional assigned power for motor or servo behavior."
---

# Hinge

> **Info:** For an overview on creating, visualizing, and simulating mechanical constraints, including `Class.HingeConstraint`, see [Mechanical constraints](/docs/en-us/physics/mechanical-constraints.md). Also see [Roblox units](/docs/en-us/physics/units.md) to understand how Roblox units compare to metric units.

A `Class.HingeConstraint` allows its two attachments to rotate about one axis, forcing them into the same position and **X** axis alignment. This constraint can also be powered to behave like a [motor](#angular-power) or [servo](#angular-power), and you can set limits to restrict the hinge's rotational range.

> **Info:** Orientation of a hinge's attachments affects how it rotates. To ensure rotation occurs around the desired axis, each attachment's `Class.Attachment.Axis|Axis`, visualized by the yellow arrow, should point in the same direction.
### Angular power

If a hinge's `Class.HingeConstraint.ActuatorType|ActuatorType` is set to `Enum.ActuatorType|Motor`, it attempts to rotate the attachments with the goal of reaching its `Class.HingeConstraint.AngularVelocity|AngularVelocity`. You can further control this rotation through both `Class.HingeConstraint.MotorMaxAcceleration|MotorMaxAcceleration` and `Class.HingeConstraint.MotorMaxTorque|MotorMaxTorque`.

If a hinge's `Class.HingeConstraint.ActuatorType|ActuatorType` is set to `Enum.ActuatorType|Servo`, it attempts to rotate to an angle specified by `Class.HingeConstraint.TargetAngle|TargetAngle`. This rotation is controlled by both `Class.HingeConstraint.AngularSpeed|AngularSpeed` and `Class.HingeConstraint.ServoMaxTorque|ServoMaxTorque`.

_ActuatorType = **Motor**_

_ActuatorType = **Servo**_

### Limits

You can set limits to restrict the rotation of a hinge, useful for mechanisms like doors which should only swing open or closed within a set range. Enabling the `Class.HingeConstraint.LimitsEnabled|LimitsEnabled` property exposes the `Class.HingeConstraint.LowerAngle|LowerAngle` and `Class.HingeConstraint.UpperAngle|UpperAngle` limits, as well as `Class.HingeConstraint.Restitution|Restitution` which defines the elasticity of the attachments when they reach either limit.
