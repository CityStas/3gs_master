---
name: NoiseType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the noise algorithm used by a `Noise` instance's `NoiseType` property."
---

# NoiseType

Specifies the noise algorithm used by a `Noise` instance's `NoiseType`
property.

**Type:** enum

## Description

Selects the procedural noise algorithm applied when sampling through a `Noise`
instance. The chosen value determines which kernel `SampleDirectional()`
evaluates; different values support different sampling modes. The default
value of `NoiseType` is [NoiseType.SimplexGabor](/docs/reference/engine/enums/NoiseType.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `SimplexGabor` | 0 | Uses an OpenSimplex2 body-centered cubic (BCC) lattice with a Gabor sinusoidal kernel for anisotropic directional noise sampling. |