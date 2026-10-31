---
name: Players
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "A service that contains presently connected Player objects."
---

# Class: Players

> A service that contains presently connected [Player](/docs/reference/engine/classes/Player.md) objects.

## Description

The [Players](/docs/reference/engine/classes/Players.md) service contains [Player](/docs/reference/engine/classes/Player.md) objects for presently
connected clients to a Roblox server. It also contains information about a
place's configuration. It can fetch information about players not connected to
the server, such as character appearances, friends, and avatar thumbnail.

## Properties

### Property: Players.BanningEnabled

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Players",
    "PluginOrOpenCloud"
  ]
}
```

Enables or disables the three [Players](/docs/reference/engine/classes/Players.md) methods
([BanAsync()](/docs/reference/engine/classes/Players.md),
[UnbanAsync()](/docs/reference/engine/classes/Players.md), and
[GetBanHistoryAsync()](/docs/reference/engine/classes/Players.md)) that constitute
the ban API. This property cannot be set through developer-facing Luau and
must be set in Studio through the Players properties window.

### Property: Players.BubbleChat

```json
{
  "type": "boolean",
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
  "category": "Data",
  "capabilities": [
    "Chat",
    "Players"
  ]
}
```

This property indicates whether or not bubble chat is enabled. It is set
with the [Players:SetChatStyle()](/docs/reference/engine/classes/Players.md) method using the [ChatStyle](/docs/reference/engine/enums/ChatStyle.md)
enum.

When this chat mode is enabled, the experience displays chats in the chat
user interface at the top-left corner of the screen.

There are two other chat modes, [Players.ClassicChat](/docs/reference/engine/classes/Players.md) and a chat
mode where both classic and bubble chat are enabled.

### Property: Players.CharacterAutoLoads

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Players"
  ]
}
```

This property indicates whether [characters](/docs/reference/engine/classes/Player.md) will
respawn automatically. The default value is true.

If this property is disabled (false), player
[characters](/docs/reference/engine/classes/Player.md) will not spawn until the
[Player:LoadCharacterAsync()](/docs/reference/engine/classes/Player.md) function is called for each
[Player](/docs/reference/engine/classes/Player.md), including when players join the experience.

This can be useful in experiences where players have finite lives, such as
competitive experiences in which players do not respawn until a round
ends.

**Player Respawn Timer**

This example demonstrates one possible usage of the
[Players.CharacterAutoLoads](/docs/reference/engine/classes/Players.md) property.

The example below respawns all players in the game, if dead, once every 10
seconds. This means that players who die 1 second after all players respawn
must wait 9 seconds until the script loads all [Player.Character](/docs/reference/engine/classes/Player.md) again.

First, this script removes a player's character when they die and the
[Humanoid.Died](/docs/reference/engine/classes/Humanoid.md) function fires. This is done so that the respawn loop
that executes every 10 seconds reloads that player when it does not find the
player's character in the Workspace.

To work as expected, this example should be run within a `Script`.

```lua
local Players = game:GetService("Players")

-- Set CharacterAutoLoads to false
Players.CharacterAutoLoads = false

-- Remove player's character from workspace on death
Players.PlayerAdded:Connect(function(player)
	while true do
		local char = player.CharacterAdded:Wait()
		char.Humanoid.Died:Connect(function()
			char:Destroy()
		end)
	end
end)

-- Respawn all dead players once every 10 seconds
while true do
	local players = Players:GetChildren()

	-- Check if each player is dead by checking if they have no character, if dead load that player's character
	for _, player in pairs(players) do
		if not workspace:FindFirstChild(player.Name) then
			player:LoadCharacterAsync()
		end
	end

	-- Wait 10 seconds until next respawn check
	task.wait(10)
end
```

### Property: Players.ClassicChat

```json
{
  "type": "boolean",
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
  "category": "Data",
  "capabilities": [
    "Chat",
    "Players"
  ]
}
```

Indicates whether or not classic chat is enabled. This property is set by
the [Players:SetChatStyle()](/docs/reference/engine/classes/Players.md) method using the [ChatStyle](/docs/reference/engine/enums/ChatStyle.md) enum.

When this chat mode is enabled, the experience displays chats in a bubble
above the sender's head.

There are two other chat modes, [Players.BubbleChat](/docs/reference/engine/classes/Players.md) and a chat mode
where both classic and bubble chat are enabled.

### Property: Players.LocalPlayer

```json
{
  "type": "Player",
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
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

This read-only property refers to the [Player](/docs/reference/engine/classes/Player.md) whose client is
running the experience.

This property is only defined for [LocalScripts](/docs/reference/engine/classes/LocalScript.md) and
[ModuleScripts](/docs/reference/engine/classes/ModuleScript.md) required by them, since they run on the
client. For the server, on which [Script](/docs/reference/engine/classes/Script.md) objects run their code,
this property is `nil`.

### Property: Players.MaxPlayers

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
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

This property determines the maximum number of players that can be in a
server. This property can only be set through a specific place's settings
on the [Creator Dashboard](https://create.roblox.com/dashboard/creations).

### Property: Players.PreferredPlayers

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
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

This property indicates the number of players to which Roblox's matchmaker
will fill servers. This number will be less than the maximum number of
players ([Players.MaxPlayers](/docs/reference/engine/classes/Players.md)) supported by the experience.

### Property: Players.RespawnTime

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

This property controls the time, in seconds, it takes for a player to
respawn when [Players.CharacterAutoLoads](/docs/reference/engine/classes/Players.md) is true. It defaults to
5.0 seconds.

This is useful when you want to change how long it takes to respawn based
on the type of your experience but don't want to handle spawning players
individually.

Although this property can be set from within a [Script](/docs/reference/engine/classes/Script.md), you can
more easily set it directly on the [Players](/docs/reference/engine/classes/Players.md) object in Studio's
[Explorer](/docs/en-us/studio/explorer.md) window.

### Property: Players.UseStrafingAnimations

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Players",
    "PluginOrOpenCloud"
  ]
}
```

When enabled, R15 character [Humanoids](/docs/reference/engine/classes/Humanoid.md) play directional
locomotion animations, strafing sideways and backpedaling while keeping
their current facing direction instead of rotating to face whichever
direction they move. When disabled, characters turn to face their
direction of movement. Defaults to `false`.

This property cannot be set through developer-facing Luau and must be set
in Studio through the [Players](/docs/reference/engine/classes/Players.md) properties window.

### Property: Players.NumPlayers

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

> **Deprecated:** This item is deprecated. Instead, of using this item, you should count the number of players returned by [Players:GetPlayers()](/docs/reference/engine/classes/Players.md).

This property indicates the number of people in the server at the current
time. It is read only. Meaning it cannot be written to, only read.

### Property: Players.localPlayer *(hidden)*

