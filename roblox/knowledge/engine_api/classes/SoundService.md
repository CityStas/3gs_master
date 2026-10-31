---
name: SoundService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "A service that determines various aspects of how the audio engine works. Most of its properties affect how Sounds play in the experience."
---

# Class: SoundService

> A service that determines various aspects of how the audio engine works. Most
> of its properties affect how [Sounds](/docs/reference/engine/classes/Sound.md) play in the experience.

## Description

A service that determines various aspects of how the audio engine works. Most
of its properties affect how [Sounds](/docs/reference/engine/classes/Sound.md) play in the experience,
while others affect the behavior of instances in the advanced audio system
such as [AudioPlayers](/docs/reference/engine/classes/AudioPlayer.md) and
[AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md).

[SoundService](/docs/reference/engine/classes/SoundService.md) is also often used to store
[SoundGroups](/docs/reference/engine/classes/SoundGroup.md), although this is not mandatory for groups to
work.

## Code Samples

**Dynamic Reverb System**

The code in this sample, when ran from a `LocalScript`, will change the
[SoundService.AmbientReverb](/docs/reference/engine/classes/SoundService.md) property of `SoundService` when the player
is inside a `BasePart` tagged using `CollectionService`.

To add or remove tags and reverb types, change the entries in the 'reverbTags'
table.

```lua
local Players = game:GetService("Players")
local CollectionService = game:GetService("CollectionService")
local SoundService = game:GetService("SoundService")

local localPlayer = Players.LocalPlayer

local reverbTags = {
	["reverb_Cave"] = Enum.ReverbType.Cave,
}

-- collect parts and group them by tag
local parts = {}
for reverbTag, reverbType in pairs(reverbTags) do
	for _, part in pairs(CollectionService:GetTagged(reverbTag)) do
		parts[part] = reverbType
	end
end

-- function to check if a position is within a part's extents
local function positionInPart(part, position)
	local extents = part.Size / 2
	local offset = part.CFrame:PointToObjectSpace(position)
	return offset.x < extents.x and offset.y < extents.y and offset.z < extents.z
end

local reverbType = SoundService.AmbientReverb

while true do
	task.wait()
	if not localPlayer then
		return
	end

	local character = localPlayer.Character

	-- default to no reverb
	local newReverbType = Enum.ReverbType.NoReverb

	if character and character.PrimaryPart then
		local position = character.PrimaryPart.Position

		-- go through all the indexed parts
		for part, type in pairs(parts) do
			-- see if the character is within them
			if positionInPart(part, position) then
				-- if so, pick that reverb type
				newReverbType = type
				break
			end
		end
	end

	-- set the reverb type if it has changed
	if newReverbType ~= reverbType then
		SoundService.AmbientReverb = newReverbType
		reverbType = newReverbType
	end
end
```

## Properties

