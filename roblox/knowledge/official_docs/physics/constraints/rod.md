---
title: "Rod"
url: /docs/en-us/physics/constraints/rod
last_updated: 2026-10-30T19:55:46Z
description: "RodConstraint keeps two attachments separated by a defined length, with optional limits on rotational tilt."
---

# Rod

> **Info:** For an overview on creating, visualizing, and simulating mechanical constraints, including `Class.RodConstraint`, see [Mechanical constraints](/docs/en-us/physics/mechanical-constraints.md). Also see [Roblox units](/docs/en-us/physics/units.md) to understand how Roblox units compare to metric units.

A `Class.RodConstraint` keeps two attachments separated by its defined `Class.RodConstraint.Length|Length`. By default, both attachments can rotate freely, although you can enable limits to restrict rotational tilt.

## Limits

You can limit rotation of the attachments within a cone, independently of each other, by enabling the `Class.RodConstraint.LimitsEnabled|LimitsEnabled` property and setting `Class.RodConstraint.LimitAngle0|LimitAngle0` and `Class.RodConstraint.LimitAngle1|LimitAngle1` respectively.
