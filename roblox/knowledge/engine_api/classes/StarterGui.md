---
name: StarterGui
last_updated: 2026-10-30T19:55:53Z
inherits:
  - BasePlayerGui
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "A container for LayerCollector objects to be copied into the PlayerGui of Players. Also provides a range of functions for interacting with the CoreGui."
---

# Class: StarterGui

> A container for [LayerCollector](/docs/reference/engine/classes/LayerCollector.md) objects to be copied into the
> [PlayerGui](/docs/reference/engine/classes/PlayerGui.md) of [Players](/docs/reference/engine/classes/Player.md). Also provides a range of
> functions for interacting with the [CoreGui](/docs/reference/engine/classes/CoreGui.md).

## Description

[StarterGui](/docs/reference/engine/classes/StarterGui.md) is a container object designed to hold
[LayerCollector](/docs/reference/engine/classes/LayerCollector.md) objects such as [ScreenGuis](/docs/reference/engine/classes/ScreenGui.md).

When a [Player.Character](/docs/reference/engine/classes/Player.md) spawns, the contents of their
[PlayerGui](/docs/reference/engine/classes/PlayerGui.md) (if any) are emptied. Children of the [StarterGui](/docs/reference/engine/classes/StarterGui.md) are
then copied along with their descendants into the [PlayerGui](/docs/reference/engine/classes/PlayerGui.md). Note,
however, that [LayerCollector](/docs/reference/engine/classes/LayerCollector.md) objects such as
[ScreenGuis](/docs/reference/engine/classes/ScreenGui.md) with their
[ResetOnSpawn](/docs/reference/engine/classes/LayerCollector.md) property set to `false` will
only be placed into each player's [PlayerGui](/docs/reference/engine/classes/PlayerGui.md) once and will not be
deleted when the [Player](/docs/reference/engine/classes/Player.md) respawns.

[StarterGui](/docs/reference/engine/classes/StarterGui.md) also includes a range of functions allowing you to interact
with the [CoreGui](/docs/reference/engine/classes/CoreGui.md). For example [StarterGui:SetCoreGuiEnabled()](/docs/reference/engine/classes/StarterGui.md)
can be used to disable elements of the [CoreGui](/docs/reference/engine/classes/CoreGui.md), and
[StarterGui:SetCore()](/docs/reference/engine/classes/StarterGui.md) can perform a range of functions including
creating notifications and system messages.

## Properties

### Property: StarterGui.ClipsDescendantsSupportsRotation

```json
{
  "type": "RolloutState",
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
    "UI"
  ]
}
```

If `true`, the [ClipsDescendants](/docs/reference/engine/classes/GuiObject.md)
property of a [GuiObject](/docs/reference/engine/classes/GuiObject.md) clips its **rotated** descendants.

### Property: StarterGui.RtlTextSupport

```json
{
  "type": "RtlTextSupport",
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
    "UI"
  ]
}
```

This property determines whether right-to-left (RTL) text layout is
applied to the text of [GuiObjects](/docs/reference/engine/classes/GuiObject.md) in the experience,
which is needed to correctly display languages written right-to-left, such
as Arabic and Hebrew.

The default value is [RtlTextSupport.Default](/docs/reference/engine/enums/RtlTextSupport.md). Both
[RtlTextSupport.Default](/docs/reference/engine/enums/RtlTextSupport.md) and [RtlTextSupport.Enabled](/docs/reference/engine/enums/RtlTextSupport.md) turn RTL
text layout support on, while [RtlTextSupport.Disabled](/docs/reference/engine/enums/RtlTextSupport.md) turns it off.

### Property: StarterGui.ScreenOrientation

```json
{
  "type": "ScreenOrientation",
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
    "UI"
  ]
}
```

This property sets the preferred screen orientation mode for users with
mobile devices. For the different modes available, see
[ScreenOrientation](/docs/reference/engine/enums/ScreenOrientation.md).

By default, this property is set to
[Sensor](/docs/reference/engine/enums/ScreenOrientation.md), meaning the experience is
displayed depending on the best match to the device's current orientation,
either landscape (left/right) or portrait.

