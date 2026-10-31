---
name: DraggerMovementMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether DraggerService moves parts geometrically or with physics simulation during Studio drag operations."
---

# DraggerMovementMode

Controls whether [DraggerService](/docs/reference/engine/classes/DraggerService.md) moves parts geometrically or with
physics simulation during Studio drag operations.

**Type:** enum

## Description

Controls whether Studio's drag tool moves parts by directly setting their
positions and orientations ([DraggerMovementMode.Geometric](/docs/reference/engine/enums/DraggerMovementMode.md)) or by
simulating physics and respecting [Constraints](/docs/reference/engine/classes/Constraint.md) during the
drag ([DraggerMovementMode.Physical](/docs/reference/engine/enums/DraggerMovementMode.md)). The active mode is set via
[DraggerService.DraggerMovementMode](/docs/reference/engine/classes/DraggerService.md), which defaults to
[DraggerMovementMode.Geometric](/docs/reference/engine/enums/DraggerMovementMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Geometric` | 0 | Parts are moved by directly updating their position and orientation, ignoring physics and constraints. |
| `Physical` | 1 | Parts are moved by applying physics impulses, so constraints and collisions are respected during the drag. |