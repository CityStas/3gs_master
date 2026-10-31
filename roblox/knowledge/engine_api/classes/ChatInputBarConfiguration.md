---
name: ChatInputBarConfiguration
last_updated: 2026-10-30T19:55:52Z
inherits:
  - TextChatConfigurations
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
summary: "Configures properties of the default chat input bar."
---

# Class: ChatInputBarConfiguration

> Configures properties of the default chat input bar.

## Description

Configures properties of the default text chat input bar. It is parented to
[TextChatService](/docs/reference/engine/classes/TextChatService.md).

#### Chat UI composition

The default chat UI is composed of two separate elements: the **chat window**
(message list) configured by [ChatWindowConfiguration](/docs/reference/engine/classes/ChatWindowConfiguration.md), and the **chat
input bar** configured by this object. Each element reports its own
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

### Property: ChatInputBarConfiguration.AbsolutePosition

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
input bar in pixels. Behaves similarly to
[GuiBase2d.AbsolutePosition](/docs/reference/engine/classes/GuiBase2d.md).

This value represents only the input bar portion of the chat UI, not the
entire chat interface. To get the total bounds including the message list,
see [ChatWindowConfiguration.AbsolutePosition](/docs/reference/engine/classes/ChatWindowConfiguration.md) and combine both
regions.

### Property: ChatInputBarConfiguration.AbsoluteSize

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

Read-only property that provides the screen size of the default chat input
bar in pixels. Behaves similarly to [GuiBase2d.AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md).

This value represents only the input bar portion of the chat UI, not the
entire chat interface. To get the total bounds including the message list,
see [ChatWindowConfiguration.AbsoluteSize](/docs/reference/engine/classes/ChatWindowConfiguration.md) and combine both regions.

### Property: ChatInputBarConfiguration.AutocompleteEnabled

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

Whether to enable autocomplete for the chat input bar. Set to `false` to
disable autocomplete.

### Property: ChatInputBarConfiguration.BackgroundColor3

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

Background color of the default chat input bar. Default value is
[Color3.new(25, 27, 29)](/docs/reference/engine/datatypes/Color3.md).

### Property: ChatInputBarConfiguration.BackgroundTransparency

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

Background transparency of the default chat input bar as a number between
`0` and `1`. This value is multiplied with the user's
[GuiService.PreferredTransparency](/docs/reference/engine/classes/GuiService.md) to create the effective
background transparency used by the chat input bar, which may be more
opaque than this value set here. Default value is `0.2`.

### Property: ChatInputBarConfiguration.Enabled

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

Whether to show the default chat input bar. Set to `false` to hide.

### Property: ChatInputBarConfiguration.FontFace

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

Font used to render text in the default chat input bar. Default is
[Font.BuilderSansMedium](/docs/reference/engine/enums/Font.md). Does not apply to [TextChannelWindow](/docs/reference/engine/classes/TextChannelWindow.md)
instances.

### Property: ChatInputBarConfiguration.IsFocused

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
  "thread_safety": "Unsafe",
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

Indicates whether the default chat input bar is focused or not. Useful for
firing property changed events so you can implement callback functions
that respond to changes in the input bar's focus state.

**Typing Indicator Bubble**

The code below includes a simple way to create a typing indicator bubble above
a user's avatar when the user is typing. Paste into a LocalScript.

