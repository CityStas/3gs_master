---
title: "Export emotes"
url: /docs/en-us/avatar/emotes/export
last_updated: 2026-10-30T19:55:37Z
description: "Use the appropriate export settings in Maya and Blender to generate Studio-ready .fbx files."
---

# Export emotes

When you are ready to export animation data that meets Roblox's [emote specifications](/docs/en-us/avatar/emotes/specifications.md), it's important to review the following prerequisite information and step-by-step instructions for the `.fbx` or `.gltf` export files so that you don't run into any errors for the [import](/docs/en-us/avatar/emotes/import.md) process.

> **Info:****How do I create animation data?** Creators typically use a third-party modeling tool like Blender or Maya to animate a character model. Once the animation is complete, you can export both the model and the animation data as a `.fbx` or `.gltf` file.
## Prerequisites

When you export a character model with full body animation or FACS animation data, ensure that your animation timeline's **Start** and **End** include the entire range of your animation.

![Zoom-in of Blender animation track indicating a Start value of 0 and End value of 308.](../../assets/art/avatar/basic-creation/Blender-Animation-Start-End.png) ## Blender export settings

Blender allows you to export your character model and animation data as either a `.fbx` or `.gltf` file. If you are exporting it as a `.fbx` file, familiarize yourself with [Blender's FBX scaling](/docs/en-us/art/blender.md#adjust-scale-fbx) to ensure that you successfully import the model into Studio at the correct scale.

To export your character model with animation data in Blender as a `.fbx` file:

1. Ensure your project's animation timeline has the correct **Start** and **End** range of all your keyframes.
2. In the topbar, click **File** > **Export** > **FBX (.fbx)**. The **Blender File View** window displays.
3. On the right-hand side, set **Path Mode** to **Copy**, then toggle the **Embed Textures** button.
4. In the **Include** section, enable **Custom Properties**.
5. In the **Transform** section, set **Apply Scalings** to **FBX Unit Scale**. If you run into scaling issues on import, see [Blender FBX scaling](/docs/en-us/art/blender.md#adjust-scale-fbx) for alternative approaches.
6. In the **Armature** section, uncheck **Add Leaf Bones**.
7. Enable and expand **Animation**, then:
  1. Uncheck **NLA Strips**, **All Actions**, and **Force Start/End Keyframes**.
  2. Set **Simplify** to `0.0`.
8. Click the **Export FBX** button and save the `.fbx` to the directory of your choice.

![Screenshot of Blender export settings](../../assets/art/avatar/basic-creation/Export-Settings.png) ## Maya export settings

> **Info:** For additional context on exporting animations from Maya, see the [Export avatar animations from Maya](/docs/en-us/art/characters/export-avatar-animations-from-maya.md) tutorial.

To export your character model with animation data in Maya as a `.fbx` file:

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
