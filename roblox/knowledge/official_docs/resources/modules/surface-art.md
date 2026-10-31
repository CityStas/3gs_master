---
title: "Surface Art"
url: /docs/en-us/resources/modules/surface-art
last_updated: 2026-10-30T19:55:55Z
description: "The Surface Art module lets players literally leave their mark in a game."
---

# Surface Art

Players often enjoy feeling like they're a part of constructing the space they're in. The **SurfaceArt** [developer module](/docs/en-us/resources/modules.md) lets players literally leave their mark in a game.

> **Warning:** By default, a player can place 2 pieces of art across all of the tagged surfaces in the workspace. All of a player's art will be removed when they leave the game.
## Module Usage

### Installation

To use the **SurfaceArt** module in a game:

1. From Studio's **Window** menu or **Home** tab toolbar, open the [Toolbox](/docs/en-us/projects/assets/toolbox.md) and select the **Creator Store** tab.
2. Make sure the **Models** sorting is selected, then click the **See All** button for **Categories**.
3. Locate and click the **Packages** tile.
4. Locate the **Surface Art** module and click it, or drag-and-drop it into the 3D view.
5. In the [Explorer](/docs/en-us/studio/explorer.md) window, move the entire **SurfaceArt** model into `Class.ReplicatedStorage`. Upon running the game the module will begin running.

### Positioning the Canvas

The module comes with one **SurfaceCanvas** model that you can position in the 3D world. This model is what players will interact with to place art on its surface.

1. Locate the **SurfaceCanvas** mesh inside the **Workspace** folder of the module's main folder.
2. Move it into the top-level **Workspace** hierarchy and position it where desired.
3. Upon publishing/running a test session, players will be able to interact with the object via a `Class.ProximityPrompt` and place art on the defined surface.