```lua
local Players = game:GetService("Players")
local TextChatService = game:GetService("TextChatService")
local ChatInputBarConfiguration = TextChatService:FindFirstChildOfClass("ChatInputBarConfiguration")
local BubbleChatConfiguration = TextChatService:FindFirstChildOfClass("BubbleChatConfiguration")

local LocalPlayer = Players.LocalPlayer
local Character = LocalPlayer.Character or LocalPlayer.CharacterAdded:Wait()

-- Set up TextLabel
local textLabel = Instance.new("TextLabel")
textLabel.Size = UDim2.fromScale(1, 1)
textLabel.Text = ". . ."
textLabel.BackgroundColor3 = BubbleChatConfiguration.BackgroundColor3
textLabel.BorderColor3 = BubbleChatConfiguration.BackgroundColor3
textLabel.BackgroundTransparency = BubbleChatConfiguration.BackgroundTransparency
textLabel.TextColor3 = BubbleChatConfiguration.TextColor3
textLabel.FontFace = BubbleChatConfiguration.FontFace
textLabel.TextSize = BubbleChatConfiguration.TextSize
-- Parent a UICorner to the TextLabel to have rounded corners
local uiCorner = Instance.new("UICorner")
uiCorner.CornerRadius = UDim.new(0, 12)
uiCorner.Parent = textLabel

-- Set up Billboard
local typingIndicatorBillboard = Instance.new("BillboardGui")
typingIndicatorBillboard.Enabled = false
typingIndicatorBillboard.Size = UDim2.fromScale(1, 1)
typingIndicatorBillboard.StudsOffsetWorldSpace = Vector3.new(-0, 4, 0)
typingIndicatorBillboard.Adornee = Character
textLabel.Parent = typingIndicatorBillboard
typingIndicatorBillboard.Parent = LocalPlayer:FindFirstChildOfClass("PlayerGui")

ChatInputBarConfiguration:GetPropertyChangedSignal("IsFocused"):Connect(function()
	-- Enable the typing indicator when the input bar is focused and disable otherwise
	typingIndicatorBillboard.Enabled = ChatInputBarConfiguration.IsFocused
end)
```

### Property: ChatInputBarConfiguration.KeyboardKeyCode

```json
{
  "type": "KeyCode",
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

Additional key users can press to trigger focusing on the default chat
input bar. Useful when you want to have an extra hotkey for focusing in
addition to the <kbd>/</kbd> key.

### Property: ChatInputBarConfiguration.PlaceholderColor3

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

Color of the text of the placeholder text in the default chat input bar.
Default value is [Color3.new(178, 178, 178)](/docs/reference/engine/datatypes/Color3.md).

### Property: ChatInputBarConfiguration.TargetTextChannel

```json
{
  "type": "TextChannel",
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

Determines which [TextChannel](/docs/reference/engine/classes/TextChannel.md) to use when the user sends a message
with the default chat input bar.

### Property: ChatInputBarConfiguration.TextBox

```json
{
  "type": "TextBox",
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

Reference to a designated [TextBox](/docs/reference/engine/classes/TextBox.md) instance that sends messages on
behalf of the user. You can use it to further integrate your custom chat
input bar UI into your experience by freely manipulating appearance,
location, and layout. When opting to set this property to a custom
[TextBox](/docs/reference/engine/classes/TextBox.md), you don't need to write any code for the following
behavior:

- When a user types a message and presses [KeyCode.Return](/docs/reference/engine/enums/KeyCode.md), the
  message will be sent to
  [ChatInputBarConfiguration.TargetTextChannel](/docs/reference/engine/classes/ChatInputBarConfiguration.md).
- When a message is sent, [TextBox.Text](/docs/reference/engine/classes/TextBox.md) will automatically clear.

For security, some limitations are imposed on the [TextBox](/docs/reference/engine/classes/TextBox.md) when it
is promoted to [ChatInputBarConfiguration.TextBox](/docs/reference/engine/classes/ChatInputBarConfiguration.md). Luau code will
not be able to:

- Change the [TextBox.Text](/docs/reference/engine/classes/TextBox.md) property.
- Use the [TextBox:CaptureFocus()](/docs/reference/engine/classes/TextBox.md) or [TextBox:ReleaseFocus()](/docs/reference/engine/classes/TextBox.md)
  methods.

### Property: ChatInputBarConfiguration.TextColor3

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

Color of the text in default chat input bar. Default value is
[Color3.new(255, 255, 255)](/docs/reference/engine/datatypes/Color3.md).

### Property: ChatInputBarConfiguration.TextSize

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

Size of the text in default chat input bar. Default value is `14`.

### Property: ChatInputBarConfiguration.TextStrokeColor3

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

Color of the text stroke for text in default chat input bar. Default value
is [Color3.new(0, 0, 0)](/docs/reference/engine/datatypes/Color3.md).

### Property: ChatInputBarConfiguration.TextStrokeTransparency

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

Transparency of the text stroke for text in default chat input bar.
Default value is `0.5`.

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