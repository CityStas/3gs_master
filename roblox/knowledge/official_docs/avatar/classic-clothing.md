---
title: "Classic clothing"
url: /docs/en-us/avatar/classic-clothing
last_updated: 2026-10-30T19:55:37Z
description: "Classic clothing are decals you can apply to a classic character model's surface. You can create classic clothing items on Roblox and upload them to the Marketplace."
---

# Classic clothing

> **Warning:** Many user-generated avatars on the Marketplace do not support 2D classic clothing. For information on creating modern 3D cosmetics, including rigid accessories and clothing items, see [Get started](/docs/en-us/avatar.md).

Create and sell your first 2D classic clothing item.

A high-level overview of avatar items on Roblox.

**Classic clothing** are 2D assets that wrap around specific areas of the avatar's body, such as their front torso for t-shirts or their torso and legs for pants. This is the most basic type of avatar item to create and sell on the [Marketplace](https://www.roblox.com/catalog) as you just need an image editor and web browser for the creation process.

To create classic clothing items:

1. Decide on the [type of classic clothing](#types-of-classic-clothing) you'd like to create.
2. [Create](#create-classic-clothing) an image for your asset using an image editor of your choice.
3. [Test](#test-classic-clothing) your creation in Studio to ensure it looks as intended.
4. [Upload](#upload-classic-clothing) the image file to the Marketplace through a web browser.

## Types of classic clothing

There are three types of classic clothing: **T-shirts**, **Shirts**, and **Pants**. Each type of classic clothing has different design and format requirements.

_T-shirts_

_Shirts_

_Pants_

### T-shirts

T-shirts are a square image, such as 512x512 pixels. When properly configured, classic t-shirts display on the front torso of a blocky character.

### Shirts and pants

Classic shirts and pants are image assets that wrap around an avatar's body. Because classic shirts and pants have specific size requirements, download and modify the provided template files to begin creating these assets.

_[Shirt (torso and arms)](../assets/accessories/classic-clothing/Classic-Clothing-Templates.zip)_

_[Pants (torso and legs)](../assets/accessories/classic-clothing/Classic-Clothing-Templates.zip)_

| Shape | Pixel size (width x height) | Clothing parts |
| --- | --- | --- |
| Large square | 128 × 128 | **FRONT** and **BACK** |
| Tall rectangle | 64 × 128 | Sides of torso (**R**, **L**) <br> Sides of arms and legs (**L**, **B**, **R**, **F**) |
| Wide rectangle | 128 × 64 | **UP** and **DOWN** |
| Small square | 64 × 64 | Top and bottom of arms and legs (**U**, **D**) |

## Create classic clothing

To begin creating classic clothing:

1. If you are creating a classic shirt or pants, [download and unzip](../assets/accessories/classic-clothing/Classic-Clothing-Templates.zip) the following clothing templates to use as a canvas for your art.
2. Modify the image in an image editor of your choice.
3. Export the image as a `.png` or `.jpg` before testing and uploading it in Studio.

When applying clothing to avatars in Roblox, some limits exist with the templates and may require some testing to get right, as shown in the following examples:

_The shoe designs in this example are near the bottom of the leg regions (L, B, R, F) but don't extend too far up. This provides a distinct separation between the shoes and the bottom of the jeans._

_The shoe designs in this example extend too far up the leg regions (L, B, R, F) which make them appear as if they're part of the pants. The same issue may occur near other joints on the avatar's body._

## Test classic clothing

To ensure the best quality results, it's recommended to test your classic clothing in Studio before uploading or selling your asset on the Marketplace. The testing process does not require any fees.

To test your classic clothing:

1. From the toolbar's **Avatar** tab, click **Character**.
2. Choose a **Block Avatar** rig type from the popup menu. An avatar mannequin named **Rig** appears in the 3D workspace.
3. In the **Explorer** window, hover over the **Rig** object, click the **⊕** button and insert either a **ShirtGraphic** (T‑shirt), **Shirt**, or **Pants** object according to the clothing you want to test.
4. Locate and select the new **Shirt Graphic** or **Clothing** object parented under **Rig**._Shirt Graphic (T-shirt)__Clothing object (Shirt/Pants)_
5. In the **Properties** window, locate the associated property as follows: | Clothing Type | Parent Class | Property |
| --- | --- | --- | | **T-Shirt** | `Class.ShirtGraphic` | `Class.ShirtGraphic.Graphic\|Graphic` | | **Shirt** | `Class.Shirt` | `Class.Shirt.ShirtTemplate\|ShirtTemplate` | | **Pants** | `Class.Pants` | `Class.Pants.PantsTemplate\|PantsTemplate` |
6. Click inside the property's row and select the image you uploaded to Roblox. This applies the clothing texture to the **Rig** character.

## Upload classic clothing

After creating and testing your classic clothing design, as long as you meet the [creator requirements](/docs/en-us/marketplace/marketplace-policy.md#creator-requirements), you can upload and sell your clothing item on the Marketplace for an [upload fee](/docs/en-us/marketplace/marketplace-fees-and-commissions.md#upload-fees) of **80 Robux** per submission.

To upload a custom clothing item:

1. Navigate to your [Creator Dashboard](https://create.roblox.com/dashboard/creations).
2. Navigate to **Avatar Items**, then select the **Classics** tab.
3. Drag and drop your image file into the upload box. Alternatively, you can click **Upload Asset** and upload your file on the next page.
4. On the **Upload Asset** page, set the **Asset Type** dropdown to **T-Shirt**, **Shirt**, or **Pants**.
5. Complete the **Name** and **Description** fields. These fields help users find your assets and allow you to organize your creations.
6. Click the **Upload** button at the bottom of the page.

## Manage classic clothing

To see your moderation status, place your item on sale, or modify your item settings:

1. Navigate to your [Creator Dashboard](https://create.roblox.com/dashboard/creations).
2. Navigate to **Avatar Items**, then select the **Classics** tab.
3. Use the **Classic Type** dropdown to filter by the type of classic clothing creation.
4. Click on the asset to navigate to the asset's **Configure** page.
5. Modify the following fields:
  1. **Item Name** — The public-facing name of the asset.
  2. **Item Description** — The public-facing description of the asset.
  3. **On Sale** — When enabled, users can view and purchase this item on the Marketplace.
  4. **Set a price** — The value of Robux that the creation sells for on the Marketplace.
