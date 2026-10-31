---
title: "Accessory Fitting Tool"
url: /docs/en-us/avatar/accessory-fitting-tool
last_updated: 2026-10-30T19:55:36Z
description: "The Accessory Fitting Tool lets you adjust and test custom accessory models on different body types, animations, or custom assets."
keywords: ["Layered clothing","Layerable accessories","Layered clothing accessories","Rigid accessories"]
---

# Accessory Fitting Tool

The **Accessory Fitting Tool** (AFT) is a built-in Studio tool that allows you to test your custom models on multiple combinations of character bodies, animations, and accessories before generating the final `Class.Accessory` object. When testing your accessories, you can make minor fit and positional changes to ensure that you get the best result possible.

The AFT automatically handles the conversion of the custom `Class.Model` or `Class.MeshPart` based on your menu selections, allowing you to create [layered accessories](/docs/en-us/avatar/layered-accessories.md) or [rigid accessories](/docs/en-us/avatar/rigid-accessories.md). After generating an accessory, the AFT creates the correct `Class.Accessory` object hierarchy with any updated fit edits, sets the appropriate `AccessoryType` property, and generates any required body attachment points.

_Test and edit the orientation and placement of your rigid accessories._

_Test and edit the cages of your layered accessories._

> **Warning:** If you are intending to sell an accessory on the Marketplace, make sure your accessory model design adheres to [Marketplace policies](/docs/en-us/marketplace/marketplace-policy.md).
## Set up accessories

The first stage of the fitting workflow allows you to configure the type of accessory to correctly populate the correct fitting tools and generate the appropriate accessory object. When selecting the type of accessory, the following options are available:

- **Clothing**: Layered accessories that use an inner and outer cage to stretch and wrap around a character body and existing clothing items.
- **Accessory**: Rigid accessories that attach to a specific attachment point of a character body and remain static in that position and orientation.

Before using the AFT, ensure that you have the `Class.MeshPart` or `Class.Model` you intend to create into an accessory selectable in your project. As a reference, you can test the AFT using a reference [layered accessory](../assets/accessories/reference-files/Additional-FBX-assets.zip) or [rigid accessory](../assets/accessories/reference-files/Bow-rigid.rbxm) custom model.

To setup your accessories:

1. In the toolbar's **Avatar** tab, click **Accessory** to open the AFT. The **Accessory Fitting Tool** panel displays.
2. In the panel:
  1. Select the **Part** field, then in the **Explorer** window, select your accessory's respective `Class.MeshPart` or `Class.Model` object. The text field populates with the name of the object.
  2. Back in the panel, click the **Next** button. The **Asset Type** page displays.
