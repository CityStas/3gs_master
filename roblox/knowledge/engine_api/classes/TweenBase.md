---
name: TweenBase
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotBrowsable
summary: "Abstract base class for in-between interpolation handlers. Tween inherits from TweenBase."
---

# Class: TweenBase

> Abstract base class for in-between interpolation handlers. [Tween](/docs/reference/engine/classes/Tween.md)
> inherits from [TweenBase](/docs/reference/engine/classes/TweenBase.md).

## Description

Abstract base class for in-between interpolation handlers; parent class of
[Tween](/docs/reference/engine/classes/Tween.md).

## Properties

### Property: TweenBase.PlaybackState

```json
{
  "type": "PlaybackState",
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
  "category": "Behavior"
}
```

Read-only property that shows the current stage for the [Tween](/docs/reference/engine/classes/Tween.md)
animation. See [PlaybackState](/docs/reference/engine/enums/PlaybackState.md) for descriptions of each state. Change
using functions like [Tween:Play()](/docs/reference/engine/classes/Tween.md).

**Tween PlaybackState**

In this example a part is rotated by a Tween back and forth several times. The
TweenInfo in this case is configured to make the tween repeat twice after the
first playback and pause between each playback. A function is connected to
when the tween's PlaybackState changes. When run, this function will fire
whenever the tween starts, pauses between playback, and ends.

```lua
local TweenService = game:GetService("TweenService")

local part = Instance.new("Part")
part.Position = Vector3.new(0, 10, 0)
part.Anchored = true
part.Parent = workspace

local goal = {}
goal.Orientation = Vector3.new(0, 90, 0)

local tweenInfo = TweenInfo.new(1, Enum.EasingStyle.Quad, Enum.EasingDirection.InOut, 2, true, 0.5)

local tween = TweenService:Create(part, tweenInfo, goal)

local function onPlaybackChanged()
	print("Tween status has changed to:", tween.PlaybackState)
end

local playbackChanged = tween:GetPropertyChangedSignal("PlaybackState")
playbackChanged:Connect(onPlaybackChanged)

tween:Play()
```

## Methods

### Method: TweenBase:Cancel

**Signature:** `TweenBase:Cancel(): ()`

Halts playback of a [Tween](/docs/reference/engine/classes/Tween.md) and resets the tween variables.

Only resets the tween variables, not the properties being changed by the
tween. If you cancel a tween halfway through its animation, the properties
do not reset to their original values. Differs from
[TweenBase:Pause()](/docs/reference/engine/classes/TweenBase.md) in that once resumed, it takes the full duration
of the tween to complete the animation.

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

**Tween Cancel**

This sample demonstrates the impact of cancelling a tween.

A part is instanced in the Workspace and a tween is set up to move it along
the Y axis. Mid way through the tween, it is cancelled. It can be observed
here that the part does not return to its original position, but when it is
resumed it takes the full length of the tween (5 seconds) to complete.

This is the key difference TweenBase:Pause() and TweenBase:Cancel().

```lua
local TweenService = game:GetService("TweenService")

local part = Instance.new("Part")
part.Position = Vector3.new(0, 10, 0)
part.Anchored = true
part.Parent = workspace

local goal = {}
goal.Position = Vector3.new(0, 50, 0)

local tweenInfo = TweenInfo.new(5)

local tween = TweenService:Create(part, tweenInfo, goal)

tween:Play()
task.wait(2.5)
tween:Cancel()

local playTick = tick()
tween:Play()

tween.Completed:Wait()

local timeTaken = tick() - playTick
print("Tween took " .. tostring(timeTaken) .. " secs to complete")

-- The tween will take 5 seconds to complete as the tween variables have been reset by tween:Cancel()
```

### Method: TweenBase:Pause

**Signature:** `TweenBase:Pause(): ()`

Halts playback of the tween. Doesn't reset its progress variables, meaning
that if you call [TweenBase:Play()](/docs/reference/engine/classes/TweenBase.md), the tween resumes playback from
the moment it was paused.

If you want to reset the progress variables of the tween, use
[TweenBase:Cancel()](/docs/reference/engine/classes/TweenBase.md).

