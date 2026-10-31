---
name: VideoSampler
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "An object for sampling frames from video content."
---

# Class: VideoSampler

> An object for sampling frames from video content.

## Description

This object lets you get image frames from selected timestamps of a video. To
create a [VideoSampler](/docs/reference/engine/classes/VideoSampler.md), call
[VideoService:CreateVideoSamplerAsync()](/docs/reference/engine/classes/VideoService.md).

## Properties

### Property: VideoSampler.TimeLength

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
    "UI"
  ]
}
```

The length of the [VideoContent](/docs/reference/engine/classes/VideoSampler.md) in
seconds.

### Property: VideoSampler.VideoContent

```json
{
  "type": "Content",
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
    "UI"
  ]
}
```

The asset loaded into the [VideoSampler](/docs/reference/engine/classes/VideoSampler.md).

## Methods

### Method: VideoSampler:GetSamplesAtTimesAsync

**Signature:** `VideoSampler:GetSamplesAtTimesAsync(times: Array): List<VideoSample>`

This method allows you to get a set of image frames from a video at
specified timestamps as image [Content](/docs/reference/engine/datatypes/Content.md) objects.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `times` | `Array` |  | An array of requested timestamps in seconds for which to retrieve image frames. Each timestamp should be a number between `0` and [TimeLength](/docs/reference/engine/classes/VideoSampler.md). |

**Returns:** `List<VideoSample>` — An array of dictionary or nil values for each requested timestamp. If
a requested timestamp is out of range or the [VideoSampler](/docs/reference/engine/classes/VideoSampler.md) was
unable to produce a sample, the corresponding entry in the returned
array will be nil.

Each dictionary contains the following keys:

- `Time` (number): The timestamp of the returned image frame in
  seconds. This value may differ slightly from the requested
  timestamp.
- `Image` ([Content](/docs/reference/engine/datatypes/Content.md)): A [Content](/docs/reference/engine/datatypes/Content.md) with a
  [SourceType](/docs/reference/engine/datatypes/Content.md) of
  [ContentSourceType.Opaque](/docs/reference/engine/enums/ContentSourceType.md) containing the image frame at the
  corresponding timestamp.

## Inherited Members

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some