---
name: Content
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Represents a reference to asset content stored externally or as an object within the place."
---

# Content

Represents a reference to asset content stored externally or as an object
within the place.

**Type:** datatype

## Description

The `Content` data type represents a reference to asset content stored
externally or as an object within the place, wrapping a single value of one of
the supported [ContentSourceType](/docs/reference/engine/enums/ContentSourceType.md) values.

##### Warning

Replication is not yet supported for [Object](/docs/reference/engine/datatypes/Content.md) values.
When an [Instance](/docs/reference/engine/classes/Instance.md) with a [Content](/docs/reference/engine/datatypes/Content.md) property containing a
[Object](/docs/reference/engine/datatypes/Content.md) value is replicated, an unusable placeholder
[Object](/docs/reference/engine/classes/Object.md) of the same type will be used instead of the [Object](/docs/reference/engine/classes/Object.md)
itself, and any attempt to read or write the contents of that placeholder
object will throw. These placeholder objects will render as a cyan and magenta
checkerboard pattern.

This will be replaced with standard replication behavior in the future. For
now, do not use [EditableImage](/docs/reference/engine/classes/EditableImage.md) or [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) as
[Content](/docs/reference/engine/datatypes/Content.md) on the server on an [Instance](/docs/reference/engine/classes/Instance.md) that can replicate to
clients.

## Constructors

### Content.fromUri

**Signature:** `Content.fromUri(uri: string)`

Returns a new `Content` with an
[asset URI](/docs/en-us/projects/assets.md#asset-uris) `string` value
referencing content external to the place.

[Content.SourceType](/docs/reference/engine/datatypes/Content.md) will be [Uri](/docs/reference/engine/enums/ContentSourceType.md), and
[Content.Uri](/docs/reference/engine/datatypes/Content.md) will contain a non‑`nil` `string` value.

If `uri` is empty, [Content.none](/docs/reference/engine/datatypes/Content.md) will be returned instead.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `uri` | `string` |  | The [asset URI](/docs/en-us/projects/assets.md#asset-uris) string. |

### Content.fromAssetId

**Signature:** `Content.fromAssetId(assetId: number)`

Returns a new `Content` from a numeric asset ID. This is a convenience
constructor equivalent to calling
`Content.fromUri("rbxassetid://" .. tostring(assetId))`.

[Content.SourceType](/docs/reference/engine/datatypes/Content.md) will be [Uri](/docs/reference/engine/enums/ContentSourceType.md), and
[Content.Uri](/docs/reference/engine/datatypes/Content.md) will contain the formatted `rbxassetid://` URI
string.

If `assetId` is `0`, [Content.none](/docs/reference/engine/datatypes/Content.md) will be returned instead.

Throws if `assetId` is non‑finite, for example [math.huge()](/docs/reference/engine/globals/math.md) or
`0/0`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetId` | `number` |  | The numeric asset ID. |

### Content.fromObject

**Signature:** `Content.fromObject(object: Object)`

Returns a new `Content` with a strong reference to an [Object](/docs/reference/engine/classes/Object.md).

[Content.SourceType](/docs/reference/engine/datatypes/Content.md) will be [Object](/docs/reference/engine/enums/ContentSourceType.md), and
[Content.Object](/docs/reference/engine/datatypes/Content.md) will contain a non‑`nil` [Object](/docs/reference/engine/classes/Object.md)
reference.

[Content.Object](/docs/reference/engine/datatypes/Content.md) references are **strong** references that hold
**shared ownership** of the [Object](/docs/reference/engine/classes/Object.md). Any [Content.Object](/docs/reference/engine/datatypes/Content.md)
reference will extend the lifetime of that [Object](/docs/reference/engine/classes/Object.md) and prevent it
from being garbage collected.

Throws if `object` is `nil`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `object` | `Object` |  | The [Object](/docs/reference/engine/classes/Object.md) to reference. |

## Constants

| Name | Type | Description |
|------|------|-------------|
| `Content.none` | `Content` | An empty `Content` value with [Content.SourceType](/docs/reference/engine/datatypes/Content.md) of [None](/docs/reference/engine/enums/ContentSourceType.md). |

## Properties

### Content.SourceType

**Type:** `Enum.ContentSourceType`

The source type of the contained value. Indicates which property contains
a non‑`nil` value.

### Content.Uri

**Type:** `string?`

A URI `string` if [Content.SourceType](/docs/reference/engine/datatypes/Content.md) is
[Uri](/docs/reference/engine/enums/ContentSourceType.md), otherwise `nil`.

### Content.Object

**Type:** `Object?`

A reference to a non-`nil` [Object](/docs/reference/engine/classes/Object.md) if [Content.SourceType](/docs/reference/engine/datatypes/Content.md)
is [Object](/docs/reference/engine/enums/ContentSourceType.md), otherwise `nil`.

### Content.Opaque

**Type:** `Opaque?`

A reference to a non-`nil` `Opaque` content if
[Content.SourceType](/docs/reference/engine/datatypes/Content.md) is [Opaque](/docs/reference/engine/enums/ContentSourceType.md),
otherwise `nil`.