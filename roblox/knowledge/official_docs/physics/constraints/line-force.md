---
title: "LineForce"
url: /docs/en-us/physics/constraints/line-force
last_updated: 2026-10-30T19:55:46Z
description: "The LineForce constraint applies force along the theoretical line connecting its two attachments."
---

# LineForce

> **Info:** For an overview on creating, visualizing, and simulating mover constraints, including `Class.LineForce`, see [mover constraints](/docs/en-us/physics/mover-constraints.md). Also see [Roblox units](/docs/en-us/physics/units.md) to understand how Roblox units compare to metric units.

The `Class.LineForce` constraint applies force along the theoretical line connecting its two `Class.Attachment|Attachments`. As the end points (attachments) move, the direction of force will change accordingly.

## Force location

By default, force is applied to either parent at its attachment location. If desired, force can be focused at each parent's center of mass by toggling on `Class.LineForce.ApplyAtCenterOfMass|ApplyAtCenterOfMass`.

_ApplyAtCenterOfMass = **false**_

_ApplyAtCenterOfMass = **true**_

## Inverse square law

When `Class.LineForce.InverseSquareLaw|InverseSquareLaw` is true, the force magnitude is multiplied by the inverse square of the distance, meaning the force will increase exponentially as the two attachments get closer together, like magnets. When using this setting, it's recommended that you set a `Class.LineForce.MaxForce|MaxForce` threshold to prevent infinite force if the attachments align precisely.

_InverseSquareLaw = **false**_

_InverseSquareLaw = **true**_

## Reactionary force

By default, the constraint only applies force to `Class.Constraint.Attachment0|Attachment0`, while `Class.Constraint.Attachment1|Attachment1` remains unaffected. However, force can be applied to both attachments in **equal and opposite directions** by enabling `Class.LineForce.ReactionForceEnabled|ReactionForceEnabled`.

_ReactionForceEnabled = **false**_

_ReactionForceEnabled = **true**_
