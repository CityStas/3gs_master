---
name: AnimationTrack
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Animation
tags:
  - NotCreatable
summary: "Controls the playback of an animation on an Animator."
---

# Class: AnimationTrack

> Controls the playback of an animation on an [Animator](/docs/reference/engine/classes/Animator.md).

## Description

Controls the playback of an animation on an [Animator](/docs/reference/engine/classes/Animator.md). This object
cannot be created, instead it is returned by the
[Animator:LoadAnimation()](/docs/reference/engine/classes/Animator.md) method.

## Properties

### Property: AnimationTrack.Animation

```json
{
  "type": "Animation",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Animation"
  ]
}
```

The [Animation](/docs/reference/engine/classes/Animation.md) object that was used to create this
[AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md). To create an [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md), you must load
an [Animation](/docs/reference/engine/classes/Animation.md) object onto an [Animator](/docs/reference/engine/classes/Animator.md) using the
[Animator:LoadAnimation()](/docs/reference/engine/classes/Animator.md) method.

**Listen For New Animations**

The following code sample prints the name of an animation whenever an
[AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) plays on a [Humanoid](/docs/reference/engine/classes/Humanoid.md). This script can be placed
in a model with a [Humanoid](/docs/reference/engine/classes/Humanoid.md) child.

```lua
local humanoid = script.Parent:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")

animator.AnimationPlayed:Connect(function(animationTrack)
	local animationName = animationTrack.Animation.Name
	print("Animation playing " .. animationName)
end)
```

### Property: AnimationTrack.IsPlaying

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Animation"
  ],
  "simulationAccess": true
}
```

A read-only property that returns true when the [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) is
playing.

This property can be used to check if an animation is already playing
before playing it (as that would cause it to restart). If you want to
obtain all playing [AnimationTracks](/docs/reference/engine/classes/AnimationTrack.md) on an
[Animator](/docs/reference/engine/classes/Animator.md) or a [Humanoid](/docs/reference/engine/classes/Humanoid.md), they should use
[Animator:GetPlayingAnimationTracks()](/docs/reference/engine/classes/Animator.md)

**AnimationTrack IsPlaying**

This code sample includes a simple function that will play an AnimationTrack
if it is not playing, or otherwise adjust its speed and weight to match the
new parameters given.

```lua
local function playOrAdjust(animationTrack, fadeTime, weight, speed)
	if not animationTrack.IsPlaying then
		animationTrack:Play(fadeTime, weight, speed)
	else
		animationTrack:AdjustSpeed(speed)
		animationTrack:AdjustWeight(weight, fadeTime)
	end
end

local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://507765644"

local humanoid = script.Parent:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")
local animationTrack = animator:LoadAnimation(animation)

playOrAdjust(animationTrack, 1, 0.6, 1)
```

### Property: AnimationTrack.Length

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Animation"
  ]
}
```

A read-only property that returns the length (in seconds) of an
[AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md). This will return `0` until the animation has fully
loaded and thus may not be immediately available.

When the [AnimationTrack.Speed](/docs/reference/engine/classes/AnimationTrack.md) of an [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) is
equal to `1`, the animation will take [AnimationTrack.Length](/docs/reference/engine/classes/AnimationTrack.md) (in
seconds) to complete.

**Playing Animation for a Specific Duration**

The following function will play an AnimationTrack for a specific duration.
This is done by changing the speed of the animation to the length of the
animation divided by the desired playback duration. This could be used in
situations where a developer wants to play a standard animation for different
duration (for example, recharging different abilities).

```lua
local function playAnimationForDuration(animationTrack, duration)
	local speed = animationTrack.Length / duration
	animationTrack:Play()
	animationTrack:AdjustSpeed(speed)
end

local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://507765000"

local humanoid = script.Parent:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")

local animationTrack = animator:LoadAnimation(animation)

playAnimationForDuration(animationTrack, 3)
```

### Property: AnimationTrack.Looped

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Animation"
  ],
  "simulationAccess": true
}
```

This property sets whether the animation will repeat after finishing. If
it is changed while playing the result will take effect after the
animation finishes.

This property defaults to how it was set in the
[Animation Editor](/docs/en-us/animation/editor.md). However, this property
can be changed, allowing control over the [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) while it
is running. This property also correctly handles animations played in
reverse (negative [AnimationTrack.Speed](/docs/reference/engine/classes/AnimationTrack.md)). After the first keyframe
is reached, it will restart at the last keyframe.

**Animation Looping**

The animation in this example normally loops. After the player and the
animation are loaded the animation is played in a non-looped fashion then in a
looped fashion.

```lua
local Players = game:GetService("Players")

local localPlayer = Players.LocalPlayer

while not localPlayer.Character do
	task.wait()
end

local character = localPlayer.Character
local humanoid = character:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")

local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://507770453"

