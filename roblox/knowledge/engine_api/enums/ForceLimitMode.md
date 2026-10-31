---
name: ForceLimitMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The **ForceLimitMode** enum determines how the maximum force for a constraint is specified and how that limit is enforced by the constraint."
---

# ForceLimitMode

The **ForceLimitMode** enum determines how the maximum force for a constraint
is specified and how that limit is enforced by the constraint.

**Type:** enum

## Description

This enum is used to determine how the maximum force for a constraint is
specified and how that limit will be enforced by the constraint.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Magnitude` | 0 | A single number is used to specify the magnitude of the maximum constraint force. The constraint will ensure that the force it applies will have a magnitude that is less than this limit. |
| `PerAxis` | 1 | A vector is used to specify the maximum force value along each axis of a given reference frame. The constraint will ensure that each component of the force will have an absolute value that's less than the corresponding vector entry. |