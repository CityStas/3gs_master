---
title: "TorsionSpring"
url: /docs/en-us/physics/constraints/torsion-spring
last_updated: 2026-10-30T19:55:46Z
description: "TorsionSpringConstraint applies torque based on a relative angle and relative angular velocity, in an attempt to bring two axes from two parts together."
---

# TorsionSpring

> **Info:** For an overview on creating, visualizing, and simulating mechanical constraints, including `Class.TorsionSpringConstraint`, see [Mechanical constraints](/docs/en-us/physics/mechanical-constraints.md). Also see [Roblox units](/docs/en-us/physics/units.md) to understand how Roblox units compare to metric units.

A `Class.TorsionSpringConstraint` applies torque based on a relative angle and relative angular velocity. It attempts to bring two axes from two parts together and is useful for [hinged](/docs/en-us/physics/constraints/hinge.md) swinging doors with a spring-back effect.

> **Info:** Correct orientation of a torsion spring's attachments is important. The constraint will attempt to bring the `Class.Attachment.SecondaryAxis|SecondaryAxis` of each attachment, visualized by the orange arrows, into alignment. When building mechanisms like swinging doors, ensure that the secondary axes are **perpendicular** to the intended axis of rotation.
## Damping

The `Class.TorsionSpringConstraint.Damping|Damping` value controls how fast the spring's oscillation dies down. A value of 0 allows the spring to oscillate endlessly, while higher values bring the spring to a rest more quickly.

_Damping = **0**_

_Damping = **50**_

## Stiffness

`Class.TorsionSpringConstraint.Stiffness|Stiffness` sets the torsional strength of the spring. Higher values create a spring that responds with more force.

## Limits

Enabling the `Class.TorsionSpringConstraint.LimitsEnabled|LimitsEnabled` property exposes the `Class.TorsionSpringConstraint.MaxAngle|MaxAngle` value to restrict the spring's range within a cone; it also exposes the `Class.TorsionSpringConstraint.Restitution|Restitution` value which defines the elasticity of the attachments when they reach their limit.
