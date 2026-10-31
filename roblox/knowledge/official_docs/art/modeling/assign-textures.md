---
title: "Blender and Maya texture settings"
url: /docs/en-us/art/modeling/assign-textures
last_updated: 2026-10-30T19:55:35Z
description: "Learn to assign basic or PBR textures in Blender or Maya to natively import into Studio."
---

# Blender and Maya texture settings

This guide covers the process to assign texture images in Blender or Maya to your 3D model so that they import seamlessly into Studio. The import process supports both basic textures and realistic PBR textures, as long as they meet Roblox's [texture specifications](/docs/en-us/art/modeling/texture-specifications.md).

> **Warning:** The following information is **specific for applying makeup textures generic meshes**. For more information on reassigning textures for makeup assets, see [Reassign textures in Blender and Maya](/docs/en-us/avatar/makeup/reassign-textures.md).
## Blender

To assign Roblox-supported textures to your 3D model in Blender:

1. In the Outliner, select your mesh object.
2. In the Properties panel, navigate to the **Materials tab**.
3. Verify that your object has a Material assigned with the Surface set to `Principled BSDF`.
4. If no material is assigned, click the + symbol to add a material.
  1. Click the New button. A new `Principled BSDF` material populates.
5. Navigate to the **Shading tab**.
6. With your mesh object selected, check the node graph. There may already be texture image nodes connected to the `Principled BSDF` node.
7. In the node graph area, add a texture image node with right-click ⟩ **Add** ⟩ **Texture** ⟩ **Image Texture**.
8. In the new Image Texture node, click Open to open a file browser and insert your custom texture.
  > **Info:** Alternatively to steps 7-8, you can **drag and drop** texture file from another window into the graph editor space.
9. After adding image texture nodes and assigning the appropriate files, drag the `Image Texture` sockets to the appropriate sockets in the `Principled BSDF` node:
  - **Basic texture** or **PBR color/albedo**: connect `Color` to `Base Color`.
  - **Metallic texture**: connect `Color` to `Metallic`.
  - **Roughness texture**: connect `Color` to `Roughness`.
  - **Normal texture** images need to be added to a NormalMap node:
    1. Right-click in the graph-editor area and select **Add** ⟩ **Vector** ⟩ **Normal Map**.
    2. Connect Image Texture `Color` to NormalMap's `Color`.
    3. Connect NormalMap's `Normal` to PrincipledBSDF's `Normal` socket.

> **Success:** After replacing your PBR textures, [export the entire model](/docs/en-us/art/modeling/export-requirements.md#blender) and follow instructions to [import into Studio](/docs/en-us/studio/importer.md)
## Maya

To assign Roblox-supported textures to your 3D model in Maya:

1. In the Status Line near the top of the default layout, click on the Hypershade icon.
2. In the Create Window panel on the Hypershade popup, navigate to **Maya** ⟩ **Surface** and click **Standard Surface**. A surface node appears in the node editor.
  1. If adding a normal map, navigate to **Maya** ⟩ **Utilities** and click **Bump 2d**. A node required for normal maps appears in the node editor.
3. Drag and drop your PBR textures to the graph network.
  1. If adding a normal map, select the Bump 2d node, and change to Tangent Space Normals.
4. Select your model and navigate to your material you intend to assign. Right-click and hold over the material and select **Assign Material to Selection**.

> **Success:** After replacing your PBR textures, [export the model](/docs/en-us/art/modeling/export-requirements.md#maya) and follow instructions to [import into Studio](/docs/en-us/studio/importer.md).
