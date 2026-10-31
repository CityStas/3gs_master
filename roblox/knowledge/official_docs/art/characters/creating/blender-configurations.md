---
title: "Blender configuration"
url: /docs/en-us/art/characters/creating/blender-configurations
last_updated: 2026-10-30T19:55:33Z
description: "Roblox avatar template projects have several helper configurations and settings to help expedite the character creation process."
---

# Blender configuration

The Blender project files of each template include additional helper configurations that are not included in the raw `.fbx` template files. If you intend on using Blender for your character creation process, it's important to understand the additions included in the `.blend` versions of the template and what they do.

## Hierarchy

The following is a breakdown of what is included in each Blender template file:

- **Cage**: Contains the character's 15 outer body cage meshes.
- **Joints**: The parent armature object contains the following objects:
  - **Bones** that make up the character's rigging armature.
  - **_Geo** mesh objects that make up the avatar appearance.
  - **_Att** attachment objects that define where accessories attach when equipped.
  - **Animation data** for saving facial animation data and poses.
- **Fill** and **Sun**: These objects are used to provide lighting, allowing you to preview your characters in neutral lighting similar to a Studio baseplate. These are **not** part of the avatar character.

![Head-Related Meshes](../../../assets/art/blender-ui/Blender-Project-Objects.png)_Blender Project Hierarchy_

## Disabled objects

When using the template project files for Blender, you might notice some objects, like attachment objects, are permanently hidden in the Viewport even when toggling the **Hide In Viewport** icon. Since attachment objects are often not modified until the end of the character creation process, these objects have **Disable In Viewport** enabled to make the organization of your project more efficient, especially when bulk toggling object visibility.

If you need access to disabled objects, use the following instructions to access the **Disable In Viewport** toggle:

1. In your Outliner, click the **Filter** dropdown.
2. Enable the **Disable In Viewport** filter.
3. The **Disable In Viewport** icon now appears next to every object in the Outliner. Toggle the icon to change the Disabled status for your objects.

## Custom skin tones

The Blender project files include a shader configuration that allows you to preview custom skin tones, similar to how they display in Roblox if users customize their skin tones.

Textures with full or partial transparency allow the underlying `Class.Part.Color` to reveal through the applied texture, enabling a user to personalize their avatar character with custom skin tones.

_A texture map example that uses low opacity to reveal underlying skin color and full opacity to apply a fully-opaque color to the undergarments, eyebrows, mouth, and eyes._

_The same avatar character using the same texture map. Each model has different underlying part colors except where the texture map applies a full color._

### Preview skin tones

> **Warning:** You must use **Blender 3.4+** to ensure that the helper shader configurations render correctly. If you are using a previous version of Blender, textures may not render as expected.

The Blender project file includes shader configurations that allow you to preview custom skin tones similar to how they appear in Studio. These custom colors do not export with the model, but can provide you a quick visual reference for how a custom skin color and texture might look in Roblox.

For this Blender shader configuration, keep in mind the following requirements:

- You must switch to **Viewport Shading** mode for textures to render as expected.
- When swapping out textures, the normal map's colorspace reverts to **SRGB** instead of **NonColor**. If this occurs, you might need to change it back in order for the normal map to render correctly.

To preview your character's skin tone in Blender:

1. In **Layout**, select any geometry object, such as **Head_Geo**.
2. Navigate to the **Shading** tab, then in the node panel, set the **Shader Type** dropdown menu to **Object**.
3. Find the **PartColor** node that is attached to the **Mix** node, then pick a color and value on the node to apply a reference custom skin tone.

### Export setup

While the skin tone preview is a critical element to verifying your templates color and tone compatibility in Roblox, it prevents your color texture map from automatically being packaged with the final `.fbx` file. There are two ways to resolve this before exporting your model:

- In the **Shading** tab, disconnect the **Mix** node and replace it with the **ColorMap** node.
- Export your textures manually as separate image files and add them later in Studio.

For instructions on how to perform either export workflow, see [Export textures](/docs/en-us/art/characters/creating/export-textures.md).

## Scene scale

> **Info:** You can skip this section if you are using a Blender downloadable template. The `.blend` versions of the templates already contain many of the project settings required when setting up a Blender project configuration.

When creating Roblox assets in a modeling application, it's important to ensure your `.fbx` exports scale correctly. During export, set **Transform** > **Apply Scalings** to **FBX Unit Scale**.

If you run into scaling issues on import, see [Blender FBX scaling](/docs/en-us/art/blender.md#adjust-scale-fbx) for alternative approaches.

## Animation range

> **Info:** You can skip this section if you are using a Blender downloadable template. The `.blend` versions of the templates already contain many of the project settings required when setting up a Blender project configuration.

For custom characters with facial animation, ensure that the timeline range is set between 0 and 330:

1. In the top right of the Animation Panel, click and set **Start** to `0`.
2. In the top right of the Animation Panel, click and set **End** to `330`.

> **Info:** After you change your project settings, you can set these as your default Blender project settings by navigating to **File** > **Defaults** > **Save Startup File**.