You can only pause tweens that are in the
[PlaybackState](/docs/reference/engine/classes/TweenBase.md) of
[ PlaybackState.Playing](/docs/reference/engine/enums/.md); tweens in other states won't pause. If a
tween is in a different [PlaybackState](/docs/reference/engine/classes/TweenBase.md) such
as [ PlaybackState.Delayed](/docs/reference/engine/enums/.md) (as a result of its
[TweenInfo.DelayTime](/docs/reference/engine/datatypes/TweenInfo.md) being greater than 0), attempting to pause
the tween will fail and the tween will play following its specified delay
time.

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

**Pausing a Tween**

This sample demonstrates how the playback of a tween can be paused and
resumed.

A part is instanced in the Workspace and a tween is setup that will move it 50
studs along the X axis. However during playback the tween is briefly paused,
then resumed. To further illustrate this the BrickColor of the part changes
from red to green while it is paused.

```lua
local TweenService = game:GetService("TweenService")

local part = Instance.new("Part")
part.Position = Vector3.new(0, 10, 0)
part.Anchored = true
part.BrickColor = BrickColor.new("Bright green")
part.Parent = workspace

local goal = {}
goal.Position = Vector3.new(50, 10, 0)

local tweenInfo = TweenInfo.new(10, Enum.EasingStyle.Linear)

local tween = TweenService:Create(part, tweenInfo, goal)

tween:Play()

task.wait(3)
part.BrickColor = BrickColor.new("Bright red")
tween:Pause()

task.wait(2)
part.BrickColor = BrickColor.new("Bright green")
tween:Play()
```

### Method: TweenBase:Play

**Signature:** `TweenBase:Play(): ()`

Starts playback of a tween. Note that if playback has already started,
calling `Play()` has no effect unless the tween has finished or is stopped
(either by [TweenBase:Cancel()](/docs/reference/engine/classes/TweenBase.md) or [TweenBase:Pause()](/docs/reference/engine/classes/TweenBase.md)).

Multiple tweens can be played on the same object at the same time, but
they must not animate the same property. If two tweens attempt to modify
the same property, the initial tween is cancelled and overwritten by the
most recent tween (see examples).

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

**Tween Creation**

In this example a Tween is created to animate the position and color of a
Part. Because the position and color are part of the same tween, they will
change at the exact same rate and will reach their goal at the same time.

```lua
local TweenService = game:GetService("TweenService")

local part = Instance.new("Part")
part.Position = Vector3.new(0, 10, 0)
part.Color = Color3.new(1, 0, 0)
part.Anchored = true
part.Parent = game.Workspace

local goal = {}
goal.Position = Vector3.new(10, 10, 0)
goal.Color = Color3.new(0, 1, 0)

local tweenInfo = TweenInfo.new(5)

local tween = TweenService:Create(part, tweenInfo, goal)

tween:Play()
```

**Tween Conflict**

This code sample includes a demonstration of tween conflict. A part is
instanced in the Workspace, and two tweens are created that attempt to move
the part in conflicting directions.

When both tweens are played, the first tween is cancelled and overwritten by
the second tween. This can be seen as the part moves along the Y axis as
opposed to the Z axis.

To further demonstrate this, connections have been made for both tweens to the
Tween.Completed event. Upon playing the tweens, the following is printed.

tween1: Enum.PlaybackState.Cancelled tween2: Enum.PlaybackState.Completed

These prints show that the first tween was cancelled (firing the Completed
event) immediately upon the second tween being played. The second tween then
went on to play until completion.

```lua
local TweenService = game:GetService("TweenService")

local part = Instance.new("Part")
part.Position = Vector3.new(0, 10, 0)
part.Anchored = true
part.Parent = game.Workspace

local tweenInfo = TweenInfo.new(5)

-- create two conflicting tweens (both trying to animate part.Position)
local tween1 = TweenService:Create(part, tweenInfo, { Position = Vector3.new(0, 10, 20) })
local tween2 = TweenService:Create(part, tweenInfo, { Position = Vector3.new(0, 30, 0) })

-- listen for their completion status
tween1.Completed:Connect(function(playbackState)
	print("tween1: " .. tostring(playbackState))
end)
tween2.Completed:Connect(function(playbackState)
	print("tween2: " .. tostring(playbackState))
end)

-- try to play them both
tween1:Play()
tween2:Play()
```

## Events

### Event: TweenBase.Completed

**Signature:** `TweenBase.Completed(playbackState: PlaybackState)`

