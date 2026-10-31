---
name: LineHandleAdornment
last_updated: 2026-10-30T19:55:52Z
inherits:
  - HandleAdornment
  - PVAdornment
  - GuiBase3d
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "A line-shaped handle that can be adorned to a BasePart."
---

# Class: LineHandleAdornment

> A line-shaped handle that can be adorned to a [BasePart](/docs/reference/engine/classes/BasePart.md).

## Description

`LineHandleAdornment` is a line-shaped handle that can be adorned to a
[BasePart](/docs/reference/engine/classes/BasePart.md). This line starts at the center of the adornment's
[CFrame](/docs/reference/engine/classes/LineHandleAdornment.md) (offset by its
[SizeRelativeOffset](/docs/reference/engine/classes/LineHandleAdornment.md)) and is
oriented along its [CFrame](/docs/reference/engine/classes/LineHandleAdornment.md). If parented to a
player's [PlayerGui](/docs/reference/engine/classes/PlayerGui.md) or the [CoreGui](/docs/reference/engine/classes/CoreGui.md), handles can listen to input
events for purposes such as making dragger tools.

## Properties

### Property: LineHandleAdornment.Length

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

The length of the line in studs.

### Property: LineHandleAdornment.Thickness

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

The thickness of the line in pixels.

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