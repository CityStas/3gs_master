---
name: SecurityCapabilities
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A set of SecurityCapability items. See [script capabilities](/docs/en-us/scripting/capabilities.md)."
---

# SecurityCapabilities

A set of [SecurityCapability](/docs/reference/engine/enums/SecurityCapability.md) items. See
[script capabilities](/docs/en-us/scripting/capabilities.md).

**Type:** datatype

## Description

An immutable set of [SecurityCapability](/docs/reference/engine/enums/SecurityCapability.md) values that controls which
engine APIs and actions a script inside a sandboxed container can access.
Assign a `SecurityCapabilities` value to an instance's
[Capabilities](/docs/reference/engine/classes/Instance.md) property to restrict the scripts
beneath it.

Capability enforcement takes effect when
[Workspace.SandboxedInstanceMode](/docs/reference/engine/classes/Workspace.md) is set to
[SandboxedInstanceMode.Experimental](/docs/reference/engine/enums/SandboxedInstanceMode.md).

## Constructors

### SecurityCapabilities.new

**Signature:** `SecurityCapabilities.new(...: SecurityCapability)`

Returns a new set of capabilities from zero or more
[SecurityCapability](/docs/reference/engine/enums/SecurityCapability.md) items.

```lua
local capabilities = SecurityCapabilities.new(Enum.SecurityCapability.Players,
    Enum.SecurityCapability.Animation,
    Enum.SecurityCapability.Basic)

local newScript = Instance.new("Script")
newScript.Capabilities = capabilities
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `...` | `SecurityCapability` |  | Zero or more [SecurityCapability](/docs/reference/engine/enums/SecurityCapability.md) values to include in the new set. |

### SecurityCapabilities.fromCurrent

**Signature:** `SecurityCapabilities.fromCurrent()`

Returns a new set of capabilities from the capabilities of the calling
function.

## Methods

### SecurityCapabilities:Add

**Signature:** `SecurityCapabilities:Add(...: SecurityCapability): SecurityCapabilities`

Returns a new set of capabilities with zero or more additions. If you add
[SecurityCapability](/docs/reference/engine/enums/SecurityCapability.md) items that are already present, they are not
duplicated.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `...` | `SecurityCapability` |  | Zero or more [SecurityCapability](/docs/reference/engine/enums/SecurityCapability.md) values to add to the set. |

**Returns:** `SecurityCapabilities` — A new set containing the union of the original capabilities and the
specified additions.

### SecurityCapabilities:Add

**Signature:** `SecurityCapabilities:Add(capabilities: SecurityCapabilities): SecurityCapabilities`

Returns a new set of capabilities with the provided set added. If you add
[SecurityCapability](/docs/reference/engine/enums/SecurityCapability.md) items that are already present, they are not
duplicated.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `capabilities` | `SecurityCapabilities` |  | A `SecurityCapabilities` set whose items are added to the original. |

**Returns:** `SecurityCapabilities` — A new set containing the union of both sets.

### SecurityCapabilities:Remove

**Signature:** `SecurityCapabilities:Remove(...: SecurityCapability): SecurityCapabilities`

Returns a new set of capabilities with zero or more deletions.
[SecurityCapability](/docs/reference/engine/enums/SecurityCapability.md) items not present in the original set are
ignored.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `...` | `SecurityCapability` |  | Zero or more [SecurityCapability](/docs/reference/engine/enums/SecurityCapability.md) values to remove from the set. |

**Returns:** `SecurityCapabilities` — A new set with the specified capabilities removed.

### SecurityCapabilities:Remove

**Signature:** `SecurityCapabilities:Remove(capabilities: SecurityCapabilities): SecurityCapabilities`

Returns a new set of capabilities with the provided set deleted.
[SecurityCapability](/docs/reference/engine/enums/SecurityCapability.md) items not present in the original set are
ignored.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `capabilities` | `SecurityCapabilities` |  | A `SecurityCapabilities` set whose items are removed from the original. |

**Returns:** `SecurityCapabilities`

### SecurityCapabilities:Contains

**Signature:** `SecurityCapabilities:Contains(...: SecurityCapability): boolean`

Returns whether a set of capabilities contains the specified
[SecurityCapability](/docs/reference/engine/enums/SecurityCapability.md) items. The set must contain **all** provided
items to return true.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `...` | `SecurityCapability` |  | Zero or more [SecurityCapability](/docs/reference/engine/enums/SecurityCapability.md) values to check for membership in the set. |

**Returns:** `boolean`

### SecurityCapabilities:Contains

**Signature:** `SecurityCapabilities:Contains(capabilities: SecurityCapabilities): boolean`

Returns whether a set of capabilities contains another set of
capabilities. The set must contain **all** items in the provided set to
return true.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `capabilities` | `SecurityCapabilities` |  | A `SecurityCapabilities` set to check for membership in the original set. |

**Returns:** `boolean`