When a [Player](/docs/reference/engine/classes/Player.md) joins the experience on a mobile device, this
property determines the device's starting orientation and sets that
player's [PlayerGui.ScreenOrientation](/docs/reference/engine/classes/PlayerGui.md) accordingly. You can also get
the player's current screen orientation through
[PlayerGui.CurrentScreenOrientation](/docs/reference/engine/classes/PlayerGui.md), useful when using one of the
"sensor" [ScreenOrientation](/docs/reference/engine/enums/ScreenOrientation.md) settings.

Note that changing this property will not change the screen orientation
for [Players](/docs/reference/engine/classes/Player.md) already in the experience. To change the
orientation for an existing player, use their
[PlayerGui.ScreenOrientation](/docs/reference/engine/classes/PlayerGui.md) property.

### Property: StarterGui.ShowDevelopmentGui

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
    "UI"
  ]
}
```

This property determines whether the contents of [StarterGui](/docs/reference/engine/classes/StarterGui.md) is
visible in Studio.

### Property: StarterGui.VirtualCursorMode

```json
{
  "type": "VirtualCursorMode",
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
    "UI"
  ]
}
```

This property determines whether the gamepad virtual cursor, which lets
players move a pointer across on-screen [GuiObjects](/docs/reference/engine/classes/GuiObject.md) using
a controller, is enabled.

The default value is [VirtualCursorMode.Default](/docs/reference/engine/enums/VirtualCursorMode.md). Setting it to
[VirtualCursorMode.Enabled](/docs/reference/engine/enums/VirtualCursorMode.md) turns the virtual cursor on and
[VirtualCursorMode.Disabled](/docs/reference/engine/enums/VirtualCursorMode.md) turns it off. When a player is in VR,
the virtual cursor is always active regardless of this property's value.

### Property: StarterGui.ResetPlayerGuiOnSpawn

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

> **Deprecated:** This property is deprecated. Use [LayerCollector.ResetOnSpawn](/docs/reference/engine/classes/LayerCollector.md) to control the resetting behavior for individual [LayerCollector](/docs/reference/engine/classes/LayerCollector.md) objects.

If set to true, each child parented to the [StarterGui](/docs/reference/engine/classes/StarterGui.md) will be
cloned into a player's [PlayerGui](/docs/reference/engine/classes/PlayerGui.md) when that player's character is
respawned.

If one of the children is a PlayerGui and it has its PlayerGui property
set to false, it will not be cloned.

### Property: StarterGui.ProcessUserInput *(hidden)*

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "UI"
  ]
}
```

Allows [StarterGui](/docs/reference/engine/classes/StarterGui.md) to process input like [PlayerGui](/docs/reference/engine/classes/PlayerGui.md) and
[CoreGui](/docs/reference/engine/classes/CoreGui.md) do. The default value is `false`.

## Methods

### Method: StarterGui:GetCore

**Signature:** `StarterGui:GetCore(parameterName: string): Variant`

This method returns data set or made available by Roblox's core scripts.
The first and only parameter is a string that selects the information to
be fetched. The following sections describe the strings and the data they
return by this function.

Calling this method may yield. Many of these also register an equivalent
[SetCore()](/docs/reference/engine/classes/StarterGui.md) function (these are marked with an
asterisk).

##### PointsNotificationsActive \*

Returns `true` if player point notifications are enabled.

##### BadgesNotificationsActive \*

Returns `true` if badge notifications are enabled.

##### AvatarContextMenuEnabled \*

Returns `true` if the
[Avatar Context Menu](/docs/en-us/players/avatar-context-menu.md) is enabled.

##### ChatActive \*

Returns whether the chat is active or not. This is indicated by the
selection state of the top bar's chat icon.

##### ChatWindowSize \*

Returns the size of the chat window as a [UDim2](/docs/reference/engine/datatypes/UDim2.md).

##### ChatWindowPosition \*

Returns the size of the chat window as a [UDim2](/docs/reference/engine/datatypes/UDim2.md).

##### ChatBarDisabled \*

Returns `true` if the chat bar is disabled.

##### GetBlockedUserIds

Returns a list of [UserIds](/docs/reference/engine/classes/Player.md) associated with users that
have been blocked by the local player.

