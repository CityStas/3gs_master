---
title: "Convert"
url: /docs/en-us/art/accessories/creating/converting
last_updated: 2026-10-30T19:55:32Z
description: "Use the Accessory Fitting Tool to convert a Model object to an Accessory."
---

# Convert

With the `Class.Model` in your project, the last step in the process of clothing creation requires you to convert this object to a standard `Class.Accessory` that avatars can equip. Using the [Accessory Fitting Tool](/docs/en-us/avatar/accessory-fitting-tool.md) (AFT), convert the model object to a `Class.Accessory` that you can then use in your game or publish to the Marketplace.

To generate the accessory object:

1. In the **Avatar** tab, click **Accessory** to open the AFT. The **Accessory Fitting Tool** panel displays.
2. In the panel:
  1. Select the **Part** field, then in the **Explorer** window, select the layered accessory `Class.MeshPart` object.
  2. Back in the panel, click the **Next** button. The **Asset Type** page displays.
3. In the **Asset Type** page:
  1. Set asset type to **Clothing**, then use the dropdown menu to select the clothing type. This tutorial sets it to **Shirt**.
  2. Click the **Next** button. A preview panel displays with a default character wearing your layered accessory.
4. Test out various sample characters, clothing, and animations. If necessary, make minor cage adjustments using the editing features, or larger cage changes back in your third-party modeling software. For more information on this process, see [Accessory Fitting Tool - Test accessories](/docs/en-us/avatar/accessory-fitting-tool.md#test-accessories).
5. After previewing your asset, click the **Generate MeshPart Accessory** button. Your 3D model populates in your project as an `Class.Accessory` object.

_Clothing accessory in viewport_

_Clothing accessory in Explorer_

> **Success:** Congratulations, you've completed the layered accessory tutorial. With your new `Class.Accessory`, you can perform any of the following: - [Upload the accessory](/docs/en-us/art/accessories/creating-rigid/publishing.md) to the Marketplace. - Use the accessory in your current game by equipping it to character models with a [`HumanoidDescription`](/docs/en-us/characters/appearance.md#manually-modify-appearance), or by dragging and dropping the accessory under the appropriate character `Class.Model` object. - Save the accessory to your [Toolbox](/docs/en-us/projects/assets/toolbox.md) to share or use within any of your games.
