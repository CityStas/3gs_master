---
title: "Export character model"
url: /docs/en-us/art/characters/creating/export-character
last_updated: 2026-10-30T19:55:33Z
description: "Export your character model from Blender using the correct settings and processes."
---

# Export character model

> **Warning:** It's important to test your assets multiple times at every point of the asset creation process, whether it is within Blender or after importing into Studio. See [Test characters](/docs/en-us/avatar/character-bodies/test.md) for more information.

Whether you are exporting your character for testing, or are performing a final export out of Blender, you must apply the appropriate export settings to ensure that Blender exports the proper character data.

To export your character:

1. In the topbar, navigate to **File** > **Export** > **FBX (.fbx)**. The Blender file browser window displays.
2. Set **Path Mode** to **Copy** and enable the **Embed Textures** icon.
3. In the **Include** section, enable **Custom Properties**.
4. Expand the **Armature** section and disable **Add Leaf Bones**.
5. Enable **Bake Animation**, expand the section, then:
  1. Disable **NLA Strips**, **All Actions**, and **Force Start/End Keyframes**.
  2. Set **Simplify** to **0.0**.
6. Click the **Export FBX** button and save the `.fbx` to the directory of your choice.

> **Warning:** After exporting your .fbx file, see [Test character bodies](/docs/en-us/avatar/character-bodies/test.md) for steps on importing your character model into a test place and verifying your avatar and related components.
> **Success:** After importing the `Class.Model` character to Studio, you can now perform the following with this asset: - [Upload the character](/docs/en-us/marketplace/publish-to-marketplace.md) to the Marketplace. - Use the humanoid character on an existing game by applying a [HumanoidDescription](/docs/en-us/characters/appearance.md#manually-modify-appearance)to the `Class.Model` object. - Save the asset to your [Toolbox](/docs/en-us/projects/assets/toolbox.md) to share or use within any of your games.
