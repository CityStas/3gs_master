---
name: TextChatCommand
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Represents a text chat command."
---

# Class: TextChatCommand

> Represents a text chat command.

## Description

Represents a text chat command. Can be used to create custom text chat
commands when parented to [TextChatService](/docs/reference/engine/classes/TextChatService.md).

Custom commands can have up to two aliases, and the Triggered event fires when
a user's message matches the value of either the
[PrimaryAlias](/docs/reference/engine/classes/TextChatCommand.md) or
[SecondaryAlias](/docs/reference/engine/classes/TextChatCommand.md). For an example of
custom commands, see
[Custom text chat commands](/docs/en-us/chat/examples/custom-text-chat-commands.md).

To learn more about using [TextChatService](/docs/reference/engine/classes/TextChatService.md), see
[In-experience text chat](/docs/en-us/chat/in-experience-text-chat.md).

## Properties

### Property: TextChatCommand.AutocompleteVisible

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
  "category": "Behavior",
  "capabilities": [
    "Chat"
  ]
}
```

Whether this [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md) appears as a suggestion in the chat
autocomplete menu. Defaults to `true`.

When `true`, [PrimaryAlias](/docs/reference/engine/classes/TextChatCommand.md) is offered
in the autocomplete list. Set to `false` to hide it from suggestions; the
command still works when typed in full via
[PrimaryAlias](/docs/reference/engine/classes/TextChatCommand.md) or
[SecondaryAlias](/docs/reference/engine/classes/TextChatCommand.md).

Autocomplete itself is controlled by
[ChatInputBarConfiguration.AutocompleteEnabled](/docs/reference/engine/classes/ChatInputBarConfiguration.md).

### Property: TextChatCommand.Enabled

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
  "category": "Behavior",
  "capabilities": [
    "Chat"
  ]
}
```

Determines whether the [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md) is enabled.

When disabled, messages that match the value of
[PrimaryAlias](/docs/reference/engine/classes/TextChatCommand.md) or
[SecondaryAlias](/docs/reference/engine/classes/TextChatCommand.md) are not sunk and is
sent to other users.

Use this to disable default commands on a case-by-case basis.

### Property: TextChatCommand.PrimaryAlias

```json
{
  "type": "string",
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
  "category": "Behavior",
  "capabilities": [
    "Chat"
  ]
}
```

A primary alias used to trigger the [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md).

If a user sends a message with [TextChannel:SendAsync()](/docs/reference/engine/classes/TextChannel.md) that
matches the [PrimaryAlias](/docs/reference/engine/classes/TextChatCommand.md), the message
is not sent and instead [TextChatCommand.Triggered](/docs/reference/engine/classes/TextChatCommand.md) is fired.

### Property: TextChatCommand.SecondaryAlias

```json
{
  "type": "string",
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
  "category": "Behavior",
  "capabilities": [
    "Chat"
  ]
}
```

A secondary alias used to trigger the [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md), in addition
to its [PrimaryAlias](/docs/reference/engine/classes/TextChatCommand.md).

If a user sends a message with [TextChannel:SendAsync()](/docs/reference/engine/classes/TextChannel.md) that
matches the [SecondaryAlias](/docs/reference/engine/classes/TextChatCommand.md), the
message is not sent and instead [TextChatCommand.Triggered](/docs/reference/engine/classes/TextChatCommand.md) is
fired, exactly as it is for the
[PrimaryAlias](/docs/reference/engine/classes/TextChatCommand.md). Matching is
case-insensitive, and the alias must be followed by the end of the message
or a space, so a [SecondaryAlias](/docs/reference/engine/classes/TextChatCommand.md) of
`"/e"` matches `"/e"` and `"/e dance"` but not `"/emote"`.

Defaults to an empty string, in which case only the
[PrimaryAlias](/docs/reference/engine/classes/TextChatCommand.md) triggers the command.

## Events

### Event: TextChatCommand.Triggered

**Signature:** `TextChatCommand.Triggered(originTextSource: TextSource, unfilteredText: string)`

An event that developers can bind to execute commands.

When a user sends a message to the server via
[TextChannel:SendAsync()](/docs/reference/engine/classes/TextChannel.md), the message is intercepted by the
[TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md) and not replicated to other users if the content
of the message matches the
[PrimaryAlias](/docs/reference/engine/classes/TextChatCommand.md) or
[SecondaryAlias](/docs/reference/engine/classes/TextChatCommand.md).

For example, for a [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md) with
[TextChatCommand.PrimaryAlias](/docs/reference/engine/classes/TextChatCommand.md) as "mute", if a user sends "/mute
SomeUserName", then the relevant [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md) for mute will
fire its [TextChatCommand.Triggered](/docs/reference/engine/classes/TextChatCommand.md). The message "/mute
SomeUserName" is not replicated to other users.

*Security: None · Capabilities: Chat*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `originTextSource` | `TextSource` | A reference to the [TextSource](/docs/reference/engine/classes/TextSource.md) responsible for triggering the command via [TextChannel:SendAsync()](/docs/reference/engine/classes/TextChannel.md). |
| `unfilteredText` | `string` | The full, unfiltered text used to trigger the command that can be used to dissect parameters from the command message. |

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