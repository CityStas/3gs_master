---
name: DataModelMesh
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotBrowsable
summary: "The DataModelMesh is an abstract class from which mesh classes descend."
---

# Class: DataModelMesh

> The DataModelMesh is an abstract class from which mesh classes descend.

## Description

The DataModelMesh is an abstract class from which mesh classes descend.

Mesh classes are objects that, when parented to [BaseParts](/docs/reference/engine/classes/BasePart.md)
alter the appearance of the part to that of a predefined mesh. Note, they only
alter the appearance of the part and not the physics/collision boundaries of
the part. Developers looking to apply a mesh to a part that alters the part's
collision should use [MeshParts](/docs/reference/engine/classes/MeshPart.md).

Note the [MeshPart](/docs/reference/engine/classes/MeshPart.md) and [CharacterMesh](/docs/reference/engine/classes/CharacterMesh.md) classes do not descend
from DataModelMesh.

## Properties

### Property: DataModelMesh.Offset

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
  "category": "Data"
}
```

The Offset of a mesh determines the distance from the
[BasePart.Position](/docs/reference/engine/classes/BasePart.md) of a [BasePart](/docs/reference/engine/classes/BasePart.md) that the mesh will be
displayed.

#### How to use mesh offset

The Offset property changes the relative position the mesh will be
rendered at. For example, an offset of 0, 5, 0 will cause the mesh to be
displayed 5 studs above the position of the [BasePart](/docs/reference/engine/classes/BasePart.md).

The position of the [BasePart](/docs/reference/engine/classes/BasePart.md) remains unchanged, meaning the
physics collision box of the part will remain in the same location. This
is demonstrated in the image below where the green outline (a
[SelectionBox](/docs/reference/engine/classes/SelectionBox.md)) shows the extents of the [BasePart](/docs/reference/engine/classes/BasePart.md).

#### Other uses for mesh offset

There are a number of interesting uses for the mesh offset property.

- Offset and [DataModelMesh.Scale](/docs/reference/engine/classes/DataModelMesh.md) can be animated using
  [TweenService](/docs/reference/engine/classes/TweenService.md) relatively inexpensively as the engine does not
  need to make any physics/collision calculations as the [BasePart](/docs/reference/engine/classes/BasePart.md)
  is not moved.
- Changing the relationship between the mesh and its collision extents
  (determined by the [BasePart](/docs/reference/engine/classes/BasePart.md))

**Mesh Offset and Scale**

In this code sample a `BasePart` is instanced with a `SpecialMesh`. The
[DataModelMesh.Scale](/docs/reference/engine/classes/DataModelMesh.md) and [DataModelMesh.Offset](/docs/reference/engine/classes/DataModelMesh.md) properties of the
`SpecialMesh` are then animated using `TweenService`.

```lua
local TweenService = game:GetService("TweenService")

-- instance a part and a mesh
local part = Instance.new("Part")
part.Size = Vector3.new(4, 8, 4)
part.Position = Vector3.new(0, 4, 0)
part.Anchored = true
part.CanCollide = false

local mesh = Instance.new("SpecialMesh")
mesh.MeshType = Enum.MeshType.FileMesh
mesh.MeshId = "rbxassetid://1086413449"
mesh.TextureId = "rbxassetid://1461576423"
mesh.Offset = Vector3.new(0, 0, 0)
mesh.Scale = Vector3.new(4, 4, 4)
mesh.Parent = part

-- selection box to show part extents
local box = Instance.new("SelectionBox")
box.Adornee = part
box.Parent = part

-- parent part to workspace
part.Parent = workspace

-- animate offset and scale with a tween
local tween = TweenService:Create(
	mesh,
	TweenInfo.new(1, Enum.EasingStyle.Linear, Enum.EasingDirection.Out, -1, true, 0),
	{ Scale = Vector3.new(1, 1, 1), Offset = Vector3.new(0, 3, 0) }
)

tween:Play()
```

### Property: DataModelMesh.Scale

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
  "category": "Data"
}
```

The Scale of a mesh determines the size of the mesh relative to its
original dimensions.

#### How to use mesh scale

The scale property works slightly differently depending on the type of
mesh being used. Note the size of the [BasePart](/docs/reference/engine/classes/BasePart.md) remains unchanged,
meaning the physics collision box of the part will remain the same.

- [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) objects with [SpecialMesh.FileType](/docs/reference/engine/classes/SpecialMesh.md) set to
  'FileMesh' scale relative to the original dimensions of the mesh when it
  was uploaded to Roblox
