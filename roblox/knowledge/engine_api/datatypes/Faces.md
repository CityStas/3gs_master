---
name: Faces
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A data type containing six booleans, each representing a face of a BasePart."
---

# Faces

A data type containing six booleans, each representing a face of a
[BasePart](/docs/reference/engine/classes/BasePart.md).

**Type:** datatype

## Description

The [Faces](/docs/reference/engine/datatypes/Faces.md) data type contains six booleans representing whether a
feature is enabled for each face ([NormalId](/docs/reference/engine/enums/NormalId.md)) of a Part. In other words,
this contains a boolean for each axes (X/Y/Z) in both directions
(positive/negative). The [Handles](/docs/reference/engine/classes/Handles.md) object uses this data type to enable
whether a direction has a visible handle on a Part's face.

```lua
local handles = Instance.new("Handles")
handles.Faces = Faces.new(Enum.NormalId.Front, Enum.NormalId.Left)
```

Like most data types on Roblox, the `Faces` data type is immutable and you
cannot assign to its properties once created.

## Constructors

### Faces.new

**Signature:** `Faces.new(normalIds...: Tuple)`

Creates a new `Faces` given some number of [NormalId](/docs/reference/engine/enums/NormalId.md) as arguments.
Each [NormalId](/docs/reference/engine/enums/NormalId.md) provided indicates the property of the same name in
the new `Faces` will be `true`.

- The [table.unpack()](/docs/reference/engine/globals/table.md) function can be used to unpack a table of
  NormalId to be included.
- Passing values that are not a [NormalId](/docs/reference/engine/enums/NormalId.md) will do nothing; they are
  ignored silently.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `normalIds...` | `Tuple` |  | Any number of [NormalId](/docs/reference/engine/enums/NormalId.md) values indicating which faces to enable in the new `Faces`. |

## Properties

### Faces.Top

**Type:** `bool`

Whether the top face (positive **Y** direction, corresponding to
[NormalId.Top](/docs/reference/engine/enums/NormalId.md)) is included in this [Faces](/docs/reference/engine/datatypes/Faces.md) value. Defaults
to `false` when [NormalId.Top](/docs/reference/engine/enums/NormalId.md) is not passed to the
[Faces.new()](/docs/reference/engine/datatypes/Faces.md) constructor.

### Faces.Bottom

**Type:** `bool`

Whether the bottom face (negative **Y** direction, corresponding to
[NormalId.Bottom](/docs/reference/engine/enums/NormalId.md)) is included in this [Faces](/docs/reference/engine/datatypes/Faces.md) value.
Defaults to `false` when [NormalId.Bottom](/docs/reference/engine/enums/NormalId.md) is not passed to the
[Faces.new()](/docs/reference/engine/datatypes/Faces.md) constructor.

### Faces.Left

**Type:** `bool`

Whether the left face (negative **X** direction, corresponding to
[NormalId.Left](/docs/reference/engine/enums/NormalId.md)) is included in this [Faces](/docs/reference/engine/datatypes/Faces.md) value. Defaults
to `false` when [NormalId.Left](/docs/reference/engine/enums/NormalId.md) is not passed to the
[Faces.new()](/docs/reference/engine/datatypes/Faces.md) constructor.

### Faces.Right

**Type:** `bool`

Whether the right face (positive **X** direction, corresponding to
[NormalId.Right](/docs/reference/engine/enums/NormalId.md)) is included in this [Faces](/docs/reference/engine/datatypes/Faces.md) value.
Defaults to `false` when [NormalId.Right](/docs/reference/engine/enums/NormalId.md) is not passed to the
[Faces.new()](/docs/reference/engine/datatypes/Faces.md) constructor.

### Faces.Back

**Type:** `bool`

Whether the back face (positive **Z** direction, corresponding to
[NormalId.Back](/docs/reference/engine/enums/NormalId.md)) is included in this [Faces](/docs/reference/engine/datatypes/Faces.md) value. Defaults
to `false` when [NormalId.Back](/docs/reference/engine/enums/NormalId.md) is not passed to the
[Faces.new()](/docs/reference/engine/datatypes/Faces.md) constructor.

### Faces.Front

**Type:** `bool`

Whether the front face (negative **Z** direction, corresponding to
[NormalId.Front](/docs/reference/engine/enums/NormalId.md)) is included in this [Faces](/docs/reference/engine/datatypes/Faces.md) value.
Defaults to `false` when [NormalId.Front](/docs/reference/engine/enums/NormalId.md) is not passed to the
[Faces.new()](/docs/reference/engine/datatypes/Faces.md) constructor.