---
name: Technology
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Enum used by Lighting.Technology to represent the different lighting systems available for rendering the 3D world."
---

# Technology

Enum used by [Lighting.Technology](/docs/reference/engine/classes/Lighting.md) to represent the different lighting
systems available for rendering the 3D world.

**Type:** enum

## Description

This enum represents the different lighting systems available for rendering
the 3D world. It is used by the [Lighting.Technology](/docs/reference/engine/classes/Lighting.md) property.

Note that [Lighting.Technology](/docs/reference/engine/classes/Lighting.md) has been superseded by
[LightingStyle](/docs/reference/engine/classes/Lighting.md) which determines the artistic
intent behind lighting, and
[PrioritizeLightingQuality](/docs/reference/engine/classes/Lighting.md) which
indicates whether you prefer lighting/shading quality or view distance to
scale down first.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Legacy` | 0 |  |
| `Voxel` | 1 | Uses a 4&times;4&times;4 voxel map for light and shadow calculation. |
| `Compatibility` | 2 | Simulates the removed legacy technology and is now deprecated. To achieve a similar look, use `Voxel` Lighting and add a [ColorGradingEffect](/docs/reference/engine/classes/ColorGradingEffect.md) post‑processing effect set to the [Retro](/docs/reference/engine/enums/TonemapperPreset.md) preset. |
| `ShadowMap` | 3 | Features shadow mapping that produces more realistic and crisp shadows from sunlight or directional light sources. |
| `Future` | 4 | Features the most advanced technology for high-fidelity lighting and shadows. |
| `Unified` | 5 |  |