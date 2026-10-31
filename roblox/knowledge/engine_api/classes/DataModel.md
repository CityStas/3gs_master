---
name: DataModel
last_updated: 2026-10-30T19:55:52Z
inherits:
  - ServiceProvider
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
summary: "The root of Roblox's parent-child hierarchy. Its direct children are services, such as Workspace and Lighting, that act as the fundamental components of a Roblox game."
---

# Class: DataModel

> The root of Roblox's parent-child hierarchy. Its direct children are services,
> such as [Workspace](/docs/reference/engine/classes/Workspace.md) and [Lighting](/docs/reference/engine/classes/Lighting.md), that act as the fundamental
> components of a Roblox game.

## Description

The [Data Model](/docs/en-us/projects/data-model.md) (commonly known as `game`
after the global variable used to access it) is the root of Roblox's
parent-child hierarchy. Its direct children are services, such as
[Workspace](/docs/reference/engine/classes/Workspace.md) and [Lighting](/docs/reference/engine/classes/Lighting.md), that act as the fundamental components
of a Roblox game.

## Code Samples

**GetService()**

Demonstrates using `game`, the root instance of [DataModel](/docs/reference/engine/classes/DataModel.md), to get
services such as [Workspace](/docs/reference/engine/classes/Workspace.md) and [Lighting](/docs/reference/engine/classes/Lighting.md).

```lua
local Workspace = game:GetService("Workspace")
local Lighting = game:GetService("Lighting")

-- Examples of modifying properties of these services
Workspace.Gravity = 20
Lighting.ClockTime = 4
```

## Properties

### Property: DataModel.CreatorId

```json
{
  "type": "int64",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "State"
}
```

This property describes the ID of the user or group that owns the place.
If the [DataModel.CreatorType](/docs/reference/engine/classes/DataModel.md) property is `User` then `CreatorId`
will be the [Player.UserId](/docs/reference/engine/classes/Player.md) of the place's owner. If the
[DataModel.CreatorType](/docs/reference/engine/classes/DataModel.md) is `Group` then `CreatorId` will be the ID
of the group that owns the place.

**Detect when the place owner joins the game**

This code sample will print an output when the user that owns the game, or a
member of the group that owns the game joins the server.

To run this script, place it inside a `Script` in `ServerScriptService`

```lua
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	if game.CreatorType == Enum.CreatorType.User then
		if player.UserId == game.CreatorId then
			print("The place owner has joined the game!")
		end
	elseif game.CreatorType == Enum.CreatorType.Group then
		if player:IsInGroupAsync(game.CreatorId) then
			print("A member of the group that owns the place has joined the game!")
		end
	end
end)
```

### Property: DataModel.CreatorType

```json
{
  "type": "CreatorType",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "State"
}
```

This property describes the [CreatorType](/docs/reference/engine/enums/CreatorType.md) of the place, whether the
place is owned by a user or a group. If `User`, then the
[DataModel.CreatorId](/docs/reference/engine/classes/DataModel.md) property will describe the
[UserId](/docs/reference/engine/classes/Player.md) of the account that owns the game. If
`Group`, then it will describe the group ID.

**Detect when the place owner joins the game**

This code sample will print an output when the user that owns the game, or a
member of the group that owns the game joins the server.

To run this script, place it inside a `Script` in `ServerScriptService`

```lua
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	if game.CreatorType == Enum.CreatorType.User then
		if player.UserId == game.CreatorId then
			print("The place owner has joined the game!")
		end
	elseif game.CreatorType == Enum.CreatorType.Group then
		if player:IsInGroupAsync(game.CreatorId) then
			print("A member of the group that owns the place has joined the game!")
		end
	end
end)
```

### Property: DataModel.GameId

```json
{
  "type": "int64",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "State"
}
```

This property describes the ID of the experience that the place running on
the server belongs to.

#### See Also

- [DataModel.PlaceId](/docs/reference/engine/classes/DataModel.md), which describes the ID of the place running
  on the server
- [DataModel.JobId](/docs/reference/engine/classes/DataModel.md), which is a unique identifier for the server
  game instance running
- [TeleportService](/docs/reference/engine/classes/TeleportService.md), which is a service that can be used to
  transport [Players](/docs/reference/engine/classes/Player.md) between games

### Property: DataModel.Genre

```json
{
  "type": "Genre",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "State"
}
```

This property is broken and should not be used.

This property historically described the [Genre](/docs/reference/engine/enums/Genre.md) of the place as set
on the Roblox website.

This property, along with [DataModel.GearGenreSetting](/docs/reference/engine/classes/DataModel.md), no longer
functions correctly due to genres existing on the Roblox website that are
not reflected in the [Genre](/docs/reference/engine/enums/Genre.md) enum. As a result, attempting to read
this property may throw an error.

