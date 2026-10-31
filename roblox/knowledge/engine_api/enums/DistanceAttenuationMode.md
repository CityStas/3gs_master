---
name: DistanceAttenuationMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines how an AudioEmitter attenuates (fades out) as the distance between the AudioEmitter and an interacting AudioListener increases."
---

# DistanceAttenuationMode

Determines how an [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) attenuates (fades out) as the distance
between the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) and an interacting [AudioListener](/docs/reference/engine/classes/AudioListener.md)
increases.

**Type:** enum

## Description

Determines how an [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) attenuates (fades out) as the distance
between the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) and an interacting [AudioListener](/docs/reference/engine/classes/AudioListener.md)
increases. Most values refer to a preset rolloff curve that the
[AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) will apply over the range given by
[DistanceAttenuationBounds](/docs/reference/engine/classes/AudioEmitter.md). When
set to [DistanceAttenuationMode.Custom](/docs/reference/engine/enums/DistanceAttenuationMode.md), the emitter instead uses a
developer-supplied curve given by
[AudioEmitter:SetDistanceAttenuation()](/docs/reference/engine/classes/AudioEmitter.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Custom` | 0 | Uses the developer-supplied [DistanceAttenuation](/docs/reference/engine/classes/AudioEmitter.md) curve for gain rolloff. |
| `InverseTapered` | 1 | Volume attenuates according to a hybrid model which follows the [DistanceAttenuationMode.Inverse](/docs/reference/engine/enums/DistanceAttenuationMode.md) model when close to the lower bound of [AudioEmitter.DistanceAttenuationBounds](/docs/reference/engine/classes/AudioEmitter.md) and the [DistanceAttenuationMode.LinearSquared](/docs/reference/engine/enums/DistanceAttenuationMode.md) model when close to the upper bound of [AudioEmitter.DistanceAttenuationBounds](/docs/reference/engine/classes/AudioEmitter.md). This is done by taking the lesser of these two curves, such that the curve mostly follows an inverse relationship but tapers to silence at the maximum distance. |
| `Linear` | 2 | Volume attenuates between the bounds of [AudioEmitter.DistanceAttenuationBounds](/docs/reference/engine/classes/AudioEmitter.md) with a linear relationship. This is done by computing (`maxDistance` - `distance`) / (`maxDistance` - `minDistance`), where distance is the [Vector3.Magnitude](/docs/reference/engine/classes/Vector3.md) between the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md)'s position and the [AudioListener](/docs/reference/engine/classes/AudioListener.md)'s position. |
| `LinearSquared` | 3 | Volume attenuates between the bounds of [AudioEmitter.DistanceAttenuationBounds](/docs/reference/engine/classes/AudioEmitter.md) with a linear-squared relationship. This is done by squaring the formula used to determine the volume when using [DistanceAttenuationMode.Linear](/docs/reference/engine/enums/DistanceAttenuationMode.md), which creates a parabolic curve with a steeper fade. |
| `Inverse` | 4 | Volume attenuates from the lower bound of [AudioEmitter.DistanceAttenuationBounds](/docs/reference/engine/classes/AudioEmitter.md) in an inverse manner, mirroring how sounds attenuate in the real world. This is done by computing (`minDistance`/`distance`), where `distance` is the [Vector2.Magnitude](/docs/reference/engine/classes/Vector2.md) between the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md)'s position and the [AudioListener](/docs/reference/engine/classes/AudioListener.md)'s position. |