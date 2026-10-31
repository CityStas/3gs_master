---
name: PlayerGui
last_updated: 2026-10-30T19:55:53Z
inherits:
  - BasePlayerGui
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - PlayerReplicated
summary: "A container that holds a player's UI."
---

# Class: PlayerGui

> A container that holds a player's UI.

## Description

The `PlayerGui` container stores objects that create the player's GUI. If a
[ScreenGui](/docs/reference/engine/classes/ScreenGui.md) is a descendant of `PlayerGui`, any [GuiObject](/docs/reference/engine/classes/GuiObject.md) inside
that [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) displays on the player's screen. Any
[LocalScript](/docs/reference/engine/classes/LocalScript.md) will also run if it is inserted into a `PlayerGui`.

When a player first joins the experience, their `PlayerGui` is automatically
inserted into their [Player](/docs/reference/engine/classes/Player.md) object. When the player's
[Player.Character](/docs/reference/engine/classes/Player.md) spawns for the first time, all of the contents of
[StarterGui](/docs/reference/engine/classes/StarterGui.md) are automatically copied into the player's `PlayerGui`. If
[StarterGui.ResetPlayerGuiOnSpawn](/docs/reference/engine/classes/StarterGui.md) is set to `true`, all the contents of
a player's `PlayerGui` are cleared and replaced with the contents of
[StarterGui](/docs/reference/engine/classes/StarterGui.md) every time the player's character respawns.

Note that if [Players.CharacterAutoLoads](/docs/reference/engine/classes/Players.md) is set to `false`, the
character won't spawn and [StarterGui](/docs/reference/engine/classes/StarterGui.md) contents won't copy over until
[Player:LoadCharacterAsync()](/docs/reference/engine/classes/Player.md) is called.

If you need to control a player's UI container during playtime, for example to
show/hide a specific [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) or any of its children, access it as
follows from a [LocalScript](/docs/reference/engine/classes/LocalScript.md):

## Code Samples

**PlayerGui Overview**

