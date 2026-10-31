---
name: WireframeHandleAdornment
last_updated: 2026-10-30T19:55:53Z
inherits:
  - HandleAdornment
  - PVAdornment
  - GuiBase3d
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Renders a wireframe adornment consisting of one or more lines onto a BasePart (including Terrain) or into the Workspace."
---

# Class: WireframeHandleAdornment

> Renders a wireframe adornment consisting of one or more lines onto a
> [BasePart](/docs/reference/engine/classes/BasePart.md) (including [Terrain](/docs/reference/engine/classes/Terrain.md)) or into the [Workspace](/docs/reference/engine/classes/Workspace.md).

## Description

`WireframeHandleAdornment` renders a wireframe adornment consisting of one or
more lines onto a [BasePart](/docs/reference/engine/classes/BasePart.md) (including [Terrain](/docs/reference/engine/classes/Terrain.md)) or into the
[Workspace](/docs/reference/engine/classes/Workspace.md). If parented to a player's [PlayerGui](/docs/reference/engine/classes/PlayerGui.md) or the
[CoreGui](/docs/reference/engine/classes/CoreGui.md), this adornment can listen to input events for purposes such
as making dragger tools.

Note that a `WireframeHandleAdornment` instance **begins empty** and you must
add lines or paths to it through methods like
[AddLines()](/docs/reference/engine/classes/WireframeHandleAdornment.md) or
[AddPath()](/docs/reference/engine/classes/WireframeHandleAdornment.md).

The rendered wireframe can be customized visually through its
[Thickness](/docs/reference/engine/classes/WireframeHandleAdornment.md),
[Color3](/docs/reference/engine/classes/WireframeHandleAdornment.md), and
[Transparency](/docs/reference/engine/classes/WireframeHandleAdornment.md) properties,
although these properties only affect subsequent draws and do not update lines
already drawn into the adornment.

## Code Samples

**Basic Path Wireframe**

```lua
local wireframe = script.Parent

-- Declare four points in a square arrangement
local pathArray = {
	Vector3.new(-10, 10, 0),
	Vector3.new(10, 10, 0),
	Vector3.new(10, -10, 0),
	Vector3.new(-10, -10, 0)
}

-- Apply path to adornment and close it (connect starting and ending points)
wireframe:AddPath(pathArray, true)
```

**Multicolor Wireframe**

```lua
local wireframe = script.Parent

wireframe.Color3 = Color3.fromRGB(255, 0, 0) -- Sets next line to red
wireframe:AddLine(Vector3.new(-10, 0, 0), Vector3.new(10, 0, 0))
wireframe.Color3 = Color3.fromRGB(0, 255, 0) -- Sets next line to green
wireframe:AddLine(Vector3.new(0, -10, 0), Vector3.new(0, 10, 0))
wireframe.Color3 = Color3.fromRGB(0, 0, 255) -- Sets next line to blue
wireframe:AddLine(Vector3.new(0, 0, -10), Vector3.new(0, 0, 10))
```

## Properties

### Property: WireframeHandleAdornment.Scale

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
    "Basic",
    "UI"
  ]
}
```

This property specifies the **XYZ** scale of the wireframe adornment as a
[Vector3](/docs/reference/engine/datatypes/Vector3.md). For example, a scale of
[Vector3.new(1, 2, 1)](/docs/reference/engine/datatypes/Vector3.md) will scale the adornment twice its normal
size on the **Y** axis while keeping the **X** and **Z** axes unchanged.

### Property: WireframeHandleAdornment.Thickness

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
    "Basic",
    "UI"
  ]
}
```

This property determines the thickness of the wireframe adornment's lines
in pixels. Note that this visual thickness does not change relative to the
adornment's distance from the viewer's camera.

## Methods

### Method: WireframeHandleAdornment:AddLine

**Signature:** `WireframeHandleAdornment:AddLine(from: Vector3, to: Vector3): ()`

This method adds a line to the wireframe adornment from a starting point
to an ending point, both defined as a [Vector3](/docs/reference/engine/datatypes/Vector3.md) relative to the
center of the [Adornee](/docs/reference/engine/classes/WireframeHandleAdornment.md).

Note that you can make a multicolor wireframe by changing the adornment's
[Color3](/docs/reference/engine/classes/WireframeHandleAdornment.md) property before new lines
are drawn via [AddLine()](/docs/reference/engine/classes/WireframeHandleAdornment.md), as
demonstrated in the following code sample.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic, UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `from` | `Vector3` |  | Starting point of the line. |
| `to` | `Vector3` |  | Ending point of the line. |

**Returns:** `()`

**Multicolor Wireframe**

```lua
local wireframe = script.Parent

wireframe.Color3 = Color3.fromRGB(255, 0, 0) -- Sets next line to red
wireframe:AddLine(Vector3.new(-10, 0, 0), Vector3.new(10, 0, 0))
wireframe.Color3 = Color3.fromRGB(0, 255, 0) -- Sets next line to green
wireframe:AddLine(Vector3.new(0, -10, 0), Vector3.new(0, 10, 0))
wireframe.Color3 = Color3.fromRGB(0, 0, 255) -- Sets next line to blue
wireframe:AddLine(Vector3.new(0, 0, -10), Vector3.new(0, 0, 10))
```

