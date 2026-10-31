---
name: AnalyticsCustomFieldKeys
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used to form a dictionary of custom fields to provide breakdowns in Roblox-provided charts."
---

# AnalyticsCustomFieldKeys

Used to form a dictionary of custom fields to provide breakdowns in
Roblox-provided charts.

**Type:** enum

## Description

Used to form a dictionary of custom fields to provide breakdowns in
Roblox-provided charts. For example:

```lua
local customFields = {
	[Enum.AnalyticsCustomFieldKeys.CustomField01.Name] = "value1",
	[Enum.AnalyticsCustomFieldKeys.CustomField02.Name] = "value2",
	[Enum.AnalyticsCustomFieldKeys.CustomField03.Name] = "value3",
}
```

## Items

| Name | Value | Description |
|------|-------|-------------|
| `CustomField01` | 0 | The first custom field key, used to provide a breakdown dimension in Roblox-provided analytics charts. |
| `CustomField02` | 1 | The second custom field key, used to provide a breakdown dimension in Roblox-provided analytics charts. |
| `CustomField03` | 2 | The third custom field key, used to provide a breakdown dimension in Roblox-provided analytics charts. |