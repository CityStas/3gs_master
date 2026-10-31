---
title: "Export layered accessories"
url: /docs/en-us/avatar/layered-accessories/export
last_updated: 2026-10-30T19:55:37Z
description: "Use the appropriate export settings in Blender and Maya to generate Studio-ready .fbx files."
keywords: ["Layered clothing","Layerable accessories","Layered clothing accessories"]
---

# Export layered accessories

When you are ready to export a layered accessory model that meets Roblox's [layered accessory specifications](/docs/en-us/avatar/layered-accessories/specifications.md), it's important to review the following prerequisite information and step-by-step instructions for the `.fbx` or `.gltf` export files so that your creation takes advantage of all of Studio's [Importer](/docs/en-us/studio/importer.md) features.

This is particularly important for layered accessory models because they contain all the mesh and texture data, including the rig and influence data that's essential for accessories to move and animate properly with character bodies across the platform.

> **Info:** **For other types of 3D models:**- [General mesh](/docs/en-us/art/modeling/export-requirements.md) export settings. - [Rigid accessory](/docs/en-us/avatar/rigid-accessories/export.md) export settings.
## Prerequisites

Before you export your custom layered accessory, ensure that you are only exporting the Roblox supported objects related to your model. If you have any modifiers to your mesh or project objects, make sure to apply or delete them before export.

You can export layered accessory models with the following object structure:

| <ul><li>Armature parent<ul><br><li>Bones / joints</li><li>Primary mesh object</li></ul></li><li>Cage parent object<ul><br><li>Inner cage mesh object</li><li>Outer cage mesh object</li></ul></li></ul> | ![Blender layered accessory data model example](../../assets/modeling/skinned-meshes/Clothing-Data-Model.png) |
| --- | --- |

You can also export shoes together. Even though left and right shoes are separate layered accessories, you can either export the left and right shoe individually, or export both shoes at the same time using the following structure:

| <ul><li>Armature parent<ul><br><li>Bones / joints</li><li>Left shoe mesh object</li><li>Right shoe mesh object</li></ul></li><li>Cage parent object<ul><br><li>Left shoe inner cage</li><li>Left shoe outer cage</li><li>Right shoe inner cage</li><li>Right shoe outer cage</li></ul></li></ul> | ![Shoe layered accessory data model example](../../assets/modeling/skinned-meshes/Shoe-Data-Model.png) |
| --- | --- |

> **Warning:** Each shoe must include their own inner and outer cage.
## Blender export settings

Blender allows you to export your layered accessory as either a `.fbx` or `.gltf` file. If you are exporting it as a `.fbx` file, familiarize yourself with [Blender's FBX scaling](/docs/en-us/art/blender.md#adjust-scale-fbx) to ensure that you successfully import the model into Studio at the correct scale.

To export your layered accessory in Blender as a `.fbx` file:

1. In the topbar, click **File** > **Export** > **FBX (.fbx)**. The **Blender File View** window displays.
2. On the right-hand side, set **Path Mode** to **Copy**, then toggle the **Embed Textures** button.
3. In the **Transform** section, set **Apply Scalings** to **FBX Unit Scale**. If you run into scaling issues on import, see [Blender FBX scaling](/docs/en-us/art/blender.md#adjust-scale-fbx) for alternative approaches.
4. In the **Armature** section, uncheck **Add Leaf Bones**.
5. Click the **Export FBX** button and save the `.fbx` to the directory of your choice.

> **Success:** You now have a `.fbx` file that you can [import into Studio](/docs/en-us/avatar/layered-accessories/import.md) as a `Class.Model` layered accessory. Once the layered accessory is in Studio, you can use the [Accessory Fitting Tool](/docs/en-us/avatar/accessory-fitting-tool.md) to convert the model into an accessory.
## Maya export settings

To export your layered accessory in Maya as a `.fbx` file:

1. In the topbar, click **File** > **Export All**. The **Export All** window displays.
2. Near the bottom of the window, click the **Files of type** dropdown, then select **FBX export**.
3. On the right-hand side of the window, navigate to the **Options...** section.
4. In the **Geometry** section, enable **Smooth Mesh** and **Referenced Asset Content**.
5. If you need to import textures as a `.png`, in the **Embed Media** section, enable **Embed Media**.
6. In the **Advanced Options** section,
  - Navigate to **Units**, then enable **Automatic**.
  - Navigate to **Axis Conversion**, then set the **Up Axis** property to **Y**.
7. Click the **Export All** button and save the `.fbx` to the directory of your choice.![Screenshot of Maya export settings for exports with animation.](../../assets/accessories/lc-requirements-maya-settings-with-animation-layeredaccessories.png)

> **Success:** You now have a `.fbx` file that you can [import into Studio](/docs/en-us/avatar/layered-accessories/import.md) as a `Class.Model` layered accessory. Once the layered accessory is in Studio, you can use the [Accessory Fitting Tool](/docs/en-us/avatar/accessory-fitting-tool.md) to convert the model into an accessory.
