---
name: BaseWrap
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
summary: "Abstract base class for WrapTarget and WrapLayer that stores cage mesh data for layered clothing deformation."
---

# Class: BaseWrap

> Abstract base class for [WrapTarget](/docs/reference/engine/classes/WrapTarget.md) and [WrapLayer](/docs/reference/engine/classes/WrapLayer.md) that stores
> cage mesh data for layered clothing deformation.

## Description

The base class for [WrapTarget](/docs/reference/engine/classes/WrapTarget.md) and [WrapLayer](/docs/reference/engine/classes/WrapLayer.md) objects. Note that
[MeshPart](/docs/reference/engine/classes/MeshPart.md) is the only valid parent type for [BaseWrap](/docs/reference/engine/classes/BaseWrap.md) and that
it behaves more like a component of [MeshPart](/docs/reference/engine/classes/MeshPart.md) than an independent
object.

## Properties

### Property: BaseWrap.CageMeshContent

```json
{
  "type": "Content",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

The cage mesh this wrap uses to deform geometry, stored as a
[Content](/docs/reference/engine/datatypes/Content.md) value that can reference an uploaded mesh asset or an
in-memory [EditableMesh](/docs/reference/engine/classes/EditableMesh.md). Set automatically by the Importer. It is
the backing store for [BaseWrap.CageMeshId](/docs/reference/engine/classes/BaseWrap.md): that property reads the
mesh ID from this content, and setting either keeps both in sync and
raises a change on both.

Defaults to an empty [Content](/docs/reference/engine/datatypes/Content.md). Without a valid cage, the wrap
cannot contribute to layered clothing deformation for [WrapLayer](/docs/reference/engine/classes/WrapLayer.md) or
[WrapTarget](/docs/reference/engine/classes/WrapTarget.md).

### Property: BaseWrap.CageMeshId

```json
{
  "type": "ContentId",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

This property is set up automatically by the 3D Importer.

Asset ID for cage mesh.

### Property: BaseWrap.CageOrigin

```json
{
  "type": "CFrame",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

This property is set up automatically by the 3D Importer.

Cage mesh offset relative to parent [MeshPart](/docs/reference/engine/classes/MeshPart.md).

### Property: BaseWrap.CageOriginWorld

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
  "category": "Data",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

Cage mesh offset in world space.

### Property: BaseWrap.HSRAssetId

```json
{
  "type": "ContentId",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxEngineSecurity"
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

This property is not accessible through scripts but is viewable in the
Properties window for any [BaseWrap](/docs/reference/engine/classes/BaseWrap.md) object. It references
precomputed data that determines which mesh triangles are hidden when
clothing layers overlap.

### Property: BaseWrap.HSRContent

```json
{
  "type": "Content",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxEngineSecurity"
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

Hidden surface removal (HSR) data for this wrap, stored as a
[Content](/docs/reference/engine/datatypes/Content.md) value that references a precomputed mesh asset. It is
the backing store for [BaseWrap.HSRAssetId](/docs/reference/engine/classes/BaseWrap.md): that property reads the
asset ID from this content, and setting either keeps both in sync.

The content determines which mesh triangles are hidden when clothing
layers overlap so occluded geometry can be culled during layered clothing
deformation. Generated automatically when a [BaseWrap](/docs/reference/engine/classes/BaseWrap.md) is published;
you do not need to set it manually.

### Property: BaseWrap.ImportOrigin

```json
{
  "type": "CFrame",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

This property is set up automatically by the 3D Importer.

Describes where a global zero was while authoring the cage mesh in an
asset creation tool such as Blender or Maya. This property is not used by
the deformer but it is useful for tools/aligning scripts, for example
aligning two parts by matching their pivots as follows:

**Import Origin**

Demonstrates [BaseWrap.ImportOrigin](/docs/reference/engine/classes/BaseWrap.md).

```lua
local function alignWraps()
	local selectionService = game:GetService("Selection")
	local selectedObjects = selectionService:Get()
	local alignObjects = {}
	for _, obj in selectedObjects do
		if obj:IsA("BaseWrap") then
			--print("Wrap: " .. obj.Name)
			table.insert(alignObjects, obj)
		else
			print("Ignore: " .. obj.Name)
		end
	end

	if #alignObjects < 2 then
		warn("You need to select at least two wraps")
		return
	end

	local anchorWrap = alignObjects[1]
	local worldA_from_Wrap = anchorWrap.ImportOriginWorld
	print("Anchor: " .. anchorWrap.Name)
	for i = 2, #alignObjects do
		local wrapToAlign = alignObjects[i]
		print("Align: " .. wrapToAlign.Name)
		local wrap_from_WorldB = wrapToAlign.ImportOriginWorld:Inverse()
		local worldA_from_WorldB = worldA_from_Wrap * wrap_from_WorldB
		local worldB = wrapToAlign.Parent.CFrame
		-- Note: adjust CFrame of the parent part
		wrapToAlign.Parent.CFrame = (worldB_from_WorldB * worldB)
	end
end
```

### Property: BaseWrap.ImportOriginWorld

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
  "category": "Data",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

Describes where the origin (in world space) was while authoring the cage
mesh in an asset creation tool such as Blender or Maya.

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