---
name: Highlight
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "A visual effect which you can use to call attention to a specific object within an experience."
---

# Class: Highlight

> A visual effect which you can use to call attention to a specific object
> within an experience.

## Description

The [Highlight](/docs/reference/engine/classes/Highlight.md) instance is a visual effect which you can use to call
attention to a specific object within an experience. Every highlight effect
has a silhouette **outline** that surrounds the object and a solid overlay
**interior** that displays over the object. You can customize both of these
components independently to modify the highlight's visual appearance.

| _Base object_ | _White outline, 50% red interior_ | _Yellow outline, black interior_ |
| --- | --- | --- |

Useful applications of the highlight effect include:

- Providing visual feedback that an object is important and/or interactable.
- Making distant objects visible through objects that are closer to the user.
- Indicating the current position and status of other characters.

#### Limitations

As a performance limit, Studio only displays 255 simultaneous
[Highlight](/docs/reference/engine/classes/Highlight.md) instances on the client at a time. If you exceed this limit,
the additional instances are silently ignored. Note that while a
[Highlight](/docs/reference/engine/classes/Highlight.md) with [Enabled](/docs/reference/engine/classes/Highlight.md) set to `false`
doesn't display, it still takes one of the 255 available slots, so if you plan
to permanently disable a [Highlight](/docs/reference/engine/classes/Highlight.md) instance, it's best to delete it
rather than disable it.

## Properties

### Property: Highlight.Adornee

```json
{
  "type": "Instance",
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

The [Instance](/docs/reference/engine/classes/Instance.md) for which to apply the [Highlight](/docs/reference/engine/classes/Highlight.md), used to
apply the effect to an [Instance](/docs/reference/engine/classes/Instance.md) outside of a child/parent
relationship.

### Property: Highlight.DepthMode

```json
{
  "type": "HighlightDepthMode",
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

Controls how the [Highlight](/docs/reference/engine/classes/Highlight.md) effect displays with respect to other
objects in the world. You can set this property to one of the following
options:

- [AlwaysOnTop](/docs/reference/engine/enums/HighlightDepthMode.md) — Allows the highlight
  to display regardless if there are objects between the camera and the
  highlighted object. This means the viewer is always able to see the
  highlight regardless of what is between the highlighted object and the
  camera.

- [Occluded](/docs/reference/engine/enums/HighlightDepthMode.md) — Hides the highlight if
  there are objects between the camera and the highlighted object. This
  means the viewer is only able to see the object if there are no
  obstructing objects between the highlighted object and the camera's
  view.

| _DepthMode = AlwaysOnTop_ | _DepthMode = Occluded_ |
| --- | --- |

### Property: Highlight.Enabled

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
    "Basic"
  ]
}
```

Sets whether or not the highlight is enabled. This does not impact
performance, but disabled [Highlight](/docs/reference/engine/classes/Highlight.md) instances will still take one
of the 255 available slots. If you plan to permanently disable a
[Highlight](/docs/reference/engine/classes/Highlight.md) instance, it's best to delete it rather than disable it.

### Property: Highlight.FillColor

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
    "Basic"
  ]
}
```

Sets the [Color3](/docs/reference/engine/datatypes/Color3.md) value of the highlight's interior.

| _FillColor = [255, 100, 50]_ | _FillColor = [0, 255, 125]_ | _FillColor = [75, 150, 255]_ |
| --- | --- | --- |

### Property: Highlight.FillTransparency

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
    "Basic"
  ]
}
```

Sets the visibility of the highlight's interior to any value between the
default value of **0** (opaque) and **1** (invisible). You can use this
property to determine how much of the object's existing color you want
viewers to see.

| _FillTransparency = 0_ | _FillTransparency = 0.5_ | _FillTransparency = 1_ |
| --- | --- | --- |

### Property: Highlight.OutlineColor

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
    "Basic"
  ]
}
```

Sets the [Color3](/docs/reference/engine/datatypes/Color3.md) value of the highlight's outline.

| _OutlineColor = [255, 100, 50]_ | _OutlineColor = [0, 255, 125]_ | _OutlineColor = [75, 150, 255]_ |
| --- | --- | --- |

### Property: Highlight.OutlineTransparency

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
    "Basic"
  ]
}
```

Sets the visibility of the highlight's outline to a value between **0**
(opaque) and **1** (transparent).

| _OutlineTransparency = 0_ | _OutlineTransparency = 1_ | |
| --- | --- | --- |

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