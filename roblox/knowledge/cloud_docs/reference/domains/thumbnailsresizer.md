---
name: "ThumbnailsResizer Api v1"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://thumbnailsresizer.roblox.com"
versions: [v1]
endpoints: 2
auth: [cookie]
---

# ThumbnailsResizer Api v1

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://thumbnailsresizer.roblox.com`
**Versions:** v1

## Endpoints

### GET `/v1/resize/{hash}/{width}/{height}/{type}/{format}/{filterType}`

Resizes larger thumbnails to specified size and format

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `hash` | path | `string` | Yes | Hash of larger thumbnail |
| `width` | path | `integer (int32)` | Yes | Desired width of thumbnail |
| `height` | path | `integer (int32)` | Yes | Desired height of thumbnail |
| `type` | path | `string` | Yes | Thumbnail Type |
| `format` | path | `string` | Yes | Desired image format of the thumbnail |
| `filterType` | query | `string` | Yes | E.g. is output circular |
| `shouldModify` | query | `boolean` | No |  |

**Responses:**

- `200`: OK

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://thumbnailsresizer.roblox.com/v1/resize/{HASH}/{WIDTH}/{HEIGHT}/{TYPE}/{FORMAT}/{filterType}?filterType={VALUE}"
```

### GET `/v1/secureresize/{thumbPrint}/{hash}/{width}/{height}/{type}/{format}/{filterType}`

Decrypts and Resizes larger thumbnails to specified size and format

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `thumbPrint` | path | `string` | Yes | The thumbPrint that represents the key version |
| `hash` | path | `string` | Yes | Hash of larger thumbnail |
| `width` | path | `integer (int32)` | Yes | Desired width of thumbnail |
| `height` | path | `integer (int32)` | Yes | Desired height of thumbnail |
| `type` | path | `string` | Yes | Thumbnail Type |
| `format` | path | `string` | Yes | Desired image format of the thumbnail |
| `filterType` | query | `string` | No | E.g. is output circular |

**Responses:**

- `200`: OK

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://thumbnailsresizer.roblox.com/v1/secureresize/{THUMBPRINT}/{HASH}/{WIDTH}/{HEIGHT}/{TYPE}/{FORMAT}/{filterType}"
```