---
name: Dragger
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "A helper object used to create tools that can drag parts."
---

# Class: Dragger

> A helper object used to create tools that can drag parts.

## Description

The **Dragger** object is a helper object used to create tools that can drag
parts. It is expected (but not required) to be used with [Mouse](/docs/reference/engine/classes/Mouse.md) events.

Primarily used with the RbxStamper library.

## Methods

### Method: Dragger:AxisRotate

**Signature:** `Dragger:AxisRotate(axis?: Axis): ()`

Rotates the currently dragged part(s) by 90 degrees around the specified
world axis. This method can only be called while a drag is actively in
progress (after [Dragger:MouseDown()](/docs/reference/engine/classes/Dragger.md) has been called and
[Dragger:MouseMove()](/docs/reference/engine/classes/Dragger.md) has initiated movement). The `axis` parameter
defaults to [Axis.X](/docs/reference/engine/enums/Axis.md).

For single-part drags the rotation is performed about the snap face axis.
For multi-part drags the rotation is applied around the computed center of
the part group using a collision-aware routine that prevents overlap with
surrounding geometry.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `axis` | `Axis` | `X` | The [Axis](/docs/reference/engine/enums/Axis.md) (`X`, `Y`, or `Z`) around which to rotate. |

**Returns:** `()`

### Method: Dragger:MouseDown

**Signature:** `Dragger:MouseDown(mousePart: Instance, pointOnMousePart: Vector3, parts: Instances): ()`

Initializes a dragging action by registering the parts to drag and the
point on the mouse part where the interaction began. This method does not
immediately begin moving parts; actual movement starts on a subsequent
[Dragger:MouseMove()](/docs/reference/engine/classes/Dragger.md) call once the mouse has moved beyond a
break-free threshold (half the current grid snap distance).

`mousePart` must be a [BasePart](/docs/reference/engine/classes/BasePart.md) that is both a member of `parts`
and a descendant of [Workspace](/docs/reference/engine/classes/Workspace.md). Calling this method while a drag is
already active (before [Dragger:MouseUp()](/docs/reference/engine/classes/Dragger.md)) throws an error. While a
drag is pending, camera mouse-pan is disabled so that mouse movement
applies to the drag instead of the viewport.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `mousePart` | `Instance` |  | The [BasePart](/docs/reference/engine/classes/BasePart.md) under the mouse that serves as the drag handle. Must be a member of `parts` and must be in the [Workspace](/docs/reference/engine/classes/Workspace.md). |
| `pointOnMousePart` | `Vector3` |  | A [Vector3](/docs/reference/engine/datatypes/Vector3.md) in the local coordinate space of `mousePart` indicating where the mouse initially contacted the part. |
| `parts` | `Instances` |  | An array of [BaseParts](/docs/reference/engine/classes/BasePart.md) to move together during the drag. Must include `mousePart` and contain at least one element. |

**Returns:** `()`

### Method: Dragger:MouseMove

**Signature:** `Dragger:MouseMove(mouseRay: Ray): ()`

Attempts to move the currently dragged parts to the location indicated by
`mouseRay`. Must be called after [Dragger:MouseDown()](/docs/reference/engine/classes/Dragger.md).

On the first call that detects sufficient mouse movement (exceeding half
the grid snap distance), the method transitions into active dragging: it
un-joins the dragged parts from surrounding geometry, aligns them to the
grid, and begins tracking movement. On each subsequent call, the ray is
cast against other parts in the [Workspace](/docs/reference/engine/classes/Workspace.md) (or against the world
ground plane at Y = 0 if nothing is hit), and the dragged parts are moved
toward that snap point using a collision-aware algorithm that prevents
them from overlapping existing geometry. Single-part drags use surface
snapping; multi-part drags use grid-aligned displacement with Y-drop
collision avoidance.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `mouseRay` | `Ray` |  | A [Ray](/docs/reference/engine/datatypes/Ray.md) representing the current mouse position in world space (origin at the camera, direction toward the pointer). |

**Returns:** `()`

### Method: Dragger:MouseUp

**Signature:** `Dragger:MouseUp(): ()`

Stops the current dragging action initiated by
[Dragger:MouseDown()](/docs/reference/engine/classes/Dragger.md). If parts were actively being dragged, this
method re-joins them to adjacent geometry and finalizes their position. If
`MouseDown` was called but the mouse never moved far enough to begin
actual dragging, the state is simply reset. In both cases camera mouse-pan
is re-enabled.

Calling this method without a prior [Dragger:MouseDown()](/docs/reference/engine/classes/Dragger.md) throws an
error.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Returns:** `()`

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