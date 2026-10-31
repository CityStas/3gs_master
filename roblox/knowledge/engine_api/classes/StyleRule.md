---
name: StyleRule
last_updated: 2026-10-30T19:55:53Z
inherits:
  - StyleBase
  - Instance
  - Object
type: class
memory_category: Gui
summary: "Defines style properties which override properties on the instances affected by the Selector property."
---

# Class: StyleRule

> Defines style properties which override properties on the instances affected
> by the [Selector](/docs/reference/engine/classes/StyleRule.md) property.

## Properties

### Property: StyleRule.Priority

```json
{
  "type": "int",
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

A number that determines how properties of the `StyleRule` apply relative
to the same properties in other [StyleRules](/docs/reference/engine/classes/StyleRule.md). Higher
priority values take precedence over lower. For example, if a `StyleRule`
with a priority of `10` has an `AnchorPoint` property of <Typography
noWrap>`1, 0`</Typography>, it will take precedence over lower-priority
[StyleRules](/docs/reference/engine/classes/StyleRule.md) with `AnchorPoint` properties.

### Property: StyleRule.Selector

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

A string specifying which instances the `StyleRule` should affect. This
can be a mix of selectors and combinators to match characteristics such as
the class name, instance name, and hierarchy relationships.

For example, `".Container > ImageLabel.BlueOnHover:Hover"` effectively
means the style rule overrides every [ImageLabel](/docs/reference/engine/classes/ImageLabel.md) that's a child of
an instance tagged with `Container` (`.Container > ImageLabel`) **and** is
tagged with `BlueOnHover` (`.BlueOnHover`) **and** is in the
[GuiState.Hover](/docs/reference/engine/enums/GuiState.md) state (`:Hover`).

#### Selectors

| Selector | Description | Examples |
| --- | --- | --- |
| `[class]` | Matches instances of a [GuiObject](/docs/reference/engine/classes/GuiObject.md) or [UIComponent](/docs/reference/engine/classes/UIComponent.md) class. | `"Frame"`
`"ImageButton"`
`"UICorner"` |
| `.[tag]` | Matches instances [tagged](/docs/en-us/studio/properties.md#instance-tags) with a [CollectionService](/docs/reference/engine/classes/CollectionService.md) tag. | `".Container"`
`".BlueOnHover"` |
| `#[name]` | Matches instances of a specific [Instance.Name](/docs/reference/engine/classes/Instance.md). | `"#ModalFrame"`
`"#CloseButton"` |
| `:[state]` | Matches instances currently in a [GuiState](/docs/reference/engine/enums/GuiState.md). | `":Hover"` |
| `@[StyleQuery name]` | Matches instances with child [StyleQuery](/docs/reference/engine/classes/StyleQuery.md) that has [IsActive](/docs/reference/engine/classes/StyleQuery.md) set to `true`.

 There are also built-in selectors for `"@ReducedMotionEnabledFalse"`, `"@ReducedMotionEnabledTrue"`, `"@PreferredInputGamepad"`, `"@PreferredInputKeyboardAndMouse"`, `"@PreferredInputTouch"`, `"@PreferredTextSizeMedium"`, `"@PreferredTextSizeLarge"`, `"@PreferredTextSizeLarger"`, `"@PreferredTextSizeLargest"`, `"@ViewportDisplaySizeSmall"`, `"@ViewportDisplaySizeMedium"`, and `"@ViewportDisplaySizeLarge"` that can match an instance without a [StyleQuery](/docs/reference/engine/classes/StyleQuery.md) instance. | `"@StyleQuerySmall"` |

#### Combinators

