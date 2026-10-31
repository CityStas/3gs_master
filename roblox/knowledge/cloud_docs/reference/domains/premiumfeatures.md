---
name: "PremiumFeatures Api v1"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://premiumfeatures.roblox.com"
versions: [v1]
endpoints: 2
auth: [cookie]
---

# PremiumFeatures Api v1

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://premiumfeatures.roblox.com`
**Versions:** v1

## Endpoints

### GET `/v1/users/{userId}/premium-upsell-precheck`

Premium upsell precheck

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | User ID |
| `universeId` | query | `integer (int64)` | Yes |  |
| `placeId` | query | `integer (int64)` | Yes |  |

**Responses:**

- `200`: OK
- `401`: 0: Authorization has been denied for this request.

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://premiumfeatures.roblox.com/v1/users/{USERID}/premium-upsell-precheck?universeId={VALUE}&placeId={VALUE}"
```

### GET `/v1/users/{userId}/validate-membership`

Get if a user has a Premium membership

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | User ID |

**Responses:**

- `200`: OK
- `401`: 0: Authorization has been denied for this request.

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://premiumfeatures.roblox.com/v1/users/{USERID}/validate-membership"
```