3. In the **Asset Type** page:
  1. Select the correct asset type for your accessory:
    - If your asset is a layered accessory, select **Clothing**.
    - If your asset is a rigid accessory, select **Accessory**.
  2. Use the dropdown menu to choose the `AssetType` of your accessory.
  3. Set body type to the [body scale](/docs/en-us/avatar/character-bodies/specifications.md#body-scale) you determined while sculpting and sizing of the asset during the creation process.
    - **Classic**: Sets the scaling of the accessory to classic proportions.
    - **Proportions Slender**: Sets the `AvatarPartScaleType` value to `ProportionsSlender`.
    - **Proportions Normal**: Sets the `AvatarPartScaleType` value to `ProportionsNormal`.
    > **Info:** This setting does not affect layered accessories, and it only affects rigid accessories if the specific body part has a different `AvatarPartScaleType` `Class.StringValue` object. For more information, see [Rigid Accessories - AvatarPartScaleType](/docs/en-us/avatar/rigid-accessories/specifications.md#avatarpartscaletype).
  4. Click the **Next** button. A preview panel displays with a default character wearing your accessory.

## Test accessories

After you provide the initial accessory details, the AFT displays a preview panel. With the preview panel, you can test how your accessory looks on different combinations of character bodies, rigid accessories, layered accessories, animations, and custom assets in your game. If you notice any fitting issues with your accessory, you can use the [edit](#edit-accessory-fit) tools to make minor adjustments to your accessory.

> **Info:** At any point of the testing process, you can [initiate a playtest](/docs/en-us/studio/testing-modes.md#playtesting) to launch an instance of your game where your avatar is replaced with the currently selected character body and accessories from the AFT.
### With different bodies

You can select different character bodies to test the fit and wear of your accessories. The AFT supplies several default character body models you can use to ensure your accessories fit as expected.

_Bazooka Bones character preview_

_Magma Fiend character preview_

To test your accessory with a different character body:

1. In the tool's catalog, navigate to **Avatars** > **Default**.
2. Click one of the character model tiles. The preview loads with the selected character model.
  1. If two character tiles are selected, click a selected tile to deselect it.
  2. In the character preview, **click** and **drag** to rotate and **right-click** to pan to inspect your character.

### With other layered accessories

You can select multiple layered accessories to test the fit and layering of your caged accessories. The AFT supplies several default character models you can use to ensure your accessories fit as expected.

To test your accessory with a different layered accessory:

1. In the tool's catalog, navigate to **Clothing** > **Default**.
2. Click one or more of the available catalog items. The character preview loads with the selected clothing accessory.
  1. In the catalog, click an active tile to deselect the asset.
  2. In the character preview, **drag** and **drop** the accessory boxes to change the layer order.
  3. In the character preview, **click** and **drag** to rotate and **right-click** to pan to inspect your character.

### With animations

You can select different animations to test the movement of your accessories. The AFT supplies several default animation assets you can use to ensure your accessories fit as expected when a model is performing various movements.

To test your accessory with different animations:

1. In the tool's catalog, navigate to **Animations** > **Default**.
2. Click one of the animation asset tiles.
  1. In the catalog, press the play and pause icon to control the playback.
  2. In the character preview, **click** and **drag** to rotate and **right-click** to pan to inspect your character.

### With custom assets

You can add custom character body models, layered accessories, and animations that are part of your workspace to the AFT preview catalog. Use this functionality to verify that your accessory works with any other custom models or accessories they may interact with in your game.

To add custom assets:

1. Click the ⊕ icon next to the catalog search. A prompt appears, allowing you to choose a supported object.
2. Select any `Class.Accessory`, `Class.Model`, `Class.MeshPart`, `Class.Animation` or `Class.Folder` within the 3D viewport or **Explorer** window. The asset displays in the corresponding **Custom** category.

## Edit accessory fit

The AFT populates different fitting tools depending on the type of accessory you're creating.

### Layered accessories

When editing layered accessories, the following tools populate in the viewport:

| Icon | Description |
| --- | --- |
|  | Toggles the [Cage Editing](#cage-editing) interface in the viewport for making minor inner or outer cage changes to your clothing. |
|  | Toggles [auto-skinning](/docs/en-us/avatar/automatic-skinning-transfer.md#enable-automatic-skinning-transfer) between `EnabledPreserved` and `EnabledOverride`. Depending on the asset and skinning quality, auto-skinning may provide better results.<br><br><ul><li>`EnabledPreserved` uses the asset's original skinning data applied in a modeling software.</li><li>`EnabledOverride` transfers skinning data from the avatar character instead of using the asset's original skinning data.</li></ul> |
|  | Displays a button to **Bring Mannequin in View** which centers mannequin in front of the camera. |
|  | Centers the camera on the mannequin. |

#### Cage editing

When the Cage Editing interface is enabled, additional tools display in the viewport along with the vertices of the selected cage over the mannequin. This allows you to make positional edits to the cage and change how a layered accessory fits on a character body.

> **Warning:** You can use these cage editing tools for minor to moderate cage edits, but if your asset requires major fit or sculpting changes, it's recommended to edit the cage meshes directly in a third-party modeling software, then reimport the updated model into Studio.

Use the following cage editing tools to help visualize and edit any cage vertices:

| Icon | Description |
| --- | --- |
|  | Toggles the selection for the inner and outer cage vertices. When selected, the vertices of that specific cage are available to edit. |
|  | Sets the radius of influence when editing vertices of the cage mesh. When editing a cage vertex, nearby vertices follow the changes for efficient cage editing. <br> <br>A higher Falloff Distance applies influence to vertices further away from the origin. |
|  | Displays additional buttons:<ul><li>Bring Mannequin in View - centers camera on the mannequin.</li><li>Reset Inner/Outer Cage - resets any changes made to the selected cage.</li></ul> |
|  | Sets the opacity of the mesh or the cage vertices, allowing you to better see and access certain vertices and angles of your layered accessory. |

To make changes to the vertices of the currently selected cage:

1. In the toolbar, disable **Move** snapping. This enables you to make detailed changes to a vertex's position.
2. Select a vertex and use the **Move** tool to reposition. Changes to the cage apply immediately and display in the preview panel.
  1. Use the opacity sliders to better visualize the changes to your cage.
  2. Set the **Falloff Distance** depending on the number of vertices being adjusted at once.

### Rigid accessories

When fitting rigid accessories, a bounding box appears around the mannequin indicating the possible placement of that specific type of accessory. You can position, rotate, and scale objects within this bounding box to ensure your accessory fits on different character models.

_Adjust your rigid accessory fit within the bounding box._

_If the accessory is outside the appropriate space, the bounding box turns red._

### Create accessory

AFT applies any fit changes and generates the appropriate `Class.Accessory` instance in the workspace depending on the type of accessory selected and any configurations applied.

When you are ready to generate your accessory, select **Generate MeshPart Accessory**.

_Hierarchy generated for layered accessories._

_Hierarchy generated for rigid accessories._

With an accessory successfully created, you can now try the following:

- Begin the process of [uploading and publishing](/docs/en-us/marketplace/publish-to-marketplace.md) the accessory to the Marketplace.
- Use the accessory in your current game by equipping it to character models with [HumanoidDescription](/docs/en-us/characters/appearance.md#manually-modify-appearance), or by dragging and dropping the accessory under the appropriate character `Class.Model` object.
- Save the accessory to your [Toolbox](/docs/en-us/projects/assets/toolbox.md) or make it public on the [Creator Store](/docs/en-us/production/creator-store.md) to use within any of your games or share with other creators.
