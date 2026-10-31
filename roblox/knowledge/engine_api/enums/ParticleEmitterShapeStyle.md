---
name: ParticleEmitterShapeStyle
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether a ParticleEmitter emits particles from the surface or the volume of its shape."
---

# ParticleEmitterShapeStyle

Controls whether a [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md) emits particles from the surface or
the volume of its shape.

**Type:** enum

## Description

Controls whether a [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md) emits particles from the surface or
throughout the volume of the shape defined by [ParticleEmitter.Shape](/docs/reference/engine/classes/ParticleEmitter.md).
Used with the [ParticleEmitter.ShapeStyle](/docs/reference/engine/classes/ParticleEmitter.md) property, which defaults to
[ParticleEmitterShapeStyle.Volume](/docs/reference/engine/enums/ParticleEmitterShapeStyle.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Volume` | 0 | Particles emit from throughout the interior volume of the emitter shape. |
| `Surface` | 1 | Particles emit only from the outer surface of the emitter shape. |