---
name: PackageLink
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotBrowsable
summary: "Links a DataModel instance to a corresponding asset in the cloud."
---

# Class: PackageLink

> Links a [DataModel](/docs/reference/engine/classes/DataModel.md) instance to a corresponding asset in the cloud.

## Description

The purpose of the [PackageLink](/docs/reference/engine/classes/PackageLink.md) object is to link a [DataModel](/docs/reference/engine/classes/DataModel.md)
instance to a corresponding asset in the cloud. This improves flows for
collaboration, version control, and sharing for models. The
[PackageLink](/docs/reference/engine/classes/PackageLink.md) instance will be a child of the root of the entire package
hierarchy.

[PackageLinks](/docs/reference/engine/classes/PackageLink.md) are not creatable through
[Scripts](/docs/reference/engine/classes/Script.md). They can only be added through interaction with Studio
and can only be parented to [Instances](/docs/reference/engine/classes/Instance.md) that can be published
independently of [DataModel](/docs/reference/engine/classes/DataModel.md) publish. The [PackageLink](/docs/reference/engine/classes/PackageLink.md) instance
will always be the first child shown in the tree view, regardless of sorting.

## Properties

### Property: PackageLink.AutoUpdate

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Link",
  "capabilities": [
    "AssetRead"
  ]
}
```

When this property is set to true, the package associated with the given
[PackageLink](/docs/reference/engine/classes/PackageLink.md) will be automatically updated to the latest version.
By default, this property is false upon creation of a package.

This property lets you decide if a given package should be automatically
updated to the latest version when entering a given place. The game
periodically checks for new updates while a place is open.

This property is visible and configurable in the Properties window in
Studio.

### Property: PackageLink.Creator

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
  "category": "Data",
  "capabilities": [
    "AssetRead"
  ]
}
```

The creator of the package asset.

### Property: PackageLink.DefaultName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "NotAccessibleSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Link",
  "capabilities": [
    "AssetRead"
  ]
}
```

Managed by the engine and not writable from scripts. Stores the name of
the package's root instance as recorded when the package was last
published or synced. It defaults to an empty string and is populated from
the base root node's name.

This value is the as-published baseline the engine compares against the
current instance name to detect local name customizations and preserve
them during a three-way merge when the package is updated.

### Property: PackageLink.PackageAssetName

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
  "category": "Data",
  "capabilities": [
    "AssetRead"
  ]
}
```

The asset name of the package.

### Property: PackageLink.PackageContent

```json
{
  "type": "Content",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Link",
  "capabilities": [
    "AssetRead"
  ]
}
```

A read-only [Content](/docs/reference/engine/datatypes/Content.md) that references the package's model asset.
The value is the same asset that [PackageLink.PackageId](/docs/reference/engine/classes/PackageLink.md) points to,
expressed as a [Content](/docs/reference/engine/datatypes/Content.md) URL rather than a `ContentId` string.
This property cannot be written from a [Script](/docs/reference/engine/classes/Script.md).

### Property: PackageLink.PackageId

```json
{
  "type": "ContentId",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Link",
  "capabilities": [
    "AssetRead"
  ]
}
```

The ID of the asset this package corresponds to.

### Property: PackageLink.PermissionLevel

```json
{
  "type": "PackagePermission",
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
  "category": "Data",
  "capabilities": [
    "AssetRead"
  ]
}
```

The package permission for the current Studio user.

### Property: PackageLink.SerializedDefaultAttributes

```json
{
  "type": "BinaryString",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "NotAccessibleSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Link",
  "capabilities": [
    "AssetRead"
  ]
}
```

Managed by the engine and not writable from scripts. Stores a serialized
(binary) snapshot of the attributes on the package's root instance as
recorded when the package was last published or synced. It defaults to an
empty value and is populated from the base root node's serialized
attributes.

This snapshot is the as-published baseline for a three-way merge: the
engine compares the root instance's current attributes against it to
preserve local customizations when the package is updated.

### Property: PackageLink.Status

```json
{
  "type": "string",
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
  "category": "Link",
  "capabilities": [
    "AssetRead"
  ]
}
```

The status of the package. It can be one of the following statuses: Up To
Date, Changed, New Version Available, Changed + New Version Available.

### Property: PackageLink.VersionNumber

```json
{
  "type": "int64",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "NotAccessibleSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Link",
  "capabilities": [
    "AssetRead"
  ]
}
```

This property refers to a revision of a specific package

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