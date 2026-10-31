---
name: AccessoryDescription
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Describes the appearance of an Accessory for the HumanoidDescription."
---

# Class: AccessoryDescription

> Describes the appearance of an [Accessory](/docs/reference/engine/classes/Accessory.md) for the
> [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).

## Description

**AccessoryDescription** is an object that stores the description for an
[Accessory](/docs/reference/engine/classes/Accessory.md). It is meant to be placed underneath a
[HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) in order to work with
[Humanoid:ApplyDescriptionAsync()](/docs/reference/engine/classes/Humanoid.md).

## Properties

### Property: AccessoryDescription.AccessoryType

```json
{
  "type": "AccessoryType",
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
    "AvatarAppearance"
  ]
}
```

The [AccessoryType](/docs/reference/engine/enums/AccessoryType.md) of the [Accessory](/docs/reference/engine/classes/Accessory.md) referred to by this
description.

### Property: AccessoryDescription.AssetId

```json
{
  "type": "int64",
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
    "AvatarAppearance"
  ]
}
```

The asset ID that should be applied when applying this
[AccessoryDescription](/docs/reference/engine/classes/AccessoryDescription.md).

### Property: AccessoryDescription.Instance

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
    "AvatarAppearance"
  ]
}
```

A reference to the [Instance](/docs/reference/engine/classes/Instance.md) that should be applied when applying
this [AccessoryDescription](/docs/reference/engine/classes/AccessoryDescription.md). This property can be used instead of
[AssetId](/docs/reference/engine/classes/AccessoryDescription.md) to apply accessories without
uploading them to the platform.

### Property: AccessoryDescription.IsLayered

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
    "AvatarAppearance"
  ]
}
```

Whether the [Accessory](/docs/reference/engine/classes/Accessory.md) is layered or rigid. This is intended to be
read-only. It will be corrected after calling
[Humanoid:ApplyDescriptionAsync()](/docs/reference/engine/classes/Humanoid.md) if this property doesn't match
the actual [Accessory](/docs/reference/engine/classes/Accessory.md) contents.

### Property: AccessoryDescription.Order

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
    "AvatarAppearance"
  ]
}
```

The [WrapLayer.Order](/docs/reference/engine/classes/WrapLayer.md) value when applying the [Accessory](/docs/reference/engine/classes/Accessory.md), if
it is layered.

### Property: AccessoryDescription.Position

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
    "AvatarAppearance"
  ]
}
```

The accessory adjustment position offset. Only applies if the
[Accessory](/docs/reference/engine/classes/Accessory.md) is rigid.

### Property: AccessoryDescription.Rotation

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
    "AvatarAppearance"
  ]
}
```

The accessory adjustment rotation offset. Only applies if the
[Accessory](/docs/reference/engine/classes/Accessory.md) is rigid.

### Property: AccessoryDescription.Scale

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
    "AvatarAppearance"
  ]
}
```

The accessory adjustment scale. Only applies if the [Accessory](/docs/reference/engine/classes/Accessory.md) is
rigid.

### Property: AccessoryDescription.Puffiness

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

The [WrapLayer.Puffiness](/docs/reference/engine/classes/WrapLayer.md) value when applying the [Accessory](/docs/reference/engine/classes/Accessory.md),
if it is layered.

## Methods

### Method: AccessoryDescription:GetAppliedInstance

**Signature:** `AccessoryDescription:GetAppliedInstance(): Instance`

Returns the applied [Accessory](/docs/reference/engine/classes/Accessory.md) if this [AccessoryDescription](/docs/reference/engine/classes/AccessoryDescription.md)
is the child of an applied [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) parented to a
[Humanoid](/docs/reference/engine/classes/Humanoid.md). Throws an error if this [AccessoryDescription](/docs/reference/engine/classes/AccessoryDescription.md) is
not a child of a [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) that has been applied to a
[Humanoid](/docs/reference/engine/classes/Humanoid.md), or if no matching applied instance is found.

*Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance*

**Returns:** `Instance` — The applied [Accessory](/docs/reference/engine/classes/Accessory.md).

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