---
title: "Cylindrical"
url: /docs/en-us/physics/constraints/cylindrical
last_updated: 2026-10-30T19:55:46Z
description: "CylindricalConstraint allows its attachments to slide along one axis and rotate about another axis, with optional assigned angular and/or linear power."
---

# Cylindrical

> **Info:** For an overview on creating, visualizing, and simulating mechanical constraints, including `Class.CylindricalConstraint`, see [Mechanical constraints](/docs/en-us/physics/mechanical-constraints.md). Also see [Roblox units](/docs/en-us/physics/units.md) to understand how Roblox units compare to metric units.

A `Class.CylindricalConstraint` allows its attachments to slide along one axis and rotate about another axis. This constraint, along with a [SpringConstraint](/docs/en-us/physics/constraints/spring.md), is ideal for building vehicle suspensions where the wheel shock can slide up and down while the wheel itself spins. This constraint can also be powered in both an [angular](#angular-power) and [linear](#linear-power) manner.

> **Info:** Orientation of the attachments affects how the cylindrical aspect will rotate. To ensure rotation occurs around the desired axis, each attachment's `Class.Attachment.Axis|Axis` and `Class.Attachment.SecondaryAxis|SecondaryAxis`, visualized by the yellow and orange arrows, should point in the same direction.
## Angular power

If a cylindrical's `Class.CylindricalConstraint.AngularActuatorType|AngularActuatorType` is set to `Enum.ActuatorType|Motor`, it attempts to rotate the attachments with the goal of reaching its `Class.CylindricalConstraint.AngularVelocity|AngularVelocity`. You can further control this rotation through both `Class.CylindricalConstraint.MotorMaxAngularAcceleration|MotorMaxAngularAcceleration` and `Class.CylindricalConstraint.MotorMaxTorque|MotorMaxTorque`.

If a cylindrical's `Class.CylindricalConstraint.AngularActuatorType|AngularActuatorType` is set to `Enum.ActuatorType|Servo`, it attempts to rotate to an angle specified by `Class.CylindricalConstraint.TargetAngle|TargetAngle`. This rotation is controlled by `Class.CylindricalConstraint.AngularSpeed|AngularSpeed`, `Class.CylindricalConstraint.AngularResponsiveness|AngularResponsiveness`, and `Class.CylindricalConstraint.ServoMaxTorque|ServoMaxTorque`.

## Linear power

If a cylindrical's `Class.CylindricalConstraint|ActuatorType` is set to `Enum.ActuatorType|Motor`, it attempts to translate the attachments with the goal of reaching `Class.CylindricalConstraint|Velocity`. You can further control this translation through both `Class.CylindricalConstraint|MotorMaxAcceleration` and `Class.CylindricalConstraint|MotorMaxForce`.

If a cylindrical's `Class.CylindricalConstraint|ActuatorType` is set to `Enum.ActuatorType|Servo`, it attempts to translate the attachments to a set separation specified by `Class.CylindricalConstraint|TargetPosition`. This translation is controlled by `Class.CylindricalConstraint|Speed`, `Class.CylindricalConstraint|LinearResponsiveness`, and `Class.CylindricalConstraint|ServoMaxForce`.

## Limits

You can set limits to restrict both the **sliding range** and **rotation** of a cylindrical constraint.

Enabling the `Class.CylindricalConstraint|LimitsEnabled` property exposes the `Class.CylindricalConstraint|LowerLimit` and `Class.CylindricalConstraint|UpperLimit` values, as well as `Class.CylindricalConstraint|Restitution` which defines the elasticity of the attachments when they reach either limit.

Enabling the `Class.CylindricalConstraint.AngularLimitsEnabled|AngularLimitsEnabled` property exposes the `Class.CylindricalConstraint.LowerAngle|LowerAngle` and `Class.CylindricalConstraint.UpperAngle|UpperAngle` limits, as well as `Class.CylindricalConstraint.AngularRestitution|AngularRestitution` which defines the elasticity of the attachments when they reach either limit.

_LimitsEnabled = **true**_

_AngularLimitsEnabled = **true**_

## Inclination angle

`Class.CylindricalConstraint.InclinationAngle|InclinationAngle` defines the direction of the rotation axis as an angle from the **X** axis in the **X**/**Y** plane of `Class.Constraint.Attachment0|Attachment0`, from -180 to 180. This lets you tilt the rotating element without changing the sliding axis.

_InclinationAngle = **90**_

_InclinationAngle = **30**_