> **Info:** It is not required that you use the packaged mesh for placing art. The module uses `Class.CollectionService` to locate parts tagged as `SurfaceCanvas` and make them operate as canvases. Any tagged canvas must be a `Class.BasePart` and it should have an [attribute](/docs/en-us/studio/properties.md#instance-attributes) defining the surface face as outlined in [Changing the Canvas Face](#changing-the-canvas-face).
### Changing the Canvas Face

Under the hood, the module uses a `Class.SurfaceGui` to display art items. To configure which surface the art appears on:

1. Select the **SurfaceCanvas** mesh.
2. At the bottom of the **Properties** window, locate the **SurfaceCanvasFace** attribute with a default value of **Right**.
3. Click the attribute and enter one of six values that describe a `Enum.NormalId`.

| Attribute Value | Corresponding Normal ID |
| --- | --- |
| **Front** | `Enum.NormalId.Front` |
| **Back** | `Enum.NormalId.Back` |
| **Right** | `Enum.NormalId.Right` |
| **Left** | `Enum.NormalId.Left` |
| **Top** | `Enum.NormalId.Top` |
| **Bottom** | `Enum.NormalId.Bottom` |

### Using Custom Art Assets

> **Info:** Currently, the surface art module only supports using the same set of assets for all tagged canvases.

To better fit the theme of your game, you may use your own set of custom assets instead of the defaults. This can be done via the [configure](#configure) function, called from a `Class.Script` in **ServerScriptService**.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SurfaceArt = require(ReplicatedStorage.SurfaceArt)

local customAssets = {
	CustomAsset1 = {
		name = "Custom Asset 1",
		assetId = "rbxassetid://7322508294",
	},
	CustomAsset2 = {
		name = "Custom Asset 2",
		assetId = "rbxassetid://7322547665",
	},
}

SurfaceArt.configure({
	assets = customAssets,
})
```

### Clearing All Canvases

To remove all existing art from all canvases in the world, call the [removeAllArt](#removeallart) function from a `Class.Script`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SurfaceArt = require(ReplicatedStorage.SurfaceArt)

SurfaceArt.removeAllArt()
```

### Showing Custom Effects

There may be cases where you'd like to include additional visual effects when an artwork is placed. This module exposes an event called [artChanged](#artchanged) on the client that you can connect to and add your own logic.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SurfaceArt = require(ReplicatedStorage.SurfaceArt)

local function createParticleEmitter(canvas, position)
	local attachment = Instance.new("Attachment")
	attachment.Position = canvas.CFrame:PointToObjectSpace(position)
	attachment.Axis = Vector3.new(0, 0, 1)
	attachment.SecondaryAxis = Vector3.new(1, 0, 0)
	attachment.Parent = canvas

	local particleEmitter = Instance.new("ParticleEmitter")
	particleEmitter.Speed = NumberRange.new(50)
	particleEmitter.Rate = 50
	particleEmitter.Color = ColorSequence.new(Color3.fromRGB(128, 254, 7))
	particleEmitter.SpreadAngle = Vector2.new(35, 35)
	particleEmitter.Parent = attachment

	return attachment
end

SurfaceArt.artChanged:Connect(function(canvas, spot, spotPosition, artId, ownerId)
	if artId then
		-- Show some sparkles for 3 seconds
		task.spawn(function()
			local emitterAttachment = createParticleEmitter(canvas, spotPosition)
			task.wait(3)
			emitterAttachment:Destroy()
		end)
	end
end)
```

## API Reference

### Types

#### SurfaceArtAsset

Images to be used as art for the canvas are represented by a table with two values.

| Key | Description |
| --- | --- |
| `name` | Metadata display name. |
| `assetId` | Asset ID of the image to include. |

### Functions

#### configure

_ configure(config: `Library.table`)_

Overrides default configuration options through the following keys/values in the `config` table. This function can only be called from a `Class.Script`.

#### General

| Key | Description | Default |
| --- | --- | --- |
| `enabled` | Toggles the module's functionality on or off. | true |
| `assets` | List of [SurfaceArtAsset](#surfaceartasset) types. | (see code below) |
| `quotaPerPlayer` | Maximum number of art pieces that can be placed by each player. | 2 |

#### Appearance

| Key | Description | Default |
| --- | --- | --- |
| `rowsPerCanvas` | Number of rows in the canvas grid. | 2 |
| `colsPerCanvas` | Number of columns in the canvas grid. | 5 |
| `itemsPerPage` | Number of items to skip when paging left and right. | 3 |
| `canvasPaddingLeft` | Left padding for the surface canvas (`Datatype.UDim`). | (0, 8) |
| `canvasPaddingRight` | Right padding for the surface canvas (`Datatype.UDim`). | (0, 8) |
| `canvasPaddingTop` | Top padding for the surface canvas (`Datatype.UDim`). | (0, 8) |
| `canvasPaddingBottom` | Bottom padding for the surface canvas (`Datatype.UDim`). | (0, 8) |
| `promptImage` | Icon shown in the proximity prompt to enter art selection view. | "rbxassetid://8076723774" |
| `leftArrowPageImage` | Image for the left arrow to flip to the previous page. | "rbxassetid://6998633654" |
| `leftArrowItemImage` | Image for the left arrow to select the previous art item. | "rbxassetid://8072765021" |
| `rightArrowPageImage` | Image for the right arrow to flip to the next page. | "rbxassetid://6998635824" |
| `rightArrowItemImage` | Image for the right arrow to select the next art item. | "rbxassetid://8072764852" |

#### Interaction

| Key | Description | Default |
| --- | --- | --- |
| `promptKeyCode` | Keyboard shortcut used to activate the prompt to enter art selection (`Enum.KeyCode`). | `Enum.KeyCode\|E` |
| `promptRequiresLineOfSight` | Boolean value that determines if the proximity prompt has to be in line of sight between user and canvas. | true |
| `promptMaxActivationDistance` | Maximum distance a player's character can be from the canvas for the prompt to appear. | 10 |
| `promptExclusivity` | `Enum.ProximityPromptExclusivity` specifying which prompts can be shown at the same time. | `Enum.ProximityPromptExclusivity\|OnePerButton` |
| `usePageHotkeys` | Whether page hotkeys are used. If true, `nextPageKey` and `prevPageKey` are used to cycle between pages. | true |
| `nextPageKey` | Key used to cycle to the next page of artwork (`Enum.KeyCode`). | `Enum.KeyCode\|E` |
| `nextItemKey` | Key used to cycle to the next item of artwork (`Enum.KeyCode`). | `Enum.KeyCode\|Right` |
| `prevPageKey` | Key used to cycle to the previous page of artwork (`Enum.KeyCode`). | `Enum.KeyCode\|Q` |
| `prevItemKey` | Key used to cycle to the previous item of artwork (`Enum.KeyCode`). | `Enum.KeyCode\|Left` |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SurfaceArt = require(ReplicatedStorage.SurfaceArt)

SurfaceArt.configure({
	quotaPerPlayer = 4,
	promptKeyCode = Enum.KeyCode.T,
	promptMaxActivationDistance = 8,
})
```

#### getCanvases

_ getCanvases(): `Library.table`_

Returns all of the canvases tagged with the `SurfaceCanvas` tag.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SurfaceArt = require(ReplicatedStorage.SurfaceArt)

local canvases = SurfaceArt.getCanvases()
```

#### placeArt

_ placeArt(player: `Class.Player`, canvas: `Class.BasePart`)_

Places an art piece programmatically on behalf of a player. Note that the `canvas` object must be tagged with the `SurfaceCanvas` tag when the server is initialized. It is recommended to use this only with a canvas returned from [getCanvases](#getcanvases).

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SurfaceArt = require(ReplicatedStorage.SurfaceArt)

local remoteEvent = ReplicatedStorage:WaitForChild("SurfaceArtRemoteEvent")

remoteEvent.OnServerEvent:Connect(function(player)
	-- Place the Bloxy Award from default art assets into the first canvas
	local canvases = SurfaceArt.getCanvases()
	SurfaceArt.placeArt(player, canvases[1], "BloxyAward")
end)
```

#### removeAllArt

_ removeAllArt()_

Removes all artwork from all surfaces.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SurfaceArt = require(ReplicatedStorage.SurfaceArt)

SurfaceArt.removeAllArt()
```

### Events

#### artChanged

Fires when an artwork is changed at a particular location on a canvas. When an artwork is removed, `artId` will be `nil`. Note that a `Datatype.Vector3` value is passed as the third parameter to the event handler so that you can position a [custom effect](#showing-custom-effects) at the exact position where the artwork is placed. This event can only be connected in a `Class.LocalScript`.

| Parameters |
| --- |
| canvas: `Class.BasePart` | Canvas upon which the artwork was changed. |
| spot: `Class.Frame` | Internal `Class.Frame` that contains the artwork `Class.ImageLabel`. |
| spotPosition: `Datatype.Vector3` | Exact position where the artwork was placed. |
| artId: `Library.string` | Asset ID of the new artwork. |
| ownerUserId: `number` | `Class.Player.UserId\|UserId` of the player who placed the art. |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SurfaceArt = require(ReplicatedStorage.SurfaceArt)

SurfaceArt.artChanged:Connect(function(canvas, spot, spotPosition, artId, ownerId)
	print("Art placed at:", spotPosition)
	print("Art asset ID:", artId)
	print("Art placed by:", ownerId)
end)
```

#### promptShown

Fires when a canvas interaction prompt is shown to a player. The connected function receives the canvas upon which the prompt is showing. This event can only be connected in a `Class.LocalScript`.

| Parameters |
| --- |
| canvas: `Class.BasePart` | Canvas upon which the prompt is showing. |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Players = game:GetService("Players")

local SurfaceArt = require(ReplicatedStorage.SurfaceArt)

SurfaceArt.promptShown:Connect(function(canvas)
	print(Players.LocalPlayer, canvas)
end)
```

#### promptHidden

Fires when a canvas interaction prompt is hidden. The connected function receives the canvas upon which the prompt was showing. This event can only be connected in a `Class.LocalScript`.

| Parameters |
| --- |
| canvas: `Class.BasePart` | Canvas upon which the prompt was showing. |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Players = game:GetService("Players")

local SurfaceArt = require(ReplicatedStorage.SurfaceArt)

SurfaceArt.promptClosed:Connect(function(canvas)
	print(Players.LocalPlayer, canvas)
end)
```

#### selectorShown

Fires when the surface art selector UI is shown to a player. This event can only be connected in a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Players = game:GetService("Players")

local SurfaceArt = require(ReplicatedStorage.SurfaceArt)

SurfaceArt.selectorShown:Connect(function()
	print(Players.LocalPlayer, "opened surface art selector")
end)
```

#### selectorHidden

Fires when the surface art selector UI is hidden for a player. This event can only be connected in a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Players = game:GetService("Players")

local SurfaceArt = require(ReplicatedStorage.SurfaceArt)

SurfaceArt.selectorHidden:Connect(function()
	print(Players.LocalPlayer, "closed surface art selector")
end)
```