local animationTrack = animator:LoadAnimation(animation)
animationTrack.Looped = false
task.wait(3)
animationTrack:Play()
task.wait(4)
animationTrack.Looped = true
animationTrack:Play()
```

**Play AnimationTrack for a Number of Loops**

The function in this code sample will play an AnimationTrack on a loop, for a
specific number of loops, before stopping the animation.

In some cases the developer may want to stop a looped animation after a
certain number of loops have completed, rather than after a certain amount of
time. This is where the DidLoop event can be used.

```lua
local function playForNumberLoops(animationTrack, number)
	animationTrack.Looped = true
	animationTrack:Play()
	local numberOfLoops = 0
	local connection = nil
	connection = animationTrack.DidLoop:Connect(function()
		numberOfLoops = numberOfLoops + 1
		print("loop: ", numberOfLoops)
		if numberOfLoops >= number then
			animationTrack:Stop()
			connection:Disconnect() -- it's important to disconnect connections when they are no longer needed
		end
	end)
end

local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://507765644"

local humanoid = script.Parent:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")
local animationTrack = animator:LoadAnimation(animation)

playForNumberLoops(animationTrack, 5)
```

### Property: AnimationTrack.Priority

```json
{
  "type": "AnimationPriority",
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
    "Animation"
  ],
  "simulationAccess": true
}
```

This property sets the priority of an [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md). Depending on
what this is set to, playing multiple animations at once will look to this
property to figure out which [Keyframe](/docs/reference/engine/classes/Keyframe.md) poses should be played over
one another. It uses [AnimationPriority](/docs/reference/engine/enums/AnimationPriority.md) which has 7 priority levels:

1. [Action4](/docs/reference/engine/enums/AnimationPriority.md) (highest priority)
2. [Action3](/docs/reference/engine/enums/AnimationPriority.md)
3. [Action2](/docs/reference/engine/enums/AnimationPriority.md)
4. [Action](/docs/reference/engine/enums/AnimationPriority.md)
5. [Movement](/docs/reference/engine/enums/AnimationPriority.md)
6. [Idle](/docs/reference/engine/enums/AnimationPriority.md)
7. [Core](/docs/reference/engine/enums/AnimationPriority.md) (lowest priority)

Properly set animation priorities, either through the
[Animation Editor](/docs/en-us/animation/editor.md) or through this property,
allow multiple animations to be played without them clashing. Where two
playing animations direct the target to move the same limb in different
ways, the [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) with the highest priority will show. If
both animations have the same priority, the weights of the tracks will be
used to combine the animations.

### Property: AnimationTrack.Speed

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Animation"
  ],
  "simulationAccess": true
}
```

This read-only property gives the current playback speed of the
[AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md). When equal to `1`, the amount of time an animation
takes to complete is equal to [AnimationTrack.Length](/docs/reference/engine/classes/AnimationTrack.md), in seconds.

If the speed is adjusted through [AnimationTrack:AdjustSpeed()](/docs/reference/engine/classes/AnimationTrack.md), the
actual time it will take a track to play can be computed by dividing the
length by the speed. Speed is a unitless quantity.

**Animation Speed**

In this example a player and an animation is loaded. The Length of an
AnimationTrack determines how long the track would take to play if the speed
is at 1. If the speed is adjusted, then the actual time it will take a track
to play can be computed by dividing the length by the speed.

```lua
local ContentProvider = game:GetService("ContentProvider")
local Players = game:GetService("Players")

local localPlayer = Players.LocalPlayer
while not localPlayer.Character do
	task.wait()
end
local character = localPlayer.Character
local humanoid = character:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")
local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://507770453"

ContentProvider:PreloadAsync({ animation })

local animationTrack = animator:LoadAnimation(animation)

local normalSpeedTime = animationTrack.Length / animationTrack.Speed
animationTrack:AdjustSpeed(3)
local fastSpeedTime = animationTrack.Length / animationTrack.Speed

print("At normal speed the animation will play for", normalSpeedTime, "seconds")
print("At 3x speed the animation will play for", fastSpeedTime, "seconds")
```

**Playing Animation for a Specific Duration**

The following function will play an AnimationTrack for a specific duration.
This is done by changing the speed of the animation to the length of the
animation divided by the desired playback duration. This could be used in
situations where a developer wants to play a standard animation for different
duration (for example, recharging different abilities).

```lua
local function playAnimationForDuration(animationTrack, duration)
	local speed = animationTrack.Length / duration
	animationTrack:Play()
	animationTrack:AdjustSpeed(speed)
end

local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://507765000"

local humanoid = script.Parent:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")

local animationTrack = animator:LoadAnimation(animation)

playAnimationForDuration(animationTrack, 3)
```

### Property: AnimationTrack.TimePosition

```json
{
  "type": "float",
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
  "category": "Data",
  "capabilities": [
    "Animation"
  ],
  "simulationAccess": true
}
```

Returns the position in time in seconds that an [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) is
through playing its source animation. Can be set to make the track jump to
a specific moment in the animation, but the [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) must be
playing to do so. It can also be used in combination with
[AnimationTrack:AdjustSpeed()](/docs/reference/engine/classes/AnimationTrack.md) to freeze the animation at a desired
point by setting speed to `0`.

**Freeze Animation at Position**