##### PlayerBlockedEvent

Returns a [BindableEvent](/docs/reference/engine/classes/BindableEvent.md) that is fired whenever a player is blocked
by the local player.

##### PlayerUnblockedEvent

Returns a [BindableEvent](/docs/reference/engine/classes/BindableEvent.md) that is fired whenever a player is
unblocked by the local player.

##### PlayerMutedEvent

Returns a [BindableEvent](/docs/reference/engine/classes/BindableEvent.md) that is fired whenever a player is muted
by the local player.

##### PlayerUnmutedEvent

Returns a [BindableEvent](/docs/reference/engine/classes/BindableEvent.md) that is fired whenever a player is unmuted
by the local player.

##### PlayerFriendedEvent

Returns a [BindableEvent](/docs/reference/engine/classes/BindableEvent.md) that is fired whenever a player is
connected by the local player.

##### PlayerUnfriendedEvent

Returns a [BindableEvent](/docs/reference/engine/classes/BindableEvent.md) that is fired whenever a player is
unconnected by the local player.

##### DevConsoleVisible \*

Returns `true` if the
[Developer Console](/docs/en-us/studio/developer-console.md) is visible.

##### VRRotationIntensity

Returns a string describing the camera rotation sensitivity in VR: `Low`,
`High` and `Smooth`. This will not be available unless
[VRService.VREnabled](/docs/reference/engine/classes/VRService.md) is `true`.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `parameterName` | `string` |  | The name of the core parameter to retrieve, such as `"PointsNotificationsActive"` or `"ChatActive"`. |

**Returns:** `Variant` — The value associated with the specified core parameter name, whose
type depends on the parameter queried.

### Method: StarterGui:GetCoreGuiEnabled

**Signature:** `StarterGui:GetCoreGuiEnabled(coreGuiType: CoreGuiType): boolean`

This function returns whether the given [CoreGuiType](/docs/reference/engine/enums/CoreGuiType.md)is enabled, or
if it has been disabled using [StarterGui:SetCoreGuiEnabled()](/docs/reference/engine/classes/StarterGui.md). This
function should be called on the client.

Note that setting `"TopbarEnabled"` to `false` using
[SetCore()](/docs/reference/engine/classes/StarterGui.md) hides all
[CoreGuiTypes](/docs/reference/engine/enums/CoreGuiType.md) but does not affect the result of this
function.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `coreGuiType` | `CoreGuiType` |  | The given [CoreGuiType](/docs/reference/engine/enums/CoreGuiType.md). |

**Returns:** `boolean` — Whether the given [CoreGuiType](/docs/reference/engine/enums/CoreGuiType.md) is enabled.

**Checking if a Core GUI is Enabled**

The below example would print whether or not the player list is visible to the
LocalPlayer.

```lua
local StarterGui = game:GetService("StarterGui")

print(StarterGui:GetCoreGuiEnabled("PlayerList"))
```

### Method: StarterGui:SetCore

**Signature:** `StarterGui:SetCore(parameterName: string, value: Variant): ()`

This method (not to be confused with
[SetCoreGuiEnabled()](/docs/reference/engine/classes/StarterGui.md)) exposes a
variety of functionality defined by Roblox's core scripts, such as sending
notifications, toggling notifications for badges/points, defining a
callback for the reset button, or toggling the topbar.

The first parameter is a string that selects the functionality with which
the call will interact. It may be necessary to call this method multiple
times using [LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md) in case the respective core script
has not yet loaded (or if it has been disabled entirely).

The following table describes the strings that may be accepted as the
first parameter. The parameters that should follow are dependent on the
functionality that will be used and are described in sub-tables.

##### ChatActive

Controls whether the chat is active.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `active` | boolean | (required) | Determines whether the chat should be made active. |

##### PointsNotificationsActive

Controls whether notifications for earned player points will appear.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `active` | boolean | (required) | Determines whether notifications for earned player points will appear. |

##### BadgesNotificationsActive

Controls whether notifications for earned badges will appear.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `active` | boolean | (required) | Determines whether notifications for earned badges will appear. |

##### ResetButtonCallback

