---
name: BodyPartDescription
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Describes the appearance of an avatar body part for the HumanoidDescription."
---

# Class: BodyPartDescription

> Describes the appearance of an avatar body part for the
> [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).

## Description

**BodyPartDescription** is an object that stores the description for an
avatar's body parts, such as the [Color](/docs/reference/engine/classes/BodyPartDescription.md). It
is meant to be placed underneath a [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) in order to
work with [Humanoid:ApplyDescriptionAsync()](/docs/reference/engine/classes/Humanoid.md).

## Properties

### Property: BodyPartDescription.AssetId

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
[BodyPartDescription](/docs/reference/engine/classes/BodyPartDescription.md).

### Property: BodyPartDescription.BodyPart

```json
{
  "type": "BodyPart",
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

The type of body part.

### Property: BodyPartDescription.Color

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
    "AvatarAppearance"
  ]
}
```

The [Color3](/docs/reference/engine/datatypes/Color3.md) for this body part.

### Property: BodyPartDescription.HeadShape

```json
{
  "type": "string",
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

**HeadShape** specifies a Classic Head shape identifier to apply to a
compatible Dynamic Head. This property is only relevant when
[BodyPart](/docs/reference/engine/classes/BodyPartDescription.md) is set to
[Head](/docs/reference/engine/enums/BodyPart.md) and [AssetId](/docs/reference/engine/classes/BodyPartDescription.md)
references a Dynamic Head that supports head shapes.

#### Example

```lua
local AvatarEditorService = game:GetService("AvatarEditorService")

-- Get available head shapes for the user
local headShapes = AvatarEditorService:GetHeadShapesAsync(userId)

-- Create a BodyPartDescription for a Dynamic Head with a Classic shape
local bodyPartDescription = Instance.new("BodyPartDescription")
bodyPartDescription.BodyPart = Enum.BodyPart.Head
bodyPartDescription.AssetId = dynamicHeadAssetId
bodyPartDescription.HeadShape = headShapes[1] -- Apply the first owned head shape
bodyPartDescription.Parent = humanoidDescription

-- Apply the description
humanoid:ApplyDescriptionAsync(humanoidDescription)
```

See also:

- [AvatarEditorService:GetHeadShapesAsync()](/docs/reference/engine/classes/AvatarEditorService.md), which returns head
  shape identifiers that can be used with this property
- [AssetId](/docs/reference/engine/classes/BodyPartDescription.md), which specifies the Dynamic
  Head asset to apply the shape to
- [BodyPart](/docs/reference/engine/classes/BodyPartDescription.md), which must be set to
  [Head](/docs/reference/engine/enums/BodyPart.md) for this property to have effect
- [Humanoid:ApplyDescriptionAsync()](/docs/reference/engine/classes/Humanoid.md), which applies the description
  containing this [BodyPartDescription](/docs/reference/engine/classes/BodyPartDescription.md)

### Property: BodyPartDescription.Instance

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
this [BodyPartDescription](/docs/reference/engine/classes/BodyPartDescription.md). This property can be used instead of
[AssetId](/docs/reference/engine/classes/BodyPartDescription.md) to apply accessories without
uploading them to the platform. This can reference either a body part with
R15, **R15ArtistIntent** and **R6** folders, or only reference a single
subfolder.

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