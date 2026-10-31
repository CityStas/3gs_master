---
name: AlphaMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used by SurfaceAppearance.AlphaMode to determine how the alpha channel of the SurfaceAppearance.ColorMap of a SurfaceAppearance is used."
---

# AlphaMode

Used by [SurfaceAppearance.AlphaMode](/docs/reference/engine/classes/SurfaceAppearance.md) to determine how the alpha channel
of the [SurfaceAppearance.ColorMap](/docs/reference/engine/classes/SurfaceAppearance.md) of a [SurfaceAppearance](/docs/reference/engine/classes/SurfaceAppearance.md) is
used.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Overlay` | 0 | Overlays the [ColorMap](/docs/reference/engine/classes/SurfaceAppearance.md) on top of the underlying part color based on the map's alpha channel. |
| `Transparency` | 1 | Uses the [ColorMap](/docs/reference/engine/classes/SurfaceAppearance.md) alpha channel to control the transparency of the surface. |
| `TintMask` | 2 | Uses the [ColorMap](/docs/reference/engine/classes/SurfaceAppearance.md) alpha channel to control the amount of [SurfaceAppearance.Color](/docs/reference/engine/classes/SurfaceAppearance.md) tinting. |
| `Opaque` | 3 | Ignores the [ColorMap](/docs/reference/engine/classes/SurfaceAppearance.md) alpha channel and assumes an opacity value of 1 everywhere. |