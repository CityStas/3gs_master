---
name: Sound
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Internal
summary: "An object that emits sound. This object can be placed within a BasePart or Attachment to emit a sound from a particular position within a place or world, or it can be attached elsewhere to play the sound at a constant volume throughout the entire place."
---

# Class: Sound

> An object that emits sound. This object can be placed within a
> [BasePart](/docs/reference/engine/classes/BasePart.md) or [Attachment](/docs/reference/engine/classes/Attachment.md) to emit a sound from a particular
> position within a place or world, or it can be attached elsewhere to play the
> sound at a constant volume throughout the entire place.

## Description

[Sound](/docs/reference/engine/classes/Sound.md) is an object that emits sound. When placed in a [BasePart](/docs/reference/engine/classes/BasePart.md)
or an [Attachment](/docs/reference/engine/classes/Attachment.md), this object will emit its sound from that part's
[BasePart.Position](/docs/reference/engine/classes/BasePart.md) or the attachment's
[Attachment.WorldPosition](/docs/reference/engine/classes/Attachment.md). In this placement, a [Sound](/docs/reference/engine/classes/Sound.md) exhibits
the Doppler effect, meaning its frequency and pitch varies with the relative
motion of whatever attachment or part it is attached to. Additionally, its
volume will be determined by the distance between the client's sound listener
(by default the [Camera](/docs/reference/engine/classes/Camera.md) position) and the position of the sound's
parent. For more information, see [RollOffMode](/docs/reference/engine/classes/Sound.md).

A sound is considered "global" if it is **not** parented to a [BasePart](/docs/reference/engine/classes/BasePart.md)
or an [Attachment](/docs/reference/engine/classes/Attachment.md). In this case, the sound will play at the same volume
throughout the entire place.

## Code Samples

**Music Playing Part**

The code in this sample demonstrates how a sound parented to a Part or
Attachment will play locally and experience volume drop off the further the
player's camera is away from the part.

A part is instanced, and a sound is instanced and parented to the part. A
click detector is set up on the part that will check if the sound is playing,
using [Sound.IsPlaying](/docs/reference/engine/classes/Sound.md) and play or stop the sound depending.

```lua
local part = Instance.new("Part")
part.Anchored = true
part.Position = Vector3.new(0, 3, 0)
part.BrickColor = BrickColor.new("Bright red")
part.Name = "MusicBox"
part.Parent = workspace

-- create a sound
local sound = Instance.new("Sound", part)
sound.SoundId = "rbxassetid://9120386436"
sound.EmitterSize = 5 -- decrease the emitter size (for earlier volume drop off)
sound.Looped = true
sound.Parent = part

local clickDetector = Instance.new("ClickDetector")
clickDetector.Parent = part

-- toggle the sound playing / not playing
clickDetector.MouseClick:Connect(function()
	if not sound.IsPlaying then
		part.BrickColor = BrickColor.new("Bright green")
		sound:Play()
	else
		part.BrickColor = BrickColor.new("Bright red")
		sound:Stop()
	end
end)
```

## Properties

### Property: Sound.AudioContent

```json
{
  "type": "Content",
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
  "category": "Asset",
  "capabilities": [
    "LegacySound"
  ]
}
```

This property is a reference to an audio asset.

### Property: Sound.IsLoaded

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
  "category": "Asset",
  "capabilities": [
    "LegacySound"
  ]
}
```

This property is `true` when the [Sound](/docs/reference/engine/classes/Sound.md) has loaded from Roblox
servers and is ready to play. You can use this property and the
[Loaded](/docs/reference/engine/classes/Sound.md) event to verify a sound has loaded before
playing it.

**Load Sound**

This simple function will verify a Sound has loaded by checking the
Sound.IsLoaded property. If Sound.IsLoaded is false it will wait for the
Loaded event before resuming.

It is important to check Sound.IsLoaded before connecting to the Sound.Loaded
event, as if the sound has already loaded the Sound.Loaded event will not fire
and the function will yield indefinitely.

```lua
local sound = script.Parent.Sound

if not sound.IsLoaded then
	sound.Loaded:Wait()
end

print("The sound has loaded!")
```

### Property: Sound.Looped

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
  "category": "Playback",
  "capabilities": [
    "LegacySound"
  ]
}
```

This sets whether or not the [Sound](/docs/reference/engine/classes/Sound.md) repeats once it has finished
playing. Looped sounds are suitable for a range of applications including
music and background ambient sounds.

The [DidLoop](/docs/reference/engine/classes/Sound.md) event can be used to track the number of
times as sound has looped.

**Loop a Number of Times**

This code sample includes a function that will play a sound and allow it to
loop for a given number of times before stopping it.

```lua
local function loopNTimes(sound, numberOfLoops)
	if not sound.IsPlaying then
		sound.Looped = true
		local connection = nil
		connection = sound.DidLoop:Connect(function(_soundId, numOfTimesLooped)
			print(numOfTimesLooped)
			if numOfTimesLooped >= numberOfLoops then
				-- disconnect the connection
				connection:Disconnect()
				-- stop the sound
				sound:Stop()
			end
		end)
		sound:Play()
	end
end

local sound = Instance.new("Sound")
sound.SoundId = "rbxassetid://0"

loopNTimes(sound, 5)
```

### Property: Sound.LoopRegion

```json
{
  "type": "NumberRange",
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
  "category": "Regions",
  "capabilities": [
    "LegacySound"
  ]
}
```

A range denoting a desired loop start and loop end within the
[PlaybackRegion](/docs/reference/engine/classes/Sound.md), in seconds.

- If [LoopRegion.Min](/docs/reference/engine/classes/Sound.md) `>`
  [PlaybackRegion.Min](/docs/reference/engine/classes/Sound.md), the loop starts from
  [LoopRegion.Min](/docs/reference/engine/classes/Sound.md).

- If [LoopRegion.Min](/docs/reference/engine/classes/Sound.md) `<`
  [PlaybackRegion.Min](/docs/reference/engine/classes/Sound.md), the loop starts from
  [PlaybackRegion.Min](/docs/reference/engine/classes/Sound.md).

- If [LoopRegion.Max](/docs/reference/engine/classes/Sound.md) `>`
  [PlaybackRegion.Max](/docs/reference/engine/classes/Sound.md), the loop starts at
  [PlaybackRegion.Max](/docs/reference/engine/classes/Sound.md).

