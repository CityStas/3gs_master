---
name: VideoCapture
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Capture
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "A child class of Capture for videos."
---

# Class: VideoCapture

> A child class of [Capture](/docs/reference/engine/classes/Capture.md) for videos.

## Properties

### Property: VideoCapture.FilePath

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Capture"
  ]
}
```

Requires `RobloxScript` security; experience scripts cannot read it even
when they hold the [VideoCapture](/docs/reference/engine/classes/VideoCapture.md) object. Absolute path on the
user's device to the video file this capture represents: the temporary
file while recording is in progress, or, after
[PromptSaveCapturesToGallery()](/docs/reference/engine/classes/CaptureService.md),
the permanent gallery location. Defaults to an empty string until a
recording has produced a video file.

### Property: VideoCapture.TimeLength

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Capture"
  ]
}
```

Duration of the video capture, in seconds. Populated once recording
finishes, whether via
[StopVideoCapture()](/docs/reference/engine/classes/CaptureService.md) or because
the capture's time limit was reached. Defaults to `0` until recording has
finished.

## Inherited Members

### From [Capture](/docs/reference/engine/classes/Capture.md)

- **Property `CaptureTime`** (`DateTime`): The date and time at which the capture was taken.
- **Property `CaptureType`** (`CaptureType`): Indicates whether the capture is a screenshot or a video.
- **Property `FilePathString`** (`string`): The local filesystem path to the capture's file, as a string.
- **Property `LocalId`** (`string`): A temporary local identifier for the capture's stored file.
- **Property `SourcePlaceId`** (`int64`): The ID of the place in which the capture was taken.
- **Property `SourceUniverseId`** (`int64`): The ID of the experience in which the capture was taken.

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some