```json
{
  "type": "Player",
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
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

> **Deprecated:** This property is a deprecated variant of [Players.LocalPlayer](/docs/reference/engine/classes/Players.md) which should be used instead.

### Property: Players.numPlayers *(hidden)*

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

> **Deprecated:** This property is a deprecated variant of [Players.NumPlayers](/docs/reference/engine/classes/Players.md) which has also been deprecated. Neither property should be used in new work. Instead, you should count the number of players returned by [Players:GetPlayers()](/docs/reference/engine/classes/Players.md).

This property indicates the number of people in the server at the current
time. It is read only. Meaning it cannot be written to, only read.

## Methods

### Method: Players:BanAsync

**Signature:** `Players:BanAsync(config: Dictionary): ()`

The [Players:BanAsync()](/docs/reference/engine/classes/Players.md) method allows you to easily ban users who
violate your experience's guidelines. You can specify the ban duration,
enable the ban to propagate to suspected alternate accounts, enable the
ban to temporarily block the banned user's device from rejoining the
experience, and provide a message to the banned user in accordance with
the [Usage Guidelines](/docs/en-us/players.md#ban-users). You should
also post your experience rules somewhere accessible to all users and
provide a way for them to appeal. This method is enabled and disabled by
the [Players.BanningEnabled](/docs/reference/engine/classes/Players.md) property, which you can toggle in
Studio.

#### Banning and Messaging

Banned users will be immediately evicted and prevented from rejoining your
experiences. They will be presented with an error modal displaying the
time left on their ban and your `DisplayReason`. Roblox's backend systems
will evict players across all servers from the place(s) that you specify.
`DisplayReason` can have a maximum length of 400 characters and is subject
to a text filter. For more information on acceptable modal text, see
[ban messaging](/docs/en-us/players.md#message-guidelines).

#### Places and Universe

By default, bans extend to any place within that universe. To limit the
ban to only the place from which this API is called, configure
`ApplyToUniverse` to `false`. However, if a user is banned in the start
place of the universe, it effectively results in the user being excluded
from the entirety of the universe, irrespective of whether a universal ban
is in place or not.

#### Alternative Accounts

Users often play under multiple different accounts, known as alternate
accounts, which are sometimes used to circumvent account bans. To help you
keep banned users out, the default behavior of this API will propagate all
bans from the source account you banned to any of their suspected
alternate accounts. You can turn off ban propagations to alternate
accounts by configuring `ExcludeAltAccounts` to `true`.

#### Device Blocks

To help address disruptive users who circumvent alternate account
detection, set `ApplyDeviceBlock` to `true`. This blocks the banned user's
device from rejoining the experience for 24 hours after the ban is
applied.

#### Ban Duration

Not all transgressions are the same, so not all bans should be the same
length. This API lets you configure the duration of the ban, in seconds,
with the `Duration` field. To specify a permanent ban, set the field to
`-1`. You may also want to dynamically configure the ban duration based on
the user's ban history, which you can query for using
[Players:GetBanHistoryAsync()](/docs/reference/engine/classes/Players.md). For example, you may want to
consider the number of bans, the duration of previous bans, or build logic
off of the notes you save under `PrivateReason` which can be up to 1000
characters and are not text filtered. `PrivateReason` notes are never
shared with the client and can be considered safe from attackers.

#### Errors and Throttling

This method invokes an HTTP call to backend services which are subject to
throttling and may fail. If you're calling this API with more than one
[UserId](/docs/reference/engine/classes/Player.md), this method will attempt to make the HTTP
call for each ID. It will then aggregate any error messages and join them
as a comma separated list. For example, if this method is invoked for five
users and requests for those with [UserIds](/docs/reference/engine/classes/Player.md) 2 and 4
fail, the following error message appears:

`HTTP failure for UserId 2: Timedout, HTTP 504 (Service unavailable) failure for UserId 4: Service exception`

The message will always include `failure for UserId {}` if it is an HTTP
error.

#### Client-Side Requirement

Because of the risks associated with banning users, this method may only
be called on the backend experience server (client-side calls will result
in an error). You may test this API in Studio, during
[collaborative](/docs/en-us/projects/collaboration.md) creation, or in a
[team test](/docs/en-us/studio/testing-modes.md#collaborative-testing), but
the bans will not apply to production.

This API uses the
[User Restrictions Open Cloud API](/docs/en-us/cloud/reference/UserRestriction.md). You
will be able to utilize these APIs to manage your bans in third party
applications.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, Consequences*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `config` | `Dictionary` |  | - `UserIds` (required; array) — Array of [UserIds](/docs/reference/engine/classes/Player.md)   of players to be banned. Max size is `50`.  - `ApplyToUniverse` (optional; boolean) — Whether ban propagates to   all places within the experience universe. Default is `true`.  - `Duration` (required; integer) — Duration of the ban, in seconds.   Permanent bans should have a value of `-1`. `0` and all other   negative values are invalid.  - `DisplayReason` (required; string) — The message that will be   displayed to users when they attempt to and fail to join an   experience. Maximum string length is `400`.  - `PrivateReason` (required; string) — Internal messaging that will be   returned when querying the user's ban history. Maximum string length   is `1000`.  - `ExcludeAltAccounts` (optional; boolean) — When `true`, Roblox does   not attempt to ban alternate accounts. Default is `false`.  - `ApplyDeviceBlock` (optional; boolean) — When `true`, Roblox will   block banned users' devices from rejoining the experience for 24   hours after the ban is applied. Default is `false`. The block can be   overridden by unbanning a user via a call to   [Players:UnbanAsync()](/docs/reference/engine/classes/Players.md). Note that unbanning a user through any   other method will not lift the device block. |

**Returns:** `()`

**Banning Users**

The following example bans a user with a duration calculated from their ban
history, scoped to the entire universe and all of the user's alternate
accounts.

```lua
local Players = game:GetService("Players")

if shouldBeBanned(player) then
	local banHistoryPages = Players:GetBanHistoryAsync(player.UserId)
	local duration = 86400 -- 24 hours in seconds. Recommendation: use your own logic based off of user's BanHistory
	local config: BanConfigType = {
		UserIds = { player.UserId },
		Duration = duration,
		DisplayReason = "You violated community guideline #5",
		PrivateReason = "Put anything here that the user should not know but is helpful for your records",
		ExcludeAltAccounts = false,
		ApplyToUniverse = true,
	}

	local success, err = pcall(function()
		return Players:BanAsync(config)
	end)
	print(success, err)
end
```

### Method: Players:Chat

**Signature:** `Players:Chat(message: string): ()`

This function makes the local player chat the given message. Since this
item is protected, attempting to use it in a [Script](/docs/reference/engine/classes/Script.md) or
[LocalScript](/docs/reference/engine/classes/LocalScript.md) will cause an error.

Instead, when creating a custom chat system, or a system that needs access
to the chat, you can use the [Chat](/docs/reference/engine/classes/Chat.md) service's [Chat:Chat()](/docs/reference/engine/classes/Chat.md)
function instead.

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `string` |  | The message chatted. |

**Returns:** `()`

**Players:Chat**

This example demonstrates that the [Players:Chat()](/docs/reference/engine/classes/Players.md) function executes
without error if using the Command Bar or a Plugin (assuming the local player
can chat freely) and errors if executed in a `Script`.

```lua
-- Command bar
game:GetService("Players"):Chat("Hello, world!") --Results in 'Hello, world!' appearing in the Chat log under your Player's name.

-- Script
local Players = game:GetService("Players")
Players:Chat("Hello, world!") --Errors
```

### Method: Players:CreateHumanoidModelFromDescriptionAsync

**Signature:** `Players:CreateHumanoidModelFromDescriptionAsync(description: HumanoidDescription, rigType: HumanoidRigType, assetTypeVerification?: AssetTypeVerification): Model`

Returns a character [Model](/docs/reference/engine/classes/Model.md) equipped with everything specified in
the passed in [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md), and is R6 or R15 as specified
by `rigType`.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance, Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `description` | `HumanoidDescription` |  | Specifies the appearance of the returned character. |
| `rigType` | `HumanoidRigType` |  | Specifies whether the returned character will be R6 or R15. |
| `assetTypeVerification` | `AssetTypeVerification` | `Default` | The asset type verification mode. |

**Returns:** `Model` — A [Humanoid](/docs/reference/engine/classes/Humanoid.md) character [Model](/docs/reference/engine/classes/Model.md).

**Create Humanoid Model From Description**

This code sample creates a Humanoid Model from the passed in
HumanoidDescription and parents the Model to the Workspace.

```lua
game.Players:CreateHumanoidModelFromDescriptionAsync(Instance.new("HumanoidDescription"), Enum.HumanoidRigType.R15).Parent =
	game.Workspace
