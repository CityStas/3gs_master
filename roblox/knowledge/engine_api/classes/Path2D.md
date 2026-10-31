---
name: Path2D
last_updated: 2026-10-30T19:55:52Z
inherits:
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Represents a 2D cubic spline path that renders a stroked curve under any GuiObject."
---

# Class: Path2D

> Represents a 2D cubic spline path that renders a stroked curve under any
> [GuiObject](/docs/reference/engine/classes/GuiObject.md).

## Description

`Path2D` is a UI instance that represents a 2D spline. It can be placed under
any [GuiObject](/docs/reference/engine/classes/GuiObject.md) and be edited directly in the viewport using built‑in
tooling. `Path2D` stores control points and exposes methods to sample
positions along the curve, enabling curved UI layouts, path‑based animations,
and interactive tools like graph editors and visual effects.

See the [2D paths](/docs/en-us/ui/2D-paths.md) guide for more information and
usage examples.

## Properties

### Property: Path2D.Closed

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

When set to `true`, the path forms a closed loop by connecting the last
control point back to the first. The closure only takes effect when the
path has at least 3 control points. Defaults to `false`.

### Property: Path2D.Color3

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
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

Determines the stroke color used to render the [Path2D](/docs/reference/engine/classes/Path2D.md). Defaults to
`[0, 0, 0]` (black). A child [UIGradient](/docs/reference/engine/classes/UIGradient.md) can override the solid
color with a gradient fill.

