---
title: "Asset privacy"
url: /docs/en-us/projects/assets/privacy
last_updated: 2026-10-30T19:55:51Z
description: "Reference for the Roblox asset privacy system. Explains which asset types Asset Privacy affects (Images, Decals, Meshes only), how to enable Asset Privacy, how to grant and revoke permissions for collaborators and games, and which operations Asset Privacy does not affect."
---

# Asset privacy

The **asset privacy system** lets you control which creators and games can use your assets on Roblox. Assets can have one of two access privacy types:

- **Restricted** — Creators or games can only use the asset after the asset owner grants permission.
- **Open Use** — Any creator or game can use the asset.

If a creator or game doesn't have permission to use an asset, it cannot load in Studio, and a clickable error message displays in the [Output](/docs/en-us/studio/output.md) window. If a creator has permission to use an asset but the game they're working on does not, clicking the error message displays a pop-up window to allow the creator to grant permission to the game for any restricted assets.

When an asset is Open Use, Roblox doesn't need to check its permissions when it loads into a game because every creator and game can freely use it. However, when an asset is Restricted, Roblox **always** checks its permissions when it loads into a game or when a creator takes an action on the asset, such as inserting it into Studio, sharing it with another creator, or listing it on the [Creator Store](/docs/en-us/production/creator-store.md).

> **Info:** The asset privacy system controls which creators and games can use the asset, but others can still see its metadata, such as its name and description.
## What Asset Privacy controls

Asset Privacy controls only the default privacy state assigned to **Images**, **Decals**, and **Meshes** when they are created. No other asset types are affected.

**Asset Privacy does not affect:**

