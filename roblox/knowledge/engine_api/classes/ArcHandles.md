---
name: ArcHandles
last_updated: 2026-10-30T19:55:51Z
inherits:
  - HandlesBase
  - PartAdornment
  - GuiBase3d
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "The ArcHandles object places 3D arc handles around any 3D object that its Adornee is set to."
---

# Class: ArcHandles

> The [ArcHandles](/docs/reference/engine/classes/ArcHandles.md) object places 3D arc handles around any 3D object that
> its [Adornee](/docs/reference/engine/classes/PartAdornment.md) is set to.

## Description

The **ArcHandles** object places 3D arc handles around any 3D object that its
[Adornee](/docs/reference/engine/classes/PartAdornment.md) is set to. For handles to be
interactive, it must be parented to a player's [PlayerGui](/docs/reference/engine/classes/PlayerGui.md) or the
[CoreGui](/docs/reference/engine/classes/CoreGui.md).

![ArcHandles example](../../../assets/engine-api/classes/ArcHandles/ArcHandles-Example.jpg)

## Properties

### Property: ArcHandles.Axes

```json
{
  "type": "Axes",
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
    "UI",
    "Input"
  ]
}
```

Sets the current Axes ArcHandles will show.

## Events

### Event: ArcHandles.MouseButton1Down

**Signature:** `ArcHandles.MouseButton1Down(axis: Axis)`

Fired when the left mouse button goes down on one of the GUI handles.

*Security: None · Capabilities: Basic, UI, Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `axis` | `Axis` | The [Axis](/docs/reference/engine/enums/Axis.md) (`X`, `Y`, or `Z`) of the arc handle on which the left mouse button was pressed. |

### Event: ArcHandles.MouseButton1Up

**Signature:** `ArcHandles.MouseButton1Up(axis: Axis)`

Fired when the left mouse button is released on one of the GUI handles.

*Security: None · Capabilities: Basic, UI, Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `axis` | `Axis` | The [Axis](/docs/reference/engine/enums/Axis.md) (`X`, `Y`, or `Z`) of the arc handle on which the left mouse button was released. |

### Event: ArcHandles.MouseDrag

**Signature:** `ArcHandles.MouseDrag(axis: Axis, relativeAngle: float, deltaRadius: float)`

Fired when the mouse moves while the MouseButton1Down event has fired, but
the left mouse button has not been released yet.

*Security: None · Capabilities: Basic, UI, Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `axis` | `Axis` | The [Axis](/docs/reference/engine/enums/Axis.md) (`X`, `Y`, or `Z`) of the arc handle being dragged. |
| `relativeAngle` | `float` | The angle, in radians, that the handle has rotated around its axis relative to the start of the drag. |
| `deltaRadius` | `float` | The change in radius (the cursor's distance from the handle's center) relative to the start of the drag. |

### Event: ArcHandles.MouseEnter

**Signature:** `ArcHandles.MouseEnter(axis: Axis)`

Fired when a mouse "enters" the GUI handle.

*Security: None · Capabilities: Basic, UI, Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `axis` | `Axis` | The [Axis](/docs/reference/engine/enums/Axis.md) (`X`, `Y`, or `Z`) of the arc handle the mouse entered. |

### Event: ArcHandles.MouseLeave

**Signature:** `ArcHandles.MouseLeave(axis: Axis)`

Fired when the mouse leaves the GUI handle.

*Security: None · Capabilities: Basic, UI, Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `axis` | `Axis` | The [Axis](/docs/reference/engine/enums/Axis.md) (`X`, `Y`, or `Z`) of the arc handle the mouse left. |

## Inherited Members

### From [PartAdornment](/docs/reference/engine/classes/PartAdornment.md)

- **Property `Adornee`** (`BasePart`): Sets the object to adorn to.

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