Fires when the tween finishes playing or when stopped with
[TweenBase:Cancel()](/docs/reference/engine/classes/TweenBase.md).

Passes the [PlaybackState](/docs/reference/engine/enums/PlaybackState.md) of the tween to any connected functions to
give an indication of why the tween ended. Note that calling
[TweenBase:Pause()](/docs/reference/engine/classes/TweenBase.md) does not fire the `Completed` event.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `playbackState` | `PlaybackState` | The [PlaybackState](/docs/reference/engine/enums/PlaybackState.md) of the tween upon completion. |

**Tween Completed**

In this example the walkspeed of any player joining the game will be slowed to
0 over 10 seconds using a Tween. The Completed event is used to reset the
walkspeed after the Tween has finished playing.

```lua
local Players = game:GetService("Players")
local TweenService = game:GetService("TweenService")

local SLOW_DURATION = 10

local function slowCharacter(humanoid)
	local goal = {}
	goal.WalkSpeed = 0

	local tweenInfo = TweenInfo.new(SLOW_DURATION)

	local tweenSpeed = TweenService:Create(humanoid, tweenInfo, goal)

	tweenSpeed:Play()

	return tweenSpeed
end

local function onCharacterAdded(character)
	local humanoid = character:WaitForChild("Humanoid")
	local initialSpeed = humanoid.WalkSpeed
	local tweenSpeed = slowCharacter(humanoid)
	tweenSpeed.Completed:Wait()
	humanoid.WalkSpeed = initialSpeed
end

local function onPlayerAdded(player)
	player.CharacterAdded:Connect(onCharacterAdded)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

**Tween Conflict**

This code sample includes a demonstration of tween conflict. A part is
instanced in the Workspace, and two tweens are created that attempt to move
the part in conflicting directions.

When both tweens are played, the first tween is cancelled and overwritten by
the second tween. This can be seen as the part moves along the Y axis as
opposed to the Z axis.

To further demonstrate this, connections have been made for both tweens to the
Tween.Completed event. Upon playing the tweens, the following is printed.

tween1: Enum.PlaybackState.Cancelled tween2: Enum.PlaybackState.Completed

These prints show that the first tween was cancelled (firing the Completed
event) immediately upon the second tween being played. The second tween then
went on to play until completion.

```lua
local TweenService = game:GetService("TweenService")

local part = Instance.new("Part")
part.Position = Vector3.new(0, 10, 0)
part.Anchored = true
part.Parent = game.Workspace

local tweenInfo = TweenInfo.new(5)

-- create two conflicting tweens (both trying to animate part.Position)
local tween1 = TweenService:Create(part, tweenInfo, { Position = Vector3.new(0, 10, 20) })
local tween2 = TweenService:Create(part, tweenInfo, { Position = Vector3.new(0, 30, 0) })

-- listen for their completion status
tween1.Completed:Connect(function(playbackState)
	print("tween1: " .. tostring(playbackState))
end)
tween2.Completed:Connect(function(playbackState)
	print("tween2: " .. tostring(playbackState))
end)

-- try to play them both
tween1:Play()
tween2:Play()
```

**Verifying a Tween has Completed**

This code sample includes an example of how Tween.Completed can be used to
determine if a Tween has been successfully completed, or cancelled.

In this case a part is instanced and tweened towards 0, 0, 0. Once the tween
has completed, if the final PlaybackState is Completed then the part will
explode. Were the tween to be cancelled prior to completion, the explosion
would not be created.

This method can be used to link tweens to other effects, or even chain several
tweens to play after each other.

```lua
local TweenService = game:GetService("TweenService")

local part = Instance.new("Part")
part.Position = Vector3.new(0, 50, 0)
part.Anchored = true
part.Parent = workspace

local goal = {}
goal.Position = Vector3.new(0, 0, 0)

local tweenInfo = TweenInfo.new(3)

local tween = TweenService:Create(part, tweenInfo, goal)

local function onTweenCompleted(playbackState)
	if playbackState == Enum.PlaybackState.Completed then
		local explosion = Instance.new("Explosion")
		explosion.Position = part.Position
		explosion.Parent = workspace
		part:Destroy()
		task.delay(2, function()
			if explosion then
				explosion:Destroy()
			end
		end)
	end
end

tween.Completed:Connect(onTweenCompleted)

tween:Play()
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