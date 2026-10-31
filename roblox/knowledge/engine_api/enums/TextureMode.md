---
name: TextureMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes how the texture of a Trail or Beam behaves."
---

# TextureMode

Describes how the texture of a [Trail](/docs/reference/engine/classes/Trail.md) or [Beam](/docs/reference/engine/classes/Beam.md) behaves.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Stretch` | 0 | For a [Trail](/docs/reference/engine/classes/Trail.md), the texture will stretch out based on the lifetime of the trail, and shrink inwards if the trail's attachments stop moving.  For a [Beam](/docs/reference/engine/classes/Beam.md), the texture will repeat [TextureLength](/docs/reference/engine/classes/Beam.md) times across the beam's overall length. See [here](/docs/en-us/effects/beams.md#texture-lengthmode) for details. |
| `Wrap` | 1 | For a [Trail](/docs/reference/engine/classes/Trail.md), the texture will be tiled as the length of the trail changes, but the textures will remain stationary relative to their attachments.  For a [Beam](/docs/reference/engine/classes/Beam.md), the texture repetitions will equal the beam's overall length (in&nbsp;studs) divided by its [TextureLength](/docs/reference/engine/classes/Beam.md). See [here](/docs/en-us/effects/beams.md#texture-lengthmode) for details. |
| `Static` | 2 | For a [Trail](/docs/reference/engine/classes/Trail.md), the texture will be rolled out as the attachments move, and they will remain in place until their lifetime is met. This setting is ideal for trail textures that should appear "stamped" where rendered, such as paw prints or tire tracks.  This value is not supported for [Beam](/docs/reference/engine/classes/Beam.md) and therefore behaves identically to **Wrap**. |