---
name: "Users"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 13
auth: [api-key, oauth2, cookie]
description: "Retrieve user information, manage inventories, and restrict users from your experience"
---

# Users

Retrieve user information, manage inventories, and restrict users from your experience. See the [Inventory Guide](/cloud/guides/inventory) for code examples.

Common use cases include:

- User lookup: [Search users by username](#users_get_v1_users_search) or ID and [retrieve profile information](#Cloud_GetUser)
- Avatar thumbnails: [Generate a user thumbnail](#Cloud_GenerateUserThumbnail) and [retrieve its generation operation](#Cloud_GetUserThumbnailGenerationOperation)
- Inventory access: [List user-owned items](#Cloud_ListInventoryItems), badges, and collectibles
- User restrictions: [Manage experience-level bans](#Cloud_UpdateUserRestriction__Using_Universes) and access restrictions

**Base URL:** `https://apis.roblox.com`

    ## Authentication

    Each endpoint requires one of the following authentication methods:

    - **API Key**: Pass your key in the `x-api-key` HTTP header. Create keys at [Creator Dashboard](https://create.roblox.com/dashboard/credentials).
- **OAuth 2.0**: Use Bearer token in the `Authorization` header. Authorization URL: `https://apis.roblox.com/oauth/v1/authorize`, Token URL: `https://apis.roblox.com/oauth/v1/token`
- **Cookie** *(not recommended)*: `.ROBLOSECURITY` cookie. Do not use in production.

    ```
    # API Key example
    curl -H "x-api-key: YOUR_API_KEY" https://apis.roblox.com/...

    # OAuth 2.0 example
    curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" https://apis.roblox.com/...
    ```

## Endpoints

### GET `/cloud/v2/universes/{universe_id}/subscription-products/{subscription_product_id}/subscriptions/{subscription_id}` [BETA]

Get Subscription

Get the subscription.

The `universe.subscription-product.subscription:read` scope only allows
reading subscriptions of the user making the request. Because of this, the
subscription ID must match the user ID of the user making the request. Note
that this scope might be more relevant for OAuth 2.0 apps.

To read all subscriptions made by users for a particular universe, use the
`universe:write` scope instead.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:write`, `universe.subscription-product.subscription:read`, `universe:write`, `universe.subscription-product.subscription:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `subscription_product_id` | path | `string` | Yes | The subscription-product ID. |
| `subscription_id` | path | `string` | Yes | The subscription ID. |
| `view` | query | `VIEW_UNSPECIFIED \| BASIC \| FULL` | No | The view in which to retrieve the subscription.  Supports BASIC and FULL.  Defaults to BASIC.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| VIEW_UNSPECIFIED \| The subscription view is not specified; the default will be used. \|   \| BASIC \| Includes only the `active` and `renewing` fields. \|   \| FULL \| Includes all fields. \| Valid values: `VIEW_UNSPECIFIED`, `BASIC`, `FULL` |

**Responses:**

- `200`: OK → `Subscription`

**Response fields** (`Subscription`)

See [Subscription](#subscription) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "active": false,
  "willRenew": false,
  "lastBillingTime": "2024-01-01T00:00:00Z"
}
```

**Rate Limits:** perApiKeyOwner: 500/minute, perOauth2Authorization: 3/second

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/subscription-products/{SUBSCRIPTION_PRODUCT_ID}/subscriptions/{SUBSCRIPTION_ID}"
```

### GET `/cloud/v2/users/{user_id}` [STABLE]

Get User

Gets a user's basic and advanced information.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `user.advanced:read`, `user.social:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `user_id` | path | `string` | Yes | The user ID. |

**Responses:**

- `200`: OK → `OpenCloudUsers.User`

**Response fields** (`OpenCloudUsers.User`)

See [OpenCloudUsers.User](#opencloudusers-user) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "id": "string",
  "name": "string",
  "displayName": "string",
  "about": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000/minute, perOauth2Authorization: 10/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/users/{USER_ID}"
```

### GET `/v1/display-names/validate`

Validate a display name for a new user.

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `displayName` | query | `string` | Yes | The display name. |
| `birthdate` | query | `string` | Yes | The new user's birthdate |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Display name is too short 2: Display name is too long 3: Display name contains invalid characters 4: Display name has been moderated 6: Request must contain a birthdate 8: Display name has too many combinations of character sets
- `429`: 5: Display name updates for this user have been throttled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/display-names/validate?displayName={VALUE}&birthdate={VALUE}"
```

### POST `/v1/user/get-tags` [EXPERIMENTAL]

Gets the tags for multiple users

**Server:** `https://contacts.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Contacts.Api.Request.GetUserTagsRequestModel`

See [Roblox.Contacts.Api.Request.GetUserTagsRequestModel](#roblox-contacts-api-request-getusertagsrequestmodel) in Models.

**Request example:**
```json
{
  "targetUserIds": [
    0
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Contacts.Api.Response.GetUserTagsResponseModel[]`
- `400`: 4: Invalid parameters. 8: Too many user Tags are requested.
- `401`: 0: Authorization has been denied for this request.
- `429`: 10: The flood limit has been exceeded.

**Response fields** (`Roblox.Contacts.Api.Response.GetUserTagsResponseModel[]`)

See [Roblox.Contacts.Api.Response.GetUserTagsResponseModel](#roblox-contacts-api-response-getusertagsresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://contacts.roblox.com/v1/user/get-tags" \
  -H "Content-Type: application/json" \
  -d '{
  "targetUserIds": [
    0
  ]
}'
```

### POST `/v1/user/tag` [EXPERIMENTAL]

Sets the tag for a user

**Server:** `https://contacts.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Contacts.Api.Request.SetUserTagRequestModel`

See [Roblox.Contacts.Api.Request.SetUserTagRequestModel](#roblox-contacts-api-request-setusertagrequestmodel) in Models.

**Request example:**
```json
{
  "targetUserId": 0,
  "userTag": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Contacts.Api.Response.SetUserTagResponseModel`
- `400`: 2: The target user is invalid or does not exist. 4: Invalid parameters. 6: The userTag is too long.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 5: The user cannot tag themselves.
- `429`: 10: The flood limit has been exceeded.

**Response fields** (`Roblox.Contacts.Api.Response.SetUserTagResponseModel`)

See [Roblox.Contacts.Api.Response.SetUserTagResponseModel](#roblox-contacts-api-response-setusertagresponsemodel) in Models.

**Response example:**
```json
{
  "status": "Success"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://contacts.roblox.com/v1/user/tag" \
  -H "Content-Type: application/json" \
  -d '{
  "targetUserId": 0,
  "userTag": "string"
}'
```

### GET `/v1/user/tag/validate` [EXPERIMENTAL]

Validates the tag for a user

**Server:** `https://contacts.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `alias` | query | `string` | No | The tag to validate |

**Responses:**

- `200`: OK → `Roblox.Contacts.Api.Response.ValidateUserTagResponseModel`
- `400`: 4: Invalid parameters.
- `401`: 0: Authorization has been denied for this request.
- `429`: 10: The flood limit has been exceeded.

**Response fields** (`Roblox.Contacts.Api.Response.ValidateUserTagResponseModel`)

See [Roblox.Contacts.Api.Response.ValidateUserTagResponseModel](#roblox-contacts-api-response-validateusertagresponsemodel) in Models.

**Response example:**
```json
{
  "status": "Success"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://contacts.roblox.com/v1/user/tag/validate"
```

### POST `/v1/usernames/users`

Get users by usernames.

This endpoint will also check previous usernames.
Does not require X-CSRF-Token protection because this is essentially a get request but as a POST to avoid URI limits.

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Users.Api.MultiGetByUsernameRequest`

See [Roblox.Users.Api.MultiGetByUsernameRequest](#roblox-users-api-multigetbyusernamerequest) in Models.

**Request example:**
```json
{
  "usernames": [
    "string"
  ],
  "excludeBannedUsers": false
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Users.Api.MultiGetUserByNameResponse_`
- `400`: 2: Too many usernames.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Users.Api.MultiGetUserByNameResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Users.Api.MultiGetUserByNameResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-users-api-multigetuserbynameresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "requestedUsername": "...",
      "hasVerifiedBadge": "...",
      "id": "...",
      "name": "...",
      "displayName": "..."
    }
  ]
}
```

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/usernames/users" \
  -H "Content-Type: application/json" \
  -d '{
  "usernames": [
    "string"
  ],
  "excludeBannedUsers": false
}'
```

### POST `/v1/users`

Get users by ids.

Does not require X-CSRF-Token protection because this is essentially a get request but as a POST to avoid URI limits.

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Users.Api.MultiGetByUserIdRequest`

See [Roblox.Users.Api.MultiGetByUserIdRequest](#roblox-users-api-multigetbyuseridrequest) in Models.

**Request example:**
```json
{
  "userIds": [
    0
  ],
  "excludeBannedUsers": false
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Users.Api.MultiGetUserResponse_`
- `400`: 1: Too many ids.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Users.Api.MultiGetUserResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Users.Api.MultiGetUserResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-users-api-multigetuserresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "hasVerifiedBadge": "...",
      "id": "...",
      "name": "...",
      "displayName": "..."
    }
  ]
}
```

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/users" \
  -H "Content-Type: application/json" \
  -d '{
  "userIds": [
    0
  ],
  "excludeBannedUsers": false
}'
```

### GET `/v1/users/search`

Searches for users by keyword.

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `keyword` | query | `string` | Yes | The search keyword. |
| `sessionId` | query | `string` | No |  |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Users.Api.SearchGetUserResponse_`
- `400`: 5: The keyword was filtered. 6: The keyword is too short.
- `429`: 4: Too many requests.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Users.Api.SearchGetUserResponse_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Users.Api.SearchGetUserResponse_](#roblox-web-webapi-models-apipageresponse-roblox-users-api-searchgetuserresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "previousUsernames": "...",
      "hasVerifiedBadge": "...",
      "id": "...",
      "name": "...",
      "displayName": "..."
    }
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/users/search?keyword={VALUE}"
```

### GET `/v1/users/{userId}/display-names/validate`

Validate a display name for an existing user.

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user id. |
| `displayName` | query | `string` | Yes | The display name. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Display name is too short 2: Display name is too long 3: Display name contains invalid characters 4: Display name has been moderated 8: Display name has too many combinations of character sets
- `401`: 0: Authorization has been denied for this request.
- `403`: 7: The user id is invalid.
- `429`: 5: Display name updates for this user have been throttled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/users/{USERID}/display-names/validate?displayName={VALUE}"
```

### GET `/v2/users/{userId}/transaction-totals`

**Server:** `https://economy.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `usedTypes` | query | `integer` | No |  |
| `timeFrame` | query | `any` | No |  |
| `transactionType` | query | `any` | No |  |
| `exclusiveStartCursor` | query | `any` | No |  |

**Responses:**

- `200`: OK → `TransactionTotalsResponse`

**Response fields** (`TransactionTotalsResponse`)

See [TransactionTotalsResponse](#transactiontotalsresponse) in Models.

**Response example:**
```json
{
  "salesTotal": 0,
  "purchasesTotal": 0,
  "affiliateSalesTotal": 0,
  "groupPayoutsTotal": 0,
  "currencyPurchasesTotal": 0,
  "premiumStipendsTotal": 0
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://economy.roblox.com/v2/users/{USERID}/transaction-totals"
```

### GET `/v2/users/{userId}/transaction-types`

**Server:** `https://economy.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `TransactionUsedTypesResponse`

**Response fields** (`TransactionUsedTypesResponse`)

See [TransactionUsedTypesResponse](#transactionusedtypesresponse) in Models.

**Response example:**
```json
{
  "HasPurchase": false,
  "HasSale": false,
  "HasAffiliatePayout": false,
  "HasAffiliateSale": false,
  "HasGroupPayout": false,
  "HasCurrencyPurchase": false
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://economy.roblox.com/v2/users/{USERID}/transaction-types"
```

### GET `/v2/users/{userId}/transactions`

**Server:** `https://economy.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `exclusiveStartCursor` | query | `any` | No |  |
| `transactionType` | query | `any` | No |  |
| `itemPricingType` | query | `any` | No |  |

**Responses:**

- `200`: OK → `TransactionRecordResponseApiPageResponse`

**Response fields** (`TransactionRecordResponseApiPageResponse`)

See [TransactionRecordResponseApiPageResponse](#transactionrecordresponseapipageresponse) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "idHash": "...",
      "transactionType": "...",
      "created": "...",
      "isPending": "...",
      "agent": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://economy.roblox.com/v2/users/{USERID}/transactions"
```

## Models

### Subscription

Represents a user's subscription to a subscription product. The
subscription ID is the same as the user ID of the user who subscribed.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the subscription.  Format: `universes/{universe_id}/subscription-products/{subscription_product_id}/subscriptions/{subscription_id}` |
| `createTime` | `string` | No | The timestamp when the subscription was created. |
| `updateTime` | `string` | No | The timestamp when the subscription was last updated. |
| `active` | `boolean` | No | Whether the subscription is active.  This is equivalent  to whether `state` is equal to SUBSCRIBED_WILL_RENEW, SUBSCRIBED_WILL_NOT_RENEW, or SUBSCRIBED_RENEWAL_PAYMENT_PENDING. |
| `willRenew` | `boolean` | No | Whether the subscription will renew.  This is equivalent to whether `state` is equal to SUBSCRIBED_WILL_RENEW or SUBSCRIBED_RENEWAL_PAYMENT_PENDING. |
| `lastBillingTime` | `string` | No | The timestamp when the subscription was last billed. |
| `nextRenewTime` | `string` | No | The timestamp when the subscription will next be automatically renewed. |
| `expireTime` | `string` | No | The timestamp when the subscription will, or did, expire. |
| `state` | `STATE_UNSPECIFIED \| SUBSCRIBED_WILL_RENEW \| SUBSCRIBED_WILL_NOT_RENEW \| SUBSCRIBED_RENEWAL_PAYMENT_PENDING \| EXPIRED` | No | The state of the subscription.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| STATE_UNSPECIFIED \| The subscription state is unspecified. \|   \| SUBSCRIBED_WILL_RENEW \| The subscription is active and will be automatically renewed at `next_renew_time`. \|   \| SUBSCRIBED_WILL_NOT_RENEW \| The subscription is active but will not be automatically renewed. \|   \| SUBSCRIBED_RENEWAL_PAYMENT_PENDING \| The subscription is active and within the renewal grace period pending payment confirmation. \|   \| EXPIRED \| The subscription has expired.  See `expiration_details` for more information. \| |
| `expirationDetails` | `Subscription_ExpirationDetails` | No | Information about the expiration of the subscription. |
| `purchasePlatform` | `PURCHASE_PLATFORM_UNSPECIFIED \| DESKTOP \| MOBILE` | No | The platform on which the subscription was purchased.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| PURCHASE_PLATFORM_UNSPECIFIED \| The purchase platform is unspecified. \|   \| DESKTOP \| The subscription was purchased on the Roblox website. \|   \| MOBILE \| The subscription was purchased on the Roblox mobile app. \| |
| `paymentProvider` | `string enum (6 values)` | No | The payment provider used to purchase the subscription.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| PAYMENT_PROVIDER_UNSPECIFIED \| The payment provider is unspecified. \|   \| STRIPE \| The subscription was purchased using Stripe. \|   \| APPLE \| The subscription was purchased using Apple. \|   \| GOOGLE \| The subscription was purchased using Google. \|   \| ROBLOX_CREDIT \| The subscription was purchased using Roblox Credit. \|   \| ROBUX \| The subscription was purchased using Robux. \| Values: PAYMENT_PROVIDER_UNSPECIFIED, STRIPE, APPLE, GOOGLE, ROBLOX_CREDIT, ROBUX |
| `user` | `string` | No |  *(immutable)* The user who subscribed to the subscription. |

### OpenCloudUsers.User

Represents any registered user of Roblox.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the user.              Format: `users/{user_id}` |
| `createTime` | `string` | No | The timestamp at which the user was created. |
| `id` | `string` | No | Unique ID that identifies a user in Roblox. |
| `name` | `string` | No | Unique username for a user in Roblox. |
| `displayName` | `string` | No | Display name for the user. |
| `about` | `string` | No | User-defined information about themselves. |
| `locale` | `string` | No | Current locale selected by the user. Returns IETF language code. |
| `premium` | `boolean` | No | Whether the user is a premium user. |
| `idVerified` | `boolean` | No | Specifies if the user is identity-verified. Verification includes, but isn't limited to, non-VoIP phone numbers or government IDs.              To access this data, you need an API key / OAuth token with the following scope: user.advanced:read. The field is omitted from the response when the caller is not authorized to read it. |
| `socialNetworkProfiles` | `any` | No | User's social network profiles and visibility. |

### Roblox.Contacts.Api.Request.GetUserTagsRequestModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetUserIds` | `integer[]` | No |  |

### Roblox.Contacts.Api.Response.GetUserTagsResponseModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetUserId` | `integer` | No |  |
| `targetUserTag` | `string` | No |  |

### Roblox.Contacts.Api.Request.SetUserTagRequestModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetUserId` | `integer` | No | The userId of the target of the userTag. |
| `userTag` | `string` | No | The userTag to be set |

### Roblox.Contacts.Api.Response.SetUserTagResponseModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | `Success \| Moderated` | No | Status message to be sent to the setter of the userTag ['Success' = 0, 'Moderated' = 1] |

### Roblox.Contacts.Api.Response.ValidateUserTagResponseModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | `Success \| Moderated \| TooLong` | No | Status message to be sent to the requester of the userTag validation ['Success' = 0, 'Moderated' = 1, 'TooLong' = 2] |

### Roblox.Users.Api.MultiGetByUsernameRequest

Request model for getting users by usernames.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `usernames` | `string[]` | No | The usernames. |
| `excludeBannedUsers` | `boolean` | No | Whether the response should exclude banned users |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Users.Api.MultiGetUserByNameResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Users.Api.MultiGetUserByNameResponse[]` | No |  |

### Roblox.Users.Api.MultiGetByUserIdRequest

Request model for getting users by ids.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userIds` | `integer[]` | No | The user ids. |
| `excludeBannedUsers` | `boolean` | No | Whether the response should exclude banned users |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Users.Api.MultiGetUserResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Users.Api.MultiGetUserResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Users.Api.SearchGetUserResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Users.Api.SearchGetUserResponse[]` | No |  |

### TransactionTotalsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `salesTotal` | `integer` | No |  |
| `purchasesTotal` | `integer` | No |  |
| `affiliateSalesTotal` | `integer` | No |  |
| `groupPayoutsTotal` | `integer` | No |  |
| `currencyPurchasesTotal` | `integer` | No |  |
| `premiumStipendsTotal` | `integer` | No |  |
| `tradeSystemEarningsTotal` | `integer` | No |  |
| `tradeSystemCostsTotal` | `integer` | No |  |
| `premiumPayoutsTotal` | `integer` | No |  |
| `groupPremiumPayoutsTotal` | `integer` | No |  |
| `adSpendTotal` | `integer` | No |  |
| `developerExchangeTotal` | `integer` | No |  |
| `pendingRobuxTotal` | `integer` | No |  |
| `incomingRobuxTotal` | `integer` | No |  |
| `outgoingRobuxTotal` | `integer` | No |  |
| `individualToGroupTotal` | `integer` | No |  |
| `csAdjustmentTotal` | `integer` | No |  |
| `adsRevsharePayoutsTotal` | `integer` | No |  |
| `groupAdsRevsharePayoutsTotal` | `integer` | No |  |
| `subscriptionsRevshareTotal` | `integer` | No |  |
| `groupSubscriptionsRevshareTotal` | `integer` | No |  |
| `subscriptionsRevshareOutgoingTotal` | `integer` | No |  |
| `groupSubscriptionsRevshareOutgoingTotal` | `integer` | No |  |
| `publishingAdvanceRebatesTotal` | `integer` | No |  |
| `affiliatePayoutTotal` | `integer` | No |  |
| `licensingPaymentTotal` | `integer` | No |  |
| `licensingPaymentClawbackOutgoingTotal` | `integer` | No |  |
| `incomingRobuxTransferTotal` | `integer` | No |  |
| `outgoingRobuxTransferTotal` | `integer` | No |  |
| `robloxSelectIncomingTotal` | `integer` | No |  |
| `robloxSelectOutgoingTotal` | `integer` | No |  |
| `privateServerEngagementPayoutsTotal` | `integer` | No |  |
| `creatorRewardsPayoutsTotal` | `integer` | No |  |
| `subscriptionReferralPayoutsTotal` | `integer` | No |  |

### TransactionUsedTypesResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `HasPurchase` | `boolean` | No |  |
| `HasSale` | `boolean` | No |  |
| `HasAffiliatePayout` | `boolean` | No |  |
| `HasAffiliateSale` | `boolean` | No |  |
| `HasGroupPayout` | `boolean` | No |  |
| `HasCurrencyPurchase` | `boolean` | No |  |
| `HasTradeRobux` | `boolean` | No |  |
| `HasPremiumStipend` | `boolean` | No |  |
| `HasEngagementPayout` | `boolean` | No |  |
| `HasGroupEngagementPayout` | `boolean` | No |  |
| `HasAdSpend` | `boolean` | No |  |
| `HasDevEx` | `boolean` | No |  |
| `HasPendingRobux` | `boolean` | No |  |
| `HasIndividualToGroup` | `boolean` | No |  |
| `HasCSAdjustment` | `boolean` | No |  |
| `HasAdsRevsharePayout` | `boolean` | No |  |
| `HasGroupAdsRevsharePayout` | `boolean` | No |  |
| `HasSubscriptionsRevsharePayout` | `boolean` | No |  |
| `HasGroupSubscriptionsRevsharePayout` | `boolean` | No |  |
| `HasPublishingAdvanceRebates` | `boolean` | No |  |
| `HasLicensingPayment` | `boolean` | No |  |
| `HasTransfer` | `boolean` | No |  |
| `HasRobloxSelectTransfer` | `boolean` | No |  |
| `HasPrivateServerEngagementPayout` | `boolean` | No |  |
| `HasCreatorRewardsPayout` | `boolean` | No |  |
| `HasSubscriptionReferralPayout` | `boolean` | No |  |
| `HasGifts` | `boolean` | No |  |

### TransactionRecordResponseApiPageResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `TransactionRecordResponse[]` | No |  |