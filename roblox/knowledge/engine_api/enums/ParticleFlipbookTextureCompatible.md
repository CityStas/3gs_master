---
name: ParticleFlipbookTextureCompatible
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates whether a ParticleEmitter's flipbook texture dimensions are compatible with the selected flipbook layout."
---

# ParticleFlipbookTextureCompatible

Indicates whether a [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md)'s flipbook texture dimensions are
compatible with the selected flipbook layout.

**Type:** enum

## Description

Describes runtime compatibility between a [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md)'s texture
and its [FlipbookLayout](/docs/reference/engine/classes/ParticleEmitter.md). Flipbook
playback requires a 1024×1024 texture; if the texture does not meet this
requirement, the engine sets
[ParticleFlipbookTextureCompatible.NotCompatible](/docs/reference/engine/enums/ParticleFlipbookTextureCompatible.md) and disables flipbook
playback. The value begins as [ParticleFlipbookTextureCompatible.Unknown](/docs/reference/engine/enums/ParticleFlipbookTextureCompatible.md)
and transitions to [ParticleFlipbookTextureCompatible.Compatible](/docs/reference/engine/enums/ParticleFlipbookTextureCompatible.md) or
[ParticleFlipbookTextureCompatible.NotCompatible](/docs/reference/engine/enums/ParticleFlipbookTextureCompatible.md) once texture dimensions
are resolved. Set automatically by the engine; not writable from scripts.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `NotCompatible` | 0 | The [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md)'s flipbook texture dimensions are incompatible with the active flipbook layout (the texture must be 1024×1024); flipbook playback is suppressed. |
| `Compatible` | 1 | The [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md)'s flipbook texture dimensions are confirmed compatible with the active flipbook layout; flipbook playback proceeds normally. |
| `Unknown` | 2 | Compatibility has not yet been determined; this is the initial state before the engine resolves the flipbook texture dimensions. |