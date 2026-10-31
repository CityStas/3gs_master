---
title: "Rigid"
url: /docs/en-us/physics/constraints/rigid
last_updated: 2026-10-30T19:55:46Z
description: "RigidConstraint connects two attachments with zero offset."
---

# Rigid

A `Class.RigidConstraint` connects two `Class.Attachment|Attachments` or `Class.Bone|Bones` and ensures they stay in the same relative position/orientation to each other. This flexibility gives it additional functionality beyond `Class.WeldConstraint`, such as attaching accessories to `Class.Attachment|Attachments` on a character rig.

> **Info:** To attach two `Class.BasePart|BaseParts` together, versus two `Class.Attachment|Attachments` or `Class.Bone|Bones`, see [WeldConstraint](/docs/en-us/physics/constraints/weld.md).

When creating a `Class.RigidConstraint` using Studio's [Constraint](/docs/en-us/physics/mechanical-constraints.md#create-constraints) button, the tool behaves differently depending on whether you click on existing `Class.BasePart|BaseParts`, `Class.Attachment|Attachments`, or `Class.Bone|Bones` after the tool is activated:

- Clicking on an existing `Class.BasePart` creates a new `Class.Attachment` upon it as the intended `Class.RigidConstraint.Attachment0` or `Class.RigidConstraint.Attachment1`.
- Clicking on an existing `Class.Attachment` or `Class.Bone` uses that instance as the intended `Class.RigidConstraint.Attachment0` or `Class.RigidConstraint.Attachment1`.

Following the second valid click, a new `Class.RigidConstraint` is created to connect the two new attachments. If either the first or second click is **not** made on a `Class.BasePart`, `Class.Attachment`, or `Class.Bone`, the workflow is canceled and no constraint is created.