### Method: WireframeHandleAdornment:AddLines

**Signature:** `WireframeHandleAdornment:AddLines(points: Array): ()`

This method adds one or more lines of the current
[Color3](/docs/reference/engine/classes/WireframeHandleAdornment.md) color to the wireframe
adornment using an array. Each pair of [Vector3](/docs/reference/engine/datatypes/Vector3.md) points in the
array acts as a starting point and ending point for a line, relative to
the center of the [Adornee](/docs/reference/engine/classes/WireframeHandleAdornment.md).

Note that lines are rendered independently and their ending points are not
connected to the starting point of any other line. To connect multiple
line segments in a sequence from point to point, see
[AddPath()](/docs/reference/engine/classes/WireframeHandleAdornment.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Basic, UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `points` | `Array` |  | Array of [Vector3](/docs/reference/engine/datatypes/Vector3.md) points in which each pair acts as a starting point and ending point for a line. |

**Returns:** `()`

**Wireframe Lines From Array**

```lua
local wireframe = script.Parent

local linesArray = {
	Vector3.new(-10, 0, 0), -- Starting point of first line
	Vector3.new(10, 0, 0), -- Ending point of first line
	Vector3.new(0, -10, 0), -- Starting point of second line
	Vector3.new(0, 10, 0), -- Ending point of second line
	Vector3.new(0, 0, -10), -- Starting point of third line
	Vector3.new(0, 0, 10) -- Ending point of third line
}
-- Apply path to adornment
wireframe:AddLines(linesArray)
```

### Method: WireframeHandleAdornment:AddPath

**Signature:** `WireframeHandleAdornment:AddPath(points: Array, loop: boolean): ()`

This method adds multiple line segments of the current
[Color3](/docs/reference/engine/classes/WireframeHandleAdornment.md) color to the wireframe
adornment in a sequence from point to point. The path can be closed
(ending point connected to starting point) by setting the `loop` parameter
to `true`.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic, UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `points` | `Array` |  | Array of [Vector3](/docs/reference/engine/datatypes/Vector3.md) points to connect in sequence with line segments. |
| `loop` | `boolean` |  | Whether the path is closed by connecting its ending point to its starting point with an additional line. |

**Returns:** `()`

**Basic Path Wireframe**

```lua
local wireframe = script.Parent

-- Declare four points in a square arrangement
local pathArray = {
	Vector3.new(-10, 10, 0),
	Vector3.new(10, 10, 0),
	Vector3.new(10, -10, 0),
	Vector3.new(-10, -10, 0)
}

-- Apply path to adornment and close it (connect starting and ending points)
wireframe:AddPath(pathArray, true)
```

### Method: WireframeHandleAdornment:AddText

**Signature:** `WireframeHandleAdornment:AddText(point: Vector3, text: string, size?: int): ()`

Adds a text label to the wireframe adornment at a [Vector3](/docs/reference/engine/datatypes/Vector3.md) point
relative to the center of the
[Adornee](/docs/reference/engine/classes/WireframeHandleAdornment.md). You can adjust the size
of the text through the `size` parameter, and the label renders in the
current [Color3](/docs/reference/engine/classes/WireframeHandleAdornment.md) color.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic, UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `point` | `Vector3` |  | Position of the text in the adornment. |
| `text` | `string` |  | String to display. |
| `size` | `int` | `12` | Size of the text. |

**Returns:** `()`

### Method: WireframeHandleAdornment:Clear

**Signature:** `WireframeHandleAdornment:Clear(): ()`

Instantly clears all lines and text in the wireframe adornment.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic, UI*

**Returns:** `()`

## Inherited Members

### From [HandleAdornment](/docs/reference/engine/classes/HandleAdornment.md)

- **Property `AdornCullingMode`** (`AdornCullingMode`): Determines whether to automatically cull the adornment.
- **Property `AlwaysOnTop`** (`boolean`): Forces this adornment to render on top of all 3D objects in the workspace.
- **Property `CFrame`** (`CFrame`): The position and rotation of the object relative to its
- **Property `SizeRelativeOffset`** (`Vector3`): The positional offset of the adornment based on the adornee's
- **Property `ZIndex`** (`int`): Determines the draw order of this HandleAdornment when
- **Event `MouseButton1Down`**: Fires when a player presses down on their left mouse button while hovering
- **Event `MouseButton1Up`**: Fires when a player releases their left mouse button while hovering over
- **Event `MouseEnter`**: Fires when a player moves their mouse over the adornment.
- **Event `MouseLeave`**: Fires when a player moves their mouse out of the adornment.

### From [PVAdornment](/docs/reference/engine/classes/PVAdornment.md)

- **Property `Adornee`** (`PVInstance`): The PVInstance which this PVAdornment is attached to.

### From [GuiBase3d](/docs/reference/engine/classes/GuiBase3d.md)

- **Property `Color`** (`BrickColor`): Sets the color of a GUI object. *(deprecated, hidden)*
- **Property `Color3`** (`Color3`): Sets the color of this GuiBase3d object.
- **Property `Transparency`** (`float`): Sets the transparency of this GuiBase3d object.
- **Property `Visible`** (`boolean`): Determines whether this GuiBase3d object and its descendants will

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