The following code sample includes two functions that demonstrate how
AdjustSpeed and TimePosition can be used to freeze an animation at a
particular point.

The first function freezes an animation at a particular point in time (defined
in seconds). The second freezes at it at a percentage (between 0 or 100) by
multiplying the percentage by the track length.

As TimePosition can not be used when an AnimationTrack is not playing, the
functions check to make sure the animation is playing before proceeding.

```lua
function freezeAnimationAtTime(animationTrack, timePosition)
	if not animationTrack.IsPlaying then
		-- Play the animation if it is not playing
		animationTrack:Play()
	end
	-- Set the speed to 0 to freeze the animation
	animationTrack:AdjustSpeed(0)
	-- Jump to the desired TimePosition
	animationTrack.TimePosition = timePosition
end

function freezeAnimationAtPercent(animationTrack, percentagePosition)
	if not animationTrack.IsPlaying then
		-- Play the animation if it is not playing
		animationTrack:Play()
	end
	-- Set the speed to 0 to freeze the animation
	animationTrack:AdjustSpeed(0)
	-- Jump to the desired TimePosition
	animationTrack.TimePosition = (percentagePosition / 100) * animationTrack.Length
end

local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://507765644"

local humanoid = script.Parent:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")
local animationTrack = animator:LoadAnimation(animation)

freezeAnimationAtTime(animationTrack, 0.5)
freezeAnimationAtPercent(animationTrack, 50)
```

### Property: AnimationTrack.WeightCurrent

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Animation"
  ],
  "simulationAccess": true
}
```

When weight is set in an [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) it does not change
instantaneously but moves from [AnimationTrack.WeightCurrent](/docs/reference/engine/classes/AnimationTrack.md) to
[AnimationTrack.WeightTarget](/docs/reference/engine/classes/AnimationTrack.md). The time it takes to do this is
determined by the `fadeTime` parameter given when the animation is played,
or the weight is adjusted.

[AnimationTrack.WeightCurrent](/docs/reference/engine/classes/AnimationTrack.md) can be checked against
[AnimationTrack.WeightTarget](/docs/reference/engine/classes/AnimationTrack.md) to see if the desired weight has been
reached. Note that these values should not be checked for equality with
the `==` operator, as both of these values are floats. To see if
[AnimationTrack.WeightCurrent](/docs/reference/engine/classes/AnimationTrack.md) has reached the target weight, it is
recommended to see if the distance between those values is sufficiently
small.

**WeightCurrent and WeightTarget**

This code sample loads two animations onto the local player's Humanoid and
demonstrates how the fadeTime paramater in AnimationTrack.Play determines how
long it takes for an AnimationTrack's WeightCurrent to reach it's
WeightTarget.

As WeightCurrent and WeightTarget are floats the == operator cannot be used to
compare, instead it is more appropriate to check that the difference between
them is sufficiently small to assume the weight fade has completed.

```lua
local Players = game:GetService("Players")

local localPlayer = Players.LocalPlayer

while not localPlayer.Character do
	task.wait()
end
local character = localPlayer.Character

local humanoid = character:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")

local animation1 = Instance.new("Animation")
animation1.AnimationId = "rbxassetid://507770453"

local animation2 = Instance.new("Animation")
animation2.AnimationId = "rbxassetid://507771019"

task.wait(3) -- arbitrary wait time to allow the character to fall into place

local animationTrack1 = animator:LoadAnimation(animation1)
local animationTrack2 = animator:LoadAnimation(animation2)

animationTrack1.Priority = Enum.AnimationPriority.Movement
animationTrack2.Priority = Enum.AnimationPriority.Action

animationTrack1:Play(0.1, 5, 1)
animationTrack2:Play(10, 3, 1)

local done = false
while not done and task.wait(0.1) do
	if math.abs(animationTrack2.WeightCurrent - animationTrack2.WeightTarget) < 0.001 then
		print("got there")
		done = true
	end
end
```

### Property: AnimationTrack.WeightTarget

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Animation"
  ],
  "simulationAccess": true
}
```

This read-only property gives the current weight of the
[AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md). It has a default value of `1` and is set when
[AnimationTrack:Play()](/docs/reference/engine/classes/AnimationTrack.md), [AnimationTrack:Stop()](/docs/reference/engine/classes/AnimationTrack.md) or
[AnimationTrack:AdjustWeight()](/docs/reference/engine/classes/AnimationTrack.md) is called. When weight is set in an
[AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) it does not change instantaneously but moves from
[AnimationTrack.WeightCurrent](/docs/reference/engine/classes/AnimationTrack.md) to
[AnimationTrack.WeightTarget](/docs/reference/engine/classes/AnimationTrack.md). The time it takes to do this is
determined by the `fadeTime` parameter given when the animation is played,
or the weight is adjusted.

[AnimationTrack.WeightCurrent](/docs/reference/engine/classes/AnimationTrack.md) can be checked against
[AnimationTrack.WeightTarget](/docs/reference/engine/classes/AnimationTrack.md) to see if the desired weight has been
reached. Note that these values should not be checked for equality with
the `==` operator, as both of these values are floats. To see if
[AnimationTrack.WeightCurrent](/docs/reference/engine/classes/AnimationTrack.md) has reached the target weight, it is
recommended to see if the distance between those values is sufficiently
small.