- If [LoopRegion.Max](/docs/reference/engine/classes/Sound.md) `<`
  [PlaybackRegion.Max](/docs/reference/engine/classes/Sound.md), the loop starts at
  **exactly** that time.

- If [LoopRegion.Min](/docs/reference/engine/classes/Sound.md) `==`
  [LoopRegion.Max](/docs/reference/engine/classes/Sound.md), the [Sound](/docs/reference/engine/classes/Sound.md) uses the
  [PlaybackRegion](/docs/reference/engine/classes/Sound.md) property instead.

### Property: Sound.PlaybackLoudness

```json
{
  "type": "double",
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
  "category": "Playback",
  "capabilities": [
    "LegacySound"
  ]
}
```

A number between `0` and `1000` indicating how loud the [Sound](/docs/reference/engine/classes/Sound.md) is
currently playing back. This property reflects the amplitude of the
sound's playback in the instance of time it is read.

**Volume Amplitude Bar**

In this sample Sound.PlaybackLoudness is used to create an amplitude bar that
shows the amplitude of a sound playing.

This code sample should be placed in StarterPlayerScripts.

A simple GUI is created, a frame holding that bar and a frame containing the
bar. A Sound is then played and the size of the bar is set to reflect the
Sound.PlaybackLoudness on a loop.

```lua
-- to be placed in StarterPlayer > StarterPlayerScripts

local Players = game:GetService("Players")

-- wait for local player PlayerGui
local LocalPlayer = Players.LocalPlayer
local playerGui = LocalPlayer:WaitForChild("PlayerGui")

-- create a ScreenGui
local screenGui = Instance.new("ScreenGui")
screenGui.Parent = playerGui

-- create a holder for our bar
local frame = Instance.new("Frame")
frame.AnchorPoint = Vector2.new(0.5, 0.5)
frame.Position = UDim2.new(0.5, 0, 0.5, 0)
frame.Size = UDim2.new(0.3, 0, 0.05, 0)
frame.Parent = screenGui

-- create a bar
local bar = Instance.new("Frame")
bar.Position = UDim2.new(0, 0, 0, 0)
bar.Size = UDim2.new(1, 0, 1, 0)
bar.BackgroundColor3 = Color3.new(0, 1, 0)
bar.Parent = frame

-- create a sound
local sound = Instance.new("Sound")
sound.SoundId = "rbxassetid://9120386436"
sound.Looped = true
sound.Parent = screenGui
sound:Play()

-- define a max loudness
local maxLoudness = 30

-- animate the amplitude bar
while true do
	local amplitude = math.clamp(sound.PlaybackLoudness / maxLoudness, 0, 1)
	bar.Size = UDim2.new(amplitude, 0, 1, 0)
	wait(0.05)
end
```

### Property: Sound.PlaybackRegion

```json
{
  "type": "NumberRange",
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
  "category": "Regions",
  "capabilities": [
    "LegacySound"
  ]
}
```

A range denoting a desired start and stop time within the
[TimeLength](/docs/reference/engine/classes/Sound.md), in seconds.

- If [PlaybackRegion.Min](/docs/reference/engine/classes/Sound.md) `>` `0`, the sound
  begins to play from the [PlaybackRegion.Min](/docs/reference/engine/classes/Sound.md)
  time.

- If [PlaybackRegion.Min](/docs/reference/engine/classes/Sound.md) `<` `0`, the sound
  begins to play from `0`.

- If [PlaybackRegion.Max](/docs/reference/engine/classes/Sound.md) `>`
  [Sound.TimeLength](/docs/reference/engine/classes/Sound.md), the sound stops at [Sound.TimeLength](/docs/reference/engine/classes/Sound.md).

- If [PlaybackRegion.Max](/docs/reference/engine/classes/Sound.md) `<`
  [Sound.TimeLength](/docs/reference/engine/classes/Sound.md), the sound stops at **exactly** that time.

- If [PlaybackRegion.Min](/docs/reference/engine/classes/Sound.md) `==`
  [PlaybackRegion.Max](/docs/reference/engine/classes/Sound.md), this property is
  inactive.

### Property: Sound.PlaybackRegionsEnabled

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
  "category": "Playback",
  "capabilities": [
    "LegacySound"
  ]
}
```

If `true`, this property gives your [Sound](/docs/reference/engine/classes/Sound.md) access to the
[PlaybackRegion](/docs/reference/engine/classes/Sound.md) and
[LoopRegion](/docs/reference/engine/classes/Sound.md) properties which can more-accurately
control its playback.

### Property: Sound.PlaybackSpeed

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Playback",
  "capabilities": [
    "LegacySound"
  ]
}
```

Determines the speed at which a [Sound](/docs/reference/engine/classes/Sound.md) will play, with higher
values causing the sound to play faster and at a higher pitch.

**Sound PlaybackSpeed**

In this example a Sound is played in the Workspace. The PlaybackSpeed property
is increased and decreased at intervals to demonstrate its impact on the
playback of the Sound.

```lua
local sound = Instance.new("Sound")
sound.SoundId = "rbxassetid://9120386436"
sound.Looped = true
sound.Parent = workspace

sound:Play()
task.wait(10)
sound.PlaybackSpeed = 3 -- 3x faster
task.wait(5)
sound.PlaybackSpeed = 0.5 -- 2x slower
task.wait(5)
sound.PlaybackSpeed = 1 -- default
```

### Property: Sound.Playing

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
  "category": "Playback",
  "capabilities": [
    "LegacySound"
  ]
}
```

Indicates whether the [Sound](/docs/reference/engine/classes/Sound.md) is currently playing. This can be
toggled, and this property will always replicate.

In Studio's [Properties](/docs/en-us/studio/properties.md) window, while in
**Edit** mode, toggling [Playing](/docs/reference/engine/classes/Sound.md) to `true` does not
begin playing the sound, but the sound will begin playing during runtime.

This property should not be confused with
[IsPlaying](/docs/reference/engine/classes/Sound.md) which is a read-only property.

Note that when [Playing](/docs/reference/engine/classes/Sound.md) is set to `false`, the
[TimePosition](/docs/reference/engine/classes/Sound.md) property of the sound will not
reset, meaning that when [Playing](/docs/reference/engine/classes/Sound.md) is set to `true`
again, the audio will continue from the time position it was at when it
was stopped. However, if the [Play()](/docs/reference/engine/classes/Sound.md) function is used
to resume the sound, the time position will reset to `0`.

**Sound Playing**

This sample demonstrates how the Sound.Playing property can be used to start
and stop playback of a sound.

A sound is instanced in the Workspace and playback is started by setting
Sound.Playing to true. After ten seconds the playback is stopped by setting
Sound.Playing to false. When the playback is again resumed using Sound.Playing
it resumes at the previous Sound.TimePosition it was stopped at. This is
demonstrated by printing the TimePosition property immediately after resuming
the sound.

```lua
local sound = Instance.new("Sound")
sound.SoundId = "rbxassetid://9120386436"
sound.Looped = true
sound.Parent = workspace

