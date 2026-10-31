---
name: TextChatService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "A service handling in-experience text chat."
---

# Class: TextChatService

> A service handling in-experience text chat.

## Description

A service handling in-experience text chat, including managing
[TextChannels](/docs/reference/engine/classes/TextChannel.md), decorating messages, filtering text,
creating [TextChatCommands](/docs/reference/engine/classes/TextChatCommand.md), and
[developing custom chats interfaces](/docs/en-us/chat/examples/simple-custom-frontend-ui.md).
To learn more, see
[text chat overview](/docs/en-us/chat/in-experience-text-chat.md).

For further customization, `TextChatService` has the following singleton
children:

- [ChatWindowConfiguration](/docs/reference/engine/classes/ChatWindowConfiguration.md)
- [ChatInputBarConfiguration](/docs/reference/engine/classes/ChatInputBarConfiguration.md)
- [BubbleChatConfiguration](/docs/reference/engine/classes/BubbleChatConfiguration.md)
- [ChannelTabsConfiguration](/docs/reference/engine/classes/ChannelTabsConfiguration.md)

To display content from a [TextChannel](/docs/reference/engine/classes/TextChannel.md) in a custom location, place a
[TextChannelWindow](/docs/reference/engine/classes/TextChannelWindow.md) under a [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) or [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md).

## Properties