### Property: SoundService.AcousticSimulationEnabled

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
  "category": "Data",
  "capabilities": [
    "Audio"
  ]
}
```

Determines at a global level whether sound from
[AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md) and
[AudioListeners](/docs/reference/engine/classes/AudioListener.md) should automatically implement
features of acoustic simulation, such as occlusion (being muffled through
walls), diffraction (bending around corners), and reverberation (echoing
off of walls).

If set to `false`, these instances will not simulate these features,
regardless of their individual
[AcousticSimulationEnabled](/docs/reference/engine/classes/AudioEmitter.md)
settings.

### Property: SoundService.AmbientReverb

```json
{
  "type": "ReverbType",
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
    "Audio"
  ]
}
```

A reverb preset that should be applied to all [Sounds](/docs/reference/engine/classes/Sound.md) in the
experience.

Each [ReverbType](/docs/reference/engine/enums/ReverbType.md) option for this property corresponds to a preset
available in the FMOD sound engine. For example, when
[AmbientReverb](/docs/reference/engine/classes/SoundService.md) is set to
[ReverbType.Hangar](/docs/reference/engine/enums/ReverbType.md), [Sounds](/docs/reference/engine/classes/Sound.md) will have reverb applied to
simulate being in a large enclosed space.

Note that this only affects [Sounds](/docs/reference/engine/classes/Sound.md) and **not** instances in
the advanced audio system such as [AudioPlayers](/docs/reference/engine/classes/AudioPlayer.md) and
[AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md). See [AudioReverb](/docs/reference/engine/classes/AudioReverb.md) for a way to
apply reverb in that system.

### Property: SoundService.CharacterSoundsUseNewApi

```json
{
  "type": "RolloutState",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Audio"
  ]
}
```

Determines which set of instances core scripts will use to create default
character sounds. If set to [RolloutState.Enabled](/docs/reference/engine/enums/RolloutState.md), it will use
instances in the advanced audio system such as
[AudioPlayers](/docs/reference/engine/classes/AudioPlayer.md) and [AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md).
If set to [RolloutState.Disabled](/docs/reference/engine/enums/RolloutState.md), it will use instances in the
legacy sound system such as [Sounds](/docs/reference/engine/classes/Sound.md).

### Property: SoundService.DefaultListenerLocation

```json
{
  "type": "ListenerLocation",
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
  "category": "Listening",
  "capabilities": [
    "Audio",
    "PluginOrOpenCloud"
  ]
}
```

Determines where to place an [AudioListener](/docs/reference/engine/classes/AudioListener.md) by default. The
[AudioListener](/docs/reference/engine/classes/AudioListener.md) will automatically be wired to a
[AudioDeviceOutput](/docs/reference/engine/classes/AudioDeviceOutput.md) and will have an empty
[AudioListener.InteractionGroup](/docs/reference/engine/classes/AudioListener.md) set.

See [ListenerLocation](/docs/reference/engine/enums/ListenerLocation.md) for detailed descriptions of each option.

### Property: SoundService.DistanceFactor

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
  "category": "Data",
  "capabilities": [
    "Audio"
  ]
}
```

The number of studs to be considered a meter by [SoundService](/docs/reference/engine/classes/SoundService.md) when
simulating the Doppler effect for [Sounds](/docs/reference/engine/classes/Sound.md). This impacts any
[Sound](/docs/reference/engine/classes/Sound.md) parented to a [BasePart](/docs/reference/engine/classes/BasePart.md) or [Attachment](/docs/reference/engine/classes/Attachment.md).

By default, this property is `3.33`, meaning that a meter is considered
3.33 studs for the purposes of simulating the Doppler effect. The greater
the [DistanceFactor](/docs/reference/engine/classes/SoundService.md), the faster the
listener has to travel relative to [Sounds](/docs/reference/engine/classes/Sound.md) in order to
experience the same Doppler shift.

It's recommended that you only change this property if the objects in your
experience are scaled differently from what they represent. For example,
if your character is meant to be very small (but is normal-sized in the
engine), you may want to increase [SoundService.DistanceFactor](/docs/reference/engine/classes/SoundService.md).

Note that this does not impact the behavior of instances in the advanced
audio system, such as [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) or [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md).