print("playing sound")
sound.Playing = true

task.wait(10)

print("stopping sound")
sound.Playing = false

task.wait(5)

sound.Playing = true
local timePosition = sound.TimePosition
print("resumed at time position: " .. tostring(timePosition)) -- c. 10 seconds
```

### Property: Sound.PlayOnRemove

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
    "LegacySound"
  ]
}
```

When `true`, the [Sound](/docs/reference/engine/classes/Sound.md) will play when it is removed from the
experience by parenting the [Sound](/docs/reference/engine/classes/Sound.md) or one if its ancestors to
`nil`. This means all of the following will cause the sound to play when
[PlayOnRemove](/docs/reference/engine/classes/Sound.md) is `true`:

- `sound:Destroy()`
- `sound.Parent = nil`
- `sound.Parent.Parent = nil`

### Property: Sound.RollOffMaxDistance

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Emitter",
  "capabilities": [
    "LegacySound"
  ]
}
```

The maximum distance, in studs, a client's listener can be from the
sound's origin and still hear it. Only applies to [Sounds](/docs/reference/engine/classes/Sound.md)
parented to a [BasePart](/docs/reference/engine/classes/BasePart.md) or [Attachment](/docs/reference/engine/classes/Attachment.md).

How [RollOffMaxDistance](/docs/reference/engine/classes/Sound.md) impacts the
attenuation of a sound (manner in which it fades out) is dependent on the
[RollOffMode](/docs/reference/engine/classes/Sound.md) property.

### Property: Sound.RollOffMinDistance

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Emitter",
  "capabilities": [
    "LegacySound"
  ]
}
```

The minimum distance, in studs, at which a [Sound](/docs/reference/engine/classes/Sound.md) which is parented
to a [BasePart](/docs/reference/engine/classes/BasePart.md) or [Attachment](/docs/reference/engine/classes/Attachment.md) will begin to attenuate
(decrease in volume).

How [RollOffMinDistance](/docs/reference/engine/classes/Sound.md) impacts the
attenuation of a sound (manner in which it fades out) is dependent on the
[RollOffMode](/docs/reference/engine/classes/Sound.md) property.

### Property: Sound.RollOffMode

```json
{
  "type": "RollOffMode",
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
  "category": "Emitter",
  "capabilities": [
    "LegacySound"
  ]
}
```

This property controls how the volume of a [Sound](/docs/reference/engine/classes/Sound.md) which is parented
to a [BasePart](/docs/reference/engine/classes/BasePart.md) or [Attachment](/docs/reference/engine/classes/Attachment.md) attenuates (fades out) as the
distance between the listener and parent changes.

For details on the different modes, see [RollOffMode](/docs/reference/engine/enums/RollOffMode.md).

### Property: Sound.SoundGroup

```json
{
  "type": "SoundGroup",
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
  "category": "Routing",
  "capabilities": [
    "LegacySound"
  ]
}
```

The [SoundGroup](/docs/reference/engine/classes/SoundGroup.md) that is linked to this [Sound](/docs/reference/engine/classes/Sound.md).

### Property: Sound.SoundId

```json
{
  "type": "ContentId",
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
  "category": "Asset",
  "capabilities": [
    "LegacySound"
  ]
}
```

This property is the content ID of the sound file to associate with the
[Sound](/docs/reference/engine/classes/Sound.md). See [Audio Assets](/docs/en-us/audio/assets.md) for more
information.

### Property: Sound.TimeLength

```json
{
  "type": "double",
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
  "category": "Asset",
  "capabilities": [
    "LegacySound"
  ]
}
```

The length of the [Sound](/docs/reference/engine/classes/Sound.md) in seconds. If the [Sound](/docs/reference/engine/classes/Sound.md) is not
loaded, this value will be `0`.

This property is often used in conjunction with
[PlaybackSpeed](/docs/reference/engine/classes/Sound.md) to adjust the speed of a sound
so that it lasts for a specific duration.

**Play a Sound for a Specific Duration**

This code sample includes a simple function that uses Sound.TimeLength and
Sound.PlaybackSpeed to play a sound that'll take the given duration to
complete. It achieves this by setting the PlaybackSpeed of the sound to be
equal to the TimeLength of the sound divided by the desired duration.

Note that as TimeLength is equal to 0 when the sound has not loaded, the
function will yield while it loads the sound.

```lua
local function playForDuration(sound, duration)
	if not sound.IsLoaded then
		sound.Loaded:wait()
	end
	local speed = sound.TimeLength / duration
	sound.PlaybackSpeed = speed
	sound:Play()
end

local sound = script.Parent
playForDuration(sound, 5)
```

### Property: Sound.TimePosition

```json
{
  "type": "double",
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
  "category": "Playback",
  "capabilities": [
    "LegacySound"
  ]
}
```

This property reflects the progress of the [Sound](/docs/reference/engine/classes/Sound.md) in seconds. It
can be changed to move the playback position of the sound both before and
during playback.

As a [Sound](/docs/reference/engine/classes/Sound.md) is played, [TimePosition](/docs/reference/engine/classes/Sound.md)
increases at a rate of [PlaybackSpeed](/docs/reference/engine/classes/Sound.md) per
second. Once [TimePosition](/docs/reference/engine/classes/Sound.md) reaches
[TimeLength](/docs/reference/engine/classes/Sound.md), the sound will stop unless it is
[Looped](/docs/reference/engine/classes/Sound.md).

