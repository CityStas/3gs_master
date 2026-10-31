---
name: TeleportService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "Enables transporting Players between places and servers. For more information on how to teleport players between servers, see [Teleport between places](/docs/en-us/projects/teleport.md)."
---

# Class: TeleportService

> Enables transporting [Players](/docs/reference/engine/classes/Player.md) between places and servers. For
> more information on how to teleport players between servers, see
> [Teleport between places](/docs/en-us/projects/teleport.md).

## Description

**TeleportService** is responsible for transporting [Players](/docs/reference/engine/classes/Player.md)
between different places and servers.

For more information on how to teleport players between servers, see
[Teleport between places](/docs/en-us/projects/teleport.md).

## Properties

### Property: TeleportService.CustomizedTeleportUI

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Teleport"
  ]
}
```

> **Deprecated:** This item is deprecated since the default message it controls has been removed. Do not use it for new work.

This property used to control whether or not a [Message](/docs/reference/engine/classes/Message.md) would be
shown by default. The default message has been removed, so this no longer
does anything.

## Methods

### Method: TeleportService:GetArrivingTeleportGui

**Signature:** `TeleportService:GetArrivingTeleportGui(): Instance`

This function returns the _customLoadingScreen_ the
[LocalPlayer](/docs/reference/engine/classes/Players.md) arrived into the place with.

Note, the _customLoadingScreen_ will not be used if the destination place
is in a different game.

#### Loading Screen

During a teleport, while the destination place is loading, the
_customLoadingScreen_ is parented to the [CoreGui](/docs/reference/engine/classes/CoreGui.md). Once the place
has loaded the [loading screen](/docs/reference/engine/classes/ScreenGui.md) is
[parented](/docs/reference/engine/classes/Instance.md) to _nil_.

If you wish to preserve the _customLoadingScreen_ and perform your own
transitions, you will need to parent it to the local player's
[PlayerGui](/docs/reference/engine/classes/PlayerGui.md). For an example of this, see the code sample below.

#### Studio Limitation

Note that this service does not work during playtesting in Roblox Studio;
to test aspects of your experience using it, you must publish the
experience and play it in the Roblox application.

*Security: None · Thread Safety: Unsafe · Capabilities: UI, Teleport*

**Returns:** `Instance` — The _customLoadingScreen_ the [LocalPlayer](/docs/reference/engine/classes/Players.md)
arrived into the place with.

**Handling a Teleport Loading GUI**

The following code, when placed inside a `LocalScript` in `ReplicatedFirst`
will preserve a custom teleport loading screen for five seconds before
destroying it.

```lua
local TeleportService = game:GetService("TeleportService")
local Players = game:GetService("Players")
local ReplicatedFirst = game:GetService("ReplicatedFirst")

local customLoadingScreen = TeleportService:GetArrivingTeleportGui()
if customLoadingScreen then
	local playerGui = Players.LocalPlayer:WaitForChild("PlayerGui")
	ReplicatedFirst:RemoveDefaultLoadingScreen()
	customLoadingScreen.Parent = playerGui
	task.wait(5)
	customLoadingScreen:Destroy()
end
```

### Method: TeleportService:GetLocalPlayerTeleportData

**Signature:** `TeleportService:GetLocalPlayerTeleportData(): Variant`

This function returns the teleport data the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md)
arrived with. It can only be called from the client.

Exploiters can spoof teleport data. Send secure data such as player
currency through a server-side service such as [DataStoreService](/docs/reference/engine/classes/DataStoreService.md) to
prevent tampering.

*Security: None · Thread Safety: Unsafe · Capabilities: Teleport*

**Returns:** `Variant` — The teleport data the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md) arrived into the
place with.

**Getting LocalPlayer Teleport Data**

When put into StarterPlayerScripts, this example runs when the player joins
the game, and prints any teleport data provided by the player's previous
server.

```lua
local TeleportService = game:GetService("TeleportService")

local teleportData = TeleportService:GetLocalPlayerTeleportData()

print("Local player arrived with this data:", teleportData)
```

**Expected output:** Local player arrived with this data: nil

### Method: TeleportService:GetPlayerPlaceInstanceAsync

**Signature:** `TeleportService:GetPlayerPlaceInstanceAsync(userId: User): Tuple`

This function returns the [PlaceId](/docs/reference/engine/classes/DataModel.md) and
[JobId](/docs/reference/engine/classes/DataModel.md) of the server the user with the given
[UserId](/docs/reference/engine/classes/Player.md) is in, provided it is in the same game as the
current place.

Then, [TeleportService:TeleportToPlaceInstance()](/docs/reference/engine/classes/TeleportService.md) can be called with
this information to allow a user to join the target user's server.

Upon a successful lookup, the function returns the following values:

| # | Name | Type | Description |
| --- | --- | --- | --- |
| **1** | currentInstance | bool | A bool indicating if the user was found in the current instance |
| **2** | error | string | An error message in the event of the lookup failing |
| **3** | placeId | int64 | The PlaceId of the server the user is in |
| **4** | instanceId | string | The JobId of the server the user is in |

If there is a problem during lookup, such as the user being offline, an
error is thrown. It is recommended that you wrap calls to this function in
`pcall`.

#### Limitations

You should be aware of the following limitations when using this function:

- This function can only be called by the server.
- This function may fail to return the correct information if the user is
  teleporting.
- It is possible for this function to throw an error, hence developers
  should wrap it in a [LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md) (see example below)
- As this function returns the JobId of the server and not the access code
  returned by [TeleportService:ReserveServerAsync()](/docs/reference/engine/classes/TeleportService.md), the ID
  returned is not appropriate for use with reserved servers.

#### Studio Limitation

Note that this service does not work during playtesting in Roblox Studio;
to test aspects of your experience using it, you must publish the
experience and play it in the Roblox application.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Teleport*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the [Player](/docs/reference/engine/classes/Player.md). |

**Returns:** `Tuple` — See the table above.

**Following Another Player**

The code sample below, when placed inside a `Script` within
`ServerScriptService`, will teleport a player who's following another player
to the associated place/server. Note that this will not work if the player
being followed is in a reserved server.

```lua
local TeleportService = game:GetService("TeleportService")
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	local followId = player.FollowUserId

	if followId and followId ~= 0 then
		-- Is this player following anyone? If so, find out where they are
		local success, currentInstance, error, placeId, jobIdOrErr = pcall(function()
			return TeleportService:GetPlayerPlaceInstanceAsync(followId)
		end)
			-- followId is the user ID of the player that you want to retrieve the place and job ID for
		if success then
			-- Teleports player on success based off jobId
			TeleportService:TeleportToPlaceInstance(placeId, jobIdOrErr, player)
		else
			-- Posts a warning based off returning error
			warn(jobIdOrErr)
		end
	else
		warn(("Player %d is not following another player!"):format(player.UserId))
	end
