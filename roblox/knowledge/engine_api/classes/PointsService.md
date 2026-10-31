---
name: PointsService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - Deprecated
summary: "This service controls the points award system used to showcase a player's achievements and participation throughout Roblox."
---

# Class: PointsService

> This service controls the points award system used to showcase a player's
> achievements and participation throughout Roblox.

## Description

The PointsService class controls points.

Points are an award system used to showcase a player's achievements and
participation throughout Roblox. How points are awarded through this service
is at the discretion of the game's developer.

## Methods

### Method: PointsService:AwardPoints

**Signature:** `PointsService:AwardPoints(userId: int64, amount: int): Tuple`

> **Deprecated:** This function was once part of the `PointService` class used to control an ancient achievement system since removed and deprecated. It should not be used in new work.

This function attempts to award the user with the specified
[Player.UserId](/docs/reference/engine/classes/Player.md) the specified number of points.

If successful, this function will return the UserId of the user the points
were awarded to, the number of points awarded, the new total number of
points the user has in the game and another value which appears to always
be 0.

This function will cause an error if the specified UserId is not positive
or if the number of points specified is 0.

The function can be used to award a negative number of points to a user
however.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `int64` |  |  |
| `amount` | `int` |  |  |

**Returns:** `Tuple`

**PointsService:AwardPoints**

The below example would attempt to award 5 points to the Roblox account. If
the account had been awarded 10 points before, it would print "The user was
awarded 5 points. They have now a total of 15 points in this game.".

```lua
local PointsService = game:GetService("PointsService")

local userId, amount, total = PointsService:AwardPoints(1, 5)

print("User", userId, "was awarded", amount, "points. They have now have a total of", total, "points in this game.")
```

**Award Points**

Demonstrates [PointsService:AwardPoints()](/docs/reference/engine/classes/PointsService.md).

```lua
local userId, amount, total = game:GetService("PointsService"):AwardPoints(1, 5)
print("The user was awarded " ..amount.. " points. They have now have a total of " ..total.. " points in this game.")
```

### Method: PointsService:GetAwardablePoints

**Signature:** `PointsService:GetAwardablePoints(): int`

> **Deprecated:** This function was once part of the `PointService` class used to control an ancient achievement system since removed and deprecated. It should not be used in new work.

This function returns the number of points the current game has available
to award to players.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `int`

### Method: PointsService:GetGamePointBalance

**Signature:** `PointsService:GetGamePointBalance(userId: int64): int`

> **Deprecated:** This function was once part of the `PointService` class used to control an ancient achievement system since removed and deprecated. It should not be used in new work.

This function returns the total number of points a player has in the
current game.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `int64` |  |  |

**Returns:** `int`

### Method: PointsService:GetPointBalance

**Signature:** `PointsService:GetPointBalance(userId: int64): int`

> **Deprecated:** This function was once part of the `PointService` class used to control an ancient achievement system since removed and deprecated. It should not be used in new work.

This function returns the total number of points the given player has
across **_all_** games.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `int64` |  |  |

**Returns:** `int`

## Events

### Event: PointsService.PointsAwarded

**Signature:** `PointsService.PointsAwarded(userId: int64, pointsAwarded: int, userBalanceInGame: int, userTotalBalance: int)`

This event fires when points have been successfully awarded to a player,
while also passing along the updated balance of points the player has in
the current game and all games.

When a player is awarded points successfully the below example would print
the userId and their new point balance. If, for example, the Roblox
account was awarded thirty points (and had none to begin with)

> User: 1 has now earned 30 (+30) points in the current game, now making
> their total balance

would be printed.

*Security: None · Capabilities: Basic*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `userId` | `int64` |  |
| `pointsAwarded` | `int` |  |
| `userBalanceInGame` | `int` |  |
| `userTotalBalance` | `int` |  |

**PointsService.PointsAwarded**

When a player is awarded points successfully the below example would print the
userId and their new point balance. If, for example, the Roblox account was
awarded thirty points (and had none to begin with) "User: 1 has now earned 30
(+30) points in the current game, now making their total balance 30" would be
printed.

```lua
local PointsService = game:GetService("PointsService")

local function onPointsAwarded(userId, pointsAwarded, userBalanceInGame, userTotalBalance)
	print(
		"User:",
		userId,
		"has now earned",
		userBalanceInGame,
		"(+",
		pointsAwarded,
		") points in the current game, now making their total balance",
		userTotalBalance
	)
end

PointsService.PointsAwarded:Connect(onPointsAwarded)
```

**Points Awarded**

Demonstrates [PointsService:PointsAwarded()](/docs/reference/engine/classes/PointsService.md).

```lua
local function pointsAwarded(userId, pointsAwarded, userBalanceInGame, userTotalBalance)
	print("User: " .. userId .. " has now earned " .. userBalanceInGame .. " (+" .. pointsAwarded ..") points in the current game, now making their total balance " .. userTotalBalance)
end

game:GetService("PointsService").PointsAwarded:Connect(pointsAwarded)
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