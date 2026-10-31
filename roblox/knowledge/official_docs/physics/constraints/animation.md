---
title: "AnimationConstraint"
url: /docs/en-us/physics/constraints/animation
last_updated: 2026-10-30T19:55:46Z
description: "AnimationConstraint aligns two base parts with an animate-able kinematic or force-based joint."
---

# AnimationConstraint

> **Info:** For an overview on creating, visualizing, and simulating mover constraints, including `Class.AnimationConstraint`, see [mover constraints](/docs/en-us/physics/mover-constraints.md). Also see [Roblox units](/docs/en-us/physics/units.md) to understand how Roblox units compare to metric units.

An `Class.AnimationConstraint` constrains its `Class.Attachment|Attachments` by an offset [transform](#transform). It can be either [kinematic](#kinematic) for snap‑to behavior or it can follow the target trajectory using [force and torque](#force-and-torque). limited by `Class.AnimationConstraint.MaxForce|MaxForce` and `Class.AnimationConstraint.MaxTorque|MaxTorque`.

## Transform

The constraint's `Class.AnimationConstraint.Transform|Transform` is the internal `Datatype.CFrame` that's manipulated when the constraint is being animated. How this transform is reached depends on the constraint's [kinematic](#kinematic) setting.

## Kinematic

When the constraint's `Class.AnimationConstraint.IsKinematic|IsKinematic` property is `true`, the connected parts snap to the [transform](#transform) instantly and precisely without participating in physics simulation. When `false`, the connected parts follow the trajectory using [force and torque](#force-and-torque).

## Force and torque

If the constraint is **not** set to [kinematic](#kinematic), the connected parts follow a trajectory toward the [transform](#transform) using a maximum force/torque limited by `Class.AnimationConstraint.MaxForce|MaxForce` and `Class.AnimationConstraint.MaxTorque|MaxTorque` respectively.
