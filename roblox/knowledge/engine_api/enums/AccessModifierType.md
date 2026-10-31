---
name: AccessModifierType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines whether an AudioDeviceInput user ID access list acts as an allow-list or a deny-list."
---

# AccessModifierType

Determines whether an [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) user ID access list acts as an
allow-list or a deny-list.

**Type:** enum

## Description

Determines whether the user IDs supplied to
[SetUserIdAccessList()](/docs/reference/engine/classes/AudioDeviceInput.md) are
treated as an allow-list or a deny-list for hearing a particular
[AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md).

The default [AccessType](/docs/reference/engine/classes/AudioDeviceInput.md) is
[AccessModifierType.Deny](/docs/reference/engine/enums/AccessModifierType.md), meaning all users can hear the device unless
explicitly excluded.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Allow` | 0 | User IDs in the access list are permitted to hear the [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) - all other users are blocked. |
| `Deny` | 1 | User IDs in the access list are blocked from hearing the [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) - all other users are permitted. |