---
title: "Scavenger Hunt"
url: /docs/en-us/resources/modules/scavenger-hunt
last_updated: 2026-10-30T19:55:55Z
description: "The Scavenger Hunt module gives players an inherently gamified way to explore a game."
---

# Scavenger Hunt

The **ScavengerHunt** [developer module](/docs/en-us/resources/modules.md) gives players an inherently gamified way to explore your game, organically introducing them to the entire place. Player progress is persistent, so scavenger hunts can continue across sessions.

> **Warning:** This module utilizes [data stores](/docs/en-us/cloud-services/data-stores.md). To test it in Studio, make sure **Enable Studio Access to API Services** is enabled from the **Security** section of Studio's **Experience Settings** window.
## Module usage

### Installation

To use the **ScavengerHunt** module in a game:

1. From Studio's **Window** menu or **Home** tab toolbar, open the [Toolbox](/docs/en-us/projects/assets/toolbox.md) and select the **Creator Store** tab.
2. Make sure the **Models** sorting is selected, then click the **See All** button for **Categories**.
3. Locate and click the **Packages** tile.
4. Locate the **Scavenger Hunt** module and click it, or drag-and-drop it into the 3D view.
5. In the [Explorer](/docs/en-us/studio/explorer.md) window, move the entire **ScavengerHunt** model into `Class.ReplicatedStorage`. Upon running the game the module will begin running.

### Use tokens

The scavenger hunt module uses **tokens** as the items which players search for and collect. The module comes with one token model that you can position in the 3D world.

1. Locate the **Token1** mesh inside the **Workspace** folder of the module's main folder.
2. Move **Token1** into the top-level **Workspace** hierarchy and position it where desired.
3. Give the token a **unique name**; this name is how the module tracks which tokens each player has collected.
4. To add more tokens, duplicate an existing token and give it a unique name.

If you don't want to use the bundled mesh tokens, any `Class.Model` or `Class.BasePart` will work, as long as it meets the following criteria:

