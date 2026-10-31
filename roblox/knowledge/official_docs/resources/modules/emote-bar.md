---
title: "Emote Bar"
url: /docs/en-us/resources/modules/emote-bar
last_updated: 2026-10-30T19:55:55Z
description: "The Emote Bar module aims to provide players an accessible, customizable way to socially interact."
---

# Emote Bar

Emotes are a core component of any social game. The **EmoteBar** [developer module](/docs/en-us/resources/modules.md) aims to provide players an accessible, customizable way to facilitate meaningful social interaction.

## Module usage

### Installation

To use the **EmoteBar** module in a game:

1. From Studio's **Window** menu or **Home** tab toolbar, open the [Toolbox](/docs/en-us/projects/assets/toolbox.md) and select the **Creator Store** tab.
2. Make sure the **Models** sorting is selected, then click the **See All** button for **Categories**.
3. Locate and click the **Packages** tile.
4. Locate the **Emote Bar** module and click it, or drag-and-drop it into the 3D view.
5. In the [Explorer](/docs/en-us/studio/explorer.md) window, move the entire **EmoteBar** model into `Class.ReplicatedStorage`. Upon running the game the module will begin running.

### Configuration

The module is preconfigured with 7 emotes and it can be easily customized with your own emotes and display options. Additionally, if the player owns any emotes from previous Roblox events such as Lil Nas X, Royal Blood, or Twenty One Pilots, those emotes will be automatically added to the list of available emotes.

