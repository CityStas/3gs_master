---
name: TextFilterResult
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "Represents the result of a call to TextService:FilterStringAsync(), used to distribute a filtered string accordingly."
---

# Class: TextFilterResult

> Represents the result of a call to [TextService:FilterStringAsync()](/docs/reference/engine/classes/TextService.md),
> used to distribute a filtered string accordingly.

## Description

Represents the result of a call to [TextService:FilterStringAsync()](/docs/reference/engine/classes/TextService.md).
Used to distribute a filtered string accordingly.

## Methods

### Method: TextFilterResult:GetNonChatStringForBroadcastAsync

**Signature:** `TextFilterResult:GetNonChatStringForBroadcastAsync(): string`

Returns the text in a properly filtered manner for all users. This should
be used in the context of non-chat text that every user can see, such as
for a dialog that lets a user write a message on a sign, visible to all
users on the server even after the author has left.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `string` — Filtered text string.

### Method: TextFilterResult:GetNonChatStringForUserAsync

**Signature:** `TextFilterResult:GetNonChatStringForUserAsync(toUserId: int64): string`

Returns the text in a properly filtered manner for the specified
[Player.UserId](/docs/reference/engine/classes/Player.md) based on age and other details. This should be used
in the context of non-chat text that one specific user can see, such as
the name of a pet.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `toUserId` | `int64` |  | [Player.UserId](/docs/reference/engine/classes/Player.md) of the user intended to see/receive the text. |

**Returns:** `string` — Filtered text string.

### Method: TextFilterResult:GetChatForUserAsync

**Signature:** `TextFilterResult:GetChatForUserAsync(toUserId: int64): string`

> **Deprecated:** This method is deprecated and returns an empty string. Text filtering pertaining to chat should be done through [TextChatService](/docs/reference/engine/classes/TextChatService.md), and experiences that do not properly filter player-generated chat text may be subject to moderation.

This method returns the text in a properly filtered manner for the
specified [Player.UserId](/docs/reference/engine/classes/Player.md) using the least restrictive filtering
appropriate for that user, with [Chat](/docs/reference/engine/classes/Chat.md) privacy settings of both
users enforced. This should be used in the context of chats between
players, although there are some other cases where text filtering is
required.

The returned string should only be shown to the target user, as it might
not be appropriate for all users.

If this method throws an error, the string should **not** be displayed to
the user. Cases for error include:

- The two users are not allowed to chat, for example if
  [Chat:CanUserChatAsync()](/docs/reference/engine/classes/Chat.md) would return `false` for the given
  sender and receiver.
- The user with the ID `toUserId` is not online on the current server.

This function will return immediately in most cases, although it will
yield if the target user has just joined the server and their filtering
info is not yet loaded.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `toUserId` | `int64` |  | [Player.UserId](/docs/reference/engine/classes/Player.md) of the user being chatted. |

**Returns:** `string` — Filtered text string.

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