---
name: NumberValue
last_updated: 2026-10-30T19:55:52Z
inherits:
  - ValueBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "A container object for a single double-precision floating point number."
---

# Class: NumberValue

> A container object for a single double-precision floating point number.

## Description

Store a single [Luau number](https://luau.org/syntax#number-literals), defined
to be
[double-precision floating point number](https://en.wikipedia.org/wiki/Double-precision_floating-point_format),
or more commonly known as a **double**. This stores a number in 64 bits (8
bytes) using the IEEE 754 representation (1 sign bit, 11 exponent bits and 52
fractional bits). Maximum and minimum values are
&PlusMinus;1.7976931348623157e+308, with a range of &PlusMinus;2^53 for exact
integer representations.

Like all [ValueBase](/docs/reference/engine/classes/ValueBase.md) objects, this single value is stored in the
[Value](/docs/reference/engine/classes/NumberValue.md) property. The `Changed` event fires with the
new value being stored in the object, instead of a string representing the
property being changed.

## Code Samples

**Changed Event**

This sample demonstrates the subtleties of the `Changed` event on normal
objects and `Value` objects.

```lua
-- Demonstrate the Changed event by creating a Part
local part = Instance.new("Part")
part.Changed:Connect(print)
-- This fires Changed with "Transparency"
part.Transparency = 0.5
-- Similarly, this fires Changed with "Number"
part.Name = "SomePart"
-- Since changing BrickColor will also change other
-- properties at the same time, this line fires Changed
-- with "BrickColor", "Color3" and "Color3uint16".
part.BrickColor = BrickColor.Red()

-- A NumberValue holds a double-precision floating-point number
local vNumber = Instance.new("NumberValue")
vNumber.Changed:Connect(print)
-- This fires Changed with 123.456 (not "Value")
vNumber.Value = 123.456
-- This does not fire Changed
vNumber.Name = "SomeNumber"

-- A StringValue stores one string
local vString = Instance.new("StringValue")
vString.Changed:Connect(print)
-- This fires Changed with "Hello" (not "Value")
vString.Value = "Hello"
```

## Properties

### Property: NumberValue.Value

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
  "category": "Data",
  "simulationAccess": true
}
```

Used to hold a double value.

## Events

### Event: NumberValue.Changed

**Signature:** `NumberValue.Changed(value: double)`

Fires whenever the [NumberValue.Value](/docs/reference/engine/classes/NumberValue.md) changes. It runs with the new
value being stored in the argument object, instead of a string
representing the property being changed.

Listening for the `Changed` signal can be useful in games that use
`NumberValues` to track values like leaderboard statistics or item prices.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `value` | `double` | The new value after the change. |

**NumberValue Changed**

This example prints the new value of the `NumberValue` each time it changes.
Here it prints 20.

```lua
local numberValue = script.Parent.NumberValue

local function printValue(value)
	print(value)
end

numberValue.Changed:Connect(printValue)

numberValue.Value = 20
```

### Event: NumberValue.changed

**Signature:** `NumberValue.changed(value: double)`

> **Deprecated:** This event is a deprecated variant of [NumberValue.Changed](/docs/reference/engine/classes/NumberValue.md) which should be used instead.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `value` | `double` |  |

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