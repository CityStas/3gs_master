---
name: ListenerLocation
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Enum used with SoundService.DefaultListenerLocation to determine where an AudioListener is placed by default."
---

# ListenerLocation

Enum used with [SoundService.DefaultListenerLocation](/docs/reference/engine/classes/SoundService.md) to determine where
an [AudioListener](/docs/reference/engine/classes/AudioListener.md) is placed by default.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Behavior depends on the value of [VoiceChatService.EnableDefaultVoice](/docs/reference/engine/classes/VoiceChatService.md) and [VoiceChatService.UseAudioApi](/docs/reference/engine/classes/VoiceChatService.md). When using the default voice setup with the audio API, this behaves similarly to `Camera`. |
| `None` | 1 | No [AudioListener](/docs/reference/engine/classes/AudioListener.md) will be created by default, but they can be created separately by scripts. |
| `Character` | 2 | All of the following, resulting in the world being heard from the position of your character while matching the orientation of your camera.  - An [Attachment](/docs/reference/engine/classes/Attachment.md) will be created and parented to the   [PrimaryPart](/docs/reference/engine/classes/Model.md) of the local player's   [Character](/docs/reference/engine/classes/Player.md) model.  - An [AudioListener](/docs/reference/engine/classes/AudioListener.md) will be created and parented to the   [Attachment](/docs/reference/engine/classes/Attachment.md).  - An [AudioDeviceOutput](/docs/reference/engine/classes/AudioDeviceOutput.md) will be created and parented to   [SoundService](/docs/reference/engine/classes/SoundService.md).  - A [Wire](/docs/reference/engine/classes/Wire.md) will be created and parented to the previously-created   [AudioListener](/docs/reference/engine/classes/AudioListener.md). The wire's   [SourceInstance](/docs/reference/engine/classes/Wire.md) will be set to the   previously-created [AudioListener](/docs/reference/engine/classes/AudioListener.md) and its   [TargetInstance](/docs/reference/engine/classes/Wire.md) will be set to the   previously-created [AudioDeviceOutput](/docs/reference/engine/classes/AudioDeviceOutput.md).  - The previously-created [Attachment](/docs/reference/engine/classes/Attachment.md) will be updated once per frame   to face the same direction as [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md). |
| `Camera` | 3 | All of the following, resulting in the world being heard from the perspective (postition and orientation) of the camera.  - An [AudioListener](/docs/reference/engine/classes/AudioListener.md) will be created and parented to   [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md). - An [AudioDeviceOutput](/docs/reference/engine/classes/AudioDeviceOutput.md) will be created and parented to   [SoundService](/docs/reference/engine/classes/SoundService.md). - A [Wire](/docs/reference/engine/classes/Wire.md) will be created and parented to the previously-created   [AudioListener](/docs/reference/engine/classes/AudioListener.md). The wire's   [SourceInstance](/docs/reference/engine/classes/Wire.md) will be set to the   previously-created [AudioListener](/docs/reference/engine/classes/AudioListener.md) and its   [TargetInstance](/docs/reference/engine/classes/Wire.md) will be set to the   previously-created [AudioDeviceOutput](/docs/reference/engine/classes/AudioDeviceOutput.md). |