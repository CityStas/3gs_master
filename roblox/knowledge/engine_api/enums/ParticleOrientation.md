---
name: ParticleOrientation
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies how a particle's rendered geometry is oriented."
---

# ParticleOrientation

Specifies how a particle's rendered geometry is oriented.

**Type:** enum

## Description

Controls the orientation mode used by [ParticleEmitter.Orientation](/docs/reference/engine/classes/ParticleEmitter.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `FacingCamera` | 0 | Orients particles as billboards that face the camera. |
| `FacingCameraWorldUp` | 1 | Orients particles toward the camera while keeping them upright on the world Y axis. |
| `VelocityParallel` | 2 | Orients particles parallel to their direction of movement. |
| `VelocityPerpendicular` | 3 | Orients particles perpendicular to their direction of movement. |