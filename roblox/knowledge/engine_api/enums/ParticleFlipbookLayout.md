---
name: ParticleFlipbookLayout
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the layout of the flipbook texture."
---

# ParticleFlipbookLayout

Determines the layout of the flipbook texture.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | Disable flipbook features and use the texture as a single static texture over the particle's lifetime. |
| `Grid2x2` | 1 | 2&times;2 frames for a 4-frame animation. |
| `Grid4x4` | 2 | 4&times;4 frames for a 16-frame animation. |
| `Grid8x8` | 3 | 8&times;8 frames for a 64-frame animation. |
| `Custom` | 4 | A custom grid size defined by [FlipbookSizeX](/docs/reference/engine/classes/ParticleEmitter.md) and [FlipbookSizeY](/docs/reference/engine/classes/ParticleEmitter.md). |