Demonstrates [PlayerGui](/docs/reference/engine/classes/PlayerGui.md).

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local playerGui = player.PlayerGui
```

## Properties

### Property: PlayerGui.CurrentScreenOrientation

```json
{
  "type": "ScreenOrientation",
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

Describes the player's current screen orientation as an
[ScreenOrientation](/docs/reference/engine/enums/ScreenOrientation.md) value. Unlike the writable
[PlayerGui.ScreenOrientation](/docs/reference/engine/classes/PlayerGui.md) property, which requests a _preferred_
orientation mode, [PlayerGui.CurrentScreenOrientation](/docs/reference/engine/classes/PlayerGui.md) is read-only
and reports the orientation the device is actually displaying, updating as
the player physically rotates a mobile device.

### Property: PlayerGui.ScreenOrientation

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

Sets the preferred screen orientation mode for this player when on a
mobile device, expressed as an [ScreenOrientation](/docs/reference/engine/enums/ScreenOrientation.md) value. Changing it
requests that the device lock to, or follow, a particular orientation (for
example [Portrait](/docs/reference/engine/enums/ScreenOrientation.md) or
[LandscapeSensor](/docs/reference/engine/enums/ScreenOrientation.md)). The orientation the device is
actually displaying is reported separately by the read-only
[PlayerGui.CurrentScreenOrientation](/docs/reference/engine/classes/PlayerGui.md) property. This property
defaults to [LandscapeSensor](/docs/reference/engine/enums/ScreenOrientation.md).

### Property: PlayerGui.SelectionImageObject

```json
{
  "type": "GuiObject",
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
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

Overrides the default selection adornment used for gamepads. For best
results, this should point to a [GuiObject](/docs/reference/engine/classes/GuiObject.md).

## Methods

### Method: PlayerGui:GetTopbarTransparency

**Signature:** `PlayerGui:GetTopbarTransparency(): float`

Returns the current transparency of the topbar [CoreGui](/docs/reference/engine/classes/CoreGui.md), a value in
the range `[0, 1]` where `0` is completely opaque and `1` is completely
transparent. This is the value previously assigned with
[PlayerGui:SetTopbarTransparency()](/docs/reference/engine/classes/PlayerGui.md), and it defaults to `0.5`. This
method can only be called from a [LocalScript](/docs/reference/engine/classes/LocalScript.md); calling it from a
server script raises an error.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `float` — The current topbar transparency, a number between 0 (completely
opaque) and 1 (completely transparent).

**PlayerGui:GetTopbarTransparency**

The following line of code prints the transparency of the topbar.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local playerGui = player:WaitForChild("PlayerGui")

print(playerGui:GetTopbarTransparency())
```

### Method: PlayerGui:SetTopbarTransparency

**Signature:** `PlayerGui:SetTopbarTransparency(transparency: float): ()`

This method sets the transparency of the top bar [CoreGui](/docs/reference/engine/classes/CoreGui.md). A value
of `0` is completely opaque and a value of `1` is completely transparent.
Values outside of the range `[0, 1]` are clamped. The default transparency
of the topbar is `0.5`.

Using the [StarterGui:SetCore()](/docs/reference/engine/classes/StarterGui.md) method with the `"TopbarEnabled"`
option allows you to enable/disable the entire topbar and all of its
features (player list, health, etc). By contrast, this method only affects
how the top bar is displayed.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `transparency` | `float` |  | A number between 0 (completely opaque) and 1 (completely transparent). Values outside this range are clamped. |

**Returns:** `()`

**PlayerGui:SetTopbarTransparency**

The following line of code makes the Topbar appear fully opaque.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local playerGui = player:WaitForChild("PlayerGui")

playerGui:WaitForChild("PlayerGui"):SetTopbarTransparency(0)
```

**Custom Topbar Style**

This code sample demonstrates how you can create a custom-styled topbar. Paste
it into a [LocalScript](/docs/reference/engine/classes/LocalScript.md) placed within [StarterPlayerScripts](/docs/reference/engine/classes/StarterPlayerScripts.md).

```lua
local Players = game:GetService("Players")

local TOPBAR_COLOR = Color3.fromRGB(0, 0, 127)
local TOPBAR_TRANSPARENCY = 0

local playerGui = Players.LocalPlayer:WaitForChild("PlayerGui")

-- Hide the topbar
playerGui:SetTopbarTransparency(1)

-- Create a "Fake" replacement topbar with a ScreenGui and Frame
local screenGui = Instance.new("ScreenGui")
local frame = Instance.new("Frame")

-- Move (0, 0) to the actual top left corner of the screen, instead of under the topbar
screenGui.IgnoreGuiInset = true
-- The topbar is 36 pixels tall, and spans the entire width of the screen
frame.Size = UDim2.new(1, 0, 0, 36)

frame.BackgroundColor3 = TOPBAR_COLOR
frame.BackgroundTransparency = TOPBAR_TRANSPARENCY
frame.BorderSizePixel = 0

frame.Parent = screenGui
screenGui.Parent = playerGui
```

## Events

### Event: PlayerGui.TopbarTransparencyChangedSignal

**Signature:** `PlayerGui.TopbarTransparencyChangedSignal(transparency: float)`

Fires whenever the transparency of the topbar [CoreGui](/docs/reference/engine/classes/CoreGui.md) changes,
such as after a call to [PlayerGui:SetTopbarTransparency()](/docs/reference/engine/classes/PlayerGui.md). The
event passes the new transparency as its `transparency` argument, a value
in the range `[0, 1]`. It only fires when the clamped transparency differs
from the previous value, so setting the same value again does not re-fire
it.

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `transparency` | `float` | The new topbar transparency after the change, a number between 0 (completely opaque) and 1 (completely transparent). |

**PlayerGui.TopbarTransparencyChangedSignal1**

The below example prints out the value of the topbar transparency when it
changes.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local playerGui = player:WaitForChild("PlayerGui")

local function onTransparencyChanged(topbarTransparency)
	print("The topbar transparency is now:", topbarTransparency)
end

playerGui.TopbarTransparencyChangedSignal:Connect(onTransparencyChanged)
```

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