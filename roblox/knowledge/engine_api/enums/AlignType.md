---
name: AlignType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "An enum that specifies how the constraint will attempt to align the body associated with the constraint."
---

# AlignType

An enum that specifies how the constraint will attempt to align the body
associated with the constraint.

**Type:** enum

## Description

An enum that specifies how the constraint will attempt to align the body
associated with the constraint and attachment. Depending on the configuration,
it can be used to align specific axes to be parallel, perpendicular, or to
look at a specific point.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Parallel` | 0 |  |
| `Perpendicular` | 1 |  |
| `PrimaryAxisParallel` | 2 | Aligns the primary axis to be parallel to the axis given by [Constraint.Attachment1](/docs/reference/engine/classes/Constraint.md). |
| `PrimaryAxisPerpendicular` | 3 | Aligns the primary axis to be perpendicular to the axis given by [Constraint.Attachment1](/docs/reference/engine/classes/Constraint.md). |
| `PrimaryAxisLookAt` | 4 | Aligns the primary axis to look at the point given by [Constraint.Attachment1](/docs/reference/engine/classes/Constraint.md) or the [AlignOrientation.LookAtPosition](/docs/reference/engine/classes/AlignOrientation.md). |
| `AllAxes` | 5 | Aligns all of the axes of [Constraint.Attachment0](/docs/reference/engine/classes/Constraint.md) to the axes given by [Constraint.Attachment1](/docs/reference/engine/classes/Constraint.md) or to the target orientation provided by [AlignOrientation.PrimaryAxis](/docs/reference/engine/classes/AlignOrientation.md) and [AlignOrientation.SecondaryAxis](/docs/reference/engine/classes/AlignOrientation.md). |