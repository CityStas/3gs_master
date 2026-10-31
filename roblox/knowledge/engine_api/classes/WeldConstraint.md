---
name: WeldConstraint
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "Connects two BaseParts together such that their relative position and orientation remain the same."
---

# Class: WeldConstraint

> Connects two [BaseParts](/docs/reference/engine/classes/BasePart.md) together such that their relative
> position and orientation remain the same.

## Description

**WeldConstraint** connects two [BaseParts](/docs/reference/engine/classes/BasePart.md) and ensures they
stay in the same relative position/orientation to each other, meaning that if
one part moves, the other moves the same amount. Even if the two parts are not
touching, they can be welded together.

The most common way to create a weld constraint is by selecting **Weld**
through Studio's **Create** menu in the toolbar's **Model** tab.

Note that this tool behaves differently depending on how many
[BaseParts](/docs/reference/engine/classes/BasePart.md) are selected when the tool is activated:

- If no [BaseParts](/docs/reference/engine/classes/BasePart.md) are selected, the next two
  [BaseParts](/docs/reference/engine/classes/BasePart.md) clicked will be connected by a new
  [WeldConstraint](/docs/reference/engine/classes/WeldConstraint.md). If the same [BasePart](/docs/reference/engine/classes/BasePart.md) is clicked twice, no
  constraint will be created.
- If one [BasePart](/docs/reference/engine/classes/BasePart.md) is already selected, the next [BasePart](/docs/reference/engine/classes/BasePart.md)
  clicked will be connected to the selected one with a new
  [WeldConstraint](/docs/reference/engine/classes/WeldConstraint.md).
- If multiple [BaseParts](/docs/reference/engine/classes/BasePart.md) are selected, those which are
  touching or overlapping will be automatically welded together by new
  [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md).

#### Repositioning Behavior

Moving a welded [BasePart](/docs/reference/engine/classes/BasePart.md) behaves differently depending on whether the
part was moved through its [Position](/docs/reference/engine/classes/BasePart.md) or through its
[CFrame](/docs/reference/engine/datatypes/CFrame.md).

- If a welded part's [Position](/docs/reference/engine/classes/BasePart.md) is updated, that part
  will move but none of the connected parts will move with it. The weld will
  recalculate the offset from the other parts based on the moved part's new
  position.

- If a welded part's [CFrame](/docs/reference/engine/datatypes/CFrame.md) is updated, that part will move **and**
  all of the connected parts will also move, ensuring they maintain the same
  offset as when the weld was created.

## Properties

### Property: WeldConstraint.Active

```json
{
  "type": "boolean",
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
  "category": "Behavior",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

True if the WeldConstraint is currently active in the world.

If the WeldConstraint or one of its parts is not in [Workspace](/docs/reference/engine/classes/Workspace.md) the
weld will be inactive.

Rigid joints like [Weld](/docs/reference/engine/classes/Weld.md), [Snap](/docs/reference/engine/classes/Snap.md), [WeldConstraint](/docs/reference/engine/classes/WeldConstraint.md),
[Motor](/docs/reference/engine/classes/Motor.md), or [Motor6D](/docs/reference/engine/classes/Motor6D.md) may also be disabled due to conflicts
with other rigid joints, such as joints between the same two parts or
indirect cycles in the weld graph. Joints disabled this way may be
re-enabled later when another joint or part is added or removed.

Duplicate WeldConstraints do not conflict because WeldConstraints derive
their internal CFrames from the relative positions of their parts when
they are enabled and all update when [BasePart.Position](/docs/reference/engine/classes/BasePart.md) or
[BasePart.Orientation](/docs/reference/engine/classes/BasePart.md) is set on a part. The spanning tree may still
disable them if they are redundant or form a cycle.

### Property: WeldConstraint.Enabled

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The **Enabled** property of a [WeldConstraint](/docs/reference/engine/classes/WeldConstraint.md) sets whether the
constraint is active or not. When this property is set to true, if the
constraint's [WeldConstraint.Part0](/docs/reference/engine/classes/WeldConstraint.md) and [WeldConstraint.Part1](/docs/reference/engine/classes/WeldConstraint.md)
properties are set, then the constraint will ensure that its two connected
parts will be locked together.

### Property: WeldConstraint.Part0

```json
{
  "type": "BasePart",
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
  "category": "Parts",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The `Part0` and [WeldConstraint.Part1](/docs/reference/engine/classes/WeldConstraint.md) properties of a
[WeldConstraint](/docs/reference/engine/classes/WeldConstraint.md) set which two [BasePart](/docs/reference/engine/classes/BasePart.md) the weld connects.
As soon as both properties are set and the weld is
[WeldConstraint.Enabled](/docs/reference/engine/classes/WeldConstraint.md), the weld will lock the two parts together.

If `Part0` or `Part1` are ever set to new parts, then the `WeldConstraint`
will instantly link the new part. The old part will no longer be
constrained.

**Part0**

Demonstrates [WeldConstraint.Part0](/docs/reference/engine/classes/WeldConstraint.md).

```lua
local Workspace = game:GetService("Workspace")

local partA = Instance.new("Part")
local partB = Instance.new("Part")

partA.Position = Vector3.new(0, 10, 0)
partA.Parent = Workspace

partB.Position = Vector3.new(0, 10, 10)
partB.Parent = Workspace

local weld = Instance.new("WeldConstraint")
weld.Part0 = partA
weld.Part1 = partB
weld.Parent = partA
```

### Property: WeldConstraint.Part1

```json
{
  "type": "BasePart",
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
  "category": "Parts",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The [WeldConstraint.Part0](/docs/reference/engine/classes/WeldConstraint.md) and `Part1` properties of a
[WeldConstraint](/docs/reference/engine/classes/WeldConstraint.md) set which two [BasePart](/docs/reference/engine/classes/BasePart.md) the weld connects.
As soon as both properties are set and the weld is
[WeldConstraint.Enabled](/docs/reference/engine/classes/WeldConstraint.md), the weld will lock the two parts together.

If `Part0` or `Part1` are ever set to new parts, then the `WeldConstraint`
will instantly link the new part. The old part will no longer be
constrained.

**Part1**

Demonstrates [WeldConstraint.Part1](/docs/reference/engine/classes/WeldConstraint.md).

```lua
local Workspace = game:GetService("Workspace")

local partA = Instance.new("Part")
local partB = Instance.new("Part")

partA.Position = Vector3.new(0, 10, 0)
partA.Parent = Workspace

partB.Position = Vector3.new(0, 10, 10)
partB.Parent = Workspace

local weld = Instance.new("WeldConstraint")
weld.Part0 = partA
weld.Part1 = partB
weld.Parent = partA
```

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