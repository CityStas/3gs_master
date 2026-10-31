---
name: FileMesh
last_updated: 2026-10-30T19:55:52Z
inherits:
  - DataModelMesh
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "The FileMesh object applies a mesh to a BasePart when parented to it. Its properties are inherited by the SpecialMesh object."
---

# Class: FileMesh

> The FileMesh object applies a mesh to a [BasePart](/docs/reference/engine/classes/BasePart.md) when parented to it.
> Its properties are inherited by the [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) object.

## Description

The FileMesh object applies a textured mesh to a [BasePart](/docs/reference/engine/classes/BasePart.md) when
parented to it. Its properties are inherited by the [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md)
object.

## What is a FileMesh?

FileMeshes allow user uploaded meshes to be applied to a [BasePart](/docs/reference/engine/classes/BasePart.md). The
mesh that is applied is dependent on the [FileMesh.MeshId](/docs/reference/engine/classes/FileMesh.md) property. A
texture can also be applied to this mesh using [FileMesh.TextureId](/docs/reference/engine/classes/FileMesh.md).

Although it is not an abstract class, and can be used by developers, all
[FileMesh](/docs/reference/engine/classes/FileMesh.md) properties are inherited by the [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) object. A
[SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) behaves identically to the FileMesh object when its
[SpecialMesh.MeshType](/docs/reference/engine/classes/SpecialMesh.md) is set to 'FileMesh'. Although both objects are
functional, the [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) object is the official supported class.

For more information on using meshes, please see the [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) page.

## Code Samples

**FileMesh Offset and Scale**

In this code sample a `BasePart` is instanced with a `FileMesh`. The
[DataModelMesh.Scale](/docs/reference/engine/classes/DataModelMesh.md) and [DataModelMesh.Offset](/docs/reference/engine/classes/DataModelMesh.md) properties of the
`FileMesh` are then animated using `TweenService`.

```lua
local TweenService = game:GetService("TweenService")

local part = Instance.new("Part")
part.Size = Vector3.new(4, 8, 4)
part.Position = Vector3.new(0, 4, 0)
part.Anchored = true
part.CanCollide = false

local mesh = Instance.new("FileMesh") -- advised to use SpecialMesh instead
mesh.MeshId = "rbxassetid://1086413449"
mesh.TextureId = "rbxassetid://1461576423"
mesh.Offset = Vector3.new(0, 0, 0)
mesh.Scale = Vector3.new(4, 4, 4)
mesh.Parent = part

local box = Instance.new("SelectionBox")
box.Adornee = part
box.Parent = part

part.Parent = workspace

local tween = TweenService:Create(
	mesh,
	TweenInfo.new(1, Enum.EasingStyle.Linear, Enum.EasingDirection.Out, -1, true, 0),
	{ Scale = Vector3.new(1, 1, 1), Offset = Vector3.new(0, 3, 0) }
)

tween:Play()
```

## Properties

### Property: FileMesh.MeshContent

