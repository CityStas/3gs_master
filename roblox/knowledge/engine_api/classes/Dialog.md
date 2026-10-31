---
name: Dialog
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Creates NPC billboard-style dialog bubbles."
---

# Class: Dialog

> Creates NPC billboard-style dialog bubbles.

## Description

The Dialog object allows users to create non-player characters (NPCs) that
players can talk to using a list of choices. The Dialog object can be inserted
into a part such as a Humanoid's head, and then a player will see a speech
bubble above the part that they can click on to start a conversation. The
creator of a place can choose what choices the player can say by inserting
[DialogChoice](/docs/reference/engine/classes/DialogChoice.md) objects into the dialog.

## Properties

### Property: Dialog.BehaviorType

```json
{
  "type": "DialogBehaviorType",
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

The BehaviorType of a Dialog determines whether multiple players can
interact with a dialog at once. The default value for this property is
SinglePlayer.

#### SinglePlayer

When a Dialog is configured to SinglePlayer, only one player can interact
with it at a time. As soon as a player engages with a dialog, other
players will not be able to initiate the dialog until the first player is
finished.

While a player is engaged with a dialog, the other players will see the
dialog choices of the player who started the dialog, along with the
responses.

#### MultiplePlayers

When a Dialog is set to MultiplePlayers, any player can initiate a dialog
at any time, even if another player has already initiated the dialog.
Unlike SinglePlayer however, Dialogs set to MultiplePlayers will not show
the dialog choices and responses to anyone but the player in the
conversation.

**Behavior Type**

Demonstrates [Dialog.BehaviorType](/docs/reference/engine/classes/Dialog.md).

```lua
local Workspace = game:GetService("Workspace")

local singlePlayerPartSetup = Instance.new("Part")
singlePlayerPartSetup.Name = "SinglePlayerPart"
singlePlayerPartSetup.Parent = Workspace
local multiplePlayersPartSetup = Instance.new("Part")
multiplePlayersPartSetup.Name = "MultiplePlayersPart"
multiplePlayersPartSetup.Parent = Workspace

local singlePlayerDialog = Instance.new("Dialog")
local singlePlayerPart = Workspace.SinglePlayerPart
singlePlayerDialog.BehaviorType = Enum.DialogBehaviorType.SinglePlayer
singlePlayerDialog.InitialPrompt = "Only one person can interact with me at once."
singlePlayerDialog.Parent = singlePlayerPart

local multiplePlayersDialog = Instance.new("Dialog")
local multiplePlayersPart = Workspace.MultiplePlayersPart
multiplePlayersDialog.BehaviorType = Enum.DialogBehaviorType.MultiplePlayers
multiplePlayersDialog.InitialPrompt = "Any number of players can interact with me at once."
multiplePlayersDialog.Parent = multiplePlayersPart
```

### Property: Dialog.ConversationDistance

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
    "UI"
  ]
}
```

The maximum distance in studs between the player's character and the
Dialog's parent [BasePart](/docs/reference/engine/classes/BasePart.md) at which the player can click on the
speech bubble to begin or continue a conversation. If the player moves
further than this distance from the parent part, they cannot initiate the
dialog. The engine uses this value to select the nearest available Dialog
when multiple are in range.

Default is 25.

### Property: Dialog.GoodbyeChoiceActive

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

Toggles whether the goodbye option will be displayed. If true, the dialog
will display the content of [Dialog.GoodbyeDialog](/docs/reference/engine/classes/Dialog.md) as the last
option after other dialog choices. Clicking on the goodbye option will
exit the dialog.

### Property: Dialog.GoodbyeDialog