end)
```

### Method: TeleportService:GetTeleportSetting

**Signature:** `TeleportService:GetTeleportSetting(setting: string): Variant`

This function retrieves a teleport setting saved using
[TeleportService:SetTeleportSetting()](/docs/reference/engine/classes/TeleportService.md) using the given key.

This method is intended for use on the client only and should not be used
on the server.

Teleport settings are preserved across teleportations within the same
game. This means data can be saved using
[TeleportService:SetTeleportSetting()](/docs/reference/engine/classes/TeleportService.md) in one place and retrieved
using GetTeleportSetting in another place the user has been teleported to.

For example, in a game that allowed crouching you could save whether the
user is currently crouching prior to teleporting as a teleport setting.
This could then be retrieved in the destination place after the
teleportation:

```lua
local TeleportService = game:GetService("TeleportService")

local isCrouching = TeleportService:GetTeleportSetting("isCrouching")
```

If no teleport setting exists under the given key, this function will
return _nil_.

#### Differences from GlobalDataStores

Although they share some similarities, there are some key differences
between teleport settings and datastores:

- [GlobalDataStore:SetAsync()](/docs/reference/engine/classes/GlobalDataStore.md) stores the data on Roblox servers
  whereas SetTeleportSetting stores the data locally
- Data stored in a [GlobalDataStore](/docs/reference/engine/classes/GlobalDataStore.md) is preserved after the user
  leaves the game universe whereas teleport settings are not
- [GlobalDataStores](/docs/reference/engine/classes/GlobalDataStore.md) can only be accessed on the
  server, whereas teleport settings can only be accessed on the client
- [GlobalDataStores](/docs/reference/engine/classes/GlobalDataStore.md) have usage limits, whereas
  teleport settings do not

In general teleport settings should be used to preserve client side
information within a single play session across different places in a
game. [GlobalDataStores](/docs/reference/engine/classes/GlobalDataStore.md) should be used to save
important player data that needs to be accessed across player sessions.

#### Teleport settings and security

As teleport settings are stored locally, it is possible they can be
manipulated by malicious users. This risk can be mitigated by employing
server side validation.

#### Studio Limitation

Note that this service does not work during playtesting in Roblox Studio;
to test aspects of your experience using it, you must publish the
experience and play it in the Roblox application.

*Security: None · Thread Safety: Unsafe · Capabilities: Teleport*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `setting` | `string` |  | The key the value was stored under using [TeleportService:SetTeleportSetting()](/docs/reference/engine/classes/TeleportService.md). |

**Returns:** `Variant` — The value stored under the given key.

### Method: TeleportService:PromptExperienceDetailsAsync

**Signature:** `TeleportService:PromptExperienceDetailsAsync(player: Player, universeId: int64): PromptExperienceDetailsResult`

Prompts the specified [Player](/docs/reference/engine/classes/Player.md) with information of the specified
experience. The prompt includes the experience name, creator name,
maturity rating, etc. The prompt also includes a **Join** button which the
player can use to be teleported to the target experience. If the player is
ineligible to join the target experience, the button will be disabled.

Any teleport failures after the player clicks the **Join** button will
also fire [TeleportService.TeleportInitFailed](/docs/reference/engine/classes/TeleportService.md) providing a reason
for the failure.

#### Limitations

- For security purposes, teleporting a user from your experience to
  another experience owned by others fails by default. See
  [here](/docs/en-us/projects/teleport.md#enable-cross-experience-teleportation)
  for steps to enable cross-experience teleportation.
- This function currently can only be called from the client with
  [Players.LocalPlayer](/docs/reference/engine/classes/Players.md) as the `player` parameter.
- The join button will always be disabled during Studio playtesting; to
  test aspects of your experience using it, you must publish the
  experience and play it in the Roblox application.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Teleport*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) to be presented the prompt. |
| `universeId` | `int64` |  | [DataModel.UniverseId](/docs/reference/engine/classes/DataModel.md) of the experience to be presented to the [Player](/docs/reference/engine/classes/Player.md). |

**Returns:** `PromptExperienceDetailsResult` — [PromptExperienceDetailsResult](/docs/reference/engine/enums/PromptExperienceDetailsResult.md)

**Show Experience Details to Player**

The code sample below, when placed inside a `Script` with Client RunContext,
will display a system dialog to the player showing details about a specified
experience. Player can choose to teleport to the experience or close the
dialog.

```lua
local TeleportService = game:GetService("TeleportService")
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local success, result = pcall(function()
	TeleportService:PromptExperienceDetailsAsync(player, 8357232245)
end)
if not success then
	warn("Error prompting experience details: " .. tostring(result))
end

if result == Enum.PromptExperienceDetailsResult.PromptClosed then
	print("Player closed the experience details prompt")
elseif result == Enum.PromptExperienceDetailsResult.TeleportAttempted then
	print("Player chose to teleport to the experience")
end
```

### Method: TeleportService:ReserveServerAsync

**Signature:** `TeleportService:ReserveServerAsync(placeId: int64): Tuple`

This function is deprecated and no longer supported. It remains available
for backward compatibility but should not be used for new work. It can
only be called on the server.

For new work, generate a GUID with [HttpService:GenerateGUID()](/docs/reference/engine/classes/HttpService.md), set
[TeleportOptions.ReservedServerId](/docs/reference/engine/classes/TeleportOptions.md), and call
[TeleportService:TeleportAsync()](/docs/reference/engine/classes/TeleportService.md).

You can see if the current server is a reserved server by using the
following code:

```lua
local isReserved = game.PrivateServerId ~= "" and game.PrivateServerOwnerId == 0
```

The [DataModel.PrivateServerId](/docs/reference/engine/classes/DataModel.md) is constant across all server
instances associated with the server access code, the
[DataModel.JobId](/docs/reference/engine/classes/DataModel.md) is not.

#### Studio Limitation

Note that this service does not work during playtesting in Roblox Studio;
to test aspects of your experience using it, you must publish the
experience and play it in the Roblox application.

#### Cross-Platform Play

Players on Xbox and PlayStation with cross‑play disabled will arrive in a
different server than players with cross‑play enabled. This can cause
multiple game servers with the same
[PrivateServerId](/docs/reference/engine/classes/DataModel.md) to exist. You can use
[DataModel.MatchmakingType](/docs/reference/engine/classes/DataModel.md) to differentiate these game servers.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Teleport*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `placeId` | `int64` |  | The [DataModel.PlaceId](/docs/reference/engine/classes/DataModel.md) of the place the reserved server is being created for. |

**Returns:** `Tuple` — The server access code required by
[TeleportService:TeleportToPrivateServer()](/docs/reference/engine/classes/TeleportService.md) and the
[DataModel.PrivateServerId](/docs/reference/engine/classes/DataModel.md) for the reserved server.

**TeleportService: Teleport to a Reserved Server**

The following code teleports everyone in the current game to a reserved server
using a developer-generated reserved server ID. The first teleport with a new
ID creates the reserved server; reusing the same ID routes subsequent
teleports to that same server.

```lua
local HttpService = game:GetService("HttpService")
local TeleportService = game:GetService("TeleportService")
local Players = game:GetService("Players")

