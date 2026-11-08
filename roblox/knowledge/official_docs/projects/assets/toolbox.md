---
title: "Toolbox"
url: /docs/en-us/projects/assets/toolbox
last_updated: 2026-10-30T19:55:53Z
description: "The Toolbox contains a selection of assets made by Roblox or Roblox community members."
---

# Toolbox

The **Toolbox**, accessible from Studio's **Window** menu or **Home** tab toolbar, contains a selection of [models](/docs/en-us/parts/models.md), [images](/docs/en-us/parts/textures-decals.md), [meshes](/docs/en-us/parts/meshes.md), [audio](/docs/en-us/audio/assets.md), [plugins](/docs/en-us/studio/plugins.md), [videos](/docs/en-us/ui/video-frames.md), and fonts made by Roblox or Roblox community members. It also includes all of the creations that you've personally published or those which were published by [groups](/docs/en-us/projects/groups.md) you belong to.

![Toolbox highlighted in Studio's toolbar.](../../assets/studio/general/Toolbar-Toolbox.png)

The toolbox contains four distinct sections:

#### Creator Store

![A close up view of the Toolbox with the Creator Store tab highlighted.](../../assets/studio/toolbox/Creator-Store-Tab.png)

The **Creator Store** section contains models, decals, meshes, audio, plugins, videos, and fonts made by Roblox or Roblox community members. See [Creator Store](/docs/en-us/production/creator-store.md) for more information.

#### Inventory

![A close up view of the Toolbox with the Inventory tab highlighted.](../../assets/studio/toolbox/Inventory-Tab.png)

The **Inventory** section contains models, decals, meshes, audio, packages, videos, plugins, animations, and fonts that you've personally published, those which were published by [groups](/docs/en-us/projects/groups.md) you belong to, or those taken from the [Creator Store](/docs/en-us/production/creator-store.md).

#### Recent

![A close up view of the Toolbox with the Recent tab highlighted.](../../assets/studio/toolbox/Recent-Tab.png)

The **Recent** tab is similar to **Inventory** except that filters your recently used models, decals, meshes, audio, videos, and animations.

#### Creations

![A close up view of the Toolbox with the Creations tab highlighted.](../../assets/studio/toolbox/Creations-Tab.png)

The **Creations** tab is similar to **Inventory**, with the important distinction that it filters models, decals, meshes, audio, plugins, and animations that you've personally published or those which were published by [groups](/docs/en-us/projects/groups.md) you belong to. You can [configure](#asset-configuration) all assets in this section directly within Studio.

## Find and use assets

With millions of assets available, it's helpful to narrow the search results to find exactly what you are looking for. To browse and use assets:

1. In the top-left corner, click the category selector dropdown and choose an asset category. Optionally click the **advanced filter** button to filter results by [verified creator](/docs/en-us/production/publishing/account-verification.md) status, a specific creator, the sale price for [plugins](/docs/en-us/studio/plugins.md), and file length for [audio assets](/docs/en-us/audio/assets.md).![The Toolbox window with the category selector highlighted](../../assets/studio/toolbox/Creator-Store-Category-Selector.png)![The Toolbox window with the advanced filter highlighted](../../assets/studio/toolbox/Creator-Store-Advanced-Filter.png)
2. In the search field, type what you want to find and press `Enter`. The view curates a selection of assets according to your query.
3. **OPTIONAL** Hover over an asset thumbnail and click the magnifying glass icon to closely inspect the asset's community rating, description, and more.![A preview view of an asset with the inspect icon highlighted.](../../assets/studio/toolbox/Asset-Inspect-Icon.png)
4. To add an asset to a game:
  - If the asset is a [model](/docs/en-us/parts/models.md), [mesh](/docs/en-us/parts/meshes.md), [decal](/docs/en-us/parts/textures-decals.md), [video](/docs/en-us/ui/video-frames.md), or [audio](/docs/en-us/audio/assets.md) asset, click it or drag‑and‑drop it into the 3D viewport. It then inserts into the [Explorer](/docs/en-us/studio/explorer.md) hierarchy, and assets with 3D content display in the viewport.
  - If the asset is a [plugin](/docs/en-us/studio/plugins.md), click it and use the **Install** button to add it to the mezzanine's **Plugins** tab.
  - If the asset is a font, click it and use the **Install** button to add it to your font library. It then becomes available for user interface elements such as [text labels](/docs/en-us/ui/labels.md) or [buttons](/docs/en-us/ui/buttons.md).
  > **Info:** Some assets include scripts that perform specific actions, such as animating at runtime or triggering a sound. If you want to use an asset without allowing any of its scripts to run, right‑click the object in the [Explorer](/docs/en-us/studio/explorer.md) window and select **Disable Scripts** from the context menu.

## Asset configuration

Right-clicking an asset and selecting **Edit Asset** opens the **Asset Configuration** window. In this window, you can edit the asset's details or restore it to a previous version.

> **Info:** Asset configuration is only possible for assets you've personally published or those which were published by [groups](/docs/en-us/projects/groups.md) you belong to. The **Creations** tab is particularly useful for filtering assets in this way.
## Troubleshooting

The toolbox runs through a web view. If you're experiencing any of the following issues, run the associated troubleshooting steps.

** General Issues**

> **Warning:** Make sure there are no active instances of Roblox Studio running before running these steps.

| Windows |
| --- |
| <ol><li>[Reinstall](https://developer.microsoft.com/en-us/microsoft-edge/webview2/) your Windows WebView2 installation.</li><li>Delete the WebView2 data folder found at `%LOCALAPPDATA%\Roblox\RobloxStudio\WebView2`. Studio will automatically recreate this folder when it opens.</li></ol> |
| Mac |
| Delete the WebKit data folders found at `~/Library/WebKit/com.Roblox.RobloxStudio` and `~/Library/Caches/com.Roblox.RobloxStudio/WebKit`. Studio will automatically recreate these folders when it opens. |

** Audio Not Working**

| Windows |
| --- |
| <ol><li>Right click the speaker icon in the taskbar.</li><li>Click **Open Volume Mixer**.</li><li>Make sure that **Microsoft Edge WebView2** is not muted.</li></ol> |