```

**Expected output:** When run, a Model is created and parented to the Workspace.

### Method: Players:CreateHumanoidModelFromUserIdAsync

**Signature:** `Players:CreateHumanoidModelFromUserIdAsync(userId: User): Model`

Returns a character Model set-up with everything equipped to match the
avatar of the user specified by the passed in userId. This includes
whether that character is currently R6 or R15.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The userId for a Roblox user. (The UserId is the number in the profile of the user e.g www.roblox.com/users/1/profile). |

**Returns:** `Model` — A Humanoid character Model.

**Create Humanoid Model From A User ID**

This code sample creates a Humanoid Model to match the avatar of the passed in
User ID, and parents the Model to the Workspace.

```lua
game.Players:CreateHumanoidModelFromUserIdAsync(1).Parent = game.Workspace
```

**Expected output:** When run, a Model is created and parented to the Workspace.

### Method: Players:GetBanHistoryAsync

**Signature:** `Players:GetBanHistoryAsync(userId: User): BanHistoryPages`

Retrieves the ban and unban history of any user within the experience's
universe. This method returns a [BanHistoryPages](/docs/reference/engine/classes/BanHistoryPages.md) instance that
inherits from [Pages](/docs/reference/engine/classes/Pages.md). This method is enabled and disabled by the
[Players.BanningEnabled](/docs/reference/engine/classes/Players.md) property, which you can toggle in Studio.

This function call will only succeed on production servers and not on
client devices or in Studio.

This API uses the
[User Restrictions Open Cloud API](/docs/en-us/cloud/reference/UserRestriction.md). You
will be able to utilize these APIs to manage your bans in third party
applications.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, Consequences*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the player whose ban history to retrieve. |

**Returns:** `BanHistoryPages` — See [BanHistoryPages](/docs/reference/engine/classes/BanHistoryPages.md) for return reference.

### Method: Players:GetCharacterAppearanceInfoAsync

**Signature:** `Players:GetCharacterAppearanceInfoAsync(userId: User): Dictionary`

This function returns information about a player's avatar on the Roblox
website in the form of a dictionary. It is not to be confused with
[GetCharacterAppearanceAsync](/docs/reference/engine/classes/Players.md),
which actually loads the assets described by this method. You can use
[InsertService:LoadAsset()](/docs/reference/engine/classes/InsertService.md) to load the assets that are used in the
player's avatar. The structure of the returned dictionary is as follows:

| Name | Type | Description |
| --- | --- | --- |
| `assets` | table (see below) | Describes the equipped assets (hats, body parts, etc) |
| `bodyColors` | table (see below) | Describes the BrickColor values for each limb |
| `bodyColor3s` | table (see below) | Describes the Color3 instance for each limb which may not match perfectly with bodyColors |
| `defaultPantsApplied` | bool | Describes whether default pants are applied |
| `defaultShirtApplied` | bool | Describes whether default shirt is applied |
| `emotes` | table (see below) | Describes the equipped emote animations |
| `playerAvatarType` | string | Either "R15" or "R6" |
| `scales` | table (see below) | Describes various body scaling factors |

#### Assets Sub-Table

The `assets` table is an array of tables containing the following keys
that describe the assets currently equipped by the player:

| Name | Type | Description |
| --- | --- | --- |
| `id` | number | The asset ID of the equipped asset |
| `assetType` | table | A table with `name` and `id` fields, each describing the kind of asset equipped ("Hat", "Face", etc.) |
| `name` | string | The name of the equipped asset |

#### Scales Sub-Table

The `scales` table has the following keys, each a number corresponding to
one [Humanoid](/docs/reference/engine/classes/Humanoid.md) scaling property: `bodyType`, `head`, `height`,
`proportion`, `depth`, `width`.

#### Body Colors Sub-Table

The `bodyColors` table has the following keys, each a number corresponding
to a [BrickColor](/docs/reference/engine/datatypes/BrickColor.md) ID number which can be used with
[BrickColor.new(id)](/docs/reference/engine/datatypes/BrickColor.md): `leftArmColorId`, `torsoColorId`,
`rightArmColorId`, `headColorId`, `leftLegColorId`, `rightLegColorId`.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The \*_userId_ of the specified player. |

**Returns:** `Dictionary` — A dictionary containing information about the character appearance of
a given user.

**Example Return Character Appearance Dictionary**

Sometimes it is best to see an example of the returned dictionary structure in
pure Lua. Here is one such example of a player whose avatar uses a package and
wears several hats. Can you guess who it is?

```lua
local result = {
	playerAvatarType = "R15",
	defaultPantsApplied = false,
	defaultShirtApplied = false,
	scales = {
		bodyType = 0,
		head = 1,
		height = 1.05,
		proportion = 0,
		depth = 0.92,
		width = 0.85,
	},
	bodyColors = {
		leftArmColorId = 1030,
		torsoColorId = 1001,
		rightArmColorId = 1030,
		headColorId = 1030,
		leftLegColorId = 1001,
		rightLegColorId = 1001,
	},
	assets = {
		{
			id = 1031492,
			assetType = {
				name = "Hat",
				id = 8,
			},
			name = "Striped Hat",
		},
		{
			id = 13062491,
			assetType = {
				name = "Face Accessory",
				id = 42,
			},
			name = "Vision Française ",
		},
		{
			id = 16598440,
			assetType = {
				name = "Neck Accessory",
				id = 43,
			},
			name = "Red Bow Tie",
		},
		{
			id = 28999228,
			assetType = {
				name = "Face",
				id = 18,
			},
			name = "Joyous Surprise",
		},
		{
			id = 86896488,
			assetType = {
				name = "Shirt",
				id = 11,
			},
			name = "Expensive Red Tuxedo Jacket",
		},
		{
			id = 86896502,
			assetType = {
				name = "Pants",
				id = 12,
			},
			name = "Expensive Red Tuxedo Pants",
		},
		{
			id = 376530220,
			assetType = {
				name = "Left Arm",
				id = 29,
			},
			name = "ROBLOX Boy Left Arm",
		},
		{
			id = 376531012,
			assetType = {
				name = "Right Arm",
				id = 28,
			},
			name = "ROBLOX Boy Right Arm",
		},
		{
			id = 376531300,
			assetType = {
				name = "Left Leg",
				id = 30,
			},
			name = "ROBLOX Boy Left Leg",
		},
		{
			id = 376531703,
			assetType = {
				name = "Right Leg",
				id = 31,
			},
			name = "ROBLOX Boy Right Leg",
		},
		{
			id = 376532000,
			assetType = {
				name = "Torso",
				id = 27,
			},
			name = "ROBLOX Boy Torso",
		},
	},
}

print(result)
```

### Method: Players:GetFriendsAsync

**Signature:** `Players:GetFriendsAsync(userId: User): FriendPages`

The GetFriendsAsync [Players](/docs/reference/engine/classes/Players.md) function returns a [FriendPages](/docs/reference/engine/classes/FriendPages.md)
object which contains information for all of the given user's friends. The
items within the [FriendPages](/docs/reference/engine/classes/FriendPages.md) object are tables with the following
fields:

| Name | Type | Description |
| --- | --- | --- |
| Id | int64 | The friend's UserId |
| Username | string | The friend's username |
| DisplayName | string | The [display name](/docs/reference/engine/classes/Player.md) of the friend. |

See the code samples for an easy way to iterate over all a player's
friends.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The user ID of the player being specified. |

**Returns:** `FriendPages` — A [FriendPages](/docs/reference/engine/classes/FriendPages.md) object containing information for all of the
given user's friends.

**Print Roblox Friends**

This code sample loads the [Player.UserId](/docs/reference/engine/classes/Player.md) of the player whose username
is provided at the top of the script by using
[Players:GetUserIdFromNameAsync()](/docs/reference/engine/classes/Players.md). It then gets a [FriendPages](/docs/reference/engine/classes/FriendPages.md)
object by calling [Players:GetFriendsAsync()](/docs/reference/engine/classes/Players.md) and walks the pages one at
a time, collecting each friend's username into a table that is printed at the
end.

```lua
local Players = game:GetService("Players")

local USERNAME = "Cozecant"

