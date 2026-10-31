---
name: IntegrityService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "A service that lets you decide how your experience responds to the device trust level of each player."
---

# Class: IntegrityService

> A service that lets you decide how your experience responds to the device
> trust level of each player.

## Description

`IntegrityService` exposes the API to measure the
[device trust level](/docs/en-us/scripting/security/device-trust.md) of every
player who joins your game. Roblox doesn't take any action based on the device
trust level; instead, you decide what it means for your experience, such as
rejecting players on untrusted devices, restricting sensitive features, or
sending players to a different place.

To accept or reject each player once their trust level is available, assign a
function to
[EvaluatePlayerDeviceTrust](/docs/reference/engine/classes/IntegrityService.md).
To read the trust level of a player at any time, use
[Player.DeviceTrustLevel](/docs/reference/engine/classes/Player.md).

The device trust level describes the player's device, not the player or their
account. **It doesn't tell you whether a player is cheating.** For code
samples and guidance on choosing a policy, see
[device trust](/docs/en-us/scripting/security/device-trust.md).

## Callbacks

### Callback: IntegrityService.EvaluatePlayerDeviceTrust

**Signature:** `IntegrityService.EvaluatePlayerDeviceTrust(player: Player, measures: Dictionary): PlayerDeviceTrustResult?`

This callback is called once for each player, as soon as their device
trust level is available. Use it to decide whether the player can stay in
the server, based on [Player.DeviceTrustLevel](/docs/reference/engine/classes/Player.md) and the `measures`
table.

Keep the following in mind when you assign this callback:

- You can only assign it from a server-side [Script](/docs/reference/engine/classes/Script.md). Assigning it
  from a client throws an error.
- Each place has one callback. If you assign it more than once, the last
  assignment replaces the earlier ones.
- It runs after [Players.PlayerAdded](/docs/reference/engine/classes/Players.md) fires, because checking the
  device takes time. When it runs, [Player.DeviceTrustLevel](/docs/reference/engine/classes/Player.md) is
  never [Pending](/docs/reference/engine/enums/PlayerDeviceTrustLevel.md).
- It can yield. The player keeps playing while it runs, so a rejected
  player can be disconnected after they've started playing.
- If the player leaves, or your scripts remove them, before their trust
  level is available, it isn't called for that player.
- Roblox doesn't check devices in Studio, so it isn't called during
  playtests.

Roblox filters a custom `Message` and shortens messages that are too long.
If filtering would change the message, Roblox shows the default message
instead.

Roblox doesn't kick the player in each of the following cases:

- No script assigns the callback.
- The callback returns `nil`, a value that isn't a table, or a table
  without a valid `Action`.
- The callback throws an error. Roblox reports the error like any other
  script error.
- The callback doesn't return in time.

For code samples, see
[device trust](/docs/en-us/scripting/security/device-trust.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Consequences*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) being evaluated. Their trust level is already set in [Player.DeviceTrustLevel](/docs/reference/engine/classes/Player.md) when this callback runs. |
| `measures` | `Dictionary` |  | A table of key-value pairs explaining the trust level of the player's device. A value of `true` means the device passed that measure:  - `IsPlatformVersionSecure` &mdash; The operating system is at or   above the minimum version that Roblox considers secure. - `IsPlatformBootSecure` &mdash; The operating system started in a   secure state. - `IsAppSecure` &mdash; The Roblox app hasn't been tampered with.  A measure that isn't available on the device reads `true`, so always check [Player.DeviceTrustLevel](/docs/reference/engine/classes/Player.md) as well. |

**Returns:** `PlayerDeviceTrustResult?` — A table that tells Roblox what to do with the player, or `nil` to keep
them:

- `Action` &mdash; Required. [PlayerDeviceTrustDecision.Reject](/docs/reference/engine/enums/PlayerDeviceTrustDecision.md)
  disconnects the player. [PlayerDeviceTrustDecision.Accept](/docs/reference/engine/enums/PlayerDeviceTrustDecision.md)
  keeps them.
- `Message` &mdash; Optional. The message that a rejected player sees.
  If you omit it, Roblox shows a default message that explains how the
  player might fix their device.

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