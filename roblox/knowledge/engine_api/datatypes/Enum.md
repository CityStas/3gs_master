---
name: Enum
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A data type that represents an individual enum."
---

# Enum

A data type that represents an individual enum.

**Type:** datatype

## Description

The [Enum](/docs/reference/engine/datatypes/Enum.md) data type represents an individual enum in Roblox. An
individual enum can be indexed through the [Enums](/docs/reference/engine/datatypes/Enums.md) type, via the name
of the enum itself.

## Methods

### Enum:GetEnumItems

**Signature:** `Enum:GetEnumItems(): Array`

Returns an array of all the [EnumItem](/docs/reference/engine/datatypes/EnumItem.md) options available for this
enum.

**Returns:** `Array` — An array of all [EnumItem](/docs/reference/engine/datatypes/EnumItem.md) values belonging to this enum.

### Enum:FromName

**Signature:** `Enum:FromName(name: string): Enum | nil`

Returns either the converted [Enum](/docs/reference/engine/datatypes/Enum.md) or `nil`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The name of the EnumItem to look up in this enum. |

**Returns:** `Enum | nil` — The [EnumItem](/docs/reference/engine/datatypes/EnumItem.md) whose Name matches the given string, or nil if
no match exists.

### Enum:FromValue

**Signature:** `Enum:FromValue(value: number): Enum | nil`

Returns either the converted [Enum](/docs/reference/engine/datatypes/Enum.md) or `nil`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `value` | `number` |  | The integer value of the EnumItem to look up in this enum. |

**Returns:** `Enum | nil` — The [EnumItem](/docs/reference/engine/datatypes/EnumItem.md) whose integer value matches the given number,
or nil if no match exists.