-- First, get the user ID of the player
local userId = Players:GetUserIdFromNameAsync(USERNAME)
-- Then, get a FriendPages object for their friends
local friendPages = Players:GetFriendsAsync(userId)

-- Walk the pages, collecting the username of every friend. Each page entry is
-- a table of information about the friend, including Username.
local usernames = {}
while true do
	for _, friend in ipairs(friendPages:GetCurrentPage()) do
		table.insert(usernames, friend.Username)
	end
	if friendPages.IsFinished then
		break
	end
	friendPages:AdvanceToNextPageAsync()
end

print("Friends of " .. USERNAME .. ": " .. table.concat(usernames, ", "))
```

**Expected output:** When run, this code sample will load the friends of the player whose username is provided at the top of the script.

### Method: Players:GetHumanoidDescriptionFromOutfitIdAsync

**Signature:** `Players:GetHumanoidDescriptionFromOutfitIdAsync(outfitId: int64): HumanoidDescription`

Returns the HumanoidDescription for a specified outfitId, which will be
set with the parts/colors/Animations etc of the outfit. An outfit can be
one created by a user, or it can be the outfit for a bundle created by
Roblox.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance, Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `outfitId` | `int64` |  | The ID of the outfit for which the HumanoidDescription is sought. |

**Returns:** `HumanoidDescription` — HumanoidDescription initialized with the specification for the passed
in outfitId.

**Get HumanoidDescription From Outfit ID**

Shows how to get the HumanoidDescription for bundle 799 (Fishman).

```lua
local Players = game:GetService("Players")
local Workspace = game:GetService("Workspace")

local function getOutfitId(bundleId)
	if bundleId <= 0 then
		return
	end
	local info = game.AssetService:GetBundleDetailsAsync(bundleId)
	if not info then
		return
	end
	for _, item in pairs(info.Items) do
		if item.Type == "UserOutfit" then
			return item.Id
		end
	end

	return nil
end

local function getHumanoidDescriptionBundle(bundleId)
	local itemId = getOutfitId(bundleId)
	if itemId and itemId > 0 then
		return Players:GetHumanoidDescriptionFromOutfitIdAsync(itemId)
	end

	return nil
end

local humanoidDescription = getHumanoidDescriptionBundle(799)
local humanoidModel = Players:CreateHumanoidModelFromDescriptionAsync(humanoidDescription, Enum.HumanoidRigType.R15)
humanoidModel.Parent = Workspace
```

**Expected output:** When run, a HumanoidDescription is placed in the Workspace.

### Method: Players:GetHumanoidDescriptionFromUserIdAsync

**Signature:** `Players:GetHumanoidDescriptionFromUserIdAsync(userId: User): HumanoidDescription`

Returns a HumanoidDescription which specifies everything equipped for the
avatar of the user specified by the passed in userId. Also includes scales
and body colors.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance, Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The userId for a Roblox user. (The UserId is the number in the profile of the user e.g www.roblox.com/users/1/profile). |

**Returns:** `HumanoidDescription` — HumanoidDescription initialized with the passed in user's avatar
specification.

**Get HumanoidDescription From User ID**

This code sample shows how to use GetHumanoidDescriptionFromUserIdAsync() to
create a Humanoid Model.

```lua
game.Players:CreateHumanoidModelFromDescriptionAsync(
	game.Players:GetHumanoidDescriptionFromUserIdAsync(1),
	Enum.HumanoidRigType.R15
).Parent =
	game.Workspace
```

**Expected output:** When run, a Humanoid Model is placed in the Workspace.

### Method: Players:GetNameFromUserIdAsync

**Signature:** `Players:GetNameFromUserIdAsync(userId: User): string`

The GetNameFromUserIdAsync [Players](/docs/reference/engine/classes/Players.md) function will send a query to
the Roblox website asking what the username is of the account with the
given [UserId](/docs/reference/engine/classes/Player.md).

This method errors if no account exists with the given UserId. If you
aren't certain such an account exists, it's recommended to wrap calls to
this function with [LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md). In addition, you can
manually cache results to make future calls with the same UserId fast. See
the code samples to learn more.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the player being specified. |

**Returns:** `string` — The name of a user with the specified [Player.UserId](/docs/reference/engine/classes/Player.md).

**Get Name from UserId**

This code sample demonstrates using the
[Players:GetNameFromUserIdAsync()](/docs/reference/engine/classes/Players.md) method to get a user's
[Player.Name](/docs/reference/engine/classes/Player.md) from their [Player.UserId](/docs/reference/engine/classes/Player.md).

```lua
local Players = game:GetService("Players")

-- Example Data:
-- UserId: 118271    Name: "RobloxRulez"
-- UserId: 131963979 Name: "docsRule"

local nameOne = Players:GetNameFromUserIdAsync(118271)
local nameTwo = Players:GetNameFromUserIdAsync(131963979)

print(nameOne, nameTwo)
-- prints: "RobloxRulez docsRule"
```

**Expected output:** RobloxRulez docsRule

**Get Name from UserId using a cache**

This code sample demonstrates using the
[Players:GetNameFromUserIdAsync()](/docs/reference/engine/classes/Players.md) method to get a user's
[Player.Name](/docs/reference/engine/classes/Player.md) from their [Player.UserId](/docs/reference/engine/classes/Player.md). Because
[GetNameFromUserIdAsync()](/docs/reference/engine/classes/Players.md) yields, you
can avoid calling it for the same [Name](/docs/reference/engine/classes/Player.md) using a table to
store each `UserId`:`Name` pair found, called a `cache`.
[LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md) is used to catch the failure in case the `Name`
doesn't exist.

```lua
local Players = game:GetService("Players")

-- Create a table called 'cache' to store each 'Name' as they are found.
-- If we lookup a 'Name' using the same 'UserId', the 'Name' will come
-- from cache (fast) instead of GetNameFromUserIdAsync() (yields).
local cache = {}

function getNameFromUserId(userId)
	-- First, check if the cache contains 'userId'
	local nameFromCache = cache[userId]
	if nameFromCache then
		-- if a value was stored in the cache at key 'userId', then this 'nameFromCache'
		-- is the correct Name and we can return it.
		return nameFromCache
	end

	-- If here, 'userId' was not previously looked up and does not exist in the
	-- cache. Now we need to use GetNameFromUserIdAsync() to look up the name
	local name
	local success, _ = pcall(function()
		name = Players:GetNameFromUserIdAsync(userId)
	end)
	if success then
		-- if 'success' is true, GetNameFromUserIdAsync() successfully found the
		-- name. Store this name in the cache using 'userId' as the key so we
		-- never have to look this name up in the future. Then return name.
		cache[userId] = name
		return name
	end
	-- If here, 'success' was false, meaning GetNameFromUserIdAsync()
	-- was unable to find the 'name' for the 'userId' provided. Warn the user
	-- this happened and then return nothing, or nil.
	warn("Unable to find Name for UserId:", userId)
	return nil
end

-- Example Data:
-- UserId: 118271    Name: "RobloxRulez"
-- UserId: 131963979 Name: "docsRule"

-- The first time a UserId is used, GetNameFromUserIdAsync() will be called
local nameOne = getNameFromUserId(118271)
local nameTwo = getNameFromUserId(131963979)
-- Because 118271 was previously used, get its Name from the cache
local nameOneQuick = getNameFromUserId(118271)

