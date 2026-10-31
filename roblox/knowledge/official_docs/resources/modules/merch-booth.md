---
title: "Merch Booth"
url: /docs/en-us/resources/modules/merch-booth
last_updated: 2026-10-30T19:55:55Z
description: "The Merch Booth module lets you sell avatar assets, passes, and products directly in a game."
---

# Merch Booth

The **MerchBooth** [developer module](/docs/en-us/resources/modules.md) lets you offer [avatar assets](/docs/en-us/avatar/rigid-accessories.md), [passes](/docs/en-us/production/monetization/passes.md), and [developer products](/docs/en-us/production/monetization/developer-products.md) for sale directly within your game. Players can browse items, preview assets on their own avatar, purchase items, and instantly use or equip them — all without leaving your game. This can help you [monetize](/docs/en-us/production/monetization.md) your game and gain revenue through the 40% affiliate fee associated with selling other creators' items.

> **Warning:** To offer assets created by third parties in the merch booth, make sure **Allow Third Party Sales** is enabled from the **Security** section of Studio's **Experience Settings** window. If this setting is disabled, you will not be able to sell UGC assets created by other users.
## Module usage

### Installation

To use the **MerchBooth** module in a game:

1. From Studio's **Window** menu or **Home** tab toolbar, open the [Toolbox](/docs/en-us/projects/assets/toolbox.md) and select the **Creator Store** tab.
2. Make sure the **Models** sorting is selected, then click the **See All** button for **Categories**.
3. Locate and click the **Packages** tile.
4. Locate the **Merch Booth** module and click it, or drag-and-drop it into the 3D view.
5. In the [Explorer](/docs/en-us/studio/explorer.md) window, move the entire **MerchBooth** model into `Class.ReplicatedStorage`. Upon running the game the module will begin running.

### Configuration

