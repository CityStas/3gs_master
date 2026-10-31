---
name: HopperBin
last_updated: 2026-10-30T19:55:52Z
inherits:
  - BackpackItem
  - Model
  - PVInstance
  - Instance
  - Object
type: class
memory_category: BaseParts
tags:
  - Deprecated
---

# Class: HopperBin

## Description

HopperBins are an outdated system for creating tools that can be used by a
player. In place of HopperBins, please use [Tool](/docs/reference/engine/classes/Tool.md) instead.

Historically, only HopperBins worked without a 'Handle' [Part](/docs/reference/engine/classes/Part.md), but this
is no longer the case thanks to the [Tool.RequiresHandle](/docs/reference/engine/classes/Tool.md) property of
Tools.

## Properties

### Property: HopperBin.Active

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
    "Input"
  ]
}
```

### Property: HopperBin.BinType

```json
{
  "type": "BinType",
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
    "Input"
  ]
}
```

## Events

### Event: HopperBin.Deselected

**Signature:** `HopperBin.Deselected()`

*Security: None · Capabilities: Input*

### Event: HopperBin.Selected

**Signature:** `HopperBin.Selected(mouse: Instance)`

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `mouse` | `Instance` |  |

## Inherited Members

### From [BackpackItem](/docs/reference/engine/classes/BackpackItem.md)

- **Property `TextureContent`** (`Content`): The texture icon that is displayed for a tool in the player's backpack.
- **Property `TextureId`** (`ContentId`): The texture icon that is displayed for a tool in the player's backpack.

### From [Model](/docs/reference/engine/classes/Model.md)

- **Property `LevelOfDetail`** (`ModelLevelOfDetail`): Sets the level of detail on the model for experiences with instance
- **Property `ModelStreamingMode`** (`ModelStreamingMode`): Controls the model streaming behavior on Models when
- **Property `PrimaryPart`** (`BasePart`): The primary part of the Model, or `nil` if not explicitly set.
- **Property `Scale`** (`float`): Editor-only property used to scale the model around its pivot. Setting
- **Property `WorldPivot`** (`CFrame`): Determines where the pivot of a Model which does **not** have a
- **Method `AddPersistentPlayer(playerInstance?: Player): ()`**: Sets this model to be persistent for the specified player.
- **Method `BreakJoints(): ()`**: Breaks connections between `BaseParts`, including surface connections with *(deprecated)*
- **Method `breakJoints(): ()`**:  *(deprecated)*
- **Method `GetBoundingBox(): Tuple`**: Returns a description of a volume that contains all parts of a Model.
- **Method `GetExtentsSize(): Vector3`**: Returns the size of the smallest bounding box that contains all of the
- **Method `GetModelCFrame(): CFrame`**: This value historically returned the CFrame of a central position in the *(deprecated)*
- **Method `GetModelSize(): Vector3`**: Returns the Vector3 size of the Model. *(deprecated)*
- **Method `GetPersistentPlayers(): List<Player>`**: Returns all the Player objects that this model object is
- **Method `GetPrimaryPartCFrame(): CFrame`**: Returns the CFrame of the model's Model.PrimaryPart. *(deprecated)*
- **Method `GetScale(): float`**: Returns the canonical scale of the model, which defaults to 1 for newly
- **Method `MakeJoints(): ()`**: Goes through all BaseParts in the Model. If any *(deprecated)*
- **Method `makeJoints(): ()`**:  *(deprecated)*
- **Method `move(location: Vector3): ()`**:  *(deprecated)*
- **Method `MoveTo(position: Vector3): ()`**: Moves the PrimaryPart to the given position. If
- **Method `moveTo(location: Vector3): ()`**:  *(deprecated)*
- **Method `RemovePersistentPlayer(playerInstance?: Player): ()`**: Makes this model no longer persistent for the specified player.
- **Method `ResetOrientationToIdentity(): ()`**: Resets the rotation of the model's parts to the previously set identity *(deprecated)*
- **Method `ScaleTo(newScaleFactor: float): ()`**: Sets the scale factor of the model, adjusting the sizing and location of
- **Method `SetIdentityOrientation(): ()`**: Sets the identity rotation of the given model, allowing you to reset the *(deprecated)*
- **Method `SetPrimaryPartCFrame(cframe: CFrame): ()`**: Sets the BasePart.CFrame of the model's Model.PrimaryPart. *(deprecated)*
- **Method `TranslateBy(delta: Vector3): ()`**: Shifts a Model by the given Vector3 offset, preserving

### From [PVInstance](/docs/reference/engine/classes/PVInstance.md)

- **Property `Origin`** (`CFrame`): Editor-only property that reads and sets the world CFrame of
- **Property `Pivot Offset`** (`CFrame`): Editor-only property that displays and edits the pivot's CFrame
- **Method `GetPivot(): CFrame`**: Gets the pivot of a PVInstance.
- **Method `PivotTo(targetCFrame: CFrame): ()`**: Transforms the PVInstance along with all of its descendant

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