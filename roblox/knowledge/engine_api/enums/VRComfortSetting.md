---
name: VRComfortSetting
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Named presets for VR comfort assists such as vignette, smooth rotation, and third-person follow camera."
---

# VRComfortSetting

Named presets for VR comfort assists such as vignette, smooth rotation, and
third-person follow camera.

**Type:** enum

## Description

Named presets for VR comfort assists. `Comfort`, `Normal`, and `Expert` are
fixed combinations of vignette, smooth rotation, and third-person follow
camera. `Custom` is not a fixed combination: it lets those assists be
configured independently. The [UserGameSettings](/docs/reference/engine/classes/UserGameSettings.md) property that stores
this value is RobloxScript-secured and hidden from the Properties window.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Comfort` | 0 | Most restrictive comfort preset: enables vignette, disables smooth rotation, and disables the third-person follow camera. |
| `Normal` | 1 | Default balanced preset: enables vignette and third-person follow camera while keeping smooth rotation disabled. |
| `Expert` | 2 | Least restrictive comfort preset: disables vignette and enables both smooth rotation and the third-person follow camera. |
| `Custom` | 3 | Lets vignette, smooth rotation, and third-person follow camera be configured independently rather than as a fixed preset. |