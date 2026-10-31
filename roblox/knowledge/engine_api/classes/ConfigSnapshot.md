---
name: ConfigSnapshot
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "A snapshot of configuration values at a given version. Can be player-specific."
---

# Class: ConfigSnapshot

> A snapshot of configuration values at a given version. Can be player-specific.

## Description

An object with the configuration values at a specific version. A snapshot can
be targeted to a single player to apply experimentation values. This is
returned by [ConfigService:GetConfigAsync()](/docs/reference/engine/classes/ConfigService.md) and
[ConfigService:GetConfigForPlayerAsync()](/docs/reference/engine/classes/ConfigService.md).

For more information, see
[Experience configs](/docs/en-us/production/configs.md).

## Properties

### Property: ConfigSnapshot.Error

```json
{
  "type": "ConfigSnapshotErrorState",
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
    "Basic"
  ]
}
```

Populated if snapshot was in an error state.

### Property: ConfigSnapshot.Outdated

```json
{
  "type": "boolean",
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
    "Basic"
  ]
}
```

If true, indicates the snapshot is outdated and can be refreshed to newer
values.

## Methods

### Method: ConfigSnapshot:GetValue

**Signature:** `ConfigSnapshot:GetValue(key: string): Variant`

Returns the value for the provided key in the snapshot.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | Key of the configuration to get the value for. |

**Returns:** `Variant` — The value of the configuration for the given key.

### Method: ConfigSnapshot:GetValueChangedSignal

**Signature:** `ConfigSnapshot:GetValueChangedSignal(key: string): RBXScriptSignal`

Returns a signal that fires when the value for the provided key changes
after calling [ConfigSnapshot:Refresh()](/docs/reference/engine/classes/ConfigSnapshot.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | Key of the configuration to get the change signal for. |

**Returns:** `RBXScriptSignal` — A `DataType.RBXScriptSignal` that fires when the value for the given
key changes upon refresh.

### Method: ConfigSnapshot:Refresh

**Signature:** `ConfigSnapshot:Refresh(): ()`

Refreshes the snapshot to the latest configuration values from the
service. If not called, the snapshot will continue to reflect the values
at the time it was created or last refreshed.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `()`

## Events

### Event: ConfigSnapshot.UpdateAvailable

**Signature:** `ConfigSnapshot.UpdateAvailable()`

Fires when a newer version of the configuration is available than the
current snapshot. You can perform validation and/or call
[ConfigSnapshot:Refresh()](/docs/reference/engine/classes/ConfigSnapshot.md) to update to the latest values.

*Security: None · Capabilities: Basic*

## Inherited Members

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some