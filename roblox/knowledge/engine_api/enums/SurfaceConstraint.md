---
name: SurfaceConstraint
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "This item is deprecated and is replaced by the SurfaceType enum."
---

# SurfaceConstraint

This item is deprecated and is replaced by the [SurfaceType](/docs/reference/engine/enums/SurfaceType.md) enum.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | No surface constraint. |
| `Hinge` | 1 | Makes the side appear with a yellow hinge. Any part connected to this hinge will stick to the side and rotate using physics. |
| `SteppingMotor` | 2 | Functions identically to a motor. It may have functioned differently in the past, but that functionality no longer seems to exist. |
| `Motor` | 3 | Acts the same as a Hinge, but has a grey ring around it and automatically rotates any part connected to it. |