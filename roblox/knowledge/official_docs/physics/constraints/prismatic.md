---
title: "Prismatic"
url: /docs/en-us/physics/constraints/prismatic
last_updated: 2026-10-30T19:55:46Z
description: "PrismaticConstraint allows two attachments to slide along one axis but not rotate, with optional assigned power for mechanisms like sliding doors and elevator platforms."
---

# Prismatic

> **Info:** For an overview on creating, visualizing, and simulating mechanical constraints, including `Class.PrismaticConstraint`, see [Mechanical constraints](/docs/en-us/physics/mechanical-constraints.md). Also see [Roblox units](/docs/en-us/physics/units.md) to understand how Roblox units compare to metric units.

A `Class.PrismaticConstraint` creates a rigid joint between two attachments, allowing them to slide along one axis but not rotate. The constraint can also be [powered](#linear-power) for mechanisms like sliding doors and elevator platforms.

> **Info:** Orientation of a prismatic's attachments affects how it will move. To ensure movement occurs along the desired axis, each attachment's `Class.Attachment.Axis|Axis`, visualized by the yellow arrow, should point in the same direction.
## Linear power

If a prismatic's `Class.PrismaticConstraint|ActuatorType` is set to `Enum.ActuatorType|Motor`, it attempts to translate the attachments with the goal of reaching `Class.PrismaticConstraint|Velocity`. You can further control this translation through both `Class.PrismaticConstraint|MotorMaxAcceleration` and `Class.PrismaticConstraint|MotorMaxForce`.

If a prismatic's `Class.PrismaticConstraint|ActuatorType` is set to `Enum.ActuatorType|Servo`, it attempts to translate the attachments to a set separation specified by `Class.PrismaticConstraint|TargetPosition`. This translation is controlled by `Class.PrismaticConstraint|Speed`, `Class.PrismaticConstraint|LinearResponsiveness`, and `Class.PrismaticConstraint|ServoMaxForce`.

_ActuatorType = **Motor**_

_ActuatorType = **Servo**_

## Limits

You can set limits to restrict the sliding range a prismatic. Enabling the `Class.PrismaticConstraint|LimitsEnabled` property exposes the `Class.PrismaticConstraint|LowerLimit` and `Class.PrismaticConstraint|UpperLimit` values, as well as `Class.PrismaticConstraint|Restitution` which defines the elasticity of the attachments when they reach either limit.
