---
name: Object
last_updated: 2026-10-30T19:55:52Z
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "`Object` is the base class for all classes in the Roblox class hierarchy."
---

# Class: Object

> `Object` is the base class for all classes in the Roblox class hierarchy.

## Description

`Object` is the base class for all classes in the Roblox class hierarchy.
Every other class that the Roblox Engine defines inherits all of the members
of `Object`. It is not possible to directly create an `Object`.

## Properties

### Property: Object.ClassName

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
  "category": "Data"
}
```

A read-only string representing the class this [Object](/docs/reference/engine/classes/Object.md) belongs to.

This property can be used with various other functions that are used to
identify objects by type, such as [Object:IsA()](/docs/reference/engine/classes/Object.md) or
[Instance:FindFirstChildOfClass()](/docs/reference/engine/classes/Instance.md).

Note this property is read only and cannot be altered by scripts.
Developers wishing to change an object's class will instead have to create
a new [Object](/docs/reference/engine/classes/Object.md).

Unlike [Object:IsA()](/docs/reference/engine/classes/Object.md), ClassName can be used to check if an object
belongs to a specific class ignoring class inheritance. For example:

**Class Name**

Demonstrates [Object.ClassName](/docs/reference/engine/classes/Object.md).

```lua
for _, child in workspace:GetChildren() do
    if child.ClassName == "Part" then
        print("Found a Part")
        -- will find Parts in model, but NOT TrussParts, WedgeParts, etc
    end
end
```

### Property: Object.className

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

> **Deprecated:** This deprecated property is a variant of [Object.ClassName](/docs/reference/engine/classes/Object.md) which should be used instead.

## Methods

### Method: Object:GetPropertyChangedSignal

**Signature:** `Object:GetPropertyChangedSignal(property: string): RBXScriptSignal`

This method returns an event that behaves exactly like the
[Changed](/docs/reference/engine/classes/Object.md) event, except that it only fires when the
given property changes. It's generally a good idea to use this method
instead of a connection to [Changed](/docs/reference/engine/classes/Object.md) with a function
that checks the property name. Subsequent calls to this method on the same
object with the same property name return the same event.

[ValueBase](/docs/reference/engine/classes/ValueBase.md) objects, such as [IntValue](/docs/reference/engine/classes/IntValue.md) and
[StringValue](/docs/reference/engine/classes/StringValue.md), use a modified [Changed](/docs/reference/engine/classes/Object.md) event
that fires with the contents of their `Value` property. As such, this
method provides a way to detect changes in other properties of those
objects.

Note that this event will not pass any arguments to a connected function,
so the value of the changed property must be read directly within a
script.

#### Limitations

The event returned by this method does **not** fire for physics-related
changes, such as when the [CFrame](/docs/reference/engine/classes/BasePart.md),
[AssemblyLinearVelocity](/docs/reference/engine/classes/BasePart.md),
[AssemblyAngularVelocity](/docs/reference/engine/classes/BasePart.md),
[Position](/docs/reference/engine/classes/BasePart.md), or
[Orientation](/docs/reference/engine/classes/BasePart.md) properties of a [BasePart](/docs/reference/engine/classes/BasePart.md)
change due to gravity. To detect changes in these properties, consider
using a physics-based event like [RunService.PreSimulation](/docs/reference/engine/classes/RunService.md).

Additionally, the returned event may not fire on every modification of
properties that change very frequently, and/or it may not fire for such
properties at all. It's recommended that you carefully test for property
changes that impact game logic.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `property` | `string` |  | The property to connect to. |

**Returns:** `RBXScriptSignal` — A signal that fires whenever the property changes.

**Old-to-New Values with Changed**

This code sample demonstrates how to save a value before a changed event fires
on it in order to get more information about a change.

```lua
local part = Instance.new("Part")

local currentColor = part.BrickColor

local function onBrickColorChanged()
	local newColor = part.BrickColor
	print("Color changed from", currentColor.Name, "to", newColor.Name)
	currentColor = newColor
end
part:GetPropertyChangedSignal("BrickColor"):Connect(onBrickColorChanged)

part.BrickColor = BrickColor.new("Really red")
part.BrickColor = BrickColor.new("Really blue")
```

**Changed and GetPropertyChangedSignal**

This code sample demonstrates the equivalence of the `Changed` event and event
returned by `GetPropertyChangedSignal`.

```lua
local part = Instance.new("Part")

local function onBrickColorChanged()
	print("My color is now " .. part.BrickColor.Name)
end

local function onChanged(property)
	if property == "BrickColor" then
		onBrickColorChanged()
	end
end

part:GetPropertyChangedSignal("BrickColor"):Connect(onBrickColorChanged)
part.Changed:Connect(onChanged)

