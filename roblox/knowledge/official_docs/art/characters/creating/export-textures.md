---
title: "Export textures"
url: /docs/en-us/art/characters/creating/export-textures
last_updated: 2026-10-30T19:55:33Z
description: "Export your character textures from Blender using the correct settings and processes."
---

# Export textures

> **Warning:** It's important to test your assets multiple times at every point of the asset creation process, whether it is within Blender or after importing into Studio. For more information, see [Test character bodies](/docs/en-us/avatar/character-bodies/test.md).

Whether you are exporting your character for testing, or are performing a final export out of Blender, you must apply the appropriate export settings to ensure that Blender exports the proper character data.

## Export textures

Including the default PBR textures, your template character includes four separate image maps that make up its surface appearance. Depending on your workflow, you can choose to embed the image maps to your export file or export the textures separately as image files. Both methods have advantages:

- [Embedding textures](#embed-textures) simplifies your export by packing all of your textures within the single `.fbx` file.
- [Exporting texture images](#export-textures) directly allows you direct access to the image textures, so you can test and swap them more quickly.

### Embed textures

Embedding the texture maps to your `.fbx` export can simplify the Blender export and Studio import process. When embedding your textures with Roblox's template files, you need to make a quick adjustment to custom skin tone shader nodes in the Blender file.

_Default node configuration: Mix node connected to Base Color_

_Exportable node configuration: Color node connected directly to Base Color_

To prepare your textures to embed with export:

1. In **Object** mode, select any part of the character.
2. Navigate to the **Shading** tab, then in the node editor, set **Shader Type** to **Object**.
3. Find the node that connects to the **Principled BSDF's Base Color** node.
4. Click and drag the line from **Base Color** to disconnect the node.
5. Find the **file26** node with the color texture map and click and drag the **Color** to the **Principled BSDF's Base Color** node.

### Unpack image files

As an alternative to embedding textures, you can export your texture files as separate `.png` image files, which allows you to quickly access and swap image texture maps.

To export your texture image files:

1. Navigate to **File** > **External Data** > **Unpack Resources**.
2. Select **Use files in current directory** to save in the same directory as your project. Blender exports your image files to a textures directory in your project's parent directory.