- [BlockMesh](/docs/reference/engine/classes/BlockMesh.md) objects or [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) objects with
  [SpecialMesh.FileType](/docs/reference/engine/classes/SpecialMesh.md) set to 'Brick', 'Wedge' or 'Sphere' scale
  uniformly relative to the [BasePart.Size](/docs/reference/engine/classes/BasePart.md) of their parent
- [CylinderMesh](/docs/reference/engine/classes/CylinderMesh.md) objects or [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) objects with
  [SpecialMesh.FileType](/docs/reference/engine/classes/SpecialMesh.md) set to 'Cylinder' scale relative to the
  [BasePart.Size](/docs/reference/engine/classes/BasePart.md) of their parent. Uniformly for the cylinders
  height axis and maintaining a 1:1 ratio for the length and width of the
  cylinder, using the lowest value.
- [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) objects with [SpecialMesh.FileType](/docs/reference/engine/classes/SpecialMesh.md) set to
  'Head' currently scale in a non standard manner. Developers should not
  rely on this as there are plans to change this behavior.
- [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) objects with [SpecialMesh.FileType](/docs/reference/engine/classes/SpecialMesh.md) set to
  'Torso' scale in a non standard manner. Developers should not rely on
  this as there are plans to deprecate this mesh type.

#### Mesh scale demonstration

The above behavior can be seen in the following demonstration images.

Linear scaling relative to part size for 'Brick', 'Wedge' and 'Sphere'
meshes.

Linear scaling relative to original uploaded mesh for 'FileMesh' meshes

Non-uniform constrained scaling for 'Cylinder' meshes

#### Other uses for mesh scale

There are a number of interesting uses for the mesh offset property.

- [DataModelMesh.Offset](/docs/reference/engine/classes/DataModelMesh.md) and Scale can be animated using
  [TweenService](/docs/reference/engine/classes/TweenService.md) relatively inexpensively as the engine does not
  need to make any physics/collision calculations as the [BasePart](/docs/reference/engine/classes/BasePart.md)
  is not changed.
- Changing the relationship between the mesh and its collision extents
  (determined by the [BasePart](/docs/reference/engine/classes/BasePart.md))

**Mesh Offset and Scale**

In this code sample a `BasePart` is instanced with a `SpecialMesh`. The
[DataModelMesh.Scale](/docs/reference/engine/classes/DataModelMesh.md) and [DataModelMesh.Offset](/docs/reference/engine/classes/DataModelMesh.md) properties of the
`SpecialMesh` are then animated using `TweenService`.

```lua
local TweenService = game:GetService("TweenService")

-- instance a part and a mesh
local part = Instance.new("Part")
part.Size = Vector3.new(4, 8, 4)
part.Position = Vector3.new(0, 4, 0)
part.Anchored = true
part.CanCollide = false

local mesh = Instance.new("SpecialMesh")
mesh.MeshType = Enum.MeshType.FileMesh
mesh.MeshId = "rbxassetid://1086413449"
mesh.TextureId = "rbxassetid://1461576423"
mesh.Offset = Vector3.new(0, 0, 0)
mesh.Scale = Vector3.new(4, 4, 4)
mesh.Parent = part

-- selection box to show part extents
local box = Instance.new("SelectionBox")
box.Adornee = part
box.Parent = part

-- parent part to workspace
part.Parent = workspace

-- animate offset and scale with a tween
local tween = TweenService:Create(
	mesh,
	TweenInfo.new(1, Enum.EasingStyle.Linear, Enum.EasingDirection.Out, -1, true, 0),
	{ Scale = Vector3.new(1, 1, 1), Offset = Vector3.new(0, 3, 0) }
)

tween:Play()
```

### Property: DataModelMesh.VertexColor

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
  "category": "Data"
}
```

**VertexColor** determines the hue change of the
[Texture](/docs/reference/engine/classes/FileMesh.md) of a [FileMesh](/docs/reference/engine/classes/FileMesh.md). Note that this
property is a [Vector3](/docs/reference/engine/datatypes/Vector3.md) rather than a [Color3](/docs/reference/engine/datatypes/Color3.md); to
convert, use the [Color3.R](/docs/reference/engine/datatypes/Color3.md), [Color3.G](/docs/reference/engine/datatypes/Color3.md), and
[Color3.B](/docs/reference/engine/datatypes/Color3.md) properties.

Although this property allows basic modification of a texture, changing a
texture entirely provides more control. See [MeshPart](/docs/reference/engine/classes/MeshPart.md) for more
details.

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