- Object has a `Class.CollectionService` tag of `ScavengerHuntPart`. If desired, the `Class.CollectionService` tag name which the module utilizes can be changed by setting a different value for `tokenTag` in a [configureServer](#configureserver) call.
- Object contains a child `Class.StringValue` instance set to the "flavor text" to display when the token is collected._Model__MeshPart_

> **Error:** Remember that each token must have a unique name as a means of tracking player progress.
> **Info:** The module will automatically disable the `Class.BasePart.CanCollide|CanCollide` property of tokens at runtime so that players do not physically collide with them. As such, all tokens should be **anchored** so they do not fall through the world geometry.
### Use regions

Regions differ slightly from tokens, as large areas that are marked as "collected" once the player enters them. Additionally, when a player leaves the region, the flavor text modal automatically dismisses and the region itself is removed from the workspace.

1. Create an anchored part around the region, such as a block or sphere. The module will automatically disable the `Class.BasePart.CanCollide|CanCollide` property on runtime so players do not physically collide with the region.
2. Give it a **unique name**. This name is how the module tracks which regions each player has entered.
3. Using the [Tags](/docs/en-us/studio/properties.md#instance-tags) section of the part's properties, apply the tag `ScavengerHuntPart` to the part so that `Class.CollectionService` detects it. If desired, the tag name which the module utilizes can be changed by setting a different value for `tokenTag` in a [configureServer](#configureserver) call.
4. Include a child `Class.StringValue` instance set to the "flavor text" to display when the region is entered.

> **Error:** Remember that each region must have a unique name as a means of tracking player progress.
### Configuration

The module is preconfigured to work for most use cases, but it can be easily customized. For example, to change the token rotation speed and customize the modal info message:

1. In **StarterPlayerScripts**, create a new `Class.LocalScript` and rename it to **ConfigureScavengerHunt**.
2. Paste the following code into the new script.```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local ScavengerHunt = require(ReplicatedStorage.ScavengerHunt)

ScavengerHunt.configureClient({
	infoModalText = "Welcome to my Scavenger Hunt!",
	completeModalText = "Thanks for playing my Scavenger Hunt!",
	tokenRotationSpeed = 60,
})
```

### Collection events

Every time a player collects a token or enters a region, the [collected](#collected) event fires. You can listen to this event from a server-side `Class.Script` and respond accordingly. The connected function receives the `Class.Player` that collided with the token or entered the region and that token or region's name.

Similarly, when a player collects **all** tokens or enters **all** tagged regions, the [allCollected](#allcollected) event fires and the connected function receives the associated `Class.Player`. This function is only fired once per player and it can be used to reward that player with a [badge](/docs/en-us/production/publishing/badges.md), access to a new area, [in-game currency](/docs/en-us/production/monetization/developer-products.md), etc.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local ScavengerHunt = require(ReplicatedStorage.ScavengerHunt)

ScavengerHunt.collected:Connect(function(player, itemName)
	print(player.DisplayName, itemName)
end)

ScavengerHunt.allCollected:Connect(function(player)
	print(player.DisplayName .. " completed the hunt!")
end)
```

### Custom GUI

This module exposes several options to customize its default GUI, but you can opt to display custom GUI elements instead.

When `useCustomModals` is set to `true` in the [configureClient](#configureclient) function, the [showInfoModal](#showinfomodal) event fires every time the player activates the token tracker. Similarly, the [showCompleteModal](#showcompletemodal) event fires when the player has collected everything in the scavenger hunt. Both of these events can be listened to in a `Class.LocalScript`.

```lua
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local ScavengerHunt = require(ReplicatedStorage.ScavengerHunt)

ScavengerHunt.showInfoModal:Connect(function()
	-- Show a custom info modal
	local infoModal = Players.LocalPlayer.PlayerGui.ScavengerInfoModal
	infoModal.Enabled = true
end)

ScavengerHunt.showCompleteModal:Connect(function()
	-- Show a custom complete modal
	local completeModal = Players.LocalPlayer.PlayerGui.ScavengerCompleteModal
	completeModal.Enabled = true
end)
```

> **Warning:** When using custom modals, be sure to provide a way for players to close/hide them, or an automatic dismissal after a delay.
### GUI visibility

By default, the scavenger hunt hides all `Class.ScreenGui|ScreenGuis` and `Class.CoreGui|CoreGuis` (except for the player list) when the info modal or completion modal appears. If you want to override this auto-hiding behavior and programmatically decide which GUIs should remain visible, include the [hideOtherGuis](#hideotherguis) and [showOtherGuis](#showotherguis) callbacks and respond with your own custom logic.

```lua
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local StarterGui = game:GetService("StarterGui")

local ScavengerHunt = require(ReplicatedStorage.ScavengerHunt)

local player = Players.LocalPlayer
local playerGui = player:WaitForChild("PlayerGui")
local hiddenInstances = {}

-- Create a screen GUI that will not be hidden
local specialGuiInstance = Instance.new("ScreenGui")
-- Draw the screen GUI above the scavenger hunt GUI
specialGuiInstance.DisplayOrder = 1
specialGuiInstance.Parent = playerGui
-- Add text label to the GUI
local specialLabel = Instance.new("TextLabel")
specialLabel.Size = UDim2.fromScale(1, 0.1)
specialLabel.Text = "Remains visible when displaying modals"
specialLabel.Font = Enum.Font.GothamMedium
specialLabel.TextSize = 24
specialLabel.Parent = specialGuiInstance

ScavengerHunt.hideOtherGuis(function()
	-- Hide all developer-defined screen GUIs
	local instances = playerGui:GetChildren()
	for _, instance in instances do
		if instance:IsA("ScreenGui") and not instance.Name == "ScavengerHunt" and instance.Enabled then
			instance.Enabled = false
			table.insert(hiddenInstances, instance)
		end
	end
	-- Hide specific core GUIs
	StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.PlayerList, false)
end)

ScavengerHunt.showOtherGuis(function()
	-- Show all developer-defined screen GUIs that were hidden
	for _, instance in hiddenInstances do
		instance.Enabled = true
	end
	hiddenInstances = {}
	-- Show specific core GUIs that were hidden
	StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.PlayerList, true)
end)
```

## API reference

### Functions

#### configureClient

_ configureClient(config: `Library.table`)_

Overrides default client-side configuration options through the following keys/values in the `config` table. This function can only be called from a `Class.LocalScript`.

#### General

| Key | Description | Default |
| --- | --- | --- |
| `autoDismissTime` | Time in seconds before the modal automatically dismisses itself or navigates to the next page if there is one. Set to 0 to disable. | 20 |
| `closeModalGamepad` | Gamepad button used to close modals (`Enum.KeyCode`). | `Enum.KeyCode\|ButtonA` |
| `closeModalKeyboard` | Keyboard key used to close modals (`Enum.KeyCode`). | `Enum.KeyCode\|E` |
| `completeModalText` | Text to show on the modal that appears after clicking the token tracker when the scavenger hunt is complete. | "Thanks for participating!" |
| `infoModalText` | Text to show on the modal that appears after clicking the token tracker. | "Find all the tokens to complete the hunt" |
| `tokenRotationSpeed` | Speed at which the tokens rotate, in degrees per second. Set to 0 to prevent rotation. | 20 |
| `nextArrowImage` | Image used to indicate there are more modal pages to show after the current modal page. | "rbxassetid://8167172095" |
| `openTokenTrackerGamepad` | Gamepad button used to show the modals that appear after activating the token tracker (`Enum.KeyCode`). | `Enum.KeyCode\|ButtonY` |
| `openTokenTrackerKeyboard` | Keyboard key used to show the modals that appear after activating the token tracker (`Enum.KeyCode`). | `Enum.KeyCode\|Y` |
| `openTokenTrackerGamepadButtonImage` | Image for the gamepad button that is used to activate the token tracker. | "rbxassetid://8025860488" |
| `regionIcon` | Icon to display next to the token tracker when entering regions. | "rbxassetid://8073794624" |
| `tokenIcon` | Icon to display next to the token tracker when collecting tokens. | "rbxassetid://8073794477" |
| `tokenTrackerPositionSmallDevice` | Position of the token tracker UI on small devices such as phones (`Datatype.UDim2`). | (1, 0, 0, 84) |
| `tokenTrackerPositionLargeDevice` | Position of the token tracker UI on larger devices like tablets and PC (`Datatype.UDim2`). | (1, 0, 1, -16) |
| `useRegions` | Instead of [tokens](#use-tokens), use [regions](#use-regions). | false |

#### Modals

| Key | Description | Default |
| --- | --- | --- |
| `modal.backgroundColor` | Background color of the modals (`Datatype.Color3`). | [0, 0, 0] |
| `modal.font` | Font of the text that appears in a modal (`Enum.Font`). | `Enum.Font\|GothamMedium` |
| `modal.textColor` | Color of the text that appears in a modal (`Datatype.Color3`). | [255, 255, 255] |
| `modal.textSize` | Size of the text that appears in a modal. | 16 |
| `useCustomModals` | If true, default modals are not displayed. This lets you show custom modals as outlined in [Custom GUI](#custom-gui). | false |
| `useCustomTokenTracker` | If true, the default token tracker is not displayed. This lets you show a custom token tracker GUI instead. | false |

#### Navigation Beam

| Key | Description | Default |
| --- | --- | --- |
| `showNavigationBeam` | If true, a `Class.Beam` from the player to the nearest token will be shown. | true |
| `navigationBeam.color` | `Datatype.ColorSequence` defining the beam's color across its segments. See `Class.Beam.Color` for details. | [255, 255, 255] → [255, 255, 255] |
| `navigationBeam.curveSize0` | Position of the first control point in the beam's Bézier curve. See `Class.Beam.CurveSize0` for more info. | 0 |
| `navigationBeam.curveSize1` | Position of the second control point in the beam's Bézier curve. See `Class.Beam.CurveSize1` for more info. | 0 |
| `navigationBeam.faceCamera` | Whether the beam's segments will always face the camera regardless of its orientation. See `Class.Beam.FaceCamera` for details. | true |
| `navigationBeam.lightEmission` | Degree to which the colors of the beam are blended with the colors behind it. See `Class.Beam.LightEmission` for details. | 0 |
| `navigationBeam.lightInfluence` | Degree to which the beam is influenced by the environment's lighting. See `Class.Beam.LightInfluence` for details. | 0 |
| `navigationBeam.segments` | How many straight segments the beam is made up of. | 10 |
| `navigationBeam.texture` | Asset ID of the texture to be displayed on the beam. | "rbxassetid://8081777495" |
| `navigationBeam.textureLength` | Length of the beam's texture, depending on the setting for `navigationBeam.textureMode`. See `Class.Beam.TextureLength` for details. | 1 |
| `navigationBeam.textureMode` | Manner in which the beam texture scales and repeats (`Enum.TextureMode`). | `Enum.TextureMode\|Wrap` |
| `navigationBeam.textureSpeed` | Speed at which the texture image moves along the beam. | 1 |
| `navigationBeam.transparency` | `Datatype.NumberSequence` defining the beam's transparency across its segments. See `Class.Beam.Transparency` for details. | (0, 0) → (0.15, 1) → (1, 1) |
| `navigationBeam.width0` | Width of the beam at its base, in studs. | 1 |
| `navigationBeam.width1` | Width of the beam at its end, in studs. | 1 |
| `navigationBeam.zOffset` | Distance, in studs, by which the beam's display is offset, relative to the camera. | 0 |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local ScavengerHunt = require(ReplicatedStorage.ScavengerHunt)

ScavengerHunt.configureClient({
	infoModalText = "Welcome to my Scavenger Hunt!",
	completeModalText = "Thanks for playing my Scavenger Hunt!",
	tokenRotationSpeed = 60,
	navigationBeam = {
		lightEmission = 1
	},
	modal = {
		textSize = 14
	},
})
```

#### configureServer

_ configureServer(config: `Library.table`)_

Overrides default server-side configuration options through the following keys/values in the `config` table. This function can only be called from a `Class.Script`.

| Key | Description | Default |
| --- | --- | --- |
| `tokenTag` | Tag used by `Class.CollectionService` to find all the tokens or regions used in the scavenger hunt. | "ScavengerHuntPart" |
| `datastoreName` | Name of the `Class.DataStore` used by the scavenger hunt to store each player's collection progress. | "ScavengerHuntTokens" |
| `resetOnPlayerRemoving` | If true, resets the user's progress when they leave the game; convenient for not saving progress while testing the scavenger hunt. | false |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local ScavengerHunt = require(ReplicatedStorage.ScavengerHunt)

ScavengerHunt.configureServer({
	tokenTag = "GreenGem",
})
```

#### disable

_ disable()_

Hides all UI for the scavenger hunt, disconnects all input event listeners, and prevents players from collecting tokens or interacting with regions. This function can only be called from a `Class.Script`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local ScavengerHunt = require(ReplicatedStorage.ScavengerHunt)

ScavengerHunt.disable()
```

#### enable

_ enable()_

Shows all UI for the scavenger hunt, connects all input event listeners, and allows players to collect tokens and interact with regions. This function can only be called from a `Class.Script`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local ScavengerHunt = require(ReplicatedStorage.ScavengerHunt)

ScavengerHunt.enable()
```

### Events

#### collected

Fires when a player collides with a token or enters a region. The connected function will receive the `Class.Player` that collided with the token or entered the region and the name of the token that was collided into or the region that was entered. This event can only be connected in a `Class.Script`.

| Parameters |
| --- |
| player: `Class.Player` | User who collided with a token or entered a region. |
| itemName: `Library.string` | Name of the token that was collided into or the region that was entered. |
| totalCollected: `number` | Total number of tokens collected by the user represented by `player`. |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local ScavengerHunt = require(ReplicatedStorage.ScavengerHunt)

ScavengerHunt.collected:Connect(function(player, itemName, totalCollected)
	print(player.DisplayName, itemName, totalCollected)
end)
```

#### allCollected

Fires when a player collects all tokens or enters all regions in the scavenger hunt. The connected function will receive the `Class.Player` that collected all tokens, and it is only ever fired once per player. This event can only be connected in a `Class.Script`.

| Parameters |
| --- |
| player: `Class.Player` | Player who collected all tokens or entered all regions. |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local ScavengerHunt = require(ReplicatedStorage.ScavengerHunt)

ScavengerHunt.allCollected:Connect(function(player)
	print(player.DisplayName .. " completed the hunt!")
end)
```

#### showInfoModal

Fires when the player clicks on the token tracker when the `useCustomModals` [configuration](#configureclient) option is set to true. This event can only be connected in a `Class.LocalScript`.

```lua
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local ScavengerHunt = require(ReplicatedStorage.ScavengerHunt)

ScavengerHunt.showInfoModal:Connect(function()
	local infoModal = Players.LocalPlayer.PlayerGui.InfoModal
	infoModal.Enabled = true
end)
```

#### showCompleteModal

Fires when the player clicks on the token tracker when the `useCustomModals` [configuration](#configureclient) option is set to `true` and the player has collected all tokens in the scavenger hunt. This event can only be connected in a `Class.LocalScript`.

```lua
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local ScavengerHunt = require(ReplicatedStorage.ScavengerHunt)

ScavengerHunt.showCompleteModal:Connect(function()
	local completeModal = Players.LocalPlayer.PlayerGui.CompleteModal
	completeModal.Enabled = true
end)
```

### Callbacks

#### hideOtherGuis

_ hideOtherGuis(callback: `function`)_

This callback runs immediately before a modal is displayed, letting you disable entire `Class.ScreenGui|ScreenGuis` or elements within them before the modal is shown. See [GUI Visibility](#gui-visibility) for details and sample code.

#### showOtherGuis

_ showOtherGuis(callback: `function`)_

This callback runs immediately after a modal has been dismissed, letting you enable entire `Class.ScreenGui|ScreenGuis` or elements within them. See [GUI Visibility](#gui-visibility) for details and sample code.
