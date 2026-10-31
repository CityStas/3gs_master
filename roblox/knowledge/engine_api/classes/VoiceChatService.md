---
name: VoiceChatService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "**VoiceChatService** is responsible for voice chat's high-level functionality."
---

# Class: VoiceChatService

> **VoiceChatService** is responsible for voice chat's high-level functionality.

## Description

**VoiceChatService** is responsible for voice chat's high-level functionality.
This mostly consists of configuration options, and functions that are not
specifically-controlled by more-specific instances.

## Properties

### Property: VoiceChatService.DefaultDistanceAttenuation

```json
{
  "type": "VoiceChatDistanceAttenuationType",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Audio",
    "Chat"
  ]
}
```

This property controls the default distance attenuation curve assigned to
any generated [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) instances in the default voice chat
setup.

This property only has an effect if
[EnableDefaultVoice](/docs/reference/engine/classes/VoiceChatService.md) and
[UseAudioApi](/docs/reference/engine/classes/VoiceChatService.md) are both enabled, since
no [AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md) are otherwise generated.

### Property: VoiceChatService.EnableDefaultVoice

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Audio",
    "Chat"
  ]
}
```

When enabled, each voice-eligible player can be heard as though they were
speaking through their character. The implementation details of the voice
setup depend on [UseAudioApi](/docs/reference/engine/classes/VoiceChatService.md).

When [UseAudioApi](/docs/reference/engine/classes/VoiceChatService.md) is
[Enabled](/docs/reference/engine/enums/AudioApiRollout.md), disabling this property disables the
default setup, but [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) will still work. Conversely,
when [UseAudioApi](/docs/reference/engine/classes/VoiceChatService.md) is
[Disabled](/docs/reference/engine/enums/AudioApiRollout.md), disabling the default voice setup
effectively disables voice chat altogether.

### Property: VoiceChatService.EnableVoiceVolumeControls

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
  "category": "Behavior",
  "capabilities": [
    "Audio",
    "Chat"
  ]
}
```

This [RolloutState](/docs/reference/engine/enums/RolloutState.md) property controls whether Roblox's built-in voice
chat volume controls are available to players, including a global voice
chat volume slider and per-user volume adjustments.

When set to [Enabled](/docs/reference/engine/enums/RolloutState.md), these controls are available to
players. When set to [Disabled](/docs/reference/engine/enums/RolloutState.md), the built-in controls
are hidden, though creators can still implement their own custom voice
volume controls. [Default](/docs/reference/engine/enums/RolloutState.md) follows the default for this
feature.

If [UseAudioApi](/docs/reference/engine/classes/VoiceChatService.md) is disabled, this
property has no effect and built-in controls will be hidden.

### Property: VoiceChatService.UseAudioApi

```json
{
  "type": "AudioApiRollout",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Audio",
    "Chat"
  ]
}
```

If [Enabled](/docs/reference/engine/enums/AudioApiRollout.md), the voice chat setup is represented and
controlled by [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) objects. More specifically:

- An [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) will be created and parented to each
  voice-eligible [Player](/docs/reference/engine/classes/Player.md).
- An [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) will be created and parented to each
  voice-eligible player's [Player.Character](/docs/reference/engine/classes/Player.md).
- An [AudioListener](/docs/reference/engine/classes/AudioListener.md) will be created and parented to
  [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md).

You can disable the default setup by setting
[VoiceChatService.EnableDefaultVoice](/docs/reference/engine/classes/VoiceChatService.md) to `false`.

If [Disabled](/docs/reference/engine/enums/AudioApiRollout.md), the voice chat setup is done through
an internal-only system.

Currently, setting this to [Automatic](/docs/reference/engine/enums/AudioApiRollout.md) has the same
meaning as [Disabled](/docs/reference/engine/enums/AudioApiRollout.md). However, in the future,
[Automatic](/docs/reference/engine/enums/AudioApiRollout.md) will become
[Enabled](/docs/reference/engine/enums/AudioApiRollout.md), so that new experiences can achieve
greater customization over voice.

## Methods

### Method: VoiceChatService:GetChatGroupsAsync

**Signature:** `VoiceChatService:GetChatGroupsAsync(players: Instances): Array`

Returns a sorted array of arrays of chat group IDs for the given players.
Each chat group ID is a string that represents a communication-compatible
group within the current universe.

If two or more players share the same chat group ID, those players are
eligible to voice chat with each other based on their age-check status,
voice chat eligibility, and communication settings.

This method is server-side only and intended for real-time use cases such
as matchmaking and teleporting. Chat group IDs are unique to the current
universe, may change over time, and should not be stored once the user has
left the experience. While you can hold onto the data returned for the
purposes of gameplay while the user is in the experience, this data should
not be stored after they've left.

To use this method, you must enable **Chat & Voice Groups APIs** in
**Experience Settings** ⟩ **Communication** in Roblox Studio and agree to
the Roblox Terms of Use.

In Roblox Studio this API is only available when the experience is running
in **Team Test**.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Audio, Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `players` | `Instances` |  | A list of [Players](/docs/reference/engine/classes/Player.md) currently in the experience to evaluate for voice chat compatibility. |

**Returns:** `Array` — A sorted array of arrays of chat group ID strings. Players who share a
matching chat group ID are eligible to voice chat with each other.

**TeleportPlayerToBestChatServer**

This server-side example teleports a newly joined player to the server where
they can communicate with the largest number of existing players.
Compatibility is determined using `VoiceChatService:GetChatGroupsAsync`.

This example assumes that your experience maintains a universe-wide data
structure mapping active servers to chat group IDs and the number of users in
each group. That structure is represented here as a stub.

```lua
-- Server Script
local VoiceChatService = game:GetService("VoiceChatService")
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
		return VoiceChatService:GetChatGroupsAsync({ player })
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

Demonstrates [VoiceChatService:GetChatGroupsAsync()](/docs/reference/engine/classes/VoiceChatService.md).

```lua
local VoiceChatService = game:GetService("VoiceChatService")
local Players = game:GetService("Players")
local players = Players:GetPlayers()

local success, chatGroups = pcall(function()
	return VoiceChatService:GetChatGroupsAsync(players)
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

### Method: VoiceChatService:IsVoiceEnabledForUserIdAsync

**Signature:** `VoiceChatService:IsVoiceEnabledForUserIdAsync(userId: User): boolean`

Returns whether or not the given user has voice enabled. On the
client-side, this can only be used to check the voice status of the local
player. On the server-side, this can only check the voice status for
players in that server.

This function can throw an error if the HTTP call fails.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Audio, Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) to check. |

**Returns:** `boolean` — If that user has voice enabled.

**Is Voice Enabled For User Id Async**

Demonstrates [VoiceChatService:IsVoiceEnabledForUserIdAsync()](/docs/reference/engine/classes/VoiceChatService.md).

```lua
local Players = game:GetService("Players")
local VoiceChatService = game:GetService("VoiceChatService")

local localPlayer = Players.LocalPlayer
local success, enabled = pcall(function()
	return VoiceChatService:IsVoiceEnabledForUserIdAsync(localPlayer.UserId)
end)
if success and enabled then
	print("Voice chat enabled!")
end
```

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