- **Audio, Video, Models, MeshParts, Animations, and Packages** — these types have their own creation defaults and are not changed by the Asset Privacy setting. If audio or other asset types are not loading or distributing as expected, Asset Privacy is not the cause.
- **Distributing assets on the Creator Store or Marketplace** — enabling or disabling Asset Privacy does not change your distribution eligibility or workflow.
- **Using your own assets in your own published games** — your assets are always accessible to you in your own games regardless of their privacy setting.
- **Assets created before Asset Privacy was enabled** — the setting only applies to newly created assets.
- **Sharing restricted assets** — Restricted does not mean permanently inaccessible. You can grant access to specific friends, groups, and games at any time through [Creator Dashboard](#grant-permissions), or use the [Revamped Asset Manager](https://devforum.roblox.com/t/beta-updates-to-revamped-asset-manager/4548832/1) to bulk-grant access across many assets at once.

**Key constraints:**

- **Open Use is irreversible.** Once an asset is set to Open Use, it cannot be changed back to Restricted.
- **Game grants are permanent.** Once you grant a game permission to use a restricted asset, that permission cannot be revoked.
- **Revoking a collaborator's access does not affect games.** If a collaborator has already used a restricted asset in a game, that game retains access even after the collaborator is removed.
- **The setting is not retroactive.** Only assets created after enabling Asset Privacy are Restricted by default.

## Restrict permissions

> **Info:** You can list your or your group's restricted assets by themselves or as a dependency of a restricted asset on the Creator Store. This allows creators to use your assets as you list them under models, mesh parts, or packages, and disallows them from accessing and repackaging your restricted asset dependencies.

By default, Images, Decals, and Meshes are created as **Open Use**. Enable **Asset Privacy** to make these asset types **Restricted** on creation instead. All other asset types are not affected by this setting.

### Enable Asset Privacy

Individual creators and groups can enable Asset Privacy via Creator Dashboard. When enabled, newly created Images, Decals, and Meshes are set to **Restricted** by default. All other asset types are unaffected by this setting.

> **Info:** Enabling Asset Privacy does not change your ability to distribute assets on the Creator Store or Marketplace, use your assets in published games, or share your assets with collaborators.

#### As a creator

To restrict your mesh, image, and decal assets on creation:

1. Navigate to the [Creator Dashboard](https://create.roblox.com/dashboard/creations).
2. In the top-right corner of the page, click on your username and select **Settings**.
3. In the left-hand navigation, select **Advanced**.
4. In the **Asset Privacy** section, enable the **Opt-in to restrict assets on creation** toggle. Every newly created Image, Decal, and Mesh is now Restricted by default.

#### As a group

> **Warning:** You can only complete this process if you are the group owner.

To restrict your group mesh, image, and decal assets on creation:

1. Navigate to the [Creator Dashboard](https://create.roblox.com/dashboard/creations).
2. In the upper-left, expand the account switcher and select your group.
3. Expand the account switcher again, select **Settings** under the group's name, then select **Group Profile**.
4. In the **Asset Privacy** section, enable the **Allow restricted assets on creation** toggle. Every newly created Image, Decal, and Mesh your group creates is now Restricted by default.

After enabling Asset Privacy, verify the asset permission of any newly uploaded asset in the asset configuration page:

![The landing page for asset permissions with the Collaborators tab selected.](../../assets/creator-dashboard/Asset-Toggle.png)

Selecting **Open Use** warns that once an asset has been set to **OpenUse**, it cannot be set back to **Restricted**.

![The landing page for asset permissions with the Collaborators tab selected.](../../assets/creator-dashboard/Asset-Make-OpenUse.png)

After setting to **Open Use**, the asset displays its current asset access permission.

![The landing page for asset permissions with the Collaborators tab selected.](../../assets/creator-dashboard/Asset-OpenUse.png) ### Decals

All `Class.Decal|Decals` are linked to an `Image`, which means a `Decal` can only be set to OpenUse if its `Image` dependency is OpenUse. Otherwise the following warning displays:

![The landing page for asset permissions with the Collaborators tab selected.](../../assets/creator-dashboard/Asset-Decals-Warning.png) ### Avatar assets

Avatar assets, such as accessories, clothing, and bodies, require all dependent textures and meshes to be `OpenUse` when uploading the Avatar asset to the Marketplace.

If you have Asset Privacy enabled and use a newly imported model in an avatar asset, you will be prompted to set your restricted texture and mesh dependencies to `OpenUse` during Marketplace [upload](/docs/en-us/marketplace/publish-to-marketplace.md#upload-an-asset):

![The landing page for asset permissions with the Collaborators tab selected.](../../assets/creator-dashboard/Asset-Avatar-Restricted.png)_ If your avatar item or bundle contains any restricted primitive assets, you must convert them to Open Use._

![The landing page for asset permissions with the Collaborators tab selected.](../../assets/creator-dashboard/Asset-Avatar-Success.png)_ If your entire avatar item has correct permissions, you can continue to upload and publish your avatar item to the Marketplace._

## Grant permissions

Restricted assets must be explicitly granted permission before they are visible or audible at runtime. Grant permissions individually through Creator Dashboard, or use the [Revamped Asset Manager](https://devforum.roblox.com/t/beta-updates-to-revamped-asset-manager/4548832/1) to bulk-grant permissions across many assets at once.

### To collaborators

To grant a collaborator permission to use one of your restricted assets, the following must be true:

- To grant to an individual creator: the creator must be your [friend](https://en.help.roblox.com/hc/en-us/articles/203313580-How-to-Make-Friends) on the platform.
- To grant to a group: you must have the [permission](/docs/en-us/projects/groups.md#roles-and-permissions) in that group.

When you grant an individual creator permission:

- They can use the asset in any of their individual or group-owned games.
- They can grant permission for games they own or have edit access to.

When you grant a group permission:

- All group members with Edit access can use the asset in games owned by that group.

Once a collaborator has permission to use one of your restricted assets, they can insert the asset from the **Inventory** and/or **Creation** tab of the [Toolbox](/docs/en-us/projects/assets/toolbox.md), or by using the restricted asset ID in the [Properties](/docs/en-us/studio/properties.md) window.

![A close up view of the Toolbox with the Inventory tab highlighted.](../../assets/studio/toolbox/Inventory-Tab.png)![A close up view of the Toolbox with the Creations tab highlighted.](../../assets/studio/toolbox/Creations-Tab.png)_Inserting a restricted asset through the Toolbox_

![A close up view of the Properties window with the Asset property highlighted.](../../assets/studio/properties/Enter-Private-Asset-ID.png)_Inserting a restricted asset in the Properties window_

If a collaborator wants to use the restricted asset in a script, or wants to save or publish a template place that includes the restricted asset, the game itself must also have permission to use the asset. If this step is skipped, the asset is not visible or audible during runtime, and a clickable error message displays in the **Output** window.

To grant a collaborator permission to use a restricted asset:

1. Navigate to the [Creator Dashboard](https://create.roblox.com/dashboard/creations).
2. In the upper tab bar, select **Development Items**, then click one of the following tabs:
  - **Models & Packages**
  - **Audio**
  - **Decals**
  - **Images**
  - **Videos**
  - **Meshes**
  - **MeshParts**
  - **Animations**
3. Select the asset you want your collaborator to have permission to use in their games. The asset's **Configure** page displays.
4. In the asset's left-hand navigation, select **Permissions**. The asset's **Permissions** page displays.
5. From the **Collaborators** tab, click the **Add collaborators** button.![The landing page for asset permissions with the Collaborators tab selected.](../../assets/creator-dashboard/Permissions-Collaborators.png)
6. Using the search bar, input and select a friend or group that you want to grant permission to use your restricted asset. The creator or group displays beneath the search bar with their access type.![The Add Collaborators pop-up menu.](../../assets/creator-dashboard/Add-Collaborators.png)
7. **OPTIONAL** If your selected asset type is a model or package, you can choose one of the following access types:
  - **Use** - The collaborator receives permission to use the asset in their games.
  - **Edit** - The collaborator receives permission to edit the asset's metadata, such as its name and description.
8. Click the **Done** button to finalize your asset access permissions.

> **Info:** To grant permissions across multiple assets at once, or to bulk-share assets with specific groups and users, use the latest Asset Manager beta. See [Revamped Asset Manager](https://devforum.roblox.com/t/beta-updates-to-revamped-asset-manager/4548832/1) for details.
### To games

> **Error:** Once a game has permission to use a restricted asset, you cannot revoke access to the asset.

To grant a game permission to use one of your restricted assets, the game must be editable to either you or a group that you belong to in which you have the [permission](/docs/en-us/projects/groups.md#roles-and-permissions).

Once a game has permission to use a restricted asset, anyone with **Edit** access to that game can:

- Copy and paste the asset into another place file within that game.
- Use its asset ID in the **Properties** window or in scripts within any place file within the game.

> **Info:** When you grant permission to a game by inserting a restricted asset into a collaborator's game, the asset is also automatically granted to the game's owner.

The following tabs walk you through the process of either granting one or more games access to a single restricted asset, or granting a game access to one or more restricted assets.

#### On an asset level

To grant a game permission to use a restricted asset:

1. Navigate to the [Creator Dashboard](https://create.roblox.com/dashboard/creations).
2. In the upper tab bar, select **Development Items**, then click one of the following tabs:
  - **Models & Packages**
  - **Audio**
  - **Decals**
  - **Images**
  - **Videos**
  - **Meshes**
  - **MeshParts**
  - **Animations**
3. Select the asset you want the game to have permission to use. The asset's **Configure** page displays.
4. In the asset's left-hand navigation, select **Permissions**. The asset's **Permissions** page displays.
5. From the **Experiences** tab, click the **Add experiences** button.![The landing page for asset permissions with the Experiences tab selected.](../../assets/creator-dashboard/Permissions-Experiences.png)
6. Type the game's universeID into the **Enter Universe IDs** input, then click the **Add** button. The game displays beneath the input with its access visible.
  > **Info:** To give multiple games permission at the same time, enter multiple universeIDs separated by commas.![The Add Experiences pop-up menu.](../../assets/creator-dashboard/Add-Experiences.png)
7. Click the **Done** button to finalize your asset access permissions.

#### On a game level

To grant a game permission to use many restricted assets:

1. Navigate to the [Creator Dashboard](https://create.roblox.com/dashboard/creations).
2. Select one of your or your group's games. The game's overview page displays.
3. In the game's left-hand navigation, navigate to **Configurations** > **Permissions**.
4. In the **Enter asset IDs** input, type every asset ID you want the game to have access to separated by commas, then click the **Add** button. All restricted assets the game has access to display beneath the input with the asset's name, asset ID, owner, and asset type.
5. At the bottom of the page, click the **Save Changes** button.

## View permissions

To view every restricted asset that your or your group's games have permission to use, review the game's **Permissions** page on the Creator Dashboard.

1. Navigate to the [Creator Dashboard](https://create.roblox.com/dashboard/creations).
2. Select one of your or your group's games. The game's overview page displays.
3. In the game's left-hand navigation, navigate to **Configurations** > **Permissions**.
4. **OPTIONAL** Click the download arrow button to export the data for offline processing.

## Revoke permissions

> **Warning:** Removing a creator as a friend does not automatically revoke their permission to use a restricted asset.

Revoking a collaborator's permission prevents them from granting new games access to the asset. It does not affect games that already use the asset — those games retain access permanently.

To revoke permission for a creator to use a restricted asset in any additional game:

1. Navigate to the [Creator Dashboard](https://create.roblox.com/dashboard/creations).
2. In the upper tab bar, select **Development Items**, then click one of the following tabs:
  - **Models & Packages**
  - **Audio**
  - **Decals**
  - **Images**
  - **Videos**
  - **Meshes**
  - **MeshParts**
  - **Animations**
3. Select the asset you want to revoke permission for one or more creators to use in their own games. The asset's **Configure** page displays.
4. In the asset's left-hand navigation, select **Permissions**. The asset's **Permissions** page displays.
5. From the **Collaborators** tab, locate the creator you want to revoke permission from, then click the Access dropdown next to their username. Additional options display.
6. Click the **Remove** button. A pop-up displays to confirm that you want to revoke permission from the collaborator.
7. From the pop-up, click the **Remove** button.

## Open permissions

> **Error:** Opening an asset's permissions is irreversible. Once you set an asset to Open Use, it **cannot** be reset to Restricted.
> **Info:** To set multiple assets to **Open Use** in bulk, use the Revamped Asset Manager. See [Revamped Asset Manager](https://devforum.roblox.com/t/beta-updates-to-revamped-asset-manager/4548832/1) for details.

With **Asset Privacy** enabled, you can still open the permissions of any Image, Decal, or Mesh so that any creator or game can freely use it.

To open permissions for your or your group's Image, Decal, or Mesh:

1. Enable Asset Privacy as described in [Restrict permissions](#restrict-permissions).
2. Back in the [Creator Dashboard](https://create.roblox.com/dashboard/creations), navigate to the upper tab bar, select **Development Items**, then click either **Decals**, **Images**, or **Meshes**. All of your Decal, Image, or Mesh assets display.
  > **Warning:** To set a Decal to Open Use, set its Image dependency to Open Use **first**. The Asset Privacy system blocks the change if the Image is still Restricted.
3. Select the asset you want every creator and game to freely use. The asset's **Configure** page displays.
4. In the **Asset Access** section, enable **Open Use**. A pop-up displays asking you to confirm this permanent change.
5. In the pop-up, click the **Make Open Use** button. Anyone on Roblox can now use your asset.
