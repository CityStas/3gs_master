---
name: Enums
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A root access point of all Enums."
---

# Enums

A root access point of all [Enums](/docs/reference/engine/datatypes/Enum.md).

**Type:** datatype

## Description

The [Enums](/docs/reference/engine/datatypes/Enums.md) data type, more commonly known as [Enum](/docs/reference/engine/datatypes/Enum.md) by its
global variable in Luau), acts as the root access point for all available
enums on Roblox. All enums on Roblox are indexed via their name through this
data type, and developers can also utilize the `GetEnums()` method to get a
list of all enums on Roblox.

## Methods

### Enums:GetEnums

**Signature:** `Enums:GetEnums(): Array`

Returns an array containing all available [Enums](/docs/reference/engine/datatypes/Enum.md) on Roblox.

**Returns:** `Array`