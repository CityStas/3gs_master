---
name: UserService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "A service that handles queries regarding users on the Roblox platform."
---

# Class: UserService

> A service that handles queries regarding users on the Roblox platform.

## Methods

### Method: UserService:GetUserInfosByUserIdsAsync

**Signature:** `UserService:GetUserInfosByUserIdsAsync(userIds: Array): Array`

This function lets you request information about users outside of the
current [DataModel](/docs/reference/engine/classes/DataModel.md) in bulk. The input and output values are both
arrays.

- The order of the user info objects in the return value's array may not
  match the order of the [UserIds](/docs/reference/engine/classes/Player.md) sent in the input
  parameter's array. Use the `Id` field of the user info object to
  identify your input array with the output array.
- It's possible to receive fewer user info objects than requested if one
  or more of the [UserIds](/docs/reference/engine/classes/Player.md) in the request array are
  invalid, such as negative numbers or user IDs that don't have accounts
  associated with them. It's possible to receive a response with zero
  results if all [UserIds](/docs/reference/engine/classes/Player.md) are invalid.
- If a Roblox user does not have a [DisplayName](/docs/reference/engine/classes/Player.md)
  associated with their account, this function will instead return the
  same string as the user's username in their info object's `DisplayName`
  field. While a user's [UserId](/docs/reference/engine/classes/Player.md) will never change,
  they may change their username or display name, so the same input
  [UserIds](/docs/reference/engine/classes/Player.md) may return a different string for these
  fields from one day to another.
- Since
  [GetUserInfosByUserIdsAsync()](/docs/reference/engine/classes/UserService.md)
  makes an external web request, it will yield and may fail if the backend
  service is experiencing interruptions. Ensure you can handle downtime
  appropriately by wrapping this method with a
  [LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md).
- Results are limited to 250 per minute, so if you receive an HTTP 429
  error, try again later, ideally after reducing the number of
  [UserIds](/docs/reference/engine/classes/Player.md) in your input array, reducing the number
  of method calls, or both.

The signature of a singular user info object is:

| Key | Type | Description |
| --- | --- | --- |
| `Id` | number | The [UserId](/docs/reference/engine/classes/Player.md) associated with the user. |
| `Username` | string | The username associated with the user. |
| `DisplayName` | string | The [DisplayName](/docs/reference/engine/classes/Player.md) associated with the user. |
| `HasVerifiedBadge` | boolean | The [HasVerifiedBadge](/docs/reference/engine/classes/Player.md) value associated with the user. |

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userIds` | `Array` |  | An array of [UserIds](/docs/reference/engine/classes/Player.md) requested. |

**Returns:** `Array` — An array of dictionary objects that contain user information.

**UserService:GetUserInfosByUserIdsAsync Example**

```lua
local UserService = game:GetService("UserService")

local success, result = pcall(function()
	return UserService:GetUserInfosByUserIdsAsync({ 156, 1, 735878936 })
end)

if success then
	for _, userInfo in ipairs(result) do
		print("Id:", userInfo.Id)
		print("Username:", userInfo.Username)
		print("DisplayName:", userInfo.DisplayName)
	end
else
	-- An error occurred
end
```

**Expected output:** Id: 156
Username: builderman
DisplayName: builderman
Id: 1
Username: Roblox
DisplayName: Roblox
Id: 735878936
Username: Cozecant
DisplayName: cozecant

### Method: UserService:GetUserFromGlobalUserIdAsync

**Signature:** `UserService:GetUserFromGlobalUserIdAsync(userId: int64): User`

Resolves a global user ID to a [User](/docs/reference/engine/datatypes/User.md) for the current experience
domain. Use this when you have a legacy global user ID (for example, one
previously saved in a data store) and need the corresponding
[User](/docs/reference/engine/datatypes/User.md) value.

This is a server-only yielding call.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `int64` |  | The global user ID to resolve. |

**Returns:** `User` — User: The [User](/docs/reference/engine/datatypes/User.md) representing the resolved domain-scoped
identity.

**Get User From Global User Id Async**

Demonstrates [UserService:GetUserFromGlobalUserIdAsync()](/docs/reference/engine/classes/UserService.md).

```lua
local UserService = game:GetService("UserService")

local user = UserService:GetUserFromGlobalUserIdAsync(globalUserId)
print(user.Id)         -- Domain user ID for this experience
print(user.DomainType) -- Enum.DomainType.EXPERIENCE
print(user.DomainId)   -- Current universe ID
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