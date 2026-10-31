---
name: SurfaceType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used to determine how a surface should be displayed on a part and how automatic surface joints should behave."
---

# SurfaceType

Used to determine how a surface should be displayed on a part and how
automatic surface joints should behave.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Smooth` | 0 | Adds no details on the surface. |
| `Glue` | 1 | Adds an "X" pattern across the surface. |
| `Weld` | 2 | Adds an "X" pattern across the surface. |
| `Studs` | 3 | Adds square studs across the surface. |
| `Inlet` | 4 | Adds square holes across the surface where studs would be. |
| `Universal` | 5 | Adds a checker pattern to the surface using studs and inlets. |
| `Hinge` | 6 | Adds a yellow hinge to the surface. Parts touching it stick to the surface, allowing for rotations using physics. This should not be used for future work and existing instances should be replaced with a [HingeConstraint](/docs/reference/engine/classes/HingeConstraint.md). |
| `Motor` | 7 | Functioned identically to a hinge with the addition of a grey ring. |
| `SteppingMotor` | 8 | Functioned identically to a motor. It may have functioned differently in the past, but that functionality is non-existent. |
| `SmoothNoOutlines` | 10 | Previously similar to **Smooth** with outlines but no longer relevant since outlines have been removed. |