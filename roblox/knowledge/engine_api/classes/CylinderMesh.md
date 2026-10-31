---
name: CylinderMesh
last_updated: 2026-10-30T19:55:52Z
inherits:
  - BevelMesh
  - DataModelMesh
  - Instance
  - Object
type: class
memory_category: BaseParts
tags:
  - Deprecated
summary: "The CylinderMesh object applies a 'cylinder' mesh to the BasePart it is parented to."
---

# Class: CylinderMesh

> The CylinderMesh object applies a 'cylinder' mesh to the [BasePart](/docs/reference/engine/classes/BasePart.md) it
> is parented to.

## Description

The CylinderMesh object applies a 'cylinder' mesh to the [BasePart](/docs/reference/engine/classes/BasePart.md) it
is parented to.

## What does a CylinderMesh do?

A CylinderMesh gives the [BasePart](/docs/reference/engine/classes/BasePart.md) it was applied to a cylinder shaped
mesh.

The mesh applied gives the same appearance as that due to the
[SpecialMesh.MeshType](/docs/reference/engine/classes/SpecialMesh.md) of a [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) being set to 'Cylinder'
or [Part.Shape](/docs/reference/engine/classes/Part.md) being set to 'Cylinder'. However, unlike those two
cases, it is orientated so that the height of the cylinder is along the
[BasePart](/docs/reference/engine/classes/BasePart.md) Y axis.

The dimensions of the mesh scale relative to the [BasePart.Size](/docs/reference/engine/classes/BasePart.md) of the
[BasePart](/docs/reference/engine/classes/BasePart.md). This scale is uniformly along the [BasePart](/docs/reference/engine/classes/BasePart.md) Y axis
and maintaining a 1:1 ratio for the part's X and Z axis, using the lowest
value. This means the [BasePart](/docs/reference/engine/classes/BasePart.md) can be resized normally, but the cross
section of the cylinder will always remain a circle and cannot be stretched or
compressed.

Note as the CylinderMesh object does not include a texture the
[DataModelMesh.VertexColor](/docs/reference/engine/classes/DataModelMesh.md) property does not do anything.

## Why use a CylinderMesh?

The advantage of using a mesh over setting the [Part.Shape](/docs/reference/engine/classes/Part.md) property of
a part to 'Cylinder' is that the [DataModelMesh.Scale](/docs/reference/engine/classes/DataModelMesh.md) and
[DataModelMesh.Offset](/docs/reference/engine/classes/DataModelMesh.md) properties are exposed. These allow the position
and dimensions of the mesh that is displayed to be changed without changing
the [BasePart.Position](/docs/reference/engine/classes/BasePart.md) or [BasePart.Size](/docs/reference/engine/classes/BasePart.md) of the [Part](/docs/reference/engine/classes/Part.md) the
mesh is parented to.

The key difference between a CylinderMesh or a [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) with
[SpecialMesh.MeshType](/docs/reference/engine/classes/SpecialMesh.md) set to 'Cylinder' is the orientation of the
cylinder mesh. With a CylinderMesh, the height of the cylinder is aligned with
the height (Y axis) of the part. With a [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) (or [Part](/docs/reference/engine/classes/Part.md)
with [Part.Shape](/docs/reference/engine/classes/Part.md) set to 'Cylinder'), the height of the cylinder is
aligned with the X axis.

## Code Samples

**CylinderMesh Instantiation**

This code sample includes a demonstration of how a `CylinderMesh` can be used,
and how it scales so as to maintain a constant ratio of length to width.

```lua
local part = Instance.new("Part")
part.Position = Vector3.new(0, 2, 0)
part.Size = Vector3.new(10, 2, 5)
part.Anchored = true

local mesh = Instance.new("CylinderMesh")
mesh.Parent = part

mesh.Scale = Vector3.new(1, 1, 1)
mesh.Offset = Vector3.new(0, 0, 0)

local adornment = Instance.new("SelectionBox")
adornment.Adornee = part
adornment.Parent = part

part.Parent = workspace
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