print(nameOne, nameTwo, nameOneQuick)
-- prints: "RobloxRulez docsRule RobloxRulez"
```

**Expected output:** RobloxRulez docsRule RobloxRulez

### Method: Players:GetPlayerByUserId

**Signature:** `Players:GetPlayerByUserId(userId: User): Player`

This function searches each [Player](/docs/reference/engine/classes/Player.md) in [Players](/docs/reference/engine/classes/Players.md) for one
whose [Player.UserId](/docs/reference/engine/classes/Player.md) matches the given `userId`. If such a player
does not exist, it returns `nil`.

This method is useful in finding the purchaser of a developer product
using [MarketplaceService.ProcessReceipt](/docs/reference/engine/classes/MarketplaceService.md) which provides a table
that includes the purchaser's [UserId](/docs/reference/engine/classes/Player.md) and not a
reference to the [Player](/docs/reference/engine/classes/Player.md) object itself. Most experiences will
require a reference to the player in order to grant products.

*Security: None · Thread Safety: Safe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the player being specified. |

**Returns:** `Player` — The [Player](/docs/reference/engine/classes/Player.md) with the given [Player.UserId](/docs/reference/engine/classes/Player.md), or `nil` if
no connected player has that UserId.

**Players:GetPlayerByUserId**

```lua
local Players = game:GetService("Players")

local player = Players:GetPlayerByUserId(1)

if player then
	print("Player with userId 1 is in this server! Their name is: " .. player.Name)
else
	print("Player with userId 1 is not in this server!")
end
```

### Method: Players:GetPlayerFromCharacter

**Signature:** `Players:GetPlayerFromCharacter(character: Model): Player`

This function returns the [Player](/docs/reference/engine/classes/Player.md) associated with the given
[Player.Character](/docs/reference/engine/classes/Player.md), or `nil` if one cannot be found. It is
equivalent to the following function:

```lua
local function getPlayerFromCharacter(character)
	for _, player in game:GetService("Players"):GetPlayers() do
		if player.Character == character then
			return player
		end
	end
end
```

This method is often used when some event in player's character fires
(such as their [Humanoid](/docs/reference/engine/classes/Humanoid.md) [dying](/docs/reference/engine/classes/Humanoid.md)). Such an
event might not directly reference the Player object, but this method
provides easy access. The inverse of this function can be described as
getting the Character of a Player. To do this, simply access the Character
property.

*Security: None · Thread Safety: Unsafe · Capabilities: Players · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `character` | `Model` |  | A character instance that you want to get the player from. |

**Returns:** `Player` — The [Player](/docs/reference/engine/classes/Player.md) whose [Player.Character](/docs/reference/engine/classes/Player.md) matches the given
model, or `nil` if one cannot be found.

**Players:GetPlayerFromCharacter**

Players:GetPlayerFromCharacter

```lua
local Players = game:GetService("Players")
local Workspace = game:GetService("Workspace")

local PLAYER_NAME = "Nightriff"

local character = Workspace:FindFirstChild(PLAYER_NAME)
local player = Players:GetPlayerFromCharacter(character)

if player then
	print(`Player {player.Name} ({player.UserId}) is in the game`)
else
	print(`Player {PLAYER_NAME} is not in the game!`)
end
```

### Method: Players:GetPlayers

**Signature:** `Players:GetPlayers(): List<Player>`

This method returns a table of all presently connected [Player](/docs/reference/engine/classes/Player.md)
objects. It functions the same way [Instance:GetChildren()](/docs/reference/engine/classes/Instance.md) would
except that it only returns [Player](/docs/reference/engine/classes/Player.md) objects found under
[Players](/docs/reference/engine/classes/Players.md). When used with a `for` loop, it is useful for iterating
over all players in an experience.

```lua
local Players = game:GetService("Players")

for _, player in Players:GetPlayers() do
	print(player.Name)
end
```

Scripts that connect to [Players.PlayerAdded](/docs/reference/engine/classes/Players.md) are often trying to
process every Player that connects to the experience. This method is
useful for iterating over already-connected players that wouldn't fire
[PlayerAdded](/docs/reference/engine/classes/Players.md). Using this method ensures that no
player is missed!

```lua
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	print("Player: " .. player.Name)
end

for _, player in Players:GetPlayers() do
	onPlayerAdded(player)
end
Players.PlayerAdded:Connect(onPlayerAdded)
```

*Security: None · Thread Safety: Safe · Capabilities: Players*

**Returns:** `List<Player>` — A table containing all the players in the server.

**Give Sparkles to Everyone**

This code sample listens for players spawning and gives them Sparkles in their
head. It does this by defining two functions, `onPlayerSpawned` and
`onPlayerAdded`.

```lua
local Players = game:GetService("Players")

local function onCharacterAdded(character)
	-- Give them sparkles on their head if they don't have them yet
	if not character:FindFirstChild("Sparkles") then
		local sparkles = Instance.new("Sparkles")
		sparkles.Parent = character:WaitForChild("Head")
	end
end

local function onPlayerAdded(player)
	-- Check if they already spawned in
	if player.Character then
		onCharacterAdded(player.Character)
	end
	-- Listen for the player (re)spawning
	player.CharacterAdded:Connect(onCharacterAdded)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: Players:GetProfileConfigurationFromUserIdAsync

**Signature:** `Players:GetProfileConfigurationFromUserIdAsync(userId: User): ProfileConfiguration`

Returns the profile configuration of the user specified by the given
[Player.UserId](/docs/reference/engine/classes/Player.md) as a dictionary. The dictionary can include a
`BackgroundAssetId` field for the user's profile background asset ID and a
`FrameAssetId` field for the user's profile frame image asset ID.

Can only be called from the server and is throttled to a limited number of
requests per minute.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance, Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the user whose profile configuration to retrieve. |

**Returns:** `ProfileConfiguration` — A dictionary containing the user's profile configuration, such as the
background asset ID.

### Method: Players:GetUserIdFromNameAsync

**Signature:** `Players:GetUserIdFromNameAsync(userName: string): int64`

This function will send a query to the Roblox website asking what the
[Player.UserId](/docs/reference/engine/classes/Player.md) is of the account with the given [Player](/docs/reference/engine/classes/Player.md)
name.

This method errors if no account exists with the given username. If you
aren't certain such an account exists, it's recommended to wrap calls to
this function with [LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md). In addition, you can
manually cache results to quickly make future calls with the same
username. See the code samples to learn more.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userName` | `string` |  | The username of the player being specified. |

**Returns:** `int64` — The [Player.UserId](/docs/reference/engine/classes/Player.md) of a user whose name is specified.

**Get UserId from Name**

This code sample demonstrates using the
[Players:GetUserIdFromNameAsync()](/docs/reference/engine/classes/Players.md) method to get a user's
[Player.UserId](/docs/reference/engine/classes/Player.md) from their [Player.Name](/docs/reference/engine/classes/Player.md).

```lua
local Players = game:GetService("Players")

-- Example Data:
-- UserId: 118271    Name: "RobloxRulez"
-- UserId: 131963979 Name: "docsRule"

local userIdOne = Players:GetUserIdFromNameAsync("RobloxRulez")
local userIdTwo = Players:GetUserIdFromNameAsync("docsRule")
print(userIdOne, userIdTwo)
-- prints: "118271 131963979"
```

**Expected output:** 118271 131963979

**Get UserId from Name using a cache**

This code sample demonstrates using the
[Players:GetUserIdFromNameAsync()](/docs/reference/engine/classes/Players.md) method to get a user's
[Player.UserId](/docs/reference/engine/classes/Player.md) from their [Player.Name](/docs/reference/engine/classes/Player.md). Because
[GetUserIdFromNameAsync()](/docs/reference/engine/classes/Players.md) yields, you
can avoid calling it for the same [UserId](/docs/reference/engine/classes/Player.md) using a table
to store each `Name`:`UserId` pair found, called a `cache`.
[LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md) is used to catch the failure in case the `UserId`
doesn't exist.

```lua
local Players = game:GetService("Players")

-- Create a table called 'cache' to store each 'UserId' as they are found.
-- If we lookup a 'UserId' using the same 'Name', the 'UserId' will come
-- from cache (fast) instead of GetUserIdFromNameAsync() (yields).
local cache = {}

