---
title: "Import emotes"
url: /docs/en-us/avatar/emotes/import
last_updated: 2026-10-30T19:55:37Z
description: "Use the Animation Editor to import and convert animations into emotes."
---

# Import emotes

Studio's [Animation Editor](/docs/en-us/animation/editor.md) lets you import animations into your projects. The following instructions detail how to import a `.fbx` file with animation data into Studio, convert it into a `CurveAnimation` object with an asset ID, then use that asset ID in `Class.Animation` objects that you can use in your games, upload to the Marketplace, or share with other creators.

It's important to ensure your emote meets Roblox's [emote specifications](/docs/en-us/avatar/emotes/specifications.md) to use or sell this asset as an avatar-ready emote, otherwise you can encounter errors at different points in the workflow.

## Import into Studio

To import your asset as an animation:

1. If you don't already have a character body with a [standard R15 rig](/docs/en-us/avatar/character-bodies/specifications.md#standard-r15-rigs), add one to your project in Studio.
  1. In the **Avatar** tab, click the **Character** button.![Character button highlighted in Studio's toolbar.](../../assets/studio/general/Toolbar-Character.png)
  2. Set **Rig Type** to **R15**.
  3. Set **Body Shape** to either **Masculine** or **Feminine**.
  4. Select an avatar style from the provided options. An avatar character body with a standard rigging armature displays in the viewport.
2. Open the Animation Editor.
  1. In the **Avatar** tab, click the **Clip Editor** button.
  2. Select the character with a standard rigging armature. The Animation Editor updates accordingly.
3. In the **Animation Editor**, select **⋯** > **Import** > **From File** and select your `.fbx` file. Your animation populates in the Animation Editor's timeline.

## Generate asset ID

To generate an asset ID for your animation, you must first convert your animation data in the timeline into a `CurveAnimation` object. When you save the `CurveAnimation` object, Roblox creates a cloud-based asset ID to represent your emote.

> **Warning:** The animation data for emotes must be a `Class.CurveAnimation` object instead of a `Class.KeyframeSequence` object.

To convert an existing keyframe sequence to a `CurveAnimation`:

1. In the **Animation Editor**, select the **Curve Editor** button next to the timeline. A confirmation prompt displays.
2. Press **Confirm** to convert your keyframes into a `CurveAnimation` clip.
3. Back in the **Animation Editor**, select the **⋯** > **Publish to Roblox**. The **Asset Configuration** window displays.
4. Add a title and description, then click the **Save** button. The **Asset Configuration** window updates with a copyable asset ID.

## Create an Animation object

To submit an emote to the Marketplace, you must submit an `Class.Animation` object with the `AnimationId` property set to the asset ID of your `CurveAnimation` object.

_`Animation` object in the Explorer window._

_`AnimationId` property in the Properties window._

To create an `Class.Animation` object you can publish as an emote:

1. In the **Explorer** window, add a new `Animation` object.
2. In the **Properties** window, add the asset ID of your emote animation.

## Upload emote to Marketplace

When you have an `Class.Animation` object with your emote animation asset ID set, you can upload the emote to the Marketplace. This process requires an [upload fee](/docs/en-us/marketplace/marketplace-fees-and-commissions.md#upload-fees) of **80 Robux**.

1. In the **Explorer** window, right-click the `Animation` object and select **Save to Roblox**. The **Asset Configuration** window displays.
2. Configure the following fields:
  1. Add a title and description.
  2. Set the **Content Type** to **Avatar Item**.
  3. Set the **Asset Category** to **Emote**.
3. Click the **Submit** button to upload your asset for moderation.

For more information on the upload and publishing process, see [Publish to Marketplace](/docs/en-us/marketplace/publish-to-marketplace.md#upload-an-asset).