```json
{
  "type": "Content",
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

The mesh content applied to the parent [BasePart](/docs/reference/engine/classes/BasePart.md). This property
accepts [Content](/docs/reference/engine/datatypes/Content.md) values including
[asset URIs](/docs/en-us/projects/assets.md#asset-uris) and
[EditableMesh](/docs/reference/engine/classes/EditableMesh.md) objects.

MeshContent is the underlying storage for [FileMesh.MeshId](/docs/reference/engine/classes/FileMesh.md). Setting
[FileMesh.MeshId](/docs/reference/engine/classes/FileMesh.md) writes through to this property, and reading
[FileMesh.MeshId](/docs/reference/engine/classes/FileMesh.md) derives its value from this property. When
MeshContent is set to [Content.none](/docs/reference/engine/datatypes/Content.md), no mesh is displayed.

This property is inherited by [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md).

### Property: FileMesh.MeshId

```json
{
  "type": "ContentId",
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

The MeshId is the content ID of the mesh that is to be displayed.

The content ID for a mesh is generated when a developer uploads a mesh to
Roblox.

**Mesh VertexColor**

In this code sample a `BasePart` is instanced with a `SpecialMesh`. The
[DataModelMesh.VertexColor](/docs/reference/engine/classes/DataModelMesh.md) property of the `SpecialMesh` is then
animated using `TweenService`.

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
mesh.VertexColor = Vector3.new(1, 1, 1)
mesh.Parent = part

-- parent part to workspace
part.Parent = workspace

-- create tweens
local tweenInfo = TweenInfo.new(1, Enum.EasingStyle.Linear, Enum.EasingDirection.Out)
local blackTween = TweenService:Create(mesh, tweenInfo, { VertexColor = Vector3.new(0, 0, 0) })
local redTween = TweenService:Create(mesh, tweenInfo, { VertexColor = Vector3.new(1, 0, 0) })
local greenTween = TweenService:Create(mesh, tweenInfo, { VertexColor = Vector3.new(0, 1, 0) })
local blueTween = TweenService:Create(mesh, tweenInfo, { VertexColor = Vector3.new(0, 0, 1) })
local resetTween = TweenService:Create(mesh, tweenInfo, { VertexColor = Vector3.new(1, 1, 1) })

-- animate
while true do
	blackTween:Play()
	blackTween.Completed:Wait()
	redTween:Play()
	redTween.Completed:Wait()
	greenTween:Play()
	greenTween.Completed:Wait()
	blueTween:Play()
	blueTween.Completed:Wait()
	resetTween:Play()
	resetTween.Completed:Wait()
	task.wait()
end
```

### Property: FileMesh.TextureContent

```json
{
  "type": "Content",
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

The texture content applied to the mesh. This property accepts
[Content](/docs/reference/engine/datatypes/Content.md) values including
[asset URIs](/docs/en-us/projects/assets.md#asset-uris) and
[EditableImage](/docs/reference/engine/classes/EditableImage.md) objects.

TextureContent is the underlying storage for [FileMesh.TextureId](/docs/reference/engine/classes/FileMesh.md).
Setting [FileMesh.TextureId](/docs/reference/engine/classes/FileMesh.md) writes through to this property, and
reading [FileMesh.TextureId](/docs/reference/engine/classes/FileMesh.md) derives its value from this property.
When TextureContent is set to [Content.none](/docs/reference/engine/datatypes/Content.md), no texture is
applied to the mesh.

When TextureContent references an [EditableImage](/docs/reference/engine/classes/EditableImage.md), the texture
live-updates with any edits to that object.

This property is inherited by [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md).

### Property: FileMesh.TextureId

```json
{
  "type": "ContentId",
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

The TextureId is the content ID of the image that is to be applied to used
for the meshes texture. When the TextureId property is set to an empty
string, no texture will be applied to the mesh.

#### How can I change the texture of a mesh?

Using the TextureId property, the texture of a mesh can be changed without
having to reupload the mesh. To do this, a new image will need to be
uploaded to Roblox with the desired texture. The original texture image
file can be obtained by exporting the mesh using the 'Export Selection'
option in Roblox Studio. The image file will be saved alongside the
exported .obj file.

The new texture can then be re-uploaded to Roblox as a Decal and its
content ID can be applied to the mesh using the TextureId property.

#### How can I make a textured mesh?

A mesh can only be textured if the mesh has been UV mapped. UV mapping
refers to the practice of projecting a texture map onto a mesh. This
cannot be done using Roblox Studio and has to be done using an external 3D
modelling application such as [Blender][1].

[1]: https://www.blender.org/

**Mesh VertexColor**

In this code sample a `BasePart` is instanced with a `SpecialMesh`. The
[DataModelMesh.VertexColor](/docs/reference/engine/classes/DataModelMesh.md) property of the `SpecialMesh` is then
animated using `TweenService`.

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
mesh.VertexColor = Vector3.new(1, 1, 1)
mesh.Parent = part

-- parent part to workspace
part.Parent = workspace

-- create tweens
local tweenInfo = TweenInfo.new(1, Enum.EasingStyle.Linear, Enum.EasingDirection.Out)
local blackTween = TweenService:Create(mesh, tweenInfo, { VertexColor = Vector3.new(0, 0, 0) })
local redTween = TweenService:Create(mesh, tweenInfo, { VertexColor = Vector3.new(1, 0, 0) })
local greenTween = TweenService:Create(mesh, tweenInfo, { VertexColor = Vector3.new(0, 1, 0) })
local blueTween = TweenService:Create(mesh, tweenInfo, { VertexColor = Vector3.new(0, 0, 1) })
local resetTween = TweenService:Create(mesh, tweenInfo, { VertexColor = Vector3.new(1, 1, 1) })

-- animate
while true do
	blackTween:Play()
	blackTween.Completed:Wait()
	redTween:Play()
	redTween.Completed:Wait()
	greenTween:Play()
	greenTween.Completed:Wait()
	blueTween:Play()
	blueTween.Completed:Wait()
	resetTween:Play()
	resetTween.Completed:Wait()
	task.wait()
end
```

## Inherited Members

### From [DataModelMesh](/docs/reference/engine/classes/DataModelMesh.md)

- **Property `Offset`** (`Vector3`): The Offset of a mesh determines the relative position from the
- **Property `Scale`** (`Vector3`): The Scale of a mesh determines the size of the mesh relative to its
- **Property `VertexColor`** (`Vector3`): Changes the hue of a mesh's texture, used with FileMesh.TextureId.

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