-- Trigger some changes (because we connected twice,
-- both of these will cause two calls to onBrickColorChanged)
part.BrickColor = BrickColor.new("Really red")
part.BrickColor = BrickColor.new("Institutional white")
```

### Method: Object:IsA

**Signature:** `Object:IsA(className: string): boolean`

IsA returns true if the object's class is **equivalent to** or a
**subclass** of a given class. This function is similar to the
**instanceof** operators in other languages, and is a form of
[type introspection](https://en.wikipedia.org/wiki/Type_introspection). To
ignore class inheritance, test the [ClassName](/docs/reference/engine/classes/Object.md)
property directly instead. For checking native Luau data types (number,
string, etc) use the functions `type` and `typeof`.

Most commonly, this function is used to test if an object is some kind of
part, such as [Part](/docs/reference/engine/classes/Part.md) or [WedgePart](/docs/reference/engine/classes/WedgePart.md), which inherits from
[BasePart](/docs/reference/engine/classes/BasePart.md) (an abstract class). For example, if your goal is to
change all of a character's limbs to the same color, you might use
[GetChildren](/docs/reference/engine/classes/Instance.md) to iterate over the children,
then use IsA to filter non-[BasePart](/docs/reference/engine/classes/BasePart.md) objects which lack the
[BrickColor](/docs/reference/engine/datatypes/BrickColor.md) property:

```lua
local Players = game:GetService("Players")

local function paintFigure(character, color)
	-- Iterate over the child objects of the character
	for _, child in character:GetChildren() do
		-- Filter out non-part objects, such as Shirt, Pants and Humanoid
		-- R15 use MeshPart and R6 use Part, so we use BasePart here to detect both:
		if child:IsA("BasePart") then
			child.BrickColor = color
		end
	end
end
paintFigure(Players.Player.Character, BrickColor.new("Bright blue"))
```

Since all classes inherit from [Object](/docs/reference/engine/classes/Object.md), calling
`object:IsA("Object")` will always return true.

*Security: None · Thread Safety: Safe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` |  | The class against which the Object's class will be checked. Case-sensitive. |

**Returns:** `boolean` — Describes whether the Object's class matched or is a subclass of the
given class.

**Instance:IsA()**

Demonstrates determining the class of Workspace using [Instance:IsA()](/docs/reference/engine/classes/Instance.md)

Workspace is of class 'Workspace', so the first statement is true. Workspace
is not of class 'BasePart', so the second statement is false. Workspace
inherits from Instance and therefore is of class 'Instance', so the third
statement is true.

```lua
local Workspace = game:GetService("Workspace")

print(Workspace:IsA("Workspace")) -- true
print(Workspace:IsA("BasePart")) -- false
print(Workspace:IsA("Instance")) -- true
```

### Method: Object:isA

**Signature:** `Object:isA(className: string): boolean`

> **Deprecated:** This deprecated function is a variant of [Object:IsA()](/docs/reference/engine/classes/Object.md) which should be used instead.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` |  |  |

**Returns:** `boolean`

## Events

### Event: Object.Changed

**Signature:** `Object.Changed(property: string)`

This event fires immediately after an object property is changed, with
some exceptions (see below). The new value of a changed property is
**not** passed as a parameter. Instead, you can access it using
`object[property]`:

```
object.Changed:Connect(function(property)
	print("The new property's value is", object[property])
end)
```

- If you are only interested in listening for changes to one specific
  property, consider using the
  [GetPropertyChangedSignal()](/docs/reference/engine/classes/Object.md)
  method instead.
- To listen for changes in attributes, see
  [Instance:GetAttributeChangedSignal()](/docs/reference/engine/classes/Instance.md) and
  [Instance.AttributeChanged](/docs/reference/engine/classes/Instance.md).
- To detect when children are added or removed, see
  [Instance.ChildAdded](/docs/reference/engine/classes/Instance.md) and [Instance.ChildRemoved](/docs/reference/engine/classes/Instance.md).

For [ValueBase](/docs/reference/engine/classes/ValueBase.md) objects such as [IntValue](/docs/reference/engine/classes/IntValue.md) and
[StringValue](/docs/reference/engine/classes/StringValue.md), this event only fires when the object's `Value`
property changes. To detect other changes in [ValueBase](/docs/reference/engine/classes/ValueBase.md) objects,
use [GetPropertyChangedSignal()](/docs/reference/engine/classes/Object.md).

#### Limitations

This event does **not** fire for physics-related changes, such as when the
[CFrame](/docs/reference/engine/classes/BasePart.md),
[AssemblyLinearVelocity](/docs/reference/engine/classes/BasePart.md),
[AssemblyAngularVelocity](/docs/reference/engine/classes/BasePart.md),
[Position](/docs/reference/engine/classes/BasePart.md), or
[Orientation](/docs/reference/engine/classes/BasePart.md) properties of a [BasePart](/docs/reference/engine/classes/BasePart.md)
change due to gravity. To detect changes in these properties, consider
using a physics-based event like [RunService.PreSimulation](/docs/reference/engine/classes/RunService.md).
Similarly, the `Changed` event does not fire when
[AssemblyMass](/docs/reference/engine/classes/BasePart.md) updates due to a change in
material, size, or density for a welded part (but the event does fire for
[Mass](/docs/reference/engine/classes/BasePart.md) if you modify a part's size).

For properties that change frequently, the `Changed` event might not fire
for every modification, or it might not fire at all. **If a property
change impacts your game logic, test carefully** to ensure the event is
firing as you expect.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `property` | `string` | The name of the property that changed. |

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

**Change Detector**

This code sample demonstrates the Changed event firing within a parent object.

```lua
local object = script.Parent

local function onChanged(property)
	-- Get the current value of the property
	local value = object[property]
	-- Print a message saying what changed
	print(object:GetFullName() .. "." .. property .. " (" .. typeof(value) .. ") changed to " .. tostring(value))
end

object.Changed:Connect(onChanged)
-- Trigger a simple change in the object (add an underscore to the name)
object.Name = "_" .. object.Name
```