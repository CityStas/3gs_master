---
name: ChatWindowConfiguration
last_updated: 2026-10-30T19:55:52Z
inherits:
  - TextChatConfigurations
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
summary: "Configures properties of the default chat window."
---

# Class: ChatWindowConfiguration

> Configures properties of the default chat window.

## Description

Configures properties of the default text chat window. It is parented to
[TextChatService](/docs/reference/engine/classes/TextChatService.md).

#### Chat UI composition

The default chat UI is composed of two separate elements: the **chat window**
(message list) configured by this object, and the **chat input bar**
configured by [ChatInputBarConfiguration](/docs/reference/engine/classes/ChatInputBarConfiguration.md). Each element reports its own
`AbsoluteSize` and `AbsolutePosition` independently. To determine the total
screen bounds of the entire chat UI, combine values from both configurations
by computing the union of the two rectangles.

## Code Samples

**Get Total Chat UI Bounds**

Computes the total screen bounds of the entire chat UI by combining the
`AbsolutePosition` and `AbsoluteSize` of both `ChatWindowConfiguration` and
`ChatInputBarConfiguration`. Note that the reported bounds do not include the
small decorative bevel areas at the top and bottom edges of the chat window,
so the actual visual footprint on screen is slightly larger than the computed
region.

```lua
local Players = game:GetService("Players")
local TextChatService = game:GetService("TextChatService")

local player = Players.LocalPlayer
local playerGui = player:WaitForChild("PlayerGui")

local windowConfig = TextChatService.ChatWindowConfiguration
local inputBarConfig = TextChatService.ChatInputBarConfiguration

local function getTotalChatBounds()
	local windowPos = windowConfig.AbsolutePosition
	local windowSize = windowConfig.AbsoluteSize
	local inputPos = inputBarConfig.AbsolutePosition
	local inputSize = inputBarConfig.AbsoluteSize

	-- Compute the union of both rectangles to get total chat UI bounds.
	-- The reported values do not include the decorative bevel at the top
	-- and bottom edges of the chat window.
	local topLeft = Vector2.new(
		math.min(windowPos.X, inputPos.X),
		math.min(windowPos.Y, inputPos.Y)
	)
	local bottomRight = Vector2.new(
		math.max(windowPos.X + windowSize.X, inputPos.X + inputSize.X),
		math.max(windowPos.Y + windowSize.Y, inputPos.Y + inputSize.Y)
	)

	return topLeft, bottomRight - topLeft
end

-- Wait for chat UI to initialize and report absolute values
task.wait(2)

local position, size = getTotalChatBounds()
print("Total chat UI position:", position)
print("Total chat UI size:", size)

-- Overlay a semi-transparent frame to visually verify the bounds
local screenGui = Instance.new("ScreenGui")
screenGui.Name = "ChatBoundsDebug"
screenGui.DisplayOrder = 100
screenGui.Parent = playerGui

local frame = Instance.new("Frame")
frame.Position = UDim2.fromOffset(position.X, position.Y)
frame.Size = UDim2.fromOffset(size.X, size.Y)
frame.BackgroundColor3 = Color3.fromRGB(255, 0, 0)
frame.BackgroundTransparency = 0.5
frame.BorderSizePixel = 2
frame.BorderColor3 = Color3.fromRGB(255, 0, 0)
frame.Parent = screenGui
```

## Properties

### Property: ChatWindowConfiguration.AbsolutePosition

```json
{
  "type": "Vector2",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "Unsafe",
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

Read-only property that provides the screen position of the default chat
window (message list) in pixels. Behaves similarly to
[GuiBase2d.AbsolutePosition](/docs/reference/engine/classes/GuiBase2d.md).

This value represents only the message list portion of the chat UI, not
the entire chat interface. To get the total bounds including the input
bar, see [ChatInputBarConfiguration.AbsolutePosition](/docs/reference/engine/classes/ChatInputBarConfiguration.md) and combine
both regions. See the code example in the class description above.

### Property: ChatWindowConfiguration.AbsoluteSize

```json
{
  "type": "Vector2",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "Unsafe",
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

Read-only property that provides the screen size of the default chat
window (message list) in pixels. Behaves similarly to
[GuiBase2d.AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md).

This value represents only the message list portion of the chat UI, not
the entire chat interface. To get the total bounds including the input
bar, see [ChatInputBarConfiguration.AbsoluteSize](/docs/reference/engine/classes/ChatInputBarConfiguration.md) and combine both
regions. See the code example in the class description above.

### Property: ChatWindowConfiguration.BackgroundColor3

```json
{
  "type": "Color3",
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
    "Chat"
  ]
}
```

Background color of the default chat window. If the background color is
not overridden, this value will respect the user's
[GuiService.PreferredTransparency](/docs/reference/engine/classes/GuiService.md) by making the menu more gray as
the transparency of the menu decreases. Default value is
[Color3.new(25, 27, 29)](/docs/reference/engine/datatypes/Color3.md).

### Property: ChatWindowConfiguration.BackgroundTransparency

```json
{
  "type": "double",
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
    "Chat"
  ]
}
```

Background transparency of the default chat window as a number between `0`
and `1`. This value is multiplied with the user's
[GuiService.PreferredTransparency](/docs/reference/engine/classes/GuiService.md) to create the effective
background transparency used by the chat window, which may be more opaque
than this value set here. Default value is `0.3`.

### Property: ChatWindowConfiguration.Enabled

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
    "Chat"
  ]
}
```

Whether to show the default chat window. Set to `false` to hide.

### Property: ChatWindowConfiguration.FontFace

```json
{
  "type": "Datatype.Font",
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
    "Chat"
  ]
}
```

Font used to render text in the default chat window. Default is
[Font.BuilderSansMedium](/docs/reference/engine/enums/Font.md). Does not apply to
[TextChannelWindow](/docs/reference/engine/classes/TextChannelWindow.md).

### Property: ChatWindowConfiguration.HeightScale

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
  "category": "Behavior",
  "capabilities": [
    "Chat"
  ]
}
```