Note that setting [TimePosition](/docs/reference/engine/classes/Sound.md) to a value
greater than the length in a looped track will not cause it to wrap
around. If that behavior is desired, consider the following code snippet:

**Sound TimePosition**

This sample demonstrates how Sound.TimePosition can be used to jump to
particular points in an audio file both before and during Sound playback.

A Sound is created in the Workspace and set to start at 30 seconds in. During
playback, it jumps forwards to 100 seconds and then back to the start (0
seconds).

```lua
local sound = Instance.new("Sound")
sound.SoundId = "rbxassetid://9120386436"
sound.Parent = workspace

sound.TimePosition = 30

sound:Play()

task.wait(5)

sound.TimePosition = 100

task.wait(5)

sound.TimePosition = 0
```

**Time Position**

Demonstrates [Sound.TimePosition](/docs/reference/engine/classes/Sound.md).

```lua
local Workspace = game:GetService("Workspace")

local sound = Instance.new("Sound")
sound.Parent = Workspace

local newPosition = 1.5

if newPosition >= sound.TimeLength then
	newPosition = newPosition - sound.TimeLength
end
sound.TimePosition = newPosition
```

### Property: Sound.Volume

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Playback",
  "capabilities": [
    "LegacySound"
  ]
}
```

The volume of the [Sound](/docs/reference/engine/classes/Sound.md). Can be set between `0` and `10` and
defaults to `0.5`.

Note that if the [Sound](/docs/reference/engine/classes/Sound.md) is a member of a [SoundGroup](/docs/reference/engine/classes/SoundGroup.md), its
playback volume (but not its [Volume](/docs/reference/engine/classes/Sound.md) property) will be
influenced by the group's [SoundGroup.Volume](/docs/reference/engine/classes/SoundGroup.md) property.

### Property: Sound.EmitterSize

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "LegacySound"
  ]
}
```

> **Deprecated:** This property has deprecated in favor of [Sound.RollOffMinDistance](/docs/reference/engine/classes/Sound.md) and [Sound.RollOffMaxDistance](/docs/reference/engine/classes/Sound.md) which should be used instead in new work.

The minimum distance, in studs, at which a 3D [Sound](/docs/reference/engine/classes/Sound.md) (direct child
of a [BasePart](/docs/reference/engine/classes/BasePart.md) or [Attachment](/docs/reference/engine/classes/Attachment.md)) will begin to attenuate
(decrease in volume).

Sounds parented to a [BasePart](/docs/reference/engine/classes/BasePart.md) or [Attachment](/docs/reference/engine/classes/Attachment.md) that are
descendants of the [Workspace](/docs/reference/engine/classes/Workspace.md) are considered 3D sounds and their
volume while playing is dependent on the distance between the client's
sound listener ([Camera](/docs/reference/engine/classes/Camera.md) position by default) and the Sound's
parent. Two properties influence this behavior EmitterSize and
[Sound.RollOffMode](/docs/reference/engine/classes/Sound.md).

The way the [Sound](/docs/reference/engine/classes/Sound.md) attenuates (fades out) after the distance
between the listener and the sound exceeds the EmitterSize is determined
by RollOffMode.

**Music Playing Part**

The code in this sample demonstrates how a sound parented to a Part or
Attachment will play locally and experience volume drop off the further the
player's camera is away from the part.

A part is instanced, and a sound is instanced and parented to the part. A
click detector is set up on the part that will check if the sound is playing,
using [Sound.IsPlaying](/docs/reference/engine/classes/Sound.md) and play or stop the sound depending.

```lua
local part = Instance.new("Part")
part.Anchored = true
part.Position = Vector3.new(0, 3, 0)
part.BrickColor = BrickColor.new("Bright red")
part.Name = "MusicBox"
part.Parent = workspace

-- create a sound
local sound = Instance.new("Sound", part)
sound.SoundId = "rbxassetid://9120386436"
sound.EmitterSize = 5 -- decrease the emitter size (for earlier volume drop off)
sound.Looped = true
sound.Parent = part

local clickDetector = Instance.new("ClickDetector")
clickDetector.Parent = part

-- toggle the sound playing / not playing
clickDetector.MouseClick:Connect(function()
	if not sound.IsPlaying then
		part.BrickColor = BrickColor.new("Bright green")
		sound:Play()
	else
		part.BrickColor = BrickColor.new("Bright red")
		sound:Stop()
	end
end)
```

### Property: Sound.isPlaying

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "LegacySound"
  ]
}
```

> **Deprecated:** This deprecated property is a variant of [Sound.IsPlaying](/docs/reference/engine/classes/Sound.md) which should be used instead.

### Property: Sound.MaxDistance

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "LegacySound"
  ]
}
```

> **Deprecated:** This property has deprecated in favor of [Sound.RollOffMinDistance](/docs/reference/engine/classes/Sound.md) and [Sound.RollOffMaxDistance](/docs/reference/engine/classes/Sound.md) which should be used instead in new work.

The maximum distance, in studs, a client's listener can be from the
[Sound](/docs/reference/engine/classes/Sound.md) origin and still hear it. Only applies to Sounds parented to
a [Part](/docs/reference/engine/classes/Part.md) or [Attachment](/docs/reference/engine/classes/Attachment.md) (3D sounds).

How MaxDistance impacts the attenuation of a sound (manner in which it
fades out) is dependent on the [Sound.RollOffMode](/docs/reference/engine/classes/Sound.md) property. When
RollOffMode is set to use an inverse type distance model (Inverse or
InverseTapered) the MaxDistance will not effect the attenuation of the
sound. This means that low values for MaxDistance will cause the sound to
abruptly cut off when the listener reaches the MaxDistance. In most cases
this is not desirable and developers are advised not to use low
MaxDistance values.

When RollOffMode is set to a linear type distance model (Linear or
LinearSquared) the sound will attenuate between [Sound.EmitterSize](/docs/reference/engine/classes/Sound.md)
and MaxDistance (with playback volume reaching zero at MaxDistance). This
is less realistic, but in some cases allows attenuation to be handled in a
more intuitive way.

**Sound MaxDistance**

This sample includes a brief demonstration of how Sound.MaxDistance works.

A Part is instanced in the Workspace with a looped Sound playing within it. A
function is made to listen to the Sound's MaxDistance and change the size of a
sphere whenever it changes. The sphere's radius will always be equal to the
Sound's MaxDistance.

