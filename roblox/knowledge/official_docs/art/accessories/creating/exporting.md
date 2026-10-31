---
title: "Export"
url: /docs/en-us/art/accessories/creating/exporting
last_updated: 2026-10-30T19:55:32Z
description: "Use Blender's FBX export with specific settings when exporting a clothing asset."
---

# Export

It's important to follow the Blender export settings to ensure a Studio-compatible `.fbx` file. Before exporting your file, ensure that you've removed extra objects, such as lights, cameras, or mannequins, and applied or removed any active modifiers.

To export your file from Blender:

1. In the Outliner, unhide all objects, make them selectable, then select everything in your project.
2. In the topbar, click **File** > **Export** > **FBX (.fbx)**. The **Blender File View** window displays.
3. On the right-hand side, set **Path Mode** to **Copy**, then toggle the **Embed Textures** button.
4. In the **Include** section, enable **Selected Objects**.
5. In the **Transform** section, set **Apply Scalings** to **FBX Unit Scale**. If you run into scaling issues on import, see [Blender FBX scaling](/docs/en-us/art/blender.md#adjust-scale-fbx) for alternative approaches.
6. In the **Armature** section, disable **Add Leaf Bones**.
7. Disable **Bake Animation**.
8. Click the **Export FBX** button.

> **Success:** You've completed the exporting section of this tutorial. If desired, download a [reference sample](../../../assets/art/accessories/creating/Long_Sleeve_Export.fbx) of this exported file for comparison. You can use this reference in the next importing step.
