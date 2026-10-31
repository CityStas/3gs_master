---
title: "On-screen UI containers"
url: /docs/en-us/ui/on-screen-containers
last_updated: 2026-10-30T19:56:02Z
description: "Learn how to display UI objects on a user's screen."
---

# On-screen UI containers

The `Class.ScreenGui` container holds `Class.GuiObject|GuiObjects` to display on a player's screen, including [frames](/docs/en-us/ui/frames.md), [labels](/docs/en-us/ui/labels.md), [buttons](/docs/en-us/ui/buttons.md), and more. All on‑screen UI objects and code are stored and changed on the client.

![Example ScreenGui with various GuiObject children, including a Frame, TextLabel, TextBox, and ImageButton.](../assets/ui/ui-objects/ScreenGui-Example.jpg)
> **Info:** For UI containers that hold `Class.GuiObject|GuiObjects` that you want to display **within** the 3D world, such as on the face of a part, see [In-game UI Containers](/docs/en-us/ui/in-experience-containers.md).

To display a `Class.ScreenGui` and its child `Class.GuiObject|GuiObjects` to every player who joins the game, place it inside the `Class.StarterGui` container. When a player joins a game and their character first spawns, the `Class.ScreenGui` and its contents clone into the `Class.PlayerGui` container for that player, located within the `Class.Players` container.