function getUserIdFromName(name)
	-- First, check if the cache contains 'name'
	local userIdFromCache = cache[name]
	if userIdFromCache then
		-- if a value was stored in the cache at key 'name', then this 'userIdFromCache'
		-- is the correct UserId and we can return it.
		return userIdFromCache
	end

	-- If here, 'name' was not previously looked up and does not exist in the
	-- cache. Now we need to use GetUserIdFromNameAsync() to look up the userId
	local userId
	local success, _ = pcall(function()
		userId = Players:GetUserIdFromNameAsync(name)
	end)
	if success then
		-- if 'success' is true, GetUserIdFromNameAsync() successfully found the
		-- userId. Store this userId in the cache using 'name' as the key so we
		-- never have to look this userId up in the future. Then return userId.
		cache[name] = userId
		return userId
	end
	-- If here, 'success' was false, meaning GetUserIdFromNameAsync()
	-- was unable to find the 'userId' for the 'name' provided. We can warn the
	-- user this happened and then return nothing, or nil.
	warn("Unable to find UserId for Name:", name)
	return nil
end

-- Example Data:
-- UserId: 118271    Name: "RobloxRulez"
-- UserId: 131963979 Name: "docsRule"

-- The first time a Name is used, GetUserIdFromNameAsync() will be called
local userIdOne = getUserIdFromName("RobloxRulez")
local userIdTwo = getUserIdFromName("docsRule")
-- Because "RobloxRulez" was previously used, get its UserId from the cache
local userIdOneQuick = getUserIdFromName("RobloxRulez")

print(userIdOne, userIdTwo, userIdOneQuick)
-- prints: "118271 131963979 118271"
```

**Expected output:** 118271 131963979 118271

### Method: Players:GetUserThumbnailAsync

**Signature:** `Players:GetUserThumbnailAsync(userId: User, thumbnailType: ThumbnailType, thumbnailSize: ThumbnailSize): Tuple`

This function returns the content URL of an image of a player's avatar
given their [UserId](/docs/reference/engine/classes/Player.md), the desired image size as a
[ThumbnailSize](/docs/reference/engine/enums/ThumbnailSize.md) enum, and the desired type as a [ThumbnailType](/docs/reference/engine/enums/ThumbnailType.md)
enum. It also returns a boolean describing if the image is ready to use.

Most often, this method is used with [ImageLabel.Image](/docs/reference/engine/classes/ImageLabel.md) or
[Decal.Texture](/docs/reference/engine/classes/Decal.md) to display user avatar pictures in an experience.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the player being specified. |
| `thumbnailType` | `ThumbnailType` |  | A [ThumbnailType](/docs/reference/engine/enums/ThumbnailType.md) describing the type of thumbnail. |
| `thumbnailSize` | `ThumbnailSize` |  | A [ThumbnailSize](/docs/reference/engine/enums/ThumbnailSize.md) specifying the size of the thumbnail. |

**Returns:** `Tuple` — A tuple containing the content URL of a user thumbnail based on the
specified parameters, and a bool describing if the image is ready to
be used or not.

**Display Player Thumbnail**

This code sample displays the current player's thumbnail in a parent
`ImageLabel` by using [Players:GetUserThumbnailAsync()](/docs/reference/engine/classes/Players.md) and setting the
[Image()](/docs/reference/engine/classes/ImageLabel.md) property as well as its
[Size()](/docs/reference/engine/classes/GuiObject.md).

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local PLACEHOLDER_IMAGE = "rbxassetid://0" -- replace with placeholder image

-- fetch the thumbnail
local userId = player.UserId
local thumbType = Enum.ThumbnailType.HeadShot
local thumbSize = Enum.ThumbnailSize.Size420x420
local content, isReady = Players:GetUserThumbnailAsync(userId, thumbType, thumbSize)

-- set the ImageLabel's content to the user thumbnail
local imageLabel = script.Parent
imageLabel.Image = (isReady and content) or PLACEHOLDER_IMAGE
imageLabel.Size = UDim2.new(0, 420, 0, 420)
```

**Expected output:** When run, the parent `ImageLabel` should have its `Class.ImageLabel.Image|Image()` and `Class.GuiObject.Size|Size()` set accordingly.

### Method: Players:SetChatStyle

**Signature:** `Players:SetChatStyle(style?: ChatStyle): ()`

This function sets whether BubbleChat and ClassicChat are being used, and
tells TeamChat and Chat what to do using the [ChatStyle](/docs/reference/engine/enums/ChatStyle.md) enum. Since
this item is protected, attempting to use it in a [Script](/docs/reference/engine/classes/Script.md) or
[LocalScript](/docs/reference/engine/classes/LocalScript.md) will cause an error.

This function is used internally when the chat mode is set by the
experience.

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `style` | `ChatStyle` | `Classic` | The specified chat style being set. |

**Returns:** `()`

**Setting a Player's Chat Style**

This example demonstrates that the [Players:SetChatStyle()](/docs/reference/engine/classes/Players.md) function
executes without error if using the Command Bar or a Plugin and errors if
executed in a `LocalScript`.

When executed in the Command Bar, this code sets the chat style to Classic
using the [ChatStyle](/docs/reference/engine/enums/ChatStyle.md) enum.

```lua
-- Command bar
game.Players:SetChatStyle(Enum.ChatStyle.Classic) -- Set's chat style to Classic

-- LocalScript
local Players = game:GetService("Players")
Players:SetChatStyle(Enum.ChatStyle.Classic) -- Errors
```

### Method: Players:TeamChat

**Signature:** `Players:TeamChat(message: string): ()`

This function makes the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md) chat the given
message, which will only be viewable by users on the same team. Since this
item is protected, attempting to use it in a [Script](/docs/reference/engine/classes/Script.md) or
[LocalScript](/docs/reference/engine/classes/LocalScript.md) will cause an error.

This function is used internally when the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md)
sends a message to their team.

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `string` |  | The message being chatted. |

**Returns:** `()`

**Sending Team Chat**

This example demonstrates that the [Players:TeamChat()](/docs/reference/engine/classes/Players.md) function
executes without error if using the Command Bar or a Plugin and errors if
executed in a `LocalScript`.

When executed in the Command Bar, the function sends the specified message to
all players on the same `Team` as the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md).

```lua
-- Command bar
game.Players:TeamChat("Hello World") -- Sends a "Hello World" message to all players on the local player's team

-- LocalScript
local Players = game:GetService("Players")
Players:TeamChat("Hello World") -- Errors
```

### Method: Players:UnbanAsync

**Signature:** `Players:UnbanAsync(config: Dictionary): ()`

Unbans players banned from [Players:BanAsync()](/docs/reference/engine/classes/Players.md) or the
[User Restrictions Open Cloud API](/docs/en-us/cloud/reference/UserRestriction.md). This
method is enabled and disabled by the [Players.BanningEnabled](/docs/reference/engine/classes/Players.md)
property, which you can toggle in Studio.

Like [Players:BanAsync()](/docs/reference/engine/classes/Players.md), this method takes in a `config`
dictionary that will let you bulk unban users. This configures the users
that are unbanned and the scope from which they are unbanned from.

Unbans will only take effect on bans with the same `ApplyToUniverse`
scope. For example, an unban with `ApplyToUniverse` set to `true` will not
invalidate a previous ban with `ApplyToUniverse` set to `false`. In other
words, a universe level unban will not invalidate a place level ban. The
opposite also holds true.

For the case where a user's device may be blocked by a ban where
`ApplyDeviceBlock` was set to `true`, an unban applied by this method will
override the device block for the unbanned player. Please note that
unbanning a user through any other method, such as the Open Cloud API or
the Creator Hub, will not lift the device block.