**WeightCurrent and WeightTarget**

This code sample loads two animations onto the local player's Humanoid and
demonstrates how the fadeTime paramater in AnimationTrack.Play determines how
long it takes for an AnimationTrack's WeightCurrent to reach it's
WeightTarget.

As WeightCurrent and WeightTarget are floats the == operator cannot be used to
compare, instead it is more appropriate to check that the difference between
them is sufficiently small to assume the weight fade has completed.

```lua
local Players = game:GetService("Players")

local localPlayer = Players.LocalPlayer

while not localPlayer.Character do
	task.wait()
end
local character = localPlayer.Character

local humanoid = character:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")

local animation1 = Instance.new("Animation")
animation1.AnimationId = "rbxassetid://507770453"

local animation2 = Instance.new("Animation")
animation2.AnimationId = "rbxassetid://507771019"

task.wait(3) -- arbitrary wait time to allow the character to fall into place

local animationTrack1 = animator:LoadAnimation(animation1)
local animationTrack2 = animator:LoadAnimation(animation2)

animationTrack1.Priority = Enum.AnimationPriority.Movement
animationTrack2.Priority = Enum.AnimationPriority.Action

animationTrack1:Play(0.1, 5, 1)
animationTrack2:Play(10, 3, 1)

local done = false
while not done and task.wait(0.1) do
	if math.abs(animationTrack2.WeightCurrent - animationTrack2.WeightTarget) < 0.001 then
		print("got there")
		done = true
	end
end
```

## Methods

### Method: AnimationTrack:AdjustSpeed

**Signature:** `AnimationTrack:AdjustSpeed(speed?: float): ()`

This method changes the [AnimationTrack.Speed](/docs/reference/engine/classes/AnimationTrack.md) of an animation. A
positive value for speed plays the animation forward, a negative one plays
it backwards, and `0` pauses it.

A track's initial speed is set as a parameter in
[AnimationTrack:Play()](/docs/reference/engine/classes/AnimationTrack.md). However a track's
[AnimationTrack.Speed](/docs/reference/engine/classes/AnimationTrack.md) can be changed during playback using this
method. When speed is equal to `1`, the amount of time an animation takes
to complete is equal to [AnimationTrack.Length](/docs/reference/engine/classes/AnimationTrack.md) (in seconds).

When is adjusted, then the actual time it will take a track to play can be
computed by dividing the length by the speed. [AnimationTrack.Speed](/docs/reference/engine/classes/AnimationTrack.md)
is a unitless quantity.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `speed` | `float` | `1` | The playback speed the animation is to be changed to. |

**Returns:** `()`

**Playing Animation for a Specific Duration**

The following function will play an AnimationTrack for a specific duration.
This is done by changing the speed of the animation to the length of the
animation divided by the desired playback duration. This could be used in
situations where a developer wants to play a standard animation for different
duration (for example, recharging different abilities).

```lua
local function playAnimationForDuration(animationTrack, duration)
	local speed = animationTrack.Length / duration
	animationTrack:Play()
	animationTrack:AdjustSpeed(speed)
end

local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://507765000"

local humanoid = script.Parent:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")

local animationTrack = animator:LoadAnimation(animation)

playAnimationForDuration(animationTrack, 3)
```

**Animation Speed**

In this example a player and an animation is loaded. The Length of an
AnimationTrack determines how long the track would take to play if the speed
is at 1. If the speed is adjusted, then the actual time it will take a track
to play can be computed by dividing the length by the speed.

```lua
local ContentProvider = game:GetService("ContentProvider")
local Players = game:GetService("Players")

local localPlayer = Players.LocalPlayer
while not localPlayer.Character do
	task.wait()
end
local character = localPlayer.Character
local humanoid = character:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")
local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://507770453"

ContentProvider:PreloadAsync({ animation })

local animationTrack = animator:LoadAnimation(animation)

local normalSpeedTime = animationTrack.Length / animationTrack.Speed
animationTrack:AdjustSpeed(3)
local fastSpeedTime = animationTrack.Length / animationTrack.Speed

print("At normal speed the animation will play for", normalSpeedTime, "seconds")
print("At 3x speed the animation will play for", fastSpeedTime, "seconds")
```

### Method: AnimationTrack:AdjustWeight

**Signature:** `AnimationTrack:AdjustWeight(weight?: float, fadeTime?: float): ()`

Changes the weight of an animation, with the optional `fadeTime` parameter
determining how long it takes for [AnimationTrack.WeightCurrent](/docs/reference/engine/classes/AnimationTrack.md) to
reach [AnimationTrack.WeightTarget](/docs/reference/engine/classes/AnimationTrack.md).

