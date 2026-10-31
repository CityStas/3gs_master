---
title: "Selfie Mode"
url: /docs/en-us/resources/modules/selfie-mode
last_updated: 2026-10-30T19:55:55Z
description: "The Selfie Mode module lets players capture screenshots to commemorate fun moments."
---

# Selfie Mode

Players already take screenshots to commemorate fun moments in games. The **SelfieMode** [developer module](/docs/en-us/resources/modules.md) lets players capture a cleaner memory of that moment without the chat window or player list, while also supporting filter effects, hiding of other characters, and posing.

## Module Usage

### Installation

To use the **SelfieMode** module in a game:

1. From Studio's **Window** menu or **Home** tab toolbar, open the [Toolbox](/docs/en-us/projects/assets/toolbox.md) and select the **Creator Store** tab.
2. Make sure the **Models** sorting is selected, then click the **See All** button for **Categories**.
3. Locate and click the **Packages** tile.
4. Locate the **Selfie Mode** module and click it, or drag-and-drop it into the 3D view.
5. In the [Explorer](/docs/en-us/studio/explorer.md) window, move the entire **SelfieMode** package into `Class.ReplicatedStorage`. Upon running the game the module will begin running.

### Configuration

The module is preconfigured to work for most use cases, but you can easily customize it through the [configure](#configure) function.

1. In **StarterPlayerScripts**, create a new `Class.LocalScript` and rename it to **ConfigureSelfieMode**.
2. Paste the following code into the new script.```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

SelfieMode.configure({
	disableCharacterMovement = true
})
```

### Character Movement

It may be advantageous to prevent the player's character from moving while in selfie mode. You can achieve this by setting `disableCharacterMovement` to true in a [configure](#configure) call.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

SelfieMode.configure({
	disableCharacterMovement = true
})
```

### Selfie Mode Actions

**SelfieMode** comes with the following [actions](#action), each of which you can use with the [activateAction](#activateaction), [deactivateAction](#deactivateaction), and [toggleAction](#toggleaction) functions, or detect through the [actionActivated](#actionactivated) and [actionDeactivated](#actiondeactivated) events.

#### Depth-of-Field

By default, **SelfieMode** shows a generic **depth‑of‑field** effect (subtle blur of the background) when a player toggles the action.

#### Off

#### On

> **Warning:** This effect does not render on mobile devices such as phones and tablets. As such, it will not be offered as an action on those devices.
>
> On non-mobile devices, the player's graphics quality must be eight or higher to render depth‑of‑field. If their graphics quality is less than eight, they'll be prompted to increase it.

To change the default depth‑of‑field effect, set `depthOfFieldEffect` to your own `Class.DepthOfFieldEffect` instance in a [configure](#configure) call.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

local customDepthOfField = Instance.new("DepthOfFieldEffect")
customDepthOfField.NearIntensity = 0
customDepthOfField.FarIntensity = 1
customDepthOfField.FocusDistance = 5
customDepthOfField.InFocusRadius = 5

SelfieMode.configure({
	depthOfFieldEffect = customDepthOfField
})
```

#### Lock Gaze

The **Lock Gaze** toggle causes the player's character to look at the camera while setting up the selfie pose, within a realistic range of how far their neck can turn.

#### Hide Others

By default, other characters are visible alongside the player's character. Players can obtain a perfect solo shot by clicking the **Hide Others** button. When toggled on, other characters fade out of view and remain invisible until the action is toggled off.

#### Filter

The **Filter** action lets the player apply a preset filter from the options **Pop**, **Soft**, **Antique**, **Cute**, **Dramatic**, and **Monochrome**.

#### Soft

#### Dramatic

#### Monochrome

#### Pose

The **Pose** action lets the player select a preset pose from the options **Cheer**, **Clapping**, **Dolphin**, **Flossing**, **Guitar**, **Jump Wave**, **Louder**, **Top Rock**, **Twirl**, and **Wave**.

#### Flossing

#### Louder

#### Twirl

## API Reference

### Types

#### Action

Each action is represented by a dictionary with the following key-value pairs:

| Key | Type | Description |
| --- | --- | --- |
| `name` | string | Name of the action, shown first in tooltips. |
| `description` | string | Description of the action, shown after **name** in tooltips. |
| `icon` | string | Asset ID for the action's icon. |
| `activeIcon` | string | Asset ID for the action's icon in "active" state. Can only be used on parent actions, not sub-actions. |
| `actions` | table | Optional list of sub-actions. This allows you to create submenus of various other actions. |
| `parent` | [Action](#action) | The parent of the action; this only applies to a sub-action and points to the action that contains it. |
| `onActivated` | function | Optional callback function that runs when a player activates an action or sub-action. Typically, if an action contains sub-actions, only the sub-actions will need a callback defined as a means of knowing that the player activated the sub-action and did not simply "expand" the parent action. |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

SelfieMode.actionActivated:Connect(function(action)
	print(action.name, "activated")
end)

SelfieMode.actionDeactivated:Connect(function(action)
	print(action.name, "deactivated")
end)
```

### Enums

#### SelfieMode.Action

**SelfieMode** comes with several [actions](#action). You can use this enum with the [activateAction](#activateaction), [deactivateAction](#deactivateaction), and [toggleAction](#toggleaction) functions.

| Name | Summary |
| --- | --- |
| `DepthOfField` | Reference to the [Depth‑of‑Field](#depth-of-field) action. |
| `LockGaze` | Reference to the [Lock Gaze](#lock-gaze) action. |
| `HideOthers` | Reference to the [Hide Others](#hide-others) action. |
| `Filter` | Reference to the [Filter](#filter) action. |
| `Pose` | Reference to the [Pose](#pose) action. |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

-- Activate "Filter" action
SelfieMode.activateAction(SelfieMode.Action.Filter)
```

### Functions

#### configure

_ configure(config: `Library.table`)_

Overrides default configuration options through the following keys/values in the `config` table. This function can only be called from a `Class.LocalScript`.

| Key | Description | Default |
| --- | --- | --- |
| `disableCharacterMovement` | If true, prevents character from moving while selfie mode is open. | false |
| `depthOfFieldEffect` | Optional custom `Class.DepthOfFieldEffect` instance that appears when the player toggles the [Depth of Field](#depth-of-field) action. | |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

SelfieMode.configure({
	disableCharacterMovement = true
})
```

#### openSelfieMode

_ openSelfieMode()_

A player will typically open selfie mode with the "camera" button on the right side of the screen, but this function lets you open it through code. When implementing a custom button as shown below, you should disable the default button through [setHudButtonEnabled](#sethudbuttonenabled). This function can only be called from a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

local button = script.Parent

-- Remove the default button
SelfieMode.setHudButtonEnabled(false)

-- Connect the custom button
button.Activated:Connect(function()
	SelfieMode.openSelfieMode()
end)
```

#### closeSelfieMode

_ closeSelfieMode()_

A player will typically close selfie mode with the **⊗** button at the bottom of the screen, but this function lets you close it through code. Can only be called from a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

SelfieMode.closeSelfieMode()
```

#### isSelfieModeOpen

_ isSelfieModeOpen(): `boolean`_

Returns `true` if selfie mode is open as a result of player action or through [openSelfieMode](#openselfiemode). This function can only be called from a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

SelfieMode.openSelfieMode()

print(SelfieMode.isSelfieModeOpen())
```

#### setHudButtonEnabled

_ setHudButtonEnabled()_

Sets whether the default button to enter selfie mode is shown. Useful when implementing [openSelfieMode](#openselfiemode) through a custom UI button. This function can only be called from a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

local button = script.Parent

-- Remove the default button
SelfieMode.setHudButtonEnabled(false)

-- Connect the custom button
button.Activated:Connect(function()
	SelfieMode.openSelfieMode()
end)
```

#### getAction

_ getAction(action: [SelfieMode.Action](#selfiemodeaction)): [Action](#action)_

Gets an [Action](#action) type through a [SelfieMode.Action](#selfiemodeaction) enum.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

local lockGazeAction = SelfieMode.getAction(SelfieMode.Action.LockGaze)
```

#### activateAction

_ activateAction(action: [SelfieMode.Action](#action))_

Programmatically activates one of the default [actions](#selfie-mode-actions). This is the same as when a player toggles the action on from the action bar. Can only be called from a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

-- Activate "Filter" action
SelfieMode.activateAction(SelfieMode.Action.Filter)
```

#### deactivateAction

_ deactivateAction(action: [SelfieMode.Action](#action))_

Programmatically deactivates one of the default [actions](#selfie-mode-actions). This is the same as when a player toggles the action off from the action bar. Can only be called from a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

-- Deactivate "Filter" action
SelfieMode.deactivateAction(SelfieMode.Action.Filter)
```

#### toggleAction

_ toggleAction(action: [SelfieMode.Action](#action)): `boolean`_

Toggles an [action](#selfie-mode-actions) on if it's off, or toggles it off if it's on. This is the same as when a player clicks the action from the action bar. Returns the new "is toggled on" state as a boolean. Can only be called from a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

local lockGazeAction = SelfieMode.getAction(SelfieMode.Action.LockGaze)

local isEnabled = SelfieMode.toggleAction(lockGazeAction)

if isEnabled then
	print("Activated", lockGazeAction.name)
else
	print("Deactivated", lockGazeAction.name)
end
```

#### setTheme

_ setTheme(theme: `Library.table`)_

Configures the selfie mode theme, including text size, font, button/tooltip colors, and more. This function can only be called from a `Class.LocalScript`.

#### General

| Key | Description | Default |
| --- | --- | --- |
| `textSize` | Size of all text. | 16 |
| `font` | Font used across all UI (`Enum.Font`). | `Enum.Font\|GothamMedium` |
| `padding` | Main padding used for laying out UI elements (`Datatype.UDim`). | (0, 12) |
| `paddingSmall` | Smaller padding used for applying subtle margins between elements (`Datatype.UDim`). | (0, 6) |
| `paddingScreen` | Padding used around the screen edges to give selfie mode some breathing room (`Datatype.UDim`). | (0, 24) |
| `backgroundColor` | Background color used for the bar that displays the actions (`Datatype.Color3`). | [0, 0, 0] |
| `scrollBarColor` | Color of the scrollbar used in `Class.ScrollingFrame` elements of the module (`Datatype.Color3`). | [255, 255, 255] |

#### Buttons and Tooltips

| Key | Description | Default |
| --- | --- | --- |
| `openButtonBackgroundColor` | Background color of the HUD button on the right side of the screen used to open selfie mode (`Datatype.Color3`). | [255, 255, 255] |
| `openButtonIconColor` | Color of the HUD button's camera icon (`Datatype.Color3`). | [0, 0, 0] |
| `closeButtonBackgroundColor` | Background color of the "close" button (`Datatype.Color3`). | [0, 0, 0] |
| `closeButtonIconColor` | Icon color for the "close" button (`Datatype.Color3`). | [255, 255, 255] |
| `actionButtonBackgroundColor` | Background color of the various action buttons used for toggling actions (`Datatype.Color3`). | [255, 255, 255] |
| `actionButtonIconColor` | Icon color for the various action buttons (`Datatype.Color3`). | [0, 0, 0] |
| `tooltipBackgroundColor` | Background color of tooltips and notifications (`Datatype.Color3`). | [0, 0, 0] |
| `tooltipNameColor` | Text color of tooltip names (`Datatype.Color3`). Also used as the text color for notifications. | [255, 255, 255] |
| `tooltipDescriptionColor` | Color of tooltip descriptions, slightly faded to give focus to tooltip names (`Datatype.Color3`). Not used for notifications. | [169, 169, 169] |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

SelfieMode.setTheme({
	textSize = 20,
	font = Enum.Font.Michroma,
	backgroundColor = Color3.fromRGB(0, 40, 75),
})
```

#### setEnabled

_ setEnabled(isEnabled: `boolean`)_

Sets whether selfie mode is enabled or not. When disabled, all UI for the module is removed and all events are disconnected. This function can only be called from a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

SelfieMode.setEnabled(false)
```

### Events

#### selfieModeOpened

Fires when the player opens selfie mode or when [openSelfieMode](#openselfiemode) is called. This event can only be connected in a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

SelfieMode.selfieModeOpened:Connect(function()
	print("Selfie mode open")
end)
```

#### selfieModeClosed

Fires when the player closes selfie mode or when [closeSelfieMode](#closeselfiemode) is called. This event can only be connected in a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

SelfieMode.selfieModeClosed:Connect(function()
	print("Selfie mode closed")
end)
```

#### actionActivated

| Parameters |
| --- |
| action: [SelfieMode.Action](#action) | The activated [Action](#action). |

Fires when an action is activated; this may be one of the primary actions like [Depth of Field](#depth-of-field), [Lock Gaze](#lock-gaze), or [Hide Others](#hide-others); alternatively it may be a sub-action like a [filter](#filter) or [pose](#pose). The connected function receives the activated [Action](#action). This event can only be connected in a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

SelfieMode.actionActivated:Connect(function(action)
	print(action.name, "activated")
end)
```

#### actionDeactivated

| Parameters |
| --- |
| action: [SelfieMode.Action](#action) | The deactivated [Action](#action). |

Fires when a primary action or sub-action is deactivated. The connected function receives the deactivated [Action](#action). This event can only be connected in a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

SelfieMode.actionDeactivated:Connect(function(action)
	print(action.name, "deactivated")
end)
```

#### filterChanged

| Parameters |
| --- |
| newFilter: `Library.string` | The new filter. |
| oldFilter: `Library.string` | The previous filter. |

Fires when a [filter](#filter) is applied or removed. The connected function receives the new filter name and the old filter name. This event can only be connected in a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

SelfieMode.filterChanged:Connect(function(newFilter, oldFilter)
	print("Filter changed from", oldFilter, "to", newFilter)
end)
```

#### poseChanged

| Parameters |
| --- |
| newPose: `Library.string` | The new pose. |
| oldPose: `Library.string` | The previous pose. |

Fires when a [pose](#pose) is applied or removed. The connected function receives the new pose name and the old pose name. This event can only be connected in a `Class.LocalScript`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SelfieMode = require(ReplicatedStorage.SelfieMode)

SelfieMode.poseChanged:Connect(function(newPose, oldPose)
	print("Pose changed from", oldPose, "to", newPose)
end)
```
