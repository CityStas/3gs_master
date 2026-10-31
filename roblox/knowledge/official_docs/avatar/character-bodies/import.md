---
title: "Import character bodies"
url: /docs/en-us/avatar/character-bodies/import
last_updated: 2026-10-30T19:55:36Z
description: "Use the Importer to add third-party models to Studio before testing, using, or uploading the character model."
---

# Import character bodies

Studio's Importer lets you import 3D assets into your projects, such as avatar clothing, accessories, and character bodies. The following instructions detail how to import a character body `.fbx` or `.gltf` file into Studio as a `Model` object that you can use in your games, upload to the Marketplace, or share with other creators.

> **Info:** If your `.fbx` or `.gltf` file is a single mesh, you can use the [Avatar Setup](/docs/en-us/avatar-setup.md) tool to automatically partition the mesh into the appropriate 15 body parts necessary for an avatar character body.

While the Importer provides object previews and error-checking to ensure that your creation meets Roblox's [general 3D requirements](/docs/en-us/art/modeling/specifications.md), it's important to ensure that your character model also meets Roblox's [character body specifications](/docs/en-us/avatar/character-bodies/specifications.md) to use or sell this asset as an avatar-ready character model, otherwise you can encounter errors at different points in the workflow.

To import your asset as a character body model:

1. In the **Home** tab, click the **Import** button to open the 3D Importer. A file browser opens.
2. Select your rigged character's `.fbx` or `.gltf` file. The 3D Importer loads a preview of the character model.
  - If textures don't load for your asset, you can manually import your textures later.
  - For additional information on import settings and troubleshooting, see [Importer](/docs/en-us/studio/importer.md).
3. In the **Rig General** section,
  1. **OPTIONAL** If you are importing an [advanced R15 rig](/docs/en-us/avatar/character-bodies/specifications.md#advanced-r15-rigs), set **Rig Type** to **Custom Humanoid**.
  2. Set **Rig Scale** to the appropriate [Body Scale](/docs/en-us/avatar/character-bodies/specifications.md#body-scale) of your character.
  3. Set **Constraint Type** to **Joint Upgrade**.
4. Select **Import**. The asset populates in your workspace as a `Class.Model` with the appropriate textures applied as a `Class.SurfaceAppearance` or `Class.MeshPart.TextureID`.

**Textures didn't load correctly?**

If your textures didn't load correctly, you can import them manually using the [Asset Manager](/docs/en-us/projects/assets/manager.md):

1. In the **Asset Manager**, click the **Import** button. If you are unable to access the Asset Manager, save and publish your game first.
2. Upload your image files.
3. After moderation clears your images, select the `Class.MeshPart` parented within your imported `Class.Model`.
4. If you are using a single basic texture, set the `Class.MeshPart.TextureID` property to your uploaded texture image.
5. If you are using PBR textures:
  1. Add a `Class.SurfaceAppearance` child to your `Class.MeshPart`.
  2. In the `Class.SurfaceAppearance` properties, click each property value and assign the appropriate texture image from the asset dropdown:
    1. Set the **ColorMap** to the **_ALB** texture image.
    2. Set the **MetalnessMap** to the **_MTL** texture image.
    3. Set the **NormalMap** to the **_NOR** texture image.
    4. Set the **RoughnessMap** to the **_RGH** texture image.

With this new character `Class.Model`, you can perform any of the following:

- If your character includes an [advanced R15 rig](/docs/en-us/avatar/character-bodies/specifications.md#advanced-r15-rigs), add `Class.HumanoidRigDescription` and/or `Class.DigitsRigDescription` objects for Marketplace and animation requirements. You may need to use the [Adaptive Animation](/docs/en-us/characters/adaptive-animation.md) plugin to remap your joints and set a baseline t-pose reference to better support your animations.
- Begin the process of [uploading and publishing](/docs/en-us/marketplace/publish-to-marketplace.md#upload-an-asset) the character model to the Marketplace. This involves some additional validation and moderation steps.
- Use the model in your current game and modify the model's appearance with [HumanoidDescription](/docs/en-us/characters/appearance.md#manually-modify-appearance).
  - Playtest as the character by renaming the `Class.Model` to `StarterCharacter` and moving the `Class.Model` to the `Class.StarterPlayer` folder in the **Explorer** before play testing.
- Save the model to your [Toolbox](/docs/en-us/projects/assets/toolbox.md) or make it public on the [Creator Store](/docs/en-us/production/creator-store.md) to use within any of your games or share with other creators.

> **Warning:** Character creation is a complex process that requires lots of testing and iteration. For information on importing your character model into a test place and verifying your avatar and related components, see [Test character bodies](/docs/en-us/avatar/character-bodies/test.md).