When weight is set in an [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) it does not change
instantaneously but moves from [AnimationTrack.WeightCurrent](/docs/reference/engine/classes/AnimationTrack.md) to
[AnimationTrack.WeightTarget](/docs/reference/engine/classes/AnimationTrack.md). The time it takes to do this is
determined by the `fadeTime` parameter given when the animation is played,
or the weight is adjusted.

The animation weighting system is used to determine how
[AnimationTracks](/docs/reference/engine/classes/AnimationTrack.md) playing at the same priority are
blended together. The default weight is `1`, and no movement will be
visible on an [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) with a weight of `0`. The pose that
is shown at any point in time is determined by the weighted average of all
the [Poses](/docs/reference/engine/classes/Pose.md) and the [AnimationTrack.WeightCurrent](/docs/reference/engine/classes/AnimationTrack.md) of
each [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md). See below for an example of animation
blending in practice. In most cases blending animations is not required
and using [AnimationTrack.Priority](/docs/reference/engine/classes/AnimationTrack.md) is more suitable.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `weight` | `float` | `1` | The weight the animation is to be changed to. |
| `fadeTime` | `float` | `0.100000001` | The duration of time that the animation will fade between the old weight and the new weight for. |

**Returns:** `()`

**AnimationTrack Change Weight**

This code sample includes a function that changes the weight of an
AnimationTrack and yields until the weight has changed to the new target
weight.

The purpose of this sample is to demonstrate how the fadeTime parameter of
AnimationTrack.AdjustWeight works. In most cases, if a developer wishes to
yield over the fadeTime it is recommended they use wait(fadeTime).

```lua
local function changeWeight(animationTrack, weight, fadeTime)
	animationTrack:AdjustWeight(weight, fadeTime)
	local startTime = tick()
	while math.abs(animationTrack.WeightCurrent - weight) > 0.001 do
		task.wait()
	end
	print("Time taken to change weight " .. tostring(tick() - startTime))
end

local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://507765644"

local humanoid = script.Parent:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")
local animationTrack = animator:LoadAnimation(animation)

changeWeight(animationTrack, 0.6, 1)
```

### Method: AnimationTrack:GetMarkerReachedSignal

**Signature:** `AnimationTrack:GetMarkerReachedSignal(name: string): RBXScriptSignal`

This method returns an [RBXScriptSignal](/docs/reference/engine/datatypes/RBXScriptSignal.md) (event) similar to the
[AnimationTrack.KeyframeReached](/docs/reference/engine/classes/AnimationTrack.md) event, except it only fires when a
specified [KeyframeMarker](/docs/reference/engine/classes/KeyframeMarker.md) has been hit in an
[animation](/docs/reference/engine/classes/Animation.md). The difference allows for greater control of
when the event will fire.

To learn more about using this method, see
[here](/docs/en-us/animation/events.md).

#### See Also

- [KeyframeMarker](/docs/reference/engine/classes/KeyframeMarker.md)
- [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md), controls the playback of an animation on a
  [Humanoid](/docs/reference/engine/classes/Humanoid.md) or [AnimationController](/docs/reference/engine/classes/AnimationController.md)
- [Keyframe](/docs/reference/engine/classes/Keyframe.md), holds the [Poses](/docs/reference/engine/classes/Pose.md) applied to joints in a
  [Model](/docs/reference/engine/classes/Model.md) at a given point of time in an animation
- [Keyframe:AddMarker()](/docs/reference/engine/classes/Keyframe.md)
- [Keyframe:RemoveMarker()](/docs/reference/engine/classes/Keyframe.md)
- [Keyframe:GetMarkers()](/docs/reference/engine/classes/Keyframe.md)

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The name of the [KeyframeMarker](/docs/reference/engine/classes/KeyframeMarker.md) the signal is being created for. Not to be confused with the name of the [Keyframe](/docs/reference/engine/classes/Keyframe.md). |

**Returns:** `RBXScriptSignal` — The signal created and fired when the animation reaches the created
[KeyframeMarker](/docs/reference/engine/classes/KeyframeMarker.md).

**Listening to Keyframe Markers**

This `LocalScript` code waits for the local player's `Humanoid` object to
load, then it creates a new `Animation` instance with the proper
[Animation.AnimationId](/docs/reference/engine/classes/Animation.md). The animation is then loaded onto the humanoid,
creating an `AnimationTrack`, and the track is played with
[AnimationTrack:Play()](/docs/reference/engine/classes/AnimationTrack.md). Following that, the
[AnimationTrack:GetMarkerReachedSignal()](/docs/reference/engine/classes/AnimationTrack.md) function detects when the
"KickEnd" marker is hit.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local character = player.Character or player.Character:Wait()
local humanoid = character:WaitForChild("Humanoid")

-- Create new "Animation" instance
local kickAnimation = Instance.new("Animation")
-- Set its "AnimationId" to the corresponding animation asset ID
kickAnimation.AnimationId = "rbxassetid://2515090838"

-- Load animation onto the humanoid
local kickAnimationTrack = humanoid:LoadAnimation(kickAnimation)

-- Play animation track
kickAnimationTrack:Play()

