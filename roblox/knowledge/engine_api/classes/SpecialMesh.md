---
name: SpecialMesh
last_updated: 2026-10-30T19:55:53Z
inherits:
  - FileMesh
  - DataModelMesh
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "The SpecialMesh object applies a mesh to a BasePart depending on the MeshType property."
---

# Class: SpecialMesh

> The [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) object applies a mesh to a [BasePart](/docs/reference/engine/classes/BasePart.md) depending
> on the [MeshType](/docs/reference/engine/classes/SpecialMesh.md) property.

## Description

The [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) object applies a mesh to a [BasePart](/docs/reference/engine/classes/BasePart.md) depending
on the [MeshType](/docs/reference/engine/classes/SpecialMesh.md) property. A number of options are
available.

- **Brick** - A block shape, equivalent to a [BlockMesh](/docs/reference/engine/classes/BlockMesh.md)
- **Cylinder** - A cylinder, identical to a [Part](/docs/reference/engine/classes/Part.md) with a
  [Part.Shape](/docs/reference/engine/classes/Part.md) of 'Cylinder'
- **FileMesh** - A user uploaded Mesh, equivalent to [FileMesh](/docs/reference/engine/classes/FileMesh.md) that a
  texture can be applied to using the [FileMesh.TextureId](/docs/reference/engine/classes/FileMesh.md) property
- **Head** - A character head shape
- **Sphere** - A sphere shape, similar to a [Part](/docs/reference/engine/classes/Part.md) with a
  [Part.Shape](/docs/reference/engine/classes/Part.md) of 'Ball' but can be freely resized on all axis
- **Wedge** - A wedge shape, identical to a [WedgePart](/docs/reference/engine/classes/WedgePart.md)
- **Torso** - A block with sloped sides, due to be deprecated

Note, each [SpecialMesh.MeshType](/docs/reference/engine/classes/SpecialMesh.md) will scale differently when using
[DataModelMesh.Scale](/docs/reference/engine/classes/DataModelMesh.md), for more information on this please see the page
on [DataModelMesh.Scale](/docs/reference/engine/classes/DataModelMesh.md). The SpecialMesh object also exposes the
[DataModelMesh.Offset](/docs/reference/engine/classes/DataModelMesh.md) property.

It is important to remember that when using a SpecialMesh, only the appearance
of a part changes. The collision model of the part remains the same. For
example, a character will not be able to walk correctly over a mesh as the
mesh geometry is not taken into account.

#### SpecialMesh vs MeshPart

There are currently two ways of using a developer created mesh. They are using
a SpecialMesh with the [SpecialMesh.FileType](/docs/reference/engine/classes/SpecialMesh.md) set to 'FileMesh', or by
using a [MeshPart](/docs/reference/engine/classes/MeshPart.md). Although, on the whole, the [MeshPart](/docs/reference/engine/classes/MeshPart.md) object
has superseded the SpecialMesh there are some differences developers should be
aware of.

- [BasePart.Material](/docs/reference/engine/classes/BasePart.md) displays correctly on the mesh when using a
  [MeshPart](/docs/reference/engine/classes/MeshPart.md) and not when using a SpecialMesh
- [MeshParts](/docs/reference/engine/classes/MeshPart.md) include the [MeshPart.CollisionFidelity](/docs/reference/engine/classes/MeshPart.md)
  property, meaning the collision model of a [MeshPart](/docs/reference/engine/classes/MeshPart.md) can be set to
  resemble the geometry of the mesh. The SpecialMesh object by contrast, uses
  the parent [BaseParts](/docs/reference/engine/classes/BasePart.md) collision model
- The mesh of a [MeshPart](/docs/reference/engine/classes/MeshPart.md) scales on all axis depending on the
  [Size](/docs/reference/engine/classes/BasePart.md) property of the [MeshPart](/docs/reference/engine/classes/MeshPart.md), the mesh of a
  SpecialMesh does not
- The SpecialMesh object includes the [Offset](/docs/reference/engine/classes/DataModelMesh.md) and
  [Scale](/docs/reference/engine/classes/DataModelMesh.md) properties whereas
  [MeshParts](/docs/reference/engine/classes/MeshPart.md) do not
- The [MeshId](/docs/reference/engine/classes/FileMesh.md) property of a [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) can be
  changed by a [Script](/docs/reference/engine/classes/Script.md) or [LocalScript](/docs/reference/engine/classes/LocalScript.md) during runtime. The
  [MeshId](/docs/reference/engine/classes/MeshPart.md) property of a [MeshPart](/docs/reference/engine/classes/MeshPart.md) can not.

## Code Samples

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

## Properties

### Property: SpecialMesh.MeshType

```json
{
  "type": "MeshType",
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

The mesh that the [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md)object applies to the
[BasePart](/docs/reference/engine/classes/BasePart.md) depends on the MeshType property. A number of options are
available.

- **Brick** - A block shape, equivalent to a [BlockMesh](/docs/reference/engine/classes/BlockMesh.md)
- **Cylinder** - A cylinder, identical to a [Part](/docs/reference/engine/classes/Part.md) with a
  [Part.Shape](/docs/reference/engine/classes/Part.md) of 'Cylinder'
- **FileMesh** - A user uploaded Mesh, equivalent to [FileMesh](/docs/reference/engine/classes/FileMesh.md) that
  a texture can be applied to using the [FileMesh.TextureId](/docs/reference/engine/classes/FileMesh.md)
  property
- **Head** - A character head shape
- **Sphere** - A sphere shape, similar to a [Part](/docs/reference/engine/classes/Part.md) with a
  [Part.Shape](/docs/reference/engine/classes/Part.md) of 'Ball' but can be freely resized on all axis
- **Wedge** - A wedge shape, identical to a [WedgePart](/docs/reference/engine/classes/WedgePart.md)
- **Torso** - A block with sloped sides, due to be deprecated

Note, each MeshType will scale differently when using
[DataModelMesh.Scale](/docs/reference/engine/classes/DataModelMesh.md), for more information on this please see the
page on [DataModelMesh.Scale](/docs/reference/engine/classes/DataModelMesh.md).

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

### From [FileMesh](/docs/reference/engine/classes/FileMesh.md)

- **Property `MeshContent`** (`Content`): The mesh content applied to the parent BasePart, supporting asset
- **Property `MeshId`** (`ContentId`): The MeshId is the content ID of the mesh that is to be displayed.
- **Property `TextureContent`** (`Content`): The texture content applied to the mesh, supporting asset URIs and
- **Property `TextureId`** (`ContentId`): The TextureId is the content ID of the texture that is to be applied to

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