Determines the behavior, if any, of the reset button given a boolean or a
[BindableEvent](/docs/reference/engine/classes/BindableEvent.md) to be fired when a player requests to reset.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `enabled` | boolean | (required) | Determines whether the reset button retains its default behavior. |
| **OR** |
| `callback` | [BindableEvent](/docs/reference/engine/classes/BindableEvent.md) | (required) | A [BindableEvent](/docs/reference/engine/classes/BindableEvent.md) to be fired when the player confirms they want to reset. |

##### ChatMakeSystemMessage

Display a formatted message in the chat. Using this method requires the
experience's [TextChatService.ChatVersion](/docs/reference/engine/classes/TextChatService.md) to be set to
[LegacyChatService](/docs/reference/engine/enums/ChatVersion.md), although legacy chat is
**deprecated** and usage is discouraged. For experiences using the current
[TextChatService](/docs/reference/engine/classes/TextChatService.md), refer to
[TextChannel:DisplaySystemMessage()](/docs/reference/engine/classes/TextChannel.md).

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `configTable` | dictionary | (required) | A dictionary of information describing the message (see below). |

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `Text` | string | (required) | The message to display. |
| `Color` | [Color3](/docs/reference/engine/datatypes/Color3.md) | [Color3.fromRGB(255, 255, 243)](/docs/reference/engine/datatypes/Color3.md) | Text color of the message. |
| `Font` | [Font](/docs/reference/engine/enums/Font.md) | `SourceSansBold` | Font of the message. |
| `TextSize` | integer | `18` | Text size of the message. |

##### SendNotification

Causes a non-intrusive notification to appear at the bottom right of the
screen. The notification may have up to two buttons.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `configTable` | dictionary | (required) | A dictionary of information describing the notification (see below). |

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `Title` | string | (required) | The title of the notification. |
| `Text` | string | (required) | The main text of the notification. |
| `Icon` | string |  | The image to display with the notification. |
| `Duration` | number | `5` | Duration (in seconds) the notification should stay visible. |
| `Callback` | [BindableFunction](/docs/reference/engine/classes/BindableFunction.md) |  | A [BindableFunction](/docs/reference/engine/classes/BindableFunction.md) that should be invoked with the text of the button pressed by the player. |
| `Button1` | string |  | The text to display on the first button. |
| `Button2` | string |  | The text to display on the second button. |

##### TopbarEnabled

Determines whether the topbar is displayed. Disabling the topbar will also
disable all [CoreGuis](/docs/reference/engine/classes/CoreGui.md) such as the chat, inventory, and
player list (for example, those set with
[SetCoreGuiEnabled](/docs/reference/engine/classes/StarterGui.md)).

When disabled, the region the topbar once occupied will still capture
mouse events; however, buttons placed there will not respond to clicks.
The origin of GUI space will still be offset 36 pixels from the top of the
screen.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `enabled` | boolean | (required) | Determines whether the topbar should be visible. |

##### DevConsoleVisible

Determines whether the
[Developer Console](/docs/en-us/studio/developer-console.md) is visible.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `visibility` | boolean | (required) | Determines whether the console is visible. |

##### PromptSendFriendRequest

Prompts the current player to send a friend request to the given
[Player](/docs/reference/engine/classes/Player.md).

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `player` | [Player](/docs/reference/engine/classes/Player.md) | (required) | The player to which the friend request should be sent. |

##### PromptUnfriend

Prompts the current player to remove a given [Player](/docs/reference/engine/classes/Player.md) from their
friends list.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `player` | [Player](/docs/reference/engine/classes/Player.md) | (required) | The player who should be unconnected. |

##### PromptBlockPlayer

Prompts the current player to block the given [Player](/docs/reference/engine/classes/Player.md).

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `player` | [Player](/docs/reference/engine/classes/Player.md) | (required) | The player who should be blocked. |

##### PromptUnblockPlayer

Prompts the current player to unblock the given [Player](/docs/reference/engine/classes/Player.md).

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `player` | [Player](/docs/reference/engine/classes/Player.md) | (required) | The player who should be unblocked. |

##### AvatarContextMenuEnabled

