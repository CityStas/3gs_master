---
name: TonemapperPreset
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls which tone-mapping algorithm ColorGradingEffect applies to the rendered scene."
---

# TonemapperPreset

Controls which tone-mapping algorithm [ColorGradingEffect](/docs/reference/engine/classes/ColorGradingEffect.md) applies to
the rendered scene.

**Type:** enum

## Description

Controls which tone-mapping algorithm [ColorGradingEffect](/docs/reference/engine/classes/ColorGradingEffect.md) applies to
the rendered scene. Assign one of these values to
[ColorGradingEffect.TonemapperPreset](/docs/reference/engine/classes/ColorGradingEffect.md) to choose between the current
Roblox visual style and the legacy pre-2019 appearance.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Sets the tone mapper to use the post‑2019 Roblox appearance which provides vivid colors and high contrasts. |
| `Retro` | 1 | Sets the tone mapper to imitate the pre‑2019 Roblox appearance. Colors look less saturated and there is less contrast between them. |