![Diagram of how a ScreenGui clones from StarterGui to a player's PlayerGui](../assets/ui/ui-objects/StarterGui-To-PlayerGui.png)
> **Success:** By default, `Class.GuiObject|GuiObjects` inside a `Class.ScreenGui` within `Class.StarterGui` appear as an overlay of the [3D viewport](/docs/en-us/studio/overview.md#3d-viewport), simulating their appearance and position in a running game. To hide all such screen overlays, toggle off **GUI overlay** from the [Visualization Options](/docs/en-us/studio/overview.md#visualization-options) widget in the upper‑right corner of the 3D viewport.
> **Info:** If `Class.Players.CharacterAutoLoads` is disabled, the contents of `Class.StarterGui` will not be cloned until `Class.Player:LoadCharacterAsync()` is called.

As a game grows in scope, you may require multiple screen interfaces such as a title screen, settings menu, shop interface, and more. In such cases, you can place multiple unique `Class.ScreenGui` containers inside `Class.StarterGui` and toggle each container's `Class.ScreenGui.Enabled|Enabled` property depending on whether it should be visible and active (while `false`, contents will not render, process user input, or update in response to changes).

![Explorer hierarchy showing multiple ScreenGui containers, one enabled and the others disabled, in order to control which are visible at a given time.](../assets/ui/ui-objects/ScreenGuis-Enabled.png)

The `Class.ScreenGui.Enabled|Enabled` property can be initially toggled through the [Properties](/docs/en-us/studio/properties.md) window and/or you can set it during playtime from a client‑side script by [accessing](#access-player-ui) the player's `Class.PlayerGui` and setting it to `true` or `false` for the desired container(s).

> **Info:** When using multiple `Class.ScreenGui` interfaces, you can layer them by Z‑index through their `Class.ScreenGui.DisplayOrder|DisplayOrder` property. See [Display Order](#display-order) for more information.
## Container properties

The following properties let you customize the [screen insets](#screen-insets) across multiple devices, the [display order](#display-order) when using multiple screen containers, and more.

### Screen insets

Modern phones take advantage of the entire screen but typically include notches, cutouts, and other elements that occupy screen space. Every Roblox game also includes the **top bar controls** for quick access to the main menu, [chat](/docs/en-us/chat/in-experience-text-chat.md), [leaderboard](/docs/en-us/players/leaderboards.md), and more.

![Mobile device showing Roblox top bar buttons and device cutout.](../../assets/engine-api/enums/ScreenInsets/Top-Bar-Cutout.png)

To ensure players can see and access all UI easily and without obstruction, Roblox provides the `Class.ScreenGui.ScreenInsets|ScreenInsets` property which controls the **safe area** insets for the contents of a `Class.ScreenGui`.

#### CoreUISafeInsets

The default of `Enum.ScreenInsets|CoreUISafeInsets` keeps all descendant `Class.GuiObject|GuiObjects` inside the core UI safe area, clear of the top bar buttons and other screen cutouts. This setting is recommended if the `Class.ScreenGui` contains interactive UI elements.

![Mobile device showing the core UI safe area.](../../assets/engine-api/enums/ScreenInsets/CoreUISafeInsets.png)

#### DeviceSafeInsets

A setting of `Enum.ScreenInsets|DeviceSafeInsets` guarantees that no descendant `Class.GuiObject|GuiObjects` are occluded by any device screen cutouts such as the camera notch, although no inset is added for Roblox core UI elements like the top bar buttons.

![Mobile device showing the device safe area.](../../assets/engine-api/enums/ScreenInsets/DeviceSafeInsets.png)

#### TopbarSafeInsets

A setting of `Enum.ScreenInsets|TopbarSafeInsets` keeps all descendant `Class.GuiObject|GuiObjects` between the top bar controls and the right edge of the device safe area. The `Class.ScreenGui` will then automatically flex in horizontal size based on the top bar's content.

![Mobile device showing the top bar safe area within the Roblox controls.](../../assets/engine-api/enums/ScreenInsets/TopbarSafeInsets.png)

#### None

No insets are added to the fullscreen area. This mode may result in UI that is obscured or completely hidden by device notches and cutouts, so you should only use it for a `Class.ScreenGui` that contains non‑interactive content like background images.

![Mobile device showing the entire screen region with no account for safe areas.](../../assets/engine-api/enums/ScreenInsets/None.png)

### Display order

When using multiple `Class.ScreenGui` interfaces, you can layer them by Z‑index through their `Class.ScreenGui.DisplayOrder|DisplayOrder` property. For example, to display a modal settings menu on one `Class.ScreenGui` in front of the game's main user interface on another `Class.ScreenGui`, assign a higher `Class.ScreenGui.DisplayOrder|DisplayOrder` to the modal's than the underlying interface's.

### Reset on spawn

The `Class.ScreenGui.ResetOnSpawn|ResetOnSpawn` boolean property determines if the `Class.ScreenGui` resets (deletes itself and re‑clones into the player's `Class.PlayerGui`) every time the player's character respawns.

| Condition | Resets |
| --- | --- |
| `Class.ScreenGui.ResetOnSpawn\|ResetOnSpawn` is `true` (default). | **YES** |
| The `Class.ScreenGui` is an **indirect** descendant of `Class.StarterGui`; for example it's placed inside a `Class.Folder` located within `Class.StarterGui`. | **YES** |
| `Class.ScreenGui.ResetOnSpawn\|ResetOnSpawn` is `false` **and** the `Class.ScreenGui` is a **direct** descendant of `Class.StarterGui`. | **NO** |

## Access player UI

As noted, parenting a `Class.ScreenGui` to `Class.StarterGui` clones it and its child `Class.GuiObject|GuiObjects` into a player's `Class.PlayerGui` container when they join the game and their character first spawns.

If you need to control a player's UI container during playtime, for example to show/hide a specific `Class.ScreenGui` or any of its children, access it as follows from a `Class.LocalScript`:

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local playerGui = player.PlayerGui

local titleScreen = playerGui:WaitForChild("TitleScreen")
local settingsMenu = playerGui:WaitForChild("SettingsMenu")

titleScreen.Enabled = false  -- Hide title screen
settingsMenu.Enabled = true  -- Show settings menu
```

## Disable default UI

All Roblox games include several UI elements that are enabled by default. If you don't need any of these elements or if you want to replace them with your own creations, you can use the `Class.StarterGui:SetCoreGuiEnabled()|SetCoreGuiEnabled()` method in a client‑side script with the associated `Enum.CoreGuiType` option.

| Default UI | Associated enum |
| --- | --- |
| Dynamically updated `Class.Players` list, commonly used as a [leaderboard](/docs/en-us/players/leaderboards.md). | `Enum.CoreGuiType.PlayerList` |
| The character's `Class.Humanoid.Health\|Health` bar. Does not appear if the character's `Class.Humanoid` is at full health. | `Enum.CoreGuiType.Health` |
| The character's `Class.Backpack` which contains [in-game tools](/docs/en-us/players/tools.md). Does not appear if there are no `Class.Tool\|Tools` in the backpack. | `Enum.CoreGuiType.Backpack` |
| The [text chat](/docs/en-us/chat/in-experience-text-chat.md) window. | `Enum.CoreGuiType.Chat` |
| Popup menu of character [emotes](/docs/en-us/characters/emotes.md). | `Enum.CoreGuiType.EmotesMenu` |
| A window displaying a player's perspective or view of their own character. Does not appear unless the player has enabled **Self View** from the Roblox menu. | `Enum.CoreGuiType.SelfView` |
| A **capture screenshot** button along the right side of the screen. Does not appear unless the player has enabled **Captures** from the Roblox menu. | `Enum.CoreGuiType.Captures` |
| The **Avatar Switcher** allows users to change their platform avatar. | `Enum.CoreGuiType.AvatarSwitcher` |

![Core UI elements in every Roblox game.](../../assets/ui/misc/CoreGui-Elements.jpg)

```lua
local StarterGui = game:GetService("StarterGui")

-- Disable default health bar and backpack
StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.Health, false)
StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.Backpack, false)
```

Additionally, devices with touch capabilities include a virtual thumbstick and a jump button by default. If desired, you can hide these elements by setting `Class.GuiService.TouchControlsEnabled` to `false` in a client‑side script.

![UI elements for touch-capable devices in every Roblox game.](../../assets/ui/misc/TouchGui-Elements.png)

```lua
local GuiService = game:GetService("GuiService")

GuiService.TouchControlsEnabled = false
```