This method invokes a HTTP call to backend services, which are throttled
and may fail. If you are calling this API with multiple UserIds, this
method will attempt to make this HTTP call for each UserId. It will then
aggregate any error messages and join them as a comma separated list. For
example, if this method is invoked for five `UserIds`: `{1, 2, 3, 4, 5}`
and requests for users 2 and 4 fail then the following error message
appears:
`HTTP failure for UserId 2: Timedout, HTTP 504 (Service unavailable) failure for UserId 4: Service exception.`
The message will always include `failure for UserId {}` if it is an HTTP
error. It is undefined behavior if you pass in both valid and invalid
UserIds, i.e. a `UserId` that is not a positive number, as some network
requests may succeed before all input is validated.

Because of the risks associated with banning users, this method may only
be called on the backend server. Client side calls will result in an
error. You may test this API in Studio, Team Create, and Team Test, but
the bans will not apply to production. This function call will only
attempt ban requests on production servers and not in Studio testing.
However, all input validation steps will still work in Studio.

This API uses the
[User Restrictions Open Cloud API](/docs/en-us/cloud/reference/UserRestriction.md). You
will be able to utilize these APIs to manage your bans in third party
applications.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, Consequences*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `config` | `Dictionary` |  | \| Name \| Type \| Description \| \| --- \| --- \| --- \| \| `UserIds` \| array \| UserIDs to be force allowed into the experience(s).    Max size is `50`. \| \| `ApplyToUniverse` \| boolean \| Propagates the unban to all places within this universe.  \| |

**Returns:** `()`

**Unbanning Users**

The following un-bans a user, as well as another unrelated account with
UserId 789.

```lua
local Players = game:GetService("Players")

if shouldBeUnbanned(player) then
	local config: UnbanConfigType = {
		UserIds = { player.UserId, 789 },
		ApplyToUniverse = false,
	}
	local success, err = pcall(function()
		return Players:UnbanAsync(config)
	end)
	print(success, err)
end
```

### Method: Players:CreateHumanoidModelFromDescription

**Signature:** `Players:CreateHumanoidModelFromDescription(description: HumanoidDescription, rigType: HumanoidRigType, assetTypeVerification?: AssetTypeVerification): Model`

> **Deprecated:** This method has been superseded by [CreateHumanoidModelFromDescriptionAsync()](/docs/reference/engine/classes/Players.md).

Returns a character [Model](/docs/reference/engine/classes/Model.md) equipped with everything specified in
the passed in [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md), and is R6 or R15 as specified
by `rigType`. This method has been superseded by
[CreateHumanoidModelFromDescriptionAsync()](/docs/reference/engine/classes/Players.md),
which should be used in new work.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance, Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `description` | `HumanoidDescription` |  | Specifies the appearance of the returned character. |
| `rigType` | `HumanoidRigType` |  | Specifies whether the returned character will be R6 or R15. |
| `assetTypeVerification` | `AssetTypeVerification` | `Default` | The asset type verification mode. |

**Returns:** `Model` — A [Humanoid](/docs/reference/engine/classes/Humanoid.md) character [Model](/docs/reference/engine/classes/Model.md).

### Method: Players:CreateHumanoidModelFromUserId

**Signature:** `Players:CreateHumanoidModelFromUserId(userId: User): Model`

> **Deprecated:** This method has been superseded by [CreateHumanoidModelFromUserIdAsync()](/docs/reference/engine/classes/Players.md).

Returns a character [Model](/docs/reference/engine/classes/Model.md) set up with everything equipped to match
the avatar of the user specified by the passed in `userId`, including
whether that character is currently R6 or R15. This method has been
superseded by
[CreateHumanoidModelFromUserIdAsync()](/docs/reference/engine/classes/Players.md),
which should be used in new work.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The userId for a Roblox user. (The UserId is the number in the profile of the user e.g www.roblox.com/users/1/profile). |

**Returns:** `Model` — A Humanoid character Model.

**Create Humanoid Model From A User ID**

This code sample creates a Humanoid Model to match the avatar of the passed in
User ID, and parents the Model to the Workspace.

```lua
game.Players:CreateHumanoidModelFromUserIdAsync(1).Parent = game.Workspace
```

**Expected output:** When run, a Model is created and parented to the Workspace.

### Method: Players:GetCharacterAppearanceAsync

**Signature:** `Players:GetCharacterAppearanceAsync(userId: User): Model`

> **Deprecated:** This method is deprecated. Do not use it for new work.

This function returns a [Model](/docs/reference/engine/classes/Model.md) containing the assets which the
player is wearing, excluding gear.

If you prefer a Luau table of information about these assets instead of a
model, use [Players:GetCharacterAppearanceInfoAsync()](/docs/reference/engine/classes/Players.md).

This method behaves similar to [InsertService:LoadAsset()](/docs/reference/engine/classes/InsertService.md), and is
like using [LoadAsset](/docs/reference/engine/classes/InsertService.md) on the asset
information returned by [Players:GetCharacterAppearanceInfoAsync()](/docs/reference/engine/classes/Players.md)
except faster.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the specified player. |

**Returns:** `Model` — A [Model](/docs/reference/engine/classes/Model.md) containing the assets the player is wearing, excluding
gear.

**How To Get A Character's Appearance**

This example demonstrates how to retrieve a character's appearance.

The returned `Model` is not a child of Workspace by default. If you want the
model to be visible, its [parent](/docs/reference/engine/classes/Instance.md) property must be set.

```lua
local Players = game:GetService("Players")

local USER_ID = 18697683

local appearanceModel = Players:GetCharacterAppearanceAsync(USER_ID)

appearanceModel.Parent = workspace
```

### Method: Players:GetHumanoidDescriptionFromOutfitId

**Signature:** `Players:GetHumanoidDescriptionFromOutfitId(outfitId: int64): HumanoidDescription`

> **Deprecated:** This method has been superseded by [GetHumanoidDescriptionFromOutfitIdAsync()](/docs/reference/engine/classes/Players.md).

Returns the [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) for the specified `outfitId`, set
with the parts, colors, animations, and other properties of the outfit. An
outfit can be one created by a user, or the outfit for a bundle created by
Roblox. This method has been superseded by
[GetHumanoidDescriptionFromOutfitIdAsync()](/docs/reference/engine/classes/Players.md),
which should be used in new work.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance, Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `outfitId` | `int64` |  | The ID of the outfit for which the HumanoidDescription is sought. |

**Returns:** `HumanoidDescription` — HumanoidDescription initialized with the specification for the passed
in outfitId.

**Get HumanoidDescription From Outfit ID**

Shows how to get the HumanoidDescription for bundle 799 (Fishman).

```lua
local Players = game:GetService("Players")
local Workspace = game:GetService("Workspace")

local function getOutfitId(bundleId)
	if bundleId <= 0 then
		return
	end
	local info = game.AssetService:GetBundleDetailsAsync(bundleId)
	if not info then
		return
	end
	for _, item in pairs(info.Items) do
		if item.Type == "UserOutfit" then
			return item.Id
		end
	end

	return nil
end

local function getHumanoidDescriptionBundle(bundleId)
	local itemId = getOutfitId(bundleId)
	if itemId and itemId > 0 then
		return Players:GetHumanoidDescriptionFromOutfitIdAsync(itemId)
	end

	return nil
end

local humanoidDescription = getHumanoidDescriptionBundle(799)
local humanoidModel = Players:CreateHumanoidModelFromDescriptionAsync(humanoidDescription, Enum.HumanoidRigType.R15)
humanoidModel.Parent = Workspace
```

**Expected output:** When run, a HumanoidDescription is placed in the Workspace.

### Method: Players:GetHumanoidDescriptionFromUserId

**Signature:** `Players:GetHumanoidDescriptionFromUserId(userId: User): HumanoidDescription`

> **Deprecated:** This method has been superseded by [GetHumanoidDescriptionFromUserIdAsync()](/docs/reference/engine/classes/Players.md).

Returns a [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) which specifies everything equipped
for the avatar of the user specified by the passed in `userId`, including
scales and body colors. This method has been superseded by
[GetHumanoidDescriptionFromUserIdAsync()](/docs/reference/engine/classes/Players.md),
which should be used in new work.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance, Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The userId for a Roblox user. (The UserId is the number in the profile of the user e.g www.roblox.com/users/1/profile). |

