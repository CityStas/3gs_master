---
title: "Export character bodies"
url: /docs/en-us/avatar/character-bodies/export
last_updated: 2026-10-30T19:55:36Z
description: "Use the appropriate export settings in Maya and Blender to generate Studio-ready .fbx files."
---

# Export character bodies

When you are ready to export a character body model that meets Roblox's [character body specifications](/docs/en-us/avatar/character-bodies/specifications.md), it's important to review the following prerequisite information and step-by-step instructions for the `.fbx` or `.gltf` export files so that your creation takes advantage of all of Studio's [Importer](/docs/en-us/studio/importer.md) features.

This is particularly important for character body models because they contain all the mesh and texture data, including the rig and influence data that's essential for characters to move and animate properly across the platform.

> **Warning:** If you are using Roblox's avatar template files, you must perform the [cleanup steps](/docs/en-us/art/characters/creating/combine-head-geometry.md) in order for the assets to properly validate.
> **Info:** **For other types of 3D models:**- [General mesh](/docs/en-us/art/modeling/export-requirements.md) export settings. - [Rigid accessory](/docs/en-us/avatar/rigid-accessories/export.md) export settings. - [Layered accessory](/docs/en-us/avatar/layered-accessories/export.md) export settings.
## Prerequisites

Before you export your custom character body:

- Ensure that you are only exporting the Roblox-supported objects related to your model. If you have any modifiers to your mesh or project objects, make sure to apply or delete them before export.
- While your mesh objects must be parented within an armature object, you can also parent your outer cage objects to a single empty object to simplify your workspace.![Screenshot of a Blender project Outliner with parent objects collapsed.](../../assets/art/avatar/Character-Data-Model-Collapsed.png)
- In the cage parent object, ensure you have an [outer cage](/docs/en-us/avatar/character-bodies/specifications.md#outer-cages) for each of your 15 body parts with appropriate naming affix.![Screenshot of the 15 outer cage meshes that you must include with a character export.](../../assets/art/avatar/Character-Data-Model-Cages.png)
- In the armature object, ensure that you include the all [15 mesh objects](/docs/en-us/avatar/character-bodies/specifications.md#body-parts) and [19 attachments](/docs/en-us/avatar/character-bodies/specifications.md#attachments) with the appropriate naming affix.![Screenshot of 15 child objects parented within an Armature object.](../../assets/art/avatar/Character-Data-Model-Joints.png)

> **Info:** For more information on supported modeling objects and proper configuration, see [Character specifications](/docs/en-us/avatar/character-bodies/specifications.md).

- When exporting character bodies with animation or FACS animation, ensure that your animation timeline **Start** and **End** include the entire range of your animations.

![Zoom-in of Blender animation track indicating a Start value of 0 and End value of 308.](../../assets/art/avatar/basic-creation/Blender-Animation-Start-End.png) ## Blender export settings

Blender allows you to export your character body as either a `.fbx` or `.gltf` file. If you are exporting it as a `.fbx` file, familiarize yourself with [Blender's FBX scaling](/docs/en-us/art/blender.md#adjust-scale-fbx) to ensure that you successfully import the model into Studio at the correct scale.

To export your character body in Blender as a `.fbx` file:

1. In the topbar, click **File** > **Export** > **FBX (.fbx)**. The **Blender File View** window displays.
2. On the right-hand side, set **Path Mode** to **Copy**, then toggle the **Embed Textures** button.
3. In the **Include** section, enable **Custom Properties**.
4. In the **Transform** section, set **Apply Scalings** to **FBX Unit Scale**. If you run into scaling issues on import, see [Blender FBX scaling](/docs/en-us/art/blender.md#adjust-scale-fbx) for alternative approaches.
5. In the **Armature** section, uncheck **Add Leaf Bones**.
6. Enable and expand **Animation**, then:
  1. Uncheck **NLA Strips**, **All Actions**, and **Force Start/End Keyframes**.
    > **Info:** Ensure your project animation timeline has the correct **Start** and **End** range of all your keyframes.
  2. Set **Simplify** to `0.0`.
7. Click the **Export FBX** button and save the `.fbx` to the directory of your choice.

![Screenshot of Blender export settings](../../assets/art/avatar/basic-creation/Export-Settings.png)
> **Success:** You now have a `.fbx` file that you can [import into Studio](/docs/en-us/avatar/character-bodies/import.md) as a `Class.Model` character. Once the character body is in Studio, you can: - [Test your character](/docs/en-us/avatar/character-bodies/test.md) using various Studio tooling and workflows. - [Upload the character](/docs/en-us/marketplace/publish-to-marketplace.md) to the Marketplace. - Use the character in an existing game project by applying a [HumanoidDescription](/docs/en-us/characters/appearance.md#manually-modify-appearance) to the `Class.Model` object. - [Save the character](/docs/en-us/projects/assets/toolbox.md) to your **Toolbox** to use within any of your games or share with other creators.
## Maya export settings

To export your character body in Maya as a `.fbx` file:

1. In the topbar, click **File** > **Export All**. The **Export All** window displays.
2. Near the bottom of the window, click the **Files of type** dropdown, then select **FBX export**.
3. On the right-hand side of the window, navigate to the **Options...** section.
4. In the **Geometry** section, enable **Smooth Mesh** and **Referenced Asset Content**.
5. In the **Animation** section, enable **Animation**. Avatar characters with [dynamic heads](/docs/en-us/avatar/dynamic-heads.md) require animation data.
6. Enable **Bake Animation**.
7. If you need to import textures as a `.png`, in the **Embed Media** section, enable **Embed Media**.
8. In the **Advanced Options** section,
  1. Navigate to **Units**, then enable **Automatic**.
  2. Navigate to **Axis Conversion**, then set the **Up Axis** property to **Y**.
9. Click the **Export All** button and save the `.fbx` to the directory of your choice.![Screenshot of Maya export settings for exports with animation.](../../assets/accessories/lc-requirements-maya-settings-with-animation.png)

> **Success:** You now have a `.fbx` file that you can [import into Studio](/docs/en-us/avatar/character-bodies/import.md) as a `Class.Model` character. Once the character body is in Studio, you can: - [Test your character](/docs/en-us/avatar/character-bodies/test.md) using various Studio tooling and workflows. - [Upload the character](/docs/en-us/art/accessories/creating-rigid/publishing.md) to the Marketplace. - Use the character in an existing game project by applying a [HumanoidDescription](/docs/en-us/characters/appearance.md#manually-modify-appearance) to the `Class.Model` object. - [Save the character](/docs/en-us/projects/assets/toolbox.md) to your **Toolbox** to use within any of your games or share with other creators.
