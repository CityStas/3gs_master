---
name: CompositeValueCurve
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "An animation curve that groups child FloatCurves which each animate a different component of a non-unary value."
---

# Class: CompositeValueCurve

> An animation curve that groups child [FloatCurves](/docs/reference/engine/classes/FloatCurve.md) which each
> animate a different component of a non-unary value.

## Description

An animation curve that groups child [FloatCurves](/docs/reference/engine/classes/FloatCurve.md) which each
animate a different component of a non-unary value. The
[CurveType](/docs/reference/engine/classes/CompositeValueCurve.md) property specifies the type of
value to be animated and, depending on this value, differently named children
are used to drive the animation of the components of the value.

As follows are the names of the child curves that drive the animation for each
possible [CompositeValueCurveType](/docs/reference/engine/enums/CompositeValueCurveType.md) value for
[CurveType](/docs/reference/engine/classes/CompositeValueCurve.md):

- [ColorRGB](/docs/reference/engine/enums/CompositeValueCurveType.md): { `"R"`, `"G"`, `"B"` }
- [ColorHSV](/docs/reference/engine/enums/CompositeValueCurveType.md): { `"H"`, `"S"`, `"V"` }
- [NumberRange](/docs/reference/engine/enums/CompositeValueCurveType.md): { `"Min"`, `"Max"` }
- [Rect](/docs/reference/engine/enums/CompositeValueCurveType.md): { `"MinX"`, `"MaxX"`, `"MinY"`,
  `"MaxY"` }
- [UDim](/docs/reference/engine/enums/CompositeValueCurveType.md): { `"Scale"`, `"Offset"` }
- [UDim2](/docs/reference/engine/enums/CompositeValueCurveType.md): { `"ScaleX"`, `"OffsetX"`,
  `"ScaleY"`, `"OffsetY"` }
- [Vector2](/docs/reference/engine/enums/CompositeValueCurveType.md): { `"X"`, `"Y"`}
- [Vector3](/docs/reference/engine/enums/CompositeValueCurveType.md): { `"X"`, `"Y"`, `"Z"` }

The children that drive the animation can be accessed via the
[GetComponentCurves()](/docs/reference/engine/classes/CompositeValueCurve.md) method
which returns an array of curves in the order specified above. The value of
the curve at a given time in the animation may be sampled by the
[GetValueAtTime()](/docs/reference/engine/classes/CompositeValueCurve.md) method.

## Properties

### Property: CompositeValueCurve.CurveType

```json
{
  "type": "CompositeValueCurveType",
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
    "Basic"
  ]
}
```

The type of value animated by this [CompositeValueCurve](/docs/reference/engine/classes/CompositeValueCurve.md). See
[CompositeValueCurveType](/docs/reference/engine/enums/CompositeValueCurveType.md) for options.

## Methods

### Method: CompositeValueCurve:GetComponentCurves

**Signature:** `CompositeValueCurve:GetComponentCurves(): List<FloatCurve>`

This method returns the child curves with the given names for the
[CurveType](/docs/reference/engine/classes/CompositeValueCurve.md) of this
[CompositeValueCurve](/docs/reference/engine/classes/CompositeValueCurve.md), in the order given by the list of child
curves outlined at the top of this page. Any curve that does not exist
prior to calling this method will be created and added as a child with the
appropriate name. That new curve will be an empty [FloatCurve](/docs/reference/engine/classes/FloatCurve.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `List<FloatCurve>` — An array of the child [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) instances that drive the
components of the animated value, in the order listed at the top of
this page. Any expected child curve that does not yet exist is created
as an empty [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) and included in the result.

### Method: CompositeValueCurve:GetValueAtTime

**Signature:** `CompositeValueCurve:GetValueAtTime(time: float): Variant`

This method returns the sampled animated value at the passed `time`
argument. The type of the returned value will match that specified by the
[CurveType](/docs/reference/engine/classes/CompositeValueCurve.md) property.

If any child curve is missing from the children of the curve, the
corresponding value in the returned property will be `0`. For example, if
a curve has a [CurveType](/docs/reference/engine/classes/CompositeValueCurve.md) of
[CompositeValueCurveType.ColorRGB](/docs/reference/engine/enums/CompositeValueCurveType.md) but only one [FloatCurve](/docs/reference/engine/classes/FloatCurve.md)
child named `"G"`, then the returned [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) will have values
of `0` for `"R"` and `"B"`, but the `"G"` value will be sampled from the
child curve.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `time` | `float` |  | Time at which to get the value. |

**Returns:** `Variant` — The value of the curve at the passed time.

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