This example helps demonstrate how the sound is only audible when the client's
listener (by default the Camera's position) is within the sphere.

```lua
local part = Instance.new("Part")
part.Position = Vector3.new(0, 3, 0)
part.Size = Vector3.new(1, 1, 1)
part.Anchored = true
part.Parent = workspace

local sphere = Instance.new("Part")
sphere.Name = "MaxDistanceSphere"
sphere.CFrame = part.CFrame
sphere.Anchored = true
sphere.CanCollide = false
sphere.Size = Vector3.new(1, 1, 1)
sphere.Shape = Enum.PartType.Ball
sphere.Transparency = 0.8
sphere.BrickColor = BrickColor.new("Lime green")
sphere.Parent = workspace

local sound = Instance.new("Sound")
sound.Name = "TestSound"
sound.MaxDistance = 20
sound.SoundId = "rbxasset://sounds/uuhhh.mp3" -- oof
sound.Looped = true
sound.Parent = part

-- a function that changes the sphere size to reflect the sound's MaxDistance
local function updateSize()
	local distance = sound.MaxDistance
	sphere.Size = Vector3.new(distance * 2, distance * 2, distance * 2)
end

-- update the sphere size
updateSize()
sound:GetPropertyChangedSignal("MaxDistance"):Connect(updateSize)

sound:Play()
```

### Property: Sound.MinDistance

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "LegacySound"
  ]
}
```

> **Deprecated:** MinDistance has been superseded by [Sound.EmitterSize](/docs/reference/engine/classes/Sound.md), whose name better describes this properties behavior.

The minimum distance at which a 3D [Sound](/docs/reference/engine/classes/Sound.md) (direct child of a
[BasePart](/docs/reference/engine/classes/BasePart.md) or [Attachment](/docs/reference/engine/classes/Attachment.md)) will begin to attenuate.
Effectively, the emitter size.

### Property: Sound.Pitch

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "LegacySound"
  ]
}
```

> **Deprecated:** This property has been deprecated in favor of [Sound.PlaybackSpeed](/docs/reference/engine/classes/Sound.md) whose name suits the behavior better.

Sets how high pitched and fast a [Sound](/docs/reference/engine/classes/Sound.md) is when it is played. The
greater the integer, the higher and faster the sound is.

### Property: Sound.IsPaused *(hidden)*

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
  "category": "Playback",
  "capabilities": [
    "LegacySound"
  ]
}
```

This read-only property returns `true` when the [Sound](/docs/reference/engine/classes/Sound.md) is not
playing. Note that it can return `true` if a sound has been paused using
[Pause()](/docs/reference/engine/classes/Sound.md), if it has been stopped using
[Stop()](/docs/reference/engine/classes/Sound.md), or the sound has never been played.

As [IsPaused](/docs/reference/engine/classes/Sound.md) is read-only, it cannot be used to stop
the sound; [Stop()](/docs/reference/engine/classes/Sound.md) or [Pause()](/docs/reference/engine/classes/Sound.md)
should be used instead.

**Sound IsPlaying and SoundIsPaused**

This code sample contains demonstrates when the Sound.IsPlaying and
Sound.IsPaused properties will be true or false.

A sound is instanced in the Workspace and the Sound.IsLoaded property is
checked to ensure it has loaded, if it has not the Sound.Loaded event is used
to yield the script until the sound has.

As the sound is played, paused and stopped the Sound.IsPlaying and
Sound.IsPaused properties are printed to demonstrate how they respond to each
of these functions. Note Sound.IsPaused will always be true if even if the
sound has been stopped rather than paused.

```lua
local sound = Instance.new("Sound")
sound.SoundId = "rbxassetid://9120386436"
sound.Looped = true
sound.Parent = workspace

if not sound.isLoaded then
	sound.Loaded:Wait()
end

sound:Play()
print(sound.IsPlaying, sound.IsPaused) -- true, false

task.wait(2)
sound:Pause()
print(sound.IsPlaying, sound.IsPaused) -- false, true

task.wait(2)
sound:Play()
print(sound.IsPlaying, sound.IsPaused) -- true, false

task.wait(2)
sound:Stop()
print(sound.IsPlaying, sound.IsPaused) -- false, true
```

### Property: Sound.IsPlaying *(hidden)*

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
  "category": "Playback",
  "capabilities": [
    "LegacySound"
  ]
}
```

This read-only property returns true when the [Sound](/docs/reference/engine/classes/Sound.md) is playing.

As [IsPlaying](/docs/reference/engine/classes/Sound.md) is read-only, it cannot be used to
play the sound; [Play()](/docs/reference/engine/classes/Sound.md) should be used instead.

**Sound IsPlaying and SoundIsPaused**

This code sample contains demonstrates when the Sound.IsPlaying and
Sound.IsPaused properties will be true or false.

A sound is instanced in the Workspace and the Sound.IsLoaded property is
checked to ensure it has loaded, if it has not the Sound.Loaded event is used
to yield the script until the sound has.

As the sound is played, paused and stopped the Sound.IsPlaying and
Sound.IsPaused properties are printed to demonstrate how they respond to each
of these functions. Note Sound.IsPaused will always be true if even if the
sound has been stopped rather than paused.

```lua
local sound = Instance.new("Sound")
sound.SoundId = "rbxassetid://9120386436"
sound.Looped = true
sound.Parent = workspace

if not sound.isLoaded then
	sound.Loaded:Wait()
end

sound:Play()
print(sound.IsPlaying, sound.IsPaused) -- true, false

task.wait(2)
sound:Pause()
print(sound.IsPlaying, sound.IsPaused) -- false, true

task.wait(2)
sound:Play()
print(sound.IsPlaying, sound.IsPaused) -- true, false

task.wait(2)
sound:Stop()
print(sound.IsPlaying, sound.IsPaused) -- false, true
```

## Methods

### Method: Sound:Pause

**Signature:** `Sound:Pause(): ()`

This method pauses playback of the [Sound](/docs/reference/engine/classes/Sound.md) if it is playing, setting
[Playing](/docs/reference/engine/classes/Sound.md) to `false`. Unlike
[Stop()](/docs/reference/engine/classes/Sound.md), it does not reset
[TimePosition](/docs/reference/engine/classes/Sound.md), meaning the sound can be resumed
using [Resume()](/docs/reference/engine/classes/Sound.md).