-- If a named event was defined for the animation, connect it to "GetMarkerReachedSignal()"
kickAnimationTrack:GetMarkerReachedSignal("KickEnd"):Connect(function(paramString)
	print(paramString)
end)
```

### Method: AnimationTrack:GetParameter

**Signature:** `AnimationTrack:GetParameter(key: string): Variant`

Returns the value of a parameter on the animation graph by key. If the
parameter has not been set via [AnimationTrack:SetParameter()](/docs/reference/engine/classes/AnimationTrack.md), this
method returns nil.

Parameters are used to drive inputs on animation graph nodes. Use this
method to read back the current value of a parameter that was previously
set with [AnimationTrack:SetParameter()](/docs/reference/engine/classes/AnimationTrack.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Animation · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The name of the parameter to retrieve. |

**Returns:** `Variant` — The current value of the parameter, or nil if not set.

### Method: AnimationTrack:GetParameterDefaults

**Signature:** `AnimationTrack:GetParameterDefaults(): Dictionary`

Returns a dictionary of default parameter values defined by the animation
graph. This can be used to discover what parameters are available on an
animation graph and their initial values.

If the underlying [Animation](/docs/reference/engine/classes/Animation.md) is not an animation graph, this method
returns an empty dictionary.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Returns:** `Dictionary` — A dictionary mapping parameter names to their default values. Returns
an empty dictionary if the animation is not an animation graph.

### Method: AnimationTrack:GetTimeOfKeyframe

**Signature:** `AnimationTrack:GetTimeOfKeyframe(keyframeName: string): double`

Returns the time position of the first [Keyframe](/docs/reference/engine/classes/Keyframe.md) of the given name
in an [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md). If multiple [Keyframes](/docs/reference/engine/classes/Keyframe.md) share
the same name, it will return the earliest one in the animation.

This method will return an error if it is uses with an invalid keyframe
name (one that does not exist for example) or if the underlying
[Animation](/docs/reference/engine/classes/Animation.md) has not yet loaded. To address this make sure only
correct keyframe names are used and the animation has loaded before
calling this method.

To check if the animation has loaded, verify that the
[AnimationTrack.Length](/docs/reference/engine/classes/AnimationTrack.md) is greater than zero.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `keyframeName` | `string` |  | The name associated with the [Keyframe](/docs/reference/engine/classes/Keyframe.md) to be found. |

**Returns:** `double` — The time, in seconds, the [Keyframe](/docs/reference/engine/classes/Keyframe.md) occurs at normal playback
speed.

**Jump To Keyframe**

This sample includes a function that will jump to the first keyframe of a
specified name in an AnimationTrack.

As AnimationTrack.TimePosition cannot be set while the animation is not
playing the function first checks to see if the animation is playing.

This sample will only work once an Animation has loaded.

```lua
local function jumpToKeyframe(animationTrack, keyframeName)
	local timePosition = animationTrack:GetTimeOfKeyframe(keyframeName)
	if not animationTrack.IsPlaying then
		animationTrack:Play()
	end
	animationTrack.TimePosition = timePosition
end

local ANIMATION_ID = 0
local KEYFRAME_NAME = "Test"

local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://" .. ANIMATION_ID

local humanoid = script.Parent:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")
local animationTrack = animator:LoadAnimation(animation)

jumpToKeyframe(animationTrack, KEYFRAME_NAME)
```

### Method: AnimationTrack:Play

**Signature:** `AnimationTrack:Play(fadeTime?: float, weight?: float, speed?: float): ()`

When [AnimationTrack:Play()](/docs/reference/engine/classes/AnimationTrack.md) is called the track's animation will
begin playing and the weight of the animation will increase from `0` to
the specified `weight` (defaults to `1`) over the specified `fadeTime`.

The speed the [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) will play at is determined by the
speed parameter (defaults to `1`). When the speed is equal to `1` the
number of seconds the track will take to complete is equal to the track's
[AnimationTrack.Length](/docs/reference/engine/classes/AnimationTrack.md) property. For example, a speed of `2` will
cause the track to play twice as fast.

The weight and speed of the animation can also be changed after the
animation has begun playing by using the
[AnimationTrack:AdjustWeight()](/docs/reference/engine/classes/AnimationTrack.md) and
[AnimationTrack:AdjustSpeed()](/docs/reference/engine/classes/AnimationTrack.md) methods.

If you want to start the animation at a specific point using
[AnimationTrack.TimePosition](/docs/reference/engine/classes/AnimationTrack.md), it's important the animation is
played before this is done.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `fadeTime` | `float` | `0.100000001` | The duration of time that the animation's weight should be faded in for. |
| `weight` | `float` | `1` | The weight the animation is to be played at. |
| `speed` | `float` | `1` | The playback speed of the animation. |

**Returns:** `()`

**Playing Animation for a Specific Duration**

The following function will play an AnimationTrack for a specific duration.
This is done by changing the speed of the animation to the length of the
animation divided by the desired playback duration. This could be used in
situations where a developer wants to play a standard animation for different
duration (for example, recharging different abilities).

```lua
local function playAnimationForDuration(animationTrack, duration)
	local speed = animationTrack.Length / duration
	animationTrack:Play()
	animationTrack:AdjustSpeed(speed)