```json
{
  "type": "string",
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

The text displayed as the goodbye option at the bottom of the dialog
choices list. When [Dialog.GoodbyeChoiceActive](/docs/reference/engine/classes/Dialog.md) is true, this string
appears as the final selectable choice; clicking it ends the conversation.
When [Dialog.GoodbyeChoiceActive](/docs/reference/engine/classes/Dialog.md) is false, this property has no
visible effect.

Default is an empty string.

### Property: Dialog.InitialPrompt

```json
{
  "type": "string",
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

The text that the NPC displays inside the speech bubble when a player
first begins the conversation. This is the opening line that appears
before the player selects from [DialogChoice](/docs/reference/engine/classes/DialogChoice.md) options nested under
this Dialog.

Default is an empty string.

### Property: Dialog.InUse

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
    "UI"
  ]
}
```

A read-only runtime indicator that is true whenever at least one player is
currently engaged in this dialog conversation. The engine sets this to
true when a player begins talking and resets it to false when all
participants leave. This property is not serialized and always starts as
false when the place loads. Scripts can read this property but cannot set
it directly.

Default is false.

### Property: Dialog.Purpose

```json
{
  "type": "DialogPurpose",
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

Controls which icon appears on the dialog's speech bubble indicator.
Accepts a value from the [DialogPurpose](/docs/reference/engine/enums/DialogPurpose.md) enum:

- **Quest** -- displays an exclamation mark (!)
- **Help** -- displays a question mark (?)
- **Shop** -- displays a dollar sign ($)

Default is Help.

### Property: Dialog.Tone

```json
{
  "type": "DialogTone",
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

Controls the color accent on the dialog's speech bubble. Accepts a value
from the [DialogTone](/docs/reference/engine/enums/DialogTone.md) enum:

- **Neutral** -- blue accent bar
- **Friendly** -- green accent bar
- **Enemy** -- red accent bar

Default is Neutral.

### Property: Dialog.TriggerDistance

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
    "UI"
  ]
}
```

The maximum distance in studs from the Dialog's parent [BasePart](/docs/reference/engine/classes/BasePart.md) at
which the dialog's trigger indicator becomes visible to a player. When a
player's character is within this distance, the speech bubble icon appears
over the parent part, inviting interaction. The value is clamped between 0
and 400.

Default is 0, which effectively disables the distance-based trigger
indicator; the player must be within [Dialog.ConversationDistance](/docs/reference/engine/classes/Dialog.md)
to see and interact with the dialog.

### Property: Dialog.TriggerOffset

```json
{
  "type": "Vector3",
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

A [Vector3](/docs/reference/engine/datatypes/Vector3.md) offset in studs that shifts the position of the
dialog's speech bubble indicator relative to the Dialog's parent
[BasePart](/docs/reference/engine/classes/BasePart.md). Use this to position the indicator above or beside the
NPC rather than at the part's center. This property participates in model
scaling.

Default is (0, 0, 0).

## Methods

### Method: Dialog:GetCurrentPlayers

**Signature:** `Dialog:GetCurrentPlayers(): Instances`

The GetCurrentPlayers function of a Dialog will return a list of
[Player](/docs/reference/engine/classes/Player.md) currently using the Dialog. If there are no players using
the dialog then the returned list will be empty.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `Instances` — A list of [Player](/docs/reference/engine/classes/Player.md) objects currently engaged in the Dialog.

**Dialog:GetCurrentPlayers**

```lua
local dialog = script.Parent

local function onChoiceSelected(_player, _choice)
	local currentPlayers = dialog:GetCurrentPlayers()
	print("The current players in the dialog:")
	for _, player in ipairs(currentPlayers) do
		print(player)
	end
end

dialog.DialogChoiceSelected:Connect(onChoiceSelected)
```

## Events

### Event: Dialog.DialogChoiceSelected

**Signature:** `Dialog.DialogChoiceSelected(player: Instance, dialogChoice: Instance)`

Fired when a player chooses something to say, through a [Dialog](/docs/reference/engine/classes/Dialog.md)
instance.

This event is client-side only and will not fire on the server. It should
be connected to in either a [LocalScript](/docs/reference/engine/classes/LocalScript.md) or a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md)
required by a [LocalScript](/docs/reference/engine/classes/LocalScript.md).

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Instance` | The [Player](/docs/reference/engine/classes/Player.md) who made the selection. |
| `dialogChoice` | `Instance` | The [DialogChoice](/docs/reference/engine/classes/DialogChoice.md) that was selected by the player. |

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