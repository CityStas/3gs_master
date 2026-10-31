---
title: "Rope"
url: /docs/en-us/physics/constraints/rope
last_updated: 2026-10-30T19:55:46Z
description: "RopeConstraint prevents two attachments from separating further than a defined length, with optional behavior as an extending or contracting winch."
---

# Rope

> **Info:** For an overview on creating, visualizing, and simulating mechanical constraints, including `Class.RopeConstraint`, see [Mechanical constraints](/docs/en-us/physics/mechanical-constraints.md). Also see [Roblox units](/docs/en-us/physics/units.md) to understand how Roblox units compare to metric units.

A `Class.RopeConstraint` prevents two attachments from separating further than a defined `Class.RopeConstraint.Length|Length`. The attachments can move closer together than this length and both can freely rotate. `Class.RopeConstraint.Restitution|Restitution` defines the elasticity of the attachments when they reach the separation limit specified by `Class.RopeConstraint.Length|Length`.

This constraint can also be powered to behave as a [motorized winch](#winch).

## Winch

If a rope's `Class.RopeConstraint.WinchEnabled|WinchEnabled` property is enabled, it attempts to translate the attachments to a set separation specified by `Class.RopeConstraint.WinchTarget|WinchTarget`, effectively the target length of the rope in studs. This translation is controlled by `Class.RopeConstraint.WinchSpeed|WinchSpeed`, `Class.RopeConstraint.WinchResponsiveness|WinchResponsiveness`, and `Class.RopeConstraint.WinchForce|WinchForce`.

> **Info:**`Class.RopeConstraint.WinchSpeed|WinchSpeed` must be a **positive** value, used to either contract or extend the rope length to `Class.RopeConstraint.WinchTarget|WinchTarget`. Setting a negative speed will revert to 0, not reverse the winch servo direction.