**Returns:** `HumanoidDescription` — HumanoidDescription initialized with the passed in user's avatar
specification.

**Get HumanoidDescription From User ID**

This code sample shows how to use GetHumanoidDescriptionFromUserIdAsync() to
create a Humanoid Model.

```lua
game.Players:CreateHumanoidModelFromDescriptionAsync(
	game.Players:GetHumanoidDescriptionFromUserIdAsync(1),
	Enum.HumanoidRigType.R15
).Parent =
	game.Workspace
```

**Expected output:** When run, a Humanoid Model is placed in the Workspace.

### Method: Players:getPlayers

**Signature:** `Players:getPlayers(): List<Player>`

> **Deprecated:** This function is a deprecated variant of [Players:GetPlayers()](/docs/reference/engine/classes/Players.md) which should be used instead.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Returns:** `List<Player>`

### Method: Players:playerFromCharacter

**Signature:** `Players:playerFromCharacter(character: Model): Player`

> **Deprecated:** This function is a deprecated variant of [Players:GetPlayerFromCharacter()](/docs/reference/engine/classes/Players.md) which should be used in new work.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `character` | `Model` |  |  |

**Returns:** `Player`

### Method: Players:players

**Signature:** `Players:players(): List<Player>`

> **Deprecated:** This item has been superseded by [Players:GetPlayers()](/docs/reference/engine/classes/Players.md) which should be used in all new work.

This function was once used to return a list of players in an experience,
but has since been deprecated in favor of [Players:GetPlayers()](/docs/reference/engine/classes/Players.md)

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Returns:** `List<Player>`

## Events

### Event: Players.PlayerAdded

**Signature:** `Players.PlayerAdded(player: Player)`

This event fires when a player enters the experience, such as loading the
player's saved [GlobalDataStore](/docs/reference/engine/classes/GlobalDataStore.md) data.

This can be used alongside the [Players.PlayerRemoving](/docs/reference/engine/classes/Players.md) event, which
fires when a player is about to leave the experience. For instance, if you
would like print a message every time a new player joins or leaves:

```lua
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	print(player.Name .. " joined the experience!")
end)

Players.PlayerRemoving:Connect(function(player, reason)
	print(player.Name .. " left the experience! Reason: " .. tostring(exitReason))
end)
```

If you want to track when a player's character is added or removed from
the experience, such as when a player respawns or dies, you can use the
[Player.CharacterAdded](/docs/reference/engine/classes/Player.md) and [Player.CharacterRemoving](/docs/reference/engine/classes/Player.md)
functions.

Note that this event does not work as expected in a solo playtest mode
because the player is created before scripts run that connect to
[PlayerAdded](/docs/reference/engine/classes/Players.md). To handle this case, as well as
cases in which the script is added into the experience after a player
enters, create an `onPlayerAdded()` function that you can call to handle a
player's entrance.

*Security: None · Capabilities: Players*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Player` | An instance of the player that joined the experience. |

**Players.PlayerAdded**

This example will print "A player has entered: " followed by the name of the
player that enters/joins a game every time a player joins.

```lua
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	print("A player has entered: " .. player.Name)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Event: Players.PlayerMembershipChanged

**Signature:** `Players.PlayerMembershipChanged(player: Player)`

This event fires when the experience server recognizes that a player's
membership has changed. Note, however, that the server will only attempt
to check and update the membership **after** the Premium modal has been
closed. Thus, to account for cases where the user purchases Premium
**outside** of the experience while playing, you must still prompt them to
purchase Premium; this will then show a message telling them they're
already upgraded and, once they close the modal, the server will update
their membership and trigger this event.

To learn more about and incorporating Premium into your experience and
monetizing with the engagement-based payouts system, see
[Engagement-Based Payouts](/docs/en-us/production/monetization/engagement-based-payouts.md).

See also:

- [MarketplaceService:PromptPremiumPurchase()](/docs/reference/engine/classes/MarketplaceService.md), used to prompt a
  user to purchase Premium
- [MarketplaceService.PromptPremiumPurchaseFinished](/docs/reference/engine/classes/MarketplaceService.md), fires when the
  Premium purchase UI closes

*Security: None · Capabilities: Players*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Player` | The [Player](/docs/reference/engine/classes/Player.md) whose membership has changed. |

**Handling Premium Membership Changes**

The function in the code sample runs after the game server confirms a player's
membership has changed. It demonstrates how you can grant players access to
Premium benefits (or revoke them) when their membership status changes.

```lua
local Players = game:GetService("Players")

local function grantPremiumBenefits(player)
	-- Grant the player access to Premium-only areas, items, or anything you can imagine!
	print("Giving", player, "premium benefits!")
end

local function playerAdded(player)
	if player.MembershipType == Enum.MembershipType.Premium then
		grantPremiumBenefits(player)
	end
end

local function playerMembershipChanged(player)
	print("Received event PlayerMembershipChanged. New membership = " .. tostring(player.MembershipType))
	if player.MembershipType == Enum.MembershipType.Premium then
		grantPremiumBenefits(player)
	end
end

Players.PlayerAdded:Connect(playerAdded)
Players.PlayerMembershipChanged:Connect(playerMembershipChanged)
```

### Event: Players.PlayerRemoving

**Signature:** `Players.PlayerRemoving(player: Player, reason: PlayerExitReason)`

This event fires right before a [Player](/docs/reference/engine/classes/Player.md) leaves the experience,
before [ChildRemoved](/docs/reference/engine/classes/Instance.md) fires on
[Players](/docs/reference/engine/classes/Players.md), and behaves somewhat similarly to
[Instance.DescendantRemoving](/docs/reference/engine/classes/Instance.md). Since it fires before the actual
removal of a [Player](/docs/reference/engine/classes/Player.md), this event is useful for storing player data
using a [GlobalDataStore](/docs/reference/engine/classes/GlobalDataStore.md).

This can be used alongside the [Player.PlayerAdded](/docs/reference/engine/classes/Player.md) event, which
fires when a player joins the experience. For instance, to print a message
every time a new player joins or leaves:

```lua
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	print(player.Name .. " joined the experience!")
end)

Players.PlayerRemoving:Connect(function(player, exitReason)
	print(player.Name .. " left the experience! - Reason: " .. tostring(exitReason))
end)
```

If you want to track when a player's character is added or removed from
the experience, such as when a player respawns or dies, you can use the
[Player.CharacterAdded](/docs/reference/engine/classes/Player.md) and [Player.CharacterRemoving](/docs/reference/engine/classes/Player.md)
functions.

*Security: None · Capabilities: Players*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Player` | An instance of the player that is leaving. |
| `reason` | `PlayerExitReason` | Enum.PlayerExitReason in attempt to inform why. |

**Players.PlayerRemoving**

This code will print "A player has left: ", followed by the player's name,
every time a player leaves:

```lua
local Players = game:GetService("Players")

local function onPlayerRemoving(player)
	print("A player has left: " .. player.Name)
end

Players.PlayerRemoving:Connect(onPlayerRemoving)
```

### Event: Players.UserSubscriptionStatusChanged

**Signature:** `Players.UserSubscriptionStatusChanged(user: Player, subscriptionId: string)`

This event fires when the experience server recognizes that the user's
status for a certain subscription has changed. Note that the server only
attempts to check and update the status **after** the Subscription
Purchase modal has been closed. To account for cases in which the user
purchases the subscription **outside** of the experience while playing,
you must still prompt them to purchase the subscription; the prompt shows
a message telling the user they're already subscribed, and after they
close the modal, the server updates their subscription status and triggers
this event.

Note that only server scripts receive this event.

*Security: None · Capabilities: Players, Monetization*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `user` | `Player` | User whose subscription status has changed. |
| `subscriptionId` | `string` | The ID of the subscription with a status change. |

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