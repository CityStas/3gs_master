---
title: "Spring"
url: /docs/en-us/physics/constraints/spring
last_updated: 2026-10-30T19:55:46Z
description: "SpringConstraint applies a force on its attachments based on spring and damper behavior, with an optional minimum/maximum length."
---

# Spring

> **Info:** For an overview on creating, visualizing, and simulating mechanical constraints, including `Class.SpringConstraint`, see [Mechanical constraints](/docs/en-us/physics/mechanical-constraints.md). Also see [Roblox units](/docs/en-us/physics/units.md) to understand how Roblox units compare to metric units.

A `Class.SpringConstraint` applies a force on its attachments based on spring and damper behavior. You can customize a spring's [damping](#damping) and [stiffness](#stiffness), as well as set minimum and maximum [limits](#limits) on the spring's length.

## Free length

`Class.SpringConstraint.FreeLength|FreeLength` defines the natural resting length of the spring. If the attachments are further apart than the free length, they are forced together; if the attachments are closer together than the free length, they are forced apart.

## Damping

The `Class.SpringConstraint.Damping|Damping` value controls how fast the spring's oscillation dies down. A value of 0 allows the spring to oscillate endlessly, while higher values bring the spring to a rest more quickly.

## Stiffness

`Class.SpringConstraint.Stiffness|Stiffness` sets the strength of the spring. Higher values create a spring that responds with more force when its attachments are closer together or further apart than `Class.SpringConstraint.FreeLength|FreeLength`.

_Stiffness = **25**_

_Stiffness = **500**_

## Limits

Enabling the `Class.SpringConstraint.LimitsEnabled|LimitsEnabled` property exposes the `Class.SpringConstraint.MinLength|MinLength` and `Class.SpringConstraint.MaxLength|MaxLength` values for setting the minimum and maximum length of the spring. If the spring's attachments reach these limits, they stop moving apart from one another without restitution.
