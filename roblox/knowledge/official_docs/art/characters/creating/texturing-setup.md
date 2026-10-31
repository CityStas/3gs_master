---
title: "Texturing setup"
url: /docs/en-us/art/characters/creating/texturing-setup
last_updated: 2026-10-30T19:55:33Z
description: "Set up Blender to optimize your project for texturing the eyes and face of your template."
---

# Texturing setup

**Texturing** is the process of customizing the color, tone, and shading of your model's surface. Custom meshes and models use a 2D image, known as a texture map, to project various surface appearance elements onto your 3D object.

_Model after custom sculpting_

_Model after texturing_

Each template comes with a color texture map, which you can alter and modify using Blender's texture editing tools. Since most Roblox avatars can take advantage of custom skin tones, it's important to understand how to [preview custom skin tones](/docs/en-us/art/characters/creating/blender-configurations.md#preview-skin-tones) in Blender to verify how your final asset will look in a Roblox game.

For the purpose of demonstrating the basic texturing process, this tutorial goes over basic texture painting setup, applies a completely opaque texture over parts of the character eyes, and partially opaque details over the face. You can apply these same techniques to other parts of your character geometry.

> **Warning:** When texturing parts of your character model's body, ensure that your character model includes a modesty layer over sensitive regions. For more information, see [Marketplace policy - Modesty layers](/docs/en-us/marketplace/marketplace-policy.md#modesty-layers).
## Texture settings

If you're using a Blender downloadable template, it's important to keep in mind that Blender requires you to **manually** save your textures in the Texture Paint tab's 2D view window. If you just save your `.blend` project file, your textures do **_not_** save with it. This can cause you to lose hours of work if you don't periodically save your progress as you go.

Blender 5.2 and later versions offer a texture setting to override this behavior:

1. In the topbar, navigate to **Edit** > **Preferences**. The **Preferences** window displays.
2. In the vertical navigation, select the **Save & Load** tab.
3. In the **Blend Files** section, set **Save Modified Images** to **Always Save**.

## Set texture resolution

Roblox Studio supports a texture resolution of **1024 x 1024** for albedo texture maps. When using applications like Blender or Maya to texture paint directly on a model, extremely fine details may not paint as expected due to the resolution and level of detail of the painting.

_Texture painting at 1024 x 1024 resolution_

_Texture painting at 2048 x 2048 resolution_

When adding fine details to your texture, increase the image resolution of your texture map temporarily to **2048 x 2048** or **4096 x 4096**. After completing your texturing, change the image resolution back to **1024 x 1024** to bake in the changes.

To change your texture image resolution:

1. In the **Layout** tab, select the `Head_Geo`.
2. Switch to the **Texture Paint** tab, then in the 2D view window, select **Image** > **Resize**.
3. Set the texture size:
  - Use **2048** or **4096** for a higher resolution when creating detailed texture work.
  - Use **1024** for the default Roblox-supported resolution.