### Property: SoundService.DopplerScale

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
  "category": "Data",
  "capabilities": [
    "Audio"
  ]
}
```

This property determines the degree to which the pitch of a [Sound](/docs/reference/engine/classes/Sound.md)
varies due to the Doppler effect. This impacts any [Sound](/docs/reference/engine/classes/Sound.md) parented
to a [BasePart](/docs/reference/engine/classes/BasePart.md) or [Attachment](/docs/reference/engine/classes/Attachment.md).

The Doppler effect is a phenomenon whereby the pitch of a sound changes as
the source and observer of the sound move further away or closer together,
which is stronger the more quickly they are moving. Increasing
[SoundService.DopplerScale](/docs/reference/engine/classes/SoundService.md) exaggerates the impact of this effect,
whereas decreasing it minimizes it. By default, the value of this property
is `1`.

Note that this does not impact the behavior of instances in the advanced
audio system, such as [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) or [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md).

### Property: SoundService.ListenerCFrame

```json
{
  "type": "CFrame",
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
  "category": "Listening",
  "capabilities": [
    "Audio"
  ]
}
```

This property is only functional when
[ListenerType](/docs/reference/engine/classes/SoundService.md) is set to
[ListenerType.CFrame](/docs/reference/engine/enums/ListenerType.md). In that scenario, this property determines the
world space position from which 3D [Sounds](/docs/reference/engine/classes/Sound.md) are heard by the
player.

### Property: SoundService.ListenerObject

```json
{
  "type": "Instance",
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
  "category": "Listening",
  "capabilities": [
    "Audio"
  ]
}
```

This property is only functional when
[ListenerType](/docs/reference/engine/classes/SoundService.md) is set to
[ListenerType.ObjectPosition](/docs/reference/engine/enums/ListenerType.md) or [ListenerType.ObjectCFrame](/docs/reference/engine/enums/ListenerType.md). In
that scenario, this property determines which [Instance](/docs/reference/engine/classes/Instance.md) will be
used to determine the position from which 3D [Sounds](/docs/reference/engine/classes/Sound.md) are
heard by the player. This property can only be set to
[Instances](/docs/reference/engine/classes/Instance.md) with a position, such as a [BasePart](/docs/reference/engine/classes/BasePart.md) or
an [Attachment](/docs/reference/engine/classes/Attachment.md). If it is set to `nil`, 3D [Sounds](/docs/reference/engine/classes/Sound.md) will
not be heard by the player.

### Property: SoundService.ListenerType

```json
{
  "type": "ListenerType",
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
  "category": "Listening",
  "capabilities": [
    "Audio"
  ]
}
```

The listener type for any 3D [Sounds](/docs/reference/engine/classes/Sound.md) in the experience,
effectively the point from which 3D [Sound](/docs/reference/engine/classes/Sound.md) audio in the experience
is heard by the player. For [Sounds](/docs/reference/engine/classes/Sound.md) parented to a
[BasePart](/docs/reference/engine/classes/BasePart.md) or [Attachment](/docs/reference/engine/classes/Attachment.md), the listener influences the volume
and left/right balance of a playing sound. By default, this listener is
set to [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md).

Note that this does not affect the listener location when using the
advanced audio system; see [AudioListener](/docs/reference/engine/classes/AudioListener.md) for a way to set the
listener location within that system.

This property may not yet be enabled for all creators. Until full rollout,
use [SoundService:GetListener()](/docs/reference/engine/classes/SoundService.md) and
[SoundService:SetListener()](/docs/reference/engine/classes/SoundService.md) instead.

### Property: SoundService.RespectFilteringEnabled

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
  "category": "Data",
  "capabilities": [
    "Audio"
  ]
}
```

This property determines whether [Sound](/docs/reference/engine/classes/Sound.md) playback is replicated from
the client to the server, and therefore from the server. In other words,
when a [LocalScript](/docs/reference/engine/classes/LocalScript.md) calls [Play()](/docs/reference/engine/classes/Sound.md) and this
property is `true`, the sound will only play on the respective client. If
this property is `false`, other clients will also hear the sound.

Default is `true`, meaning filtering is enabled.

