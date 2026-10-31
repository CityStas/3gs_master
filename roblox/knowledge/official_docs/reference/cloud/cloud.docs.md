---
name: "Cloud API"
last_updated: 2026-10-30T19:55:51Z
type: opencloud
api_base_url: "https://apis.roblox.com"
version: "2.0.1"
endpoints: 75
description: "The Roblox Open Cloud v2 API"
---

# Cloud API

The Roblox Open Cloud v2 API. This is a subset of endpoints that Roblox
provides. See https://create.roblox.com/docs/cloud/open-cloud for more
details.

**API Version:** 2.0.1

**Base URL(s):**
- `https://apis.roblox.com`

## Endpoints

### POST `/cloud/v2/creator-store-products`

Create Creator Store Product

Add a Creator Store product. Only use this method if your product has never
been distributed on the Creator Store; otherwise, use the `PATCH` method to
update the product.

**Scopes:** `creator-store-product:write`

**Request Body:** `application/json` — Type: `CreatorStoreProduct`

See [CreatorStoreProduct](#creatorstoreproduct) in Models.

**Request example:**
```json
{
  "path": "string",
  "basePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "purchasePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "published": false,
  "restrictions": [
    "RESTRICTION_UNSPECIFIED"
  ],
  "purchasable": false
}
```

**Responses:**

- `200`: OK → `CreatorStoreProduct`

**Response fields** (`CreatorStoreProduct`)

See [CreatorStoreProduct](#creatorstoreproduct) in Models.

**Response example:**
```json
{
  "path": "string",
  "basePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "purchasePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "published": false,
  "restrictions": [
    "RESTRICTION_UNSPECIFIED"
  ],
  "purchasable": false
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/creator-store-products" \
  -H "Content-Type: application/json" \
  -d '{"path":"string","basePrice":{"currencyCode":"string","quantity":{"significand":"...","exponent":"..."}},"purchasePrice":{"currencyCode":"string","quantity":{"significand":"...","exponent":"..."}},"published":false,"restrictions":["RESTRICTION_UNSPECIFIED"],"purchasable":false}'
```

### GET `/cloud/v2/creator-store-products/{creator_store_product_id}`

Get Creator Store Product

Get a Creator Store product.

**Scopes:** `creator-store-product:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `creator_store_product_id` | path | `string` | Yes | The creator-store-product ID. |

**Responses:**

- `200`: OK → `CreatorStoreProduct`

**Response fields** (`CreatorStoreProduct`)

See [CreatorStoreProduct](#creatorstoreproduct) in Models.

**Response example:**
```json
{
  "path": "string",
  "basePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "purchasePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "published": false,
  "restrictions": [
    "RESTRICTION_UNSPECIFIED"
  ],
  "purchasable": false
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/creator-store-products/{CREATOR_STORE_PRODUCT_ID}"
```

### PATCH `/cloud/v2/creator-store-products/{creator_store_product_id}`

Update Creator Store Product

Update a Creator Store product.

**Scopes:** `creator-store-product:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `creator_store_product_id` | path | `string` | Yes | The creator-store-product ID. |
| `updateMask` | query | `string` | No | The list of fields to update. |
| `allowMissing` | query | `boolean` | No | If set to true, and the creator store product is not found, a creator store product is created. In this situation, `update_mask` is ignored. |

**Request Body:** `application/json` — Type: `CreatorStoreProduct`

See [CreatorStoreProduct](#creatorstoreproduct) in Models.

**Request example:**
```json
{
  "path": "string",
  "basePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "purchasePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "published": false,
  "restrictions": [
    "RESTRICTION_UNSPECIFIED"
  ],
  "purchasable": false
}
```

**Responses:**

- `200`: OK → `CreatorStoreProduct`

**Response fields** (`CreatorStoreProduct`)

See [CreatorStoreProduct](#creatorstoreproduct) in Models.

**Response example:**
```json
{
  "path": "string",
  "basePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "purchasePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "published": false,
  "restrictions": [
    "RESTRICTION_UNSPECIFIED"
  ],
  "purchasable": false
}
```

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/creator-store-products/{CREATOR_STORE_PRODUCT_ID}" \
  -H "Content-Type: application/json" \
  -d '{"path":"string","basePrice":{"currencyCode":"string","quantity":{"significand":"...","exponent":"..."}},"purchasePrice":{"currencyCode":"string","quantity":{"significand":"...","exponent":"..."}},"published":false,"restrictions":["RESTRICTION_UNSPECIFIED"],"purchasable":false}'
```

### GET `/cloud/v2/groups/{group_id}`

Get Group

Gets the specified group.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `group_id` | path | `string` | Yes | The group ID. |

**Responses:**

- `200`: OK → `Group`

**Response fields** (`Group`)

See [Group](#group) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "id": "string",
  "displayName": "string",
  "description": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}"
```

### GET `/cloud/v2/groups/{group_id}/forum-categories`

List Group Forum Categories

Lists forum categories in the group. Supports filtering.

**Scopes:** `group-forum:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `group_id` | path | `string` | Yes | The group ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of group forum categories to return. The service might return fewer than this value. If unspecified, at most 10 group forum categories are returned. The maximum value is 10 and higher values are set to 10. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  Filtering conforms to Common Expression Language (CEL). Only the boolean field `archived` and `==` operator are supported. If `archived=false`, archived categories are not returned. The default value is `false`. Example: `"filter=archived==true"` |

**Responses:**

- `200`: OK → `ListGroupForumCategoriesResponse`

**Response fields** (`ListGroupForumCategoriesResponse`)

See [ListGroupForumCategoriesResponse](#listgroupforumcategoriesresponse) in Models.

**Response example:**
```json
{
  "groupForumCategories": [
    {
      "path": "...",
      "createTime": "...",
      "updateTime": "...",
      "groupForumCategoryId": "...",
      "displayName": "...",
      "creator": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/forum-categories"
```

### GET `/cloud/v2/groups/{group_id}/forum-categories/{forum_category_id}/posts`

List Group Forum Posts

Lists forum posts in the group's forum category. Supports filtering.

**Scopes:** `group-forum:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `group_id` | path | `string` | Yes | The group ID. |
| `forum_category_id` | path | `string` | Yes | The forum-category ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of group forum posts to return. The service might return fewer than this value. If unspecified, at most 10 group forum posts are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  Filtering conforms to Common Expression Language (CEL). Only the query `filter=pinned==true` is supported, where only pinned posts are returned. `filter=pinned==false`is not supported. |
| `view` | query | `VIEW_UNSPECIFIED \| FULL \| FULL_WITH_FIRST_COMMENT` | No | The view in which to retrieve the group forum post.  Supports FULL and FULL_WITH_FIRST_COMMENT.  Defaults to FULL.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| VIEW_UNSPECIFIED \| The group forum post view is not specified; the default will be used. \|   \| FULL \| Includes all fields but does not dereference `first_comment`. Only the `path` field is populated. \|   \| FULL_WITH_FIRST_COMMENT \| Includes all fields and also fully populates `first_comment`. The default view. \| Valid values: `VIEW_UNSPECIFIED`, `FULL`, `FULL_WITH_FIRST_COMMENT` |

**Responses:**

- `200`: OK → `ListGroupForumPostsResponse`

**Response fields** (`ListGroupForumPostsResponse`)

See [ListGroupForumPostsResponse](#listgroupforumpostsresponse) in Models.

**Response example:**
```json
{
  "groupForumPosts": [
    {
      "path": "...",
      "createTime": "...",
      "updateTime": "...",
      "pinned": "...",
      "locked": "...",
      "groupForumPostId": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/forum-categories/{FORUM_CATEGORY_ID}/posts"
```

### GET `/cloud/v2/groups/{group_id}/forum-categories/{forum_category_id}/posts/{post_id}/comments`

List Group Forum Comments

Lists forum comments on a group's forum post. Supports filtering.

**Scopes:** `group-forum:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `group_id` | path | `string` | Yes | The group ID. |
| `forum_category_id` | path | `string` | Yes | The forum-category ID. |
| `post_id` | path | `string` | Yes | The post ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of group forum comments to return. The service might return fewer than this value. If unspecified, at most 10 group forum comments are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  Filtering conforms to Common Expression Language (CEL). Only the string field `repliesToCommentId` and the `==` operator are supported. If `repliesToCommentId` is specified, only comments that respond to the comment are returned. The default value is `''`. If `repliesToCommentId=''`, only comments responding directly to the post are returned. Example: `"filter=repliesToCommentId==01234567-89ab-cdef-0123-456789abcdef"` |

**Responses:**

- `200`: OK → `ListGroupForumCommentsResponse`

**Response fields** (`ListGroupForumCommentsResponse`)

See [ListGroupForumCommentsResponse](#listgroupforumcommentsresponse) in Models.

**Response example:**
```json
{
  "groupForumComments": [
    {
      "path": "...",
      "groupForumCommentId": "...",
      "message": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/forum-categories/{FORUM_CATEGORY_ID}/posts/{POST_ID}/comments"
```

### GET `/cloud/v2/groups/{group_id}/join-requests`

List Group Join Requests

List join requests under a group. Supports filtering.

**Scopes:** `group:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `group_id` | path | `string` | Yes | The group ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of group join requests to return. The service might return fewer than this value. If unspecified, at most 10 group join requests are returned. The maximum value is 20 and higher values are set to 20. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  Filtering conforms to Common Expression Language (CEL). Only the `user` field and `==` operator are supported.   Example: `"user == 'users/156'"` |

**Responses:**

- `200`: OK → `ListGroupJoinRequestsResponse`

**Response fields** (`ListGroupJoinRequestsResponse`)

See [ListGroupJoinRequestsResponse](#listgroupjoinrequestsresponse) in Models.

**Response example:**
```json
{
  "groupJoinRequests": [
    {
      "path": "...",
      "createTime": "...",
      "user": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/join-requests"
```

### POST `/cloud/v2/groups/{group_id}/join-requests/{join_request_id}:accept`

Accept Group Join Request

Accepts a join request.

**Scopes:** `group:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `group_id` | path | `string` | Yes | The group ID. |
| `join_request_id` | path | `string` | Yes | The join-request ID. |

**Request Body:** `application/json` — Type: `AcceptGroupJoinRequestRequest`

See [AcceptGroupJoinRequestRequest](#acceptgroupjoinrequestrequest) in Models.

**Request example:**
```json
{}
```

**Responses:**

- `200`: OK

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/join-requests/{JOIN_REQUEST_ID}:accept" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST `/cloud/v2/groups/{group_id}/join-requests/{join_request_id}:decline`

Decline Group Join Request

Declines a join request.

**Scopes:** `group:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `group_id` | path | `string` | Yes | The group ID. |
| `join_request_id` | path | `string` | Yes | The join-request ID. |

**Request Body:** `application/json` — Type: `DeclineGroupJoinRequestRequest`

See [DeclineGroupJoinRequestRequest](#declinegroupjoinrequestrequest) in Models.

**Request example:**
```json
{}
```

**Responses:**

- `200`: OK

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/join-requests/{JOIN_REQUEST_ID}:decline" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### GET `/cloud/v2/groups/{group_id}/memberships`

List Group Memberships

List group members in a group. Supports filtering.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `group_id` | path | `string` | Yes | The group ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of group memberships to return. The service might return fewer than this value. If unspecified, at most 10 group memberships are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  See the [filtering](/docs/en-us/cloud/reference/patterns.md#list-group-memberships) documentation for more information. |

**Responses:**

- `200`: OK → `ListGroupMembershipsResponse`

**Response fields** (`ListGroupMembershipsResponse`)

See [ListGroupMembershipsResponse](#listgroupmembershipsresponse) in Models.

**Response example:**
```json
{
  "groupMemberships": [
    {
      "path": "...",
      "createTime": "...",
      "updateTime": "...",
      "user": "...",
      "role": "...",
      "roles": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/memberships"
```

### PATCH `/cloud/v2/groups/{group_id}/memberships/{membership_id}`

Update Group Membership

**Deprecated.** Use AssignGroupRole and UnassignGroupRole instead.
Updates the group membership for a particular group member. This action
requires the requester to be able to assign or remove roles below their
highest role. The requester cannot change their own roles.

**Scopes:** `group:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `group_id` | path | `string` | Yes | The group ID. |
| `membership_id` | path | `string` | Yes | The membership ID. |

**Request Body:** `application/json` — Type: `GroupMembership`

See [GroupMembership](#groupmembership) in Models.

**Request example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "role": "string",
  "roles": [
    "string"
  ]
}
```

**Responses:**

- `200`: OK → `GroupMembership`

**Response fields** (`GroupMembership`)

See [GroupMembership](#groupmembership) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "role": "string",
  "roles": [
    "string"
  ]
}
```

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/memberships/{MEMBERSHIP_ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "role": "string",
  "roles": [
    "string"
  ]
}'
```

### POST `/cloud/v2/groups/{group_id}/memberships/{membership_id}:assignRole`

Assign Role Group Membership

Assigns a specific role to a user within a group. If the user already
holds the specified role, no action is taken.

**Scopes:** `group:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `group_id` | path | `string` | Yes | The group ID. |
| `membership_id` | path | `string` | Yes | The membership ID. |

**Request Body:** `application/json` — Type: `AssignRoleGroupMembershipRequest`

See [AssignRoleGroupMembershipRequest](#assignrolegroupmembershiprequest) in Models.

**Request example:**
```json
{
  "role": "string"
}
```

**Responses:**

- `200`: OK → `GroupMembership`

**Response fields** (`GroupMembership`)

See [GroupMembership](#groupmembership) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "role": "string",
  "roles": [
    "string"
  ]
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/memberships/{MEMBERSHIP_ID}:assignRole" \
  -H "Content-Type: application/json" \
  -d '{
  "role": "string"
}'
```

### POST `/cloud/v2/groups/{group_id}/memberships/{membership_id}:unassignRole`

Unassign Role Group Membership

Unassigns a specific role from a user within a group. If the user does
not hold the specified role, no action is taken.

**Scopes:** `group:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `group_id` | path | `string` | Yes | The group ID. |
| `membership_id` | path | `string` | Yes | The membership ID. |

**Request Body:** `application/json` — Type: `UnassignRoleGroupMembershipRequest`

See [UnassignRoleGroupMembershipRequest](#unassignrolegroupmembershiprequest) in Models.

**Request example:**
```json
{
  "role": "string"
}
```

**Responses:**

- `200`: OK → `GroupMembership`

**Response fields** (`GroupMembership`)

See [GroupMembership](#groupmembership) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "role": "string",
  "roles": [
    "string"
  ]
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/memberships/{MEMBERSHIP_ID}:unassignRole" \
  -H "Content-Type: application/json" \
  -d '{
  "role": "string"
}'
```

### GET `/cloud/v2/groups/{group_id}/roles`

List Group Roles

List roles in a group.

Roles can be public or private. The response includes private roles and
their fields only when the acting user is permitted to view them. The
endpoint does not provide a public-roles-only view.

The permissions field for roles is viewable based on the requester's access
and scopes.

Permissions for the guest role are always visible - a scope is not needed.

If the requester is a member of the group and has the `group:read` scope,
permissions in their role are visible.

If the requester is the owner of the group and has the `group:read` scope,
permissions in all roles are visible.

**Scopes:** `group:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `group_id` | path | `string` | Yes | The group ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of group roles to return. The service might return fewer than this value. If unspecified, at most 10 group roles are returned. The maximum value is 20 and higher values are set to 20. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |

**Responses:**

- `200`: OK → `ListGroupRolesResponse`

**Response fields** (`ListGroupRolesResponse`)

See [ListGroupRolesResponse](#listgrouprolesresponse) in Models.

**Response example:**
```json
{
  "groupRoles": [
    {
      "path": "...",
      "createTime": "...",
      "updateTime": "...",
      "id": "...",
      "displayName": "...",
      "description": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/roles"
```

### GET `/cloud/v2/groups/{group_id}/roles/{role_id}`

Get Group Role

Get the group role

**Scopes:** `group:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `group_id` | path | `string` | Yes | The group ID. |
| `role_id` | path | `string` | Yes | The role ID. |

**Responses:**

- `200`: OK → `GroupRole`

**Response fields** (`GroupRole`)

See [GroupRole](#grouprole) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "id": "string",
  "displayName": "string",
  "description": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/roles/{ROLE_ID}"
```

### GET `/cloud/v2/universes/{universe_id}`

Get Universe

Gets the specified universe.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |

**Responses:**

- `200`: OK → `Universe`

**Response fields** (`Universe`)

See [Universe](#universe) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "description": "string",
  "user": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}"
```

### PATCH `/cloud/v2/universes/{universe_id}`

Update Universe

Updates the specified universe.

This method is guaranteed to return all updated fields.
This method may additionally return the full resource.

**Scopes:** `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `updateMask` | query | `string` | No | The list of fields to update. |

**Request Body:** `application/json` — Type: `Universe`

See [Universe](#universe) in Models.

**Request example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "description": "string",
  "user": "string"
}
```

**Responses:**

- `200`: OK → `Universe`

**Response fields** (`Universe`)

See [Universe](#universe) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "description": "string",
  "user": "string"
}
```

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "description": "string",
  "user": "string"
}'
```

### GET `/cloud/v2/universes/{universe_id}/data-stores`

List Data Stores

Returns a list of data stores.

Data stores scheduled for permanent deletion are omitted from the results
by default (or when `showDeleted` is set to `false`). When this is the
case, the operation will check up to 512 data stores. If all checked data
stores are deleted, it will return an empty list with a page token to
continue iteration.

**Scopes:** `universe-datastores.control:list`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of data stores to return. The service might return fewer than this value. If unspecified, at most 10 data stores are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  The `filter` field supports a very small subset of CEL:  * Only the `id` field is supported. * Only the `startsWith` function is available; no other operators nor   built-ins are supported.  Example filter: `id.startsWith("foo")` |
| `showDeleted` | query | `boolean` | No | If true, resources marked for pending deletion will be included in the results. |

**Responses:**

- `200`: OK → `ListDataStoresResponse`

**Response fields** (`ListDataStoresResponse`)

See [ListDataStoresResponse](#listdatastoresresponse) in Models.

**Response example:**
```json
{
  "dataStores": [
    {
      "path": "...",
      "createTime": "...",
      "expireTime": "...",
      "state": "...",
      "id": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores"
```

### DELETE `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}`

Delete Data Store

Schedules the specified data store for permanent deletion.

This operation assigns the data store an expiry time 30 days in the future,
at which point permanent deletion begins. To cancel, use the
`UndeleteDataStore` operation before the data store's expiry time.

Permanent deletion consists of deleting all of the entries in the data
store and then the data store resource itself. The data store is no longer
returned by the `ListDataStores` Open Cloud endpoint or
`ListDataStoresAsync` Luau API, and you can reuse the data store's name.

The duration of the permanent deletion process depends on the number of
entries in the data store. However, you can expect a data store with 1
million or fewer entries to be permanently deleted within 3 days.

Data stores scheduled for permanent deletion are returned by the
`ListDataStores` Open Cloud endpoint when the query parameter `showDeleted`
is set to `true`. In the return value, each data store will have a
`DELETED` state and an `expireTime` field.

Data stores scheduled for permanent deletion are immediately made
inaccessible, meaning attempts to read or write to their entries will fail.

Note: Due to caching in the backend service, attempts to read from or write
to entries in these data stores can continue to succeed for a limited time
after the deletion:
* `GetDataStoreEntry`: can succeed for up to 24 hours.
* All other endpoints: can succeed for several minutes.

If the data store is already in a `DELETED` state, this operation is a
no-op, and the data store is returned as-is.

**Scopes:** `universe-datastores.control:delete`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |

**Responses:**

- `200`: OK → `DataStore`

**Response fields** (`DataStore`)

See [DataStore](#datastore) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "expireTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "id": "string"
}
```

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}"
```

### GET `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/entries`

List Data Store Entries

Returns a list of entries from a data store.

Only the `path` and `id` fields are populated; use `GetDataStoreEntry`
to retrieve other fields.

Specify the wildcard scope (`-`) to list entries from all scopes.

**Scopes:** `universe-datastores.objects:list`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of data store entries to return. The service might return fewer than this value. If unspecified, at most 10 data store entries are returned. The maximum value is 256 and higher values are set to 256. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  The `filter` field supports a very small subset of CEL:  * Only the `id` field is supported. * Only the `startsWith` function is available; no other operators nor   built-ins are supported.  Example filter: `id.startsWith("foo")` |
| `showDeleted` | query | `boolean` | No | If true, resources marked for pending deletion will be included in the results. |

**Responses:**

- `200`: OK → `ListDataStoreEntriesResponse`

**Response fields** (`ListDataStoreEntriesResponse`)

See [ListDataStoreEntriesResponse](#listdatastoreentriesresponse) in Models.

**Response example:**
```json
{
  "dataStoreEntries": [
    {
      "path": "...",
      "createTime": "...",
      "revisionId": "...",
      "revisionCreateTime": "...",
      "state": "...",
      "etag": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/entries"
```

### POST `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/entries`

Create Data Store Entry

Creates an entry with the provided ID and value.

Returns a 400 Bad Request if the entry exists.

**Scopes:** `universe-datastores.objects:create`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `id` | query | `string` | No | The ID to use for the data store entry, which will become the final component of the data store entry's resource path.  This value should be a 1-50 character string. We strongly recommend using only lowercase letters, numeric digits, and hyphens. |

**Request Body:** `application/json` — Type: `DataStoreEntry`

See [DataStoreEntry](#datastoreentry) in Models.

**Request example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Responses:**

- `200`: OK → `DataStoreEntry`

**Response fields** (`DataStoreEntry`)

See [DataStoreEntry](#datastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/entries" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}'
```

### GET `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/entries/{entry_id}`

Get Data Store Entry

Gets the specified entry.

To get the entry at a specific revision, add `@<revisionId>` to the end of
the path.

For example, to get `my-entry` at the revision ID
`08DC3D3F43F9FCC1.0000000001.08DC3D3F43F9FCC1.01`, use the path
`/cloud/v2/universes/1234/data-stores/5678/entries/my-entry@08DC3D3F43F9FCC1.0000000001.08DC3D3F43F9FCC1.01`.

If your entry ID contains one or more `@` characters, and you want to get
the latest version rather than at any specific revision, append the special
revision ID `@latest` to the end of the path. Otherwise, the segment of the
entry ID after the last `@` will be interpreted as a revision ID.

For example, to get the latest revision of `my-entry`, use the path
`/cloud/v2/universes/1234/data-stores/5678/entries/my@entry@latest`.

To get the entry that was current at a specific time, add
`@latest:<timestamp>` to the end of the path, where `<timestamp>` is
RFC-3339 formatted. The given timestamp must be after
the Unix epoch (1/1/1970) and not more than ten minutes in the future.

For example, to get the revision of `my-entry` that was current on
12/2/2024 at 06:00 UTC, use the path
`/cloud/v2/universes/1234/data-stores/5678/entries/my-entry@latest:2024-12-02T06:00:00Z`.

**Scopes:** `universe-datastores.objects:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Responses:**

- `200`: OK → `DataStoreEntry`

**Response fields** (`DataStoreEntry`)

See [DataStoreEntry](#datastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/entries/{ENTRY_ID}"
```

### PATCH `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/entries/{entry_id}`

Update Data Store Entry

Updates the value, attributes, and users of an entry.

Updating specific revisions of the entry is **unsupported**. If you specify
a revision ID in the path and `allow_missing` is `true`, the update request
will instead create a new entry with the `@<revisionId>` suffix as part of
the key.

Partial update is **unsupported**. If attributes or users are not
provided when updating the value, they will be cleared. Value must always
be provided when updating an entry.

**Scopes:** `universe-datastores.objects:update`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |
| `allowMissing` | query | `boolean` | No | If set to true, and the data store entry is not found, a data store entry is created. |

**Request Body:** `application/json` — Type: `DataStoreEntry`

See [DataStoreEntry](#datastoreentry) in Models.

**Request example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Responses:**

- `200`: OK → `DataStoreEntry`

**Response fields** (`DataStoreEntry`)

See [DataStoreEntry](#datastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/entries/{ENTRY_ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}'
```

### DELETE `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/entries/{entry_id}`

Delete Data Store Entry

Marks the specified entry for deletion.

Entries are not be deleted immediately; instead, the `state` field will
be set to `DELETED`. Permanent deletion occurs after 30 days.

On success, returns 200 OK. If the entry doesn't exist, returns
404 Not Found.

**Scopes:** `universe-datastores.objects:delete`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Responses:**

- `200`: OK

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/entries/{ENTRY_ID}"
```

### POST `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/entries/{entry_id}:increment`

Increment Data Store Entry

Increments the value of the specified entry. Both the existing value and
the increment amount must be integers.

If the entry doesn't exist, creates an entry with the specified value.

Incrementing specific revisions of the entry is **unsupported**. If you
specify a revision ID in the path, the increment request will create a new
entry with the `@<revisionId>` suffix as part of the key.

Known issue: the value may be incremented past the valid range of  values.
When this happens, the returned value will be clamped to the valid range,
but the backend may persist the original value. This behavior is maintained
for backwards compatibility reasons, but may change in a future version of
this API.

**Scopes:** `universe-datastores.objects:create`, `universe-datastores.objects:update`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Request Body:** `application/json` — Type: `IncrementDataStoreEntryRequest`

See [IncrementDataStoreEntryRequest](#incrementdatastoreentryrequest) in Models.

**Request example:**
```json
{
  "amount": 0,
  "users": [
    "string"
  ],
  "attributes": "..."
}
```

**Responses:**

- `200`: OK → `DataStoreEntry`

**Response fields** (`DataStoreEntry`)

See [DataStoreEntry](#datastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/entries/{ENTRY_ID}:increment" \
  -H "Content-Type: application/json" \
  -d '{
  "amount": 0,
  "users": [
    "string"
  ],
  "attributes": "..."
}'
```

### GET `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/entries/{entry_id}:listRevisions`

List Data Store Entry Revisions

List revisions of the data store entry.

This method returns partial data store entries.

In particular, only the `path`, `id`, `createTime`, `revisionCreateTime`,
`revisionId`, `etag`, and `state` fields are populated. Both the `path` and
`id` fields will have an `@<version>` suffix.

In order to get the full entry at a revision, you can use the provided
`path` field with the `GetDataStoreEntry` method, i.e. `GET
/cloud/v2/universes/1234/data-stores/5678/entries/my-entry@<version>`.

**Scopes:** `universe-datastores.versions:list`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of revisions to return per page.  The service might return fewer than the maximum number of revisions. If unspecified, at most 10 revisions are returned. The maximum value is 100 values and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | Supports the following subset of CEL:  * Only the `&&`, `<=`, and `>=` operators are supported. * Only the `revision_create_time` field is supported.  For example:    `"revision_create_time >= 2000-01-01T00:00:00Z && revision_create_time <=   2001-01-01T00:00:00Z"` |

**Responses:**

- `200`: OK → `ListDataStoreEntryRevisionsResponse`

**Response fields** (`ListDataStoreEntryRevisionsResponse`)

See [ListDataStoreEntryRevisionsResponse](#listdatastoreentryrevisionsresponse) in Models.

**Response example:**
```json
{
  "dataStoreEntries": [
    {
      "path": "...",
      "createTime": "...",
      "revisionId": "...",
      "revisionCreateTime": "...",
      "state": "...",
      "etag": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/entries/{ENTRY_ID}:listRevisions"
```

### GET `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries`

List Data Store Entries

Returns a list of entries from a data store.

Only the `path` and `id` fields are populated; use `GetDataStoreEntry`
to retrieve other fields.

Specify the wildcard scope (`-`) to list entries from all scopes.

**Scopes:** `universe-datastores.objects:list`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of data store entries to return. The service might return fewer than this value. If unspecified, at most 10 data store entries are returned. The maximum value is 256 and higher values are set to 256. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  The `filter` field supports a very small subset of CEL:  * Only the `id` field is supported. * Only the `startsWith` function is available; no other operators nor   built-ins are supported.  Example filter: `id.startsWith("foo")` |
| `showDeleted` | query | `boolean` | No | If true, resources marked for pending deletion will be included in the results. |

**Responses:**

- `200`: OK → `ListDataStoreEntriesResponse`

**Response fields** (`ListDataStoreEntriesResponse`)

See [ListDataStoreEntriesResponse](#listdatastoreentriesresponse) in Models.

**Response example:**
```json
{
  "dataStoreEntries": [
    {
      "path": "...",
      "createTime": "...",
      "revisionId": "...",
      "revisionCreateTime": "...",
      "state": "...",
      "etag": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/scopes/{SCOPE_ID}/entries"
```

### POST `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries`

Create Data Store Entry

Creates an entry with the provided ID and value.

Returns a 400 Bad Request if the entry exists.

**Scopes:** `universe-datastores.objects:create`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `id` | query | `string` | No | The ID to use for the data store entry, which will become the final component of the data store entry's resource path.  This value should be a 1-50 character string. We strongly recommend using only lowercase letters, numeric digits, and hyphens. |

**Request Body:** `application/json` — Type: `DataStoreEntry`

See [DataStoreEntry](#datastoreentry) in Models.

**Request example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Responses:**

- `200`: OK → `DataStoreEntry`

**Response fields** (`DataStoreEntry`)

See [DataStoreEntry](#datastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/scopes/{SCOPE_ID}/entries" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}'
```

### GET `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries/{entry_id}`

Get Data Store Entry

Gets the specified entry.

To get the entry at a specific revision, add `@<revisionId>` to the end of
the path.

For example, to get `my-entry` at the revision ID
`08DC3D3F43F9FCC1.0000000001.08DC3D3F43F9FCC1.01`, use the path
`/cloud/v2/universes/1234/data-stores/5678/entries/my-entry@08DC3D3F43F9FCC1.0000000001.08DC3D3F43F9FCC1.01`.

If your entry ID contains one or more `@` characters, and you want to get
the latest version rather than at any specific revision, append the special
revision ID `@latest` to the end of the path. Otherwise, the segment of the
entry ID after the last `@` will be interpreted as a revision ID.

For example, to get the latest revision of `my-entry`, use the path
`/cloud/v2/universes/1234/data-stores/5678/entries/my@entry@latest`.

To get the entry that was current at a specific time, add
`@latest:<timestamp>` to the end of the path, where `<timestamp>` is
RFC-3339 formatted. The given timestamp must be after
the Unix epoch (1/1/1970) and not more than ten minutes in the future.

For example, to get the revision of `my-entry` that was current on
12/2/2024 at 06:00 UTC, use the path
`/cloud/v2/universes/1234/data-stores/5678/entries/my-entry@latest:2024-12-02T06:00:00Z`.

**Scopes:** `universe-datastores.objects:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Responses:**

- `200`: OK → `DataStoreEntry`

**Response fields** (`DataStoreEntry`)

See [DataStoreEntry](#datastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}"
```

### PATCH `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries/{entry_id}`

Update Data Store Entry

Updates the value, attributes, and users of an entry.

Updating specific revisions of the entry is **unsupported**. If you specify
a revision ID in the path and `allow_missing` is `true`, the update request
will instead create a new entry with the `@<revisionId>` suffix as part of
the key.

Partial update is **unsupported**. If attributes or users are not
provided when updating the value, they will be cleared. Value must always
be provided when updating an entry.

**Scopes:** `universe-datastores.objects:update`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |
| `allowMissing` | query | `boolean` | No | If set to true, and the data store entry is not found, a data store entry is created. |

**Request Body:** `application/json` — Type: `DataStoreEntry`

See [DataStoreEntry](#datastoreentry) in Models.

**Request example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Responses:**

- `200`: OK → `DataStoreEntry`

**Response fields** (`DataStoreEntry`)

See [DataStoreEntry](#datastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}'
```

### DELETE `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries/{entry_id}`

Delete Data Store Entry

Marks the specified entry for deletion.

Entries are not be deleted immediately; instead, the `state` field will
be set to `DELETED`. Permanent deletion occurs after 30 days.

On success, returns 200 OK. If the entry doesn't exist, returns
404 Not Found.

**Scopes:** `universe-datastores.objects:delete`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Responses:**

- `200`: OK

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}"
```

### POST `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries/{entry_id}:increment`

Increment Data Store Entry

Increments the value of the specified entry. Both the existing value and
the increment amount must be integers.

If the entry doesn't exist, creates an entry with the specified value.

Incrementing specific revisions of the entry is **unsupported**. If you
specify a revision ID in the path, the increment request will create a new
entry with the `@<revisionId>` suffix as part of the key.

Known issue: the value may be incremented past the valid range of  values.
When this happens, the returned value will be clamped to the valid range,
but the backend may persist the original value. This behavior is maintained
for backwards compatibility reasons, but may change in a future version of
this API.

**Scopes:** `universe-datastores.objects:create`, `universe-datastores.objects:update`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Request Body:** `application/json` — Type: `IncrementDataStoreEntryRequest`

See [IncrementDataStoreEntryRequest](#incrementdatastoreentryrequest) in Models.

**Request example:**
```json
{
  "amount": 0,
  "users": [
    "string"
  ],
  "attributes": "..."
}
```

**Responses:**

- `200`: OK → `DataStoreEntry`

**Response fields** (`DataStoreEntry`)

See [DataStoreEntry](#datastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}:increment" \
  -H "Content-Type: application/json" \
  -d '{
  "amount": 0,
  "users": [
    "string"
  ],
  "attributes": "..."
}'
```

### GET `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries/{entry_id}:listRevisions`

List Data Store Entry Revisions

List revisions of the data store entry.

This method returns partial data store entries.

In particular, only the `path`, `id`, `createTime`, `revisionCreateTime`,
`revisionId`, `etag`, and `state` fields are populated. Both the `path` and
`id` fields will have an `@<version>` suffix.

In order to get the full entry at a revision, you can use the provided
`path` field with the `GetDataStoreEntry` method, i.e. `GET
/cloud/v2/universes/1234/data-stores/5678/entries/my-entry@<version>`.

**Scopes:** `universe-datastores.versions:list`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of revisions to return per page.  The service might return fewer than the maximum number of revisions. If unspecified, at most 10 revisions are returned. The maximum value is 100 values and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | Supports the following subset of CEL:  * Only the `&&`, `<=`, and `>=` operators are supported. * Only the `revision_create_time` field is supported.  For example:    `"revision_create_time >= 2000-01-01T00:00:00Z && revision_create_time <=   2001-01-01T00:00:00Z"` |

**Responses:**

- `200`: OK → `ListDataStoreEntryRevisionsResponse`

**Response fields** (`ListDataStoreEntryRevisionsResponse`)

See [ListDataStoreEntryRevisionsResponse](#listdatastoreentryrevisionsresponse) in Models.

**Response example:**
```json
{
  "dataStoreEntries": [
    {
      "path": "...",
      "createTime": "...",
      "revisionId": "...",
      "revisionCreateTime": "...",
      "state": "...",
      "etag": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}:listRevisions"
```

### POST `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}:undelete`

Undelete Data Store

Restore the data store

**Scopes:** `universe-datastores.control:delete`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |

**Request Body:** `application/json` — Type: `UndeleteDataStoreRequest`

See [UndeleteDataStoreRequest](#undeletedatastorerequest) in Models.

**Request example:**
```json
{}
```

**Responses:**

- `200`: OK → `DataStore`

**Response fields** (`DataStore`)

See [DataStore](#datastore) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "expireTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "id": "string"
}
```

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}:undelete" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST `/cloud/v2/universes/{universe_id}/data-stores:snapshot`

Snapshot Data Stores

Takes a new snapshot of the data stores in an experience.

After a snapshot, the next write to every key in the experience will
create a versioned backup of the previous data, regardless of the time of
the last write.

In effect, all data current at the time of the snapshot is guaranteed to be
available as a versioned backup for at least 30 days.

Snapshots can be taken once per UTC day, per experience. If the latest
snapshot was taken within the same UTC day, this operation is a no-op and
the time of the latest snapshot will be returned.

For more information on using snapshots, see the [Data
stores](https://create.roblox.com/docs/cloud-services/data-stores#snapshots)
Engine guide.

**Scopes:** `universe-datastores.control:snapshot`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |

**Request Body:** `application/json` — Type: `SnapshotDataStoresRequest`

See [SnapshotDataStoresRequest](#snapshotdatastoresrequest) in Models.

**Request example:**
```json
{}
```

**Responses:**

- `200`: OK → `SnapshotDataStoresResponse`

**Response fields** (`SnapshotDataStoresResponse`)

See [SnapshotDataStoresResponse](#snapshotdatastoresresponse) in Models.

**Response example:**
```json
{
  "newSnapshotTaken": false,
  "latestSnapshotTime": "2024-01-01T00:00:00Z"
}
```

**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores:snapshot" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST `/cloud/v2/universes/{universe_id}/luau-execution-session-task-binary-inputs`

Create Luau Execution Session Task Binary Input

Create a new `LuauExecutionSessionTaskBinaryInput`.

**Scopes:** `universe.place.luau-execution-session:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |

**Request Body:** `application/json` — Type: `LuauExecutionSessionTaskBinaryInput`

See [LuauExecutionSessionTaskBinaryInput](#luauexecutionsessiontaskbinaryinput) in Models.

**Request example:**
```json
{
  "path": "string",
  "size": 0,
  "uploadUri": "string"
}
```

**Responses:**

- `200`: OK → `LuauExecutionSessionTaskBinaryInput`

**Response fields** (`LuauExecutionSessionTaskBinaryInput`)

See [LuauExecutionSessionTaskBinaryInput](#luauexecutionsessiontaskbinaryinput) in Models.

**Response example:**
```json
{
  "path": "string",
  "size": 0,
  "uploadUri": "string"
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/luau-execution-session-task-binary-inputs" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "size": 0,
  "uploadUri": "string"
}'
```

### POST `/cloud/v2/universes/{universe_id}/memory-store/queues/{queue_id}/items`

Create Memory Store Queue Item

Creates a new queue item.

If `ttl` is set, the item will automatically be removed from the queue
after the time interval specified.

If a numerical `priority` is set, the item will be inserted into the queue
based on the priority value. The higher the value, the closer to the front
of the queue the item will be. If priority values are the same then the
item will be inserted after existing values with the same priority.

**Scopes:** `memory-store.queue:add`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `queue_id` | path | `string` | Yes | The queue ID. |

**Request Body:** `application/json` — Type: `MemoryStoreQueueItem`

See [MemoryStoreQueueItem](#memorystorequeueitem) in Models.

**Request example:**
```json
{
  "path": "string",
  "data": "...",
  "priority": 0,
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}
```

**Responses:**

- `200`: OK → `MemoryStoreQueueItem`

**Response fields** (`MemoryStoreQueueItem`)

See [MemoryStoreQueueItem](#memorystorequeueitem) in Models.

**Response example:**
```json
{
  "path": "string",
  "data": "...",
  "priority": 0,
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store/queues/{QUEUE_ID}/items" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "data": "...",
  "priority": 0,
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}'
```

### POST `/cloud/v2/universes/{universe_id}/memory-store/queues/{queue_id}/items:discard`

Discard Memory Store Queue Items

Discards read items from the front of the queue.

Takes a `readId` from a previous `Read` operation.

**Scopes:** `memory-store.queue:discard`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `queue_id` | path | `string` | Yes | The queue ID. |

**Request Body:** `application/json` — Type: `DiscardMemoryStoreQueueItemsRequest`

See [DiscardMemoryStoreQueueItemsRequest](#discardmemorystorequeueitemsrequest) in Models.

**Request example:**
```json
{
  "readId": "string"
}
```

**Responses:**

- `200`: OK

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store/queues/{QUEUE_ID}/items:discard" \
  -H "Content-Type: application/json" \
  -d '{
  "readId": "string"
}'
```

### GET `/cloud/v2/universes/{universe_id}/memory-store/queues/{queue_id}/items:read`

Read Memory Store Queue Items

Returns the specified number of items at the front of the queue.

**Scopes:** `memory-store.queue:dequeue`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `queue_id` | path | `string` | Yes | The queue ID. |
| `count` | query | `integer` | No | The number of items to read from the queue If unspecified, 1 item will be returned. The maximum value is 200; values above 200 will be coerced to 200. |
| `allOrNothing` | query | `boolean` | No | If `all_or_nothing` is true and the requested number of objects is not available, will return a 404 Error.  Otherwise, will return the path and read_id of the read operation and a list of the MemoryStoreQueue items. |
| `invisibilityWindow` | query | `string` | No | Invisibility window for items read, in seconds.  Items read are invisible in subsequent reads during the invisibility window duration.  It must be written in seconds greater than 0 and end with `s`.  Defaults to `30s`. |

**Responses:**

- `200`: OK → `ReadMemoryStoreQueueItemsResponse`

**Response fields** (`ReadMemoryStoreQueueItemsResponse`)

See [ReadMemoryStoreQueueItemsResponse](#readmemorystorequeueitemsresponse) in Models.

**Response example:**
```json
{
  "readId": "string",
  "items": [
    {
      "path": "...",
      "data": "...",
      "priority": "...",
      "ttl": "...",
      "expireTime": "...",
      "id": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store/queues/{QUEUE_ID}/items:read"
```

### GET `/cloud/v2/universes/{universe_id}/memory-store/sorted-maps/{sorted_map_id}/items`

List Memory Store Sorted Map Items

Gets and returns items in the map with a given order and filter.

**Scopes:** `memory-store.sorted-map:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `sorted_map_id` | path | `string` | Yes | The sorted-map ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of memory store sorted map items to return. The service might return fewer than this value. If unspecified, at most 1 memory store sorted map items are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `orderBy` | query | `string` | No | If specified, results are ordered according to the specified fields.  Values must be a comma-separated list of fields, with an optional, per-field " desc" suffix to sort by descending rather than ascending values. You can access subfields with a `.` operator.  Results may be ordered by the following fields: id.  Example: "id desc" |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  Filtering conforms to Common Expression Language (CEL). Only the `id` and `sortKey` fields are supported. In terms of operators, only `<`, `>` and `&&` are allowed'  Example: `id > "key-001" && id < "key-100"` |

**Responses:**

- `200`: OK → `ListMemoryStoreSortedMapItemsResponse`

**Response fields** (`ListMemoryStoreSortedMapItemsResponse`)

See [ListMemoryStoreSortedMapItemsResponse](#listmemorystoresortedmapitemsresponse) in Models.

**Response example:**
```json
{
  "items": [
    {
      "path": "...",
      "value": "...",
      "etag": "...",
      "ttl": "...",
      "expireTime": "...",
      "id": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store/sorted-maps/{SORTED_MAP_ID}/items"
```

### POST `/cloud/v2/universes/{universe_id}/memory-store/sorted-maps/{sorted_map_id}/items`

Create Memory Store Sorted Map Item

Creates the specified map item if it doesn't exist.

**Scopes:** `memory-store.sorted-map:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `sorted_map_id` | path | `string` | Yes | The sorted-map ID. |
| `id` | query | `string` | No | The ID to use for the memory store sorted map item, which will become the final component of the memory store sorted map item's resource path.  This value should be a 1-127 character string that supports alphanumeric and special characters. This id is case sensitive. The id must be url encoded if it contains any url breaking special characters. |

**Request Body:** `application/json` — Type: `MemoryStoreSortedMapItem`

See [MemoryStoreSortedMapItem](#memorystoresortedmapitem) in Models.

**Request example:**
```json
{
  "path": "string",
  "value": "...",
  "etag": "string",
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}
```

**Responses:**

- `200`: OK → `MemoryStoreSortedMapItem`

**Response fields** (`MemoryStoreSortedMapItem`)

See [MemoryStoreSortedMapItem](#memorystoresortedmapitem) in Models.

**Response example:**
```json
{
  "path": "string",
  "value": "...",
  "etag": "string",
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store/sorted-maps/{SORTED_MAP_ID}/items" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "value": "...",
  "etag": "string",
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}'
```

### GET `/cloud/v2/universes/{universe_id}/memory-store/sorted-maps/{sorted_map_id}/items/{item_id}`

Get Memory Store Sorted Map Item

Gets and returns the value of the given key in the map.

**Scopes:** `memory-store.sorted-map:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `sorted_map_id` | path | `string` | Yes | The sorted-map ID. |
| `item_id` | path | `string` | Yes | The item ID. |

**Responses:**

- `200`: OK → `MemoryStoreSortedMapItem`

**Response fields** (`MemoryStoreSortedMapItem`)

See [MemoryStoreSortedMapItem](#memorystoresortedmapitem) in Models.

**Response example:**
```json
{
  "path": "string",
  "value": "...",
  "etag": "string",
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store/sorted-maps/{SORTED_MAP_ID}/items/{ITEM_ID}"
```

### PATCH `/cloud/v2/universes/{universe_id}/memory-store/sorted-maps/{sorted_map_id}/items/{item_id}`

Update Memory Store Sorted Map Item

Updates the specified map item.

**Scopes:** `memory-store.sorted-map:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `sorted_map_id` | path | `string` | Yes | The sorted-map ID. |
| `item_id` | path | `string` | Yes | The item ID. |
| `allowMissing` | query | `boolean` | No | If set to true, and the memory store sorted map item is not found, a memory store sorted map item is created. |

**Request Body:** `application/json` — Type: `MemoryStoreSortedMapItem`

See [MemoryStoreSortedMapItem](#memorystoresortedmapitem) in Models.

**Request example:**
```json
{
  "path": "string",
  "value": "...",
  "etag": "string",
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}
```

**Responses:**

- `200`: OK → `MemoryStoreSortedMapItem`

**Response fields** (`MemoryStoreSortedMapItem`)

See [MemoryStoreSortedMapItem](#memorystoresortedmapitem) in Models.

**Response example:**
```json
{
  "path": "string",
  "value": "...",
  "etag": "string",
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}
```

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store/sorted-maps/{SORTED_MAP_ID}/items/{ITEM_ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "value": "...",
  "etag": "string",
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}'
```

### DELETE `/cloud/v2/universes/{universe_id}/memory-store/sorted-maps/{sorted_map_id}/items/{item_id}`

Delete Memory Store Sorted Map Item

Deletes the specified item from the map.

**Scopes:** `memory-store.sorted-map:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `sorted_map_id` | path | `string` | Yes | The sorted-map ID. |
| `item_id` | path | `string` | Yes | The item ID. |

**Responses:**

- `200`: OK

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store/sorted-maps/{SORTED_MAP_ID}/items/{ITEM_ID}"
```

### POST `/cloud/v2/universes/{universe_id}/memory-store:flush`

Flush Memory Store

Asynchronously flush all data structures in the universe.

Unlike some other endpoints, the flush response `path` already
includes the `cloud/v2` prefix. Poll the operation at
`https://apis.roblox.com/{path}` without adding another prefix.

**Scopes:** `memory-store:flush`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `scope` | query | `LIVE \| TEST` | No | The scope of the memory store to flush.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| LIVE \|  Flush the live memory store scope. This is the default. \|   \| TEST \| Flush the test memory store scope. \| Valid values: `LIVE`, `TEST` |

**Responses:**

- `200`: OK → `Operation`

**Response fields** (`Operation`)

See [Operation](#operation) in Models.

**Response example:**
```json
{
  "path": "string",
  "metadata": {
    "@type": "string"
  },
  "done": false,
  "error": {
    "code": 0,
    "message": "string",
    "details": [
      "..."
    ]
  },
  "response": {
    "@type": "string"
  }
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store:flush"
```

### GET `/cloud/v2/universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{scope_id}/entries`

List Ordered Data Store Entries

Returns a list of entries from an ordered data store.

**Scopes:** `universe.ordered-data-store.scope.entry:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `ordered_data_store_id` | path | `string` | Yes | The ordered-data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of ordered data store entries to return. The service might return fewer than this value. If unspecified, at most 10 ordered data store entries are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `orderBy` | query | `string` | No | If specified, results are ordered according to the specified fields.  Values must be a comma-separated list of fields, with an optional, per-field " desc" suffix to sort by descending rather than ascending values. You can access subfields with a `.` operator.  Results may be ordered by the following fields: value.  Example: "value desc" |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  We support two comparison operators for this operation: `<=` and `>=`.These comparison operators act as a minValue and maxValue for the values returned. If filtering is needed for a value between a minValue and maxValue the user can use the logical operator `&&`. All tokens in the filter expression must be separated by a single space.  Example filters: `entry <= 10`; `entry >= 10 && entry <= 30` |

**Responses:**

- `200`: OK → `ListOrderedDataStoreEntriesResponse`

**Response fields** (`ListOrderedDataStoreEntriesResponse`)

See [ListOrderedDataStoreEntriesResponse](#listordereddatastoreentriesresponse) in Models.

**Response example:**
```json
{
  "orderedDataStoreEntries": [
    {
      "path": "...",
      "value": "...",
      "id": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limit Note:** Ordered data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/ordered-data-stores/{ORDERED_DATA_STORE_ID}/scopes/{SCOPE_ID}/entries"
```

### POST `/cloud/v2/universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{scope_id}/entries`

Create Ordered Data Store Entry

Creates an entry with the provided ID and value.

Returns a 400 Bad Request if the entry exists.

**Scopes:** `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `ordered_data_store_id` | path | `string` | Yes | The ordered-data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `id` | query | `string` | No | The ID to use for the ordered data store entry, which will become the final component of the ordered data store entry's resource path.  This value should be A 1-63 character string. We strongly recommend using only lowercase letters, numeric digits, and hyphens. |

**Request Body:** `application/json` — Type: `OrderedDataStoreEntry`

See [OrderedDataStoreEntry](#ordereddatastoreentry) in Models.

**Request example:**
```json
{
  "path": "string",
  "value": 0,
  "id": "string"
}
```

**Responses:**

- `200`: OK → `OrderedDataStoreEntry`

**Response fields** (`OrderedDataStoreEntry`)

See [OrderedDataStoreEntry](#ordereddatastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "value": 0,
  "id": "string"
}
```

**Rate Limit Note:** Ordered data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/ordered-data-stores/{ORDERED_DATA_STORE_ID}/scopes/{SCOPE_ID}/entries" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "value": 0,
  "id": "string"
}'
```

### GET `/cloud/v2/universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{scope_id}/entries/{entry_id}`

Get Ordered Data Store Entry

Gets the specified entry.

**Scopes:** `universe.ordered-data-store.scope.entry:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `ordered_data_store_id` | path | `string` | Yes | The ordered-data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Responses:**

- `200`: OK → `OrderedDataStoreEntry`

**Response fields** (`OrderedDataStoreEntry`)

See [OrderedDataStoreEntry](#ordereddatastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "value": 0,
  "id": "string"
}
```

**Rate Limit Note:** Ordered data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/ordered-data-stores/{ORDERED_DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}"
```

### PATCH `/cloud/v2/universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{scope_id}/entries/{entry_id}`

Update Ordered Data Store Entry

Updates the value of an entry.

**Scopes:** `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `ordered_data_store_id` | path | `string` | Yes | The ordered-data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |
| `allowMissing` | query | `boolean` | No | If set to true, and the ordered data store entry is not found, a ordered data store entry is created. |

**Request Body:** `application/json` — Type: `OrderedDataStoreEntry`

See [OrderedDataStoreEntry](#ordereddatastoreentry) in Models.

**Request example:**
```json
{
  "path": "string",
  "value": 0,
  "id": "string"
}
```

**Responses:**

- `200`: OK → `OrderedDataStoreEntry`

**Response fields** (`OrderedDataStoreEntry`)

See [OrderedDataStoreEntry](#ordereddatastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "value": 0,
  "id": "string"
}
```

**Rate Limit Note:** Ordered data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/ordered-data-stores/{ORDERED_DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "value": 0,
  "id": "string"
}'
```

### DELETE `/cloud/v2/universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{scope_id}/entries/{entry_id}`

Delete Ordered Data Store Entry

Deletes the specified entry.

On success, returns 200 OK. If the entry doesn't exist, returns
404 Not Found.

**Scopes:** `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `ordered_data_store_id` | path | `string` | Yes | The ordered-data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Responses:**

- `200`: OK

**Rate Limit Note:** Ordered data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/ordered-data-stores/{ORDERED_DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}"
```

### POST `/cloud/v2/universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{scope_id}/entries/{entry_id}:increment`

Increment Ordered Data Store Entry

Increments the value of the specified entry. Both the existing value and
the increment amount must be integers.

If the entry doesn't exist, creates an entry with the specified value.

Known issue: the value may be incremented past the valid range of  values.
When this happens, the returned value will be clamped to the valid range,
but the backend may persist the original value. This behavior is maintained
for backwards compatibility reasons, but may change in a future version of
this API.

**Scopes:** `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `ordered_data_store_id` | path | `string` | Yes | The ordered-data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Request Body:** `application/json` — Type: `IncrementOrderedDataStoreEntryRequest`

See [IncrementOrderedDataStoreEntryRequest](#incrementordereddatastoreentryrequest) in Models.

**Request example:**
```json
{
  "amount": 0
}
```

**Responses:**

- `200`: OK → `OrderedDataStoreEntry`

**Response fields** (`OrderedDataStoreEntry`)

See [OrderedDataStoreEntry](#ordereddatastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "value": 0,
  "id": "string"
}
```

**Rate Limit Note:** Ordered data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/ordered-data-stores/{ORDERED_DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}:increment" \
  -H "Content-Type: application/json" \
  -d '{
  "amount": 0
}'
```

### GET `/cloud/v2/universes/{universe_id}/places/{place_id}`

Get Place

Gets the specified place.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |

**Responses:**

- `200`: OK → `Place`

**Response fields** (`Place`)

See [Place](#place) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "description": "string",
  "serverSize": 0
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}"
```

### PATCH `/cloud/v2/universes/{universe_id}/places/{place_id}`

Update Place

Updates the specified place. To avoid overwriting changes, this endpoint
responds with an HTTP 409 Conflict error if the place is open in an
active Team Create session.

**Scopes:** `universe.place:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |
| `updateMask` | query | `string` | No | The list of fields to update. |

**Request Body:** `application/json` — Type: `Place`

See [Place](#place) in Models.

**Request example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "description": "string",
  "serverSize": 0
}
```

**Responses:**

- `200`: OK → `Place`

**Response fields** (`Place`)

See [Place](#place) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "description": "string",
  "serverSize": 0
}
```

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "description": "string",
  "serverSize": 0
}'
```

### GET `/cloud/v2/universes/{universe_id}/places/{place_id}/instances/{instance_id}`

Get Instance

Gets an instance and its property data.

The maximum supported response data size is 500,000 bytes. If this limit is
exceeded, the returned `Operation` will be completed with an error result
that has an error code of `422`.

**Scopes:** `universe.place.instance:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |
| `instance_id` | path | `string` | Yes | The instance ID. |

**Responses:**

- `200`: OK → `Operation`

**Response fields** (`Operation`)

See [Operation](#operation) in Models.

**Response example:**
```json
{
  "path": "string",
  "metadata": {
    "@type": "string"
  },
  "done": false,
  "error": {
    "code": 0,
    "message": "string",
    "details": [
      "..."
    ]
  },
  "response": {
    "@type": "string"
  }
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}/instances/{INSTANCE_ID}"
```

### PATCH `/cloud/v2/universes/{universe_id}/places/{place_id}/instances/{instance_id}`

Update Instance

Updates an instance's property data.

When updating a `Script` instance's source property, the maximum supported
property size is 200,000 bytes after UTF-8 encoding.

**Scopes:** `universe.place.instance:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |
| `instance_id` | path | `string` | Yes | The instance ID. |
| `updateMask` | query | `string` | No | The list of fields to update. |

**Request Body:** `application/json` — Type: `Instance`

See [Instance](#instance) in Models.

**Request example:**
```json
{
  "path": "string",
  "hasChildren": false,
  "engineInstance": {
    "Id": "string",
    "Parent": "string",
    "Name": "string",
    "Details": {
      "Folder": "...",
      "LocalScript": "...",
      "ModuleScript": "...",
      "Script": "..."
    }
  }
}
```

**Responses:**

- `200`: OK → `Operation`

**Response fields** (`Operation`)

See [Operation](#operation) in Models.

**Response example:**
```json
{
  "path": "string",
  "metadata": {
    "@type": "string"
  },
  "done": false,
  "error": {
    "code": 0,
    "message": "string",
    "details": [
      "..."
    ]
  },
  "response": {
    "@type": "string"
  }
}
```

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}/instances/{INSTANCE_ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "hasChildren": false,
  "engineInstance": {
    "Id": "string",
    "Parent": "string",
    "Name": "string",
    "Details": {
      "Folder": "...",
      "LocalScript": "...",
      "ModuleScript": "...",
      "Script": "..."
    }
  }
}'
```

### GET `/cloud/v2/universes/{universe_id}/places/{place_id}/instances/{instance_id}:listChildren`

List Instance Children

Lists an instance's children.

The maximum supported response data size is 500,000 bytes. If this limit is
exceeded, the returned `Operation` will be completed with an error result
that has an error code of `422`.

**Scopes:** `universe.place.instance:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |
| `instance_id` | path | `string` | Yes | The instance ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of child instance to return. The service may return fewer than this value. If unspecified, at most 200 children will be returned. The maximum value is 200; values above 200 will be coerced to 200. |
| `pageToken` | query | `string` | No | A page token, received from a previous `ListInstanceChildrenRequest` call. Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to `ListInstanceChildrenRequest` must match the call that provided the page token. |

**Responses:**

- `200`: OK → `Operation`

**Response fields** (`Operation`)

See [Operation](#operation) in Models.

**Response example:**
```json
{
  "path": "string",
  "metadata": {
    "@type": "string"
  },
  "done": false,
  "error": {
    "code": 0,
    "message": "string",
    "details": [
      "..."
    ]
  },
  "response": {
    "@type": "string"
  }
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}/instances/{INSTANCE_ID}:listChildren"
```

### POST `/cloud/v2/universes/{universe_id}/places/{place_id}/luau-execution-session-tasks`

Create Luau Execution Session Task

Creates a task but does not wait for the task to complete.

To check whether a task has
completed, call the `GetLuauExecutionSessionTask` method and inspect the
`state` field of the returned resource.

**Scopes:** `universe.place.luau-execution-session:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |

**Request Body:** `application/json` — Type: `LuauExecutionSessionTask`

See [LuauExecutionSessionTask](#luauexecutionsessiontask) in Models.

**Request example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "state": "STATE_UNSPECIFIED",
  "script": "string"
}
```

**Responses:**

- `200`: OK → `LuauExecutionSessionTask`

**Response fields** (`LuauExecutionSessionTask`)

See [LuauExecutionSessionTask](#luauexecutionsessiontask) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "state": "STATE_UNSPECIFIED",
  "script": "string"
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}/luau-execution-session-tasks" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "state": "STATE_UNSPECIFIED",
  "script": "string"
}'
```

### GET `/cloud/v2/universes/{universe_id}/places/{place_id}/user-restrictions`

List User Restrictions

List user restrictions for users that have ever been banned in either a
universe or a specific place.

**Scopes:** `universe.user-restriction:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of user restrictions to return. The service might return fewer than this value. If unspecified, at most 10 user restrictions are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |

**Responses:**

- `200`: OK → `ListUserRestrictionsResponse`

**Response fields** (`ListUserRestrictionsResponse`)

See [ListUserRestrictionsResponse](#listuserrestrictionsresponse) in Models.

**Response example:**
```json
{
  "userRestrictions": [
    {
      "path": "...",
      "updateTime": "...",
      "user": "...",
      "gameJoinRestriction": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limit Note:** User Restrictions are subject to the additional rate limits, applied per universe

* Get User Restriction: 50 req/s
* List User Restrictions: 50 req/s
* Update User Restrictions: 10 req/s
* List User Restriction Logs: 50 req/s

Additionally, we impose the following rate limit for the same user within a universe:

* Update User Restriction: 2 req/min

For example, Update User Restriction may not be called for user 123 more than twice every minute.

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}/user-restrictions"
```

### GET `/cloud/v2/universes/{universe_id}/places/{place_id}/user-restrictions/{user_restriction_id}`

Get User Restriction

Get the user restriction.

**Scopes:** `universe.user-restriction:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |
| `user_restriction_id` | path | `string` | Yes | The user-restriction ID. |

**Responses:**

- `200`: OK → `UserRestriction`

**Response fields** (`UserRestriction`)

See [UserRestriction](#userrestriction) in Models.

**Response example:**
```json
{
  "path": "string",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "gameJoinRestriction": {
    "active": false,
    "startTime": "2024-01-01T00:00:00Z",
    "duration": "string",
    "privateReason": "string",
    "displayReason": "string",
    "excludeAltAccounts": false
  }
}
```

**Rate Limit Note:** User Restrictions are subject to the additional rate limits, applied per universe

* Get User Restriction: 50 req/s
* List User Restrictions: 50 req/s
* Update User Restrictions: 10 req/s
* List User Restriction Logs: 50 req/s

Additionally, we impose the following rate limit for the same user within a universe:

* Update User Restriction: 2 req/min

For example, Update User Restriction may not be called for user 123 more than twice every minute.

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}/user-restrictions/{USER_RESTRICTION_ID}"
```

### PATCH `/cloud/v2/universes/{universe_id}/places/{place_id}/user-restrictions/{user_restriction_id}`

Update User Restriction

Update the user restriction.

**Scopes:** `universe.user-restriction:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |
| `user_restriction_id` | path | `string` | Yes | The user-restriction ID. |
| `updateMask` | query | `string` | No | The list of fields to update.  The `game_join_restriction` field must be updated atomically; field masks that index into `game_join_restriction` (such as `"game_join_restriction.active"`) are not supported. |
| `idempotencyKey.key` | query | `string` | No | The unique key to use for idempotency. |
| `idempotencyKey.firstSent` | query | `string` | No | The timestamp at which the first request was sent.  If this is further in the past than the lifetime of the idempotency key (which *may* exceed the annotated minimum lifetime), the server *must* return an error. |

**Request Body:** `application/json` — Type: `UserRestriction`

See [UserRestriction](#userrestriction) in Models.

**Request example:**
```json
{
  "path": "string",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "gameJoinRestriction": {
    "active": false,
    "startTime": "2024-01-01T00:00:00Z",
    "duration": "string",
    "privateReason": "string",
    "displayReason": "string",
    "excludeAltAccounts": false
  }
}
```

**Responses:**

- `200`: OK → `UserRestriction`

**Response fields** (`UserRestriction`)

See [UserRestriction](#userrestriction) in Models.

**Response example:**
```json
{
  "path": "string",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "gameJoinRestriction": {
    "active": false,
    "startTime": "2024-01-01T00:00:00Z",
    "duration": "string",
    "privateReason": "string",
    "displayReason": "string",
    "excludeAltAccounts": false
  }
}
```

**Rate Limit Note:** User Restrictions are subject to the additional rate limits, applied per universe

* Get User Restriction: 50 req/s
* List User Restrictions: 50 req/s
* Update User Restrictions: 10 req/s
* List User Restriction Logs: 50 req/s

Additionally, we impose the following rate limit for the same user within a universe:

* Update User Restriction: 2 req/min

For example, Update User Restriction may not be called for user 123 more than twice every minute.

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}/user-restrictions/{USER_RESTRICTION_ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "gameJoinRestriction": {
    "active": false,
    "startTime": "2024-01-01T00:00:00Z",
    "duration": "string",
    "privateReason": "string",
    "displayReason": "string",
    "excludeAltAccounts": false
  }
}'
```

### POST `/cloud/v2/universes/{universe_id}/places/{place_id}/versions/{version_id}/luau-execution-session-tasks`

Create Luau Execution Session Task

Creates a task but does not wait for the task to complete.

To check whether a task has
completed, call the `GetLuauExecutionSessionTask` method and inspect the
`state` field of the returned resource.

**Scopes:** `universe.place.luau-execution-session:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |
| `version_id` | path | `string` | Yes | The version ID. |

**Request Body:** `application/json` — Type: `LuauExecutionSessionTask`

See [LuauExecutionSessionTask](#luauexecutionsessiontask) in Models.

**Request example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "state": "STATE_UNSPECIFIED",
  "script": "string"
}
```

**Responses:**

- `200`: OK → `LuauExecutionSessionTask`

**Response fields** (`LuauExecutionSessionTask`)

See [LuauExecutionSessionTask](#luauexecutionsessiontask) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "state": "STATE_UNSPECIFIED",
  "script": "string"
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}/versions/{VERSION_ID}/luau-execution-session-tasks" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "state": "STATE_UNSPECIFIED",
  "script": "string"
}'
```

### GET `/cloud/v2/universes/{universe_id}/places/{place_id}/versions/{version_id}/luau-execution-sessions/{luau_execution_session_id}/tasks/{task_id}`

Get Luau Execution Session Task

Gets information about a task.

**Scopes:** `universe.place.luau-execution-session:read`, `universe.place.luau-execution-session:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |
| `version_id` | path | `string` | Yes | The version ID. |
| `luau_execution_session_id` | path | `string` | Yes | The luau-execution-session ID. |
| `task_id` | path | `string` | Yes | The task ID. |
| `view` | query | `VIEW_UNSPECIFIED \| BASIC \| FULL` | No | The view in which to retrieve the luau execution session task.  Supports BASIC and FULL.  Defaults to BASIC.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| VIEW_UNSPECIFIED \| The luau execution session task view is not specified; the default will be used. \|   \| BASIC \| Excludes the `script` field. \|   \| FULL \| Includes all fields. \| Valid values: `VIEW_UNSPECIFIED`, `BASIC`, `FULL` |

**Responses:**

- `200`: OK → `LuauExecutionSessionTask`

**Response fields** (`LuauExecutionSessionTask`)

See [LuauExecutionSessionTask](#luauexecutionsessiontask) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "state": "STATE_UNSPECIFIED",
  "script": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}/versions/{VERSION_ID}/luau-execution-sessions/{LUAU_EXECUTION_SESSION_ID}/tasks/{TASK_ID}"
```

### GET `/cloud/v2/universes/{universe_id}/places/{place_id}/versions/{version_id}/luau-execution-sessions/{luau_execution_session_id}/tasks/{task_id}/logs`

List Luau Execution Session Task Logs

Lists log chunks generated by a `LuauExecutionSessionTask`.

**Scopes:** `universe.place.luau-execution-session:read`, `universe.place.luau-execution-session:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |
| `version_id` | path | `string` | Yes | The version ID. |
| `luau_execution_session_id` | path | `string` | Yes | The luau-execution-session ID. |
| `task_id` | path | `string` | Yes | The task ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of luau execution session task logs to return. The service might return fewer than this value. If unspecified, at most 10000 luau execution session task logs are returned. The maximum value is 10000 and higher values are set to 10000. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `view` | query | `VIEW_UNSPECIFIED \| FLAT \| STRUCTURED` | No | The view in which to retrieve the luau execution session task log.  Supports FLAT and STRUCTURED.  Defaults to FLAT.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| VIEW_UNSPECIFIED \| The luau execution session task log view is not specified; the default will be used. \|   \| FLAT \| If this view is selected, the `messages` field will be populated (and the `structuredMessages` field will not). Each entry of the `messages` array contains only the log message, without additional medata. This is the default. \|   \| STRUCTURED \| If this view is selected, the `structuredMessages` field will be populated (and the `messages` field will not). Each entry of the `structuredMessages` array contains the log message plus additional metadata (see `LogMessage` for details). \| Valid values: `VIEW_UNSPECIFIED`, `FLAT`, `STRUCTURED` |

**Responses:**

- `200`: OK → `ListLuauExecutionSessionTaskLogsResponse`

**Response fields** (`ListLuauExecutionSessionTaskLogsResponse`)

See [ListLuauExecutionSessionTaskLogsResponse](#listluauexecutionsessiontasklogsresponse) in Models.

**Response example:**
```json
{
  "luauExecutionSessionTaskLogs": [
    {
      "path": "...",
      "messages": "...",
      "structuredMessages": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}/versions/{VERSION_ID}/luau-execution-sessions/{LUAU_EXECUTION_SESSION_ID}/tasks/{TASK_ID}/logs"
```

### GET `/cloud/v2/universes/{universe_id}/subscription-products/{subscription_product_id}/subscriptions/{subscription_id}`

Get Subscription

Get the subscription.

The `universe.subscription-product.subscription:read` scope only allows
reading subscriptions of the user making the request. Because of this, the
subscription ID must match the user ID of the user making the request. Note
that this scope might be more relevant for OAuth 2.0 apps.

To read all subscriptions made by users for a particular universe, use the
`universe:write` scope instead.

**Scopes:** `universe:write`, `universe.subscription-product.subscription:read`

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

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/subscription-products/{SUBSCRIPTION_PRODUCT_ID}/subscriptions/{SUBSCRIPTION_ID}"
```

### GET `/cloud/v2/universes/{universe_id}/user-restrictions`

List User Restrictions

List user restrictions for users that have ever been banned in either a
universe or a specific place.

**Scopes:** `universe.user-restriction:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of user restrictions to return. The service might return fewer than this value. If unspecified, at most 10 user restrictions are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |

**Responses:**

- `200`: OK → `ListUserRestrictionsResponse`

**Response fields** (`ListUserRestrictionsResponse`)

See [ListUserRestrictionsResponse](#listuserrestrictionsresponse) in Models.

**Response example:**
```json
{
  "userRestrictions": [
    {
      "path": "...",
      "updateTime": "...",
      "user": "...",
      "gameJoinRestriction": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limit Note:** User Restrictions are subject to the additional rate limits, applied per universe

* Get User Restriction: 50 req/s
* List User Restrictions: 50 req/s
* Update User Restrictions: 10 req/s
* List User Restriction Logs: 50 req/s

Additionally, we impose the following rate limit for the same user within a universe:

* Update User Restriction: 2 req/min

For example, Update User Restriction may not be called for user 123 more than twice every minute.

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/user-restrictions"
```

### GET `/cloud/v2/universes/{universe_id}/user-restrictions/{user_restriction_id}`

Get User Restriction

Get the user restriction.

**Scopes:** `universe.user-restriction:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `user_restriction_id` | path | `string` | Yes | The user-restriction ID. |

**Responses:**

- `200`: OK → `UserRestriction`

**Response fields** (`UserRestriction`)

See [UserRestriction](#userrestriction) in Models.

**Response example:**
```json
{
  "path": "string",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "gameJoinRestriction": {
    "active": false,
    "startTime": "2024-01-01T00:00:00Z",
    "duration": "string",
    "privateReason": "string",
    "displayReason": "string",
    "excludeAltAccounts": false
  }
}
```

**Rate Limit Note:** User Restrictions are subject to the additional rate limits, applied per universe

* Get User Restriction: 50 req/s
* List User Restrictions: 50 req/s
* Update User Restrictions: 10 req/s
* List User Restriction Logs: 50 req/s

Additionally, we impose the following rate limit for the same user within a universe:

* Update User Restriction: 2 req/min

For example, Update User Restriction may not be called for user 123 more than twice every minute.

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/user-restrictions/{USER_RESTRICTION_ID}"
```

### PATCH `/cloud/v2/universes/{universe_id}/user-restrictions/{user_restriction_id}`

Update User Restriction

Update the user restriction.

**Scopes:** `universe.user-restriction:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `user_restriction_id` | path | `string` | Yes | The user-restriction ID. |
| `updateMask` | query | `string` | No | The list of fields to update.  The `game_join_restriction` field must be updated atomically; field masks that index into `game_join_restriction` (such as `"game_join_restriction.active"`) are not supported. |
| `idempotencyKey.key` | query | `string` | No | The unique key to use for idempotency. |
| `idempotencyKey.firstSent` | query | `string` | No | The timestamp at which the first request was sent.  If this is further in the past than the lifetime of the idempotency key (which *may* exceed the annotated minimum lifetime), the server *must* return an error. |

**Request Body:** `application/json` — Type: `UserRestriction`

See [UserRestriction](#userrestriction) in Models.

**Request example:**
```json
{
  "path": "string",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "gameJoinRestriction": {
    "active": false,
    "startTime": "2024-01-01T00:00:00Z",
    "duration": "string",
    "privateReason": "string",
    "displayReason": "string",
    "excludeAltAccounts": false
  }
}
```

**Responses:**

- `200`: OK → `UserRestriction`

**Response fields** (`UserRestriction`)

See [UserRestriction](#userrestriction) in Models.

**Response example:**
```json
{
  "path": "string",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "gameJoinRestriction": {
    "active": false,
    "startTime": "2024-01-01T00:00:00Z",
    "duration": "string",
    "privateReason": "string",
    "displayReason": "string",
    "excludeAltAccounts": false
  }
}
```

**Rate Limit Note:** User Restrictions are subject to the additional rate limits, applied per universe

* Get User Restriction: 50 req/s
* List User Restrictions: 50 req/s
* Update User Restrictions: 10 req/s
* List User Restriction Logs: 50 req/s

Additionally, we impose the following rate limit for the same user within a universe:

* Update User Restriction: 2 req/min

For example, Update User Restriction may not be called for user 123 more than twice every minute.

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/user-restrictions/{USER_RESTRICTION_ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "gameJoinRestriction": {
    "active": false,
    "startTime": "2024-01-01T00:00:00Z",
    "duration": "string",
    "privateReason": "string",
    "displayReason": "string",
    "excludeAltAccounts": false
  }
}'
```

### GET `/cloud/v2/universes/{universe_id}/user-restrictions:listLogs`

List User Restriction Logs

List changes to UserRestriction resources within a given universe.
This includes both universe-level and place-level restrictions.

For universe-level restriction logs, the `place` field will be empty.

**Scopes:** `universe.user-restriction:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of UserRestrictionLogs to return. The service may return fewer than this value. If unspecified, at most 10 UserRestrictionLogs are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | This field may be set to filter the logs returned.  The `filter` field supports a very small number of CEL:  * `user` * `place` * The `==` comparison operator is available. * The `&&` logical operator is also supported.  As an example, filtering for a user and a place takes the form `filter="user == 'users/123'" && "place == 'places/456'"` |

**Responses:**

- `200`: OK → `ListUserRestrictionLogsResponse`

**Response fields** (`ListUserRestrictionLogsResponse`)

See [ListUserRestrictionLogsResponse](#listuserrestrictionlogsresponse) in Models.

**Response example:**
```json
{
  "logs": [
    {
      "user": "...",
      "place": "...",
      "moderator": "...",
      "createTime": "...",
      "active": "...",
      "startTime": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limit Note:** User Restrictions are subject to the additional rate limits, applied per universe

* Get User Restriction: 50 req/s
* List User Restrictions: 50 req/s
* Update User Restrictions: 10 req/s
* List User Restriction Logs: 50 req/s

Additionally, we impose the following rate limit for the same user within a universe:

* Update User Restriction: 2 req/min

For example, Update User Restriction may not be called for user 123 more than twice every minute.

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/user-restrictions:listLogs"
```

### POST `/cloud/v2/universes/{universe_id}:generateSpeechAsset`

Generate Speech Asset

Generates an English speech audio asset from the specified text.

This endpoint requires the `asset:read` and `asset:write` scopes in
addition to the `universe:write` scope.

The response returns an `Operation` object that must be prefixed with
`/assets/v1`. For example, the URL to discover the result of the operation
could be
`https://apis.roblox.com/assets/v1/operations/8b42ef30-9c17-4526-b8cf-2ff0136ca94d`.

**Scopes:** `universe:write`, `asset:read`, `asset:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |

**Request Body:** `application/json` — Type: `GenerateSpeechAssetRequest`

See [GenerateSpeechAssetRequest](#generatespeechassetrequest) in Models.

**Request example:**
```json
{
  "text": "string",
  "speechStyle": {
    "voiceId": "string",
    "pitch": 0,
    "speed": 0
  }
}
```

**Responses:**

- `200`: OK → `Operation`

**Response fields** (`Operation`)

See [Operation](#operation) in Models.

**Response example:**
```json
{
  "path": "string",
  "metadata": {
    "@type": "string"
  },
  "done": false,
  "error": {
    "code": 0,
    "message": "string",
    "details": [
      "..."
    ]
  },
  "response": {
    "@type": "string"
  }
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}:generateSpeechAsset" \
  -H "Content-Type: application/json" \
  -d '{
  "text": "string",
  "speechStyle": {
    "voiceId": "string",
    "pitch": 0,
    "speed": 0
  }
}'
```

### POST `/cloud/v2/universes/{universe_id}:publishMessage`

Publish Universe Message

Publishes a message to the universe's live servers.

Servers can consume messages via
[MessagingService](https://create.roblox.com/docs/reference/engine/classes/MessagingService).

**Scopes:** `universe-messaging-service:publish`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |

**Request Body:** `application/json` — Type: `PublishUniverseMessageRequest`

See [PublishUniverseMessageRequest](#publishuniversemessagerequest) in Models.

**Request example:**
```json
{
  "topic": "string",
  "message": "string"
}
```

**Responses:**

- `200`: OK

**Rate Limit Note:** Messaging Service requests are subject to additional throttling limits described in the [Open Cloud guide for Messaging Service](https://create.roblox.com/docs/cloud/guides/usage-messaging#limits).

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}:publishMessage" \
  -H "Content-Type: application/json" \
  -d '{
  "topic": "string",
  "message": "string"
}'
```

### POST `/cloud/v2/universes/{universe_id}:restartServers`

Restart Universe Servers

Restarts active servers for a specific universe. Defaults to only
restarting servers running older versions, but can be configured to restart
all servers regardless of version. Used for releasing experience updates.

**Scopes:** `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |

**Request Body:** `application/json` — Type: `RestartUniverseServersRequest`

See [RestartUniverseServersRequest](#restartuniverseserversrequest) in Models.

**Request example:**
```json
{
  "placeIds": [
    0
  ],
  "closeAllVersions": false,
  "bleedOffServers": false,
  "bleedOffDurationMinutes": 0
}
```

**Responses:**

- `200`: OK → `RestartUniverseServersResponse`

**Response fields** (`RestartUniverseServersResponse`)

See [RestartUniverseServersResponse](#restartuniverseserversresponse) in Models.

**Response example:**
```json
{}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}:restartServers" \
  -H "Content-Type: application/json" \
  -d '{
  "placeIds": [
    0
  ],
  "closeAllVersions": false,
  "bleedOffServers": false,
  "bleedOffDurationMinutes": 0
}'
```

### POST `/cloud/v2/universes/{universe_id}:translateText`

Translate Text

Translates the provided text from one language to another.

**Scopes:** `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |

**Request Body:** `application/json` — Type: `TranslateTextRequest`

See [TranslateTextRequest](#translatetextrequest) in Models.

**Request example:**
```json
{
  "text": "string",
  "sourceLanguageCode": "string",
  "targetLanguageCodes": [
    "string"
  ]
}
```

**Responses:**

- `200`: OK → `TranslateTextResponse`

**Response fields** (`TranslateTextResponse`)

See [TranslateTextResponse](#translatetextresponse) in Models.

**Response example:**
```json
{
  "sourceLanguageCode": "string",
  "translations": "..."
}
```

**Rate Limit Note:** Text translation requests are subject to additional rate limits [documented here](https://create.roblox.com/docs/production/localization/auto-translate-dynamic-content#limits).

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}:translateText" \
  -H "Content-Type: application/json" \
  -d '{
  "text": "string",
  "sourceLanguageCode": "string",
  "targetLanguageCodes": [
    "string"
  ]
}'
```

### GET `/cloud/v2/users/{user_id}/asset-quotas`

List Asset Quotas

Returns a list of asset quotas.

**Scopes:** `asset:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `user_id` | path | `string` | Yes | The user ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of asset quotas to return. The service might return fewer than this value. If unspecified, at most 10 asset quotas are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  Supports the following subset of CEL: * Only the `quotaType` and `assetType` fields are supported. * Only the `==` and `&&` operator are supported.  For example:   `quotaType == RateLimitUpload && assetType == Audio` |

**Responses:**

- `200`: OK → `ListAssetQuotasResponse`

**Response fields** (`ListAssetQuotasResponse`)

See [ListAssetQuotasResponse](#listassetquotasresponse) in Models.

**Response example:**
```json
{
  "assetQuotas": [
    {
      "path": "...",
      "quotaType": "...",
      "assetType": "...",
      "usage": "...",
      "capacity": "...",
      "period": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/users/{USER_ID}/asset-quotas"
```

### POST `/cloud/v2/users/{user_id}/notifications`

Create User Notification

Sends a notification to a user.

**Scopes:** `user.user-notification:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `user_id` | path | `string` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `UserNotification`

See [UserNotification](#usernotification) in Models.

**Request example:**
```json
{
  "path": "string",
  "id": "string",
  "source": {
    "universe": "string"
  },
  "payload": {
    "type": "TYPE_UNSPECIFIED",
    "messageId": "string",
    "parameters": "...",
    "joinExperience": {
      "launchData": "..."
    },
    "analyticsData": {
      "category": "..."
    }
  }
}
```

**Responses:**

- `200`: OK → `UserNotification`

**Response fields** (`UserNotification`)

See [UserNotification](#usernotification) in Models.

**Response example:**
```json
{
  "path": "string",
  "id": "string",
  "source": {
    "universe": "string"
  },
  "payload": {
    "type": "TYPE_UNSPECIFIED",
    "messageId": "string",
    "parameters": "...",
    "joinExperience": {
      "launchData": "..."
    },
    "analyticsData": {
      "category": "..."
    }
  }
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/cloud/v2/users/{USER_ID}/notifications" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "id": "string",
  "source": {
    "universe": "string"
  },
  "payload": {
    "type": "TYPE_UNSPECIFIED",
    "messageId": "string",
    "parameters": "...",
    "joinExperience": {
      "launchData": "..."
    },
    "analyticsData": {
      "category": "..."
    }
  }
}'
```
