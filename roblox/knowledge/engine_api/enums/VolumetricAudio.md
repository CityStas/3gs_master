---
name: VolumetricAudio
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls how the engine renders volumetric audio effects."
---

# VolumetricAudio

Controls how the engine renders volumetric audio effects.

**Type:** enum

## Description

Controls how the engine renders volumetric audio effects, allowing sound to
emanate from the surface of a [Part](/docs/reference/engine/classes/Part.md) rather than a single point in
space.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Disabled` | 0 | Volumetric audio is disabled; sound emanates from a single point. |
| `Automatic` | 1 | Currently equivalent to [VolumetricAudio.Disabled](/docs/reference/engine/enums/VolumetricAudio.md). |
| `Enabled` | 2 | Volumetric audio is enabled; sound emanates from the object's volume. |