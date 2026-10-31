---
title: "Friends Locator"
url: /docs/en-us/resources/modules/friends-locator
last_updated: 2026-10-30T19:55:55Z
description: "The Friends Locator module lets players easily find and teleport to their friends inside a place."
---

# Friends Locator

It can be challenging to locate friends in-game. The **FriendsLocator** [developer module](/docs/en-us/resources/modules.md) lets players easily find and teleport to their friends inside a place.

## Module usage

### Installation

To use the **FriendsLocator** module in a game:

1. From Studio's **Window** menu or **Home** tab toolbar, open the [Toolbox](/docs/en-us/projects/assets/toolbox.md) and select the **Creator Store** tab.
2. Make sure the **Models** sorting is selected, then click the **See All** button for **Categories**.
3. Locate and click the **Packages** tile.
4. Locate the **Friends Locator** module and click it, or drag-and-drop it into the 3D view.
5. In the [Explorer](/docs/en-us/studio/explorer.md) window, move the entire **FriendsLocator** model into `Class.ReplicatedStorage`. Upon running the game the module will begin running.

### Test in Studio

To test the module in Studio, the **FriendsLocator** module must be run in a multi-client simulation, since no friends will be present in a solo playtest.

1. In **StarterPlayerScripts**, create a new `Class.LocalScript` and rename it **ConfigureFriendsLocator**.
2. Paste the following code into the new **ConfigureFriendsLocator** script. The `showAllPlayers` setting within the [configure](#configure) function ensures that locators are shown for all users while testing in Studio, but not in a published place.```lua
local RunService = game:GetService("RunService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local FriendsLocator = require(ReplicatedStorage.FriendsLocator)

FriendsLocator.configure({
	showAllPlayers = RunService:IsStudio(), -- Allows for debugging in Studio
})
```
3. From Studio's mezzanine, start a [multi-client simulation](/docs/en-us/studio/testing-modes.md#multi-client-simulation) with 2 clients. Three new instances of Studio will open; one simulated server and two simulated clients.![Server & Clients option in the testing modes dropdown of Studio's mezzanine.](../../assets/studio/general/Mezzanine-Testing-Mode-Server-Clients.png)
4. Go into either of the **client** Studio instances, move a distance of 100 studs away from the other character, and you should see a **locator icon** appear over its head.
  > **Info:** Due to the way user IDs are handled in Studio, avatar images will not appear on the locator icons during testing.
  > **Warning:** By default, clicking/tapping a friends's icon will teleport your character to that character's location. If you keep this default behavior and you find that streaming pause is occurring under the [instance streaming](/docs/en-us/workspace/streaming.md) architecture, you may want to [request area streaming](/docs/en-us/workspace/streaming/techniques.md#proactive-streaming) around the teleport location as shown in the [clicked](#clicked) event code sample.

### Connect to events

The **FriendsLocator** module exposes [events](#events) so that you can introduce custom behaviors when users interact with a locator icon.

1. Make sure that you've created the **ConfigureFriendsLocator** script outlined in [testing in Studio](#test-in-studio).
2. Add lines 8 and 11-13 to the script:```lua
local RunService = game:GetService("RunService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local FriendsLocator = require(ReplicatedStorage.FriendsLocator)

FriendsLocator.configure({
	showAllPlayers = RunService:IsStudio(), -- Allows for debugging in Studio
	teleportToFriend = false, -- Prevent teleport on icon click/tap
})

FriendsLocator.clicked:Connect(function(player, playerCFrame)
	print("You clicked on locator icon for", player.DisplayName)
end)
```
3. Conduct a [multi-client test](#test-in-studio) and click on another character's locator icon. Notice that your character does not teleport to that location, and the event triggers to allow for custom handling of icon clicks.

### Custom locator UI

If the default style does not fit your game, you can replace the default avatar portrait UI with your own UI.

To replace the default UI:

1. Create a new `Class.ScreenGui` instance inside the **StarterGui** container.
2. Create a `Class.Frame` instance named **FriendLocator** as a child of the new `Class.ScreenGui`, then add elements like `Class.ImageLabel|ImageLabels`, `Class.TextLabel|TextLabels` to design your custom UI.
3. When finished, **disable** the parent `Class.ScreenGui` so that the module doesn't show the custom locator UI until needed.
4. **OPTIONAL** If you want the friend's avatar portrait and `Class.Player.DisplayName|DisplayName` to show up somewhere in the custom UI, you can place the following instances inside the **FriendLocator** frame.
  - An `Class.ImageLabel` of the name **Portrait**.
  - A `Class.TextLabel` of the name **DisplayName**. The module will look for these items and display the friend's avatar portrait and/or display name respectively.

## API reference

### Functions

#### configure

_ configure(config: `Library.table`)_

Overrides default configuration options through the following keys/values in the `config` table.

| Key | Description | Default |
| --- | --- | --- |
| `alwaysOnTop` | If `true`, shows locator icons on top of everything, preventing them from being blocked by 3D world objects. | true |
| `showAllPlayers` | If `true`, shows locations for all players, not just friends; this can help verify the module's functionality in Studio. | false |
| `teleportToFriend` | Teleports player character to the friend's location when their locator icon is clicked or tapped. | true |
| `thresholdDistance` | Camera distance threshold at which locator icons appear; friends closer than this distance will not display icons. | 100 |
| `maxLocators` | Maximum number of locator icons shown at any given time. | 10 |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local FriendsLocator = require(ReplicatedStorage.FriendsLocator)

FriendsLocator.configure({
	alwaysOnTop = true,
	showAllPlayers = false,
	teleportToFriend = true,
	thresholdDistance = 100,
	maxLocators = 10
})
```

### Events

#### clicked

Fires when a locator icon is clicked/activated by the local player. This event can only be connected in a `Class.LocalScript`.

| Parameters |
| --- |
| player: `Class.Player` | Player that the locator icon belongs to. |
| playerCFrame: `Datatype.CFrame` | `Datatype.CFrame` of the player's `Class.Humanoid.RootPart` that the locator icon belongs to. |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Players = game:GetService("Players")
local Workspace = game:GetService("Workspace")

local FriendsLocator = require(ReplicatedStorage.FriendsLocator)

local localPlayer = Players.LocalPlayer

FriendsLocator.clicked:Connect(function(player, playerCFrame)
	-- Request streaming around target location
	if Workspace.StreamingEnabled then
		local success, errorMessage = pcall(function()
			localPlayer:RequestStreamAroundAsync(playerCFrame.Position)
		end)
		if not success then
			print(errorMessage)
		end
	end

	print("You clicked on locator icon for", player.DisplayName, "at position", playerCFrame.Position)
end)
```

#### visibilityChanged

Fires when a locator icon is shown/hidden on the local player's screen. This event can only be connected in a `Class.LocalScript`.

| Parameters |
| --- |
| player: `Class.Player` | `Class.Player` object that the locator icon belongs to. |
| playerCFrame: `Datatype.CFrame` | `Datatype.CFrame` of the player's `Class.Humanoid.RootPart` that the locator icon belongs to. |
| isVisible: `boolean` | Whether the locator icon is currently visible on the local player's screen. Note that this will still be `true` if `alwaysOnTop` is `false` and the locator renders behind an object in the 3D world. |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local FriendsLocator = require(ReplicatedStorage.FriendsLocator)

FriendsLocator.visibilityChanged:Connect(function(player, playerCFrame, isVisible)
	print("Visibility of locator icon for", player.DisplayName, ":", isVisible)
end)
```