1. In **ServerScriptService**, create a new `Class.Script` and rename it **ConfigureEmotes**.
2. Paste the following code into the new **ConfigureEmotes** script. The `useDefaultEmotes` setting of `false` overrides the default emotes and lets you define custom emotes via the [setEmotes](#setemotes) function.```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local EmoteBar = require(ReplicatedStorage.EmoteBar)

EmoteBar.configureServer({
	useDefaultEmotes = false,
})

EmoteBar.setEmotes({
	{
		name = "Hello",
		animation = "rbxassetid://3344650532",
		image = "rbxassetid://7719817462",
		defaultTempo = 1,
	},
	{
		name = "Applaud",
		animation = "rbxassetid://5915693819",
		image = "rbxassetid://7720292217",
		defaultTempo = 2,
	},
})
```

> **Info:** If you want to disable loading of user-owned emotes into the emote bar or wheel, make sure the **UserEmotesEnabled** property is disabled for the **StarterPlayer** object. Note that this property can only be set in Studio and cannot be set by scripts at runtime.
>
> Also note that this developer module will modify the local user's emotes via `Class.HumanoidDescription:SetEmotes()`, meaning that calls to `Class.HumanoidDescription:GetEmotes()` will return values modified by this module.
### Mega emotes

A **mega emote** is formed when multiple players in the same area perform the same emote at the same time. As more and more players join in, the mega emote grows larger. As players stop performing the emote, the mega emote grows smaller until eventually it disappears.

### Tempo

An emote's **tempo** is the speed at which it plays when its button is tapped once. The default speed of an emote is determined by its `defaultTempo`. An emote's speed can be increased or decreased by tapping its button faster or slower.

## API reference

### Types

#### Emote

Each emote is represented by a dictionary with the following key-value pairs:

| Key | Type | Description |
| --- | --- | --- |
| `name` | string | Emote name, for example `"Shrug"`. |
| `animation` | string | Asset ID for the emote's animation. |
| `image` | string | Asset ID for the emote's image in the GUI. |
| `defaultTempo` | number | Default speed factor at which to play the emote animation. For example, a tempo of 2 will play the animation at twice its normal speed. Must be greater than 0. |
| `isLocked` | bool | Whether the emote is "locked" from being activated. |

### Enums

#### EmoteBar.GuiType

| Name | Summary |
| --- | --- |
| `EmoteBar` | Default form where emotes are displayed in a bar along the bottom of the screen, separated into individual "pages." |
| `EmoteWheel` | Variant where emotes are displayed in a ring when a player clicks or taps on their player character. |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local EmoteBar = require(ReplicatedStorage.EmoteBar)

EmoteBar.configureClient({
	guiType = EmoteBar.GuiType.EmoteWheel,
})
```

### Functions

#### configureServer

_ configureServer(config: `Library.table`)_

Overrides default server-side configuration options through the following keys/values in the `config` table. This function can only be called from a `Class.Script` and changes will automatically replicate to all clients.

| Key | Description | Default |
| --- | --- | --- |
| `useDefaultEmotes` | Whether the provided default emotes are included or not. | true |
| `useMegaEmotes` | Enables or disables the [mega emotes](#mega-emotes) feature. | true |
| `emoteMinPlayers` | Minimum number of players performing the same emote to contribute to a mega emote. | 3 |
| `emoteMaxPlayers` | Maximum number of players performing the same emote to contribute to a mega emote. | 50 |
| `playParticles` | Enables or disables the emotes players are playing as floating particles above their heads. | true |
| `sendContributingEmotes` | Enables or disables sending a small emote icon to contribute to the mega emote. | true |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local EmoteBar = require(ReplicatedStorage.EmoteBar)

EmoteBar.configureServer({
	emoteMinPlayers = 2,
	playParticles = false,
})
```

#### configureClient

_ configureClient(config: `Library.table`)_

Overrides default client-side configuration options through the following keys/values in the `config` table. This function can only be called from a `Class.LocalScript`. Depending on the value of `guiType`, options in the noted tabs also apply.

#### General

| Key | Description | Default |
| --- | --- | --- |
| `guiType` | Controls which form the GUI will take for displaying emotes ([EmoteBar.GuiType](#emotebarguitype)). | [EmoteBar](#emotebarguitype) |
| `useTempo` | Enables or disables the [tempo](#tempo) feature where users are able to control how fast or slow their emotes are played by repeatedly activating the same emote rhythmically. | true |
| `tempoActivationWindow` | Amount of time, in seconds, the user has between sequential activations of an emote for it to count as part of the tempo. | 3 |
| `lockedImage` | Image to display overtop locked emotes. | "rbxassetid://6905802778" |

#### Bar

If the value of `guiType` is [EmoteBar](#emotebarguitype) (default), the following options apply:

| Key | Description | Default |
| --- | --- | --- |
| `maxEmotesPerPage` | Maximum number of emotes that are displayed at a time. Smaller screens will automatically show fewer emotes. | 4 |
| `emoteBarPosLandscape` | Position of the emote bar in landscape mode (`Datatype.UDim2`). | (0.5, 0, 1, -16) |
| `emoteBarPosPortrait` | Position of the emote bar in portrait mode (`Datatype.UDim2`). | (0.5, 0, 1, -100) |
| `useEmoteHotkeys` | Whether emote hotkeys are used. If `true`, this binds 1, 2, 3, 4, etc. as hotkeys for the emote bar. Only numeric keys 1–9 are supported. | true |
| `usePageHotkeys` | Whether page hotkeys are used. If `true`, `nextPageKey` and `prevPageKey` are used to cycle between pages. | true |
| `prevPageKey` | Key used to cycle to the previous page of emotes (`Enum.KeyCode`). | `Enum.KeyCode\|Q` |
| `nextPageKey` | Key used to cycle to the next page of emotes (`Enum.KeyCode`). | `Enum.KeyCode\|E` |
| `leftArrowImage` | Image for the left arrow (previous page). | "rbxassetid://6998633654" |
| `rightArrowImage` | Image for the right arrow (next page). | "rbxassetid://6998635824" |

#### Wheel

If the value of `guiType` is [EmoteWheel](#emotebarguitype), the following options apply:

| Key | Description | Default |
| --- | --- | --- |
| `closeImage` | Image for the close button on the emote wheel, placed overtop the `closeBackgroundImage` image. | "rbxassetid://7027440823" |
| `closeBackgroundImage` | Background image for the close button on the emote wheel. | "rbxassetid://7027440823" |
| `emoteHoverImage` | Image for hover-over indication of the selected emote in the wheel. | "rbxassetid://7344843157" |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local EmoteBar = require(ReplicatedStorage.EmoteBar)

EmoteBar.configureClient({
	guiType = EmoteBar.GuiType.EmoteBar,
	maxEmotesPerPage = 6,
	nextPageKey = Enum.KeyCode.Z,
	prevPageKey = Enum.KeyCode.C,
})
```

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local EmoteBar = require(ReplicatedStorage.EmoteBar)

EmoteBar.configureClient({
	guiType = EmoteBar.GuiType.EmoteWheel,
})
```

#### setEmotes

_ setEmotes(emotes: `Library.table`)_

Sets the custom emotes to use. These will be added to the defaults if `useDefaultEmotes` is `true`, or replace the defaults if `useDefaultEmotes` is `false`. This function can only be called from a `Class.Script` and changes will automatically replicate to all clients.

See [Emote](#emote) for the structure of each emote passed to this function.

> **Info:** The order of custom emotes in the array determines how each emote is ordered in the UI.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local EmoteBar = require(ReplicatedStorage.EmoteBar)

EmoteBar.configureServer({
	useDefaultEmotes = false,
})

EmoteBar.setEmotes({
	{
		name = "Hello",
		animation = "rbxassetid://3344650532",
		image = "rbxassetid://7719817462",
		defaultTempo = 1,
	},
	{
		name = "Applaud",
		animation = "rbxassetid://5915693819",
		image = "rbxassetid://7720292217",
		defaultTempo = 2,
	},
})
```

#### setGuiVisibility

_ setGuiVisibility(visible: `boolean`)_

Shows or hides the emotes GUI. This function can only be called from a `Class.LocalScript` on a specific client.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local EmoteBar = require(ReplicatedStorage.EmoteBar)

EmoteBar.setGuiVisibility(false)
```

#### getEmote

_ getEmote(emoteName: `Library.string`): `Library.table`_

Gets an [Emote](#emote) by name. Returns `nil` if the emote cannot be found. This function can only be called from a `Class.LocalScript` on a specific client.

> **Info:** Emotes registered on the server with [setEmotes](#setemotes) can be retrieved client-side using this function. This can also be used to retrieve any of the default emotes by name: `"Hello"`, `"Applaud"`, `"Point"`, `"Stadium"`, `"Tilt"`, `"Shrug"`, or `"Salute"`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local EmoteBar = require(ReplicatedStorage.EmoteBar)

local shrug = EmoteBar.getEmote("Shrug")
```

#### playEmote

_ playEmote(emote: [Emote](#emote))_

Plays the given [Emote](#emote) and fires the [emotePlayed](#emoteplayed) event on the server, if connected. This function can only be called from a `Class.LocalScript` on a specific client.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local EmoteBar = require(ReplicatedStorage.EmoteBar)

local shrug = EmoteBar.getEmote("Shrug")
EmoteBar.playEmote(shrug)
```

#### lockEmote

_ lockEmote(emoteName: `Library.string`)_

Locks the [Emote](#emote) with the given name. This function can only be called from a `Class.LocalScript` on the client.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local EmoteBar = require(ReplicatedStorage.EmoteBar)

EmoteBar.lockEmote("Applaud")
```

#### unlockEmote

_ unlockEmote(emoteName: `Library.string`)_

Unlocks the [Emote](#emote) with the given name. This function can only be called from a `Class.LocalScript` on the client.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local EmoteBar = require(ReplicatedStorage.EmoteBar)

EmoteBar.unlockEmote("Applaud")
```

### Events

#### emotePlayed

Fires when any client plays an emote. This event can only be connected in a `Class.LocalScript`.

| Parameters |
| --- |
| player: `Class.Player` | Player who acted out the emote. |
| emote: [Emote](#emote) | Emote which was played. |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local EmoteBar = require(ReplicatedStorage.EmoteBar)

EmoteBar.emotePlayed:Connect(function(player, emote)
	print(player.Name, "played", emote.name)
end)
```

#### lockedEmoteActivated

Fires when a client clicks a locked emote. This event can only be connected in a `Class.LocalScript`.

| Parameters |
| --- |
| emote: [Emote](#emote) | Locked emote which was activated. |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Players = game:GetService("Players")

local EmoteBar = require(ReplicatedStorage.EmoteBar)

EmoteBar.lockedEmoteActivated:Connect(function(emote)
	print(Players.LocalPlayer, "clicked", emote.name)
end)
```