### Property: Path2D.SelectedControlPoint

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Control Points",
  "capabilities": [
    "UI"
  ]
}
```

The 1-based index of the currently selected control point. Defaults to `1`
and is clamped to the range [1, number of control points]. Changing this
value updates [Path2D.SelectedControlPointData](/docs/reference/engine/classes/Path2D.md) to reflect the
control point at the new index.

### Property: Path2D.SelectedControlPointData

```json
{
  "type": "Path2DControlPoint",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Control Points",
  "capabilities": [
    "UI"
  ]
}
```

A read-only computed property that returns the
[Path2DControlPoint](/docs/reference/engine/datatypes/Path2DControlPoint.md) at the index specified by
[Path2D.SelectedControlPoint](/docs/reference/engine/classes/Path2D.md). If the path has no control points,
returns a default-constructed [Path2DControlPoint](/docs/reference/engine/datatypes/Path2DControlPoint.md) (position and
tangents all at `{0, 0, 0, 0}`).

### Property: Path2D.Thickness

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

Determines the stroke width of the [Path2D](/docs/reference/engine/classes/Path2D.md) in pixels. Defaults to
`1` and is clamped to the range [0, 100].

### Property: Path2D.Visible

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

Determines if the [Path2D](/docs/reference/engine/classes/Path2D.md) path is rendered or not. When `false`,
the path will not render. However, any modifications to the control points
will update correctly, ensuring that querying data will have the correct
info.

### Property: Path2D.ZIndex

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

Determines the order in which a [Path2D](/docs/reference/engine/classes/Path2D.md) path renders relative to
other GUIs. Works the same as [GuiObject.ZIndex](/docs/reference/engine/classes/GuiObject.md) but does not
interact with layout order in any way.

## Methods

### Method: Path2D:GetBoundingRect

**Signature:** `Path2D:GetBoundingRect(): Rect`

Returns the [Rect](/docs/reference/engine/datatypes/Rect.md) bounding size for the [Path2D](/docs/reference/engine/classes/Path2D.md). This is
computed based on the control points and is not modifiable outside of
changing the control point data.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `Rect` — The [Rect](/docs/reference/engine/datatypes/Rect.md) bounding box that encloses the path, expanded by
its rendered thickness.

### Method: Path2D:GetControlPoint

**Signature:** `Path2D:GetControlPoint(index: int): Path2DControlPoint`

Returns the [Path2DControlPoint](/docs/reference/engine/datatypes/Path2DControlPoint.md) for a given index. If the index
is out of bounds, this method will throw an error.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `index` | `int` |  | The 1-based index of the control point to return. |

**Returns:** `Path2DControlPoint` — The control point at the given index.

### Method: Path2D:GetControlPoints

**Signature:** `Path2D:GetControlPoints(): Array`

Returns a table of all the
[Path2DControlPoints](/docs/reference/engine/datatypes/Path2DControlPoint.md) for the [Path2D](/docs/reference/engine/classes/Path2D.md).

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `Array` — Table of all the [Path2DControlPoints](/docs/reference/engine/datatypes/Path2DControlPoint.md).

### Method: Path2D:GetLength

**Signature:** `Path2D:GetLength(): float`

Returns the length of the [Path2D](/docs/reference/engine/classes/Path2D.md). This function can be expensive
if called too frequently.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `float` — The total length of the path.

### Method: Path2D:GetMaxControlPoints

**Signature:** `Path2D:GetMaxControlPoints(): int`

Returns `100`, the hard upper limit on the number of control points a
[Path2D](/docs/reference/engine/classes/Path2D.md) can contain. Attempting to add points beyond this limit via
[Path2D:InsertControlPoint()](/docs/reference/engine/classes/Path2D.md) or [Path2D:SetControlPoints()](/docs/reference/engine/classes/Path2D.md)
throws an error.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `int` — The maximum number of control points a [Path2D](/docs/reference/engine/classes/Path2D.md) supports.

### Method: Path2D:GetPositionOnCurve

**Signature:** `Path2D:GetPositionOnCurve(t: float): UDim2`

Returns the 2D [UDim2](/docs/reference/engine/datatypes/UDim2.md) position at a given `t` value between `0`
and `1` (inclusive), representing the parameter space result of querying
the spline. The values will be more tightly packed near bends and wider
apart in straighter segments; see
[GetPositionOnCurveArcLength()](/docs/reference/engine/classes/Path2D.md)
for even spacing results.

Throws an error if the [Path2D](/docs/reference/engine/classes/Path2D.md) has less than two control points.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `float` |  | The value to query the [Path2D](/docs/reference/engine/classes/Path2D.md) at. |

**Returns:** `UDim2` — The position in parameter space.

### Method: Path2D:GetPositionOnCurveArcLength

**Signature:** `Path2D:GetPositionOnCurveArcLength(t: float): UDim2`

Returns the 2D [UDim2](/docs/reference/engine/datatypes/UDim2.md) position at a given `t` value between `0`
and `1` (inclusive), representing the arc length space result of querying
the spline. The values will be evenly spaced along the spline; see
[GetPositionOnCurve()](/docs/reference/engine/classes/Path2D.md) for parameter
spacing results.

Throws an error if the [Path2D](/docs/reference/engine/classes/Path2D.md) has less than two control points.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `float` |  | The value to query the Path2D at. |

**Returns:** `UDim2` — The position in arc length space.

### Method: Path2D:GetTangentOnCurve

**Signature:** `Path2D:GetTangentOnCurve(t: float): Vector2`

Returns the tangent at a given `t` value in parameter space where `t` is a
value between `0` and `1` (inclusive). Throws an error if the
[Path2D](/docs/reference/engine/classes/Path2D.md) has less than two control points.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `float` |  | The value to query the [Path2D](/docs/reference/engine/classes/Path2D.md) at. |

**Returns:** `Vector2` — The tangent in parameter space.

### Method: Path2D:GetTangentOnCurveArcLength

**Signature:** `Path2D:GetTangentOnCurveArcLength(t: float): Vector2`

Returns the tangent at a given `t` value in arc length space where `t` is
a value between `0` and `1` (inclusive). Throws an error if the
[Path2D](/docs/reference/engine/classes/Path2D.md) has less than two control points.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `float` |  | The value to query the [Path2D](/docs/reference/engine/classes/Path2D.md) at. |

**Returns:** `Vector2` — The tangent in arc length space.

### Method: Path2D:InsertControlPoint

**Signature:** `Path2D:InsertControlPoint(index: int, point: Path2DControlPoint): ()`

Inserts a new [Path2DControlPoint](/docs/reference/engine/datatypes/Path2DControlPoint.md) at a given index. Throws a
warning if the index is out of bounds or if you're trying to add control
points past the limit of 50.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `index` | `int` |  | The index to insert at. |
| `point` | `Path2DControlPoint` |  | The control point to insert. |

**Returns:** `()`

### Method: Path2D:RemoveControlPoint

**Signature:** `Path2D:RemoveControlPoint(index: int): ()`

Removes a control point at the given index. Throws a warning if the index
is out of bounds.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `index` | `int` |  | The index to remove at. |

**Returns:** `()`

### Method: Path2D:SetControlPoints

**Signature:** `Path2D:SetControlPoints(controlPoints: Array): ()`

Sets all the control points to the specified array, replacing all existing
points with new ones. Throws a warning if there are more than 50 points in
the `controlPoints` array.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `controlPoints` | `Array` |  | The new list of control points to set. |

**Returns:** `()`

### Method: Path2D:UpdateControlPoint

**Signature:** `Path2D:UpdateControlPoint(index: int, point: Path2DControlPoint): ()`

Updates the control point at the given index. Throws a warning if the
index is out of range.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `index` | `int` |  | The control point index to update. |
| `point` | `Path2DControlPoint` |  | The new [Path2DControlPoint](/docs/reference/engine/datatypes/Path2DControlPoint.md) value to store at the index. |

**Returns:** `()`

## Events

### Event: Path2D.ControlPointChanged

**Signature:** `Path2D.ControlPointChanged()`

Fires whenever the path's control-point data is mutated. This includes
calls to [Path2D:SetControlPoints()](/docs/reference/engine/classes/Path2D.md),
[Path2D:InsertControlPoint()](/docs/reference/engine/classes/Path2D.md), [Path2D:UpdateControlPoint()](/docs/reference/engine/classes/Path2D.md),
and [Path2D:RemoveControlPoint()](/docs/reference/engine/classes/Path2D.md). Does not fire for changes to
visual properties such as [Path2D.Color3](/docs/reference/engine/classes/Path2D.md) or
[Path2D.Thickness](/docs/reference/engine/classes/Path2D.md).

*Security: None · Capabilities: UI*

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