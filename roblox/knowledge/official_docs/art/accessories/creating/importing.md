---
title: "Import"
url: /docs/en-us/art/accessories/creating/importing
last_updated: 2026-10-30T19:55:32Z
description: "Use the Importer to import your custom accessory into Studio."
---

# Import

After creating your t-shirt in Blender, import the `.fbx` using Studio's Importer tool to add the t-shirt to your project as a `Class.Model`.

Use the Importer to import your `.fbx` into Studio:

1. In the **Home** tab, click the **Import** button to open the Importer. A file browser opens.
2. Select your t-shirt's `.fbx` file. The Importer loads a preview of the layered accessory.
3. Select **Import**. The asset populates in your workspace as a `Class.Model` with the appropriate textures applied as a `Class.MeshPart.TextureID`.

**Textures didn't load correctly?**

If your textures didn't load correctly, you can import them manually using the [Asset Manager](/docs/en-us/projects/assets/manager.md):

1. In the **Asset Manager**, click the **Import** button. If you are unable to access the Asset Manager, save and publish your game first.
2. Upload your image file.
3. After moderation clears your image, select the `Class.MeshPart` parented within your imported `Class.Model`.
4. In the **TextureID** property, select the value field and add the asset ID of the texture image.
