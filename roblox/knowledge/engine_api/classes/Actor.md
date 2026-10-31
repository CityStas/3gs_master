---
name: Actor
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Model
  - PVInstance
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "An Actor is a container for code that can be safely split into its own thread."
---

# Class: Actor

> An [Actor](/docs/reference/engine/classes/Actor.md) is a container for code that can be safely split into its own
> thread.

## Description

An [Actor](/docs/reference/engine/classes/Actor.md) is a container for code that can be safely split into its own
thread using [task.desynchronize()](/docs/reference/engine/globals/task.md). It should also contain the
instances used by its scripts.

To learn more about using multiple Actors to optimize script performance, see
[Parallel Luau](/docs/en-us/scripting/multithreading.md).

#### Notes

- Each `Actor` runs in its own Luau VM. [ModuleScripts](/docs/reference/engine/classes/ModuleScript.md)
  required by an `Actor` are **not** shared or cached across `Actors` or with
  the main thread. Each VM executes its own copy of the module, so
  module-level state is isolated per `Actor`. Design accordingly if your
  modules hold state you intend to share.
- `script:GetActor()` returns `nil` when called from a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md)
  unless the `ModuleScript` is a descendant of the `Actor`. `ModuleScripts`
  stored elsewhere (for example, [ReplicatedStorage](/docs/reference/engine/classes/ReplicatedStorage.md)) and required by an
  `Actor` are not considered descendants of the `Actor`.

## Methods

### Method: Actor:BindToMessage

**Signature:** `Actor:BindToMessage(topic: string, function: Function): RBXScriptConnection`

This method is used to bind a Luau callback to a message with the
specified topic. When a message is sent (using
[SendMessage()](/docs/reference/engine/classes/Actor.md)) to the topic specified the
provided callback will be called in a _serial_ execution context.

Multiple Luau callbacks may be bound to a single actor and even to a
single message topic.

Note: Only the scripts which are descendants of an Actor may bind to its
messages.

*Security: None · Thread Safety: Safe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `topic` | `string` |  | The topic used to identify the type of message. |
| `function` | `Function` |  | The Luau callback to invoke when a message with the specified topic is received. The callback receives the message contents as its arguments. |

**Returns:** `RBXScriptConnection` — This connection object may be used to disconnect the Luau callback
from receiving messages.

**Bind To Message**

Demonstrates [Actor:BindToMessage()](/docs/reference/engine/classes/Actor.md).

```lua
local actor = script:GetActor()

-- Print out a message when a greeting message is sent to the Actor
-- this script is a descendant of.
local connection = actor:BindToMessage("Greeting", function(message)
  print("Received Greeting Message:", message)
end)
```

### Method: Actor:BindToMessageParallel

**Signature:** `Actor:BindToMessageParallel(topic: string, function: Function): RBXScriptConnection`

This method is used to bind a Luau callback to a message with the
specified topic. When a message is sent (using
[SendMessage()](/docs/reference/engine/classes/Actor.md)) to the topic specified the
provided callback will be called in a _parallel_ execution context.

Multiple Luau callbacks may be bound to a single actor and even to a
single message topic.

Note: Only the scripts which are descendants of an Actor may bind to its
messages.

*Security: None · Thread Safety: Safe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `topic` | `string` |  | The topic used to identify the type of message. |
| `function` | `Function` |  | The Luau callback to invoke when a message with the specified topic is received. The callback receives the message contents as its arguments. |

**Returns:** `RBXScriptConnection` — This connection object may be used to disconnect the Luau callback
from receiving messages.

**Bind To Message Parallel**

Demonstrates [Actor:BindToMessageParallel()](/docs/reference/engine/classes/Actor.md).

```lua
local actor = script:GetActor()

-- Print out a message when a greeting message is sent to the Actor
-- this script is a descendant of.
local connection = actor:BindToMessageParallel("Greeting", function(message)
  print("Received Greeting Message:", message)
end)
```

### Method: Actor:SendMessage

**Signature:** `Actor:SendMessage(topic: string, message: Tuple): ()`

Sends a message to an Actor. Messages are sent asynchronously, so the
sender will not block or yield when calling the
[SendMessage()](/docs/reference/engine/classes/Actor.md) method.

Since a single Actor may receive different kinds of messages, a `topic`
parameter is used to distinguish between various kinds of messages.

See [BindToMessage()](/docs/reference/engine/classes/Actor.md) for details on receiving
a message sent using [SendMessage()](/docs/reference/engine/classes/Actor.md).

Note that message arguments are **passed by copy** across Luau VM
boundaries, not by reference. Sending large tables incurs a full copy on
each call. Functions are bound to a specific VM and cannot be passed in
messages.

*Security: None · Thread Safety: Safe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `topic` | `string` |  | The topic used to identify the message being sent. |
| `message` | `Tuple` |  | The contents of the message to send to the Actor. |

**Returns:** `()`

**Send Message**

Demonstrates [Actor:SendMessage()](/docs/reference/engine/classes/Actor.md).

```lua
local actor = script:GetActor()

actor:SendMessage("Greeting", "Hello World")
```

## Inherited Members

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