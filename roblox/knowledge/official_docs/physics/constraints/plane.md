---
title: "Plane"
url: /docs/en-us/physics/constraints/plane
last_updated: 2026-10-30T19:55:46Z
description: "PlaneConstraint moves two attachments into a position/orientation along a plane, and both attachments remain free to translate and rotate unless otherwise constrained."
---

# Plane

> **Info:** For an overview on creating, visualizing, and simulating mechanical constraints, including `Class.PlaneConstraint`, see [Mechanical constraints](/docs/en-us/physics/mechanical-constraints.md). Also see [Roblox units](/docs/en-us/physics/units.md) to understand how Roblox units compare to metric units.

A `Class.PlaneConstraint` moves its `Class.Constraint.Attachment0|Attachment0` and `Class.Constraint.Attachment1|Attachment1` into a position/orientation along a plane whose normal vector is the primary axis of `Class.Constraint.Attachment0|Attachment0`. Both parent assemblies remain free to translate and rotate unless otherwise constrained.

Compare the following examples for how the orientation of `Class.Constraint.Attachment0|Attachment0` defines the plane, while the orientation of `Class.Constraint.Attachment1|Attachment1` has no bearing.

#### Orientation = (0, 0, 90)

![Attachment0 oriented to (0, 0, 90)](../../assets/physics/constraints/Plane-Attachment0-1.jpg)

#### Orientation = (-45, 0, 90)

![Attachment0 oriented to (-45, 0, 90)](../../assets/physics/constraints/Plane-Attachment0-2.jpg)