### Property: SoundService.RolloffScale

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
  "category": "Data",
  "capabilities": [
    "Audio"
  ]
}
```

Determines how fast the volume of a spatialized [Sound](/docs/reference/engine/classes/Sound.md) attenuates.
This impacts any [Sound](/docs/reference/engine/classes/Sound.md) parented to a [BasePart](/docs/reference/engine/classes/BasePart.md) or
[Attachment](/docs/reference/engine/classes/Attachment.md).

A higher [RolloffScale](/docs/reference/engine/classes/SoundService.md) means the volume
of a [Sound](/docs/reference/engine/classes/Sound.md) will attenuate more rapidly as the distance between the
listener and the [Sound](/docs/reference/engine/classes/Sound.md) grows. More precisely, the volume of
the [Sound](/docs/reference/engine/classes/Sound.md) will still start attenuating at a distance equal to
[Sound.RollOffMinDistance](/docs/reference/engine/classes/Sound.md), but the attenuation curve will be
steeper or more gradual based on the value of
[RolloffScale](/docs/reference/engine/classes/SoundService.md). Note that the
[Sound](/docs/reference/engine/classes/Sound.md) will still be inaudible past its the
[Sound.RollOffMaxDistance](/docs/reference/engine/classes/Sound.md) regardless of the value of
[SoundService.RolloffScale](/docs/reference/engine/classes/SoundService.md).

Note that this property does not affect the behavior of instances in the
advanced audio system, such as [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md). See
[AudioEmitter:SetDistanceAttenuation](/docs/reference/engine/classes/AudioEmitter.md) for a way to apply custom
attenuation in that system.

### Property: SoundService.VolumetricAudio

```json
{
  "type": "VolumetricAudio",
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
    "Audio"
  ]
}
```

Determines whether any [Sounds](/docs/reference/engine/classes/Sound.md) parented to a [Part](/docs/reference/engine/classes/Part.md)
emit volumetrically. If set to [VolumetricAudio.Enabled](/docs/reference/engine/enums/VolumetricAudio.md), the
[Sound](/docs/reference/engine/classes/Sound.md) will simulate being emitted from every point in the interior
of the [Part](/docs/reference/engine/classes/Part.md). If set to [VolumetricAudio.Disabled](/docs/reference/engine/enums/VolumetricAudio.md), the
[Sound](/docs/reference/engine/classes/Sound.md) will only emit from a single point in the center of the
[Part](/docs/reference/engine/classes/Part.md).

Note that this does not impact [Sounds](/docs/reference/engine/classes/Sound.md) parented to other
objects, such as [Attachments](/docs/reference/engine/classes/Attachment.md) or
[MeshParts](/docs/reference/engine/classes/MeshPart.md). This also does not impact the behavior of
instances in the advanced audio system such as [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md).

## Methods

### Method: SoundService:GetListener

**Signature:** `SoundService:GetListener(): Tuple`

Returns the current listener type used by [Sounds](/docs/reference/engine/classes/Sound.md) and what
object or position that listener is currently set to. This is the point
from which [Sound](/docs/reference/engine/classes/Sound.md) audio in the experience is heard by the player.
By default, the listener is set to [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md). The
listener can be changed using
[SetListener()](/docs/reference/engine/classes/SoundService.md).

Note that this does not affect the listener location when using the
advanced audio system. See [AudioListener](/docs/reference/engine/classes/AudioListener.md) for a way to set the
listener location in that system.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Tuple` — A table containing two results. The first result is the listener's
[ListenerType](/docs/reference/engine/enums/ListenerType.md) and the second result is dependent on that type:

| Listener Type | Description |
| --- | --- |
| [ListenerType.Camera](/docs/reference/engine/enums/ListenerType.md) | Does not return a listener object as [CurrentCamera](/docs/reference/engine/classes/Workspace.md) is always used. |
| [ListenerType.CFrame](/docs/reference/engine/enums/ListenerType.md) | Returns the [CFrame](/docs/reference/engine/datatypes/CFrame.md) used in [SetListener()](/docs/reference/engine/classes/SoundService.md). |
| [ListenerType.ObjectPosition](/docs/reference/engine/enums/ListenerType.md) | Returns the [BasePart](/docs/reference/engine/classes/BasePart.md) used in [SetListener()](/docs/reference/engine/classes/SoundService.md). |
| [ListenerType.ObjectCFrame](/docs/reference/engine/enums/ListenerType.md) | Returns the [BasePart](/docs/reference/engine/classes/BasePart.md) used in [SetListener()](/docs/reference/engine/classes/SoundService.md). |

### Method: SoundService:GetMixerTime

**Signature:** `SoundService:GetMixerTime(): double`

Returns a number in seconds that increases as the audio engine produces
output. Because this clock is derived from the number of audio samples the
mixer has processed, it is stable, sample-accurate, and monotonically
increasing, which makes it suitable for scheduling audible changes at
precise moments.

Use this value as the basis for the `atTime` argument of methods that
support scheduling playback to begin or end at an exact point in the
future, such as [Play()](/docs/reference/engine/classes/AudioPlayer.md) and
[Stop()](/docs/reference/engine/classes/AudioPlayer.md). Those methods expect times derived from
[GetMixerTime()](/docs/reference/engine/classes/SoundService.md).

