---
title: "Export from Blender"
url: /docs/en-us/art/accessories/creating-rigid/exporting
last_updated: 2026-10-30T19:55:32Z
description: "Use Blender's .fbx exporter with the correct settings to create a Studio-ready asset."
---

# Export from Blender

After modeling and texturing your asset, you can begin the process of **exporting** your Blender project as a `.fbx` or `.gltf`. For up-to-date settings, see [Export settings](/docs/en-us/art/modeling/export-requirements.md).

> **Warning:** If you are creating your own accessory object, it's important to clean up your project, which can involve deleting or removing any extra objects, such as lights, cameras, or mannequins, to ensure you only export the accessory mesh, and applying any modifiers to your mesh object.

To export your model as a `.fbx`:

1. In the topbar, click **File** > **Export** > **FBX (.fbx)**. The **Blender File View** window displays.
2. On the right-hand side, set **Path Mode** to **Copy**, then toggle the **Embed Textures** button.
3. In the **Transform** section, set **Apply Scalings** to **FBX Unit Scale**. If you run into scaling issues on import, see [Blender FBX scaling](/docs/en-us/art/blender.md#adjust-scale-fbx) for alternative approaches.
4. Click the **Export FBX** button.

> **Success:** You've completed the exporting section of this tutorial. If desired, download a [reference sample](../../../assets/art/accessories/creating-rigid/Chest-Texturing-Complete.fbx) of this exported file for comparison. You can use this reference in the next importing step.