### Property: TextChatService.ChatTranslationEnabled

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
    "Chat"
  ]
}
```

Determines whether a user has chat translation enabled. If `true`,
messages the user receives will be translated into their preferred
language. Use [TextChatMessage.Translation](/docs/reference/engine/classes/TextChatMessage.md) to get the message
translation. This property is client-side only and reflects the user's own
preference; read it from a [LocalScript](/docs/reference/engine/classes/LocalScript.md) to adapt custom chat UIs
when the user toggles translation.

### Property: TextChatService.ChatVersion

```json
{
  "type": "ChatVersion",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

Determines whether to fully enable [TextChatService](/docs/reference/engine/classes/TextChatService.md) or revert to
the legacy chat system. Setting this property to
[ChatVersion.LegacyChatService](/docs/reference/engine/enums/ChatVersion.md) effectively disables
[TextChatService](/docs/reference/engine/classes/TextChatService.md).

### Property: TextChatService.CreateDefaultCommands

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
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

Determines whether [TextChatService](/docs/reference/engine/classes/TextChatService.md) should create default
[TextChatCommands](/docs/reference/engine/classes/TextChatCommand.md). If `true`, the following
[TextChatCommands](/docs/reference/engine/classes/TextChatCommand.md) are created and put in a
[Folder](/docs/reference/engine/classes/Folder.md) named **TextChatCommands** inside [TextChatService](/docs/reference/engine/classes/TextChatService.md):

| Name | Primary Alias | Secondary Alias | Description | Usage Example |
| --- | --- | --- | --- | --- |
| **RBXClearCommand** | clear | cls | Clears the chat log for the local user. | `/cls` |
| **RBXConsoleCommand** | console |  | Opens the Developer Console. | `/console` |
| **RBXEmoteCommand** | emote | e | Plays an avatar emote. | `/e dance` |
| **RBXHelpCommand** | help | ? | Shows a list of chat commands. | `/help` |
| **RBXMuteCommand** | mute | m | Mutes a user by their [Name](/docs/reference/engine/classes/Player.md) or [DisplayName](/docs/reference/engine/classes/Player.md) in all [TextChannels](/docs/reference/engine/classes/TextChannel\.md). | `/m Username` |
| **RBXTeamCommand** | team | t | Enters team chat mode where messages are only visible to teammates. | `/t` |
| **RBXUnmuteCommand** | unmute | um | Unmutes a user by their [Name](/docs/reference/engine/classes/Player.md) or [DisplayName](/docs/reference/engine/classes/Player.md) in all [TextChannels](/docs/reference/engine/classes/TextChannel\.md). | `/um Username` |
| **RBXVersionCommand** | version | v | Shows the chat version. | `/version` |
| **RBXWhisperCommand** | whisper | w | Enters whisper mode with another [Player](/docs/reference/engine/classes/Player.md). | `/w DisplayName` or `/w @Username` |

Note that you can edit, create, and remove
[TextChatCommands](/docs/reference/engine/classes/TextChatCommand.md) even if
[CreateDefaultCommands](/docs/reference/engine/classes/TextChatService.md) is
`true`. Also note that mute and unmute commands apply to all
[TextChannels](/docs/reference/engine/classes/TextChannel.md).

### Property: TextChatService.CreateDefaultTextChannels

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
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

Determines whether [TextChatService](/docs/reference/engine/classes/TextChatService.md) should create default
[TextChannels](/docs/reference/engine/classes/TextChannel.md). If `true`, a [Folder](/docs/reference/engine/classes/Folder.md) named
**TextChannels** is created inside [TextChatService](/docs/reference/engine/classes/TextChatService.md) at runtime to
contain the [TextChannels](/docs/reference/engine/classes/TextChannel.md) outlined in the table below.
Each of the default channels has the described special behavior applied to
messages using its internally bound [TextChannel.OnIncomingMessage](/docs/reference/engine/classes/TextChannel.md)
callback function, changing how messages appear when sent through the
channel. The callback is assigned automatically either at runtime (if the
[TextChannel](/docs/reference/engine/classes/TextChannel.md) exists) or when the [TextChannel](/docs/reference/engine/classes/TextChannel.md) is created.

| Channel | Description |
| --- | --- |
| **RBXGeneral** | [TextChannel](/docs/reference/engine/classes/TextChannel.md) for player messages. In the chat window, messages are modified such that [PrefixText](/docs/reference/engine/classes/TextChatMessage.md) receives a [rich text](/docs/en-us/ui/rich-text.md) font color tag to give chatting players their distinctive name color. If [Player.Team](/docs/reference/engine/classes/Player.md) exists, that [Team.TeamColor](/docs/reference/engine/classes/Team.md) is used instead of the default name color. |
| **RBXSystem** | [TextChannel](/docs/reference/engine/classes/TextChannel.md) for system messages. In the chat window, messages are modified such that [TextChatMessage.Text](/docs/reference/engine/classes/TextChatMessage.md) is given a light grey color tag by default, or a red color tag if [TextChatMessage.Metadata](/docs/reference/engine/classes/TextChatMessage.md) contains the word `"Error"`. |
| **RBXTeam[BrickColor]** | [TextChannel](/docs/reference/engine/classes/TextChannel.md) for team-specific player messages, created when a [TeamColor](/docs/reference/engine/classes/Team.md) is in use by any [Team](/docs/reference/engine/classes/Team.md) within the [Teams](/docs/reference/engine/classes/Teams.md) service. Name of the created channel is **RBXTeam** followed by the [TeamColor](/docs/reference/engine/classes/Team.md) name. For example, **RBXTeamCrimson** is a [TextChannel](/docs/reference/engine/classes/TextChannel.md) created when there is an active team whose [TeamColor](/docs/reference/engine/classes/Team.md) property is the "Crimson" [BrickColor](/docs/reference/engine/datatypes/BrickColor.md).

In the chat window, messages are modified such that [PrefixText](/docs/reference/engine/classes/TextChatMessage.md) is colored according to the [TeamColor](/docs/reference/engine/classes/Player.md) and is prepended with **[Team]**.

Team channels create [TextSources](/docs/reference/engine/classes/TextSource\.md) for all non‑[Neutral](/docs/reference/engine/classes/Player.md) players with the matching [TeamColor](/docs/reference/engine/classes/Team.md), allowing them to use team‑only chat. Channels are removed if there are no remaining teams with an associated [TeamColor](/docs/reference/engine/classes/Team.md). |
| **RBXWhisper:[UserId1]_[UserId2]** | [TextChannel](/docs/reference/engine/classes/TextChannel.md) for whisper messages between two players, created when a player uses the `/whisper` command on another player. For example **RBXWhisper:2276836_505306092** is a [TextChannel](/docs/reference/engine/classes/TextChannel.md) for players with [UserIds](/docs/reference/engine/classes/Player.md) **2276836** and **505306092**. Inside whisper channels are two [TextSources](/docs/reference/engine/classes/TextSource\.md) associated with the respective [UserIds](/docs/reference/engine/classes/Player.md).

In the chat window, messages are colored the same as those in **RBXGeneral** and [TextChatMessage.PrefixText](/docs/reference/engine/classes/TextChatMessage.md) is modified to show whether a message was sent from or received by the local user.

Whisper channels are removed when either player leaves the experience. |

Note that the default [TextChannel.OnIncomingMessage](/docs/reference/engine/classes/TextChannel.md) callbacks can
be overwritten. Also note that you can edit, create, and remove
[TextChannels](/docs/reference/engine/classes/TextChannel.md) even if
[CreateDefaultTextChannels](/docs/reference/engine/classes/TextChatService.md)
is `true`.

Messages from different TextChannels can be separated into different tabs
in the chat window using [ChannelTabsConfiguration](/docs/reference/engine/classes/ChannelTabsConfiguration.md).

### Property: TextChatService.PlatformIntegratedChat

```json
{
  "type": "RolloutState",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

Requires `RobloxScript` security; not accessible from experience scripts.
Controls whether platform-integrated chat is enabled for the experience.
When set to [RolloutState.Enabled](/docs/reference/engine/enums/RolloutState.md),
[TextChatService.OnIncomingMessage](/docs/reference/engine/classes/TextChatService.md) and
[TextChannel.OnIncomingMessage](/docs/reference/engine/classes/TextChannel.md) callbacks from developer scripts are
not invoked, and only CoreScripts can set those callbacks. When set to
[RolloutState.Disabled](/docs/reference/engine/enums/RolloutState.md), behavior is explicitly disabled. Defaults to
[RolloutState.Default](/docs/reference/engine/enums/RolloutState.md).

## Methods

### Method: TextChatService:CanUserChatAsync

**Signature:** `TextChatService:CanUserChatAsync(userId: User): boolean`

Determines whether a user has permission to chat in experiences. Factors
such as parental control settings may prevent the user from sending
messages. Errors if the `userId` is not in the current server. Note that
this method can be used with all current player
[UserIds](/docs/reference/engine/classes/Player.md) in a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext](/docs/reference/engine/classes/Script.md) of [RunContext.Server](/docs/reference/engine/enums/RunContext.md) or
[RunContext.Legacy](/docs/reference/engine/enums/RunContext.md). This method can also be used in a
[LocalScript](/docs/reference/engine/classes/LocalScript.md) but only with the [UserId](/docs/reference/engine/classes/Player.md) of the
local player.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the user whose chat permission is being checked. |

**Returns:** `boolean` — A boolean indicating whether the user has permission to chat.

### Method: TextChatService:CanUsersChatAsync

**Signature:** `TextChatService:CanUsersChatAsync(userIdFrom: User, userIdTo: User): boolean`

Determines whether or not two users can receive messages from each other.
Both users must be in the current server, otherwise an error will occur.

Factors such as incompatible parental control settings or blocked status
may prevent the delivery of messages between users
([TextChannels](/docs/reference/engine/classes/TextChannel.md) internally use this result to determine
whether to deliver messages between users). Note that this method is only
available for use in a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext](/docs/reference/engine/classes/Script.md) of [RunContext.Server](/docs/reference/engine/enums/RunContext.md) or
[RunContext.Legacy](/docs/reference/engine/enums/RunContext.md).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userIdFrom` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the potential message sender. |
| `userIdTo` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the potential message receiver. |

**Returns:** `boolean` — A boolean indicating whether the two users can exchange messages.

### Method: TextChatService:CanUsersDirectChatAsync

**Signature:** `TextChatService:CanUsersDirectChatAsync(requesterUserId: User, userIds: Array): Array`

Determines whether a user has permission to chat directly with other users
in experiences based on their parental control settings, such as a whisper
channel between two users. To be used when:

- The line of communication is user-initiated (not developer- or
  gameplay-initiated).
- Access to the communication is closed and limited.

You may use this method to gate certain features in your experience
depending on the result.

When creating a [TextChannel](/docs/reference/engine/classes/TextChannel.md) for a direct chat, use
[TextChannel:SetDirectChatRequester](/docs/reference/engine/classes/TextChannel.md) to set the `requesterUserId` so
that the channel can determine whether to deliver messages between users.
When [TextChannel.DirectChatRequester](/docs/reference/engine/classes/TextChannel.md) is non-`nil`,
[TextChannels](/docs/reference/engine/classes/TextChannel.md) internally use this result to determine
whether to deliver messages between users.

Note that this method is only available for use in a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext](/docs/reference/engine/classes/Script.md) of [RunContext.Server](/docs/reference/engine/enums/RunContext.md) or
[RunContext.Legacy](/docs/reference/engine/enums/RunContext.md).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `requesterUserId` | `User` |  | The user who would have initiated the direct chat request. If the user is not in the current server, this method will error. |
| `userIds` | `Array` |  | A list of users who the `requesterUserId` would like to chat with directly. Users not in the current server are ignored. |

