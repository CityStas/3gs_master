---
name: ServiceVisibility
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls when a service is displayed in the Explorer window in Roblox Studio."
---

# ServiceVisibility

Controls when a service is displayed in the Explorer window in Roblox Studio.

**Type:** enum

## Description

Controls when a service is displayed in the Explorer panel in Roblox Studio.
This enum is used by the `ServiceVisibility` property on
[ReflectionMetadataClass](/docs/reference/engine/classes/ReflectionMetadataClass.md), which defines the default explorer visibility
for a service class. It does not affect whether the service is accessible via
[GetService()](/docs/reference/engine/classes/ServiceProvider.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Always` | 0 | The service is always visible in the Explorer window. |
| `Off` | 1 | The service is hidden from the Explorer window by default, but can still be added via the Insert Service menu. |
| `WithChildren` | 2 | The service is visible in the Explorer window only when it has children; it can still be added via the Insert Service menu. |