local reservedServerId = HttpService:GenerateGUID(false)

local teleportOptions = Instance.new("TeleportOptions")
teleportOptions.ReservedServerId = reservedServerId

local players = Players:GetPlayers()

TeleportService:TeleportAsync(game.PlaceId, players, teleportOptions)
-- You could add extra arguments to the TeleportOptions: SetTeleportData, ServerInstanceId, etc.
```

**TeleportService: Teleport to a Reserved Server via Chat**

The following code generates a reserved server ID, persists it in a DataStore,
and teleports any player who says "reserved" to that same reserved server
using TeleportAsync.

```lua
local HttpService = game:GetService("HttpService")
local TeleportService = game:GetService("TeleportService")
local Players = game:GetService("Players")
local DataStoreService = game:GetService("DataStoreService")

local dataStore = DataStoreService:GetGlobalDataStore()

-- Get the saved reserved server ID
local reservedServerId = dataStore:GetAsync("ReservedServerId")
if typeof(reservedServerId) ~= "string" then -- None saved, create one
	reservedServerId = HttpService:GenerateGUID(false)
	dataStore:SetAsync("ReservedServerId", reservedServerId)
end

local function joined(player)
	player.Chatted:Connect(function(message)
		if message == "reserved" then
			local teleportOptions = Instance.new("TeleportOptions")
			teleportOptions.ReservedServerId = reservedServerId
			TeleportService:TeleportAsync(game.PlaceId, { player }, teleportOptions)
		end
	end)
end

