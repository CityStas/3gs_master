---
name: DraggerService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "A service that centralizes the global dragger settings that Studio's dragging tools read so they move, snap, and highlight objects consistently."
---

# Class: DraggerService

> A service that centralizes the global dragger settings that Studio's dragging
> tools read so they move, snap, and highlight objects consistently.

## Description

`DraggerService` is a central hub for dragger-related settings that Studio's
dragging tools (and other dragger-like editing UX) read when deciding how to
move, snap, and highlight objects. Because the Move, Scale, and Rotate tools
all consult the same service, changing a setting here keeps their snapping,
collision, joint, and hover behavior in sync. Each property reflects the
corresponding Studio editing preference or global editing state.

## Properties

### Property: DraggerService.AlignDraggedObjects

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
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

When `true`, a dragged object is rotated to align with the surface it is
dropped on instead of keeping its original orientation. This reflects
Studio's "Align Dragged Objects" editing preference and is read by the
dragging tools.

### Property: DraggerService.AngleSnapEnabled

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
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

When `true`, rotating an object with a dragger snaps the rotation to
multiples of [DraggerService.AngleSnapIncrement](/docs/reference/engine/classes/DraggerService.md). When `false`,
rotation is continuous and the increment has no effect.

### Property: DraggerService.AngleSnapIncrement

```json
{
  "type": "float",
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

The rotation snapping step, in degrees, applied while
[DraggerService.AngleSnapEnabled](/docs/reference/engine/classes/DraggerService.md) is `true`; it has no effect when
angle snapping is disabled. The value is clamped to a small positive
minimum, so it can never be set to `0` or a negative number.

### Property: DraggerService.AnimateHover

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
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

When `true`, the highlight drawn over the object under the cursor animates
(pulses) at [DraggerService.HoverAnimateFrequency](/docs/reference/engine/classes/DraggerService.md). It only has a
visible effect when [DraggerService.ShowHover](/docs/reference/engine/classes/DraggerService.md) is `true`.

### Property: DraggerService.CollisionsEnabled

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
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

When `true`, dragging performs collision checking so that a moved object
stops against other parts instead of passing through them. When `false`,
objects can be dragged freely through existing geometry.

### Property: DraggerService.DraggerCoordinateSpace

```json
{
  "type": "DraggerCoordinateSpace",
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

Controls the coordinate space draggers operate in:
[DraggerCoordinateSpace.Object](/docs/reference/engine/enums/DraggerCoordinateSpace.md) moves and rotates relative to the
object's own orientation, while [DraggerCoordinateSpace.World](/docs/reference/engine/enums/DraggerCoordinateSpace.md) uses
the global axes. Defaults to [DraggerCoordinateSpace.Object](/docs/reference/engine/enums/DraggerCoordinateSpace.md).

### Property: DraggerService.DraggerMovementMode

```json
{
  "type": "DraggerMovementMode",
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

Selects how draggers compute movement:
[DraggerMovementMode.Geometric](/docs/reference/engine/enums/DraggerMovementMode.md) applies transforms directly, while
[DraggerMovementMode.Physical](/docs/reference/engine/enums/DraggerMovementMode.md) respects physical constraints while
dragging. Defaults to [DraggerMovementMode.Geometric](/docs/reference/engine/enums/DraggerMovementMode.md).

### Property: DraggerService.GeometrySnapColor

```json
{
  "type": "Color3",
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

The [Color3](/docs/reference/engine/datatypes/Color3.md) used to draw the snapping indicators (such as
pivot-to-geometry snap points) shown while dragging. It reflects the
corresponding Studio color preference.

### Property: DraggerService.HoverAnimateFrequency

```json
{
  "type": "float",
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

How fast the hover highlight pulses, in cycles per second, when
[DraggerService.AnimateHover](/docs/reference/engine/classes/DraggerService.md) is `true`. The value corresponds to
Studio's hover-animation speed preference, which ranges from `0.5` (very
slow) to `10` (very fast).

### Property: DraggerService.HoverThickness

```json
{
  "type": "float",
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

The thickness of the outline drawn around the object beneath the cursor.
It is only visible when [DraggerService.ShowHover](/docs/reference/engine/classes/DraggerService.md) is `true`, and
reflects Studio's hover-outline thickness preference.

### Property: DraggerService.JointsEnabled

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
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

When `true`, parts that come to rest against other surfaces during a drag
are joined to them (for example, surface welds) when the drag finishes.
When `false`, dragging does not create joints.

### Property: DraggerService.LinearSnapEnabled

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
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

When `true`, moving an object with a dragger snaps its position to a grid
whose spacing is [DraggerService.LinearSnapIncrement](/docs/reference/engine/classes/DraggerService.md). When `false`,
movement is continuous and the increment has no effect.

### Property: DraggerService.LinearSnapIncrement

```json
{
  "type": "float",
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

The spacing, in studs, of the movement grid applied while
[DraggerService.LinearSnapEnabled](/docs/reference/engine/classes/DraggerService.md) is `true`; it has no effect when
linear snapping is disabled. The value is clamped to a small positive
minimum, so it can never be set to `0` or a negative number.

### Property: DraggerService.PartSnapEnabled

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

When `true`, dragging snaps the moved object to salient points (such as
edges and corners) on nearby parts, in addition to any grid snapping. When
`false`, part-to-part snapping is off.

### Property: DraggerService.PivotSnapToGeometry

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

When `true`, dragging an object's pivot snaps it to points on surrounding
geometry (for example vertices, edges, and face centers). When `false`,
the pivot moves freely.

### Property: DraggerService.ShowHover

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
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

When `true`, draggers draw a highlight over the object beneath the cursor
to indicate what a drag would affect. When `false`, no hover highlight is
shown and [DraggerService.AnimateHover](/docs/reference/engine/classes/DraggerService.md),
[DraggerService.HoverThickness](/docs/reference/engine/classes/DraggerService.md), and
[DraggerService.HoverAnimateFrequency](/docs/reference/engine/classes/DraggerService.md) have no visible effect.

### Property: DraggerService.ShowPivotIndicator

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
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

When `true`, the pivot indicator (the marker showing an object's pivot
point) is shown while dragging. Defaults to `false`.

### Property: DraggerService.UseBoundingBoxes

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

When `true`, the dragging tools use the axis-aligned bounding box of an
object for snapping instead of its precise geometric shape. This can
simplify placement when objects have complex geometry. The setting
corresponds to Studio's "Use Bounding Boxes" option in the
dragger-settings ribbon dropdown. Defaults to `false`.

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