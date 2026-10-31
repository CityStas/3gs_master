---
name: ScreenshotCapture
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Capture
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "A child class of Capture for screenshots."
---

# Class: ScreenshotCapture

> A child class of [Capture](/docs/reference/engine/classes/Capture.md) for screenshots.

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