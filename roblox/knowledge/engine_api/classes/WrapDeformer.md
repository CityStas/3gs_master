---
name: WrapDeformer
last_updated: 2026-10-30T19:55:53Z
inherits:
  - BaseWrap
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Allows for the real-time deformation of a MeshPart."
---

# Class: WrapDeformer

> Allows for the real-time deformation of a [MeshPart](/docs/reference/engine/classes/MeshPart.md).

## Description

The [WrapDeformer](/docs/reference/engine/classes/WrapDeformer.md) object provides a low-resolution cage mesh that pairs
with a [WrapTarget](/docs/reference/engine/classes/WrapTarget.md) sibling to deform a parent [MeshPart](/docs/reference/engine/classes/MeshPart.md). The
[MeshPart](/docs/reference/engine/classes/MeshPart.md) geometry is deformed according to the displacement between
pairs of [WrapTarget](/docs/reference/engine/classes/WrapTarget.md) cage mesh vertices and [WrapDeformer](/docs/reference/engine/classes/WrapDeformer.md) cage
mesh vertices. Cage mesh vertices are paired based on UV equivalence.

[WrapDeformer](/docs/reference/engine/classes/WrapDeformer.md) may be used with avatars or on distinct
[MeshParts](/docs/reference/engine/classes/MeshPart.md), as long as [WrapTarget](/docs/reference/engine/classes/WrapTarget.md) children are present
for the parent [MeshParts](/docs/reference/engine/classes/MeshPart.md). [WrapDeformer](/docs/reference/engine/classes/WrapDeformer.md) is similar to
[WrapLayer](/docs/reference/engine/classes/WrapLayer.md) but doesn't require layered clothing and can directly deform
[MeshParts](/docs/reference/engine/classes/MeshPart.md) for publishing.

## Methods

### Method: WrapDeformer:CreateEditableMeshAsync

**Signature:** `WrapDeformer:CreateEditableMeshAsync(): EditableMesh`

Constructs and returns an [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) corresponding to the
deformed parent mesh geometry. This method respects all updates made to
the deformation inputs prior to the request. It also sets the returned
result's [FixedSize](/docs/reference/engine/classes/EditableMesh.md) to `true`.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance*

**Returns:** `EditableMesh` — An [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) matching the deformed parent mesh geometry,
with its [FixedSize](/docs/reference/engine/classes/EditableMesh.md) set to `true`.

### Method: WrapDeformer:GetDeformedCFrameAsync

**Signature:** `WrapDeformer:GetDeformedCFrameAsync(originalCFrame: CFrame): CFrame`

Returns a [CFrame](/docs/reference/engine/datatypes/CFrame.md) deformed by the same deformation field used
for the geometry of the parent [MeshPart](/docs/reference/engine/classes/MeshPart.md). This method is useful for
the placement of accessories.

The input and output [CFrame](/docs/reference/engine/datatypes/CFrame.md) are both in the space of the parent
[MeshPart](/docs/reference/engine/classes/MeshPart.md); only position (not rotation) will be deformed. This
method respects all updates made to the deformation inputs prior to the
request.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `originalCFrame` | `CFrame` |  | The [CFrame](/docs/reference/engine/datatypes/CFrame.md), expressed in the local space of the parent [MeshPart](/docs/reference/engine/classes/MeshPart.md), whose position is deformed. |

**Returns:** `CFrame` — A [CFrame](/docs/reference/engine/datatypes/CFrame.md) in the parent [MeshPart](/docs/reference/engine/classes/MeshPart.md) space with its
position displaced by the same deformation field applied to the parent
mesh; rotation is unchanged.

### Method: WrapDeformer:SetCageMeshContent

**Signature:** `WrapDeformer:SetCageMeshContent(content: Content, cageOrigin: CFrame?): ()`

Sets the cage mesh used to deform the parent [MeshPart](/docs/reference/engine/classes/MeshPart.md) in
conjunction with a sibling [WrapTarget](/docs/reference/engine/classes/WrapTarget.md) cage mesh. The `content`
parameter should represent a Roblox mesh asset ID or an
[EditableMesh](/docs/reference/engine/classes/EditableMesh.md) reference in your [DataModel](/docs/reference/engine/classes/DataModel.md).

*Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `content` | `Content` |  | A Roblox mesh asset ID or an [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) reference specifying the cage mesh to deform against the sibling [WrapTarget](/docs/reference/engine/classes/WrapTarget.md). |
| `cageOrigin` | `CFrame?` |  | An optional [CFrame](/docs/reference/engine/datatypes/CFrame.md), in the parent [MeshPart](/docs/reference/engine/classes/MeshPart.md) space, that sets the cage's [CageOrigin](/docs/reference/engine/classes/BaseWrap.md). When omitted, the existing [CageOrigin](/docs/reference/engine/classes/BaseWrap.md) is left unchanged. |

**Returns:** `()`

## Inherited Members

### From [BaseWrap](/docs/reference/engine/classes/BaseWrap.md)

- **Property `CageMeshContent`** (`Content`): The cage mesh this wrap uses to deform geometry, stored as a
- **Property `CageMeshId`** (`ContentId`): Asset ID for cage mesh.
- **Property `CageOrigin`** (`CFrame`): Cage mesh offset relative to parent MeshPart.
- **Property `CageOriginWorld`** (`CFrame`): Cage mesh offset in world space.
- **Property `HSRAssetId`** (`ContentId`): Asset ID for the hidden surface removal (HSR) data used by layered
- **Property `HSRContent`** (`Content`): The hidden surface removal data for this wrap, stored as a
- **Property `ImportOrigin`** (`CFrame`): Describes where a global zero was while authoring the cage mesh in an
- **Property `ImportOriginWorld`** (`CFrame`): Describes where the origin (in world space) was while authoring the cage

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