| Combinator | Description | Examples |
| --- | --- | --- |
| `>` | Matches instances that are **direct children** of the previous filter matches. | `"Frame > .Inventory"` |
| `>>` | Matches instances that are **descendants** of the previous filter matches. | `"ImageButton >> .BlueOnHover"` |
| `,` | Specifies a list of multiple independent selectors for the style rule. | `"Frame.TagA, TextLabel.TagA"` |
| `::` | Creates a phantom [UIComponent](/docs/reference/engine/classes/UIComponent.md) instance under the previous filter matches and applies the style rule's properties to it.

 Multiple instances can be created for [StyleQuery](/docs/reference/engine/classes/StyleQuery.md) and [UIStroke](/docs/reference/engine/classes/UIStroke.md) by aliasing the instance with a name selector. Some nested instances are supported, including [UIGradient](/docs/reference/engine/classes/UIGradient.md) under [UIStroke](/docs/reference/engine/classes/UIStroke.md) or [UIConstraint](/docs/reference/engine/classes/UIConstraint.md) under a [UIGridLayout](/docs/reference/engine/classes/UIGridLayout.md). | `"Frame::UICorner" "::UIStroke #Outer"` |

**UI Class Selector**

The following example shows how to define a **class** selector which targets
all [TextButton](/docs/reference/engine/classes/TextButton.md) instances and styles them with blue background and
light grey text. To test, paste the code into a [LocalScript](/docs/reference/engine/classes/LocalScript.md) which is a
child of a [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) located inside the [StarterGui](/docs/reference/engine/classes/StarterGui.md) container.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local screenGui = script.Parent

local coreSheet = Instance.new("StyleSheet")
coreSheet.Parent = ReplicatedStorage
local styleLink = Instance.new("StyleLink")
styleLink.StyleSheet = coreSheet
styleLink.Parent = screenGui
local rule = Instance.new("StyleRule")
rule.Parent = coreSheet

-- Class selector
rule.Selector = "TextButton"

-- Set rule properties
rule:SetProperties({
	["BackgroundColor3"] = Color3.fromHex("335FFF"),
	["TextColor3"] = Color3.fromHex("E1E1E1"),
	["Size"] = UDim2.new(0.15, 0, 0, 40),
	["BorderSizePixel"] = 0,
})

