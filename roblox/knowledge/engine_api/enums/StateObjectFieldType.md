---
name: StateObjectFieldType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Identifies the data type of a field in a deprecated `StateObject`; all values are deprecated and the enum is retained only for backward compatibility."
---

# StateObjectFieldType

Identifies the data type of a field in a deprecated `StateObject`; all values
are deprecated and the enum is retained only for backward compatibility.

**Type:** enum

## Description

`StateObjectFieldType` formerly described the data type of a field within a
`StateObject`. All enum values are deprecated. The enum itself is not used by
engine code and is preserved solely so that existing creator scripts that
reference it continue to function. New code should not depend on this enum.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Boolean` | 0 | A boolean field. |
| `CFrame` | 1 | A [CFrame](/docs/reference/engine/datatypes/CFrame.md) field. |
| `Color3` | 2 | A [Color3](/docs/reference/engine/datatypes/Color3.md) field. |
| `Float` | 3 | A floating-point number field. |
| `Instance` | 4 | An [Instance](/docs/reference/engine/classes/Instance.md) reference field. |
| `Random` | 5 | A [Random](/docs/reference/engine/datatypes/Random.md) field. |
| `Vector2` | 6 | A [Vector2](/docs/reference/engine/datatypes/Vector2.md) field. |
| `Vector3` | 7 | A [Vector3](/docs/reference/engine/datatypes/Vector3.md) field. |
| `INVALID` | 8 | An invalid or unrecognized field type. |