Note, [GetMixerTime()](/docs/reference/engine/classes/SoundService.md) starts at an
arbitrary value, and can differ between machines. It is not suitable for
synchronizing audio across sessions or networks.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `double` — A number in seconds. This value is stable, sample-accurate, and
monotonically-increasing. It's intended to be used for scheduling
audible changes at precise times.

### Method: SoundService:OpenAttenuationCurveEditor

**Signature:** `SoundService:OpenAttenuationCurveEditor(selectedCurveObjects: Instances): ()`

Opens the attenuation curve editor in Studio for the provided
[AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) or [AudioListener](/docs/reference/engine/classes/AudioListener.md) instances.

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `selectedCurveObjects` | `Instances` |  | A list of [AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md) or [AudioListeners](/docs/reference/engine/classes/AudioListener.md). |

**Returns:** `()`

### Method: SoundService:OpenDirectionalCurveEditor

**Signature:** `SoundService:OpenDirectionalCurveEditor(selectedCurveObjects: Instances): ()`

Opens the directional curve editor in Studio for the provided
[AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) or [AudioListener](/docs/reference/engine/classes/AudioListener.md) instances. This method is
intended for use by Studio plugins that need to programmatically surface
the editor, in the same way a user would open it from the Properties
window.

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `selectedCurveObjects` | `Instances` |  | A list of [AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md) or [AudioListeners](/docs/reference/engine/classes/AudioListener.md). |

**Returns:** `()`

### Method: SoundService:PlayLocalSound

**Signature:** `SoundService:PlayLocalSound(sound: Instance): ()`

Plays a copy of a [Sound](/docs/reference/engine/classes/Sound.md) locally. The [Sound](/docs/reference/engine/classes/Sound.md) will only be
heard by the client calling this method, regardless of where it's parented
to.

Some properties of the [Sound](/docs/reference/engine/classes/Sound.md) will be carried over into the copy.
These include its [Sound.Volume](/docs/reference/engine/classes/Sound.md), [Sound.TimePosition](/docs/reference/engine/classes/Sound.md),
[Sound.PlaybackSpeed](/docs/reference/engine/classes/Sound.md), and any spatialization and effects that are
applied to it, including through [SoundGroups](/docs/reference/engine/classes/Sound.md).
Properties that do not affect the copy include [Sound.Looped](/docs/reference/engine/classes/Sound.md) and
[SoundService.AmbientReverb](/docs/reference/engine/classes/SoundService.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `sound` | `Instance` |  | The [Sound](/docs/reference/engine/classes/Sound.md) to be played. |

**Returns:** `()`

### Method: SoundService:SetListener

**Signature:** `SoundService:SetListener(listenerType: ListenerType, listener: Tuple): ()`

Sets the listener type for any [Sounds](/docs/reference/engine/classes/Sound.md) in the experience,
which defines the point from which [Sound](/docs/reference/engine/classes/Sound.md) audio in the experience
is heard by the player. For [Sounds](/docs/reference/engine/classes/Sound.md) parented to a
[BasePart](/docs/reference/engine/classes/BasePart.md) or [Attachment](/docs/reference/engine/classes/Attachment.md), the listener influences the volume
and left/right balance of a playing sound. By default, this listener is
set to [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md).

Note that this does not affect the listener location when using the
advanced audio system. See [AudioListener](/docs/reference/engine/classes/AudioListener.md) for a way to set the
listener location in that system.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `listenerType` | `ListenerType` |  | The [ListenerType](/docs/reference/engine/enums/ListenerType.md) of the listener. |
| `listener` | `Tuple` |  | Dependent on the [ListenerType](/docs/reference/engine/enums/ListenerType.md). Use a [BasePart](/docs/reference/engine/classes/BasePart.md) for [ListenerType.ObjectPosition](/docs/reference/engine/enums/ListenerType.md) or [ListenerType.ObjectCFrame](/docs/reference/engine/enums/ListenerType.md), a [CFrame](/docs/reference/engine/datatypes/CFrame.md) for [ListenerType.CFrame](/docs/reference/engine/enums/ListenerType.md), or `nil` for [ListenerType.Camera](/docs/reference/engine/enums/ListenerType.md). |

**Returns:** `()`

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