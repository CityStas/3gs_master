---
title: "Import layered accessories"
url: /docs/en-us/avatar/layered-accessories/import
last_updated: 2026-10-30T19:55:37Z
description: "Use the Importer to add third-party models to Studio before using the Accessory Fitting Tool to convert the model to an Accessory."
keywords: ["Layered clothing","Layerable accessories","Layered clothing accessories"]
---

# Import layered accessories

Studio's Importer lets you import 3D assets into your projects, such as character bodies, makeup, and layered accessories. The following instructions detail how to import a layered accessory `.fbx` or `.gltf` file into Studio as a `Model` object and convert it into an `Accessory` object that you can use in your games, upload to the Marketplace, or share with other creators.

While the Importer provides object previews and error-checking to ensure that your creation meets Roblox's [general 3D requirements](/docs/en-us/art/modeling/specifications.md), it's important to ensure that your character model also meets Roblox's [layered accessory specifications](/docs/en-us/avatar/layered-accessories/specifications.md) to use or sell this asset as an avatar-ready layered accessory, otherwise you can encounter errors at different points in the workflow.

## Import accessories

To import your asset as a layered accessory:

1. In the **Home** tab, click the **Import** button to open the Importer. A file browser opens.
2. Select your layered accessory's `.fbx` or `.gltf` file. The Importer loads a preview of the layered accessory.
3. Select **Import**. The asset populates in your workspace as a `Class.Model` with the appropriate textures applied as a `Class.SurfaceAppearance` or `Class.MeshPart.TextureID`.

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

## Convert layered accessories

After importing your asset into Studio, you can begin **converting** the `Class.Model` object into a `Class.Accessory` using the [Accessory Fitting Tool](/docs/en-us/avatar/accessory-fitting-tool.md) (AFT) so that avatar character bodies can equip your layered accessory.

> **Warning:** For shoes, you must convert the left shoe and the right shoe as separate layered accessories. Use the following instructions for each shoe before grouping both shoe accessories as a `Class.Model` when [saving to Roblox](/docs/en-us/marketplace/publish-to-marketplace.md#upload-an-asset).

To generate your layered accessory:

1. In the toolbar's **Avatar** tab, click **Accessory** to open the AFT. The **Accessory Fitting Tool** panel displays.
2. In the panel:
  1. Select the **Part** field, then in the **Explorer** window, select the layered accessory `Class.MeshPart` object.
  2. Back in the panel, click the **Next** button. The **Asset Type** page displays.
3. In the **Asset Type** page:
  1. Set asset type to **Clothing**, then use the dropdown menu to choose the clothing type of your layered accessory.
  2. Click the **Next** button. A preview panel displays with a default character wearing your layered accessory.
4. [Test](/docs/en-us/avatar/accessory-fitting-tool.md#test-accessories) out various sample characters and animations to make sure your layered accessory is deforming and moving correctly.
  - If necessary, make minor cage adjustments using the editing features. Larger cage changes may require returning to your third-party modeling software and re-exporting the asset.
5. After previewing your asset, click the **Generate MeshPart Accessory** button. Your 3D model populates in your project as an `Class.Accessory` object.

With this `Class.Accessory` object, you can perform any of the following:

- Begin the process of [uploading and publishing](/docs/en-us/marketplace/publish-to-marketplace.md#upload-an-asset) the layered accessory to the Marketplace.
- Use the layered accessory in your current game by equipping it to character models with [HumanoidDescription](/docs/en-us/characters/appearance.md#manually-modify-appearance), or by dragging and dropping the layered accessory under the appropriate character `Class.Model` object.
- Save the layered accessory to your [Toolbox](/docs/en-us/projects/assets/toolbox.md) or make it public on the [Creator Store](/docs/en-us/production/creator-store.md) to use within any of your games or share with other creators.
