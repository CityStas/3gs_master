---
name: RollOffMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "How Sounds parented to a BasePart or Attachment attenuate (fade out) as the distance between the listener and the parent increases."
---

# RollOffMode

How [Sounds](/docs/reference/engine/classes/Sound.md) parented to a [BasePart](/docs/reference/engine/classes/BasePart.md) or [Attachment](/docs/reference/engine/classes/Attachment.md)
attenuate (fade out) as the distance between the listener and the parent
increases.

**Type:** enum

## Description

Enum which determines how [Sounds](/docs/reference/engine/classes/Sound.md) parented to a [BasePart](/docs/reference/engine/classes/BasePart.md)
or [Attachment](/docs/reference/engine/classes/Attachment.md) attenuate (fade out) as the distance between the
listener and the parent increases.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Inverse` | 0 | Volume attenuates from [Sound.RollOffMinDistance](/docs/reference/engine/classes/Sound.md) in an inverse manner, mirroring how sounds attenuate in the real world. This is done through [Sound.RollOffMinDistance](/docs/reference/engine/classes/Sound.md)/`distance`, where `distance` is the [Vector3.Magnitude](/docs/reference/engine/datatypes/Vector3.md) between the audio source and the audio listener. |
| `Linear` | 1 | Volume attenuates between [Sound.RollOffMinDistance](/docs/reference/engine/classes/Sound.md) and [Sound.RollOffMaxDistance](/docs/reference/engine/classes/Sound.md) with a linear relationship. This is done through ([Sound.RollOffMaxDistance](/docs/reference/engine/classes/Sound.md)/`distance`)/([Sound.RollOffMaxDistance](/docs/reference/engine/classes/Sound.md)-[Sound.RollOffMinDistance](/docs/reference/engine/classes/Sound.md)), where `distance` is the [Vector3.Magnitude](/docs/reference/engine/datatypes/Vector3.md) between the audio source and the audio listener. |
| `LinearSquare` | 2 | Volume attenuates between [Sound.RollOffMinDistance](/docs/reference/engine/classes/Sound.md) and [Sound.RollOffMaxDistance](/docs/reference/engine/classes/Sound.md) with a linear squared relationship. This is done through squaring `Linear`. |
| `InverseTapered` | 3 | A hybrid model which follows the `Inverse` model when close to [Sound.RollOffMinDistance](/docs/reference/engine/classes/Sound.md) and the `LinearSquare` model when close to [Sound.RollOffMaxDistance](/docs/reference/engine/classes/Sound.md). This is done by taking the lesser of `Inverse` and `LinearSquare`. |