Determines whether the
[Avatar Context Menu](/docs/en-us/players/avatar-context-menu.md) is enabled.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `enabled` | boolean | (required) | Determines whether the context menu is enabled. |

##### AvatarContextMenuTarget

Forcibly opens the
[Avatar Context Menu](/docs/en-us/players/avatar-context-menu.md).

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `player` | [Player](/docs/reference/engine/classes/Player.md) | (required) | The player on whom the context menu will be opened. |

##### AddAvatarContextMenuOption

Adds an option to the
[Avatar Context Menu](/docs/en-us/players/avatar-context-menu.md).

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `option` | [AvatarContextMenuOption](/docs/reference/engine/enums/AvatarContextMenuOption.md) | (required) | Option to add. |
| **OR** |
| `option` | table | (required) | A two-element table, where the first is the name of the custom action, and the second is a [BindableEvent](/docs/reference/engine/classes/BindableEvent.md) which will be fired with a player was selected when the option was activated. |

##### RemoveAvatarContextMenuOption

Removes an option to the
[Avatar Context Menu](/docs/en-us/players/avatar-context-menu.md). The
`option` argument must be the same as what was used with
`"AddAvatarContextMenuOption"` (see above).

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `option` | Variant | (required) | The same value provided to **AddAvatarContextMenuOption**. |

##### AvatarContextMenuTheme

Configures the customizable
[Avatar Context Menu](/docs/en-us/players/avatar-context-menu.md) which is an
opt-in feature that allows easy player-to-player social interaction via
custom actions, such as initiating trades, battles, and more. For more
info on how to customize its theme, see the
[Avatar Context Menu](/docs/en-us/players/avatar-context-menu.md) article.

##### CoreGuiChatConnections

Sets up a bindable gateway connection between the [CoreGui](/docs/reference/engine/classes/CoreGui.md) topbar's
chat button and the legacy chat system. The second parameter must be a
table of [BindableEvents](/docs/reference/engine/classes/BindableEvent.md) and
[BindableFunctions](/docs/reference/engine/classes/BindableFunction.md).

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `parameterName` | `string` |  | Selects the functionality with which the call will interact. |
| `value` | `Variant` |  | A table of [BindableEvents](/docs/reference/engine/classes/BindableEvent.md) and [BindableFunctions](/docs/reference/engine/classes/BindableFunction.md). |

**Returns:** `()`

**StarterGui Setting Core GUI**

```lua
local StarterGui = game:GetService("StarterGui")

StarterGui:SetCore("AvatarContextMenuTheme", {
	BackgroundImage = "",
	BackgroundTransparency = 0.5,
	BackgroundColor = Color3.fromRGB(111, 145, 242),
	NameTagColor = Color3.fromRGB(0, 0, 200),
	NameUnderlineColor = Color3.fromRGB(213, 233, 255),
	ButtonFrameColor = Color3.fromRGB(15, 24, 65),
	ButtonFrameTransparency = 0.2,
	ButtonUnderlineColor = Color3.fromRGB(213, 233, 255),
	Font = Enum.Font.SciFi,
})
```

### Method: StarterGui:SetCoreGuiEnabled

**Signature:** `StarterGui:SetCoreGuiEnabled(coreGuiType: CoreGuiType, enabled: boolean): ()`

This function sets whether the [CoreGui](/docs/reference/engine/classes/CoreGui.md) element associated with the
given [CoreGuiType](/docs/reference/engine/enums/CoreGuiType.md) is enabled or disabled.

The top bar cannot be disabled using this function. To disable it, set
`"TopbarEnabled"` to `false` using [StarterGui:SetCore()](/docs/reference/engine/classes/StarterGui.md).

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `coreGuiType` | `CoreGuiType` |  | The given [CoreGuiType](/docs/reference/engine/enums/CoreGuiType.md). |
| `enabled` | `boolean` |  | Whether to enable or disable the given [CoreGuiType](/docs/reference/engine/enums/CoreGuiType.md). |

**Returns:** `()`

## Inherited Members

### From [BasePlayerGui](/docs/reference/engine/classes/BasePlayerGui.md)

- **Method `GetGuiObjectsAtPosition(x: int, y: int): Instances`**: Returns a list of all GuiObject instances occupying the given

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