*Security: None · Thread Safety: Unsafe · Capabilities: LegacySound*

**Returns:** `()`

**Sound Functions**

This sample gives a simple demonstration of what each of the Sound functions
(Sound.Play, Sound.Stop, Sound.Pause and Sound.Resume) do to Sound.Playing and
Sound.TimePosition.

```lua
-- create a sound
local sound = Instance.new("Sound", game.Workspace)
sound.SoundId = "rbxassetid://9120386436"

if not sound.IsLoaded then
	sound.Loaded:Wait()
end

-- listen for events
sound.Played:Connect(function(_soundId)
	print("Sound.Played event")
end)

sound.Paused:Connect(function(_soundId)
	print("Sound.Paused event")
end)

sound.Resumed:Connect(function(_soundId)
	print("Sound.Resumed event")
end)

sound.Stopped:Connect(function(_soundId)
	print("Sound.Stopped event")
end)

sound:Play()
print("play", sound.Playing, sound.TimePosition) -- play true 0

task.wait(10)

sound:Pause()
print("pause", sound.Playing, sound.TimePosition) -- pause false 10

task.wait(3)

sound:Resume()
print("play", sound.Playing, sound.TimePosition) -- play true 10

task.wait(3)

sound:Stop()
print("stop", sound.Playing, sound.TimePosition) -- stop false 0

task.wait(3)

sound:Play()
print("play", sound.Playing, sound.TimePosition) -- play true 0
```

### Method: Sound:Play

**Signature:** `Sound:Play(): ()`

This method plays the [Sound](/docs/reference/engine/classes/Sound.md) and sets
[TimePosition](/docs/reference/engine/classes/Sound.md) to the last value set by a script
(or `0` if it has not been set), then sets [Playing](/docs/reference/engine/classes/Sound.md)
to `true`.

*Security: None · Thread Safety: Unsafe · Capabilities: LegacySound*

**Returns:** `()`

**Sound Functions**

This sample gives a simple demonstration of what each of the Sound functions
(Sound.Play, Sound.Stop, Sound.Pause and Sound.Resume) do to Sound.Playing and
Sound.TimePosition.

```lua
-- create a sound
local sound = Instance.new("Sound", game.Workspace)
sound.SoundId = "rbxassetid://9120386436"

if not sound.IsLoaded then
	sound.Loaded:Wait()
end

-- listen for events
sound.Played:Connect(function(_soundId)
	print("Sound.Played event")
end)

sound.Paused:Connect(function(_soundId)
	print("Sound.Paused event")
end)

sound.Resumed:Connect(function(_soundId)
	print("Sound.Resumed event")
end)

sound.Stopped:Connect(function(_soundId)
	print("Sound.Stopped event")
end)

sound:Play()
print("play", sound.Playing, sound.TimePosition) -- play true 0

task.wait(10)

sound:Pause()
print("pause", sound.Playing, sound.TimePosition) -- pause false 10

task.wait(3)

sound:Resume()
print("play", sound.Playing, sound.TimePosition) -- play true 10

task.wait(3)

sound:Stop()
print("stop", sound.Playing, sound.TimePosition) -- stop false 0

task.wait(3)

sound:Play()
print("play", sound.Playing, sound.TimePosition) -- play true 0
```

### Method: Sound:Resume

**Signature:** `Sound:Resume(): ()`

This method resumes the [Sound](/docs/reference/engine/classes/Sound.md) and sets
[Playing](/docs/reference/engine/classes/Sound.md) to `true`. Does not alter
[TimePosition](/docs/reference/engine/classes/Sound.md) and thus can be used to resume
playback of a sound paused through [Pause()](/docs/reference/engine/classes/Sound.md).

*Security: None · Thread Safety: Unsafe · Capabilities: LegacySound*

**Returns:** `()`

**Sound Functions**

This sample gives a simple demonstration of what each of the Sound functions
(Sound.Play, Sound.Stop, Sound.Pause and Sound.Resume) do to Sound.Playing and
Sound.TimePosition.

```lua
-- create a sound
local sound = Instance.new("Sound", game.Workspace)
sound.SoundId = "rbxassetid://9120386436"

if not sound.IsLoaded then
	sound.Loaded:Wait()
end

-- listen for events
sound.Played:Connect(function(_soundId)
	print("Sound.Played event")
end)

sound.Paused:Connect(function(_soundId)
	print("Sound.Paused event")
end)

sound.Resumed:Connect(function(_soundId)
	print("Sound.Resumed event")
end)

sound.Stopped:Connect(function(_soundId)
	print("Sound.Stopped event")
end)

sound:Play()
print("play", sound.Playing, sound.TimePosition) -- play true 0

task.wait(10)

sound:Pause()
print("pause", sound.Playing, sound.TimePosition) -- pause false 10

task.wait(3)

sound:Resume()
print("play", sound.Playing, sound.TimePosition) -- play true 10

task.wait(3)

sound:Stop()
print("stop", sound.Playing, sound.TimePosition) -- stop false 0

task.wait(3)

sound:Play()
print("play", sound.Playing, sound.TimePosition) -- play true 0
```

### Method: Sound:Stop

**Signature:** `Sound:Stop(): ()`

This method stops the [Sound](/docs/reference/engine/classes/Sound.md) and sets [Playing](/docs/reference/engine/classes/Sound.md)
to `false`, then sets [TimePosition](/docs/reference/engine/classes/Sound.md) to `0`.

*Security: None · Thread Safety: Unsafe · Capabilities: LegacySound*

**Returns:** `()`

**Sound Functions**

This sample gives a simple demonstration of what each of the Sound functions
(Sound.Play, Sound.Stop, Sound.Pause and Sound.Resume) do to Sound.Playing and
Sound.TimePosition.

