---
title: "Studio interface"
url: /docs/en-us/studio/overview
last_updated: 2026-10-30T19:55:57Z
description: "User interface overview for Roblox Studio, the essential building tool for Roblox games."
---

# Studio interface

## Toolbar and mezzanine

The **toolbar** and **mezzanine** reside at the top of Studio.

![Mezzanine and toolbar indicated in Studio.](../assets/studio/general/Toolbar-Mezzanine.png)

The left side of the mezzanine contains easily-accessible [testing controls](/docs/en-us/studio/testing-modes.md#playtest-options).

![Testing controls indicated in Studio's mezzanine.](../assets/studio/general/Mezzanine-Testing-Controls.png)

The right side of the mezzanine contains buttons/menus for [collaboration](/docs/en-us/projects/collaboration.md), sharing, [Assistant](/docs/en-us/assistant/guide.md), creator notifications, and account options.

![Other options indicated in Studio's mezzanine.](../assets/studio/general/Mezzanine-Right.png)

In the center of the mezzanine are the default tool tabs of **Home**, **Model**, **Avatar**, **UI**, **Script**, and **Plugins**. You can also add [custom tabs](#custom-tabs) for your specific needs.

![Default tabs indicated in Studio's mezzanine.](../assets/studio/general/Mezzanine-Default-Tabs.png)

#### Home

The **Home** tab contains the core [transform](/docs/en-us/parts.md#transform-parts) tools, [part inserter](/docs/en-us/parts.md#insert-parts), the [color](/docs/en-us/parts.md#color) and [material](/docs/en-us/parts.md#material) widgets, the [group](/docs/en-us/parts.md#group) and [lock](/docs/en-us/parts.md#lock) tools, and [anchor](/docs/en-us/parts.md#anchor) toggle. Also contains the [Terrain Editor](/docs/en-us/studio/terrain-editor.md).

#### Model

The **Model** tab contains the core [transform](/docs/en-us/parts.md#transform-parts) tools, the [pivot](/docs/en-us/studio/pivot-tools.md) and [align](/docs/en-us/studio/align-tool.md) tools, insertion widgets for [effects](/docs/en-us/effects.md) and [constraints](/docs/en-us/physics.md#constraints), and [solid‑modeling](/docs/en-us/parts/solid-modeling.md) tools.

#### Avatar

The **Avatar** tab contains the core [transform](/docs/en-us/parts.md#transform-parts) tools, as well as specialized tools for building default rigs, configuring [avatars](/docs/en-us/avatar-setup.md), working with [animations](/docs/en-us/animation.md), and [creating/fitting accessories](/docs/en-us/avatar/accessory-fitting-tool.md).

#### UI

The **UI** tab contains insertion widgets for [UI objects](/docs/en-us/ui.md#ui-objects) and lets you access the [Style Editor](/docs/en-us/ui/styling/editor.md), a comprehensive tool that allows you to create, manage, and apply UI styles.

#### Script

The **Script** tab contains tools for writing and testing scripts, including [debugging](/docs/en-us/studio/debugging.md) tools.

#### Plugins

The **Plugins** tab contains [plugins](/docs/en-us/studio/plugins.md) created by the community or plugins you've created yourself to use across your games.

### Appearance

You can customize the appearance of the toolbar by right-clicking in an empty area within the mezzanine/toolbar and selecting from the following options:

- **Manage tabs** — Reveals a popup window with the following options:![The Manage Tabs popup in Studio.](../assets/studio/general/Manage-Tabs-Popup.png)
  1. Show or hide the tab.
  2. With a tab selected, reorder it relative to the other tabs.
  3. Delete a selected [custom tab](#custom-tabs).
  4. Choose between tabs **Center** alignment or **Left** alignment (next to the [testing controls](/docs/en-us/studio/testing-modes.md#playtest-options)).
- **Collapse toolbar** — Maximizes space by hiding the toolbar while keeping the mezzanine visible. Hovering over a tab in the mezzanine temporarily reveals the toolbar.
- **Compact toolbar** — Makes the toolbar considerably more compact through smaller icons and labels, ideal for laptops or smaller monitors.
- **Show labels** — Toggles the text labels below tools on or off.

### Custom tabs

Beyond the default tool tabs, you can add **custom tabs** for your specific needs, either through Studio's interface or by editing local `.json` files.

#### Studio

The easiest way to create custom tabs is through Studio's workflow.

1. Click the `+` button to the right of the default tabs, then type in a name for the new tab and press `Enter`.![Button to add custom tab indicated in Studio's mezzanine.](../assets/studio/general/Toolbar-Add-Custom-Tab.png)
  > **Success:** Alternatively to creating a new, empty tab, you can duplicate any existing tab by right‑clicking it and selecting **Duplicate tab**. Unlike default tabs, tools within duplicated tabs can be freely modified.
2. Click the button or right‑click in an empty region of the toolbar and select **Add tools**.![Button to add new tool to a custom tab in Studio's toolbar.](../assets/studio/general/Toolbar-Custom-Tab-Add-Tool.png)
3. In the popup window, search for a tool and toggle its checkbox to add. New tools appear to the right of other tools, but you can right‑click any tool and select **Move left** or **Move right** to reorder it relative to other tools. You can also insert a divider by right‑clicking in an empty region of the toolbar and selecting **Add divider**.![Custom tab populated with tools.](../assets/studio/general/Toolbar-Custom-Tab-Filled.png)
  > **Info:** If you need to remove a tool from a custom tab, right‑click it and select **Remove tool**.

#### JSON

Custom tab configurations are saved **locally** on each machine in `.json` format, allowing you to build customized tabs and share them with your team or the community.

1. **OPTIONAL** To modify `.json` from a default tab toolset, begin by right‑clicking an existing tab and selecting **Duplicate tab**.
2. Open the custom tabs folder which is stored in a location unaffected by Studio updates.
  - **Windows** — `%LOCALAPPDATA%\Roblox\<userID>\CustomRibbonTabs`
  - **Mac** — `~/Documents/Roblox/<userID>/CustomRibbonTabs`
3. In the `CustomRibbonTabs` directory are `.json` files which define the toolbar's structure:
  - The `RibbonLayout.json` file controls the overall ordering and visibility of tabs.```json
{
	"TabLayout": [
		{
			"Identifier": {
				"Type": "BuiltIn",
				"Filename": "HomeTab"
			},
			"Visible": true
		},
{
```
  - Other `.json` files represent individual tabs and can be named whatever you prefer. Each file's `Name` represents the tab's name as it will appear in Studio.```json
{
  "Name": "Custom",
  "Controls": []
}
```
4. In the `Controls` array for a tab file, insert various buttons, submenus, and more. Each control's `Id` value must be **unique** within the file. The following examples illustrate common elements in a custom tab: #### IconButton`IconButton` inserts a button with an optional text label.```json
{
  "Name": "Custom",
  "Controls": [
    {
      "Id": "Select",
      "Type": "IconButton",
      "Action": {
        "Category": "Actions",
        "DataModel": "Standalone",
        "ItemId": "Select",
        "PluginId": "BuilderTools"
      }
    }
  ]
}
```#### Separator`Separator` inserts a non-interactable separation line. `Size` options are `Large`, `Medium`, or `Small`.```json
{
  "Name": "Custom",
  "Controls": [
    {
      "Type": "Separator",
      "Size": "Large"
    }
  ]
}
```#### SplitButton`SplitButton` inserts a button which reveals a dropdown menu when the small triangle to the right of its icon is pressed.```json
{
  "Name": "Custom",
  "Controls": [
    {
      "Id": "SimpleSplit",
      "Type": "SplitButton",
      "Action": {
        "Category": "Actions",
        "DataModel": "Standalone",
        "ItemId": "Select",
        "PluginId": "BuilderTools"
      },
      "Children": [
        {
          "Type": "Column",
          "Children": [
            {
              "Id": "Move",
              "Type": "Option",
              "Action": {
                "Category": "Actions",
                "DataModel": "Standalone",
                "ItemId": "Move",
                "PluginId": "BuilderTools"
              }
            },
            {
              "Id": "Scale",
              "Type": "Option",
              "Action": {
                "Category": "Actions",
                "DataModel": "Standalone",
                "ItemId": "Scale",
                "PluginId": "BuilderTools"
              }
            },
            {
              "Id": "Rotate",
              "Type": "Option",
              "Action": {
                "Category": "Actions",
                "DataModel": "Standalone",
                "ItemId": "Rotate",
                "PluginId": "BuilderTools"
              }
            }
          ]
        }
      ]
    }
  ]
}
```#### IconButton (Plugin)`IconButton` can be used to insert a button which links to a [plugin](/docs/en-us/studio/plugins.md) through its ID, assuming the plugin, such as [Tailor Swiftly](https://create.roblox.com/store/asset/130172194397869/Tailor-Swiftly), is installed in your version of Studio.```json
{
  "Name": "Custom",
  "Controls": [
    {
      "Id": "PrinceTybalt_Tailor Swiftly",
      "Type": "IconButton",
      "Action": {
        "Category": "Actions",
        "DataModel": "Edit",
        "ItemId": "PrinceTybalt_Tailor Swiftly",
        "PluginId": "130172194397869",
        "PluginType": "Cloud"
      }
    }
  ]
}
```#### Text`Text` inserts a basic text label, useful to label groups of other controls in submenus.```json
{
  "Name": "Custom",
  "Controls": [
    {
      "Id": "CustomHeader",
      "Type": "Text",
      "Title": "Insert UI"
    }
  ]
}
```
  > **Success:** Beyond the above examples, you can right-click any default tab and select **Duplicate tab**. This will create a new custom tab and corresponding `.json` file in your local `CustomRibbonTabs` directory which you can inspect to explore how various default tools and menus are constructed.
5. Save the `.json` file and then reload Studio's plugins:
  1. Right-click anywhere in the toolbar or mezzanine and select **Manage tabs**.
  2. Access the options menu from the popup's upper‑right corner and select **Reload custom tabs**.![Options menu in the Manage Tabs popup.](../assets/studio/general/Manage-Tabs-Popup-Options.png)

## 3D viewport

The 3D viewport represents the `Class.Workspace` of a place. From here, you can move the camera around the virtual world, manipulate objects with the mouse, and playtest a game without leaving Studio.

![An example viewport display of a desert environment with multiple stone pillars. One of the pillars displays movement visual aids from the Move tool.](../assets/studio/general/Editor-Window.jpg)_3D viewport in Roblox Studio_

### Camera controls

Inside the viewport, you can move the camera with the following controls.

| Keys/Shortcuts | Action |
| --- | --- |
| `W` `A` `S` `D` | Moves the camera forward/left/back/right. |
| `Q` `E` | Moves the camera down/up. |
| `Shift` | In combination with any movement key, changes the camera speed. |
| `F` | Focuses the camera on a selected part. |
| **Right Mouse Button** | When pressed, dragging the mouse moves the camera view around. |
| **Mouse Scroll Wheel**<br>`Ctrl``=` or `⌘``=`<br>`Ctrl``-` or `⌘``-` or `O` | Zooms the camera in or out.<br>Zooms the camera in.<br>Zooms the camera out. |
| `,` / `.` | Rotates the camera left/right. If a part/model is in focus via the `F` shortcut, rotates the camera counterclockwise/clockwise around that focused object. |
| **Middle Mouse Button** | When pressed, dragging the mouse pans the camera. |
| **Right Mouse Button** & **Mouse Scroll Wheel** | Pressing the right mouse button and scrolling the mouse wheel **up** increases the camera scroll speed. Conversely, pressing the right mouse button and scrolling the mouse wheel **down** reduces the camera scroll speed. > **Success:** This feature is currently in beta. Enable it through **File** ⟩ **Beta Features** ⟩ **New Studio Camera Controls**. |

### Object selection

As you hover over parts and models in the viewport, they are outlined to indicate their potential selection. You can select an outlined object by clicking it, or you can select multiple objects by holding `Shift`, `Ctrl`, or `⌘` as you hover over and click them.

![A warehouse environment with the stairs and multiple pallet box objects with a blue highlight to signify that they are selected in the 3D viewport.](../assets/studio/general/Editor-Window-Object-Selection.jpg)

In more complex environments or when zoomed in, objects will commonly be hidden from your view by other objects in front. To select hidden objects without moving the camera around, hold `Alt` or `⌥` and click to perform **selection cycling** to the next further object behind the currently selected object.

> **Info:** When one or more objects or [models](/docs/en-us/parts/models.md) are selected in the [Explorer](/docs/en-us/studio/explorer.md) window, you can select all of their **children** by right-clicking and choosing **Hierarchy** ⟩ **Select Children** from the context menu. Similarly, choosing **Select Parent(s)** selects the **direct parents** of those objects.

To customize the appearance of selection lines and boxes around objects, set your desired options in the **Selection Visualization** section within the **Selection** panel of Studio's settings.

![A warehouse environment with rope object's selection outline and bounding box highlighted.](../assets/studio/general/Selected-Object-Bounding-Box.jpg) ### Visualization options

In the upper-right corner of the 3D viewport, you can quickly toggle or set common visualization options related to [on‑screen UI](/docs/en-us/ui/on-screen-containers.md) overlays, [light sources](/docs/en-us/effects/light-sources.md), physics simulation, character [pathfinding](/docs/en-us/characters/pathfinding.md), and more. The menu also contains a control for viewing/setting the camera scroll speed.

![A close up view of the 3D viewport with the Visualization Options button indicated in the upper-right corner.](../assets/studio/general/Visualization-Options.png) ## Frequently-used tools

Commonly used windows include the [Explorer](/docs/en-us/studio/explorer.md), the [Properties](/docs/en-us/studio/properties.md) window, [Asset Manager](/docs/en-us/projects/assets/manager.md), [Toolbox](/docs/en-us/projects/assets/toolbox.md), and others.

### Explorer

The [Explorer](/docs/en-us/studio/explorer.md) window, visible by default and accessible from Studio's **Window** menu or **Home** tab, shows a hierarchical list of every object and service inside the place, collectively referred to as its **data model**. Frequently used services in the hierarchy include `Class.Workspace` which mirrors the [3D viewport](#3d-viewport), as well as `Class.ReplicatedStorage` and `Class.ServerStorage`.

![Explorer hierarchy showing Camera, Terrain, and SignModel as children of Workspace; Board and Post as children of SignModel](../assets/studio/explorer/Parent-Child-Hierarchy.png) ### Properties

The [Properties](/docs/en-us/studio/properties.md) window, visible by default and accessible from Studio's **Window** menu or **Home** tab, lets you adjust properties of a selected object to change how it looks and behaves. Object properties are divided into sections; for example, a `Class.MeshPart` includes sections like **Appearance** which allows you to change its color, material, transparency, and more.

At the bottom of the window, you can define custom [attributes](/docs/en-us/studio/properties.md#instance-attributes) for an object, similar to its default properties. Attributes and their values are saved with your place/assets and they're an ideal way for team members to experiment with different values during runtime, even if they don't understand the underlying code.

![A close up view of the Attributes section of the Properties window.](../assets/studio/properties/Attributes-Example.png) ### Asset Manager

The [Asset Manager](/docs/en-us/projects/assets/manager.md), accessible from Studio's **Window** menu or **Home** tab, lets you manage places, images, meshes, audio, and more. It also provides a mechanism to bulk import large groups of assets.

### Toolbox

The [Toolbox](/docs/en-us/projects/assets/toolbox.md), accessible from Studio's **Window** menu or **Home** tab, contains a selection of models, images, meshes, audio, plugins, videos, and fonts made by Roblox or Roblox community members. It also includes all of the creations that you've personally [distributed on the Creator Store](/docs/en-us/production/creator-store.md) or those which were distributed by [groups](/docs/en-us/projects/groups.md) you belong to.

![The Toolbox window.](../assets/studio/toolbox/Model-Search-Example.png) ### Output

The [Output](/docs/en-us/studio/output.md) window, accessible from Studio's **Window** menu or **Script** tab, displays errors captured from running scripts, messages from Roblox Engine, messages from calls to `Global.LuaGlobals.print()`, and errors from calls to `Global.RobloxGlobals.warn()`.

### Command Bar

The **Command Bar**, accessible from Studio's **Script** tab toolbar or the **Window** ⟩ **Script** menu, lets you execute Luau code outside of scripts. To quickly jump to the command bar at any time, press `Ctrl``9` (Windows) or `⌘``9` (Mac).

> **Success:** Most of the features outlined below are in beta and must be enabled through **File** ⟩ **Beta Features** ⟩ **Multi-line Command Bar**.

Features include:

- **Multiline editing** — Press `Enter` to insert new lines while typing. The bar starts with 2 lines, grows up to 10 lines as new lines are inserted, and shrinks as lines are deleted. When you're ready to run/execute the contents of the bar, click the **Run** button or use the shortcut `Ctrl``Enter` (`⌘``Enter`).
- **Command history** — The last 10 executed commands are visible by clicking the **History** button and navigating to the **Recent** tab. Clicking on a command in the list loads it into the bar, or you can navigate the list with `↑`/`↓` and insert the highlighted command with `Enter`. Alternatively, you can scrub through commands with`Ctrl`/`⌘` + `↑`/`↓` when the command bar is selected.
- **Saved commands** — You can explicitly save commands with the **Save** button or the default shortcut `Ctrl``B` (`⌘``B`). Saved commands can be accessed through the **Saved** tab in the popup list, and the mechanics of loading saved commands from the list are the same as those in the command history.
- **Script Editor integration** — The command bar is an embedded script editor and supports a wide subset of Studio's [Script Editor](/docs/en-us/studio/script-editor.md) features, including [autocomplete](/docs/en-us/studio/script-editor.md#autocomplete-features), Luau [linting](https://luau.org/lint), [go to declaration](/docs/en-us/studio/script-editor.md#go-to-declaration), [function filter](/docs/en-us/studio/script-editor.md#script-function-filter), [Code Assist](/docs/en-us/studio/script-editor.md#code-assist), and [multi‑cursor](/docs/en-us/studio/script-editor.md#multi-cursor).

## Layout customization

Studio's drag-and-drop interface lets you easily customize window layout to best suit your workflows.

### Reposition windows

You can reposition any window by click-dragging its **header bar**. As you begin dragging the window, the interface reveals **empty docking area** regions. If you drag the mouse pointer into any empty region, a floating **position selector** appears in that region. Dragging the pointer over the "center" of the floating selector targets the empty region as the dragged window's destination, indicated by the region darkening and becoming outlined.

![Mouse pointer hovering over the 'center' icon of the position selector in an empty docking area, showing that region as the dragged window's destination.](../assets/studio/general/Docking-Position-Selector-Empty.png)_Mouse pointer hovering over the "center" icon of the position selector in an empty docking area_

If you drag the mouse pointer into a **populated** region such as the 3D viewport, a floating position selector appears with multiple options for the window's destination. For example, dragging the pointer over the "left" icon will position the window on the region's left side.

#### Viewport left

![Mouse pointer hovering over the 'left half' icon of the position selector in a populated region, showing the left side of the region as the dragged window's destination.](../assets/studio/general/Docking-Position-Selector-Left.png)

#### Viewport right

![Mouse pointer hovering over the 'right half' icon of the position selector in a populated region, showing the right side of the region as the dragged window's destination.](../assets/studio/general/Docking-Position-Selector-Right.png)

### Group windows

If you drag a window into a **populated** region and choose the "center" icon of the [position selector](#reposition-windows), the dragged window will group into that region as a tab. This allows you to set up tab groups of commonly used windows.

![An example of an Explorer window if you choose the center icon of the position selection. It includes three tabs at the bottom of the window: the Explorer window, the Properties window, and the Terrain Editor window.](../assets/studio/general/Docking-Grouped-Tabs.png)_Three windows grouped together as tabs_

### Pin windows

To maximize screen space for the 3D viewport, you can **pin** windows (or an entire [group](#group-windows) of windows) to the edges of the overall Studio window. Once pinned, you can temporarily open any window by clicking its tab — this does not disturb other windows, and the expanded window will automatically collapse when you click in another window or click its tab again.

![An example 3D viewport where the Explorer, Properties, and Terrain Editor windows are pinned to the right of the Studio window.](../assets/studio/general/Docking-Pinned-Tabs.png)_Three windows pinned to the right side of the Studio window_

To pin a window or an entire [group](#group-windows) of windows, click the "collapse" button. Alternatively, to un‑pin a pinned window/group, open it by clicking its tab, then click the "expand" button.

![A close up view of the Explorer window with the Collapse button highlighted.](../assets/studio/general/Docking-Expand-Collapse.png) ### Float windows

To float a window freely of other windows, simply drag‑and‑drop it without selecting any icon from the floating [position selector](#reposition-windows).