**Returns:** `Array` — A list of users who could participate in the direct chat request. If
none of the users can direct chat with the `requesterUserId`, the
result is an empty array.

**CanUsersDirectChatAsync**

This example checks if two users can chat, creates a new [TextChannel](/docs/reference/engine/classes/TextChannel.md),
and adds them to it.

```lua
local TextChatService = game:GetService("TextChatService")

local directChatParticipants = TextChatService:CanUsersDirectChatAsync(userId1, { userId2 })

-- Check for eligible participants
if #directChatParticipants > 0 then
	local directChannel = Instance.new("TextChannel")
	directChannel.Parent = TextChatService
	for _, participant in directChatParticipants do
		directChannel:AddUserAsync(participant)
	end
	return directChannel
end

warn("Could not create TextChannel. Not enough eligible users.")
return nil
```

### Method: TextChatService:DisplayBubble

**Signature:** `TextChatService:DisplayBubble(partOrCharacter: Instance, message: string): ()`

Displays a chat bubble above the provided part or player character, and
fires the [BubbleDisplayed](/docs/reference/engine/classes/TextChatService.md) event
with the parameters specified in this method. Can display bubbles for
non-player characters (NPCs) if you specify a part within the character,
such as its head.

Note that this method is only available for use in [LocalScript](/docs/reference/engine/classes/LocalScript.md), or
in a [Script](/docs/reference/engine/classes/Script.md) with [RunContext](/docs/reference/engine/classes/Script.md) of
[RunContext.Client](/docs/reference/engine/enums/RunContext.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `partOrCharacter` | `Instance` |  | The part or character that the bubble to be displayed above. |
| `message` | `string` |  | The text to be displayed in the chat bubble. |

**Returns:** `()`

### Method: TextChatService:GetChatGroupsAsync

**Signature:** `TextChatService:GetChatGroupsAsync(players: Instances): Array`

Returns a sorted array of arrays of chat group IDs for the given players.
Each chat group ID is a string that represents a communication-compatible
group within the current universe.

If two or more players share the same chat group ID, those players are
able to synchronously text chat with each other based on their age-check
status and chat settings.

This method is server-side only and intended for real-time use cases such
as matchmaking and teleporting. It is more efficient than calling
[TextChatService:CanUsersChatAsync()](/docs/reference/engine/classes/TextChatService.md) pairwise when evaluating many
players at once, since pairwise checks scale as N^2 and cannot be merged
across player lists. Chat group IDs are unique to the current universe,
may change over time, and should not be stored once the user has left the
experience. While you can hold onto the data returned for the purposes of
gameplay while the user is in the experience, this data should not be
stored after they've left.

To use this method, you must enable **Chat & Voice Groups APIs** in
**Experience Settings** ⟩ **Communication** in Roblox Studio and agree to
the Roblox Terms of Use.

In Roblox Studio this API is only available when the experience is running
in **Team Test**.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `players` | `Instances` |  | A list of [Players](/docs/reference/engine/classes/Player.md) currently in the experience to evaluate for text chat compatibility. |

**Returns:** `Array` — A sorted array of arrays of chat group ID strings. Players who share a
matching chat group ID are eligible to synchronously text chat with
each other.

**TeleportPlayerToBestChatServer**

This server-side example teleports a newly joined player to the server where
they can communicate with the largest number of existing players.
Compatibility is determined using `TextChatService:GetChatGroupsAsync`.

This example assumes that your experience maintains a universe-wide data
structure mapping active servers to chat group IDs and the number of users in
each group. That structure is represented here as a stub.

```lua
-- Server Script
local TextChatService = game:GetService("TextChatService")
local TeleportService = game:GetService("TeleportService")
local Players = game:GetService("Players")

local TARGET_PLACE_ID = 1234567890 -- Destination place ID

--[[
	Stubbed universe-wide server state.
	In practice, this data could be stored and updated using MemoryStore
	or another backend system.

	Example shape:
	ActiveServers = {
		{
			serverId = "abc",
			privateServerId = game.PrivateServerId,
			groupUserCounts = {
				groupA = 12,
				groupB = 5
			}
		},
		{
			serverId = "def",
			privateServerId = game.PrivateServerId,
			groupUserCounts = {
				groupB = 8
			}
		}
	}
]]
local ActiveServers = {}

local function teleportPlayerToBestServer(player)
	local success, chatGroups = pcall(function()
		return TextChatService:GetChatGroupsAsync({ player })
	end)

	if not success or not chatGroups then
		warn("Failed to retrieve chat groups for player:", player.UserId)
		return
	end

	-- Collect all chat group IDs the player is eligible for
	local playerGroupIds = {}
	for _, group in ipairs(chatGroups) do
		for _, groupId in ipairs(group) do
			playerGroupIds[groupId] = true
		end
	end

	local bestServer = nil
	local bestUserCount = 0

	-- Choose the server with the highest number of compatible users
	for _, server in ipairs(ActiveServers) do
		local compatibleUserCount = 0

		for groupId, userCount in pairs(server.groupUserCounts) do
			if playerGroupIds[groupId] then
				compatibleUserCount += userCount
			end
		end

		if compatibleUserCount > bestUserCount then
			bestUserCount = compatibleUserCount
			bestServer = server
		end
	end

	if not bestServer then
		warn("No suitable server found for player:", player.UserId)
		return
	end

	local ok, err = pcall(function()
		local teleportOptions = Instance.new("TeleportOptions")
		teleportOptions.ReservedServerId = bestServer.privateServerId
		TeleportService:TeleportAsync(
			TARGET_PLACE_ID,
			{ player },
			teleportOptions
		)
	end)

	if not ok then
		warn("Teleport failed:", err)
	end
end

Players.PlayerAdded:Connect(teleportPlayerToBestServer)
```

**Get Chat Groups Async**

Demonstrates [TextChatService:GetChatGroupsAsync()](/docs/reference/engine/classes/TextChatService.md).

```lua
local TextChatService = game:GetService("TextChatService")
local Players = game:GetService("Players")
local players = Players:GetPlayers()

local success, chatGroups = pcall(function()
  return TextChatService:GetChatGroupsAsync(players)
end)

if not success then
  warn("Failed to retrieve chat groups")
  return
end

for _, group in ipairs(chatGroups) do
  -- Each group contains chat group ID strings.
  -- Players who share a matching group ID can chat with each other.
  for _, groupId in ipairs(group) do
    print("Chat group ID:", groupId)
  end
end
```

## Events

### Event: TextChatService.BubbleDisplayed

**Signature:** `TextChatService.BubbleDisplayed(partOrCharacter: Instance, textChatMessage: TextChatMessage)`

Fires when [TextChatService:DisplayBubble()](/docs/reference/engine/classes/TextChatService.md) is called.

*Security: None · Capabilities: Chat*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `partOrCharacter` | `Instance` | The part or character that the bubble chat is displayed above. |
| `textChatMessage` | `TextChatMessage` | The [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md) associated with the bubble. |

### Event: TextChatService.MessageReceived

**Signature:** `TextChatService.MessageReceived(textChatMessage: TextChatMessage)`

Like [TextChannel.MessageReceived](/docs/reference/engine/classes/TextChannel.md), fires when
[TextChannel:DisplaySystemMessage()](/docs/reference/engine/classes/TextChannel.md) is invoked on the client, or
when the client receives a valid [TextChannel:SendAsync()](/docs/reference/engine/classes/TextChannel.md) response
from the server. This event is only fired on the client.

If the server's [TextChannel.ShouldDeliverCallback](/docs/reference/engine/classes/TextChannel.md) property is
bound and returns `false`, the client will not fire
[TextChatService.MessageReceived](/docs/reference/engine/classes/TextChatService.md).

Use the [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md) parameter to get the [TextSource](/docs/reference/engine/classes/TextSource.md)
and the text of the message (with [TextChatMessage.Text](/docs/reference/engine/classes/TextChatMessage.md)).

The [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md) parameter is the final result of any functions
bound to [TextChatService.OnIncomingMessage](/docs/reference/engine/classes/TextChatService.md) or
[TextChannel.OnIncomingMessage](/docs/reference/engine/classes/TextChannel.md).

*Security: None · Capabilities: Chat*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `textChatMessage` | `TextChatMessage` | The received [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md). |

### Event: TextChatService.SendingMessage

**Signature:** `TextChatService.SendingMessage(textChatMessage: TextChatMessage)`

Fires when [TextChannel:SendAsync()](/docs/reference/engine/classes/TextChannel.md) is called by the sending
client. Use this to allow placeholder messages to be shown to the user
while waiting for server response to [TextChannel:SendAsync()](/docs/reference/engine/classes/TextChannel.md).

*Security: None · Capabilities: Chat*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `textChatMessage` | `TextChatMessage` | The [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md) from the [TextChannel:SendAsync()](/docs/reference/engine/classes/TextChannel.md) call. |

## Callbacks

### Callback: TextChatService.OnBubbleAdded

**Signature:** `TextChatService.OnBubbleAdded(message: TextChatMessage, adornee: Instance): Tuple`

Called when a bubble chat is about to be displayed. This can only be
implemented on the client.

Use this to customize individual bubble chat messages. If this callback
returns a [BubbleChatMessageProperties](/docs/reference/engine/classes/BubbleChatMessageProperties.md), those properties will be
applied to the associated bubble, overriding
[BubbleChatConfiguration](/docs/reference/engine/classes/BubbleChatConfiguration.md) properties. If a [UICorner](/docs/reference/engine/classes/UICorner.md),
[UIGradient](/docs/reference/engine/classes/UIGradient.md), or [ImageLabel](/docs/reference/engine/classes/ImageLabel.md) is parented under
[BubbleChatMessageProperties](/docs/reference/engine/classes/BubbleChatMessageProperties.md), they will also override their
respective counterparts defined in [BubbleChatConfiguration](/docs/reference/engine/classes/BubbleChatConfiguration.md).

If the chat message is sent by a player, `message.TextSource` will
correspond to that player, and `adornee` will be `nil`.

If the chat message is sent via [TextChatService:DisplayBubble](/docs/reference/engine/classes/TextChatService.md),
`adornee` will be the `partOrCharacter` provided, and `message.TextSource`
will be `nil`.

When bound to the client sending a message, this callback is run twice:
first when the message is initially sent and received locally, then again
when the client receives the result of the filtered message from the
server.

*Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `TextChatMessage` |  | The incoming [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md). |
| `adornee` | `Instance` |  | The part or character the bubble chat message is attached to. |

**Returns:** `Tuple` — If a [BubbleChatMessageProperties](/docs/reference/engine/classes/BubbleChatMessageProperties.md) is returned, its properties
override the [BubbleChatConfiguration](/docs/reference/engine/classes/BubbleChatConfiguration.md) properties.

### Callback: TextChatService.OnChatWindowAdded

**Signature:** `TextChatService.OnChatWindowAdded(message: TextChatMessage): Tuple`

Called when a new message is about to be displayed in the chat window.
This can only be implemented on the client.

Use this to customize individual messages that appear in the chat window.
If this callback returns a [ChatWindowMessageProperties](/docs/reference/engine/classes/ChatWindowMessageProperties.md), those
properties will be applied to the associated message, overriding
[ChatWindowConfiguration](/docs/reference/engine/classes/ChatWindowConfiguration.md) properties. If a [UIGradient](/docs/reference/engine/classes/UIGradient.md) is
parented under [ChatWindowMessageProperties](/docs/reference/engine/classes/ChatWindowMessageProperties.md), it will also override
the [TextColor3](/docs/reference/engine/classes/ChatWindowConfiguration.md) property defined
in [ChatWindowConfiguration](/docs/reference/engine/classes/ChatWindowConfiguration.md).

When bound to the client sending a message, this callback is run twice:
first when the message is initially sent and received locally, then again
when the client receives the result of the filtered message from the
server.

*Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `TextChatMessage` |  | The incoming [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md). |

**Returns:** `Tuple` — If a [ChatWindowMessageProperties](/docs/reference/engine/classes/ChatWindowMessageProperties.md) is returned, its properties
override the [ChatWindowConfiguration](/docs/reference/engine/classes/ChatWindowConfiguration.md) properties.

### Callback: TextChatService.OnIncomingMessage

**Signature:** `TextChatService.OnIncomingMessage(message: TextChatMessage): Tuple`

Called when [TextChatService](/docs/reference/engine/classes/TextChatService.md) is receiving an incoming message. Can
only be implemented on the client.

Use this to decorate [TextChatMessages](/docs/reference/engine/classes/TextChatMessage.md). If this
callback returns a [TextChatMessageProperties](/docs/reference/engine/classes/TextChatMessageProperties.md), those properties are
merged with the [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md) parameter to create a new
[TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md).

When bound to the client sending a message, this callback is run twice;
first when the message is initially sent and received locally, and again
when the client receives the result of the filtered message from the
server.

Note that this [TextChatService.OnIncomingMessage](/docs/reference/engine/classes/TextChatService.md) callback runs
**before** any [TextChannel.OnIncomingMessage](/docs/reference/engine/classes/TextChannel.md) callbacks.

This should be defined only once in the source code. Multiple bindings
will override one another in a non‑deterministic manner. This callback is
not invoked when [TextChatService.PlatformIntegratedChat](/docs/reference/engine/classes/TextChatService.md) is set to
[RolloutState.Enabled](/docs/reference/engine/enums/RolloutState.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `TextChatMessage` |  | The incoming [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md). |

**Returns:** `Tuple` — If a [TextChatMessageProperties](/docs/reference/engine/classes/TextChatMessageProperties.md) is returned, those properties
are merged with the [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md) parameter to create a new
[TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md) with those properties, otherwise, if `nil` is
returned, then [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md) is not changed.

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