### Property: DataModel.JobId

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "JobInfo"
}
```

This property is a unique identifier for the running game server instance.
It is a universally unique identifier (UUID), meaning that no two servers,
past or present, will ever have the same ID.

Defaults to an empty string in Studio.

#### See Also

- [TeleportService:GetPlayerPlaceInstanceAsync()](/docs/reference/engine/classes/TeleportService.md) which can be used
  to retrieve the [DataModel.JobId](/docs/reference/engine/classes/DataModel.md) of a user's current server.
- [TeleportService:TeleportToPlaceInstance()](/docs/reference/engine/classes/TeleportService.md) which can be used to
  teleport a [Player](/docs/reference/engine/classes/Player.md) to a specific server.
- [DataModel.PrivateServerId](/docs/reference/engine/classes/DataModel.md) describes the ID of the private server
  the game server instance belongs to.
- [HttpService:GenerateGUID()](/docs/reference/engine/classes/HttpService.md), a function that can be used to
  generate your own UUIDs.

### Property: DataModel.MatchmakingType

```json
{
  "type": "MatchmakingType",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

This property represents how players in the server are handled by
matchmaking. Players with different
[MatchmakingTypes](/docs/reference/engine/classes/DataModel.md) cannot be in or
teleport to the same server.

Note that this property is only valid on the server [DataModel](/docs/reference/engine/classes/DataModel.md) and
it will be the [MatchmakingType.Default](/docs/reference/engine/enums/MatchmakingType.md) value for all clients, so
only reference this property inside of a server‑side [Script](/docs/reference/engine/classes/Script.md).

### Property: DataModel.PlaceId

```json
{
  "type": "int64",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "State"
}
```

This property describes the ID of the place running on the server.

If the place has not been published to Roblox, this ID will correspond
with the template being used.

#### See Also

- [DataModel.GameId](/docs/reference/engine/classes/DataModel.md), which describes the ID of the experience that
  the current place belongs to
- [DataModel.JobId](/docs/reference/engine/classes/DataModel.md), which is a unique identifier for the server
  game instance running
- [TeleportService](/docs/reference/engine/classes/TeleportService.md), which is a service that can be used to
  transport [Players](/docs/reference/engine/classes/Player.md) between places

### Property: DataModel.PlaceVersion

```json
{
  "type": "int",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "State"
}
```

This property describes the version of the place the server is running on.

This version number corresponds with the version number shown under the
**Version History** section of the place's settings. It is not the current
version of the Roblox client. This property is 0 for all unpublished
experiences.

When a server instance is created for a place, it uses the place's current
version. If the place is later updated while this server is running, the
server will remain at its current version.

This property can be used to display a [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) showing the
current version of the game to [Players](/docs/reference/engine/classes/Player.md) to assist with
debugging.

**Server version number GUI**

This code sample will place a simple GUI in the `StarterGui` showing the place
version the server is running at.

To use this sample, place it inside a `Script` in `ServerScriptService`.

```lua
local StarterGui = game:GetService("StarterGui")

local versionGui = Instance.new("ScreenGui")

local textLabel = Instance.new("TextLabel")
textLabel.Position = UDim2.new(1, -10, 1, 0)
textLabel.AnchorPoint = Vector2.new(1, 1)
textLabel.Size = UDim2.new(0, 150, 0, 40)

textLabel.BackgroundTransparency = 1
textLabel.TextColor3 = Color3.new(1, 1, 1)
textLabel.TextStrokeTransparency = 0
textLabel.TextXAlignment = Enum.TextXAlignment.Right
textLabel.TextScaled = true

local placeVersion = game.PlaceVersion
textLabel.Text = string.format("Server version: %s", placeVersion)

textLabel.Parent = versionGui
versionGui.Parent = StarterGui
```

### Property: DataModel.PrivateServerId

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

This property describes the private server ID of the server, if the server
is a private server.

If the server is not a private server, then this property will be an empty
string.

#### Private servers

Private servers refer to the following:

- [VIP servers](/docs/en-us/production/monetization/private-servers.md),
  private servers that users can purchase from the games page.
- Reserved servers, private servers created by the developer using
  [TeleportService:TeleportAsync()](/docs/reference/engine/classes/TeleportService.md) with
  [TeleportOptions.ReservedServerId](/docs/reference/engine/classes/TeleportOptions.md).

#### PrivateServerId vs JobId

The PrivateServerId of a server is different from the
[DataModel.JobId](/docs/reference/engine/classes/DataModel.md). The [JobId](/docs/reference/engine/classes/DataModel.md) is the unique
identifier of the current server instance.

Private servers (private or reserved servers) can have multiple server
instances associated with them over time. This is because, although only
one server instance can be running at once for a private server, new
server instances can open and close as players join and leave the game.
For example, no server instance is running when nobody is playing in the
server. The PrivateServerId will be consistent across all of these server
instances, and the [DataModel.JobId](/docs/reference/engine/classes/DataModel.md) will be unique for each one.

See also:

- [DataModel.PrivateServerOwnerId](/docs/reference/engine/classes/DataModel.md), a property describing the owner
  of a private server
- [TeleportService:TeleportAsync()](/docs/reference/engine/classes/TeleportService.md), a function which can create a
  reserved server when used with [TeleportOptions.ReservedServerId](/docs/reference/engine/classes/TeleportOptions.md)

**Detecting Private Servers**

[DataModel.PrivateServerId](/docs/reference/engine/classes/DataModel.md) and [DataModel.PrivateServerOwnerId](/docs/reference/engine/classes/DataModel.md)
can be used to detect if the current server instance is a standard server, a
VIP server or a reserved server.

```lua
local function getServerType()
	if game.PrivateServerId ~= "" then
		if game.PrivateServerOwnerId ~= 0 then
			return "VIPServer"
		else
			return "ReservedServer"
		end
	else
		return "StandardServer"
	end
end

print(getServerType())
```

### Property: DataModel.PrivateServerOwnerId

```json
{
  "type": "int64",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

This property describes the [UserId](/docs/reference/engine/classes/Player.md) of the
[Player](/docs/reference/engine/classes/Player.md) that owns the
[VIP server](/docs/en-us/production/monetization/private-servers.md) if the
server is a VIP server.

If the server is a standard or reserved server then this property will be
set to `0`.

This property could be used to identify if a [Player](/docs/reference/engine/classes/Player.md) is the owner
of the private server, for example:

```lua
local Players = game:GetService("Players")

-- is this a private server?
if game.PrivateServerId ~= "" and game.PrivateServerOwnerId ~= 0 then

    -- listen for new players being added
    Players.PlayerAdded:Connect(function(player)

        -- check if the player is the server owner
        if player.UserId == game.PrivateServerOwnerId then
            print("The private server owner has joined the game")
        end
    end)
end
```

See also:

- [DataModel.PrivateServerId](/docs/reference/engine/classes/DataModel.md), a property describing the unique ID
  of VIP and reserved servers

**Detecting Private Servers**

[DataModel.PrivateServerId](/docs/reference/engine/classes/DataModel.md) and [DataModel.PrivateServerOwnerId](/docs/reference/engine/classes/DataModel.md)
can be used to detect if the current server instance is a standard server, a
VIP server or a reserved server.

```lua
local function getServerType()
	if game.PrivateServerId ~= "" then
		if game.PrivateServerOwnerId ~= 0 then
			return "VIPServer"
		else
			return "ReservedServer"
		end
	else
		return "StandardServer"
	end
end

print(getServerType())
```

### Property: DataModel.RunService

```json
{
  "type": "RunService",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

A reference to the [RunService](/docs/reference/engine/classes/RunService.md) service. Always points to
[RunService](/docs/reference/engine/classes/RunService.md) and is never `nil`. You can also retrieve it with
[GetService()](/docs/reference/engine/classes/ServiceProvider.md), for example
`game:GetService("RunService")`.

### Property: DataModel.Workspace

```json
{
  "type": "Workspace",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

This property is a reference to the [Workspace](/docs/reference/engine/classes/Workspace.md) service. It always
points to [Workspace](/docs/reference/engine/classes/Workspace.md) and will never be `nil`.

### Property: DataModel.GearGenreSetting

```json
{
  "type": "GearGenreSetting",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "State"
}
```

> **Deprecated:** This property is deprecated and is no longer functional. It should not be used.

This property, along with [DataModel.Genre](/docs/reference/engine/classes/DataModel.md), no longer functions
correctly and attempting to read it may throw an error.

### Property: DataModel.lighting

```json
{
  "type": "Instance",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

> **Deprecated:** This item has been superseded by [game:GetService("Lighting")](/docs/reference/engine/classes/ServiceProvider.md), which should be used instead.

This property was once used to get the game's [Lighting](/docs/reference/engine/classes/Lighting.md) service.

### Property: DataModel.workspace

```json
{
  "type": "Workspace",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

> **Deprecated:** This deprecated property is a variant of [DataModel.Workspace](/docs/reference/engine/classes/DataModel.md) which should be used instead.

### Property: DataModel.VIPServerId *(hidden)*

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

> **Deprecated:** This property has been deprecated. Use [DataModel.PrivateServerId](/docs/reference/engine/classes/DataModel.md) instead.

This property was string that could identify the current server as a
private server.

### Property: DataModel.VIPServerOwnerId *(hidden)*

```json
{
  "type": "int64",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

> **Deprecated:** This property has been deprecated. Use [DataModel.PrivateServerOwnerId](/docs/reference/engine/classes/DataModel.md) instead.

This property indicates the [UserId](/docs/reference/engine/classes/Player.md) of the account
who owns the private server.

## Methods

### Method: DataModel:BindToClose

**Signature:** `DataModel:BindToClose(function: Function): ()`

Binds a function to be called before the server shuts down. If the bound
function accepts a parameter, it passes [CloseReason](/docs/reference/engine/enums/CloseReason.md) specifying the
reason for the server shutdown.

You can bind multiple functions by calling
[BindToClose()](/docs/reference/engine/classes/DataModel.md) repeatedly. Bound functions
are called in parallel and run at the same time.

The experience server waits 30 seconds for all bound functions to stop
running before it shuts down. After 30 seconds, the server shuts down even
if functions are still running. Teleports are disabled during moderation
shutdowns.

To verify that the current session is not in Roblox Studio, use
[RunService:IsStudio()](/docs/reference/engine/classes/RunService.md). This prevents bound functions from
completing their run in offline testing sessions.

When you use [DataStoreService](/docs/reference/engine/classes/DataStoreService.md), you should also use `BindToClose`
to bind a function saving all unsaved data to
[DataStores](/docs/reference/engine/classes/GlobalDataStore.md). This prevents data loss if the server
shuts down unexpectedly.

See also:

- [CloseReason](/docs/reference/engine/enums/CloseReason.md) for reasons for the experience server shutdown.
- [PluginGui:BindToClose()](/docs/reference/engine/classes/PluginGui.md), which binds a function to a
  [PluginGui](/docs/reference/engine/classes/PluginGui.md) close button.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `function` | `Function` |  | A function called before the experience server shuts down. If the bound function accepts a parameter, it passes [CloseReason](/docs/reference/engine/enums/CloseReason.md) specifying the reason for the server shutdown. |

**Returns:** `()`

**Saving player data before shutting down**

The following code sample is an example of how [DataModel:BindToClose()](/docs/reference/engine/classes/DataModel.md)
can be used to save player data in the event of a server shutdown. In this
example, player data is stored in a dictionary named _playerData_ with
[UserIds](/docs/reference/engine/classes/Player.md) as keys.

```lua
local DataStoreService = game:GetService("DataStoreService")
local RunService = game:GetService("RunService")

local playerDataStore = DataStoreService:GetDataStore("PlayerData")

local allPlayerSessionDataCache = {}

local function savePlayerDataAsync(userId, data)
	return playerDataStore:UpdateAsync(userId, function(oldData)
		return data
	end)
end

local function onServerShutdown(closeReason)
	if RunService:IsStudio() then
		-- Avoid writing studio data to production and stalling test session closing
		return
	end

	-- Reference for yielding and resuming later
	local mainThread = coroutine.running()

	-- Counts up for each new thread, down when the thread finishes. When 0 is reached,
	-- the individual thread knows it's the last thread to finish and should resume the main thread
	local numThreadsRunning = 0

	-- Calling this function later starts on a new thread because of coroutine.wrap
	local startSaveThread = coroutine.wrap(function(userId, sessionData)
		-- Perform the save operation
		local success, result = pcall(savePlayerDataAsync, userId, sessionData)
		if not success then
			-- Could implement a retry
			warn(string.format("Failed to save %d's data: %s", userId, result))
		end

		-- Thread finished, decrement counter
		numThreadsRunning -= 1

		if numThreadsRunning == 0 then
			-- This was the last thread to finish, resume main thread
			coroutine.resume(mainThread)
		end
	end)

	-- This assumes playerData gets cleared from the data table during a final save on PlayerRemoving,
	-- so this is iterating over all the data of players still in the game that hasn't been saved
	for userId, sessionData in pairs(allPlayerSessionDataCache) do
		numThreadsRunning += 1

		-- This loop finishes running and counting numThreadsRunning before any of
		-- the save threads start because coroutine.wrap has built-in deferral on start
		startSaveThread(userId, sessionData)
	end

	if numThreadsRunning > 0 then
		-- Stall shutdown until save threads finish. Resumed by the last save thread when it finishes
		coroutine.yield()
	end
end

game:BindToClose(onServerShutdown)
```

**Binding to and Handling Game Shutdown**

The following example prints the close reason to the output. It prints `Done`
after three seconds, and then allows Roblox to shut down the experience
server.

The close reason matches one of the values in [CloseReason](/docs/reference/engine/enums/CloseReason.md).

```lua
game:BindToClose(function(closeReason)
	print(`Closing with reason {closeReason}`)
	task.wait(3)
	print("Done")
end)
```

### Method: DataModel:GetJobsInfo

**Signature:** `DataModel:GetJobsInfo(): Array`

Returns a table containing basic information about the jobs performed by
the task scheduler.

In computing, a task scheduler is a system responsible for executing key
tasks at the appropriate intervals.

You can also find live task scheduler statistics in the Task Scheduler
window in Roblox Studio.

The first entry in the table returned is a reference dictionary containing
the statistics (or headings) available. It is in the following format:

```lua
{
    ["name"] = "name",
    ["averageDutyCycle"] = "averageDutyCycle",
    ["averageStepsPerSecond"] = "averageStepsPerSecond",
    ["averageStepTime"] = "averageStepTime",
    ["averageError"] = "averageError",
    ["isRunning"] = "isRunning",
}
```

The subsequent entries in the table returned are dictionaries containing
the above statistics for jobs performed by the task scheduler. For
example:

```lua
{
    ["name"] = "Heartbeat",
    ["averageDutyCycle"] = 0,
    ["averageStepsPerSecond"] = 0,
    ["averageStepTime"] = 0,
    ["averageError"] = 0,
    ["isRunning"] = false,
}
```

See also:

- [TaskScheduler](/docs/reference/engine/classes/TaskScheduler.md)

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `Array` — A table containing information about the jobs performed by the task
scheduler, see above for the format.

**Getting Jobs Info**

Here is an example of iterating over the job info.

```lua
local jobInfo = game:GetJobsInfo()
local jobTitles = jobInfo[1]

table.remove(jobInfo, 1)

local divider = string.rep("-", 120)
print(divider)
warn("JOB INFO:")
print(divider)

for _, job in pairs(jobInfo) do
	for jobIndex, jobValue in pairs(job) do
		local jobTitle = jobTitles[jobIndex]
		warn(jobTitle, "=", jobValue)
	end
	print(divider)
end
```

### Method: DataModel:GetObjects

**Signature:** `DataModel:GetObjects(url: ContentId): Instances`

This method returns an array of [Instances](/docs/reference/engine/classes/Instance.md) associated with
the given content URL. It can be used to insert content from the Roblox
library. It's not possible to insert [Sounds](/docs/reference/engine/classes/Sound.md) using this
method as they do not have an [Instance](/docs/reference/engine/classes/Instance.md) associated with them and
have only a content URL.

Unlike [InsertService:LoadAsset()](/docs/reference/engine/classes/InsertService.md), `DataModel:GetObjects()` does
not require an asset to be "trusted," meaning that an asset doesn't need
to be owned by the logged in user, or created by Roblox, to be inserted.
However, if the asset is not owned by the logged in user it must be freely
available.

Due to this function's security context it can only be used by plugins or
the command bar. For an alternative that can be used in
[Scripts](/docs/reference/engine/classes/Script.md) and [LocalScripts](/docs/reference/engine/classes/LocalScript.md), see
[InsertService:LoadAsset()](/docs/reference/engine/classes/InsertService.md).

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `url` | `ContentId` |  | The given content URL. |

**Returns:** `Instances` — An array of [Instances](/docs/reference/engine/classes/Instance.md) associated with the content
URL.

**View a plugin's source code**

If you want to view a plugin's source code without installing it, you can use
[DataModel:GetObjects()](/docs/reference/engine/classes/DataModel.md) to download the plugin. The code sample below
includes a function that will take a plugin's website URL and insert the
plugin into the currently selected `Instance` or the `Workspace`.

Due to [GetObjects'](/docs/reference/engine/classes/DataModel.md) security context, this
function can only be used in the command line or in a plugin.

```lua
local Selection = game:GetService("Selection")

local WEB_URL = "plugin URL here"

local function downloadPlugin(webURL)
	-- get the content URL
	local contentID = string.match(webURL, "%d+")
	local contentURL = "rbxassetid://" .. contentID

	-- download the objects
	local objects = game:GetObjects(contentURL)

	-- decide where to parent them
	local selection = Selection:Get()
	local parent = #selection == 1 and selection[1] or workspace

	-- parent the objects
	for _, object in pairs(objects) do
		object.Parent = parent
	end
end

downloadPlugin(WEB_URL)
```

**Batch convert decal IDs**

The content ID of a `Decal` on the Roblox website is associated with a `Decal`
`Instance` rather than the actual content ID of the texture.

The code below, will use [DataModel:GetObjects()](/docs/reference/engine/classes/DataModel.md) to insert `Decal`
objects into place and read their [Decal.ColorMapContent](/docs/reference/engine/classes/Decal.md) property to
obtain the image content IDs.

To use this code sample, enter the web URLs of the decals you'd like to
convert into the array named _IMAGES_ (as strings). A dictionary with the
converted textures will be outputted.

```lua
local IMAGES = {
	-- Insert Decal web URLs in an array here (as strings)
}

-- open the dictionary
local outputString = "textures = {"

-- utility function to add a new entry to the dictionary (as a string)
local function addEntryToDictionary(original, new)
	outputString = outputString
		.. "\n" -- new line
		.. "    " -- indent
		.. '["'
		.. original
		.. '"]' -- key
		.. ' = "'
		.. new
		.. '",' -- value
end

print("Starting conversion")

for _, webURL in pairs(IMAGES) do
	-- get the content URL
	local contentID = string.match(webURL, "%d+")
	local contentURL = "rbxassetid://" .. contentID

	local success, result = pcall(function()
		local objects = game:GetObjects(contentURL)
		return objects[1].Texture
	end)

	if success then
		addEntryToDictionary(webURL, result)
	else
		addEntryToDictionary(webURL, "Error downloading decal")
	end

	task.wait()
end

print("Conversion complete")

-- close the dictionary
outputString = outputString .. "\n}"

-- print the dictionary
print(outputString)
```

**Expected output:** Starting conversion
Conversion complete
textures = {
-- a dictionary with the original web URLs as keys, and the texture content IDs as values
}

### Method: DataModel:IsLoaded

**Signature:** `DataModel:IsLoaded(): boolean`

When all initial [Instances](/docs/reference/engine/classes/Instance.md) in the game have finished
replicating to the client, this function returns true.

Unless they are parented to [ReplicatedFirst](/docs/reference/engine/classes/ReplicatedFirst.md),
[LocalScripts](/docs/reference/engine/classes/LocalScript.md) do not run until the game has loaded. The
following snippet, run from a [LocalScript](/docs/reference/engine/classes/LocalScript.md) in
[ReplicatedFirst](/docs/reference/engine/classes/ReplicatedFirst.md) yields until the game has loaded:

```lua
if not game:IsLoaded() then
    game.Loaded:Wait()
end
```

See also:

- [Replication order](/docs/en-us/scripting/attributes.md#replication-order)
  for a more detailed summary of the loading process.
- [DataModel.Loaded](/docs/reference/engine/classes/DataModel.md), an event that fires when the game has loaded
- [Instance:WaitForChild()](/docs/reference/engine/classes/Instance.md), a function which can be used to wait
  for an individual [Instance](/docs/reference/engine/classes/Instance.md) to replicate without having to wait
  for the whole game to finish loading.

*Security: None · Thread Safety: Unsafe*

**Returns:** `boolean` — Whether the client has finished loading the game for the first time.

**Custom Loading Screen**

This sample demonstrates a custom loading screen with a basic `TextLabel`. The
code should be placed in a `LocalScript` within `ReplicatedFirst`. To expand
on this sample with loading screen animations, see the
[`Custom Loading Screens`](/docs/en-us/ui/customizing-loading-screens.md)
article.

```lua
local Players = game:GetService("Players")
local ReplicatedFirst = game:GetService("ReplicatedFirst")

local player = Players.LocalPlayer
local playerGui = player:WaitForChild("PlayerGui")

-- Create a basic loading screen
local screenGui = Instance.new("ScreenGui")
screenGui.IgnoreGuiInset = true

local textLabel = Instance.new("TextLabel")
textLabel.Size = UDim2.new(1, 0, 1, 0)
textLabel.BackgroundColor3 = Color3.fromRGB(0, 20, 40)
textLabel.Font = Enum.Font.GothamMedium
textLabel.TextColor3 = Color3.new(0.8, 0.8, 0.8)
textLabel.Text = "Loading"
textLabel.TextSize = 28
textLabel.Parent = screenGui

-- Parent entire screen GUI to player GUI
screenGui.Parent = playerGui

-- Remove the default loading screen
ReplicatedFirst:RemoveDefaultLoadingScreen()

--task.wait(3)  -- Optionally force screen to appear for a minimum number of seconds
if not game:IsLoaded() then
	game.Loaded:Wait()
end
screenGui:Destroy()
```

### Method: DataModel:SetPlaceId

**Signature:** `DataModel:SetPlaceId(placeId: int64): ()`

This function sets the [DataModel.PlaceId](/docs/reference/engine/classes/DataModel.md) of the game instance to
the given `placeId`.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `placeId` | `int64` |  | The ID to set the [DataModel.PlaceId](/docs/reference/engine/classes/DataModel.md) to. |

**Returns:** `()`

### Method: DataModel:SetUniverseId

**Signature:** `DataModel:SetUniverseId(universeId: int64): ()`

This function sets the [DataModel.GameId](/docs/reference/engine/classes/DataModel.md) of the current game
instance to the given `universeId`. This is useful when testing local
.rbxl files that have not been published to Roblox.

To access the [DataStoreService](/docs/reference/engine/classes/DataStoreService.md) in an unpublished place, both
[DataModel:SetUniverseId()](/docs/reference/engine/classes/DataModel.md) and [DataModel:SetPlaceId()](/docs/reference/engine/classes/DataModel.md) must
be set.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `universeId` | `int64` |  | The ID to set the [DataModel.GameId](/docs/reference/engine/classes/DataModel.md) to. |

**Returns:** `()`

### Method: DataModel:GetMessage

**Signature:** `DataModel:GetMessage(): string`

> **Deprecated:** This item is deprecated since the system was phased out a very long time ago, and recently the APIs for setting this message were removed.

This function will always return a blank string. It was originally used to
set the message displayed on screen while the game was loading.

This system was phased out a very long time ago, and recently the APIs for
setting this message were removed.

*Security: None · Thread Safety: Unsafe*

**Returns:** `string`

### Method: DataModel:GetRemoteBuildMode

**Signature:** `DataModel:GetRemoteBuildMode(): boolean`

> **Deprecated:** This item is deprecated. Use [RunService:IsServer()](/docs/reference/engine/classes/RunService.md) to see if your code is running on the server.

This method is no longer useful and will always return false. Use
[RunService:IsServer()](/docs/reference/engine/classes/RunService.md) to see if your code is running on the
server.

*Security: None · Thread Safety: Unsafe*

**Returns:** `boolean`

### Method: DataModel:IsGearTypeAllowed

**Signature:** `DataModel:IsGearTypeAllowed(gearType: GearType): boolean`

> **Deprecated:** This property is deprecated and is no longer functional. It should not be used.

Currently this function only returns the correct value on the client

This function returns whether gear of the given [GearType](/docs/reference/engine/enums/GearType.md) is
permitted to be added to [Players'](/docs/reference/engine/classes/Player.md)
[StarterGears](/docs/reference/engine/classes/StarterGear.md). For example:

```lua
local meleeWeaponsAllowed = game:IsGearTypeAllowed(Enum.GearType.MeleeWeapons)
```

Whether gear of a specific [GearType](/docs/reference/engine/enums/GearType.md) is permitted in the game is
determined in a place's settings page under 'Permissions'. Note, all of a
gear's associated [GearTypes](/docs/reference/engine/enums/GearType.md) must be enabled for it to be
permitted in a place.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `gearType` | `GearType` |  | The given [GearType](/docs/reference/engine/enums/GearType.md). |

**Returns:** `boolean` — Whether gear of the given [GearType](/docs/reference/engine/enums/GearType.md) is permitted in the game.

### Method: DataModel:SavePlace

**Signature:** `DataModel:SavePlace(saveFilter?: SaveFilter): boolean`

> **Deprecated:** This item is deprecated. Do not use it for new work.

This function was used by an ancient data persistence method to save the
current place.

Note:

- In order for this method to work the save place API has to be enabled
  for the current place.

*Yields · Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `saveFilter` | `SaveFilter` | `SaveAll` |  |

**Returns:** `boolean`

## Events

### Event: DataModel.GraphicsQualityChangeRequest

**Signature:** `DataModel.GraphicsQualityChangeRequest(betterQuality: boolean)`

Fires when the user prompts an increase or decrease in graphics quality
using the hotkeys.

This event fires under the following conditions:

- If the user presses <kbd>F10</kbd>, this event fires with a
  `betterQuality` argument of `true`.
- If the user presses <kbd>Shift</kbd><kbd>F10</kbd>, this event fires
  with a `betterQuality` argument of `false`.

This event does not provide the current graphics quality level or cover
all updates to the graphics quality. For example, changes made in the core
GUI escape menu are not registered.

You can retrieve a user's [SavedQualitySetting](/docs/reference/engine/enums/SavedQualitySetting.md) using
[UserGameSettings](/docs/reference/engine/classes/UserGameSettings.md) with the following snippet:

```lua
UserSettings():GetService("UserGameSettings").SavedQualityLevel
```

If the user's graphics settings are set to automatic then the
[SavedQualitySetting](/docs/reference/engine/enums/SavedQualitySetting.md) will be
[Automatic](/docs/reference/engine/enums/SavedQualitySetting.md). There is currently no way
for developers to reliably get the current graphics quality level of a
user's machine.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `betterQuality` | `boolean` | Whether the user has prompted an increase (_true_) or a decrease (_false_) in graphics quality. |

**Handling User Changes in Graphics Quality**

```lua
game.GraphicsQualityChangeRequest:Connect(function(betterQuality)
	if betterQuality then
		print("The user has requested an increase in graphics quality!")
	else
		print("The user has requested a decrease in graphics quality!")
	end
end)
```

### Event: DataModel.Loaded

**Signature:** `DataModel.Loaded()`

This event fires on the client when all initial [Instances](/docs/reference/engine/classes/Instance.md)
in the game have finished replicating to the client.

Unless they are parented to [ReplicatedFirst](/docs/reference/engine/classes/ReplicatedFirst.md),
[LocalScripts](/docs/reference/engine/classes/LocalScript.md) do not run until the game has loaded. The
following snippet, run from a [LocalScript](/docs/reference/engine/classes/LocalScript.md) in
[ReplicatedFirst](/docs/reference/engine/classes/ReplicatedFirst.md) yields until the game has loaded:

```lua
if not game:IsLoaded() then
    game.Loaded:Wait()
end
```

See also:

- [Replication order](/docs/en-us/scripting/attributes.md#replication-order)
  for a more detailed summary of the loading process.
- [DataModel.Loaded](/docs/reference/engine/classes/DataModel.md), an event that fires when the game has loaded
- [Instance:WaitForChild()](/docs/reference/engine/classes/Instance.md), a function which can be used to wait
  for an individual [Instance](/docs/reference/engine/classes/Instance.md) to replicate without having to wait
  for the whole game to finish loading.

*Security: None*

### Event: DataModel.ServerRestartScheduled

**Signature:** `DataModel.ServerRestartScheduled(restartTime: DateTime, source: CloseReason, attributes: Dictionary)`

Fires when the server has been scheduled to restart, for example when you
restart servers from the Creator Hub or
[Open Cloud](https://create.roblox.com/docs/cloud/reference/features/universes#Restarts_LaunchRestart)
to [release an experience update](/docs/en-us/projects/update-games.md), or
when Roblox needs to restart servers for infrastructure maintenance.

You can use this event to inform players on the server of the impending
restart. You could then let them save their progress or teleport them to
updated servers at the most convenient time for your game.

*Security: None · Capabilities: ServerCommunication*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `restartTime` | `DateTime` | A [DateTime](/docs/reference/engine/datatypes/DateTime.md) indicating when the server is scheduled to shut down. The actual restart may happen slightly after this projected time, but not before. |
| `source` | `CloseReason` | An [CloseReason](/docs/reference/engine/enums/CloseReason.md) describing what triggered the restart. The value will be [CloseReason.DeveloperUpdate](/docs/reference/engine/enums/CloseReason.md) for experience updates, and [CloseReason.RobloxMaintenance](/docs/reference/engine/enums/CloseReason.md) for server maintenance updates. |
| `attributes` | `Dictionary` | A dictionary of developer-supplied metadata associated with the restart. If no attributes are provided, then this will be an empty table. |

**ServerRestartScheduled**

Connects a callback to the `ServerRestartScheduled` event to teleport players
to an updated game server before the scheduled restart when there is a break
in between game rounds.

```lua
local roundInProgress = false -- Set elsewhere in game code whenever a game round starts or ends
local restartPending = false

game.ServerRestartScheduled:Connect(function(restartTime, source, attributes)
	local msg = attributes and attributes.message or ""
	local timeStr = restartTime:FormatLocalTime("LTS", "en-us") -- since this is run on the server, it will be in UTC
	-- Forward these fields to clients via remote:FireAllClients() to display customized messages in your UI
	print(string.format("Server restart at %s from source: %s. Reason: %s.", timeStr, tostring(source), msg))
	if not roundInProgress then
		print("No round in progress. Teleporting players in 10 seconds")
		task.wait(10)
		-- Teleporting players when a restart has been scheduled will bring them to a server on the latest place version
		game:GetService("TeleportService"):TeleportAsync(game.PlaceId, game:GetService("Players"):GetPlayers())
	else
		-- You can add code to teleport players after a game round ends if restartPending is true.
		restartPending = true
	end
end)
```

### Event: DataModel.AllowedGearTypeChanged

**Signature:** `DataModel.AllowedGearTypeChanged()`

> **Deprecated:** This item is deprecated . Do not use it for new work.

This event fires when SetGearSettings is called with a different value for
`allowedGenres`.

*Security: None*

### Event: DataModel.ItemChanged

**Signature:** `DataModel.ItemChanged(object: Instance, descriptor: string)`

> **Deprecated:** This function has been superseded by [Object.Changed](/docs/reference/engine/classes/Object.md), which should be used in new work instead.

This event fires when a property of any object in the [DataModel](/docs/reference/engine/classes/DataModel.md) is
changed.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `object` | `Instance` |  |
| `descriptor` | `string` |  |

**DataModel.ItemChanged**

```lua
game.ItemChanged:Connect(function(item, property)
	print(string.format("%s.%s has changed", item.Name, property))
end)

--> Workspace.DistributedGameTime has changed
```

## Callbacks

### Callback: DataModel.OnClose

**Signature:** `DataModel.OnClose(): Tuple`

> **Deprecated:** This function is deprecated. It is recommended to use [DataModel:BindToClose()](/docs/reference/engine/classes/DataModel.md) instead.

Invoked before the game is shut down. When this callback returns, or the
timeout period is hit, the game finishes shutting down.

*Security: None · Thread Safety: Unsafe*

**Returns:** `Tuple`

**DataModel.OnClose1**

The example below would print "Closing, waiting" to the output. It would wait
three seconds and then print "Done". At this point Roblox will be able to shut
down the server.

```lua
game.OnClose = function()
	print("Closing, waiting")
	task.wait(3)
	print("Done")
end
```

## Inherited Members

### From [ServiceProvider](/docs/reference/engine/classes/ServiceProvider.md)

- **Method `FindService(className: string): Instance`**: Returns the service specified by the given className if it's already
- **Method `GetService(className: string): Instance`**: Returns the service with the requested class name, creating it if it does
- **Method `getService(className: string): Instance`**:  *(deprecated)*
- **Method `service(className: string): Instance`**:  *(deprecated)*
- **Event `Close`**: Fires when the current place is exited.
- **Event `ServiceAdded`**: Fired when a service is created.
- **Event `ServiceRemoving`**: Fired when a service is about to be removed.

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