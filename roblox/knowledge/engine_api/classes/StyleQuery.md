---
name: StyleQuery
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Instance used to set conditions such as `\"MaxSize\"` and `\"PreferredInput\"` for a StyleRule."
---

# Class: StyleQuery

> Instance used to set conditions such as `"MaxSize"` and `"PreferredInput"` for
> a [StyleRule](/docs/reference/engine/classes/StyleRule.md).

## Description

`StyleQuery` is an instance used to set conditions like `"MaxSize"` and
`"PreferredInput"` for a [StyleRule](/docs/reference/engine/classes/StyleRule.md). If the conditions are `true`, the
rule's `@` selector is enabled. This is helpful to author styling with dynamic
container sizes and cross-platform UI.

## Properties

### Property: StyleQuery.IsActive

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "UI"
  ]
}
```

A boolean that determines whether a [StyleRule.Selector](/docs/reference/engine/classes/StyleRule.md) of `@` will
match the `StyleQuery` name. For example, if a `StyleQuery` named
`SmGamepad` has conditions set for [UserInputService.PreferredInput](/docs/reference/engine/classes/UserInputService.md)
of [Gamepad](/docs/reference/engine/enums/PreferredInput.md) and
[GuiService.ViewportDisplaySize](/docs/reference/engine/classes/GuiService.md) of [Small](/docs/reference/engine/enums/DisplaySize.md)
and both of these conditions are `true` (player is playing on a small
display size and using a gamepad), the parent of the `StyleQuery` will
match any [StyleRule.Selector](/docs/reference/engine/classes/StyleRule.md) `@SmGamepad`.

#### Conditions

| Condition | Type | Description |
| --- | --- | --- |
| `AspectRatioRange` | [NumberRange](/docs/reference/engine/datatypes/NumberRange.md) | Evaluates to `true` if the parent width-to-height ratio of [GuiBase2d.AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md) is greater than or equal to `AspectRatioRange.Min` and less than `AspectRatioRange.Max`. |
| `MaxSize` | [Vector2](/docs/reference/engine/datatypes/Vector2.md) | Evaluates to `true` if the parent [GuiBase2d.AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md) is less than `MaxSize`. |
| `MinSize` | [Vector2](/docs/reference/engine/datatypes/Vector2.md) | Evaluates to `true` if the parent [GuiBase2d.AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md) is greater than or equal to `MinSize`. |
| `PreferredInput` | [PreferredInput](/docs/reference/engine/enums/PreferredInput.md) | Evaluates to `true` if `PreferredInput` matches [UserInputService.PreferredInput](/docs/reference/engine/classes/UserInputService.md). |
| `PreferredTextSize` | [PreferredTextSize](/docs/reference/engine/enums/PreferredTextSize.md) | Evaluates to `true` if `PreferredTextSize` matches [GuiService.PreferredTextSize](/docs/reference/engine/classes/GuiService.md). |
| `ReducedMotionEnabled` | boolean | Evaluates to `true` if `ReducedMotionEnabled` matches [GuiService.ReducedMotionEnabled](/docs/reference/engine/classes/GuiService.md). |
| `ViewportDisplaySize` | [DisplaySize](/docs/reference/engine/enums/DisplaySize.md) | Evaluates to `true` if `ViewportDisplaySize` matches [GuiService.ViewportDisplaySize](/docs/reference/engine/classes/GuiService.md). |

## Methods

### Method: StyleQuery:GetCondition

**Signature:** `StyleQuery:GetCondition(name: string): Variant`

Returns the value of a specific condition in the `StyleQuery`.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | String name of the condition, for example `"MaxSize"` or `"ViewportDisplaySize"`. |

**Returns:** `Variant` — Value of the condition.

### Method: StyleQuery:GetConditions

**Signature:** `StyleQuery:GetConditions(): Dictionary`

Returns a dictionary of key-value pairs describing the conditoins set on
the `StyleQuery`.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `Dictionary` — Dictionary of key-value pairs describing the conditions set on the
`StyleQuery`.

### Method: StyleQuery:SetCondition

**Signature:** `StyleQuery:SetCondition(name: string, value: Variant): ()`

Sets a new condition (or modifies an existing condition) for the
`StyleQuery`. The `name` parameter should be a valid condition of
`StyleQuery`, and the assigned value should match the condition's value
type, for example [Vector2](/docs/reference/engine/datatypes/Vector2.md) for `MaxSize` or
[PreferredInput](/docs/reference/engine/enums/PreferredInput.md) for `PreferredInput`.

Attempts to assign invalid condition names such as `"Size"` or `"Input"`
will silently fail. Type mismatches such as [UDim2](/docs/reference/engine/datatypes/UDim2.md) for `MaxSize`
or `string` for `ReducedMotionEnabled` will also fail.

To set multiple conditions for a `StyleQuery` at once, see
[SetConditions()](/docs/reference/engine/classes/StyleQuery.md).

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | Condition name to set, for example `"MinSize"`. |
| `value` | `Variant` |  | Condition value to set, for example [Vector2.new(100, 0)](/docs/reference/engine/datatypes/Vector2.md). |

**Returns:** `()`

**Set Condition**

Demonstrates [StyleQuery:SetCondition()](/docs/reference/engine/classes/StyleQuery.md).

```lua
local styleQuery = Instance.new("StyleQuery")
styleQuery:SetCondition("MaxSize", Vector2.new(200, math.huge))
```

### Method: StyleQuery:SetConditions

**Signature:** `StyleQuery:SetConditions(conditions: Dictionary): ()`

Similar to [SetCondition()](/docs/reference/engine/classes/StyleQuery.md) but lets you
declare and set multiple conditions of the `StyleQuery` at once. Each
`name` parameter should be a valid condition of `StyleQuery`, and the
assigned value should match the condition's value type, for example
[Vector2](/docs/reference/engine/datatypes/Vector2.md) for `MaxSize` or [PreferredInput](/docs/reference/engine/enums/PreferredInput.md) for
`PreferredInput`.

Attempts to assign invalid condition names such as `"Size"` or `"Input"`
will silently fail. Type mismatches such as [UDim2](/docs/reference/engine/datatypes/UDim2.md) for `MaxSize`
or `string` for `ReducedMotionEnabled` will also fail.

To set/update just one condition of a `StyleQuery`, see
[SetCondition()](/docs/reference/engine/classes/StyleQuery.md).

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `conditions` | `Dictionary` |  | Dictionary of key-value pairs defining the conditions to set. |

**Returns:** `()`

**Set Conditions**

Demonstrates [StyleQuery:SetConditions()](/docs/reference/engine/classes/StyleQuery.md).

```lua
local styleQuery = Instance.new("StyleQuery")
styleQuery:SetConditions({
	["AspectRatioRange"] = NumberRange.new(0, 1),
	["MaxSize"] = Vector2.new(200, math.huge),
})
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