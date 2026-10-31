---
name: FluidForces
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls the enablement of aerodynamic forces on parts and assemblies in the workspace."
---

# FluidForces

Controls the enablement of aerodynamic forces on parts and assemblies in the
workspace.

**Type:** enum

## Description

Used as an enum value for [Workspace.FluidForces](/docs/reference/engine/classes/Workspace.md) to control the
enablement of aerodynamic forces on parts and assemblies in the workspace.
Note that this enum is not applicable in scripting and
[Workspace.FluidForces](/docs/reference/engine/classes/Workspace.md) must be toggled in Studio.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Aerodynamic forces will not be calculated on any [BaseParts](/docs/reference/engine/classes/BasePart.md). |
| `Experimental` | 1 | Aerodynamic forces will be calculated on [BaseParts](/docs/reference/engine/classes/BasePart.md) with [EnableFluidForces](/docs/reference/engine/classes/BasePart.md) set to true. During the beta phase, the behavior of the aerodynamic force model may change as the model improves. |