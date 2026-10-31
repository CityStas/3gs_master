---
name: ParticleEmitterShapeInOut
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls the direction particles travel when emitted from a shaped ParticleEmitter."
---

# ParticleEmitterShapeInOut

Controls the direction particles travel when emitted from a shaped
[ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md).

**Type:** enum

## Description

Controls whether particles emitted from a [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md) travel
outward from, inward toward, or in both directions relative to the emitter
shape surface. Used with the [ParticleEmitter.ShapeInOut](/docs/reference/engine/classes/ParticleEmitter.md) property,
which defaults to [ParticleEmitterShapeInOut.Outward](/docs/reference/engine/enums/ParticleEmitterShapeInOut.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Outward` | 0 | Particles emit directed outward away from the emitter shape surface. |
| `Inward` | 1 | Particles emit directed inward toward the center of the emitter shape. |
| `InAndOut` | 2 | Particles emit in both outward and inward directions from the emitter shape surface, chosen randomly per particle. |