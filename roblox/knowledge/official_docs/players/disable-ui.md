---
title: "Disable default UI"
url: /docs/en-us/players/disable-ui
last_updated: 2026-10-30T19:55:47Z
description: "Explains the process of disabling Roblox's default user interface elements."
---

# Disable default UI

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