The module is preconfigured to work for most use cases, but it can be easily customized through the [configure](#configure) function. For example, to create a lighter theme and disable the default **Filter** button in the upper-left area of the catalog view:

1. In **StarterPlayerScripts**, create a new `Class.LocalScript` and rename it to **ConfigureMerchBooth**.
2. Paste the following code into the new script.```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.configure({
	backgroundColor = Color3.fromRGB(220, 210, 200),
	textSize = 17,
	textFont = Enum.Font.Fondamento,
	textColor = Color3.fromRGB(20, 20, 20),
	useFilters = false
})
```

### Add items

What's a merch booth without merch? The following sections outline how to add [avatar assets](#avatar-assets), [passes](#passes), and [developer products](#developer-products) to your merch booth.

#### Avatar assets

Items such as [clothing and accessories](/docs/en-us/avatar/rigid-accessories.md) must be added through their **asset ID** located on the item's detail page in the [Avatar Shop](https://www.roblox.com/catalog).

1. Create a `Class.Script` within **ServerScriptService** and paste in the following code.```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local items = {

}

for _, assetId in items do
	local success, errorMessage = pcall(function()
		MerchBooth.addItemAsync(assetId)
	end)
	if not success then
		warn(errorMessage)
	end
end
```
2. Copy item asset IDs from their [Avatar Shop](https://www.roblox.com/catalog) website URL. For example, the ID of [Roblox Baseball Cap](https://www.roblox.com/catalog/607702162/Roblox-Baseball-Cap) is **607702162**.
3. Paste each copied ID into a comma-delimited list within the `items` table. By default, items appear in the catalog view in alphabetical order, but you can customize sorting using [setCatalogSort](#setcatalogsort).```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local items = {
	607702162, -- Roblox Baseball Cap
	4819740796, -- Robox
	1374269, -- Kitty Ears
	11884330, -- Nerd Glasses
	10476359, -- Paper Hat
}

for _, assetId in items do
	local success, errorMessage = pcall(function()
		MerchBooth.addItemAsync(assetId)
	end)
	if not success then
		warn(errorMessage)
	end
end
```
  > **Info:** This example uses assets owned by the Roblox account, but a thriving marketplace of incredible community-made assets is available [here](https://www.roblox.com/catalog?Category=13&Subcategory=40).

#### Passes

Adding [passes](/docs/en-us/production/monetization/passes.md) requires pass IDs which can be located in the [Creator Dashboard](https://create.roblox.com/dashboard/creations).

1. Create a `Class.Script` within **ServerScriptService** and paste in the following code.```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local items = {

}

for _, assetId in items do
	local success, errorMessage = pcall(function()
		MerchBooth.addItemAsync(assetId)
	end)
	if not success then
		warn(errorMessage)
	end
end
```
2. Navigate to the [Creator Dashboard](https://create.roblox.com/dashboard/creations) and select the game.
3. In the left column, under **Monetization**, select **Passes**.
4. Hover over a pass' thumbnail, click the **⋯** button, and select **Copy Asset ID** from the context menu.
5. Paste each copied ID into a comma-delimited list within the `items` table **and** include `Enum.InfoType.GamePass` as the second parameter for [addItemAsync](#additemasync) to indicate that the items are passes. By default, items will appear in the catalog view in alphabetical order, but sorting can be customized via [setCatalogSort](#setcatalogsort).```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local items = {
	4343758, -- ColdFyre Armor
	28521575, -- Slime Shield
}

for _, assetId in items do
	local success, errorMessage = pcall(function()
		MerchBooth.addItemAsync(assetId, Enum.InfoType.GamePass)
	end)
	if not success then
		warn(errorMessage)
	end
end
```

#### Developer Products

Adding [developer products](/docs/en-us/production/monetization/developer-products.md) requires product IDs which can be located in the [Creator Dashboard](https://create.roblox.com/dashboard/creations).

1. Create a `Class.Script` within **ServerScriptService** and paste in the following code.```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local items = {

}

for _, assetId in items do
	local success, errorMessage = pcall(function()
		MerchBooth.addItemAsync(assetId)
	end)
	if not success then
		warn(errorMessage)
	end
end
```
2. Navigate to the [Creator Dashboard](https://create.roblox.com/dashboard/creations) and select the game.
3. In the left column, under **Monetization**, select **Developer Products**.
4. Hover over a product's thumbnail, click the **⋯** button, and select **Copy Asset ID** from the context menu.
5. Paste each copied ID into a comma-delimited list within the `items` table **and** include `Enum.InfoType.Product` as the second parameter for [addItemAsync](#additemasync) to indicate that the items are developer products. By default, items appear in the catalog view in alphabetical order, but you can customize sorting using [setCatalogSort](#setcatalogsort).```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local items = {
	1236602053, -- Mana Refill
	1257880672, -- Healing Potion
}

for _, assetId in items do
	local success, errorMessage = pcall(function()
		MerchBooth.addItemAsync(assetId, Enum.InfoType.Product)
	end)
	if not success then
		warn(errorMessage)
	end
end
```

### Custom catalog button

By default, a right-side **catalog button** lets players open the booth at any time.

In some cases, it may be useful to [remove](#togglecatalogbutton) this button and connect your own:

1. Create a new button as outlined in [Buttons](/docs/en-us/ui/buttons.md).
2. Create a `Class.LocalScript` as a child of the button object.
3. Paste the following code into the new script.```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

-- Remove the default catalog button
MerchBooth.toggleCatalogButton(false)

-- Connect the custom button
script.Parent.Activated:Connect(function()
	MerchBooth.openMerchBooth()
end)
```

### Shoppable regions

A helpful way to drive purchases in your game is to automatically show the merch booth when a player enters an area.

To create a shoppable region:

1. Create an `Class.BasePart.Anchored|Anchored` block that encompasses the detection region. Make sure the block is tall enough to collide with the `Class.Model.PrimaryPart|PrimaryPart` of character models (**HumanoidRootPart** by default)._Block to detect when players approach the front of the shop counter_
2. Using the [Tags](/docs/en-us/studio/properties.md#instance-tags) section of the block's properties, apply the tag `ShopRegion` to the block so that `Class.CollectionService` detects it.
3. Set the part's `Class.BasePart.Transparency|Transparency` to the maximum to hide it from players in the game. Also disable its `Class.BasePart.CanCollide|CanCollide` and `Class.BasePart.CanQuery|CanQuery` properties so that objects do not physically collide with it and raycasts do not detect it.
4. Insert a new `Class.LocalScript` under **StarterPlayerScripts**.
5. In the new script, paste the following code which uses the `Class.BasePart.Touched|Touched` and `Class.BasePart.TouchEnded|TouchEnded` events to detect when characters enter/leave the region and calls [openMerchBooth](#openmerchbooth) and [closeMerchBooth](#closemerchbooth) to open/close the booth GUI.```lua
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local CollectionService = game:GetService("CollectionService")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

-- Remove the default catalog button
MerchBooth.toggleCatalogButton(false)

local function setupRegion(region: BasePart)
	region.Touched:Connect(function(otherPart)
		local character = Players.LocalPlayer.Character
		if character and otherPart == character.PrimaryPart then
			MerchBooth.openMerchBooth()
		end
	end)

	region.TouchEnded:Connect(function(otherPart)
		local character = Players.LocalPlayer.Character
		if character and otherPart == character.PrimaryPart then
			MerchBooth.closeMerchBooth()
		end
	end)
end

-- Iterate through existing tagged shop regions
for _, region in CollectionService:GetTagged("ShopRegion") do
	setupRegion(region)
end
-- Detect when non-streamed shop regions stream in
CollectionService:GetInstanceAddedSignal("ShopRegion"):Connect(setupRegion)
```

### Proximity prompts

As an alternative to the 2D catalog view, you can add **proximity prompts** over in-game objects. This encourages players to discover items in the 3D environment, preview them on their own avatar, purchase them, and instantly equip them. See [addProximityButton](#addproximitybutton) for details.

> **Info:** If a player has opened an item view through a proximity prompt, it automatically closes when the player moves further away from the prompt object than its activation distance. If you want to keep the booth open regardless of the player's distance from the prompt, set `closeWhenFarFromPrompt` to `false` in a [configure](#configure) call.
### Change the equip effect

By default, the merch booth shows a generic sparkle effect when a player equips an item from it. To change the effect, set `particleEmitterTemplate` to your own instance of a `Class.ParticleEmitter` in a [configure](#configure) call.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local myParticleEmitter = Instance.new("ParticleEmitter")
myParticleEmitter.SpreadAngle = Vector2.new(22, 22)
myParticleEmitter.Lifetime = NumberRange.new(0.5, 1.5)
myParticleEmitter.Shape = Enum.ParticleEmitterShape.Sphere
myParticleEmitter.Transparency = NumberSequence.new(0, 1)
myParticleEmitter.RotSpeed = NumberRange.new(200, 200)

MerchBooth.configure({
	particleEmitterTemplate = myParticleEmitter
})
```

### GUI visibility

By default, the merch booth hides all `Class.ScreenGui|ScreenGuis` and `Class.CoreGui|CoreGuis` when its UI appears, including the chat, leaderboard, and others included by Roblox. If you want to disable this behavior, set `hideOtherUis` to `false` in a [configure](#configure) call.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.configure({
	hideOtherUis = false
})
```

### Character movement

It can be advantageous to prevent a character from moving while they are in the merch booth. This can be done by setting `disableCharacterMovement` to `true` in a [configure](#configure) call.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.configure({
	disableCharacterMovement = true
})
```

## API reference

### Types

#### Item

Items in the merch booth are represented by a dictionary with the following key-value pairs. Items can be gathered through the [getItems](#getitems) function or the [itemAdded](#itemadded) event.

| Key | Type | Description |
| --- | --- | --- |
| `assetId` | number | Catalog ID of the item, as passed to [addItemAsync](#additemasync). |
| `title` | string | Item title as it appears in the catalog. |
| `price` | number | Item price in Robux. |
| `description` | string | Item description as it appears in the catalog. |
| `assetType` | string | String representing the item's accessory type. |
| `isOwned` | bool | Whether the current player owns the item. |
| `creatorName` | string | Item creator as shown in the catalog. |
| `creatorType` | `Enum.CreatorType` | Creator type for the item. |

### Enums

#### MerchBooth.Controls

Used along with [setControlKeyCodes](#setcontrolkeycodes) to customize the keys and gamepad buttons for interacting with the merch booth.

| Name | Summary |
| --- | --- |
| `ProximityPrompts` | Key and/or gamepad button to open the item view when [proximity prompts](#proximity-prompts) are configured. |
| `OpenMerchBooth` | Key and/or gamepad button to open the merch booth. |
| `CloseMerchBooth` | Key and/or gamepad button to close the merch booth. |
| `Filter` | Key and/or gamepad button to use the default **Filter** pulldown in the upper-left area of the catalog view. |
| `ViewItem` | Key and/or gamepad button to open a specific merch booth item view. |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.setControlKeyCodes(MerchBooth.Controls.ProximityPrompts, {
	keyboard = Enum.KeyCode.Q,
	gamepad = Enum.KeyCode.ButtonL1
})
```

### Functions

#### configure

_ configure(config: `Library.table`)_

Overrides default client-side configuration options through the following keys/values in the `config` table. This function can only be called from a `Class.LocalScript`.

#### Appearance

| Key | Description | Default |
| --- | --- | --- |
| `backgroundColor` | Main background color of the window (`Datatype.Color3`). | [0, 0, 0] |
| `cornerRadius` | Corner radius for the main window (`Datatype.UDim`). | (0, 16) |
| `cornerRadiusSmall` | Corner radius for elements inside the window (`Datatype.UDim`). | (0, 8) |
| `textFont` | Font of "main text" such as prices, descriptions, and other general info (`Enum.Font`). | `Enum.Font\|Gotham` |
| `textSize` | Size of the main text. | 14 |
| `textColor` | Color of the main text (`Datatype.Color3`). | [255, 255, 255] |
| `secondaryTextColor` | Color used for some variations of the main text (`Datatype.Color3`). | [153, 153, 158] |
| `headerFont` | Font of the header text used for the window title (`Enum.Font`). | `Enum.Font\|GothamMedium` |
| `headerTextSize` | Size of the header text used for the window title. | 18 |
| `titleFont` | Font of the title text used for item names on the item detail page (`Enum.Font`). | `Enum.Font\|GothamBold` |
| `titleTextSize` | Size of the title text used for item names on the item detail page. | 28 |
| `buttonColor` | Background color for larger buttons in a clickable state, such as the main purchase button in item view (`Datatype.Color3`). | [255, 255, 255] |
| `buttonTextColor` | Text color for larger buttons in a clickable state, such as the main purchase button in item view (`Datatype.Color3`). | [0, 0, 0] |
| `secondaryButtonColor` | Background color for smaller buttons such as the price buttons in catalog view or the **Try On** button (`Datatype.Color3`). | [34, 34, 34] |
| `secondaryButtonTextColor` | Text color for smaller buttons such as the price buttons in catalog view or the **Try On** button (`Datatype.Color3`). | [255, 255, 255] |
| `inactiveButtonColor` | Background color for all buttons in an un-clickable state (`Datatype.Color3`). | [153, 153, 158] |
| `inactiveButtonTextColor` | Text color for all buttons in an un-clickable state (`Datatype.Color3`). | [255, 255, 255] |
| `particleEmitterTemplate` | Optional custom `Class.ParticleEmitter` instance that appears and plays on equip. | |

#### Proximity Prompts

| Key | Description | Default |
| --- | --- | --- |
| `proximityButtonActivationDistance` | Maximum distance a player's character can be from the [prompt](#proximity-prompts) adornee for the prompt to appear. | 10 |
| `proximityButtonExclusivity` | `Enum.ProximityPromptExclusivity` specifying which prompts can be shown at the same time. | `Enum.ProximityPromptExclusivity\|OnePerButton` |
| `proximityButtonOffset` | Pixel offset applied to the prompt's UI (`Datatype.Vector2`). | (0, 0) |
| `proximityButtonPulseCount` | How many "pulses" occur around proximity buttons before stopping. | 3 |

#### Behavior

| Key | Description | Default |
| --- | --- | --- |
| `useFilters` | Toggles on/off the **Filter** button shown in the catalog. | true |
| `disableCharacterMovement` | If `true`, prevents character from moving while the merch booth is open. | false |
| `hideOtherUis` | If `true`, the merch booth hides all `Class.ScreenGui\|ScreenGuis` and `Class.CoreGui\|CoreGuis` when its UI appears. | true |
| `closeWhenFarFromPrompt` | If `true` **and** if the player has opened an item view through a proximity prompt, the merch booth will automatically close when the player moves further away from the prompt object than its activation distance. | true |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.configure({
	backgroundColor = Color3.fromRGB(255, 255, 255),
	textSize = 16,
	textFont = Enum.Font.Roboto,
	textColor = Color3.fromRGB(20, 20, 20),
	hideOtherUis = false,
})
```

#### addItemAsync

_ addItemAsync(assetId: `number`, productType: `Enum.InfoType`, hideFromCatalog: `boolean`)_

Asynchronously adds an item to the merch booth so that it's eligible for purchase in the game. `assetId` is the item's asset ID, `productType` is the item's `Enum.InfoType` enum, and `hideFromCatalog` can be used to hide the item in the catalog view.

See [Adding Items](#add-items) for details, as usage varies slightly for **assets** versus **game passes** or **developer products**.

> **Warning:** This function can only be called from a `Class.Script` and it performs an asynchronous network call that may occasionally fail. As shown below, it's recommended that it be wrapped in `Global.LuaGlobals.pcall()` to catch and handle errors.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local items = {
	607702162, -- Roblox Baseball Cap
	4819740796, -- Robox
	1374269, -- Kitty Ears
	11884330, -- Nerd Glasses
	10476359, -- Paper Hat
}

for _, assetId in items do
	local success, errorMessage = pcall(function()
		MerchBooth.addItemAsync(assetId)
	end)
	if not success then
		warn(errorMessage)
	end
end
```

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local items = {
	4343758, -- ColdFyre Armor
	28521575, -- Slime Shield
}

for _, assetId in items do
	local success, errorMessage = pcall(function()
		MerchBooth.addItemAsync(assetId, Enum.InfoType.GamePass)
	end)
	if not success then
		warn(errorMessage)
	end
end
```

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local items = {
	1236602053, -- Mana Refill
	1257880672, -- Healing Potion
}

for _, assetId in items do
	local success, errorMessage = pcall(function()
		MerchBooth.addItemAsync(assetId, Enum.InfoType.Product)
	end)
	if not success then
		warn(errorMessage)
	end
end
```

#### getItems

_ getItems(): `Library.table`_

Returns a dictionary representing all of the currently registered items. Each key is an item's asset ID as a string, and each key's value is an [Item](#item). This function can only be called from a `Class.Script`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local success, errorMessage = pcall(function()
	MerchBooth.addItemAsync(4819740796)
end)
if success then
	local items = MerchBooth.getItems()
	print(items)
end
```

#### removeItem

_ removeItem(assetId: `number`)_

Unregisters an item previously added with [addItemAsync](#additemasync), removing its tile in the catalog view and any [proximity prompts](#proximity-prompts) assigned to it. This function can only be called from a `Class.Script`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local success, errorMessage = pcall(function()
	MerchBooth.addItemAsync(4819740796)
end)
if success then
	-- After some time, remove the item
	task.wait(5)
	MerchBooth.removeItem(4819740796)
end
```

#### addProximityButton

_ addProximityButton(adornee: `Class.BasePart`|`Class.Model`|`Class.Attachment|Attachment`, assetId: `number`)_

Adds a [proximity prompt](#proximity-prompts) over the given `adornee` that will trigger the display of an item's purchase view, given its asset ID. This can be used as an alternative to the 2D catalog view, encouraging players to discover items in the 3D environment.

Note that an item must be added via [addItemAsync](#additemasync) before a proximity button can be assigned to it. See also [removeProximityButton](#removeproximitybutton) to remove the proximity prompt from an object.

> **Info:** When implementing proximity prompts, you may want to [remove the catalog button](#togglecatalogbutton) to eliminate its usage in opening the booth.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Workspace = game:GetService("Workspace")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local success, errorMessage = pcall(function()
	MerchBooth.addItemAsync(4819740796)
end)
if success then
	local item = Workspace:FindFirstChild("Robox")
	if item then
		MerchBooth.addProximityButton(item, 4819740796)
	end
end
```

#### removeProximityButton

_ removeProximityButton(adornee: `Class.BasePart`|`Class.Model`|`Class.Attachment|Attachment`)_

Removes a [proximity prompt](#proximity-prompts) generated through [addProximityButton](#addproximitybutton). This function can only be called from a `Class.Script`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Workspace = game:GetService("Workspace")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local success, errorMessage = pcall(function()
	MerchBooth.addItemAsync(4819740796)
end)
if success then
	local item = Workspace:FindFirstChild("Robox")
	if item then
		MerchBooth.addProximityButton(item, 4819740796)
	end

	-- After some time, remove the prompt
	task.wait(5)
	MerchBooth.removeProximityButton(item)
end
```

#### setCatalogSort

_ setCatalogSort(sortFunction: `function`): `boolean`_

Sets the sorting function `sortFunction` to be used in the catalog view. The provided sorting function can use logic based on [Item](#item) info such as `price` or `title`. This function can only be called from a `Class.LocalScript`.

Here are some examples for sorting the catalog:

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.setCatalogSort(function(a, b)
	return a.price < b.price
end)
```

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.setCatalogSort(function(a, b)
	return a.price > b.price
end)
```

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.setCatalogSort(function(a, b)
	return if a.price == b.price then a.title < b.title else a.price < b.price
end)
```

#### setControlKeyCodes

_ setControlKeyCodes(control: [MerchBooth.Controls](#merchboothcontrols), keyCodes: `Library.table`)_

Configures the key and button values for interactions with the merch booth. The first parameter must be a [MerchBooth.Controls](#merchboothcontrols) enum and the second parameter a table containing the keys `keyboard` and/or `gamepad` with corresponding `Enum.KeyCode` enums.

| Enum (`control`) | Default `keyCodes` Keys/Values |
| --- | --- |
| `MerchBooth.Controls.ProximityPrompts` | `keyboard = Enum.KeyCode.E`<br>`gamepad = Enum.KeyCode.ButtonY` |
| `MerchBooth.Controls.OpenMerchBooth` | `gamepad = Enum.KeyCode.ButtonY` |
| `MerchBooth.Controls.CloseMerchBooth` | `gamepad = Enum.KeyCode.ButtonB` |
| `MerchBooth.Controls.Filter` | `gamepad = Enum.KeyCode.ButtonX` |
| `MerchBooth.Controls.ViewItem` | `gamepad = Enum.KeyCode.ButtonA` |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.setControlKeyCodes(MerchBooth.Controls.ProximityPrompts, {
	keyboard = Enum.KeyCode.Q,
	gamepad = Enum.KeyCode.ButtonL1,
})
```

#### openMerchBooth

_ openMerchBooth()_

Opens the merch booth window (if closed) and navigates to the catalog view. This function can only be called from a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local success, errorMessage = pcall(function()
	MerchBooth.addItemAsync(assetId)
end)
if not success then
	warn(errorMessage)
end

MerchBooth.openMerchBooth()
```

#### openItemView

_ openItemView(itemId: `number`)_

Navigates to the single item view of the given `itemId`, opening the merch booth window if it is currently closed. This function can only be called from a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local success, errorMessage = pcall(function()
	MerchBooth.addItemAsync(4819740796)
end)
if success then
	MerchBooth.openItemView(4819740796)
end
```

#### toggleCatalogButton

_ toggleCatalogButton(enabled: `boolean`)_

Toggles on/off the catalog button on the right side of the screen. This is useful when implementing a [custom button](#custom-catalog-button) or limiting the merch booth's appearance to [regions](#shoppable-regions) or [proximity prompts](#proximity-prompts). Can only be called from a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.toggleCatalogButton(false)
```

#### isMerchBoothOpen

_ isMerchBoothOpen(): `Tuple`_

Returns `true` if either the catalog or the item view is open. If the item view is open, the item's asset ID is returned as the second value. This function can only be called from a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local success, errorMessage = pcall(function()
	MerchBooth.addItemAsync(4819740796)
end)
if success then
	MerchBooth.openItemView(4819740796)

	local isOpen, itemId = MerchBooth.isMerchBoothOpen()
	print(isOpen, itemId)
end
```

#### closeMerchBooth

_ closeMerchBooth()_

Closes the merch booth window. This function can only be called from a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.closeMerchBooth()
```

#### isMerchBoothEnabled

_ isMerchBoothEnabled(): `boolean`_

This function may be used in tandem with [setEnabled](#setenabled) to check whether the merch booth is currently enabled or not. Can only be called from a `Class.LocalScript`.

#### setEnabled

_ setEnabled(enabled: `boolean`)_

Sets whether the entire merch booth is enabled or not. When disabled, this function removes the entire UI, including [proximity prompts](#proximity-prompts), and disconnects all [events](#events). This function can only be called from a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

local isEnabled = MerchBooth.isMerchBoothEnabled()
if isEnabled then
	MerchBooth.setEnabled(false)
end
```

### Events

#### itemAdded

Fires when an item is added through [addItemAsync](#additemasync). This event can only be connected in a `Class.Script`.

| Parameters |
| --- |
| assetId: `number` | Item asset ID. |
| itemInfo: `Library.table` | Dictionary of [Item](#item) info such as `price` or `title`. |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.itemAdded:Connect(function(assetId, itemInfo)
	print("Item added with asset ID of", assetId)
	print(itemInfo)
end)
```

#### itemRemoved

Fires when an item is removed through [removeItem](#removeitem). This event can only be connected in a `Class.Script`.

| Parameters |
| --- |
| assetId: `number` | Item asset ID. |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.itemRemoved:Connect(function(assetId)
	print("Item removed with asset ID of", assetId)
end)
```

#### merchBoothOpened

Fires when either the catalog **or** item detail view are opened.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.merchBoothOpened:Connect(function()
	print("Booth view opened")
end)
```

#### merchBoothClosed

Fires when either the catalog **or** item detail view are closed.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.merchBoothClosed:Connect(function()
	print("Booth view closed")
end)
```

#### catalogViewOpened

Fires when the catalog view is opened.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.catalogViewOpened:Connect(function()
	print("Catalog view opened")
end)
```

#### catalogViewClosed

Fires when the catalog view is closed.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.catalogViewClosed:Connect(function()
	print("Catalog view closed")
end)
```

#### itemViewOpened

Fires when the item detail view is opened.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.itemViewOpened:Connect(function()
	print("Item view opened")
end)
```

#### itemViewClosed

Fires when the item detail view is closed.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local MerchBooth = require(ReplicatedStorage.MerchBooth)

MerchBooth.itemViewClosed:Connect(function()
	print("Item view closed")
end)
```
