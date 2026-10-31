---
title: "Export settings"
url: /docs/en-us/art/modeling/export-requirements
last_updated: 2026-10-30T19:55:35Z
description: "Use the appropriate export settings in Maya and Blender to generate Studio-ready .fbx files."
---

# Export settings

Export your mesh or model as a `.fbx` to take advantage of all of Studio's 3D import features. When rigging or skinning a model, a `.fbx` export contains both the rig and influence data you need to later [import](/docs/en-us/parts/meshes.md#import-meshes) into Studio.

Check that your model meets Roblox's [modeling specifications](/docs/en-us/art/modeling/specifications.md) before exporting to ensure Studio compatibility. Specific types of assets, like characters and accessories, have additional specifications:

> **Warning:** **If creating other types of 3D models:**- For rigid accessories, see [accessory specifications](/docs/en-us/avatar/rigid-accessories/specifications.md) and [accessory export settings](/docs/en-us/avatar/rigid-accessories/export.md). - For layered accessories, see [layered accessory specifications](/docs/en-us/avatar/layered-accessories/specifications.md) and [layered export settings](/docs/en-us/avatar/layered-accessories/export.md). - For avatar characters, see [avatar specifications](/docs/en-us/avatar/character-bodies/specifications.md) and [avatar export settings](/docs/en-us/avatar/character-bodies/export.md).
## Blender

To export the `.fbx` file in Blender:

1. In the topbar, click **File**. A pop-up menu displays.
2. Select **Export**, then **FBX (.fbx)**. The **Blender File View** window displays.
3. On the right-hand side, change **Path Mode** to **Copy**, then toggle the **Embed Textures** button.![Blender export sidebar showing Path Mode set to Copy and the Embed Textures button enabled.](../../assets/modeling/skinned-meshes/Blender-Export-Settings-1.png)
4. Set **Transform** > **Apply Scalings** to **FBX Unit Scale**. If you run into scaling issues on import, see [Blender FBX scaling](/docs/en-us/art/blender.md#adjust-scale-fbx) for alternative approaches.![Blender export sidebar showing Apply Scalings set to FBX Unit Scale.](../../assets/modeling/skinned-meshes/Blender-Export-Settings-5.png)
5. Under the **Armature** section, disable **Add Leaf Bones**.![Blender export sidebar showing Transform Scale set to .01](../../assets/modeling/skinned-meshes/Blender-Export-Settings-3.png)
6. Unless exporting content with animation keyframes, such as a walk cycle or a character with [facial animation data](/docs/en-us/avatar/dynamic-heads.md), disable **Bake Animation**.![Blender export sidebar showing Add Leaf Bones as unchecked](../../assets/modeling/skinned-meshes/Blender-Export-Settings-4.png)
7. Click the **Export FBX** button.

## Maya

To export a mesh in Maya as a `.fbx` file:

1. In the topbar, click **File**. A pop-up menu displays.
2. Select **Export All**. The **Export All** window displays.
3. Near the bottom of the window, click the **Files of type** dropdown, then select **FBX export**.
4. On the right-hand side of the window, navigate to the **Options...** section.
5. In the **Geometry** section, enable **Smooth Mesh** and **Referenced Asset Content**.
6. In the **Animation** section, disable **Animation**, unless you need to import an animation to Studio. Some avatar assets require animation.
  1. If you are exporting animation, enable **Bake Animation**.
7. If you need to import textures as a `.png`, in the **Embed Media** section, enable **Embed Media**.
8. In the **Advanced Options** section,
  - Navigate to **Units**, then enable **Automatic**.
  - Navigate to **Axis Conversion**, then set the **Up Axis** property to **Y**.
9. Click the **Export All** button.![Maya export sidebar showing Bake Animation as unchecked](../../assets/accessories/lc-requirements-maya-settings.png)