end

local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://507765000"

local humanoid = script.Parent:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")

local animationTrack = animator:LoadAnimation(animation)

playAnimationForDuration(animationTrack, 3)
```

**Freeze Animation at Position**

The following code sample includes two functions that demonstrate how
AdjustSpeed and TimePosition can be used to freeze an animation at a
particular point.

The first function freezes an animation at a particular point in time (defined
in seconds). The second freezes at it at a percentage (between 0 or 100) by
multiplying the percentage by the track length.

As TimePosition can not be used when an AnimationTrack is not playing, the
functions check to make sure the animation is playing before proceeding.

```lua
function freezeAnimationAtTime(animationTrack, timePosition)
	if not animationTrack.IsPlaying then
		-- Play the animation if it is not playing
		animationTrack:Play()
	end
	-- Set the speed to 0 to freeze the animation
	animationTrack:AdjustSpeed(0)
	-- Jump to the desired TimePosition
	animationTrack.TimePosition = timePosition
end

function freezeAnimationAtPercent(animationTrack, percentagePosition)
	if not animationTrack.IsPlaying then
		-- Play the animation if it is not playing
		animationTrack:Play()
	end
	-- Set the speed to 0 to freeze the animation
	animationTrack:AdjustSpeed(0)
	-- Jump to the desired TimePosition
	animationTrack.TimePosition = (percentagePosition / 100) * animationTrack.Length
end

local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://507765644"

local humanoid = script.Parent:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")
local animationTrack = animator:LoadAnimation(animation)

freezeAnimationAtTime(animationTrack, 0.5)
freezeAnimationAtPercent(animationTrack, 50)
```

### Method: AnimationTrack:SetParameter

**Signature:** `AnimationTrack:SetParameter(key: string, value: Variant): ()`

Sets a parameter value on the animation graph, driving animation graph
node inputs. Parameters can be set before or during playback. If set
before the animation graph has loaded, the value is stored and applied
once the graph is ready.

Non-finite numeric values (NaN, Inf) are sanitized to 0 and produce a
warning. Use [AnimationTrack:GetParameterDefaults()](/docs/reference/engine/classes/AnimationTrack.md) to discover
what parameters are available and their default values.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The name of the parameter to set. |
| `value` | `Variant` |  | The value to assign to the parameter. Non-finite numeric values are sanitized to 0. |

**Returns:** `()`

### Method: AnimationTrack:Stop

**Signature:** `AnimationTrack:Stop(fadeTime?: float): ()`

Stops the [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md). Once called, the weight of the animation
will move towards zero over a length of time specified by the optional
`fadeTime` parameter. For example, if `Stop()` is called with a `fadeTime`
of `2`, it will take two seconds for the weight of the track to reach zero
and its effects completely end. Please note this will be the case
regardless of the initial weight of the animation.

#### Usage Notes

After calling `Stop()`, subsequent calls to `Stop()` and
[AdjustWeight()](/docs/reference/engine/classes/AnimationTrack.md) will not work as
expected. To adjust a track that's fading out, you must first call
[Play()](/docs/reference/engine/classes/AnimationTrack.md) to reset the
[IsPlaying](/docs/reference/engine/classes/AnimationTrack.md) property to `true`.

It is not recommended to use a `fadeTime` of `0` in an attempt to override
this effect and end the animation immediately for [Motor6Ds](/docs/reference/engine/classes/Motor6D.md)
that have their [Motor.MaxVelocity](/docs/reference/engine/classes/Motor.md) set to zero, as this causes the
joints to freeze in place. If it must end immediately, ensure the
[Motor.MaxVelocity](/docs/reference/engine/classes/Motor.md) of [Motor6Ds](/docs/reference/engine/classes/Motor6D.md) in your rig are high
enough for them to snap properly.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `fadeTime` | `float` | `0.100000001` | The time, in seconds, for which animation weight is to be faded out over. |

**Returns:** `()`

**AnimationTrack Stop**

This code sample includes a function that stops an AnimationTrack with a
specific fadeTime, and yields until the fade is completed and the weight of
the AnimationTrack is equal to zero.

The purpose of this sample is to demonstrate how the fadeTime parameter of
AnimationTrack.Stop works. In most cases, if a developer wishes to yield over
the fadeTime it is recommended they use wait(fadeTime).

```lua
local function fadeOut(animationTrack, fadeTime)
	animationTrack:Stop(fadeTime)
	local startTime = tick()
	while animationTrack.WeightCurrent > 0 do
		task.wait()
	end
	local timeTaken = tick() - startTime
	print("Time taken for weight to reset: " .. tostring(timeTaken))
end

local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://507765644"

local humanoid = script.Parent:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")
local animationTrack = animator:LoadAnimation(animation)

animationTrack:Play()

