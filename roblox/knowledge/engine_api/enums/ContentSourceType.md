---
name: ContentSourceType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The source type of a Content value."
---

# ContentSourceType

The source type of a [Content](/docs/reference/engine/datatypes/Content.md) value.

**Type:** enum

## Description

The source type of [Content](/docs/reference/engine/datatypes/Content.md) value. Indicates which properties of a
[Content](/docs/reference/engine/datatypes/Content.md) contain the referenced content.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | Empty value with no source type. Does not reference any content or hold any non‑`nil` value. |
| `Uri` | 1 | An [asset URI](/docs/en-us/projects/assets.md#asset-uris) `string` value contained in [Content.Uri](/docs/reference/engine/datatypes/Content.md). |
| `Object` | 2 | A non-`nil` [Object](/docs/reference/engine/classes/Object.md) reference contained in [Content.Object](/docs/reference/engine/datatypes/Content.md). |
| `Opaque` | 3 | A non-`nil` `Opaque` reference contained in [Content.Opaque](/docs/reference/engine/datatypes/Content.md). |