---
title: "Universal"
url: /docs/en-us/physics/constraints/universal
last_updated: 2026-10-30T19:55:46Z
description: "UniversalConstraint ensures two axes on two assemblies remain perpendicular, useful for applications such as vehicle power transmission to rear drive shafts, robotics, and more."
---

# Universal

> **Info:** For an overview on creating, visualizing, and simulating mechanical constraints, including `Class.UniversalConstraint`, see [Mechanical constraints](/docs/en-us/physics/mechanical-constraints.md). Also see [Roblox units](/docs/en-us/physics/units.md) to understand how Roblox units compare to metric units.

A `Class.UniversalConstraint` ensures two axes on two assemblies remain perpendicular. Example applications include vehicle power transmission to the rear drive shafts, robotics, and more.

## Orientations

Orientation of a universal's two attachments affects how it will move. To ensure it behaves correctly, the `Class.Attachment.SecondaryAxis|SecondaryAxis` of the attachments, visualized by the orange arrows, should be **perpendicular** to each other. Note that a green L-shaped indicator appears when the axes are properly oriented.

#### Axes Perpendicular

![Secondary axes perpendicular for correct behavior](../../assets/physics/constraints/Universal-Attachments-Correct.jpg)

#### Axes Misoriented

![Secondary axes misoriented](../../assets/physics/constraints/Universal-Attachments-Incorrect.jpg)

## Limits

Enabling the `Class.UniversalConstraint.LimitsEnabled|LimitsEnabled` property exposes the `Class.UniversalConstraint.MaxAngle|MaxAngle` limit to restrict tilt within a cone, as well as `Class.UniversalConstraint.Restitution|Restitution` which defines the elasticity of the attachments when they reach the limit.