fadeOut(animationTrack, 1)
```

## Events

### Event: AnimationTrack.DidLoop

**Signature:** `AnimationTrack.DidLoop()`

This event fires whenever a looped [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) completes a
loop, on the next update.

Currently it may also fire at the exact end of a non looped animation
track but this behavior should not be relied upon.

*Security: None · Capabilities: Animation*

**Play AnimationTrack for a Number of Loops**

The function in this code sample will play an AnimationTrack on a loop, for a
specific number of loops, before stopping the animation.

In some cases the developer may want to stop a looped animation after a
certain number of loops have completed, rather than after a certain amount of
time. This is where the DidLoop event can be used.

```lua
local function playForNumberLoops(animationTrack, number)
	animationTrack.Looped = true
	animationTrack:Play()
	local numberOfLoops = 0
	local connection = nil
	connection = animationTrack.DidLoop:Connect(function()
		numberOfLoops = numberOfLoops + 1
		print("loop: ", numberOfLoops)
		if numberOfLoops >= number then
			animationTrack:Stop()
			connection:Disconnect() -- it's important to disconnect connections when they are no longer needed
		end
	end)
end

local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://507765644"

local humanoid = script.Parent:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")
local animationTrack = animator:LoadAnimation(animation)

playForNumberLoops(animationTrack, 5)
```

### Event: AnimationTrack.Ended

**Signature:** `AnimationTrack.Ended()`

Fires when the [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) is completely done moving anything
in the world, meaning the animation has finished playing, the "fade out"
is finished, and the subject is in a neutral pose.

You can use this to take action when the animation track's subject is back
in a neutral pose that's unaffected by the [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) or to
clean up the [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md).

*Security: None · Capabilities: Animation*

**AnimationTrack Ended**

The function in this code sample plays an animationTrack and yields until it
has stopped and ended, printing at each step along the way.

```lua
local InsertService = game:GetService("InsertService")
local Players = game:GetService("Players")

-- Create an NPC model to animate.
local npcModel = Players:CreateHumanoidModelFromUserIdAsync(129687796)
npcModel.Name = "JoeNPC"
npcModel.Parent = workspace
npcModel:MoveTo(Vector3.new(0, 15, 4))
local humanoid = npcModel:WaitForChild("Humanoid")

-- Load an animation.
local animationModel = InsertService:LoadAsset(2510238627)
local animation = animationModel:FindFirstChildWhichIsA("Animation", true)
local animator = humanoid:WaitForChild("Animator")
local animationTrack = animator:LoadAnimation(animation)

-- Connect to Stopped event. This fires when animation stops of
-- it's own accord, or we explicitly call Stop.
animationTrack.Stopped:Connect(function()
	print("Animation stopped")
end)

-- Connect to Ended event. This fires when when animation is completely
-- finished affecting the world. In this case it will fire 3 seconds
-- after we call animationTrack:Stop because we pass in a 3
-- second fadeOut.
animationTrack.Ended:Connect(function()
	print("Animation ended")
	animationTrack:Destroy()
end)

-- Run, give it a bit to play, then stop.
print("Calling Play")
animationTrack:Play()
task.wait(10)
print("Calling Stop")
animationTrack:Stop(3)
```

### Event: AnimationTrack.KeyframeReached

**Signature:** `AnimationTrack.KeyframeReached(keyframeName: string)`

Fires every time playback of an [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) reaches a
[Keyframe](/docs/reference/engine/classes/Keyframe.md) that does not have the default name of `Keyframe`. This
event lets you run code at predefined points in an animation (set by
[Keyframe](/docs/reference/engine/classes/Keyframe.md) names).

[Keyframe](/docs/reference/engine/classes/Keyframe.md) names do not need to be unique. For example, if an
animation has three keyframes named `Particles`, this event will fire each
time one of these keyframes is reached.

[Keyframe](/docs/reference/engine/classes/Keyframe.md) names can be set in the
[Animation Editor](/docs/en-us/animation/editor.md) when creating or editing
an animation. They cannot however be set by a [Script](/docs/reference/engine/classes/Script.md) on an
existing animation prior to playing it.

*Security: None · Capabilities: Animation*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `keyframeName` | `string` | The name of the [Keyframe](/docs/reference/engine/classes/Keyframe.md) reached. |

### Event: AnimationTrack.Stopped

**Signature:** `AnimationTrack.Stopped()`

Fires whenever the [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) finishes playing.

This event has a number of uses. It can be used to wait until an
[AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) has stopped before continuing (for example, if
chaining a series of animations to play after each other). It can also be
used to clean up any [Instances](/docs/reference/engine/classes/Instance.md) created during the
animation playback.

*Security: None · Capabilities: Animation*

**AnimationTrack Stopped**

The function in this code sample will play an animationTrack and yield until
it has stopped, before printing.

```lua
local function yieldPlayAnimation(animationTrack, fadeTime, weight, speed)
	animationTrack:Play(fadeTime, weight, speed)
	animationTrack.Stopped:Wait()
	print("Animation has stopped")
end

local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://507765644"

local humanoid = script.Parent:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")
local animationTrack = animator:LoadAnimation(animation)

yieldPlayAnimation(animationTrack, 1, 0.6, 1)
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