Factor by which the height of the default chat window should be scaled.
Must be a value between `0.5` and `2`. Defining a value outside of range
clamps the actual value to the closest bound.

### Property: ChatWindowConfiguration.HorizontalAlignment

```json
{
  "type": "HorizontalAlignment",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "Unsafe",
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

Horizontal alignment of the chat window. Behaves similarly to
[UIGridStyleLayout.HorizontalAlignment](/docs/reference/engine/classes/UIGridStyleLayout.md). Setting to
[Left](/docs/reference/engine/enums/HorizontalAlignment.md) or [Right](/docs/reference/engine/enums/HorizontalAlignment.md) adding
a small padding away from touching the corresponding horizontal edge of
the screen. Setting to [Center](/docs/reference/engine/enums/HorizontalAlignment.md) aligns the window
in the horizontal middle of the screen. Default value is
[Left](/docs/reference/engine/enums/HorizontalAlignment.md).

### Property: ChatWindowConfiguration.TextColor3

```json
{
  "type": "Color3",
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
    "Chat"
  ]
}
```

Color of the text in default chat window. Default value is
[Color3.new(255, 255, 255)](/docs/reference/engine/datatypes/Color3.md).

### Property: ChatWindowConfiguration.TextSize

```json
{
  "type": "int64",
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
    "Chat"
  ]
}
```

Size of the text in default chat window. Default value is `14`.

### Property: ChatWindowConfiguration.TextStrokeColor3

```json
{
  "type": "Color3",
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
    "Chat"
  ]
}
```

Color of the text stroke for text in default chat window. Default value is
[Color3.new(0, 0, 0)](/docs/reference/engine/datatypes/Color3.md).

### Property: ChatWindowConfiguration.TextStrokeTransparency

```json
{
  "type": "double",
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
    "Chat"
  ]
}
```

Transparency of the text stroke for text in default chat window. Default
value is `0.5`.

### Property: ChatWindowConfiguration.VerticalAlignment

```json
{
  "type": "VerticalAlignment",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "Unsafe",
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

Vertical alignment of the chat window. Behaves similarly to
[UIGridStyleLayout.VerticalAlignment](/docs/reference/engine/classes/UIGridStyleLayout.md). Setting to
[Top](/docs/reference/engine/enums/VerticalAlignment.md) or [Bottom](/docs/reference/engine/enums/VerticalAlignment.md) adds a
small padding away from touching the corresponding edge of the screen.
Setting to [Center](/docs/reference/engine/enums/VerticalAlignment.md) aligns the window in the
vertical middle of the screen. Default value is
[Top](/docs/reference/engine/enums/VerticalAlignment.md).

### Property: ChatWindowConfiguration.WidthScale

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
  "category": "Behavior",
  "capabilities": [
    "Chat"
  ]
}
```

Factor by which the width of the default chat window should be scaled.
Must be a value between `0.5` and `2`. Defining a value outside of range
clamps the actual value to the closest bound.

## Methods

### Method: ChatWindowConfiguration:DeriveNewMessageProperties

**Signature:** `ChatWindowConfiguration:DeriveNewMessageProperties(): ChatWindowMessageProperties`

Creates a new [ChatWindowMessageProperties](/docs/reference/engine/classes/ChatWindowMessageProperties.md) instance that can be
used to customize the appearance of messages in the chat window.
[ChatWindowMessageProperties](/docs/reference/engine/classes/ChatWindowMessageProperties.md) inherits from
[TextChatMessageProperties](/docs/reference/engine/classes/TextChatMessageProperties.md).

This is intended to be used during custom
[TextChatService.OnChatWindowAdded](/docs/reference/engine/classes/TextChatService.md) callbacks.

*Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Returns:** `ChatWindowMessageProperties` — A new [ChatWindowMessageProperties](/docs/reference/engine/classes/ChatWindowMessageProperties.md) instance whose values you
can modify and return from a [TextChatService.OnChatWindowAdded](/docs/reference/engine/classes/TextChatService.md)
callback to customize how individual messages appear in the chat
window.

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

**Derive New Message Properties**

Demonstrates [ChatWindowConfiguration:DeriveNewMessageProperties()](/docs/reference/engine/classes/ChatWindowConfiguration.md).

```lua
local TextChatService = game:GetService("TextChatService")
local ChatWindowConfiguration = TextChatService.ChatWindowConfiguration

TextChatService.OnChatWindowAdded = function(textChatMessage)
  local properties = ChatWindowConfiguration:DeriveNewMessageProperties()

  if textChatMessage.Metadata == "Important" then
    properties.TextColor3 = Color3.fromRGB(255, 0, 0)
  end

  return properties
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