```lua
-- create a sound
local sound = Instance.new("Sound", game.Workspace)
sound.SoundId = "rbxassetid://9120386436"

if not sound.IsLoaded then
	sound.Loaded:Wait()
end

-- listen for events
sound.Played:Connect(function(_soundId)
	print("Sound.Played event")
end)

sound.Paused:Connect(function(_soundId)
	print("Sound.Paused event")
end)

sound.Resumed:Connect(function(_soundId)
	print("Sound.Resumed event")
end)

sound.Stopped:Connect(function(_soundId)
	print("Sound.Stopped event")
end)

sound:Play()
print("play", sound.Playing, sound.TimePosition) -- play true 0

task.wait(10)

sound:Pause()
print("pause", sound.Playing, sound.TimePosition) -- pause false 10

task.wait(3)

sound:Resume()
print("play", sound.Playing, sound.TimePosition) -- play true 10

task.wait(3)

sound:Stop()
print("stop", sound.Playing, sound.TimePosition) -- stop false 0

task.wait(3)

sound:Play()
print("play", sound.Playing, sound.TimePosition) -- play true 0
```

### Method: Sound:pause

**Signature:** `Sound:pause(): ()`

> **Deprecated:** This deprecated function is a variant of [Sound:Pause()](/docs/reference/engine/classes/Sound.md) which should be used instead.

*Security: None · Thread Safety: Unsafe · Capabilities: LegacySound*

**Returns:** `()`

### Method: Sound:play

**Signature:** `Sound:play(): ()`

> **Deprecated:** This deprecated function is a variant of [Sound:Play()](/docs/reference/engine/classes/Sound.md) which should be used instead.

*Security: None · Thread Safety: Unsafe · Capabilities: LegacySound*

**Returns:** `()`

### Method: Sound:stop

**Signature:** `Sound:stop(): ()`

> **Deprecated:** This deprecated function is a variant of [Sound:Stop()](/docs/reference/engine/classes/Sound.md) which should be used instead.

*Security: None · Thread Safety: Unsafe · Capabilities: LegacySound*

**Returns:** `()`

## Events

### Event: Sound.DidLoop

**Signature:** `Sound.DidLoop(soundId: string, numOfTimesLooped: int)`

Fires whenever the [Sound](/docs/reference/engine/classes/Sound.md) loops. Returns `soundId` and
`numOfTimesLooped`, giving the content ID of the sound and the number of
times looped respectively.

When the [Sound](/docs/reference/engine/classes/Sound.md) is stopped through [Stop()](/docs/reference/engine/classes/Sound.md), the
looped counter resets meaning the next [DidLoop](/docs/reference/engine/classes/Sound.md) event
will return `1` for `numOfTimesLooped`.

*Security: None · Capabilities: LegacySound*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `soundId` | `string` | The [SoundId](/docs/reference/engine/classes/Sound.md) of the [Sound](/docs/reference/engine/classes/Sound.md) that looped. |
| `numOfTimesLooped` | `int` | The number of times the [Sound](/docs/reference/engine/classes/Sound.md) has looped. |

**Loop a Number of Times**

This code sample includes a function that will play a sound and allow it to
loop for a given number of times before stopping it.

```lua
local function loopNTimes(sound, numberOfLoops)
	if not sound.IsPlaying then
		sound.Looped = true
		local connection = nil
		connection = sound.DidLoop:Connect(function(_soundId, numOfTimesLooped)
			print(numOfTimesLooped)
			if numOfTimesLooped >= numberOfLoops then
				-- disconnect the connection
				connection:Disconnect()
				-- stop the sound
				sound:Stop()
			end
		end)
		sound:Play()
	end
end

local sound = Instance.new("Sound")
sound.SoundId = "rbxassetid://0"

loopNTimes(sound, 5)
```

### Event: Sound.Ended

**Signature:** `Sound.Ended(soundId: string)`

Fires when the [Sound](/docs/reference/engine/classes/Sound.md) has completed playback and stopped. This
event is often used to destroy a sound when it has completed playback:

```
sound:Play()
sound.Ended:Wait()
sound:Destroy()
```

Note that this event will **not** fire for sounds with
[Looped](/docs/reference/engine/classes/Sound.md) set to `true`, as they continue playing upon
reaching their end. This event will also **not** fire when the sound is
stopped before playback has completed; for this use the
[Stopped](/docs/reference/engine/classes/Sound.md) event.

*Security: None · Capabilities: LegacySound*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `soundId` | `string` | The [SoundId](/docs/reference/engine/classes/Sound.md) of the [Sound](/docs/reference/engine/classes/Sound.md) that has ended. |

### Event: Sound.Loaded

**Signature:** `Sound.Loaded(soundId: string)`

Fires when the [Sound](/docs/reference/engine/classes/Sound.md) is loaded.

As this event only fires at the time the sound is loaded, it's recommended
to check the sound's [IsLoaded](/docs/reference/engine/classes/Sound.md) property prior to
connecting to this event.

*Security: None · Capabilities: LegacySound*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `soundId` | `string` | The [SoundId](/docs/reference/engine/classes/Sound.md) of the [Sound](/docs/reference/engine/classes/Sound.md) that loaded. |

**Load Sound**

This simple function will verify a Sound has loaded by checking the
Sound.IsLoaded property. If Sound.IsLoaded is false it will wait for the
Loaded event before resuming.

It is important to check Sound.IsLoaded before connecting to the Sound.Loaded
event, as if the sound has already loaded the Sound.Loaded event will not fire
and the function will yield indefinitely.

```lua
local sound = script.Parent.Sound

if not sound.IsLoaded then
	sound.Loaded:Wait()
end

print("The sound has loaded!")
```

### Event: Sound.Paused

**Signature:** `Sound.Paused(soundId: string)`

Fires whenever the [Sound](/docs/reference/engine/classes/Sound.md) is paused using
[Pause()](/docs/reference/engine/classes/Sound.md).

*Security: None · Capabilities: LegacySound*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `soundId` | `string` | The [SoundId](/docs/reference/engine/classes/Sound.md) of the [Sound](/docs/reference/engine/classes/Sound.md) that was paused. |

**Sound Functions**

This sample gives a simple demonstration of what each of the Sound functions
(Sound.Play, Sound.Stop, Sound.Pause and Sound.Resume) do to Sound.Playing and
Sound.TimePosition.

