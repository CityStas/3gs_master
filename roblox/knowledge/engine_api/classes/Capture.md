---
name: Capture
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "A class which defines a piece of content, such as a screenshot or video, taken in-experience."
---

# Class: Capture

> A class which defines a piece of content, such as a screenshot or video, taken
> in-experience.

## Description

Represents a single piece of content — a screenshot or a video — captured
within an experience. A [Capture](/docs/reference/engine/classes/Capture.md) records metadata about that content,
including when it was taken ([Capture.CaptureTime](/docs/reference/engine/classes/Capture.md)), what kind of
content it is ([Capture.CaptureType](/docs/reference/engine/classes/Capture.md)), the place and experience it
originated from ([Capture.SourcePlaceId](/docs/reference/engine/classes/Capture.md) and
[Capture.SourceUniverseId](/docs/reference/engine/classes/Capture.md)), and where its underlying file is stored
([Capture.LocalId](/docs/reference/engine/classes/Capture.md) and [Capture.FilePathString](/docs/reference/engine/classes/Capture.md)).

## Properties

### Property: Capture.CaptureTime

```json
{
  "type": "DateTime",
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

The date and time at which the capture was taken, as a
[DateTime](/docs/reference/engine/datatypes/DateTime.md). It defaults to the moment the [Capture](/docs/reference/engine/classes/Capture.md) is
created. This property is read-only.

### Property: Capture.CaptureType

```json
{
  "type": "CaptureType",
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

Indicates the kind of content the capture holds, as an [CaptureType](/docs/reference/engine/enums/CaptureType.md)
value. Defaults to [CaptureType.Screenshot](/docs/reference/engine/enums/CaptureType.md). This property is
read-only.

### Property: Capture.FilePathString

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

The path to the capture's file on the local filesystem, returned as a
string. It resolves to the file backing the capture in local capture
storage, or an empty string when no file is associated with the capture.
This property is read-only.

### Property: Capture.LocalId

```json
{
  "type": "string",
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

A local identifier for the capture's stored file, in the form
`rbxtemp://<key>`. It is empty until the capture has been saved to local
capture storage, after which it references the stored file by key. This
property is read-only.

### Property: Capture.SourcePlaceId

```json
{
  "type": "int64",
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

The [PlaceId](/docs/reference/engine/classes/DataModel.md) of the place in which the capture
was taken. Defaults to `0` when the source place is unknown or unset. This
property is read-only.

### Property: Capture.SourceUniverseId

```json
{
  "type": "int64",
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

The universe (experience) ID of the experience in which the capture was
taken. Defaults to `0` when the source universe is unknown or unset. This
property is read-only.

## Inherited Members

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some