local button = Instance.new("TextButton")
button.Text = "Main Menu"
button.Parent = screenGui
```

**UI Tag Selector**

The following example shows how to define a **tag** selector which utilizes
[tags](/docs/en-us/studio/properties.md#instance-tags) applied through
[CollectionService](/docs/reference/engine/classes/CollectionService.md) to target a [TextButton](/docs/reference/engine/classes/TextButton.md) tagged with
`ButtonPrimary`. To test, paste the code into a [LocalScript](/docs/reference/engine/classes/LocalScript.md) which is a
child of a [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) located inside the [StarterGui](/docs/reference/engine/classes/StarterGui.md) container.

```lua
local CollectionService = game:GetService("CollectionService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local screenGui = script.Parent

local coreSheet = Instance.new("StyleSheet")
coreSheet.Parent = ReplicatedStorage
local styleLink = Instance.new("StyleLink")
styleLink.StyleSheet = coreSheet
styleLink.Parent = screenGui
local rule = Instance.new("StyleRule")
rule.Parent = coreSheet

-- Tag selector
rule.Selector = ".ButtonPrimary"

-- Set rule properties
rule:SetProperties({
	["BackgroundColor3"] = Color3.fromHex("FF0099"),
	["TextColor3"] = Color3.fromHex("E1E1E1"),
	["Size"] = UDim2.new(0.15, 0, 0, 40),
	["BorderSizePixel"] = 0,
})

local button = Instance.new("TextButton")
button.Text = "Main Menu"
button.Parent = screenGui
-- Apply tag to button
CollectionService:AddTag(button, "ButtonPrimary")
```

**UI Modifier Selector**

The following example shows how to define a UI **modifier** selector which
applies a phantom [UICorner](/docs/reference/engine/classes/UICorner.md) instance to a [Frame](/docs/reference/engine/classes/Frame.md) tagged with
`RoundedCorner20`. To test, paste the code into a [LocalScript](/docs/reference/engine/classes/LocalScript.md) which is
a child of a [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) located inside the [StarterGui](/docs/reference/engine/classes/StarterGui.md)
container.

```lua
local CollectionService = game:GetService("CollectionService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local screenGui = script.Parent

local coreSheet = Instance.new("StyleSheet")
coreSheet.Parent = ReplicatedStorage
local styleLink = Instance.new("StyleLink")
styleLink.StyleSheet = coreSheet
styleLink.Parent = screenGui
local rule = Instance.new("StyleRule")
rule.Parent = coreSheet

-- UI component selector
rule.Selector = "Frame.RoundedCorner20::UICorner"

-- Set rule property
rule:SetProperty("CornerRadius", UDim.new(0, 20))

-- Create frame
local frame = Instance.new("Frame")
frame.Size = UDim2.new(0.4, 0, 0.2, 0)
frame.Parent = screenGui
-- Apply tag to frame
CollectionService:AddTag(frame, "RoundedCorner20")
```

**UI Style Query Selector**

The following example shows how to define a **query** selector which utilizes
[StyleQuery](/docs/reference/engine/classes/StyleQuery.md) to target a [TextButton](/docs/reference/engine/classes/TextButton.md) at different widths. To
test, paste the code into a [LocalScript](/docs/reference/engine/classes/LocalScript.md) which is a child of a
[ScreenGui](/docs/reference/engine/classes/ScreenGui.md) located inside the [StarterGui](/docs/reference/engine/classes/StarterGui.md) container, and resize
the viewport width.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local screenGui = script.Parent

local coreSheet = Instance.new("StyleSheet")
coreSheet.Parent = ReplicatedStorage
local styleLink = Instance.new("StyleLink")
styleLink.StyleSheet = coreSheet
styleLink.Parent = screenGui

local smallRule = Instance.new("StyleRule")
smallRule.Parent = coreSheet
local mediumRule = Instance.new("StyleRule")
mediumRule.Parent = coreSheet

-- Declare style query selectors
smallRule.Selector = "@Small"
mediumRule.Selector = "@Medium"

-- Set rule properties
smallRule:SetProperties({
	["BackgroundColor3"] = Color3.fromHex("FF0099"),
	["Text"] = "Small Container",
	["TextColor3"] = Color3.fromHex("E1E1E1"),
	["TextSize"] = 12,
})
mediumRule:SetProperties({
	["BackgroundColor3"] = Color3.fromHex("F0F0F0"),
	["Text"] = "Medium Container",
	["TextColor3"] = Color3.fromHex("0022FC"),
	["TextSize"] = 24,
})

local button = Instance.new("TextButton")
button.Text = "Main Menu"
button.Parent = screenGui
button.Size = UDim2.fromScale(0.5, 0.2)

-- Create style queries with names matching style rule selectors
local mediumSQ = Instance.new("StyleQuery")
mediumSQ.Parent = button
mediumSQ.Name = "Medium"
mediumSQ:SetConditions({
	["MinSize"] = Vector2.new(200, 0),
})
local smallSQ = Instance.new("StyleQuery")
smallSQ.Parent = button
smallSQ.Name = "Small"
smallSQ:SetConditions({
	["MaxSize"] = Vector2.new(200, math.huge),
	["MinSize"] = Vector2.new(0, 0),
})
```

### Property: StyleRule.SelectorError

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
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

A read-only string that displays errors from the
[Selector](/docs/reference/engine/classes/StyleRule.md) property such as syntax errors,
unsupported class types, etc.

## Methods

### Method: StyleRule:GetDefaultPropertyTransition

**Signature:** `StyleRule:GetDefaultPropertyTransition(): Variant`

Returns the default transition applied to all properties of the
`StyleRule` that don't have an explicit transition set. This is equivalent
to calling
[GetPropertyTransitions()](/docs/reference/engine/classes/StyleRule.md) and
reading the value at key `"*"`.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `Variant` — The default transition as a [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) or string token, or
`nil` if no default transition is set.

### Method: StyleRule:GetProperties

**Signature:** `StyleRule:GetProperties(): Dictionary`

Returns a dictionary of key-value pairs describing the properties of the
`StyleRule`, for example:

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `Dictionary` — Dictionary of key-value pairs describing the properties of the
`StyleRule`.

**Get Properties**

Demonstrates [StyleRule:GetProperties()](/docs/reference/engine/classes/StyleRule.md).

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local coreSheet = Instance.new("StyleSheet")
coreSheet.Name = "CoreSheet"
coreSheet.Parent = ReplicatedStorage

local frameRule = Instance.new("StyleRule")
frameRule.Name = "Frame"
frameRule:SetProperty("AnchorPoint", Vector2.new(0.5, 0))
frameRule:SetProperty("BackgroundColor3", Color3.new(1, 0, 0.25))
frameRule.Parent = coreSheet

-- Get reference to style rule
local frameRule = coreSheet.Frame

local props = frameRule:GetProperties()
print(props)
--[[
{
	["AnchorPoint"] = 0.5, 0,
	["BackgroundColor3"] = 1, 0, 0.25
}
]]
```

### Method: StyleRule:GetProperty

**Signature:** `StyleRule:GetProperty(name: string): Variant`

Returns the value of a specific property in the `StyleRule`.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | String name of the property, for example `"AnchorPoint"` or `"BackgroundColor3"`. |

**Returns:** `Variant` — Value of the property.

**Get Property**

Demonstrates [StyleRule:GetProperty()](/docs/reference/engine/classes/StyleRule.md).

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local coreSheet = Instance.new("StyleSheet")
coreSheet.Name = "CoreSheet"
coreSheet.Parent = ReplicatedStorage

local frameRule = Instance.new("StyleRule")
frameRule.Name = "Frame"
frameRule:SetProperty("AnchorPoint", Vector2.new(0.5, 0))
frameRule.Parent = coreSheet

local prop = frameRule:GetProperty("AnchorPoint")
print(prop) --> 0.5, 0
```

### Method: StyleRule:GetPropertyTransitions

**Signature:** `StyleRule:GetPropertyTransitions(): Dictionary`

Returns a dictionary of all property transitions set on the `StyleRule`.
Each key is a property name (string) and each value is a
[TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) or a string token that defines the transition's
timing for that property.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `Dictionary` — Dictionary of key-value pairs mapping property names to their
transition parameters.

**GetPropertyTransitions()**

This example shows how to retrieve a table of property transitions.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local coreSheet = ReplicatedStorage:FindFirstChild("CoreSheet")

-- Get reference to style rule
local frameRule = coreSheet.Frame

-- Set some transitions
frameRule:SetPropertyTransition("BackgroundColor3", TweenInfo.new(1, Enum.EasingStyle.Linear))
frameRule:SetPropertyTransition("BackgroundTransparency", "$DefaultTransition")

local transitions = frameRule:GetPropertyTransitions()
print(transitions)
```

### Method: StyleRule:SetDefaultPropertyTransition

**Signature:** `StyleRule:SetDefaultPropertyTransition(transitionParams: Variant): ()`

Sets or clears a default transition that applies to all properties of the
`StyleRule` that don't have an explicit transition set. This is equivalent
to calling
[SetPropertyTransition()](/docs/reference/engine/classes/StyleRule.md) with
`"*"` as the property name.

The `transitionParams` parameter accepts a [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) that
configures the transition's timing. The following [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md)
properties are used:

- [Time](/docs/reference/engine/datatypes/TweenInfo.md) &mdash; Duration of the transition in
  seconds.
- [EasingStyle](/docs/reference/engine/datatypes/TweenInfo.md) &mdash; The easing function
  used for interpolation.
- [EasingDirection](/docs/reference/engine/datatypes/TweenInfo.md) &mdash; The
  direction of the easing function.
- [DelayTime](/docs/reference/engine/datatypes/TweenInfo.md) &mdash; Delay in seconds before
  the transition starts.

Note that the [RepeatCount](/docs/reference/engine/datatypes/TweenInfo.md) and
[Reverses](/docs/reference/engine/datatypes/TweenInfo.md) fields of [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) are
ignored, as style transitions cannot repeat or reverse automatically.

A per-property transition set via
[SetPropertyTransition()](/docs/reference/engine/classes/StyleRule.md) takes
precedence over the default transition for that property.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `transitionParams` | `Variant` |  | Either a [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md), a token string defining the default transition timing, or `nil` to remove the default transition. |

**Returns:** `()`

### Method: StyleRule:SetProperties

**Signature:** `StyleRule:SetProperties(styleProperties: Dictionary): ()`

Similar to [SetProperty()](/docs/reference/engine/classes/StyleRule.md) but lets you
declare and set multiple properties of the `StyleRule` at once. Each
assignment should be a valid property of the affected [GuiObject](/docs/reference/engine/classes/GuiObject.md) or
[UIComponent](/docs/reference/engine/classes/UIComponent.md) ([UICorner](/docs/reference/engine/classes/UICorner.md), [UIGradient](/docs/reference/engine/classes/UIGradient.md), etc.), and each
assigned value should match its property's value type, for example
[Vector2](/docs/reference/engine/datatypes/Vector2.md) for [AnchorPoint](/docs/reference/engine/classes/GuiObject.md) or
[Color3](/docs/reference/engine/datatypes/Color3.md) for [BackgroundColor3](/docs/reference/engine/classes/GuiObject.md).

Attempts to assign invalid property names such as `"AnchorPt"` or
`"BkColor"` will silently fail. Type mismatches such as [CFrame](/docs/reference/engine/datatypes/CFrame.md)
for [AnchorPoint](/docs/reference/engine/classes/GuiObject.md) or [UDim2](/docs/reference/engine/datatypes/UDim2.md) for
[BackgroundColor3](/docs/reference/engine/classes/GuiObject.md) will also fail and an
error will appear in the [Output](/docs/en-us/studio/output.md) window.

To set/update just one property of a `StyleRule`, see
[SetProperty()](/docs/reference/engine/classes/StyleRule.md).

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local coreSheet = ReplicatedStorage:FindFirstChild("CoreSheet")

-- Get reference to style rule
local frameRule = coreSheet.Frame

-- Set rule properties
frameRule:SetProperties({
	["AnchorPoint"] = Vector2.new(0.5, 0),
	["BackgroundColor3"] = Color3.new(1, 0, 0.25)
})
```

Note that you can assign **tokens** as property values through the `$`
prefix:

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local coreSheet = ReplicatedStorage:FindFirstChild("CoreSheet")
local tokensSheet = ReplicatedStorage:FindFirstChild("Tokens")

-- Set tokens (attributes) on tokens sheet
tokensSheet:SetAttribute("TopCenterAnchor", Vector2.new(0.5, 0))
tokensSheet:SetAttribute("MainBackgroundColor", Color3.new(0.2, 0.2, 0.3))

-- Get reference to style rule
local frameRule = coreSheet.Frame

-- Set rule properties
frameRule:SetProperties({
	["AnchorPoint"] = "$TopCenterAnchor",
	["BackgroundColor3"] = "$MainBackgroundColor"
})
```

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `styleProperties` | `Dictionary` |  | Dictionary of key-value pairs defining the properties to set. |

**Returns:** `()`

### Method: StyleRule:SetProperty

**Signature:** `StyleRule:SetProperty(name: string, value: Variant): ()`

Sets a new property (or modifies an existing property) for the
`StyleRule`. The `name` parameter should be a valid property of the
affected [GuiObject](/docs/reference/engine/classes/GuiObject.md) or [UIComponent](/docs/reference/engine/classes/UIComponent.md) ([UICorner](/docs/reference/engine/classes/UICorner.md),
[UIGradient](/docs/reference/engine/classes/UIGradient.md), etc.), and the assigned value should match the
property's value type, for example [Vector2](/docs/reference/engine/datatypes/Vector2.md) for
[AnchorPoint](/docs/reference/engine/classes/GuiObject.md) or [Color3](/docs/reference/engine/datatypes/Color3.md) for
[BackgroundColor3](/docs/reference/engine/classes/GuiObject.md).

Attempts to assign invalid property names such as `"AnchorPt"` or
`"BkColor"` will silently fail. Type mismatches such as [CFrame](/docs/reference/engine/datatypes/CFrame.md)
for [AnchorPoint](/docs/reference/engine/classes/GuiObject.md) or [UDim2](/docs/reference/engine/datatypes/UDim2.md) for
[BackgroundColor3](/docs/reference/engine/classes/GuiObject.md) will also fail and an
error will appear in the [Output](/docs/en-us/studio/output.md) window.

To set multiple properties for a `StyleRule` at once, see
[SetProperties()](/docs/reference/engine/classes/StyleRule.md).

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local coreSheet = ReplicatedStorage:FindFirstChild("CoreSheet")

-- Get reference to style rule
local frameRule = coreSheet.Frame

-- Set rule property
frameRule:SetProperty("BackgroundColor3", Color3.new(1, 0, 0.25))
```

Note that you can assign **tokens** as property values through the `$`
prefix:

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local coreSheet = ReplicatedStorage:FindFirstChild("CoreSheet")
local tokensSheet = ReplicatedStorage:FindFirstChild("Tokens")

-- Set new token (attribute) on tokens sheet
tokensSheet:SetAttribute("MainBackgroundColor", Color3.new(0.2, 0.2, 0.3))

-- Get reference to style rule
local frameRule = coreSheet.Frame
-- Set rule property to use the token as its value
frameRule:SetProperty("BackgroundColor3, "$MainBackgroundColor")
```

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | Property name to set, for example `"BackgroundColor3"`. |
| `value` | `Variant` |  | Property value to set, for example [Color3.new(1, 0, 0.25)](/docs/reference/engine/datatypes/Color3.md). |

**Returns:** `()`

### Method: StyleRule:SetPropertyTransition

**Signature:** `StyleRule:SetPropertyTransition(property: string, transitionParams: Variant): ()`

Sets or clears the transition for a single property on the `StyleRule`.
When a transition is set for a property, any change to that property's
styled value will be animated over time instead of applied immediately.

The `transitionParams` parameter accepts a [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) that
configures the transition's timing. The following [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md)
properties are used:

- [Time](/docs/reference/engine/datatypes/TweenInfo.md) &mdash; Duration of the transition in
  seconds.
- [EasingStyle](/docs/reference/engine/datatypes/TweenInfo.md) &mdash; The easing function
  used for interpolation.
- [EasingDirection](/docs/reference/engine/datatypes/TweenInfo.md) &mdash; The
  direction of the easing function.
- [DelayTime](/docs/reference/engine/datatypes/TweenInfo.md) &mdash; Delay in seconds before
  the transition starts.

Note that the [RepeatCount](/docs/reference/engine/datatypes/TweenInfo.md) and
[Reverses](/docs/reference/engine/datatypes/TweenInfo.md) fields of [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) are
ignored, as style transitions cannot repeat or reverse automatically.

To set transitions for multiple properties at once, see
[SetPropertyTransitions()](/docs/reference/engine/classes/StyleRule.md).

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `property` | `string` |  | String name of the property to set a transition for, for example `"BackgroundColor3"` or `"Size"`. |
| `transitionParams` | `Variant` |  | A [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) or token string defining the transition timing, or `nil` to remove the transition for this property. |

**Returns:** `()`

**SetPropertyTransition()**

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local coreSheet = ReplicatedStorage:FindFirstChild("CoreSheet")

-- Get reference to style rule
local frameRule = coreSheet.Frame

-- Set a 1-second linear transition on BackgroundColor3
frameRule:SetPropertyTransition("BackgroundColor3", TweenInfo.new(
	1, -- Time
	Enum.EasingStyle.Linear -- EasingStyle
))

-- Remove the transition
frameRule:SetPropertyTransition("BackgroundColor3", nil)
```

**SetPropertyTransition() Using Tokens**

This example shows how you can assign **tokens** as transition values using a
string with the `$` prefix.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local coreSheet = ReplicatedStorage:FindFirstChild("CoreSheet")
local tokensSheet = ReplicatedStorage:FindFirstChild("Tokens")

-- Set tokens (attributes) on tokens sheet
tokensSheet:SetAttribute("LinearTransition", TweenInfo.new(1, Enum.EasingStyle.Linear))

-- Get reference to style rule
local frameRule = coreSheet.Frame

frameRule:SetPropertyTransition("BackgroundColor3", "$LinearTransition")
```

### Method: StyleRule:SetPropertyTransitions

**Signature:** `StyleRule:SetPropertyTransitions(properties: Dictionary): ()`

Similar to
[SetPropertyTransition()](/docs/reference/engine/classes/StyleRule.md) but lets
you declare and set transitions for multiple properties of the `StyleRule`
at once.

Calling this method **replaces** all existing transitions on the
`StyleRule` with the provided set. Each key should be a property name
(string) and each value should be a [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) or string token
defining the transition timing for that property. Passing `nil` as a value
for a key excludes that property from the resulting transitions.

The following [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) properties are used:

- [Time](/docs/reference/engine/datatypes/TweenInfo.md) &mdash; Duration of the transition in
  seconds.
- [EasingStyle](/docs/reference/engine/datatypes/TweenInfo.md) &mdash; The easing function
  used for interpolation.
- [EasingDirection](/docs/reference/engine/datatypes/TweenInfo.md) &mdash; The
  direction of the easing function.
- [DelayTime](/docs/reference/engine/datatypes/TweenInfo.md) &mdash; Delay in seconds before
  the transition starts.

Note that the [RepeatCount](/docs/reference/engine/datatypes/TweenInfo.md) and
[Reverses](/docs/reference/engine/datatypes/TweenInfo.md) fields of [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) are
ignored, as style transitions cannot repeat or reverse automatically.

To set/update just one property transition on a `StyleRule`, see
[SetPropertyTransition()](/docs/reference/engine/classes/StyleRule.md).

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `properties` | `Dictionary` |  | Dictionary of property names to transition parameters. |

**Returns:** `()`

**SetPropertyTransitions()**

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local coreSheet = ReplicatedStorage:FindFirstChild("CoreSheet")

-- Get reference to style rule
local frameRule = coreSheet.Frame

-- Sets transitions for two properties at once
frameRule:SetPropertyTransitions({
  ["BackgroundColor3"] = TweenInfo.new(1, Enum.EasingStyle.Linear),
  ["BackgroundTransparency"] = TweenInfo.new(0.25, Enum.EasingStyle.Quad, Enum.EasingDirection.Out),
})

-- Remove all transitions
frameRule:SetPropertyTransitions({})
```

**SetPropertyTransitions() Using Tokens**

This example shows how you can assign **tokens** as transition values using a
string with the `$` prefix.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local coreSheet = ReplicatedStorage:FindFirstChild("CoreSheet")
local tokenSheet = ReplicatedStorage:FindFirstChild("Tokens")

-- Set tokens (attributes) on token sheet
tokenSheet:SetAttribute("LinearTransition", TweenInfo.new(1, Enum.EasingStyle.Linear)) 
tokenSheet:SetAttribute("QuadTransition", TweenInfo.new(0.25, Enum.EasingStyle.Quad))

-- Get reference to style rule
local frameRule = coreSheet.Frame

-- Set transitions for multiple properties at once
frameRule:SetPropertyTransitions({
	["BackgroundColor3"] = "$LinearTransition",
	["BackgroundTransparency"] = "$QuadTransition",
})
```

## Inherited Members

### From [StyleBase](/docs/reference/engine/classes/StyleBase.md)

- **Method `GetStyleRules(): List<StyleRule>`**: Returns an array of associated StyleRules.
- **Method `InsertStyleRule(rule: StyleRule, priority: int?): ()`**: Inserts a new StyleRule into the array of rules.
- **Method `SetStyleRules(rules: Instances): ()`**: Similar to InsertStyleRule() but lets
- **Event `StyleRulesChanged`**: Fires when one or more StyleRules is explicitly changed

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