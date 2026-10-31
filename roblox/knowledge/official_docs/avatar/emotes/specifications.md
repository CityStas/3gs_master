---
title: "Emote specifications"
url: /docs/en-us/avatar/emotes/specifications
last_updated: 2026-10-30T19:55:37Z
description: "Emote specifications list the specific technical requirements necessary for Studio compatibility."
---

# Emote specifications

Emotes are made up of an `Class.Animation` object with the `Class.Animation.AnimationId` property set to the asset ID of your animation sequence. The `Class.Animation` object is the only component required to upload an emote to the Marketplace because animations do not require meshes, textures, or other 3D art components.

_`Animation` object in the Explorer window._

_`AnimationId` property in the Properties window._

## Animation requirements

Emotes must meet the following requirements before you upload them to the Marketplace, otherwise they may fail validation:

- Emotes must be less than 10 seconds.
- The joint root of the character cannot move too far from its starting position.
- Movement speed can't exceed a certain threshold to prevent teleportation abuse (measured from a frame-by-frame basis).
- Animation data must reference a [standard R15 rig](/docs/en-us/avatar/character-bodies/specifications.md#standard-r15-rigs).
  > **Info:** Emotes for [advanced R15 rigs](/docs/en-us/avatar/character-bodies/specifications.md#advanced-r15-rigs) are currently in a closed beta. For more information, see the [DevForum announcement](https://devforum.roblox.com/t/upload-and-publish-for-emotes-with-additional-joints-is-now-open/4710932).
- Animation must be sourced from a `CurveAnimation`. For information on converting animation data, see [Import emotes - Generate asset ID](/docs/en-us/avatar/emotes/import.md#generate-asset-id).
- Animations must meet Roblox's [Community Standards](https://en.help.roblox.com/hc/en-us/articles/203313410-Roblox-Community-Standards) and [Marketplace policies](/docs/en-us/marketplace/marketplace-policy.md).