Players.PlayerAdded:Connect(joined)
```

### Method: TeleportService:SetTeleportGui

**Signature:** `TeleportService:SetTeleportGui(gui: Instance): ()`

This function sets the custom [teleport GUI](/docs/reference/engine/classes/ScreenGui.md) that will be
shown to the local user during teleportation, prior to the teleport being
invoked.

Note, the [teleport GUI](/docs/reference/engine/classes/ScreenGui.md) will not be used if the
destination place is in a different game. It will also not persist across
multiple teleports and will need to be set prior to each one.

This function should only be used on the client. If the teleportation
function is called from the server (as is the case with
[TeleportService:TeleportAsync()](/docs/reference/engine/classes/TeleportService.md)) then this function should be
called on the client prior to this. One way of doing this is listening to
a [RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md) that fires several seconds before teleportation.

#### Loading screen

During a teleport, while the destination place is loading, the
_customLoadingScreen_ is parented to the [CoreGui](/docs/reference/engine/classes/CoreGui.md). Once the place
has loaded the [loading screen](/docs/reference/engine/classes/ScreenGui.md) is
[parented](/docs/reference/engine/classes/Instance.md) to _nil_.

This [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) can be fetched at the destination place using
[TeleportService:GetArrivingTeleportGui()](/docs/reference/engine/classes/TeleportService.md), allowing you to parent
it to the [PlayerGui](/docs/reference/engine/classes/PlayerGui.md) and perform your own transitions.

You are advised to also [parent](/docs/reference/engine/classes/Instance.md) the
[ScreenGui](/docs/reference/engine/classes/ScreenGui.md) to the [PlayerGui](/docs/reference/engine/classes/PlayerGui.md) in the start place while the
teleport is initiating.

#### External references

The teleport GUI and all of its descendants are carried to the destination
place, but any property that references an [Instance](/docs/reference/engine/classes/Instance.md) **outside**
the GUI's own tree is cleared during the teleport. For example, a
[Sound](/docs/reference/engine/classes/Sound.md) inside the GUI whose [SoundGroup](/docs/reference/engine/classes/Sound.md)
points to a [SoundGroup](/docs/reference/engine/classes/SoundGroup.md) under [SoundService](/docs/reference/engine/classes/SoundService.md) will arrive with
that reference set to `nil`, because the target lives outside the GUI and
cannot safely cross the boundary between servers.

References that point to other instances **within** the GUI tree are
preserved. If your loading screen depends on an external instance,
recreate that instance inside the GUI tree.

#### Studio Limitation

Note that this service does not work during playtesting in Roblox Studio;
to test aspects of your experience using it, you must publish the
experience and play it in the Roblox application.

*Security: None · Thread Safety: Unsafe · Capabilities: UI, Teleport*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `gui` | `Instance` |  | The loading [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) that is to be displayed during teleportation. |

**Returns:** `()`

**Teleporting the local player**

This snippet demonstrates how `TeleportService` can be used to teleport the
[LocalPlayer()](/docs/reference/engine/classes/Players.md) from the client.

It also shows how [TeleportService:SetTeleportGui()](/docs/reference/engine/classes/TeleportService.md) can be used to
define a custom loading GUI. Note, this `ScreenGui` will need to be retrieved
at the destination place using
[TeleportService:GetArrivingTeleportGui()](/docs/reference/engine/classes/TeleportService.md) and be parented to the
`PlayerGui`.

```lua
local TeleportService = game:GetService("TeleportService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Players = game:GetService("Players")

local playerGui = Players.LocalPlayer:WaitForChild("PlayerGui")

local PLACE_ID = 0 -- replace here
local loadingGui = ReplicatedStorage:FindFirstChild("LoadingGui")

-- parent the loading gui for this place
loadingGui.Parent = playerGui

-- set the loading gui for the destination place
TeleportService:SetTeleportGui(loadingGui)

TeleportService:Teleport(PLACE_ID)
```

### Method: TeleportService:SetTeleportSetting

**Signature:** `TeleportService:SetTeleportSetting(setting: string, value: Variant): ()`

This function stores a value under a given key that persists across all
teleportations in the same game.

This method is intended for use on the client only and should not be used
on the server.

The stored value can later be retrieved using
[TeleportService:GetTeleportSetting()](/docs/reference/engine/classes/TeleportService.md). This will work in the
current place and any subsequent places the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md)
teleports to, provided they are in the same game.

For example, in a game that allowed crouching you could save whether the
user is currently crouching prior to teleporting as a teleport setting:

```lua
local TeleportService = game:GetService("TeleportService")

local isCrouching = false
TeleportService:SetTeleportSetting("isCrouching", isCrouching)
```

The stored value may only contain value types. It cannot contain
[Instances](/docs/reference/engine/classes/Instance.md) or other types that reference engine state, as
these cannot safely cross the boundary between servers.

Allowed values:

- Primitives: a `bool`, a `number`, or a `string`
- Value types such as [Vector3](/docs/reference/engine/datatypes/Vector3.md), [CFrame](/docs/reference/engine/datatypes/CFrame.md),
  [Color3](/docs/reference/engine/datatypes/Color3.md), [UDim2](/docs/reference/engine/datatypes/UDim2.md), [NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md),
  [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md), `Enum` items, and similar
- A table without mixed keys (all strings or all integers) containing only
  the allowed types above

Not allowed (these will be removed before the teleport completes):

- [Instance](/docs/reference/engine/classes/Instance.md) and instance references
- [Connections](/docs/reference/engine/datatypes/RBXScriptConnection.md), [RBXScriptSignal](/docs/reference/engine/datatypes/RBXScriptSignal.md),
  and functions
- `SharedTable`
- Types that reference engine or [DataModel](/docs/reference/engine/classes/DataModel.md) state, such as
  [InputObject](/docs/reference/engine/classes/InputObject.md), [RaycastParams](/docs/reference/engine/datatypes/RaycastParams.md), and
  [RaycastResult](/docs/reference/engine/datatypes/RaycastResult.md)

If a stored setting contains a disallowed type, that value is removed and
an error is written to the developer console. Convert instance references
to plain values (for example, a numeric ID or a string path).

If data is already stored under the given key, the previous value will be
overwritten by the new value.

#### Differences from GlobalDataStores

Although they share some similarities, there are some key differences
between teleport settings and datastores:

- [GlobalDataStore:SetAsync()](/docs/reference/engine/classes/GlobalDataStore.md) stores the data on Roblox servers
  whereas SetTeleportSetting stores the data locally
- Data stored in a [GlobalDataStore](/docs/reference/engine/classes/GlobalDataStore.md) is preserved after the user
  leaves the game universe whereas teleport settings are not
- [GlobalDataStores](/docs/reference/engine/classes/GlobalDataStore.md) can only be accessed on the
  server, whereas teleport settings can only be accessed on the client
- [GlobalDataStores](/docs/reference/engine/classes/GlobalDataStore.md) have usage limits, whereas
  teleport settings do not

In general teleport settings should be used to preserve client side
information within a single play session across different places in a
game. [GlobalDataStores](/docs/reference/engine/classes/GlobalDataStore.md) should be used to save
important player data that needs to be accessed across player sessions.

#### Teleport settings and security

As teleport settings are stored locally, it is possible they can be
manipulated by malicious users. This risk can be mitigated by employing
server side validation.

#### Studio Limitation

Note that this service does not work during playtesting in Roblox Studio;
to test aspects of your experience using it, you must publish the
experience and play it in the Roblox application.

*Security: None · Thread Safety: Unsafe · Capabilities: Teleport*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `setting` | `string` |  | The key to store the _value_ under. This key can be used to retrieve the value using [TeleportService:GetTeleportSetting()](/docs/reference/engine/classes/TeleportService.md). |
| `value` | `Variant` |  | The value to store. |

**Returns:** `()`

### Method: TeleportService:Teleport

**Signature:** `TeleportService:Teleport(placeId: int64, player?: Instance, teleportData: Variant, customLoadingScreen?: Instance): ()`

This method should not be used for new work; the numerous teleport
functions have been combined into a single method,
[TeleportAsync()](/docs/reference/engine/classes/TeleportService.md), which should be
used instead.

*Security: None · Thread Safety: Unsafe · Capabilities: UI, Teleport*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `placeId` | `int64` |  | The ID of the place to teleport to. |
| `player` | `Instance` | `nil` | The [Player](/docs/reference/engine/classes/Player.md) to teleport, if this function is being called from the client this defaults to the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md). |
| `teleportData` | `Variant` |  | Optional data to be passed to the destination place. Can be retrieved using [TeleportService:GetLocalPlayerTeleportData()](/docs/reference/engine/classes/TeleportService.md). |
| `customLoadingScreen` | `Instance` | `nil` | Optional custom loading screen to be placed in the [CoreGui](/docs/reference/engine/classes/CoreGui.md) at the destination place. Can be retrieved using [TeleportService:GetArrivingTeleportGui()](/docs/reference/engine/classes/TeleportService.md). |

**Returns:** `()`

**Teleporting the local player**

This snippet demonstrates how `TeleportService` can be used to teleport the
[LocalPlayer()](/docs/reference/engine/classes/Players.md) from the client.

It also shows how [TeleportService:SetTeleportGui()](/docs/reference/engine/classes/TeleportService.md) can be used to
define a custom loading GUI. Note, this `ScreenGui` will need to be retrieved
at the destination place using
[TeleportService:GetArrivingTeleportGui()](/docs/reference/engine/classes/TeleportService.md) and be parented to the
`PlayerGui`.

```lua
local TeleportService = game:GetService("TeleportService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Players = game:GetService("Players")

local playerGui = Players.LocalPlayer:WaitForChild("PlayerGui")

local PLACE_ID = 0 -- replace here
local loadingGui = ReplicatedStorage:FindFirstChild("LoadingGui")

-- parent the loading gui for this place
loadingGui.Parent = playerGui

-- set the loading gui for the destination place
TeleportService:SetTeleportGui(loadingGui)

TeleportService:Teleport(PLACE_ID)
```

**Teleporting from the server**

This snippet demonstrates how `TeleportService` can be used to teleport a
`Player` from the server.

```lua
local Players = game:GetService("Players")
local TeleportService = game:GetService("TeleportService")

local PLACE_ID = 0 -- replace here
local USER_ID = 1 -- replace with player's UserId

local player = Players:GetPlayerByUserId(USER_ID)

TeleportService:Teleport(PLACE_ID, player)
```

### Method: TeleportService:TeleportAsync

**Signature:** `TeleportService:TeleportAsync(placeId: int64, players: Instances, teleportOptions?: Instance): Instance`

This function serves as the all-encompassing method to teleport a player
or group of players from one server to another. It can be used to:

- Teleport players to a different place.
- Teleport players to a specific server.
- Teleport players to a reserved server.

#### Server-Only

This method can only be called from the server. If you need to initiate a
teleport from the client, use a [RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md) to signal the server,
then call [TeleportService:TeleportAsync()](/docs/reference/engine/classes/TeleportService.md) from a server
[Script](/docs/reference/engine/classes/Script.md). Client-side teleports using
[TeleportService:Teleport()](/docs/reference/engine/classes/TeleportService.md) is not recommended for new work. See
[Teleport between places](/docs/en-us/projects/teleport.md) for more
information.

#### Group Teleport Limitations

- Groups of players can only be teleported within a single experience.
- No more than 50 players can be teleported with a single
  [TeleportService:TeleportAsync()](/docs/reference/engine/classes/TeleportService.md) call.

#### Potential Errors

This is a list of potential reasons a teleport may fail, ranging from
invalid teleports to network issues.

| Error | Description |
| --- | --- |
| Invalid placeId | The provided place ID is below 0. |
| Players empty | The provided list of players to teleport is empty. |
| List of players instances is incorrect | Any of the provided players is not a Player object. |
| TeleportOptions not of correct type | The provided teleportOption is not a TeleportOptions object. |
| TeleportAsync called from Client | The client called TeleportAsync, which can only be called from the server. |
| Incompatible Parameters | Conflicting teleport options were used and TeleportService doesn't know where to send the player.

 Only one of the following private-server routing fields may be set at a time:
 * ReservedServerId
 * VipServerId
 * ReservedServerAccessCode
 * ShouldReserveServer
 * ServerInstanceId |

For more information on how to teleport players between servers and
receive user data from a teleport, see
[Teleport between places](/docs/en-us/projects/teleport.md#sending-user-data-along-with-teleports).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: UI, Teleport*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `placeId` | `int64` |  | The place ID the player(s) should be teleported to. |
| `players` | `Instances` |  | An array of the player(s) to teleport. |
| `teleportOptions` | `Instance` | `nil` | An optional [TeleportOptions](/docs/reference/engine/classes/TeleportOptions.md) object containing additional arguments to the [TeleportService:TeleportAsync()](/docs/reference/engine/classes/TeleportService.md) call. If this is not passed, no result will be returned. |

**Returns:** `Instance` — If a [TeleportOptions](/docs/reference/engine/classes/TeleportOptions.md) parameter is passed, this will be a
[TeleportAsyncResult](/docs/reference/engine/classes/TeleportAsyncResult.md) object that provides information about the
final teleport destination.

### Method: TeleportService:ReserveServer

**Signature:** `TeleportService:ReserveServer(placeId: int64): Tuple`

> **Deprecated:** Use [TeleportAsync()](/docs/reference/engine/classes/TeleportService.md) with [TeleportOptions.ReservedServerId](/docs/reference/engine/classes/TeleportOptions.md) instead. Generate a GUID with [HttpService:GenerateGUID()](/docs/reference/engine/classes/HttpService.md) and pass it as [TeleportOptions.ReservedServerId](/docs/reference/engine/classes/TeleportOptions.md).

This function is deprecated and no longer supported. It remains available
for backward compatibility but should not be used for new work.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Teleport*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `placeId` | `int64` |  | The [DataModel.PlaceId](/docs/reference/engine/classes/DataModel.md) of the place the reserved server is being created for. |

**Returns:** `Tuple` — The server access code required by
[TeleportService:TeleportToPrivateServer()](/docs/reference/engine/classes/TeleportService.md) and the
[DataModel.PrivateServerId](/docs/reference/engine/classes/DataModel.md) for the reserved server.

**TeleportService: Teleport to a Reserved Server**

The following code teleports everyone in the current game to a reserved server
using a developer-generated reserved server ID. The first teleport with a new
ID creates the reserved server; reusing the same ID routes subsequent
teleports to that same server.

```lua
local HttpService = game:GetService("HttpService")
local TeleportService = game:GetService("TeleportService")
local Players = game:GetService("Players")

local reservedServerId = HttpService:GenerateGUID(false)

local teleportOptions = Instance.new("TeleportOptions")
teleportOptions.ReservedServerId = reservedServerId

local players = Players:GetPlayers()

TeleportService:TeleportAsync(game.PlaceId, players, teleportOptions)
-- You could add extra arguments to the TeleportOptions: SetTeleportData, ServerInstanceId, etc.
```

**TeleportService: Teleport to a Reserved Server via Chat**

The following code generates a reserved server ID, persists it in a DataStore,
and teleports any player who says "reserved" to that same reserved server
using TeleportAsync.

```lua
local HttpService = game:GetService("HttpService")
local TeleportService = game:GetService("TeleportService")
local Players = game:GetService("Players")
local DataStoreService = game:GetService("DataStoreService")

local dataStore = DataStoreService:GetGlobalDataStore()

-- Get the saved reserved server ID
local reservedServerId = dataStore:GetAsync("ReservedServerId")
if typeof(reservedServerId) ~= "string" then -- None saved, create one
	reservedServerId = HttpService:GenerateGUID(false)
	dataStore:SetAsync("ReservedServerId", reservedServerId)
end

local function joined(player)
	player.Chatted:Connect(function(message)
		if message == "reserved" then
			local teleportOptions = Instance.new("TeleportOptions")
			teleportOptions.ReservedServerId = reservedServerId
			TeleportService:TeleportAsync(game.PlaceId, { player }, teleportOptions)
		end
	end)
end

Players.PlayerAdded:Connect(joined)
```

### Method: TeleportService:TeleportPartyAsync

**Signature:** `TeleportService:TeleportPartyAsync(placeId: int64, players: Instances, teleportData: Variant, customLoadingScreen?: Instance): string`

> **Deprecated:** Use [TeleportAsync()](/docs/reference/engine/classes/TeleportService.md) instead. For a migration guide, see [Teleport between places](/docs/en-us/projects/teleport.md#migrate-to-secure-teleports).

This method should not be used for new work; the numerous teleport
functions have been combined into a single method,
[TeleportAsync()](/docs/reference/engine/classes/TeleportService.md), which should be
used instead.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: UI, Teleport*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `placeId` | `int64` |  | The ID of the place to teleport to. |
| `players` | `Instances` |  | An array containing the [Players](/docs/reference/engine/classes/Player.md) to teleport. |
| `teleportData` | `Variant` |  | Optional data to be passed to the destination place. Can be retrieved using [TeleportService:GetLocalPlayerTeleportData()](/docs/reference/engine/classes/TeleportService.md). |
| `customLoadingScreen` | `Instance` | `nil` | Optional custom loading screen to be placed in the [CoreGui](/docs/reference/engine/classes/CoreGui.md) at the destination place. Can be retrieved using [TeleportService:GetArrivingTeleportGui()](/docs/reference/engine/classes/TeleportService.md). |

**Returns:** `string` — The [DataModel.JobId](/docs/reference/engine/classes/DataModel.md) of the server instance the
[Players](/docs/reference/engine/classes/Player.md) were teleported to.

**Teleport all players in the server**

This code sample is an example of how
[TeleportService:TeleportPartyAsync()](/docs/reference/engine/classes/TeleportService.md) can be used to teleport a group
of `Player|Players`.

In this case, all `Player|Players` will be teleported to the specified
_placeId_ as a party. The [DataModel.JobId](/docs/reference/engine/classes/DataModel.md) of the destination server is
then printed.

```lua
local Players = game:GetService("Players")
local TeleportService = game:GetService("TeleportService")

local PLACE_ID = 0 -- replace
local playerList = Players:GetPlayers()

local success, result = pcall(function()
	return TeleportService:TeleportPartyAsync(PLACE_ID, playerList)
end)

if success then
	local jobId = result
	print("Players teleported to", jobId)
else
	warn(result)
end
```

### Method: TeleportService:TeleportToPlaceInstance

**Signature:** `TeleportService:TeleportToPlaceInstance(placeId: int64, instanceId: string, player?: Instance, spawnName: string, teleportData: Variant, customLoadingScreen?: Instance): ()`

> **Deprecated:** Use [TeleportAsync()](/docs/reference/engine/classes/TeleportService.md) instead. For a migration guide, see [Teleport between places](/docs/en-us/projects/teleport.md#migrate-to-secure-teleports).

This method should not be used for new work; the numerous teleport
functions have been combined into a single method,
[TeleportAsync()](/docs/reference/engine/classes/TeleportService.md), which should be
used instead.

*Security: None · Thread Safety: Unsafe · Capabilities: UI, Teleport*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `placeId` | `int64` |  | The ID of the place to teleport to. |
| `instanceId` | `string` |  | The [DataModel.JobId](/docs/reference/engine/classes/DataModel.md) of the server instance to teleport to. |
| `player` | `Instance` | `nil` | The [Player](/docs/reference/engine/classes/Player.md) to teleport, if this function is being called from the client this defaults to the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md). |
| `spawnName` | `string` |  | Optional name of the [SpawnLocation](/docs/reference/engine/classes/SpawnLocation.md) to spawn at. |
| `teleportData` | `Variant` |  | Optional data to be passed to the destination place. Can be retrieved using [TeleportService:GetLocalPlayerTeleportData()](/docs/reference/engine/classes/TeleportService.md). |
| `customLoadingScreen` | `Instance` | `nil` | Optional custom loading screen to be placed in the [CoreGui](/docs/reference/engine/classes/CoreGui.md) at the destination place. Can be retrieved using [TeleportService:GetArrivingTeleportGui()](/docs/reference/engine/classes/TeleportService.md). |

**Returns:** `()`

**Following Another Player**

The code sample below, when placed inside a `Script` within
`ServerScriptService`, will teleport a player who's following another player
to the associated place/server. Note that this will not work if the player
being followed is in a reserved server.

```lua
local TeleportService = game:GetService("TeleportService")
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	local followId = player.FollowUserId

	if followId and followId ~= 0 then
		-- Is this player following anyone? If so, find out where they are
		local success, currentInstance, error, placeId, jobIdOrErr = pcall(function()
			return TeleportService:GetPlayerPlaceInstanceAsync(followId)
		end)
			-- followId is the user ID of the player that you want to retrieve the place and job ID for
		if success then
			-- Teleports player on success based off jobId
			TeleportService:TeleportToPlaceInstance(placeId, jobIdOrErr, player)
		else
			-- Posts a warning based off returning error
			warn(jobIdOrErr)
		end
	else
		warn(("Player %d is not following another player!"):format(player.UserId))
	end
end)
```

### Method: TeleportService:TeleportToPrivateServer

**Signature:** `TeleportService:TeleportToPrivateServer(placeId: int64, reservedServerAccessCode: string, players: Instances, spawnName: string, teleportData: Variant, customLoadingScreen?: Instance): ()`

> **Deprecated:** Use [TeleportAsync()](/docs/reference/engine/classes/TeleportService.md) with [TeleportOptions.ReservedServerId](/docs/reference/engine/classes/TeleportOptions.md) instead. Generate a GUID with [HttpService:GenerateGUID()](/docs/reference/engine/classes/HttpService.md) and pass it as [TeleportOptions.ReservedServerId](/docs/reference/engine/classes/TeleportOptions.md).

This method is deprecated and no longer supported. It remains available
for backward compatibility but should not be used for new work. Use
[TeleportAsync()](/docs/reference/engine/classes/TeleportService.md) with
[TeleportOptions.ReservedServerId](/docs/reference/engine/classes/TeleportOptions.md) instead.

*Security: None · Thread Safety: Unsafe · Capabilities: UI, Teleport*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `placeId` | `int64` |  | The ID of the place to teleport to. |
| `reservedServerAccessCode` | `string` |  | The reserved server access code returned by [TeleportService:ReserveServerAsync()](/docs/reference/engine/classes/TeleportService.md). |
| `players` | `Instances` |  | An array of [Players](/docs/reference/engine/classes/Player.md) to teleport. |
| `spawnName` | `string` |  | Optional name of the [SpawnLocation](/docs/reference/engine/classes/SpawnLocation.md) to spawn at. |
| `teleportData` | `Variant` |  | Optional data to be passed to the destination place. Can be retrieved using [TeleportService:GetLocalPlayerTeleportData()](/docs/reference/engine/classes/TeleportService.md). |
| `customLoadingScreen` | `Instance` | `nil` | Optional custom loading screen to be placed in the [CoreGui](/docs/reference/engine/classes/CoreGui.md) at the destination place. Can be retrieved using [TeleportService:GetArrivingTeleportGui()](/docs/reference/engine/classes/TeleportService.md). |

**Returns:** `()`

**TeleportService: Teleport to a Reserved Server via Chat**

The following code generates a reserved server ID, persists it in a DataStore,
and teleports any player who says "reserved" to that same reserved server
using TeleportAsync.

```lua
local HttpService = game:GetService("HttpService")
local TeleportService = game:GetService("TeleportService")
local Players = game:GetService("Players")
local DataStoreService = game:GetService("DataStoreService")

local dataStore = DataStoreService:GetGlobalDataStore()

-- Get the saved reserved server ID
local reservedServerId = dataStore:GetAsync("ReservedServerId")
if typeof(reservedServerId) ~= "string" then -- None saved, create one
	reservedServerId = HttpService:GenerateGUID(false)
	dataStore:SetAsync("ReservedServerId", reservedServerId)
end

local function joined(player)
	player.Chatted:Connect(function(message)
		if message == "reserved" then
			local teleportOptions = Instance.new("TeleportOptions")
			teleportOptions.ReservedServerId = reservedServerId
			TeleportService:TeleportAsync(game.PlaceId, { player }, teleportOptions)
		end
	end)
end

Players.PlayerAdded:Connect(joined)
```

**TeleportService: Teleport to a Reserved Server**

The following code teleports everyone in the current game to a reserved server
using a developer-generated reserved server ID. The first teleport with a new
ID creates the reserved server; reusing the same ID routes subsequent
teleports to that same server.

```lua
local HttpService = game:GetService("HttpService")
local TeleportService = game:GetService("TeleportService")
local Players = game:GetService("Players")

local reservedServerId = HttpService:GenerateGUID(false)

local teleportOptions = Instance.new("TeleportOptions")
teleportOptions.ReservedServerId = reservedServerId

local players = Players:GetPlayers()

TeleportService:TeleportAsync(game.PlaceId, players, teleportOptions)
-- You could add extra arguments to the TeleportOptions: SetTeleportData, ServerInstanceId, etc.
```

### Method: TeleportService:TeleportToSpawnByName

**Signature:** `TeleportService:TeleportToSpawnByName(placeId: int64, spawnName: string, player?: Instance, teleportData: Variant, customLoadingScreen?: Instance): ()`

> **Deprecated:** Use [TeleportAsync()](/docs/reference/engine/classes/TeleportService.md) instead. For a migration guide, see [Teleport between places](/docs/en-us/projects/teleport.md#migrate-to-secure-teleports).

This method should not be used for new work; the numerous teleport
functions have been combined into a single method,
[TeleportAsync()](/docs/reference/engine/classes/TeleportService.md), which should be
used instead.

*Security: None · Thread Safety: Unsafe · Capabilities: UI, Teleport*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `placeId` | `int64` |  | The ID of the place to teleport to. |
| `spawnName` | `string` |  | The name of the [SpawnLocation](/docs/reference/engine/classes/SpawnLocation.md) to spawn at. |
| `player` | `Instance` | `nil` | The [Player](/docs/reference/engine/classes/Player.md) to teleport, if this function is being called from the client this defaults to the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md). |
| `teleportData` | `Variant` |  | Optional data to be passed to the destination place. Can be retrieved using [TeleportService:GetLocalPlayerTeleportData()](/docs/reference/engine/classes/TeleportService.md). |
| `customLoadingScreen` | `Instance` | `nil` | Optional custom loading screen to be placed in the [CoreGui](/docs/reference/engine/classes/CoreGui.md) at the destination place. Can be retrieved using [TeleportService:GetArrivingTeleportGui()](/docs/reference/engine/classes/TeleportService.md). |

**Returns:** `()`

**TeleportService:TeleportToSpawnByName**

This code will teleport a player to Crossroads, and if there is a spawn named
"TeleportSpawn" then the player would spawn on it. This assumes it's being
used in a [LocalScript](/docs/reference/engine/classes/LocalScript.md).

```lua
local TeleportService = game:GetService("TeleportService")

TeleportService:TeleportToSpawnByName(1818, "TeleportSpawn")
```

## Events

### Event: TeleportService.LocalPlayerArrivedFromTeleport

**Signature:** `TeleportService.LocalPlayerArrivedFromTeleport(loadingGui: Instance, dataTable: Variant)`

This function fires when the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md) enters the place
following a teleport. The `teleportData` and `customLoadingScreen` are
provided as arguments.

When fetching _teleportData_ and the _customLoadingScreen_ you are advised
to use [TeleportService:GetLocalPlayerTeleportData()](/docs/reference/engine/classes/TeleportService.md) and
[TeleportService:GetArrivingTeleportGui()](/docs/reference/engine/classes/TeleportService.md) instead. This is because
these functions can be called immediately without having to wait for this
event to fire.

This event should be connected immediately in a [LocalScript](/docs/reference/engine/classes/LocalScript.md)
parented to [ReplicatedFirst](/docs/reference/engine/classes/ReplicatedFirst.md). Otherwise, when the connection is
made the event may have already fired.

#### Loading Screen

During a teleport, while the destination place is loading, the
_customLoadingScreen_ is parented to the [CoreGui](/docs/reference/engine/classes/CoreGui.md). Once the place
has loaded the [loading screen](/docs/reference/engine/classes/ScreenGui.md) is
[parented](/docs/reference/engine/classes/Instance.md) to _nil_.

If you wish to preserve the _customLoadingScreen_ and perform your own
transitions, you will need to parent it to the local player's
[PlayerGui](/docs/reference/engine/classes/PlayerGui.md). For example, using the following code inside a
[LocalScript](/docs/reference/engine/classes/LocalScript.md) in [ReplicatedFirst](/docs/reference/engine/classes/ReplicatedFirst.md):

```lua
local TeleportService = game:GetService("TeleportService")
local Players = game:GetService("Players")
local ReplicatedFirst = game:GetService("ReplicatedFirst")

TeleportService.LocalPlayerArrivedFromTeleport:Connect(function(customLoadingScreen, teleportData)
	local playerGui = Players.LocalPlayer:WaitForChild("PlayerGui")
	ReplicatedFirst:RemoveDefaultLoadingScreen()

	customLoadingScreen.Parent = playerGui
	-- animate screen here
	wait(5)
	-- destroy screen
	customLoadingScreen:Destroy()
end)
```

The _customLoadingScreen_ will not be used if the destination place is in
a different game.

#### Studio Limitation

Note that this service does not work during playtesting in Roblox Studio;
to test aspects of your experience using it, you must publish the
experience and play it in the Roblox application.

*Security: None · Capabilities: Teleport*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `loadingGui` | `Instance` | The _customLoadingScreen_ the [LocalPlayer](/docs/reference/engine/classes/Players.md) arrived into the place with. |
| `dataTable` | `Variant` | The _teleportData_ the [LocalPlayer](/docs/reference/engine/classes/Players.md) arrived into the place with. |

### Event: TeleportService.TeleportInitFailed

**Signature:** `TeleportService.TeleportInitFailed(player: Instance, teleportResult: TeleportResult, errorMessage: string, placeId: int64, teleportOptions: Instance)`

This event fires on both the client and the server when a request to
teleport from a function such as [TeleportService:TeleportAsync()](/docs/reference/engine/classes/TeleportService.md)
fails and the player does not leave the current server. It provides a
reason for the failure, as well as all of the information necessary to
retry the teleport. If a group teleport fails, the event will fire once
per player.

#### TeleportOptions

The [TeleportOptions](/docs/reference/engine/classes/TeleportOptions.md) object provided by this event is not identical
to the one passed to the original [TeleportService:TeleportAsync()](/docs/reference/engine/classes/TeleportService.md)
call. It is a new object populated with the necessary parameters to retry
the teleport and send the player to the exact same destination. This is
especially important for facilitating group teleports when they fail.

| Original Teleport Type | Teleport Data | ReservedServerId | VipServerId | ReservedServerAccessCode | ServerInstanceId | ShouldReserveServer |
| --- | --- | --- | --- | --- | --- | --- |
| Individual player to place | Original value | None | None | None | None | false |
| Player(s) to reserved server (ReservedServerId) | Original value | Original value | None | None | None | false |
| Player(s) to VIP server (VipServerId) | Original value | None | Original value | None | None | false |
| Player(s) to reserved server (legacy access code) | Original value | None | None | Original value, or the code generated if ShouldReserveServer was originally true | None | false |
| Player(s) to specific server | Original value | None | None | None | Original value | false |
| Players to place | Original value | None | None | None | Same destination ID as the other players in the original teleport | false |

When the engine routes a plain teleport to a VIP server, VIP-specific join
failures such as a full or flooded server fall back to a public join and
this event does not fire. Only teleports with an explicit
[TeleportOptions.VipServerId](/docs/reference/engine/classes/TeleportOptions.md) surface a VIP join failure through
this event.

For more information on how to teleport players between servers, see
[Teleport between places](/docs/en-us/projects/teleport.md).

*Security: None · Capabilities: Teleport*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Instance` | The [Player](/docs/reference/engine/classes/Player.md) instance that failed to teleport. |
| `teleportResult` | `TeleportResult` | The reason for the teleport failure. |
| `errorMessage` | `string` | The message provided to the player explaining the teleport failure. |
| `placeId` | `int64` | The original target place ID of the teleport. |
| `teleportOptions` | `Instance` | A [TeleportOptions](/docs/reference/engine/classes/TeleportOptions.md) object that can be passed back to [TeleportService:TeleportAsync()](/docs/reference/engine/classes/TeleportService.md) to retry the failed teleport. |

## Inherited Members

### From [Instance](/docs/reference/engine/classes/Instance.md)

- **Property `Archivable`** (`boolean`): Determines if an Instance and its descendants can be cloned using
- **Property `archivable`** (`boolean`):  *(deprecated, hidden)*
- **Property `Capabilities`** (`SecurityCapabilities`): The set of capabilities allowed to be used for scripts inside this
- **Property `IsInSandbox`** (`boolean`): Indicates whether the instance is inside a sandboxed container.
- **Property `Name`** (`string`): A non-unique identifier of the Instance.
- **Property `Parent`** (`Instance`): Determines the hierarchical parent of the Instance.
- **Property `PredictionMode`** (`PredictionMode`): Reflects the client-side prediction mode applied to the instance under
- **Property `RobloxLocked`** (`boolean`): A deprecated property that used to protect CoreGui objects. *(hidden)*
- **Property `Sandboxed`** (`boolean`): When enabled, the instance can only access abilities in its `Capabilities`
- **Property `UniqueId`** (`UniqueId`): A unique identifier for the instance.
- **Method `AddTag(tag: string): ()`**: Applies a tag to the instance.
- **Method `children(): Instances`**: Returns an array of the object's children. *(deprecated)*
- **Method `ClearAllChildren(): ()`**: This method destroys all of an instance's children.
- **Method `Clone(): Instance`**: Create a copy of an instance and all its descendants, ignoring instances
- **Method `clone(): Instance`**:  *(deprecated)*
- **Method `Destroy(): ()`**: Sets the Instance.Parent property to `nil`, locks the
- **Method `destroy(): ()`**:  *(deprecated)*
- **Method `FindFirstAncestor(name: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorOfClass(className: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorWhichIsA(className: string): Instance?`**: Returns the first ancestor of the Instance for whom
- **Method `FindFirstChild(name: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance found with the given name.
- **Method `findFirstChild(name: string, recursive?: boolean): Instance`**:  *(deprecated)*
- **Method `FindFirstChildOfClass(className: string): Instance?`**: Returns the first child of the Instance whose
- **Method `FindFirstChildWhichIsA(className: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance for whom
- **Method `FindFirstDescendant(name: string): Instance?`**: Returns the first descendant found with the given Instance.Name.
- **Method `GetActor(): Actor?`**: Returns the Actor associated with the Instance, if any.
- **Method `GetAttribute(attribute: string): Variant`**: Returns the value which has been assigned to the given attribute name.
- **Method `GetAttributeChangedSignal(attribute: string): RBXScriptSignal`**: Returns an event that fires when the given attribute changes.
- **Method `GetAttributes(): Dictionary`**: Returns a dictionary of the instance's attributes.
- **Method `GetChildren(): Instances`**: Returns an array containing all of the instance's children.
- **Method `getChildren(): Instances`**:  *(deprecated)*
- **Method `GetDebugId(scopeLength?: int): string`**: Returns a coded string of the debug ID used internally by Roblox.
- **Method `GetDescendants(): Instances`**: Returns an array containing all of the descendants of the instance.
- **Method `GetFullName(): string`**: Returns a string describing the instance's ancestry.
- **Method `GetStyled(name: string, selector: string?): Variant`**: Returns the styled or explicitly modified value of the specified property,
- **Method `GetStyledPropertyChangedSignal(property: string): RBXScriptSignal`**: Returns an event that fires when the given style property changes on the
- **Method `GetTags(): Array`**: Gets an array of all tags applied to the instance.
- **Method `HasTag(tag: string): boolean`**: Check whether the instance has a given tag.
- **Method `IsAncestorOf(descendant: Instance): boolean`**: Returns true if an Instance is an ancestor of the given
- **Method `IsDescendantOf(ancestor: Instance): boolean`**: Returns `true` if an Instance is a descendant of the given
- **Method `isDescendantOf(ancestor: Instance): boolean`**:  *(deprecated)*
- **Method `IsPropertyModified(property: string): boolean`**: Returns `true` if the value stored in the specified property is not equal
- **Method `QueryDescendants(selector: string): Instances`**: Returns an array containing all descendants of the instance that match the
- **Method `Remove(): ()`**: Sets the object's `Parent` to `nil`, and does the same for all its *(deprecated)*
- **Method `remove(): ()`**:  *(deprecated)*
- **Method `RemoveTag(tag: string): ()`**: Removes a tag from the instance.
- **Method `ResetPropertyToDefault(property: string): ()`**: Resets a property to its default value.
- **Method `SetAttribute(attribute: string, value: Variant): ()`**: Sets the attribute with the given name to the given value.
- **Method `WaitForChild(childName: string, timeOut: double): Instance`**: Returns the child of the Instance with the given name. If the
- **Event `AncestryChanged`**: Fires when the Instance.Parent property of this object or one of
- **Event `AttributeChanged`**: Fires whenever an attribute is changed on the Instance.
- **Event `ChildAdded`**: Fires after an object is parented to this Instance.
- **Event `childAdded`**:  *(deprecated)*
- **Event `ChildRemoved`**: Fires after a child is removed from this Instance.
- **Event `DescendantAdded`**: Fires after a descendant is added to the Instance.
- **Event `DescendantRemoving`**: Fires immediately before a descendant of the Instance is removed.
- **Event `Destroying`**: Fires immediately before (or is deferred until after) the instance is
- **Event `StyledPropertiesChanged`**: Fires whenever any style property is changed on the instance, including

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some