```lua
-- create a sound
local sound = Instance.new("Sound", game.Workspace)
sound.SoundId = "rbxassetid://9120386436"

if not sound.IsLoaded then
	sound.Loaded:Wait()
end

-- listen for events
sound.Played:Connect(function(_soundId)
	print("Sound.Played event")
end)

sound.Paused:Connect(function(_soundId)
	print("Sound.Paused event")
end)

sound.Resumed:Connect(function(_soundId)
	print("Sound.Resumed event")
end)

sound.Stopped:Connect(function(_soundId)
	print("Sound.Stopped event")
end)

sound:Play()
print("play", sound.Playing, sound.TimePosition) -- play true 0

task.wait(10)

sound:Pause()
print("pause", sound.Playing, sound.TimePosition) -- pause false 10

task.wait(3)

sound:Resume()
print("play", sound.Playing, sound.TimePosition) -- play true 10

task.wait(3)

sound:Stop()
print("stop", sound.Playing, sound.TimePosition) -- stop false 0

task.wait(3)

sound:Play()
print("play", sound.Playing, sound.TimePosition) -- play true 0
```

### Event: Sound.Played

**Signature:** `Sound.Played(soundId: string)`

Fires whenever the [Sound](/docs/reference/engine/classes/Sound.md) is played using
[Play()](/docs/reference/engine/classes/Sound.md). This event will **not** fire if the
[Sound](/docs/reference/engine/classes/Sound.md) is played due to [PlayOnRemove](/docs/reference/engine/classes/Sound.md)
being set to `true` and the sound being destroyed.

*Security: None · Capabilities: LegacySound*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `soundId` | `string` | The [SoundId](/docs/reference/engine/classes/Sound.md) of the [Sound](/docs/reference/engine/classes/Sound.md) that was played. |

**Sound Functions**

This sample gives a simple demonstration of what each of the Sound functions
(Sound.Play, Sound.Stop, Sound.Pause and Sound.Resume) do to Sound.Playing and
Sound.TimePosition.

```lua
-- create a sound
local sound = Instance.new("Sound", game.Workspace)
sound.SoundId = "rbxassetid://9120386436"

if not sound.IsLoaded then
	sound.Loaded:Wait()
end

-- listen for events
sound.Played:Connect(function(_soundId)
	print("Sound.Played event")
end)

sound.Paused:Connect(function(_soundId)
	print("Sound.Paused event")
end)

sound.Resumed:Connect(function(_soundId)
	print("Sound.Resumed event")
end)

sound.Stopped:Connect(function(_soundId)
	print("Sound.Stopped event")
end)

sound:Play()
print("play", sound.Playing, sound.TimePosition) -- play true 0

task.wait(10)

sound:Pause()
print("pause", sound.Playing, sound.TimePosition) -- pause false 10

task.wait(3)

sound:Resume()
print("play", sound.Playing, sound.TimePosition) -- play true 10

task.wait(3)

sound:Stop()
print("stop", sound.Playing, sound.TimePosition) -- stop false 0

task.wait(3)

sound:Play()
print("play", sound.Playing, sound.TimePosition) -- play true 0
```

### Event: Sound.Resumed

**Signature:** `Sound.Resumed(soundId: string)`

Fires when the [Sound](/docs/reference/engine/classes/Sound.md) is resumed using
[Resume()](/docs/reference/engine/classes/Sound.md).

*Security: None · Capabilities: LegacySound*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `soundId` | `string` | The [SoundId](/docs/reference/engine/classes/Sound.md) of the [Sound](/docs/reference/engine/classes/Sound.md) being resumed. |

**Sound Functions**

This sample gives a simple demonstration of what each of the Sound functions
(Sound.Play, Sound.Stop, Sound.Pause and Sound.Resume) do to Sound.Playing and
Sound.TimePosition.

```lua
-- create a sound
local sound = Instance.new("Sound", game.Workspace)
sound.SoundId = "rbxassetid://9120386436"

if not sound.IsLoaded then
	sound.Loaded:Wait()
end

-- listen for events
sound.Played:Connect(function(_soundId)
	print("Sound.Played event")
end)

sound.Paused:Connect(function(_soundId)
	print("Sound.Paused event")
end)

sound.Resumed:Connect(function(_soundId)
	print("Sound.Resumed event")
end)

sound.Stopped:Connect(function(_soundId)
	print("Sound.Stopped event")
end)

sound:Play()
print("play", sound.Playing, sound.TimePosition) -- play true 0

task.wait(10)

sound:Pause()
print("pause", sound.Playing, sound.TimePosition) -- pause false 10

task.wait(3)

sound:Resume()
print("play", sound.Playing, sound.TimePosition) -- play true 10

task.wait(3)

sound:Stop()
print("stop", sound.Playing, sound.TimePosition) -- stop false 0

task.wait(3)

sound:Play()
print("play", sound.Playing, sound.TimePosition) -- play true 0
```

### Event: Sound.Stopped

**Signature:** `Sound.Stopped(soundId: string)`

Fires when the [Sound](/docs/reference/engine/classes/Sound.md) is stopped through using
[Stop()](/docs/reference/engine/classes/Sound.md). Destroying a sound while it is playing will
not cause this event to fire.

*Security: None · Capabilities: LegacySound*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `soundId` | `string` | The [SoundId](/docs/reference/engine/classes/Sound.md) of the [Sound](/docs/reference/engine/classes/Sound.md) that stopped. |

**Sound Functions**

This sample gives a simple demonstration of what each of the Sound functions
(Sound.Play, Sound.Stop, Sound.Pause and Sound.Resume) do to Sound.Playing and
Sound.TimePosition.

```lua
-- create a sound
local sound = Instance.new("Sound", game.Workspace)
sound.SoundId = "rbxassetid://9120386436"

if not sound.IsLoaded then
	sound.Loaded:Wait()
end

-- listen for events
sound.Played:Connect(function(_soundId)
	print("Sound.Played event")
end)

sound.Paused:Connect(function(_soundId)
	print("Sound.Paused event")
end)

sound.Resumed:Connect(function(_soundId)
	print("Sound.Resumed event")
end)

sound.Stopped:Connect(function(_soundId)
	print("Sound.Stopped event")
end)

sound:Play()
print("play", sound.Playing, sound.TimePosition) -- play true 0

task.wait(10)

sound:Pause()
print("pause", sound.Playing, sound.TimePosition) -- pause false 10

task.wait(3)

sound:Resume()
print("play", sound.Playing, sound.TimePosition) -- play true 10

task.wait(3)

sound:Stop()
print("stop", sound.Playing, sound.TimePosition) -- stop false 0

task.wait(3)

sound:Play()
print("play", sound.Playing, sound.TimePosition) -- play true 0
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