---
name: Bone
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Attachment
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Bones are non-rendered objects that drive the movement of one or more parts for the purposes of animation, or creating clothing and characters."
---

# Class: Bone

> Bones are non-rendered objects that drive the movement of one or more parts
> for the purposes of animation, or creating clothing and characters.

## Description

Bones are non-rendered objects that drive the movement of one or more parts
for the purposes of animation, or creating clothing and characters. Bones are
part of a [Model](/docs/reference/engine/classes/Model.md) or [MeshPart](/docs/reference/engine/classes/MeshPart.md) object's skeletal **rig** that you
typically access and animate through the
[Animation Editor](/docs/en-us/animation/editor.md).

Rigs are created during the modeling process in third-party software such as
Blender or Maya. After importing the rigged model into Studio, you can add the
model directly to your experience, or save and share the model as an asset.
See [Rigging](/docs/en-us/art/modeling/rigging.md) for more details on creating
and using rigged models.

Note that you can parent [Bones](/docs/reference/engine/classes/Bone.md) under other [Bones](/docs/reference/engine/classes/Bone.md) and
parts. When parenting a bone to another bone, the child bone's world position
will be relative to the parent bone's position, and the hierarchy of parented
[Bone](/docs/reference/engine/classes/Bone.md) objects can change the behavior of affected parts during posing
or animation.

##### Relationship with Motor6D

To support animations with older rigs using joints, such as [Motor6D](/docs/reference/engine/classes/Motor6D.md),
you can use the [Bone.Transform](/docs/reference/engine/classes/Bone.md) property in the same way as
[Motor6D.Transform](/docs/reference/engine/classes/Motor6D.md). Roblox uses the offset of the bones from the
default pose to drive an animation, and bones are not replicated or
serialized.

##### Bone.CFrame

Bones inherit the [CFrame](/docs/reference/engine/classes/Attachment.md) property of
[Attachments](/docs/reference/engine/classes/Attachment.md) which Roblox uses as the bone's reference
position. The inherited [WorldCFrame](/docs/reference/engine/classes/Attachment.md) and other
world properties return the initial un-transformed position.

## Properties

### Property: Bone.Transform

```json
{
  "type": "CFrame",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Transform",
  "capabilities": [
    "Basic",
    "Animation"
  ]
}
```

**Transform** determines the current animated offset of the bone relative
to its [CFrame](/docs/reference/engine/classes/Attachment.md). This property is set by Roblox
when animations on skinned meshes are played, although it can be
manipulated manually in a manner similar to [Motor6D.Transform](/docs/reference/engine/classes/Motor6D.md).

See also:

- [Motor6D.Transform](/docs/reference/engine/classes/Motor6D.md), a property which plays a similar role in
  character rig animation
- [TransformedCFrame](/docs/reference/engine/classes/Bone.md) and
  [TransformedWorldCFrame](/docs/reference/engine/classes/Bone.md), whose values
  are partially determined by this property

### Property: Bone.TransformedWorldCFrame

```json
{
  "type": "CFrame",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "Unsafe",
  "category": "Derived World Data",
  "capabilities": [
    "Basic",
    "Animation"
  ]
}
```

**TransformedWorldCFrame** describes the combined
[CFrame](/docs/reference/engine/classes/Attachment.md) offset of the bone and the current
animation offset ([Transform](/docs/reference/engine/classes/Bone.md)) in world space.

See also:

- [Transform](/docs/reference/engine/classes/Bone.md), a property which partially determines
  this property's value
- [Bone.TransformedCFrame](/docs/reference/engine/classes/Bone.md), a local-space variant of this property

### Property: Bone.TransformedCFrame *(hidden)*

```json
{
  "type": "CFrame",
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
  "category": "Derived Data",
  "capabilities": [
    "Basic",
    "Animation"
  ]
}
```

**TransformedCFrame** describes the combined
[CFrame](/docs/reference/engine/classes/Attachment.md) offset of the bone and the current
animation offset ([Transform](/docs/reference/engine/classes/Bone.md)) in the bone's local
space.

See also:

- [Transform](/docs/reference/engine/classes/Bone.md), a property which partially determines
  this property's value
- [Bone.TransformedWorldCFrame](/docs/reference/engine/classes/Bone.md), a world-space variant of this
  property

## Inherited Members

### From [Attachment](/docs/reference/engine/classes/Attachment.md)

- **Property `Axis`** (`Vector3`): Direction of the **X** axis of the attachment, represented as a unit
- **Property `CFrame`** (`CFrame`): CFrame offset of the attachment.
- **Property `Orientation`** (`Vector3`): Orientation of the attachment relative to the orientation of its parent. *(hidden)*
- **Property `Position`** (`Vector3`): Positional offset of the attachment, relative to the position and *(hidden)*
- **Property `Rotation`** (`Vector3`): Rotation of the attachment relative to the rotation of its parent. *(deprecated, hidden)*
- **Property `SecondaryAxis`** (`Vector3`): Direction of the **Y** axis of the attachment, represented as a unit
- **Property `Visible`** (`boolean`): Toggles the in-experience visibility of the attachment.
- **Property `WorldAxis`** (`Vector3`): Direction of the **X** axis of the attachment relative to the world,
- **Property `WorldCFrame`** (`CFrame`): The exact CFrame of the attachment in world space coordinates.
- **Property `WorldOrientation`** (`Vector3`): Orientation of the attachment relative to the world rather than its own *(hidden)*
- **Property `WorldPosition`** (`Vector3`): Position of the attachment relative to the world rather than its own *(hidden)*
- **Property `WorldRotation`** (`Vector3`): Rotation of the attachment relative to the world rather than its own *(deprecated, hidden)*
- **Property `WorldSecondaryAxis`** (`Vector3`): Direction of the **Y** axis of the attachment relative to the world,
- **Method `GetAxis(): Vector3`**: Returns the value of the attachment's Axis. *(deprecated)*
- **Method `GetConstraints(): List<Constraint>`**: Returns a list of Constraints connected to the
- **Method `GetSecondaryAxis(): Vector3`**: Returns the value of the attachment's *(deprecated)*
- **Method `SetAxis(axis: Vector3): ()`**: Sets the value of the attachment's Axis. *(deprecated)*
- **Method `SetSecondaryAxis(axis: Vector3): ()`**: Sets the value of the attachment's *(deprecated)*

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