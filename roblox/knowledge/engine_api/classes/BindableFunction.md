---
name: BindableFunction
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "An object which allows for synchronous two-way communication between scripts on the same side of the client-server boundary. Scripts invoking a BindableFunction yield until the corresponding callback is found."
---

# Class: BindableFunction

> An object which allows for synchronous two-way communication between scripts
> on the same side of the client-server boundary. Scripts invoking a
> [BindableFunction](/docs/reference/engine/classes/BindableFunction.md) yield until the corresponding callback is found.

## Description

The **BindableFunction** object allows for synchronous two-way communication
between scripts on the same side of the
[client-server](/docs/en-us/projects/client-server.md) boundary. You can use it
to define a custom callback function and invoke it manually by calling
[BindableFunction:Invoke()](/docs/reference/engine/classes/BindableFunction.md). The code invoking the function **yields**
until the corresponding callback is found, and the callback receives the
arguments that you passed to [Invoke()](/docs/reference/engine/classes/BindableFunction.md). If
the callback was never set, the script that invokes it will not resume
execution.

As an alternative for one-way communication between two scripts on the same
side of the client-server boundary, consider [BindableEvent](/docs/reference/engine/classes/BindableEvent.md) which does
**not** yield for a return.

As stated, [BindableFunctions](/docs/reference/engine/classes/BindableFunction.md) do not allow for
communication between the server and clients. If you are looking for this
functionality, use a [RemoteFunction](/docs/reference/engine/classes/RemoteFunction.md) as outlined in
[Remote events and callbacks](/docs/en-us/scripting/events/remote.md).

See [Bindable events and callbacks](/docs/en-us/scripting/events/bindable.md) for
code samples and further details on [BindableFunction](/docs/reference/engine/classes/BindableFunction.md).

#### Parameter Limitations

Any type of Roblox object such as an [Enum](/docs/reference/engine/datatypes/Enum.md), [Instance](/docs/reference/engine/classes/Instance.md), or
others can be passed as a parameter when a [BindableFunction](/docs/reference/engine/classes/BindableFunction.md) is
invoked, as well as Luau types such as numbers, strings, and booleans,
although you should carefully explore the
[limitations](/docs/en-us/scripting/events/bindable.md#argument-limitations).

## Methods

### Method: BindableFunction:Invoke

**Signature:** `BindableFunction:Invoke(arguments: Tuple): Tuple`

Invokes the [BindableFunction](/docs/reference/engine/classes/BindableFunction.md) which in turn calls the
[OnInvoke](/docs/reference/engine/classes/BindableFunction.md) callback, returning any values
returned by the callback. Invocations yield until the corresponding
callback is found, and if the callback was never set, the script that
invokes it will not resume execution.

Any type of Roblox object such as an [Enum](/docs/reference/engine/datatypes/Enum.md), [Instance](/docs/reference/engine/classes/Instance.md), or
others can be passed as a parameter to
[Invoke()](/docs/reference/engine/classes/BindableFunction.md), as well as Luau types such as
numbers, strings, and booleans, although you should carefully explore the
[limitations](/docs/en-us/scripting/events/bindable.md#argument-limitations).

Only one function can be bound to
[Invoke()](/docs/reference/engine/classes/BindableFunction.md) at a time. If you assign
multiple functions, only the last one assigned will be used.

See [Bindable events and callbacks](/docs/en-us/scripting/events/bindable.md)
for code samples and further details on
[Invoke()](/docs/reference/engine/classes/BindableFunction.md).

*Yields · Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `arguments` | `Tuple` |  | Values to pass to the [OnInvoke](/docs/reference/engine/classes/BindableFunction.md) callback. |

**Returns:** `Tuple` — Values returned from the [OnInvoke](/docs/reference/engine/classes/BindableFunction.md)
callback.

## Callbacks

### Callback: BindableFunction.OnInvoke

**Signature:** `BindableFunction.OnInvoke(arguments: Tuple): Tuple`

This callback is called when the [BindableFunction](/docs/reference/engine/classes/BindableFunction.md) is invoked with
[Invoke()](/docs/reference/engine/classes/BindableFunction.md). It can be set multiple times
but cannot be called directly. Invocations will yield until this callback
is found and, if it is never set, the script that invoked it will not
resume execution.

See [Bindable events and callbacks](/docs/en-us/scripting/events/bindable.md)
for code samples and further details on
[OnInvoke](/docs/reference/engine/classes/BindableFunction.md).

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `arguments` | `Tuple` |  | The parameters sent through [Invoke()](/docs/reference/engine/classes/BindableFunction.md). |

**Returns:** `Tuple` — Values returned by the callback function.

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