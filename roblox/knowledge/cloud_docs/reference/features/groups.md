---
name: "Groups"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 116
auth: [api-key, oauth2, cookie]
description: "Manage Roblox groups including memberships, roles, and group settings"
---

# Groups

Manage Roblox groups including memberships, roles, and group settings.

Common use cases include:

- Membership management: [Accept](#Cloud_AcceptGroupJoinRequest) or [decline](#Cloud_DeclineGroupJoinRequest) join requests and [manage member roles](#Cloud_UpdateGroupMembership)
- Role configuration: [Create](#groups_post_v1_groups__groupId__rolesets_create), [update](#groups_patch_v1_groups__groupId__rolesets__rolesetId_), and [delete](#groups_delete_v1_groups__groupId__rolesets__rolesetId_) group roles with custom permissions
- Audit logging: [Review group activity](#get_legacy_groups_v1_groups__groupId__audit_log) through audit logs

> **See also:** To group member inventories, see [inventories](/docs/cloud/reference/features/inventories.md).

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

### GET `/cloud/v2/groups/{group_id}` [BETA]

Get Group

Gets the specified group.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

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

**Rate Limits:** perApiKeyOwner: 150/minute, perOauth2Authorization: 30/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}"
```

### GET `/cloud/v2/groups/{group_id}/forum-categories` [BETA]

List Group Forum Categories

Lists forum categories in the group. Supports filtering.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `group-forum:read`, `group-forum:read`

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

**Rate Limits:** perApiKeyOwner: 150/minute, perOauth2Authorization: 30/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/forum-categories"
```

### GET `/cloud/v2/groups/{group_id}/forum-categories/{forum_category_id}/posts` [BETA]

List Group Forum Posts

Lists forum posts in the group's forum category. Supports filtering.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `group-forum:read`, `group-forum:read`

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

**Rate Limits:** perApiKeyOwner: 150/minute, perOauth2Authorization: 30/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/forum-categories/{FORUM_CATEGORY_ID}/posts"
```

### GET `/cloud/v2/groups/{group_id}/forum-categories/{forum_category_id}/posts/{post_id}/comments` [BETA]

List Group Forum Comments

Lists forum comments on a group's forum post. Supports filtering.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `group-forum:read`, `group-forum:read`

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

**Rate Limits:** perApiKeyOwner: 150/minute, perOauth2Authorization: 30/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/forum-categories/{FORUM_CATEGORY_ID}/posts/{POST_ID}/comments"
```

### GET `/cloud/v2/groups/{group_id}/join-requests` [BETA]

List Group Join Requests

List join requests under a group. Supports filtering.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `group:read`, `group:read`

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

**Rate Limits:** perApiKeyOwner: 300/minute, perOauth2Authorization: 90/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/join-requests"
```

### POST `/cloud/v2/groups/{group_id}/join-requests/{join_request_id}:accept` [BETA]

Accept Group Join Request

Accepts a join request.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `group:write`, `group:write`

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

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 90/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/join-requests/{JOIN_REQUEST_ID}:accept" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST `/cloud/v2/groups/{group_id}/join-requests/{join_request_id}:decline` [BETA]

Decline Group Join Request

Declines a join request.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `group:write`, `group:write`

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

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 90/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/join-requests/{JOIN_REQUEST_ID}:decline" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### GET `/cloud/v2/groups/{group_id}/memberships` [BETA]

List Group Memberships

List group members in a group. Supports filtering.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `group_id` | path | `string` | Yes | The group ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of group memberships to return. The service might return fewer than this value. If unspecified, at most 10 group memberships are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  See the [filtering](/cloud/reference/patterns#list-group-memberships) documentation for more information. |

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

**Rate Limits:** perApiKeyOwner: 300/minute, perOauth2Authorization: 90/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/memberships"
```

### PATCH `/cloud/v2/groups/{group_id}/memberships/{membership_id}` [BETA]

Update Group Membership

**Deprecated.** Use AssignGroupRole and UnassignGroupRole instead.
Updates the group membership for a particular group member. This action
requires the requester to be able to assign or remove roles below their
highest role. The requester cannot change their own roles.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `group:write`, `group:write`

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

**Rate Limits:** perApiKeyOwner: 300/minute, perOauth2Authorization: 90/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
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

### POST `/cloud/v2/groups/{group_id}/memberships/{membership_id}:assignRole` [BETA]

Assign Role Group Membership

Assigns a specific role to a user within a group. If the user already
holds the specified role, no action is taken.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `group:write`, `group:write`

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

**Rate Limits:** perApiKeyOwner: 300/minute, perOauth2Authorization: 90/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/memberships/{MEMBERSHIP_ID}:assignRole" \
  -H "Content-Type: application/json" \
  -d '{
  "role": "string"
}'
```

### POST `/cloud/v2/groups/{group_id}/memberships/{membership_id}:unassignRole` [BETA]

Unassign Role Group Membership

Unassigns a specific role from a user within a group. If the user does
not hold the specified role, no action is taken.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `group:write`, `group:write`

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

**Rate Limits:** perApiKeyOwner: 300/minute, perOauth2Authorization: 90/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/memberships/{MEMBERSHIP_ID}:unassignRole" \
  -H "Content-Type: application/json" \
  -d '{
  "role": "string"
}'
```

### GET `/cloud/v2/groups/{group_id}/roles` [BETA]

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

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

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

**Rate Limits:** perApiKeyOwner: 300/minute, perOauth2Authorization: 90/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/roles"
```

### GET `/cloud/v2/groups/{group_id}/roles/{role_id}` [BETA]

Get Group Role

Get the group role

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

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

**Rate Limits:** perApiKeyOwner: 300/minute, perOauth2Authorization: 90/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/groups/{GROUP_ID}/roles/{ROLE_ID}"
```

### GET `/legacy-develop/v1/user/groups/canmanage` [EXPERIMENTAL]

Gets a list of Groups that a user can manage.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-group:manage`

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.GroupModel_`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.GroupModel_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.GroupModel_](#roblox-web-webapi-models-apiarrayresponse-roblox-api-develop-models-groupmodel-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "name": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-develop/v1/user/groups/canmanage"
```

### POST `/legacy-groups/v1/groups/policies`

Gets group policy info used for compliance.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-group:manage`

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.GroupPolicyRequest`

See [Roblox.Groups.Api.GroupPolicyRequest](#roblox-groups-api-grouppolicyrequest) in Models.

**Request example:**
```json
{
  "groupIds": [
    0
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupPoliciesResponse`
- `400`: 1: Too many ids in request. 2: Ids could not be parsed from request.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Groups.Api.GroupPoliciesResponse`)

See [Roblox.Groups.Api.GroupPoliciesResponse](#roblox-groups-api-grouppoliciesresponse) in Models.

**Response example:**
```json
{
  "groups": [
    {
      "canViewGroup": "...",
      "groupId": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-groups/v1/groups/policies" \
  -H "Content-Type: application/json" \
  -d '{
  "groupIds": [
    0
  ]
}'
```

### GET `/legacy-groups/v1/groups/{groupId}/audit-log`

Gets the Group's audit log

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-group:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The id of the group the user is in. |
| `actionType` | query | `string enum (80 values)` | No | Filter for specific type of action performed Valid values: `DeletePost`, `RemoveMember`, `AcceptJoinRequest`, `DeclineJoinRequest`, `PostStatus`, `ChangeRank`, `BuyAd`, `SendAllyRequest`, `CreateEnemy`, `AcceptAllyRequest`, `DeclineAllyRequest`, `DeleteAlly`, `DeleteEnemy`, `AddGroupPlace`, `RemoveGroupPlace`, `CreateItems`, `ConfigureItems`, `SpendGroupFunds`, `ChangeOwner`, `Delete`, `AdjustCurrencyAmounts`, `Abandon`, `Claim`, `Rename`, `ChangeDescription`, `InviteToClan`, `KickFromClan`, `CancelClanInvite`, `BuyClan`, `CreateGroupAsset`, `UpdateGroupAsset`, `ConfigureGroupAsset`, `RevertGroupAsset`, `CreateGroupDeveloperProduct`, `ConfigureGroupGame`, `CreateGroupDeveloperSubscriptionProduct`, `Lock`, `Unlock`, `CreateGamePass`, `CreateBadge`, `ConfigureBadge`, `SavePlace`, `PublishPlace`, `UpdateRolesetRank`, `UpdateRolesetData`, `UpdateRoleSetPosition`, `BanMember`, `UnbanMember`, `CreateForumCategory`, `UpdateForumCategory`, `ArchiveForumCategory`, `DeleteForumCategory`, `DeleteForumPost`, `DeleteForumComment`, `PinForumPost`, `UnpinForumPost`, `LockForumPost`, `UnlockForumPost`, `CreateRoleset`, `DeleteRoleset`, `CreateCommerceProduct`, `SetCommerceProductActive`, `ArchiveCommerceProduct`, `AcceptCommerceProductBundlingFee`, `SetCommerceProductInactive`, `ConnectMerchant`, `DisconnectMerchant`, `JoinGroup`, `LeaveGroup`, `UpdateGroupIcon`, `UpdateGroupCoverPhoto`, `AssignRole`, `UnassignRole`, `PublishAnnouncement`, `DeleteAnnouncement`, `UpdateRoleSetPermissions`, `UpdateGroupSecuritySettings`, `GrantEnterpriseTier`, `RevokeEnterpriseTier`, `DeactivateGroup` |
| `userId` | query | `integer` | No | Filter for specific user id |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupAuditLogPageResponse_Roblox.Groups.Api.Models.Response.GroupAuditLogResponseItem_`
- `400`: 1: Group is invalid or does not exist. 8: Invalid or missing pagination parameters
- `401`: 0: Authorization has been denied for this request.
- `403`: 23: Insufficient permissions to complete the request.

**Response fields** (`Roblox.Groups.Api.GroupAuditLogPageResponse_Roblox.Groups.Api.Models.Response.GroupAuditLogResponseItem_`)

See [Roblox.Groups.Api.GroupAuditLogPageResponse_Roblox.Groups.Api.Models.Response.GroupAuditLogResponseItem_](#roblox-groups-api-groupauditlogpageresponse-roblox-groups-api-models-response-groupauditlogresponseitem-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "actor": "...",
      "actionType": "...",
      "description": "...",
      "created": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-groups/v1/groups/{GROUPID}/audit-log"
```

### PATCH `/legacy-groups/v1/groups/{groupId}/description`

Updates the groups description

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-group:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The id of the group the user is in. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.UpdateGroupDescriptionRequest`

See [Roblox.Groups.Api.UpdateGroupDescriptionRequest](#roblox-groups-api-updategroupdescriptionrequest) in Models.

**Request example:**
```json
{
  "description": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupDescriptionResponse`
- `400`: 1: Group is invalid or does not exist. 29: Your group description was empty.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: The description is too long. 23: Insufficient permissions to complete the request.

**Response fields** (`Roblox.Groups.Api.GroupDescriptionResponse`)

See [Roblox.Groups.Api.GroupDescriptionResponse](#roblox-groups-api-groupdescriptionresponse) in Models.

**Response example:**
```json
{
  "newDescription": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-groups/v1/groups/{GROUPID}/description" \
  -H "Content-Type: application/json" \
  -d '{
  "description": "string"
}'
```

### PATCH `/legacy-groups/v1/groups/{groupId}/notification-preference`

Updates the group's settings

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-user:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The id of the group the user is in. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.UpdateGroupNotificationPreferenceRequest`

See [Roblox.Groups.Api.UpdateGroupNotificationPreferenceRequest](#roblox-groups-api-updategroupnotificationpreferencerequest) in Models.

**Request example:**
```json
{
  "notificationsEnabled": false,
  "type": 0
}
```

**Responses:**

- `200`: OK → `0 \| 1 \| 2 \| 3`
- `400`: 1: Group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-groups/v1/groups/{GROUPID}/notification-preference" \
  -H "Content-Type: application/json" \
  -d '{
  "notificationsEnabled": false,
  "type": 0
}'
```

### GET `/legacy-groups/v1/groups/{groupId}/settings`

Gets the Group's settings

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-group:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The id of the group the user is in. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupSettingsResponse`
- `400`: 1: Group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 23: Insufficient permissions to complete the request.

**Response fields** (`Roblox.Groups.Api.GroupSettingsResponse`)

See [Roblox.Groups.Api.GroupSettingsResponse](#roblox-groups-api-groupsettingsresponse) in Models.

**Response example:**
```json
{
  "isApprovalRequired": false,
  "isBuildersClubRequired": false,
  "areEnemiesAllowed": false,
  "areGroupFundsVisible": false,
  "areGroupGamesVisible": false,
  "isGroupNameChangeEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-groups/v1/groups/{GROUPID}/settings"
```

### PATCH `/legacy-groups/v1/groups/{groupId}/settings`

Updates the group's settings

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-group:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The id of the group the user is in. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.UpdateGroupSettingsRequest`

See [Roblox.Groups.Api.UpdateGroupSettingsRequest](#roblox-groups-api-updategroupsettingsrequest) in Models.

**Request example:**
```json
{
  "isApprovalRequired": false,
  "areEnemiesAllowed": false,
  "areGroupFundsVisible": false,
  "areGroupGamesVisible": false,
  "verificationLevel": 0,
  "accountTenureRequirement": 0
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 23: Insufficient permissions to complete the request.
- `503`: 31: Service is currently unavailable.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-groups/v1/groups/{GROUPID}/settings" \
  -H "Content-Type: application/json" \
  -d '{
  "isApprovalRequired": false,
  "areEnemiesAllowed": false,
  "areGroupFundsVisible": false,
  "areGroupGamesVisible": false,
  "verificationLevel": 0,
  "accountTenureRequirement": 0
}'
```

### PATCH `/legacy-groups/v1/groups/{groupId}/status`

Sets group status

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-group:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.PostGroupStatusRequest`

See [Roblox.Groups.Api.PostGroupStatusRequest](#roblox-groups-api-postgroupstatusrequest) in Models.

**Request example:**
```json
{
  "message": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Groups.Api.ShoutResponse`
- `400`: 1: Group is invalid or does not exist. 7: Missing group status content. 32: Description was filtered.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 6: You are not authorized to set the status of this group

**Response fields** (`Roblox.Groups.Api.ShoutResponse`)

See [Roblox.Groups.Api.ShoutResponse](#roblox-groups-api-shoutresponse) in Models.

**Response example:**
```json
{
  "body": "string",
  "poster": {
    "buildersClubMembershipType": 0,
    "hasVerifiedBadge": false,
    "userId": 0,
    "username": "string",
    "displayName": "string"
  },
  "created": "2024-01-01T00:00:00Z",
  "updated": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-groups/v1/groups/{GROUPID}/status" \
  -H "Content-Type: application/json" \
  -d '{
  "message": "string"
}'
```

### GET `/legacy-groups/v1/user/groups/pending`

Gets groups that the authenticated user has requested to join

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-group:manage`

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupDetailResponse_`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupDetailResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupDetailResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-groups-api-groupdetailresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "name": "...",
      "description": "...",
      "owner": "...",
      "shout": "...",
      "memberCount": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-groups/v1/user/groups/pending"
```

### GET `/v1/featured-content/event`

Gets the featured event for a group

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | query | `integer` | Yes | The group Id. |

**Responses:**

- `200`: OK → `Roblox.Groups.Client.GroupFeaturedContentResponse`

**Response fields** (`Roblox.Groups.Client.GroupFeaturedContentResponse`)

See [Roblox.Groups.Client.GroupFeaturedContentResponse](#roblox-groups-client-groupfeaturedcontentresponse) in Models.

**Response example:**
```json
{
  "groupId": 0,
  "contentType": "string",
  "contentId": "string"
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/featured-content/event?groupId={VALUE}"
```

### POST `/v1/featured-content/event`

Sets the featured event for a group

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | query | `integer` | Yes | The group Id. |
| `eventId` | query | `integer` | Yes | The event Id. |

**Responses:**

- `200`: OK → `Roblox.Groups.Client.GroupFeaturedContentResponse`
- `403`: 0: Token Validation Failed 3: User is not authorized to set featured content for this group.

**Response fields** (`Roblox.Groups.Client.GroupFeaturedContentResponse`)

See [Roblox.Groups.Client.GroupFeaturedContentResponse](#roblox-groups-client-groupfeaturedcontentresponse) in Models.

**Response example:**
```json
{
  "groupId": 0,
  "contentType": "string",
  "contentId": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/featured-content/event?groupId={VALUE}&eventId={VALUE}"
```

### DELETE `/v1/featured-content/event`

Deletes the featured event for a group

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | query | `integer` | Yes | The group Id. |
| `eventId` | query | `integer` | Yes | The event Id. |

**Responses:**

- `200`: OK
- `403`: 0: Token Validation Failed 3: User is not authorized to set featured content for this group.

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/featured-content/event?groupId={VALUE}&eventId={VALUE}"
```

### GET `/v1/groups/configuration/metadata`

Gets Group configuration contextual information

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupConfigurationDisplayOptionsResponse`

**Response fields** (`Roblox.Groups.Api.GroupConfigurationDisplayOptionsResponse`)

See [Roblox.Groups.Api.GroupConfigurationDisplayOptionsResponse](#roblox-groups-api-groupconfigurationdisplayoptionsresponse) in Models.

**Response example:**
```json
{
  "groupConfiguration": {
    "nameMaxLength": 0,
    "descriptionMaxLength": 0,
    "iconMaxFileSizeMb": 0,
    "coverPhotoMaxFileSizeMb": 0,
    "validCoverPhotoDimensions": "string",
    "cost": 0
  },
  "recurringPayoutsConfiguration": {
    "maxPayoutPartners": 0
  },
  "roleConfiguration": {
    "nameMaxLength": 0,
    "descriptionMaxLength": 0,
    "limit": 0,
    "cost": 0,
    "minRank": 0,
    "maxRank": 0
  },
  "groupNameChangeConfiguration": {
    "cost": 0,
    "cooldownInDays": 0,
    "ownershipCooldownInDays": 0
  },
  "isPremiumPayoutsEnabled": false,
  "isDefaultEmblemPolicyEnabled": false
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/configuration/metadata"
```

### POST `/v1/groups/create`

Creates a new group.

This endpoint will charge Robux for the group purchase.
Accepts "icon" and "coverPhoto" in Files object. Defaults to first file if "icon" is not present.
Http status code 413 is thrown when the group icon file size is too large.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `multipart/form-data` — Type: `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The name of the group. |
| `description` | `string` | No | The group description. |
| `publicGroup` | `boolean` | No | Whether or not the group is open for anyone to join. |
| `buildersClubMembersOnly` | `boolean` | No | Whether or not the group is only open to join for builders club members. |
| `Files` | `string` | No |  |

**Request example:**
```json
{
  "name": "string",
  "description": "string",
  "publicGroup": false,
  "buildersClubMembersOnly": false,
  "Files": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.Responses.Groups.GroupResponseV2`
- `400`: 13: The name is invalid. 15: The group icon is invalid. 16: The group icon is missing from the request. 18: The description is too long. 19: The name is too long. 20: The name has been taken. 46: Invalid file format or dimensions for group cover photo.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 10: User must have builders club membership. 11: User is in maximum number of groups. 12: Insufficient Robux funds. 14: The name is moderated.
- `409`: 37: The name was in use too recently.
- `413`: 0: Unknown error.
- `429`: 17: Too many requests.
- `503`: 21: Group creation is currently disabled.

**Response fields** (`Roblox.Web.Responses.Groups.GroupResponseV2`)

See [Roblox.Web.Responses.Groups.GroupResponseV2](#roblox-web-responses-groups-groupresponsev2) in Models.

**Response example:**
```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "owner": {
    "id": 0,
    "type": 0,
    "name": "string"
  },
  "memberCount": 0,
  "created": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/create" \
  -F "name=string" \
  -F "description=string" \
  -F "publicGroup=false" \
  -F "buildersClubMembersOnly=false" \
  -F "Files=@file.bin;type=application/octet-stream"
```

### PATCH `/v1/groups/icon`

Updates the group icon.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | query | `integer` | Yes | The group Id. |

**Request Body:** `multipart/form-data` — Type: `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Files` | `string` | No |  |

**Request example:**
```json
{
  "Files": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Group is invalid or does not exist. 16: The group icon is missing from the request. 17: Too many requests. 30: Invalid file type for group icon.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 23: Insufficient permissions to complete the request.
- `413`: 0: Unknown error.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/icon?groupId={VALUE}" \
  -F "Files=@file.bin;type=application/octet-stream"
```

### GET `/v1/groups/icons` [STABLE]

Fetches thumbnail URLs for a list of groups. Ids that do not correspond to groups will be filtered out.

**Server:** `https://thumbnails.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupIds` | query | `integer[]` | Yes |  |
| `size` | query | `150x150 \| 420x420` | No | The thumbnail size, formatted widthxheight Valid values: `150x150`, `420x420` |
| `format` | query | `Png \| Webp` | No | The thumbnail format Valid values: `Png`, `Webp` |
| `isCircular` | query | `true \| false` | No | The circle thumbnail output parameter, true or false Valid values: `true`, `false` |

**Responses:**

- `200`: OK
- `400`: 1: There are too many requested Ids. 2: The requested image format is invalid. Please see documentation for valid thumbnail format parameter name and values. 3: The requested size is invalid. Please see documentation for valid thumbnail size parameter name and format. 4: The requested Ids are invalid, of an invalid type or missing. 10: Circular thumbnail requests are not allowed

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://thumbnails.roblox.com/v1/groups/icons?groupIds={VALUE}"
```

### GET `/v1/groups/metadata`

Gets Groups contextual information:
Max number of groups a user can be part of.
Current number of groups a user is a member of.
Whether to show/hide certain features based on device type.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupsDisplayOptionsResponse`

**Response fields** (`Roblox.Groups.Api.GroupsDisplayOptionsResponse`)

See [Roblox.Groups.Api.GroupsDisplayOptionsResponse](#roblox-groups-api-groupsdisplayoptionsresponse) in Models.

**Response example:**
```json
{
  "groupLimit": 0,
  "currentGroupCount": 0,
  "groupStatusMaxLength": 0,
  "areProfileGroupsHidden": false,
  "isGroupDetailsPolicyEnabled": false,
  "showPreviousGroupNames": false
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/metadata"
```

### POST `/v1/groups/policies`

Gets group policy info used for compliance.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.GroupPolicyRequest`

See [Roblox.Groups.Api.GroupPolicyRequest](#roblox-groups-api-grouppolicyrequest) in Models.

**Request example:**
```json
{
  "groupIds": [
    0
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupPoliciesResponse`
- `400`: 1: Too many ids in request. 2: Ids could not be parsed from request.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Groups.Api.GroupPoliciesResponse`)

See [Roblox.Groups.Api.GroupPoliciesResponse](#roblox-groups-api-grouppoliciesresponse) in Models.

**Response example:**
```json
{
  "groups": [
    {
      "canViewGroup": "...",
      "groupId": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/policies" \
  -H "Content-Type: application/json" \
  -d '{
  "groupIds": [
    0
  ]
}'
```

### GET `/v1/groups/search`

Search for groups by keyword.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `keyword` | query | `string` | Yes | The keyword or phrase to use as the search parameter. |
| `prioritizeExactMatch` | query | `boolean` | No | Whether to move the exact-name group to first (optional, defaults to false). Ignored when the user's group search config sets its own position. |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupSearchPageResponse`
- `400`: 2: Search term not appropriate for Roblox. 3: Search term was left empty.

**Response fields** (`Roblox.Groups.Api.GroupSearchPageResponse`)

See [Roblox.Groups.Api.GroupSearchPageResponse](#roblox-groups-api-groupsearchpageresponse) in Models.

**Response example:**
```json
{
  "keyword": "string",
  "totalResults": 0,
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "name": "...",
      "description": "...",
      "memberCount": "...",
      "previousName": "...",
      "publicEntryAllowed": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/search?keyword={VALUE}"
```

### GET `/v1/groups/search/lookup`

Looks up groups by a name. Prioritizes an exact match as the first result.

Should only be used for direct lookups where a user is inputting a group name, shouldn't be used for search pages.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupName` | query | `string` | Yes | The group name. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Web.Responses.Groups.GroupBasicResponse_`
- `400`: 1: Name is missing or has invalid characters.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Web.Responses.Groups.GroupBasicResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Web.Responses.Groups.GroupBasicResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-web-responses-groups-groupbasicresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "name": "...",
      "memberCount": "...",
      "hasVerifiedBadge": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/search/lookup?groupName={VALUE}"
```

### GET `/v1/groups/search/metadata`

Get suggested groups and other miscellaneous information needed for the group/join page like flags

Although there is no reason for this to require an authenticated user right now, in the future,
we will use coco to return different suggested groups based upon that user's request context

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupSearchMetadataResponse`
- `404`: 5: No Localized Version of group search category exists

**Response fields** (`Roblox.Groups.Api.GroupSearchMetadataResponse`)

See [Roblox.Groups.Api.GroupSearchMetadataResponse](#roblox-groups-api-groupsearchmetadataresponse) in Models.

**Response example:**
```json
{
  "SuggestedGroupKeywords": [
    "string"
  ],
  "ShowFriendsGroupsSort": false
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/search/metadata"
```

### GET `/v1/groups/{groupId}`

Gets group information

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupDetailResponse`
- `400`: 1: Group is invalid or does not exist.

**Response fields** (`Roblox.Groups.Api.GroupDetailResponse`)

See [Roblox.Groups.Api.GroupDetailResponse](#roblox-groups-api-groupdetailresponse) in Models.

**Response example:**
```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "owner": {
    "buildersClubMembershipType": 0,
    "hasVerifiedBadge": false,
    "userId": 0,
    "username": "string",
    "displayName": "string"
  },
  "shout": {
    "body": "string",
    "poster": {
      "buildersClubMembershipType": "...",
      "hasVerifiedBadge": "...",
      "userId": "...",
      "username": "...",
      "displayName": "..."
    },
    "created": "2024-01-01T00:00:00Z",
    "updated": "2024-01-01T00:00:00Z"
  },
  "memberCount": 0
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}"
```

### GET `/v1/groups/{groupId}/audit-log`

Gets the Group's audit log

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The id of the group the user is in. |
| `actionType` | query | `string enum (80 values)` | No | Filter for specific type of action performed Valid values: `DeletePost`, `RemoveMember`, `AcceptJoinRequest`, `DeclineJoinRequest`, `PostStatus`, `ChangeRank`, `BuyAd`, `SendAllyRequest`, `CreateEnemy`, `AcceptAllyRequest`, `DeclineAllyRequest`, `DeleteAlly`, `DeleteEnemy`, `AddGroupPlace`, `RemoveGroupPlace`, `CreateItems`, `ConfigureItems`, `SpendGroupFunds`, `ChangeOwner`, `Delete`, `AdjustCurrencyAmounts`, `Abandon`, `Claim`, `Rename`, `ChangeDescription`, `InviteToClan`, `KickFromClan`, `CancelClanInvite`, `BuyClan`, `CreateGroupAsset`, `UpdateGroupAsset`, `ConfigureGroupAsset`, `RevertGroupAsset`, `CreateGroupDeveloperProduct`, `ConfigureGroupGame`, `CreateGroupDeveloperSubscriptionProduct`, `Lock`, `Unlock`, `CreateGamePass`, `CreateBadge`, `ConfigureBadge`, `SavePlace`, `PublishPlace`, `UpdateRolesetRank`, `UpdateRolesetData`, `UpdateRoleSetPosition`, `BanMember`, `UnbanMember`, `CreateForumCategory`, `UpdateForumCategory`, `ArchiveForumCategory`, `DeleteForumCategory`, `DeleteForumPost`, `DeleteForumComment`, `PinForumPost`, `UnpinForumPost`, `LockForumPost`, `UnlockForumPost`, `CreateRoleset`, `DeleteRoleset`, `CreateCommerceProduct`, `SetCommerceProductActive`, `ArchiveCommerceProduct`, `AcceptCommerceProductBundlingFee`, `SetCommerceProductInactive`, `ConnectMerchant`, `DisconnectMerchant`, `JoinGroup`, `LeaveGroup`, `UpdateGroupIcon`, `UpdateGroupCoverPhoto`, `AssignRole`, `UnassignRole`, `PublishAnnouncement`, `DeleteAnnouncement`, `UpdateRoleSetPermissions`, `UpdateGroupSecuritySettings`, `GrantEnterpriseTier`, `RevokeEnterpriseTier`, `DeactivateGroup` |
| `userId` | query | `integer` | No | Filter for specific user id |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupAuditLogPageResponse_Roblox.Groups.Api.Models.Response.GroupAuditLogResponseItem_`
- `400`: 1: Group is invalid or does not exist. 8: Invalid or missing pagination parameters
- `401`: 0: Authorization has been denied for this request.
- `403`: 23: Insufficient permissions to complete the request.

**Response fields** (`Roblox.Groups.Api.GroupAuditLogPageResponse_Roblox.Groups.Api.Models.Response.GroupAuditLogResponseItem_`)

See [Roblox.Groups.Api.GroupAuditLogPageResponse_Roblox.Groups.Api.Models.Response.GroupAuditLogResponseItem_](#roblox-groups-api-groupauditlogpageresponse-roblox-groups-api-models-response-groupauditlogresponseitem-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "actor": "...",
      "actionType": "...",
      "description": "...",
      "created": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/audit-log"
```

### POST `/v1/groups/{groupId}/change-owner`

Changes the group owner to another user.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.ChangeOwnerRequest`

See [Roblox.Groups.Api.ChangeOwnerRequest](#roblox-groups-api-changeownerrequest) in Models.

**Request example:**
```json
{
  "userId": 0
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: The group is invalid or does not exist. 3: The user is invalid or does not exist. 15: User is not a member of the group. 16: The user does not have the necessary level of premium membership.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 17: You are not authorized to change the owner of this group. 25: 2-Step Verification is required to make further transactions. Go to Settings > Security to complete 2-Step Verification.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/change-owner" \
  -H "Content-Type: application/json" \
  -d '{
  "userId": 0
}'
```

### POST `/v1/groups/{groupId}/claim-ownership`

Claims ownership of the group as the authenticated user

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: The group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 11: You are not authorized to claim this group 12: This group already has an owner 13: Too many attempts to claim groups. Please try again later.
- `503`: 18: The operation is temporarily unavailable. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/claim-ownership"
```

### GET `/v1/groups/{groupId}/community-feature-freezes` [EXPERIMENTAL]

Gets the freeze status of the community features for a group.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GetCommunityFeatureFreezesResponse`

**Response fields** (`Roblox.Groups.Api.GetCommunityFeatureFreezesResponse`)

See [Roblox.Groups.Api.GetCommunityFeatureFreezesResponse](#roblox-groups-api-getcommunityfeaturefreezesresponse) in Models.

**Response example:**
```json
{
  "features": [
    {
      "feature": "...",
      "isDisabled": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/community-feature-freezes"
```

### POST `/v1/groups/{groupId}/community-tier/evaluate` [EXPERIMENTAL]

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Groups.Client.TierEvaluationResultResponse`
- `400`: 1: Group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 22: The feature is disabled. 23: Insufficient permissions to complete the request. 49: User is invalid or does not exist

**Response fields** (`Roblox.Groups.Client.TierEvaluationResultResponse`)

See [Roblox.Groups.Client.TierEvaluationResultResponse](#roblox-groups-client-tierevaluationresultresponse) in Models.

**Response example:**
```json
{
  "tierInfo": {
    "groupId": 0,
    "currentTier": 0,
    "previousTier": 0,
    "tierUpdatedTime": "2024-01-01T00:00:00Z",
    "lastEvaluatedTime": "2024-01-01T00:00:00Z",
    "requirements": [
      "..."
    ]
  },
  "passedSignals": [
    "string"
  ],
  "requirements": [
    {
      "key": "...",
      "satisfied": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/community-tier/evaluate"
```

### GET `/v1/groups/{groupId}/configuration`

Gets group configuration information

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupConfigurationDetailsResponse`
- `400`: 1: Group is invalid or does not exist. 15: User is not a member of the group.
- `403`: 1: Group is invalid or does not exist. 23: Insufficient permissions to complete the request.
- `503`: 31: Service is currently unavailable.

**Response fields** (`Roblox.Groups.Api.GroupConfigurationDetailsResponse`)

See [Roblox.Groups.Api.GroupConfigurationDetailsResponse](#roblox-groups-api-groupconfigurationdetailsresponse) in Models.

**Response example:**
```json
{
  "groupId": 0,
  "emblemId": 0,
  "coverPhotoId": 0
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/configuration"
```

### POST `/v1/groups/{groupId}/deactivate`

Deactivates the group as its owner.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 19: You have insufficient permissions for this request.
- `404`: 1: The group is invalid or does not exist.
- `409`: 18: The operation is temporarily unavailable. Please try again later.
- `500`: 0: Something went wrong.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/deactivate"
```

### PATCH `/v1/groups/{groupId}/description`

Updates the groups description

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The id of the group the user is in. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.UpdateGroupDescriptionRequest`

See [Roblox.Groups.Api.UpdateGroupDescriptionRequest](#roblox-groups-api-updategroupdescriptionrequest) in Models.

**Request example:**
```json
{
  "description": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupDescriptionResponse`
- `400`: 1: Group is invalid or does not exist. 29: Your group description was empty.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: The description is too long. 23: Insufficient permissions to complete the request.

**Response fields** (`Roblox.Groups.Api.GroupDescriptionResponse`)

See [Roblox.Groups.Api.GroupDescriptionResponse](#roblox-groups-api-groupdescriptionresponse) in Models.

**Response example:**
```json
{
  "newDescription": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/description" \
  -H "Content-Type: application/json" \
  -d '{
  "description": "string"
}'
```

### GET `/v1/groups/{groupId}/emotes`

Gets a groups emote sets.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Groups.Client.GetGroupEmoteSetsResponse`

**Response fields** (`Roblox.Groups.Client.GetGroupEmoteSetsResponse`)

See [Roblox.Groups.Client.GetGroupEmoteSetsResponse](#roblox-groups-client-getgroupemotesetsresponse) in Models.

**Response example:**
```json
{
  "emoteSets": [
    {
      "id": "...",
      "name": "...",
      "emotes": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/emotes"
```

### GET `/v1/groups/{groupId}/features` [EXPERIMENTAL]

Gets the freeze status of all features and the lock status for a group.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GetGroupFeaturesResponse`
- `400`: 1: Group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 23: Insufficient permissions to complete the request. 49: User is invalid or does not exist

**Response fields** (`Roblox.Groups.Api.GetGroupFeaturesResponse`)

See [Roblox.Groups.Api.GetGroupFeaturesResponse](#roblox-groups-api-getgroupfeaturesresponse) in Models.

**Response example:**
```json
{
  "isLocked": false,
  "features": [
    {
      "feature": "...",
      "isFeatureBlocked": "...",
      "expiration": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/features"
```

### PATCH `/v1/groups/{groupId}/features` [EXPERIMENTAL]

Sets the desired status of group features.
Currently only removes active freezes for features set to Roblox.Groups.Api.FeatureStatus.On.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.SetFeaturesRequestModel`

See [Roblox.Groups.Api.SetFeaturesRequestModel](#roblox-groups-api-setfeaturesrequestmodel) in Models.

**Request example:**
```json
{
  "Features": {
    "Payouts": "On",
    "ContentUpload": "On",
    "GroupOwnershipTransfer": "On",
    "GameOwnershipTransfer": "On",
    "ForumRead": "On",
    "ForumWrite": "On"
  }
}
```

**Responses:**

- `200`: OK → `Roblox.Groups.Api.SetFeaturesResponseModel`
- `400`: 1: Group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 23: Insufficient permissions to complete the request. 49: User is invalid or does not exist

**Response fields** (`Roblox.Groups.Api.SetFeaturesResponseModel`)

See [Roblox.Groups.Api.SetFeaturesResponseModel](#roblox-groups-api-setfeaturesresponsemodel) in Models.

**Response example:**
```json
{
  "Updated": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/features" \
  -H "Content-Type: application/json" \
  -d '{
  "Features": {
    "Payouts": "On",
    "ContentUpload": "On",
    "GroupOwnershipTransfer": "On",
    "GameOwnershipTransfer": "On",
    "ForumRead": "On",
    "ForumWrite": "On"
  }
}'
```

### GET `/v1/groups/{groupId}/features/status`

Checks whether a group has ANY feature disabled (includes feature freezes and group lock).
Used to display a banner on Creator Hub/Studio to inform group members that some features may not be available.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.HasGroupFeaturesBlockedResponse`
- `400`: 1: Group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 23: Insufficient permissions to complete the request. 49: User is invalid or does not exist

**Response fields** (`Roblox.Groups.Api.HasGroupFeaturesBlockedResponse`)

See [Roblox.Groups.Api.HasGroupFeaturesBlockedResponse](#roblox-groups-api-hasgroupfeaturesblockedresponse) in Models.

**Response example:**
```json
{
  "hasFeaturesBlocked": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/features/status"
```

### GET `/v1/groups/{groupId}/join-requests`

Gets a page of Group Join Requests for a group.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.GroupJoinRequestResponse_`
- `400`: 1: The group is invalid or does not exist. 36: The pagination cursor is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 19: You have insufficient permissions for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.GroupJoinRequestResponse_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.GroupJoinRequestResponse_](#roblox-web-webapi-models-apipageresponse-roblox-groups-api-groupjoinrequestresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "requester": "...",
      "created": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/join-requests"
```

### POST `/v1/groups/{groupId}/join-requests`

Batch accepts group join requests

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: The group is invalid or does not exist. 3: The user is invalid or does not exist. 20: The group join request is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 6: You are already in the maximum number of groups. 19: You have insufficient permissions for this request.
- `500`: 0: Something went wrong.
- `503`: 18: The operation is temporarily unavailable. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/join-requests" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### DELETE `/v1/groups/{groupId}/join-requests`

Batch declines group join requests

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: The group is invalid or does not exist. 3: The user is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/join-requests" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### GET `/v1/groups/{groupId}/join-requests/users/{userId}`

Gets a group join request by userId.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |
| `userId` | path | `integer` | Yes | The user Id. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupJoinRequestResponse`
- `400`: 1: The group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 19: You have insufficient permissions for this request.

**Response fields** (`Roblox.Groups.Api.GroupJoinRequestResponse`)

See [Roblox.Groups.Api.GroupJoinRequestResponse](#roblox-groups-api-groupjoinrequestresponse) in Models.

**Response example:**
```json
{
  "requester": {
    "buildersClubMembershipType": 0,
    "hasVerifiedBadge": false,
    "userId": 0,
    "username": "string",
    "displayName": "string"
  },
  "created": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/join-requests/users/{USERID}"
```

### POST `/v1/groups/{groupId}/join-requests/users/{userId}`

Accepts a group join request.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |
| `userId` | path | `integer` | Yes | The user Id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: The group is invalid or does not exist. 3: The user is invalid or does not exist. 20: The group join request is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 6: You are already in the maximum number of groups. 19: You have insufficient permissions for this request.
- `503`: 18: The operation is temporarily unavailable. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/join-requests/users/{USERID}"
```

### DELETE `/v1/groups/{groupId}/join-requests/users/{userId}`

Declines/cancels a group join request.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |
| `userId` | path | `integer` | Yes | The user Id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: The group is invalid or does not exist. 3: The user is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 4: You do not have permission to manage this member.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/join-requests/users/{USERID}"
```

### GET `/v1/groups/{groupId}/membership`

Gets group membership information in the context of the authenticated user

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |
| `includeNotificationPreferences` | query | `boolean` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupMembershipMetadataResponse`
- `400`: 1: The group is invalid or does not exist.

**Response fields** (`Roblox.Groups.Api.GroupMembershipMetadataResponse`)

See [Roblox.Groups.Api.GroupMembershipMetadataResponse](#roblox-groups-api-groupmembershipmetadataresponse) in Models.

**Response example:**
```json
{
  "groupId": 0,
  "isPrimary": false,
  "isPendingJoin": false,
  "userRole": {
    "user": {
      "buildersClubMembershipType": "...",
      "hasVerifiedBadge": "...",
      "userId": "...",
      "username": "...",
      "displayName": "..."
    },
    "role": {
      "id": "...",
      "name": "...",
      "description": "...",
      "rank": "...",
      "memberCount": "...",
      "isBase": "..."
    }
  },
  "permissions": {
    "groupPostsPermissions": {
      "viewStatus": "...",
      "postToStatus": "..."
    },
    "groupForumsPermissions": {
      "viewForums": "...",
      "manageCategories": "...",
      "createPosts": "...",
      "removePosts": "...",
      "lockPosts": "...",
      "pinPosts": "..."
    },
    "groupContentModerationPermissions": {
      "manageKeywordBlockList": "...",
      "viewKeywordBlockList": "..."
    },
    "groupMembershipPermissions": {
      "changeRank": "...",
      "inviteMembers": "...",
      "removeMembers": "...",
      "banMembers": "..."
    },
    "groupManagementPermissions": {
      "manageRelationships": "...",
      "manageClan": "...",
      "viewAuditLogs": "...",
      "bypassSlowmode": "...",
      "viewCommunityAnalytics": "..."
    },
    "groupEconomyPermissions": {
      "spendGroupFunds": "...",
      "advertiseGroup": "...",
      "createItems": "...",
      "manageItems": "...",
      "addGroupPlaces": "...",
      "manageGroupGames": "..."
    }
  },
  "channelPermissions": [
    {
      "channelId": "...",
      "groupForumsPermissions": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/membership?includeNotificationPreferences={VALUE}"
```

### PATCH `/v1/groups/{groupId}/name`

Updates the group's name.

This endpoint will charge Robux for the group rename.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The id of the group the user is in. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.UpdateGroupNameRequest`

See [Roblox.Groups.Api.UpdateGroupNameRequest](#roblox-groups-api-updategroupnamerequest) in Models.

**Request example:**
```json
{
  "name": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Groups.Api.UpdateGroupNameResponse`
- `400`: 1: Group is invalid or does not exist. 13: The name is invalid. 19: The name is too long. 20: The name has been taken.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 12: Insufficient Robux funds. 14: The name is moderated. 23: Insufficient permissions to complete the request. 38: Your account must be verified in order to change your group's name. 39: The group ownership was changed too recently.
- `409`: 36: The name was changed too recently. 37: The name was in use too recently.
- `413`: 0: Unknown error.
- `429`: 17: Too many requests.

**Response fields** (`Roblox.Groups.Api.UpdateGroupNameResponse`)

See [Roblox.Groups.Api.UpdateGroupNameResponse](#roblox-groups-api-updategroupnameresponse) in Models.

**Response example:**
```json
{
  "newName": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/name" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string"
}'
```

### GET `/v1/groups/{groupId}/name-history`

Gets the Group's name change history.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The id of the group. |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.Models.Response.GroupNameHistoryResponseItem_`
- `400`: 1: Group is invalid or does not exist.
- `403`: 23: Insufficient permissions to complete the request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.Models.Response.GroupNameHistoryResponseItem_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.Models.Response.GroupNameHistoryResponseItem_](#roblox-web-webapi-models-apipageresponse-roblox-groups-api-models-response-groupnamehistoryresponseitem-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "name": "...",
      "created": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/name-history"
```

### PATCH `/v1/groups/{groupId}/notification-preference`

Updates the group's settings

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The id of the group the user is in. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.UpdateGroupNotificationPreferenceRequest`

See [Roblox.Groups.Api.UpdateGroupNotificationPreferenceRequest](#roblox-groups-api-updategroupnotificationpreferencerequest) in Models.

**Request example:**
```json
{
  "notificationsEnabled": false,
  "type": 0
}
```

**Responses:**

- `200`: OK → `0 \| 1 \| 2 \| 3`
- `400`: 1: Group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/notification-preference" \
  -H "Content-Type: application/json" \
  -d '{
  "notificationsEnabled": false,
  "type": 0
}'
```

### GET `/v1/groups/{groupId}/payout-restriction`

Gets a value indicating whether the group can use payout feature

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupPayoutRestrictionResponse`
- `400`: 1: Group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 9: You don't have permission to view this group's payouts.

**Response fields** (`Roblox.Groups.Api.GroupPayoutRestrictionResponse`)

See [Roblox.Groups.Api.GroupPayoutRestrictionResponse](#roblox-groups-api-grouppayoutrestrictionresponse) in Models.

**Response example:**
```json
{
  "canUseRecurringPayout": false,
  "canUseOneTimePayout": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/payout-restriction"
```

### GET `/v1/groups/{groupId}/payouts`

Gets a list of the group payout percentages

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupPayoutResponse_`
- `400`: 1: Group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 9: You don't have permission to view this group's payouts.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupPayoutResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupPayoutResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-groups-api-grouppayoutresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "user": "...",
      "percentage": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/payouts"
```

### POST `/v1/groups/{groupId}/payouts`

Pays out a user in Robux.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.OneTimePayoutResponse`
- `400`: 1: Group is invalid or does not exist. 12: Insufficient Robux funds. 24: Invalid payout type. 25: The amount is invalid. 26: Too many recipients.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 23: Insufficient permissions to complete the request. 28: Group has paid out too recently. Please wait and try again. 35: 2-Step Verification is required to make further transactions. Go to Settings > Security to complete 2-Step Verification. 52: Group has paid out to this recipient too many times recently. Please try again later.
- `503`: 22: The feature is disabled.

**Response fields** (`Roblox.Groups.Api.OneTimePayoutResponse`)

See [Roblox.Groups.Api.OneTimePayoutResponse](#roblox-groups-api-onetimepayoutresponse) in Models.

**Response example:**
```json
{
  "status": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/payouts" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### GET `/v1/groups/{groupId}/payouts/latest` [BETA]

Gets the latest one-time payout for each requested user.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |
| `userIds` | query | `string[]` | No |  |

**Responses:**

- `200`: Success → `PublicAllOneTimePayoutsResponseModel`
- `400`: Bad Request → `OrganizationsServiceApi.ErrorResponse`
- `401`: Unauthorized → `OrganizationsServiceApi.ErrorResponse`
- `403`: Forbidden → `OrganizationsServiceApi.ErrorResponse`

**Response fields** (`PublicAllOneTimePayoutsResponseModel`)

See [PublicAllOneTimePayoutsResponseModel](#publicallonetimepayoutsresponsemodel) in Models.

**Response example:**
```json
{
  "payouts": [
    {
      "recipientUserId": "...",
      "status": "...",
      "oneTimePayout": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/payouts/latest"
```

### POST `/v1/groups/{groupId}/payouts/recurring`

Updates recurring payouts.

This endpoint will remove any recipients not sent in the request.
If a recipient in the request is not a valid member in the group they will not be added to the recurring payouts.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Group is invalid or does not exist. 24: Invalid payout type. 25: The amount is invalid. 26: Too many recipients. 27: The recipients are invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 12: Insufficient Robux funds. 28: Group has paid out too recently. Please wait and try again. 35: 2-Step Verification is required to make further transactions. Go to Settings > Security to complete 2-Step Verification.
- `503`: 22: The feature is disabled.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/payouts/recurring" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### GET `/v1/groups/{groupId}/payouts/suggested` [BETA]

Gets suggested one-time payouts for eligible collaborators.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |

**Responses:**

- `200`: Success → `PublicAllOneTimePayoutsResponseModel`
- `401`: Unauthorized → `OrganizationsServiceApi.ErrorResponse`
- `403`: Forbidden → `OrganizationsServiceApi.ErrorResponse`

**Response fields** (`PublicAllOneTimePayoutsResponseModel`)

See [PublicAllOneTimePayoutsResponseModel](#publicallonetimepayoutsresponsemodel) in Models.

**Response example:**
```json
{
  "payouts": [
    {
      "recipientUserId": "...",
      "status": "...",
      "oneTimePayout": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/payouts/suggested"
```

### GET `/v1/groups/{groupId}/payouts/universes` [BETA]

Gets payout-visible universes for a group.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |
| `limit` | query | `integer` | No |  |
| `cursor` | query | `string` | No |  |

**Responses:**

- `200`: Success → `PublicGroupUniversePayoutPageResponseModel`
- `400`: Bad Request → `OrganizationsServiceApi.ErrorResponse`
- `401`: Unauthorized → `OrganizationsServiceApi.ErrorResponse`
- `403`: Forbidden → `OrganizationsServiceApi.ErrorResponse`

**Response fields** (`PublicGroupUniversePayoutPageResponseModel`)

See [PublicGroupUniversePayoutPageResponseModel](#publicgroupuniversepayoutpageresponsemodel) in Models.

**Response example:**
```json
{
  "data": [
    {
      "universeId": "...",
      "percentage": "..."
    }
  ],
  "nextPageCursor": "string",
  "previousPageCursor": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/payouts/universes"
```

### GET `/v1/groups/{groupId}/relationships/{groupRelationshipType}`

Gets a group's relationships

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |
| `groupRelationshipType` | path | `string` | Yes | The group relationship type, enemies or allies. |
| `StartRowIndex` | query | `integer` | Yes | The start index of the page request |
| `MaxRows` | query | `integer` | Yes | The maximum number of rows for the page request, should be at least 1. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupRelationshipsResponse`
- `400`: 1: Group is invalid or does not exist. 4: Group relationship type or request type is invalid. 8: Invalid or missing pagination parameters

**Response fields** (`Roblox.Groups.Api.GroupRelationshipsResponse`)

See [Roblox.Groups.Api.GroupRelationshipsResponse](#roblox-groups-api-grouprelationshipsresponse) in Models.

**Response example:**
```json
{
  "groupId": 0,
  "relationshipType": 1,
  "totalGroupCount": 0,
  "relatedGroups": [
    {
      "id": "...",
      "name": "...",
      "description": "...",
      "owner": "...",
      "shout": "...",
      "memberCount": "..."
    }
  ],
  "nextRowIndex": 0
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}?StartRowIndex={VALUE}&MaxRows={VALUE}"
```

### GET `/v1/groups/{groupId}/relationships/{groupRelationshipType}/requests`

Gets a group's relationship requests

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |
| `groupRelationshipType` | path | `string` | Yes | The group relationship type of the request, only allies are supported. |
| `StartRowIndex` | query | `integer` | Yes | The start index of the page request |
| `MaxRows` | query | `integer` | Yes | The maximum number of rows for the page request, should be at least 1. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupRelationshipsResponse`
- `400`: 1: Group is invalid or does not exist. 4: Group relationship type or request type is invalid. 8: Invalid or missing pagination parameters
- `401`: 0: Authorization has been denied for this request.
- `403`: 5: You don't have permission to manage this group's relationships.

**Response fields** (`Roblox.Groups.Api.GroupRelationshipsResponse`)

See [Roblox.Groups.Api.GroupRelationshipsResponse](#roblox-groups-api-grouprelationshipsresponse) in Models.

**Response example:**
```json
{
  "groupId": 0,
  "relationshipType": 1,
  "totalGroupCount": 0,
  "relatedGroups": [
    {
      "id": "...",
      "name": "...",
      "description": "...",
      "owner": "...",
      "shout": "...",
      "memberCount": "..."
    }
  ],
  "nextRowIndex": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}/requests?StartRowIndex={VALUE}&MaxRows={VALUE}"
```

### POST `/v1/groups/{groupId}/relationships/{groupRelationshipType}/requests`

Create a group relationship.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |
| `groupRelationshipType` | path | `string` | Yes | The group relationship type, enemies or allies. |
| `relatedGroupId` | path | `integer` | Yes | The id of the group you want to create a relationship with. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Group relationship type or request type is invalid. 2: Invalid group. 3: Target group is invalid or does not exist. 4: Your group cannot establish a relationship with itself.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 5: Your group does not allow enemy declarations. 6: Other group does not allow enemy declarations. 7: Your group already has a relationship with the target group. 8: You are blocked from communicating with this user. 9: Insufficient permissions.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}/requests"
```

### DELETE `/v1/groups/{groupId}/relationships/{groupRelationshipType}/requests`

Deletes a group relationship.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |
| `groupRelationshipType` | path | `string` | Yes | The group relationship type, enemies or allies. |
| `relatedGroupId` | path | `integer` | Yes | The id of the group you want to delete the relationship with. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 2: Invalid group. 3: Target group is invalid or does not exist. 11: Relationship does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 8: You are blocked from communicating with this user.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}/requests"
```

### POST `/v1/groups/{groupId}/relationships/{groupRelationshipType}/requests/{relatedGroupId}`

Accepts a group relationship request.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |
| `groupRelationshipType` | path | `string` | Yes | The group relationship type, enemies or allies, only allies are supported. |
| `relatedGroupId` | path | `integer` | Yes | The id of the group you want to accept the relationship request with. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Group relationship type or request type is invalid. 2: Invalid group. 3: Target group is invalid or does not exist. 10: Relationship request does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 9: Insufficient permissions.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}/requests/{RELATEDGROUPID}"
```

### DELETE `/v1/groups/{groupId}/relationships/{groupRelationshipType}/requests/{relatedGroupId}`

Declines a group relationship request.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |
| `groupRelationshipType` | path | `string` | Yes | The group relationship type, enemies or allies. |
| `relatedGroupId` | path | `integer` | Yes | The id of the group you want to accept the relationship request with. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Group relationship type or request type is invalid. 2: Invalid group. 3: Target group is invalid or does not exist. 10: Relationship request does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 9: Insufficient permissions.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}/requests/{RELATEDGROUPID}"
```

### POST `/v1/groups/{groupId}/relationships/{groupRelationshipType}/{relatedGroupId}`

Create a group relationship.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |
| `groupRelationshipType` | path | `string` | Yes | The group relationship type, enemies or allies. |
| `relatedGroupId` | path | `integer` | Yes | The id of the group you want to create a relationship with. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Group relationship type or request type is invalid. 2: Invalid group. 3: Target group is invalid or does not exist. 4: Your group cannot establish a relationship with itself.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 5: Your group does not allow enemy declarations. 6: Other group does not allow enemy declarations. 7: Your group already has a relationship with the target group. 8: You are blocked from communicating with this user. 9: Insufficient permissions.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}/{RELATEDGROUPID}"
```

### DELETE `/v1/groups/{groupId}/relationships/{groupRelationshipType}/{relatedGroupId}`

Deletes a group relationship.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |
| `groupRelationshipType` | path | `string` | Yes | The group relationship type, enemies or allies. |
| `relatedGroupId` | path | `integer` | Yes | The id of the group you want to delete the relationship with. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 2: Invalid group. 3: Target group is invalid or does not exist. 11: Relationship does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 8: You are blocked from communicating with this user.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}/{RELATEDGROUPID}"
```

### GET `/v1/groups/{groupId}/revenue/summary/{timeFrame}`

**Server:** `https://economy.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |
| `timeFrame` | path | `any` | Yes |  |

**Responses:**

- `200`: OK → `RevenueSummaryResponse`

**Response fields** (`RevenueSummaryResponse`)

See [RevenueSummaryResponse](#revenuesummaryresponse) in Models.

**Response example:**
```json
{
  "recurringRobuxStipend": 0,
  "itemSaleRobux": 0,
  "purchasedRobux": 0,
  "tradeSystemRobux": 0,
  "pendingRobux": 0,
  "groupPayoutRobux": 0
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://economy.roblox.com/v1/groups/{GROUPID}/revenue/summary/{TIMEFRAME}"
```

### GET `/v1/groups/{groupId}/roles`

Gets a list of the rolesets in a group.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |
| `includePrivate` | query | `boolean` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupAllRolesResponse`
- `400`: 1: The group is invalid or does not exist.

**Response fields** (`Roblox.Groups.Api.GroupAllRolesResponse`)

See [Roblox.Groups.Api.GroupAllRolesResponse](#roblox-groups-api-groupallrolesresponse) in Models.

**Response example:**
```json
{
  "groupId": 0,
  "roles": [
    {
      "id": "...",
      "name": "...",
      "description": "...",
      "rank": "...",
      "memberCount": "...",
      "isBase": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/roles?includePrivate={VALUE}"
```

### GET `/v1/groups/{groupId}/roles/guest/permissions`

Gets the permissions for a group's guest roleset. These can be viewed by all (members and guests) users.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupPermissionsResponse`
- `400`: 1: Group is invalid or does not exist.

**Response fields** (`Roblox.Groups.Api.GroupPermissionsResponse`)

See [Roblox.Groups.Api.GroupPermissionsResponse](#roblox-groups-api-grouppermissionsresponse) in Models.

**Response example:**
```json
{
  "groupId": 0,
  "role": {
    "id": 0,
    "name": "string",
    "description": "string",
    "rank": 0,
    "memberCount": 0,
    "isBase": false
  },
  "permissions": {
    "groupPostsPermissions": {
      "viewStatus": "...",
      "postToStatus": "..."
    },
    "groupForumsPermissions": {
      "viewForums": "...",
      "manageCategories": "...",
      "createPosts": "...",
      "removePosts": "...",
      "lockPosts": "...",
      "pinPosts": "..."
    },
    "groupContentModerationPermissions": {
      "manageKeywordBlockList": "...",
      "viewKeywordBlockList": "..."
    },
    "groupMembershipPermissions": {
      "changeRank": "...",
      "inviteMembers": "...",
      "removeMembers": "...",
      "banMembers": "..."
    },
    "groupManagementPermissions": {
      "manageRelationships": "...",
      "manageClan": "...",
      "viewAuditLogs": "...",
      "bypassSlowmode": "...",
      "viewCommunityAnalytics": "..."
    },
    "groupEconomyPermissions": {
      "spendGroupFunds": "...",
      "advertiseGroup": "...",
      "createItems": "...",
      "manageItems": "...",
      "addGroupPlaces": "...",
      "manageGroupGames": "..."
    }
  }
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/roles/guest/permissions"
```

### GET `/v1/groups/{groupId}/roles/permissions`

Gets all permissions for each role

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupPermissionsResponse_`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupPermissionsResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupPermissionsResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-groups-api-grouppermissionsresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "groupId": "...",
      "role": "...",
      "permissions": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/roles/permissions"
```

### GET `/v1/groups/{groupId}/roles/{roleSetId}/permissions`

Gets the permissions for a group's roleset. The authorized user must either be the group owner or the roleset being requested, except for guest roles, which can be viewed by all (members and guests).

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |
| `roleSetId` | path | `integer` | Yes | The group's role set id. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupPermissionsResponse`
- `400`: 1: Group is invalid or does not exist. 2: The roleset is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 3: You are not authorized to view/edit permissions for this role.

**Response fields** (`Roblox.Groups.Api.GroupPermissionsResponse`)

See [Roblox.Groups.Api.GroupPermissionsResponse](#roblox-groups-api-grouppermissionsresponse) in Models.

**Response example:**
```json
{
  "groupId": 0,
  "role": {
    "id": 0,
    "name": "string",
    "description": "string",
    "rank": 0,
    "memberCount": 0,
    "isBase": false
  },
  "permissions": {
    "groupPostsPermissions": {
      "viewStatus": "...",
      "postToStatus": "..."
    },
    "groupForumsPermissions": {
      "viewForums": "...",
      "manageCategories": "...",
      "createPosts": "...",
      "removePosts": "...",
      "lockPosts": "...",
      "pinPosts": "..."
    },
    "groupContentModerationPermissions": {
      "manageKeywordBlockList": "...",
      "viewKeywordBlockList": "..."
    },
    "groupMembershipPermissions": {
      "changeRank": "...",
      "inviteMembers": "...",
      "removeMembers": "...",
      "banMembers": "..."
    },
    "groupManagementPermissions": {
      "manageRelationships": "...",
      "manageClan": "...",
      "viewAuditLogs": "...",
      "bypassSlowmode": "...",
      "viewCommunityAnalytics": "..."
    },
    "groupEconomyPermissions": {
      "spendGroupFunds": "...",
      "advertiseGroup": "...",
      "createItems": "...",
      "manageItems": "...",
      "addGroupPlaces": "...",
      "manageGroupGames": "..."
    }
  }
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/roles/{ROLESETID}/permissions"
```

### PATCH `/v1/groups/{groupId}/roles/{roleSetId}/permissions`

Updates the permissions for a group's roleset. The authorized user must be the group owner.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group's id. |
| `roleSetId` | path | `integer` | Yes | The roleset's id. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.UpdatePermissionsRequest`

See [Roblox.Groups.Api.UpdatePermissionsRequest](#roblox-groups-api-updatepermissionsrequest) in Models.

**Request example:**
```json
{
  "permissions": {
    "InviteMembers": false,
    "PostToStatus": false,
    "RemoveMembers": false,
    "BanMembers": false,
    "ViewStatus": false,
    "ChangeRank": false
  }
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Group is invalid or does not exist. 2: The roleset is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 3: You are not authorized to view/edit permissions for this role. 4: This role's permissions can not be modified.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/roles/{ROLESETID}/permissions" \
  -H "Content-Type: application/json" \
  -d '{
  "permissions": {
    "InviteMembers": false,
    "PostToStatus": false,
    "RemoveMembers": false,
    "BanMembers": false,
    "ViewStatus": false,
    "ChangeRank": false
  }
}'
```

### GET `/v1/groups/{groupId}/roles/{roleSetId}/users`

Gets a list of users in a group for a specific roleset.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |
| `roleSetId` | path | `integer` | Yes | The group's role set id. |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.Models.Response.UserModel_`
- `400`: 1: The group is invalid or does not exist. 36: The pagination cursor is invalid.
- `403`: 2: The roleset is invalid or does not exist. 35: You do not have permission to view this group's member list.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.Models.Response.UserModel_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.Models.Response.UserModel_](#roblox-web-webapi-models-apipageresponse-roblox-groups-api-models-response-usermodel-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "buildersClubMembershipType": "...",
      "hasVerifiedBadge": "...",
      "userId": "...",
      "username": "...",
      "displayName": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/roles/{ROLESETID}/users"
```

### POST `/v1/groups/{groupId}/rolesets/create`

Creates new group roleset.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.Models.Request.CreateRoleSetRequest`

See [Roblox.Groups.Api.Models.Request.CreateRoleSetRequest](#roblox-groups-api-models-request-createrolesetrequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "description": "string",
  "rank": 0,
  "usingGroupFunds": false,
  "isPrivate": false
}
```

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupRoleResponse`
- `400`: 0: Something went wrong. 3: You do not have enough funds to purchase this role. 5: Role name already exists. 6: Rank value is out of bounds. 7: The role name is too long. 8: The role description is too long. 10: This group does not exist. 11: Failed to process payment to purchase role. 12: Limit for roles have been reached on this group. 14: Role name can not be empty. 15: This role does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 9: You do not have permissions to perform this action.

**Response fields** (`Roblox.Groups.Api.GroupRoleResponse`)

See [Roblox.Groups.Api.GroupRoleResponse](#roblox-groups-api-grouproleresponse) in Models.

**Response example:**
```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "rank": 0,
  "memberCount": 0,
  "isBase": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/rolesets/create" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string",
  "rank": 0,
  "usingGroupFunds": false,
  "isPrivate": false
}'
```

### PATCH `/v1/groups/{groupId}/rolesets/{rolesetId}`

Updates existing group roleset.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |
| `rolesetId` | path | `integer` | Yes | The roleset Id. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.Models.Request.UpdateRoleSetRequest`

See [Roblox.Groups.Api.Models.Request.UpdateRoleSetRequest](#roblox-groups-api-models-request-updaterolesetrequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "description": "string",
  "rank": 0,
  "color": 0,
  "isPrivate": false
}
```

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupRoleResponse`
- `400`: 5: Role name already exists. 6: Rank value is out of bounds. 7: The role name is too long. 8: The role description is too long. 10: This group does not exist. 14: Role name can not be empty. 15: This role does not exist. 19: Cannot update Guest role. 20: Cannot update Owner role rank. 30: Invalid role color.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 9: You do not have permissions to perform this action.

**Response fields** (`Roblox.Groups.Api.GroupRoleResponse`)

See [Roblox.Groups.Api.GroupRoleResponse](#roblox-groups-api-grouproleresponse) in Models.

**Response example:**
```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "rank": 0,
  "memberCount": 0,
  "isBase": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/rolesets/{ROLESETID}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string",
  "rank": 0,
  "color": 0,
  "isPrivate": false
}'
```

### DELETE `/v1/groups/{groupId}/rolesets/{rolesetId}`

Deletes existing group roleset.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |
| `rolesetId` | path | `integer` | Yes | The roleset Id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 10: This group does not exist. 15: This role does not exist. 17: Cannot remove any more roles 18: Cannot delete this role.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 9: You do not have permissions to perform this action. 16: There are users in this role.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/rolesets/{ROLESETID}"
```

### GET `/v1/groups/{groupId}/settings`

Gets the Group's settings

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The id of the group the user is in. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupSettingsResponse`
- `400`: 1: Group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 23: Insufficient permissions to complete the request.

**Response fields** (`Roblox.Groups.Api.GroupSettingsResponse`)

See [Roblox.Groups.Api.GroupSettingsResponse](#roblox-groups-api-groupsettingsresponse) in Models.

**Response example:**
```json
{
  "isApprovalRequired": false,
  "isBuildersClubRequired": false,
  "areEnemiesAllowed": false,
  "areGroupFundsVisible": false,
  "areGroupGamesVisible": false,
  "isGroupNameChangeEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/settings"
```

### PATCH `/v1/groups/{groupId}/settings`

Updates the group's settings

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The id of the group the user is in. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.UpdateGroupSettingsRequest`

See [Roblox.Groups.Api.UpdateGroupSettingsRequest](#roblox-groups-api-updategroupsettingsrequest) in Models.

**Request example:**
```json
{
  "isApprovalRequired": false,
  "areEnemiesAllowed": false,
  "areGroupFundsVisible": false,
  "areGroupGamesVisible": false,
  "verificationLevel": 0,
  "accountTenureRequirement": 0
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 23: Insufficient permissions to complete the request.
- `503`: 31: Service is currently unavailable.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/settings" \
  -H "Content-Type: application/json" \
  -d '{
  "isApprovalRequired": false,
  "areEnemiesAllowed": false,
  "areGroupFundsVisible": false,
  "areGroupGamesVisible": false,
  "verificationLevel": 0,
  "accountTenureRequirement": 0
}'
```

### GET `/v1/groups/{groupId}/social-links`

Get social link data associated with a group

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The Id of the game |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GetSocialLinkResponse`
- `400`: 1: Group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 13: Only users who are over thirteen years of age may edit social links.
- `404`: 11: Social links cannot be processed as this time.

**Response fields** (`Roblox.Groups.Api.GetSocialLinkResponse`)

See [Roblox.Groups.Api.GetSocialLinkResponse](#roblox-groups-api-getsociallinkresponse) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "type": "...",
      "url": "...",
      "title": "..."
    }
  ],
  "socialLinksVerificationStatus": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/social-links"
```

### POST `/v1/groups/{groupId}/social-links`

Posts a social links

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The id of the group |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.SocialLinkRequest`

See [Roblox.Groups.Api.SocialLinkRequest](#roblox-groups-api-sociallinkrequest) in Models.

**Request example:**
```json
{
  "type": 0,
  "url": "string",
  "title": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Groups.Api.SocialLinkResponse`
- `400`: 3: The social link title is too long. 4: The social link title cannot be empty. 5: The social link url cannot be empty. 7: The request was null. 9: The social link type is invalid. 12: The social link title was moderated.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You do not have permission to configure this social link.
- `404`: 8: The requested group or social link was not found.
- `503`: 11: Social links cannot be processed as this time.

**Response fields** (`Roblox.Groups.Api.SocialLinkResponse`)

See [Roblox.Groups.Api.SocialLinkResponse](#roblox-groups-api-sociallinkresponse) in Models.

**Response example:**
```json
{
  "id": 0,
  "type": 0,
  "url": "string",
  "title": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/social-links" \
  -H "Content-Type: application/json" \
  -d '{
  "type": 0,
  "url": "string",
  "title": "string"
}'
```

### PATCH `/v1/groups/{groupId}/social-links/{socialLinkId}`

Updates a social link

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The id of the universe |
| `socialLinkId` | path | `integer` | Yes | The id of the social link being updated |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.SocialLinkRequest`

See [Roblox.Groups.Api.SocialLinkRequest](#roblox-groups-api-sociallinkrequest) in Models.

**Request example:**
```json
{
  "type": 0,
  "url": "string",
  "title": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Group is invalid or does not exist. 3: The social link title is too long. 4: The social link title cannot be empty. 5: The social link url cannot be empty. 6: The social link url was improperly formatted. 7: The request was null. 8: The requested group or social link was not found. 9: The social link type is invalid. 10: The social link is not for a group. 12: The social link title was moderated. 16: A social link with this type already exists on this group.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You do not have permission to configure this social link.
- `404`: 11: Social links cannot be processed as this time.
- `503`: 11: Social links cannot be processed as this time.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/social-links/{SOCIALLINKID}" \
  -H "Content-Type: application/json" \
  -d '{
  "type": 0,
  "url": "string",
  "title": "string"
}'
```

### DELETE `/v1/groups/{groupId}/social-links/{socialLinkId}`

Deletes a social link

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The id of the game you are editing, required for permissions checking |
| `socialLinkId` | path | `integer` | Yes | The id of the social link |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Group is invalid or does not exist. 10: The social link is not for a group. 15: The social link id doesn't match the group id.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You do not have permission to configure this social link. 13: Only users who are over thirteen years of age may edit social links.
- `404`: 11: Social links cannot be processed as this time.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/social-links/{SOCIALLINKID}"
```

### GET `/v1/groups/{groupId}/universes` [EXPERIMENTAL]

Gets a list of universes for the given group.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |
| `isArchived` | query | `boolean` | No | Whether or not to return archived games. |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | Sorted by universeId Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Api.Develop.Models.UniverseModel_`
- `400`: Invalid groupId.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Api.Develop.Models.UniverseModel_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Api.Develop.Models.UniverseModel_](#roblox-web-webapi-models-apipageresponse-roblox-api-develop-models-universemodel-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "name": "...",
      "description": "...",
      "isArchived": "...",
      "rootPlaceId": "...",
      "isActive": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/groups/{GROUPID}/universes"
```

### GET `/v1/groups/{groupId}/users`

Gets a list of users in a group.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.UserGroupRoleResponse_`
- `400`: 1: The group is invalid or does not exist. 36: The pagination cursor is invalid.
- `403`: 35: You do not have permission to view this group's member list.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.UserGroupRoleResponse_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.UserGroupRoleResponse_](#roblox-web-webapi-models-apipageresponse-roblox-groups-api-usergrouproleresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "user": "...",
      "role": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/users"
```

### POST `/v1/groups/{groupId}/users`

Joins a group

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |
| `Roblox-Place-Id` | header | `integer` | No | The place ID of the experience the player is in. |
| `Roblox-Game-Id` | header | `string` | No | The player's current game Id. |
| `Roblox-Session-Id` | header | `string` | No | The player's current session Id. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.JoinGroupRequest`

See [Roblox.Groups.Api.JoinGroupRequest](#roblox-groups-api-joingrouprequest) in Models.

**Request example:**
```json
{
  "sessionId": "string",
  "redemptionToken": "string",
  "captchaId": "string",
  "captchaToken": "string",
  "captchaProvider": "string",
  "challengeId": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: The group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 6: You are already in the maximum number of groups. 9: You do not have the builders club membership necessary to join this group. 14: You cannot join a closed group. 33: You do not have the required verification level to join this group. 34: You do not have the required account tenure to join this group.
- `409`: 7: You have already requested to join this group. 8: You are already a member of this group.
- `429`: 10: Too many attempts to join the group. Please try again later.
- `503`: 18: The operation is temporarily unavailable. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/users" \
  -H "Content-Type: application/json" \
  -d '{
  "sessionId": "string",
  "redemptionToken": "string",
  "captchaId": "string",
  "captchaToken": "string",
  "captchaProvider": "string",
  "challengeId": "string"
}'
```

### PATCH `/v1/groups/{groupId}/users/{userId}`

Updates a users role in a group.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The id of the group the user is in. |
| `userId` | path | `integer` | Yes | The id of the user being updated. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.UpdateUserRoleRequest`

See [Roblox.Groups.Api.UpdateUserRoleRequest](#roblox-groups-api-updateuserrolerequest) in Models.

**Request example:**
```json
{
  "roleId": 0
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: The group is invalid or does not exist. 2: The roleset is invalid or does not exist. 3: The user is invalid or does not exist. 23: You cannot change your own role. 26: You cannot change the user's role to the same role.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 4: You do not have permission to manage this member.
- `503`: 18: The operation is temporarily unavailable. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/users/{USERID}" \
  -H "Content-Type: application/json" \
  -d '{
  "roleId": 0
}'
```

### DELETE `/v1/groups/{groupId}/users/{userId}`

Removes a user from a group

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |
| `userId` | path | `integer` | Yes | The Id of the user being removed. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: The group is invalid or does not exist. 3: The user is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 4: You do not have permission to manage this member. 25: 2-Step Verification is required to make further transactions. Go to Settings > Security to complete 2-Step Verification.
- `503`: 18: The operation is temporarily unavailable. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/users/{USERID}"
```

### GET `/v1/groups/{groupId}/users/{userId}/permissions`

Gets the permissions a user has in a group. Only available to group owner and RCC

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group id. |
| `userId` | path | `integer` | Yes | The user id. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupPermissionsResponse`
- `400`: 1: Group is invalid or does not exist.
- `403`: 3: You are not authorized to view/edit permissions for this role.
- `404`: 3: The user is invalid or does not exist.

**Response fields** (`Roblox.Groups.Api.GroupPermissionsResponse`)

See [Roblox.Groups.Api.GroupPermissionsResponse](#roblox-groups-api-grouppermissionsresponse) in Models.

**Response example:**
```json
{
  "groupId": 0,
  "role": {
    "id": 0,
    "name": "string",
    "description": "string",
    "rank": 0,
    "memberCount": 0,
    "isBase": false
  },
  "permissions": {
    "groupPostsPermissions": {
      "viewStatus": "...",
      "postToStatus": "..."
    },
    "groupForumsPermissions": {
      "viewForums": "...",
      "manageCategories": "...",
      "createPosts": "...",
      "removePosts": "...",
      "lockPosts": "...",
      "pinPosts": "..."
    },
    "groupContentModerationPermissions": {
      "manageKeywordBlockList": "...",
      "viewKeywordBlockList": "..."
    },
    "groupMembershipPermissions": {
      "changeRank": "...",
      "inviteMembers": "...",
      "removeMembers": "...",
      "banMembers": "..."
    },
    "groupManagementPermissions": {
      "manageRelationships": "...",
      "manageClan": "...",
      "viewAuditLogs": "...",
      "bypassSlowmode": "...",
      "viewCommunityAnalytics": "..."
    },
    "groupEconomyPermissions": {
      "spendGroupFunds": "...",
      "advertiseGroup": "...",
      "createItems": "...",
      "manageItems": "...",
      "addGroupPlaces": "...",
      "manageGroupGames": "..."
    }
  }
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/users/{USERID}/permissions"
```

### GET `/v1/roles`

Gets the Roles by their ids.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `ids` | query | `integer[]` | Yes | A list of role ids |
| `includePrivate` | query | `boolean` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupRoleDetailResponse_`
- `400`: 1: Ids could not be parsed from request. 2: Too many ids in request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupRoleDetailResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupRoleDetailResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-groups-api-grouproledetailresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "groupId": "...",
      "id": "...",
      "name": "...",
      "description": "...",
      "rank": "...",
      "memberCount": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/roles?ids={VALUE}&includePrivate={VALUE}"
```

### GET `/v1/universes/{universeId}/payouts` [BETA]

Gets recurring payouts for a group-owned universe.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: Success → `PublicAllGroupUniversePayoutsResponseModel`
- `401`: Unauthorized → `OrganizationsServiceApi.ErrorResponse`
- `403`: Forbidden → `OrganizationsServiceApi.ErrorResponse`
- `404`: Not Found → `OrganizationsServiceApi.ErrorResponse`

**Response fields** (`PublicAllGroupUniversePayoutsResponseModel`)

See [PublicAllGroupUniversePayoutsResponseModel](#publicallgroupuniversepayoutsresponsemodel) in Models.

**Response example:**
```json
{
  "payouts": [
    {
      "userId": "...",
      "percentage": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/universes/{UNIVERSEID}/payouts"
```

### PATCH `/v1/universes/{universeId}/payouts`

Updates recurring payouts for a group-owned universe.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Request Body:** `application/json-patch+json` — Type: `PublicUpdateUniverseRecurringPayoutsRequestModel`

See [PublicUpdateUniverseRecurringPayoutsRequestModel](#publicupdateuniverserecurringpayoutsrequestmodel) in Models.

**Request example:**
```json
{
  "payouts": [
    {
      "userId": "...",
      "percentage": "..."
    }
  ]
}
```

**Responses:**

- `200`: Success → `PublicAllGroupUniversePayoutsResponseModel`
- `400`: Bad Request → `OrganizationsServiceApi.ErrorResponse`
- `401`: Unauthorized → `OrganizationsServiceApi.ErrorResponse`
- `403`: Forbidden → `OrganizationsServiceApi.ErrorResponse`
- `404`: Not Found → `OrganizationsServiceApi.ErrorResponse`

**Response fields** (`PublicAllGroupUniversePayoutsResponseModel`)

See [PublicAllGroupUniversePayoutsResponseModel](#publicallgroupuniversepayoutsresponsemodel) in Models.

**Response example:**
```json
{
  "payouts": [
    {
      "userId": "...",
      "percentage": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/universes/{UNIVERSEID}/payouts" \
  -H "Content-Type: application/json" \
  -d '{
  "payouts": [
    {
      "userId": "...",
      "percentage": "..."
    }
  ]
}'
```

### GET `/v1/user/groups/canmanage` [EXPERIMENTAL]

Gets a list of Groups that a user can manage.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.GroupModel_`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.GroupModel_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.GroupModel_](#roblox-web-webapi-models-apiarrayresponse-roblox-api-develop-models-groupmodel-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "name": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/user/groups/canmanage"
```

### GET `/v1/user/groups/pending`

Gets groups that the authenticated user has requested to join

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupDetailResponse_`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupDetailResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupDetailResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-groups-api-groupdetailresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "name": "...",
      "description": "...",
      "owner": "...",
      "shout": "...",
      "memberCount": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/user/groups/pending"
```

### POST `/v1/user/groups/primary`

Sets the authenticated user's primary group

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.PrimaryGroupRequest`

See [Roblox.Groups.Api.PrimaryGroupRequest](#roblox-groups-api-primarygrouprequest) in Models.

**Request example:**
```json
{
  "groupId": 0
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You aren't a member of the group specified.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/user/groups/primary" \
  -H "Content-Type: application/json" \
  -d '{
  "groupId": 0
}'
```

### DELETE `/v1/user/groups/primary`

Removes the authenticated user's primary group

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/user/groups/primary"
```

### GET `/v1/users/{userId}/groups/primary/role`

Gets a user's primary group.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user id. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupMembershipDetailResponse`
- `400`: 4: User is invalid or does not exist.

**Response fields** (`Roblox.Groups.Api.GroupMembershipDetailResponse`)

See [Roblox.Groups.Api.GroupMembershipDetailResponse](#roblox-groups-api-groupmembershipdetailresponse) in Models.

**Response example:**
```json
{
  "group": {
    "id": 0,
    "name": "string",
    "description": "string",
    "owner": {
      "buildersClubMembershipType": "...",
      "hasVerifiedBadge": "...",
      "userId": "...",
      "username": "...",
      "displayName": "..."
    },
    "shout": {
      "body": "...",
      "poster": "...",
      "created": "...",
      "updated": "..."
    },
    "memberCount": 0
  },
  "role": {
    "id": 0,
    "name": "string",
    "description": "string",
    "rank": 0,
    "memberCount": 0,
    "isBase": false
  },
  "isPrimaryGroup": false,
  "isNotificationsEnabled": false,
  "notificationPreferences": [
    {
      "type": "...",
      "enabled": "...",
      "name": "...",
      "description": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/users/{USERID}/groups/primary/role"
```

### GET `/v1/users/{userId}/groups/roles`

Gets a list of all group roles for groups the specified user is in.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user id. |
| `includeLocked` | query | `boolean` | No |  |
| `includeNotificationPreferences` | query | `boolean` | No |  |
| `discoveryType` | query | `0 \| 1 \| 2` | No | Valid values: `0`, `1`, `2` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupMembershipDetailResponse_`
- `400`: 3: The user is invalid or does not exist.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupMembershipDetailResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupMembershipDetailResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-groups-api-groupmembershipdetailresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "group": "...",
      "role": "...",
      "isPrimaryGroup": "...",
      "isNotificationsEnabled": "...",
      "notificationPreferences": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/users/{USERID}/groups/roles"
```

### PATCH `/v1/vip-servers/{id}/permissions`

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `id` | path | `integer` | Yes |  |

**Request Body:** `application/json` — Type: `any`

**Responses:**

- `200`: OK → `PrivateServerPermissionsResponse`

**Response fields** (`PrivateServerPermissionsResponse`)

See [PrivateServerPermissionsResponse](#privateserverpermissionsresponse) in Models.

**Response example:**
```json
{
  "clanAllowed": false,
  "enemyClanId": 0,
  "friendsAllowed": false,
  "users": [
    {
      "id": "...",
      "name": "...",
      "displayName": "..."
    }
  ]
}
```

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/vip-servers/{ID}/permissions" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### GET `/v2/groups`

Multi-get groups information by Ids.

If a group comes back as null, it will not be returned in the response.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupIds` | query | `integer[]` | Yes | The group Ids. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Web.Responses.Groups.GroupResponseV2_`
- `400`: 2: Too many ids in request. 3: Ids could not be parsed from request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Web.Responses.Groups.GroupResponseV2_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Web.Responses.Groups.GroupResponseV2_](#roblox-web-webapi-models-apiarrayresponse-roblox-web-responses-groups-groupresponsev2-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "name": "...",
      "description": "...",
      "owner": "...",
      "memberCount": "...",
      "created": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v2/groups?groupIds={VALUE}"
```

### GET `/v2/groups/{groupId}/games`

Gets experiences created by the specified group id.

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id |
| `accessFilter` | query | `1 \| 2 \| 4` | No | The access type of the experiences. Valid values: `1`, `2`, `4` |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.Models.Response.GroupExperienceResponse_`
- `501`: 47: Code path is not implemented.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.Models.Response.GroupExperienceResponse_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.Models.Response.GroupExperienceResponse_](#roblox-web-webapi-models-apipageresponse-roblox-groups-api-models-response-groupexperienceresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "name": "...",
      "description": "...",
      "creator": "...",
      "rootPlace": "...",
      "created": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v2/groups/{GROUPID}/games"
```

### GET `/v2/groups/{groupId}/gamesV2`

Gets experiences created by the specified group id.

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id |
| `accessFilter` | query | `1 \| 2 \| 4` | No | The access type of the experiences. Valid values: `1`, `2`, `4` |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.Models.Response.GroupExperienceResponse_`
- `501`: 47: Code path is not implemented.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.Models.Response.GroupExperienceResponse_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.Models.Response.GroupExperienceResponse_](#roblox-web-webapi-models-apipageresponse-roblox-groups-api-models-response-groupexperienceresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "name": "...",
      "description": "...",
      "creator": "...",
      "rootPlace": "...",
      "created": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v2/groups/{GROUPID}/gamesV2"
```

### GET `/v2/groups/{groupId}/invitations` [BETA]

List open invitations to a group

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |
| `Cursor` | query | `string` | No | Cursor returned by a previous page. Omit for the first page. |
| `Limit` | query | `integer` | No | Page size: 10, 25, 50, or 100. Defaults to 10. |
| `SortOrder` | query | `OrganizationsServiceApi.SortOrder` | No | Sort order. Only `Asc` is currently supported; defaults to `Asc`. |

**Responses:**

- `200`: Success → `GroupInvitationCursorPageResponse`
- `400`: Bad Request → `OrganizationsServiceApi.ErrorResponse`
- `401`: Unauthorized → `OrganizationsServiceApi.ErrorResponse`
- `403`: Forbidden → `OrganizationsServiceApi.ErrorResponse`
- `404`: Not Found → `OrganizationsServiceApi.ErrorResponse`
- `500`: Server Error → `OrganizationsServiceApi.ErrorResponse`

**Response fields** (`GroupInvitationCursorPageResponse`)

See [GroupInvitationCursorPageResponse](#groupinvitationcursorpageresponse) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "groupId": "...",
      "recipientUserId": "...",
      "senderUserId": "...",
      "status": "...",
      "roleIds": "..."
    }
  ],
  "nextPageCursor": "string",
  "previousPageCursor": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v2/groups/{GROUPID}/invitations"
```

### POST `/v2/groups/{groupId}/invitations` [BETA]

Invite a user to a group

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |
| `isSecure` | query | `boolean` | No |  |

**Request Body:** `application/json-patch+json` — Type: `CreateGroupInvitationRequestModel`

See [CreateGroupInvitationRequestModel](#creategroupinvitationrequestmodel) in Models.

**Request example:**
```json
{
  "recipientUserId": 0,
  "roleIds": [
    0
  ]
}
```

**Responses:**

- `200`: Success → `GroupInvitation`
- `400`: Bad Request → `OrganizationsServiceApi.ErrorResponse`
- `401`: Unauthorized → `OrganizationsServiceApi.ErrorResponse`
- `403`: Forbidden → `OrganizationsServiceApi.ErrorResponse`
- `404`: Not Found → `OrganizationsServiceApi.ErrorResponse`
- `429`: Too Many Requests → `OrganizationsServiceApi.ErrorResponse`
- `500`: Server Error → `OrganizationsServiceApi.ErrorResponse`

**Response fields** (`GroupInvitation`)

See [GroupInvitation](#groupinvitation) in Models.

**Response example:**
```json
{
  "id": "string",
  "groupId": 0,
  "recipientUserId": 0,
  "senderUserId": 0,
  "status": "Open",
  "roleIds": [
    0
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v2/groups/{GROUPID}/invitations" \
  -H "Content-Type: application/json" \
  -d '{
  "recipientUserId": 0,
  "roleIds": [
    0
  ]
}'
```

### GET `/v2/groups/{groupId}/invitations/{invitationId}` [BETA]

Get an invitation to a group

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |
| `invitationId` | path | `integer` | Yes |  |

**Responses:**

- `200`: Success → `GroupInvitation`
- `401`: Unauthorized → `OrganizationsServiceApi.ErrorResponse`
- `403`: Forbidden → `OrganizationsServiceApi.ErrorResponse`
- `404`: Not Found → `OrganizationsServiceApi.ErrorResponse`
- `500`: Server Error → `OrganizationsServiceApi.ErrorResponse`

**Response fields** (`GroupInvitation`)

See [GroupInvitation](#groupinvitation) in Models.

**Response example:**
```json
{
  "id": "string",
  "groupId": 0,
  "recipientUserId": 0,
  "senderUserId": 0,
  "status": "Open",
  "roleIds": [
    0
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v2/groups/{GROUPID}/invitations/{INVITATIONID}"
```

### PATCH `/v2/groups/{groupId}/invitations/{invitationId}` [BETA]

Accept or decline an invitation to a group (recipient)

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |
| `invitationId` | path | `integer` | Yes |  |

**Request Body:** `application/json-patch+json` — Type: `UpdateGroupInvitationRequestModel`

See [UpdateGroupInvitationRequestModel](#updategroupinvitationrequestmodel) in Models.

**Request example:**
```json
{
  "status": "Open"
}
```

**Responses:**

- `200`: Success → `SuccessResponse`
- `400`: Bad Request → `OrganizationsServiceApi.ErrorResponse`
- `401`: Unauthorized → `OrganizationsServiceApi.ErrorResponse`
- `403`: Forbidden → `OrganizationsServiceApi.ErrorResponse`
- `404`: Not Found → `OrganizationsServiceApi.ErrorResponse`
- `500`: Server Error → `OrganizationsServiceApi.ErrorResponse`

**Response fields** (`SuccessResponse`)

See [SuccessResponse](#successresponse) in Models.

**Response example:**
```json
{
  "success": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v2/groups/{GROUPID}/invitations/{INVITATIONID}" \
  -H "Content-Type: application/json" \
  -d '{
  "status": "Open"
}'
```

### DELETE `/v2/groups/{groupId}/invitations/{invitationId}` [BETA]

Revoke an invitation to a group (member manager)

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |
| `invitationId` | path | `integer` | Yes |  |

**Responses:**

- `200`: Success → `SuccessResponse`
- `401`: Unauthorized → `OrganizationsServiceApi.ErrorResponse`
- `403`: Forbidden → `OrganizationsServiceApi.ErrorResponse`
- `404`: Not Found → `OrganizationsServiceApi.ErrorResponse`
- `500`: Server Error → `OrganizationsServiceApi.ErrorResponse`

**Response fields** (`SuccessResponse`)

See [SuccessResponse](#successresponse) in Models.

**Response example:**
```json
{
  "success": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v2/groups/{GROUPID}/invitations/{INVITATIONID}"
```

### GET `/v2/groups/{groupId}/roles/{roleId}/invitations` [BETA]

List open invitations to a group that grant a role

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |
| `roleId` | path | `integer` | Yes |  |
| `Cursor` | query | `string` | No | Cursor returned by a previous page. Omit for the first page. |
| `Limit` | query | `integer` | No | Page size: 10, 25, 50, or 100. Defaults to 10. |
| `SortOrder` | query | `OrganizationsServiceApi.SortOrder` | No | Sort order. Only `Asc` is currently supported; defaults to `Asc`. |

**Responses:**

- `200`: Success → `GroupInvitationCursorPageResponse`
- `400`: Bad Request → `OrganizationsServiceApi.ErrorResponse`
- `401`: Unauthorized → `OrganizationsServiceApi.ErrorResponse`
- `403`: Forbidden → `OrganizationsServiceApi.ErrorResponse`
- `404`: Not Found → `OrganizationsServiceApi.ErrorResponse`
- `500`: Server Error → `OrganizationsServiceApi.ErrorResponse`

**Response fields** (`GroupInvitationCursorPageResponse`)

See [GroupInvitationCursorPageResponse](#groupinvitationcursorpageresponse) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "groupId": "...",
      "recipientUserId": "...",
      "senderUserId": "...",
      "status": "...",
      "roleIds": "..."
    }
  ],
  "nextPageCursor": "string",
  "previousPageCursor": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v2/groups/{GROUPID}/roles/{ROLEID}/invitations"
```

### GET `/v2/groups/{groupId}/transactions`

**Server:** `https://economy.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |
| `exclusiveStartRequest` | query | `any` | No |  |
| `transactionType` | query | `any` | No |  |

**Responses:**

- `200`: OK → `TransactionResponseApiPageResponse`

**Response fields** (`TransactionResponseApiPageResponse`)

See [TransactionResponseApiPageResponse](#transactionresponseapipageresponse) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "idHash": "...",
      "created": "...",
      "isPending": "...",
      "agent": "...",
      "details": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://economy.roblox.com/v2/groups/{GROUPID}/transactions"
```

### GET `/v2/groups/{groupId}/users/{userId}/invitation` [BETA]

Get the open invitation to a group for a user

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |
| `userId` | path | `integer` | Yes |  |

**Responses:**

- `200`: Success → `GroupInvitation`
- `401`: Unauthorized → `OrganizationsServiceApi.ErrorResponse`
- `403`: Forbidden → `OrganizationsServiceApi.ErrorResponse`
- `404`: Not Found → `OrganizationsServiceApi.ErrorResponse`
- `500`: Server Error → `OrganizationsServiceApi.ErrorResponse`

**Response fields** (`GroupInvitation`)

See [GroupInvitation](#groupinvitation) in Models.

**Response example:**
```json
{
  "id": "string",
  "groupId": 0,
  "recipientUserId": 0,
  "senderUserId": 0,
  "status": "Open",
  "roleIds": [
    0
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v2/groups/{GROUPID}/users/{USERID}/invitation"
```

### GET `/v2/users/{userId}/groups/roles`

Gets a list of all group roles for groups the specified user is in.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user id. |
| `includeLocked` | query | `boolean` | Yes |  |
| `includeNotificationPreferences` | query | `boolean` | Yes |  |
| `discoveryType` | query | `0 \| 1 \| 2` | Yes | Valid values: `0`, `1`, `2` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupMembershipResponse_`
- `400`: 3: The user is invalid or does not exist.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupMembershipResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupMembershipResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-groups-api-groupmembershipresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "group": "...",
      "role": "...",
      "isNotificationsEnabled": "...",
      "notificationPreferences": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v2/users/{USERID}/groups/roles?includeLocked={VALUE}&includeNotificationPreferences={VALUE}&discoveryType={VALUE}"
```

## Models

### Group

A mini-community within Roblox for communication, discussions, and more.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the group.  Format: `groups/{group_id}` |
| `createTime` | `string` | No | The timestamp when the group was created. |
| `updateTime` | `string` | No | The timestamp when the group was last updated. |
| `id` | `string` | No | A unique ID that identifies the group. |
| `displayName` | `string` | No | The name of the group.  Must be non-empty. Has a maximum limit of 50 characters. |
| `description` | `string` | No | The description of the group.  Has a maximum limit of 1000 characters. |
| `owner` | `string` | No | The resource path of the owner.  If the group is abandoned and has no owner, this field is not returned. |
| `memberCount` | `integer` | No | The total number of members within a group. |
| `publicEntryAllowed` | `boolean` | No | Whether the group allows public entry. |
| `locked` | `boolean` | No | Whether the group is locked.  A locked group is a group that has been moderated/banned by Roblox. |
| `verified` | `boolean` | No | Whether the group has the verified badge. |

### ListGroupForumCategoriesResponse

A list of GroupForumCategories in the parent collection.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupForumCategories` | `GroupForumCategory[]` | No | The GroupForumCategories from the specified Group. |
| `nextPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### ListGroupForumPostsResponse

A list of GroupForumPosts in the parent collection.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupForumPosts` | `GroupForumPost[]` | No | The GroupForumPosts from the specified GroupForumCategory. |
| `nextPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### ListGroupForumCommentsResponse

A list of GroupForumComments in the parent collection.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupForumComments` | `GroupForumComment[]` | No | The GroupForumComments from the specified GroupForumPost. |
| `nextPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### ListGroupJoinRequestsResponse

A list of GroupJoinRequests in the parent collection.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupJoinRequests` | `GroupJoinRequest[]` | No | The GroupJoinRequests from the specified Group. |
| `nextPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### AcceptGroupJoinRequestRequest

A join request ID.

| Property | Type | Required | Description |
|----------|------|----------|-------------|

### DeclineGroupJoinRequestRequest

A join request ID.

| Property | Type | Required | Description |
|----------|------|----------|-------------|

### ListGroupMembershipsResponse

A list of GroupMemberships in the parent collection.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupMemberships` | `GroupMembership[]` | No | The GroupMemberships from the specified Group. |
| `nextPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### GroupMembership

A membership to a group. A user ID can be used in place of a membership ID.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the group membership.  Format: `groups/{group_id}/memberships/{group_membership_id}` |
| `createTime` | `string` | No | The timestamp when the group membership was created. |
| `updateTime` | `string` | No | The timestamp when the group membership was last updated. |
| `user` | `string` | No |  *(immutable)* The resource path of a member of the group. |
| `role` | `string` | No | The resource path of the member's highest-ranked role. When the member holds multiple roles, this reflects only the highest-ranked one. Prefer using the `roles` field, which always contains the complete set of assigned roles. |
| `roles` | `string[]` | No | The resource paths of all roles assigned to the group member. This is the recommended field for reading a member's roles, as it always contains the complete set of roles held by the member. |

### AssignRoleGroupMembershipRequest

Assigns a role to the specified group membership.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `role` | `string` | Yes | The resource path of the role to assign.  Format: `groups/{group_id}/roles/{group_role_id}` |

### UnassignRoleGroupMembershipRequest

Unassigns a role from the specified group membership.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `role` | `string` | Yes | The resource path of the role to unassign.  Format: `groups/{group_id}/roles/{group_role_id}` |

### ListGroupRolesResponse

A list of GroupRoles in the parent collection.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupRoles` | `GroupRole[]` | No | The GroupRoles from the specified Group. |
| `nextPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### GroupRole

A configurable property to grant specific privileges for members within a
group.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the group role.  Format: `groups/{group_id}/roles/{group_role_id}` |
| `createTime` | `string` | No | The timestamp for when the group role was last updated.  Visible only to owners of the group. |
| `updateTime` | `string` | No | The timestamp when the group role was last updated.  Visible only to owners of the group. |
| `id` | `string` | No | A unique ID that identifies a role.  Distinct from a role's rank, which is only unique within the group. |
| `displayName` | `string` | No | The name of the role.  Has a maximum limit of 100 characters. Names above the limit are rejected. |
| `description` | `string` | No | The description of the role.  Has a maximum limit of 1000 characters. Strings above the limit are rejected. Visible only to owners of the group. |
| `rank` | `integer` | No | The rank of the role.  The minimum value is 0. The maximum value is 255. |
| `memberCount` | `integer` | No | Total number of members within a role.  This field is not returned for guest roles. |
| `permissions` | `GroupRole_RolePermissions` | No | The permissions granted for this role.  This value is populated based on the read scope and role of the authorized user or API key creator. If the user or creator is the owner of the parent group, they are able to view all role permissions in the group. If the user or creator is a member of the parent group, they are able to view their role's permissions in the group. Anyone can view guest permissions. In the case that someone can't view the permissions, this field is not returned. |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.GroupModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Api.Develop.Models.GroupModel[]` | No |  |

### Roblox.Groups.Api.GroupPolicyRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupIds` | `integer[]` | No |  |

### Roblox.Groups.Api.GroupPoliciesResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groups` | `Roblox.Groups.Api.GroupPolicyResponse[]` | No |  |

### Roblox.Groups.Api.GroupAuditLogPageResponse_Roblox.Groups.Api.Models.Response.GroupAuditLogResponseItem_

ApiPageResponse for group audit log

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Api.Models.Response.GroupAuditLogResponseItem[]` | No |  |

### Roblox.Groups.Api.UpdateGroupDescriptionRequest

A request model for setting a description for the group

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | `string` | No | The group description being set. |

### Roblox.Groups.Api.GroupDescriptionResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `newDescription` | `string` | No | The new description returned |

### Roblox.Groups.Api.UpdateGroupNotificationPreferenceRequest

A request model for updating a group's notification preference.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `notificationsEnabled` | `boolean` | No | Whether the user wants to receive notifications from the group. |
| `type` | `0 \| 1 \| 2 \| 3 \| 4` | No | ['AnnouncementCreatedNotification' = 0, 'ForumPostCreatedNotification' = 1, 'ForumCommentCreatedNotification' = 2, 'ForumCommentReplyCreatedNotification' = 3, 'ForumSubscriberNotification' = 4] |

### Roblox.Groups.Api.GroupSettingsResponse

Response model for Group Settings

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isApprovalRequired` | `boolean` | No | Whether public entry is allowed. |
| `isBuildersClubRequired` | `boolean` | No | Whether Builder's Club is required. |
| `areEnemiesAllowed` | `boolean` | No | Whether enemy club declarations are allowed. |
| `areGroupFundsVisible` | `boolean` | No | Whether funds are publicly visible. |
| `areGroupGamesVisible` | `boolean` | No | Whether games are publicly visible. |
| `isGroupNameChangeEnabled` | `boolean` | No | If the group name change feature is enabled for this group. |
| `verificationLevel` | `0 \| 1 \| 2 \| 3` | No | The verification level for the group. Null if the verification level could not be determined due to an error. |
| `accountTenureRequirement` | `integer enum (6 values)` | No | The account tenure requirement for the group. Null if the account tenure requirement could not be determined due to an error. Values: 0, 1, 2, 3, 4, 5 |
| `slowmode` | `0 \| 1 \| 2 \| 3` | No | The slowmode level for the group (0-4). 0 = No slowmode, 1-4 = Slowmode levels with increasing restrictions. |
| `isMemberListVisibleToPublic` | `boolean` | No | Whether the group member list is visible to public. |
| `isAutoAssignRoleDisabled` | `boolean` | No | Whether automatic assignment of the lowest non-guest role is disabled for this group. For non-legacy groups (created after the multi-role cutoff), this is always true. For legacy groups, reflects the persisted GroupFeatureSettings value. Null when the value could not be determined. |
| `hasLegacyAutoAssignRole` | `boolean` | No | Whether this group still auto-assigns its lowest non-guest role to new members. |
| `communityTier` | `Roblox.Groups.Client.CommunityTierInfoResponse` | No |  |

### Roblox.Groups.Api.UpdateGroupSettingsRequest

A request model for updating a group's settings.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isApprovalRequired` | `boolean` | No | Whether public entry is allowed. |
| `areEnemiesAllowed` | `boolean` | No | Whether enemy club declarations are allowed. |
| `areGroupFundsVisible` | `boolean` | No | Whether funds are publicly visible. |
| `areGroupGamesVisible` | `boolean` | No | Whether games are publicly visible. |
| `verificationLevel` | `0 \| 1 \| 2 \| 3` | No | The verification level for the group. |
| `accountTenureRequirement` | `integer enum (6 values)` | No | The account tenure requirement for the group. Values: 0, 1, 2, 3, 4, 5 |
| `slowmode` | `0 \| 1 \| 2 \| 3` | No | The slowmode level for the group (0-4). 0 = No slowmode, 1-4 = Slowmode levels with increasing restrictions. Null = No change to current slowmode setting. |
| `isMemberListVisibleToPublic` | `boolean` | No | Whether the group member list is visible to public. |

### Roblox.Groups.Api.PostGroupStatusRequest

A request model for setting the authenticated user's primary group.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | `string` | No | The message to set the group status to. |

### Roblox.Groups.Api.ShoutResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `body` | `string` | No | The shout's message |
| `poster` | `Roblox.Groups.Api.Models.Response.UserModel` | No |  |
| `created` | `string` | No | The shout's created time |
| `updated` | `string` | No | The shout's last updated time |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupDetailResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Groups.Api.GroupDetailResponse[]` | No |  |

### Roblox.Groups.Client.GroupFeaturedContentResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupId` | `integer` | No |  |
| `contentType` | `string` | No |  |
| `contentId` | `string` | No |  |

### Roblox.Groups.Api.GroupConfigurationDisplayOptionsResponse

A response model for group configuration

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupConfiguration` | `Roblox.Groups.Api.GroupConfigurationResponse` | No |  |
| `recurringPayoutsConfiguration` | `Roblox.Groups.Api.RecurringPayoutsConfigurationResponse` | No |  |
| `roleConfiguration` | `Roblox.Groups.Api.RoleConfigurationResponse` | No |  |
| `groupNameChangeConfiguration` | `Roblox.Groups.Api.GroupNameChangeConfigurationResponse` | No |  |
| `isPremiumPayoutsEnabled` | `boolean` | No | The configuration of premium payouts shows in Group Revenue Summary page |
| `isDefaultEmblemPolicyEnabled` | `boolean` | No | If set to true, default group emblem policies handled by GUAC will be enabled              If set to false, default group emblem policies will not be enabled |

### Roblox.Web.Responses.Groups.GroupResponseV2

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `description` | `string` | No |  |
| `owner` | `Roblox.Web.Responses.RelatedEntityTypeResponse_Roblox.Web.Responses.Groups.GroupOwnerType_` | No |  |
| `memberCount` | `integer` | No |  |
| `created` | `string` | No |  |
| `hasVerifiedBadge` | `boolean` | No |  |

### Roblox.Groups.Api.GroupsDisplayOptionsResponse

A group roles response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupLimit` | `integer` | No | The user's builders club membership group limit |
| `currentGroupCount` | `integer` | No | The user's current group membership count |
| `groupStatusMaxLength` | `integer` | No | The maximum length of a group status |
| `areProfileGroupsHidden` | `boolean` | No | If set to true, groups showcase will not show on users profiles.              If set to false, group showcase will display on users profiles. |
| `isGroupDetailsPolicyEnabled` | `boolean` | No | If set to true, group details will respect GUAC policies for group details              If set to false, group details will not respect GUAC policies |
| `showPreviousGroupNames` | `boolean` | No | Whether or not we should show previous names of this group |
| `areGroupBansEnabled` | `boolean` | No | Whether or not group bans are enabled |
| `canEnableGroupNotifications` | `boolean` | No | Whether or not group notifications can be enabled |

### Roblox.Groups.Api.GroupSearchPageResponse

ApiPageResponse for catalog search

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `keyword` | `string` | No | Keyword used for search query |
| `totalResults` | `integer` | No |  |
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Api.GroupSearchResponseItem[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Web.Responses.Groups.GroupBasicResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Web.Responses.Groups.GroupBasicResponse[]` | No |  |

### Roblox.Groups.Api.GroupSearchMetadataResponse

Response Model For Group Search Metadata Endpoint

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `SuggestedGroupKeywords` | `string[]` | No | Suggested Group Category translation keys |
| `ShowFriendsGroupsSort` | `boolean` | No | Whether or not the Friends' Groups sort should show for the authenticated user |

### Roblox.Groups.Api.GroupDetailResponse

A detailed group response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The group id |
| `name` | `string` | No | The group name |
| `description` | `string` | No | The group description |
| `owner` | `Roblox.Groups.Api.Models.Response.UserModel` | No |  |
| `shout` | `Roblox.Groups.Api.ShoutResponse` | No |  |
| `memberCount` | `integer` | No | The number of members in the group |
| `isBuildersClubOnly` | `boolean` | No | Whether the group is Builders Club only |
| `publicEntryAllowed` | `boolean` | No | Whether the group is public (no approval required) |
| `isLocked` | `boolean` | No | Whether the group is locked |
| `isDeactivated` | `boolean` | No | Whether the group is deactivated |
| `hasVerifiedBadge` | `boolean` | No | Whether the group has a verified badge. |
| `hasSocialModules` | `boolean` | No | Whether the group has social modules enabled (e.g. Forums) (determines if "Followers" vs "Members" should be shown). |
| `communityTier` | `Roblox.Groups.Client.CommunityTierInfoResponse` | No |  |

### Roblox.Groups.Api.ChangeOwnerRequest

A request model for changing the group owner.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | `integer` | No | The user id. |

### Roblox.Groups.Api.GetCommunityFeatureFreezesResponse

Response model for the community feature freezes endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `features` | `Roblox.Groups.Api.CommunityFeatureFreezeStatus[]` | No | The freeze status of each community feature. |

### Roblox.Groups.Client.TierEvaluationResultResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tierInfo` | `Roblox.Groups.Client.CommunityTierInfoResponse` | Yes |  |
| `passedSignals` | `string[]` | Yes |  |
| `requirements` | `Roblox.Groups.Client.TierRequirement[]` | No |  |

### Roblox.Groups.Api.GroupConfigurationDetailsResponse

A detailed group response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupId` | `integer` | No | The group id |
| `emblemId` | `integer` | No | The group emblem id |
| `coverPhotoId` | `integer` | No | The group cover photo id |

### Roblox.Groups.Client.GetGroupEmoteSetsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `emoteSets` | `Roblox.Groups.Client.EmoteSetModel[]` | No |  |

### Roblox.Groups.Api.GetGroupFeaturesResponse

Response model for the group features endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isLocked` | `boolean` | No | Whether the group is currently locked. |
| `features` | `Roblox.Groups.Api.GroupFeatureResponse[]` | No | The freeze status of each feature for the group. |

### Roblox.Groups.Api.SetFeaturesRequestModel

Request model for setting the desired status of group features.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Features` | `object` | Yes | Dictionary of features and their desired status. |

### Roblox.Groups.Api.SetFeaturesResponseModel

Response model for setting the desired status of group features.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Updated` | `boolean` | Yes | Whether any features were updated. |

### Roblox.Groups.Api.HasGroupFeaturesBlockedResponse

Response model for the features/status endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `hasFeaturesBlocked` | `boolean` | No | Whether the group has any active feature freezes. |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.GroupJoinRequestResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Api.GroupJoinRequestResponse[]` | No |  |

### Roblox.Groups.Api.GroupJoinRequestResponse

Response model for a group join request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `requester` | `Roblox.Groups.Api.Models.Response.UserModel` | No |  |
| `created` | `string` | No | The DateTime the request was created |

### Roblox.Groups.Api.GroupMembershipMetadataResponse

A user's group membership metadata response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupId` | `integer` | No | The group id |
| `isPrimary` | `boolean` | No | Whether the group is primary |
| `isPendingJoin` | `boolean` | No | Whether there has been a request to join this group |
| `userRole` | `Roblox.Groups.Api.UserGroupRoleResponse` | No |  |
| `permissions` | `Roblox.Groups.Api.GroupPermissionsModel` | No |  |
| `channelPermissions` | `Roblox.Groups.Api.GroupChannelPermissionsModel[]` | No | The users's permissions for each communication channel in the group |
| `areGroupGamesVisible` | `boolean` | No | Whether group games are visible |
| `areGroupFundsVisible` | `boolean` | No | Whether group funds are visible |
| `areEnemiesAllowed` | `boolean` | No | Whether enemies are allowed |
| `canConfigure` | `boolean` | No | If the user can configure the group |
| `isNotificationsEnabled` | `boolean` | No | Whether the group's notification preferences set to enabled for the user |
| `notificationPreferences` | `Roblox.Groups.Api.GroupNotificationPreferenceData[]` | No |  |
| `isBannedFromGroup` | `boolean` | No | Whether the user is banned from the group |
| `canViewMemberList` | `boolean` | No | Whether the user can view the group member list |
| `isOwner` | `boolean` | No | Whether the authenticated user is the owner of the group |

### Roblox.Groups.Api.UpdateGroupNameRequest

A request model for setting a name for the group

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The group name being set. |

### Roblox.Groups.Api.UpdateGroupNameResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `newName` | `string` | No | The new description returned |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.Models.Response.GroupNameHistoryResponseItem_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Api.Models.Response.GroupNameHistoryResponseItem[]` | No |  |

### Roblox.Groups.Api.GroupPayoutRestrictionResponse

Response model for Group Payout Restriction

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `canUseRecurringPayout` | `boolean` | No | Whether the group can use recurring payout feature. |
| `canUseOneTimePayout` | `boolean` | No | Whether the group can use one-time payout feature. |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupPayoutResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Groups.Api.GroupPayoutResponse[]` | No |  |

### Roblox.Groups.Api.OneTimePayoutResponse

Response model for one-time payout requests.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | `0 \| 1` | No | One-time payout status. ['NotHeld' = 0, 'Held' = 1] |

### PublicAllOneTimePayoutsResponseModel

Public response for one-time payouts.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `payouts` | `PublicOneTimePayoutResponseModel[]` | No |  |

### OrganizationsServiceApi.ErrorResponse

Standard error response model.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | `OrganizationsServiceApi.ErrorCode` | Yes |  |
| `message` | `string` | No | The error message. |
| `field` | `string` | No | Field on which model validation failed. |

### PublicGroupUniversePayoutPageResponseModel

Public groups-style payout page.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `PublicUserUniversePayout[]` | No |  |
| `nextPageCursor` | `string` | No |  |
| `previousPageCursor` | `string` | No |  |

### Roblox.Groups.Api.GroupRelationshipsResponse

A group relationships response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupId` | `integer` | No | The group id |
| `relationshipType` | `1 \| 2` | No | The group relationship type ['Allies' = 1, 'Enemies' = 2] |
| `totalGroupCount` | `integer` | No | The total number of groups for this relationship type |
| `relatedGroups` | `Roblox.Groups.Api.GroupDetailResponse[]` | No | The related or requested groups |
| `nextRowIndex` | `integer` | No | The index for the next page of related groups |

### RevenueSummaryResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `recurringRobuxStipend` | `integer` | No |  |
| `itemSaleRobux` | `integer` | No |  |
| `purchasedRobux` | `integer` | No |  |
| `tradeSystemRobux` | `integer` | No |  |
| `pendingRobux` | `integer` | No |  |
| `groupPayoutRobux` | `integer` | No |  |
| `individualToGroupRobux` | `integer` | No |  |
| `premiumPayouts` | `integer` | No |  |
| `groupPremiumPayouts` | `integer` | No |  |
| `adjustmentRobux` | `integer` | No |  |
| `immersiveAdPayouts` | `integer` | No |  |
| `subscriptionPayouts` | `integer` | No |  |
| `subscriptionClawbacks` | `integer` | No |  |
| `isShowImmersiveAdPayoutSummaryOnZeroEnabled` | `boolean` | No |  |
| `commissionRobux` | `integer` | No |  |
| `publishingAdvanceRebates` | `integer` | No |  |
| `groupAffiliatePayoutRobux` | `integer` | No |  |
| `creatorRewardsPayoutRobux` | `integer` | No |  |

### Roblox.Groups.Api.GroupAllRolesResponse

A group roles response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupId` | `integer` | No | The group id |
| `roles` | `Roblox.Groups.Api.GroupRoleResponse[]` | No | The roles in the group |

### Roblox.Groups.Api.GroupPermissionsResponse

A group role's permissions response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupId` | `integer` | No | The group id |
| `role` | `Roblox.Groups.Api.GroupRoleResponse` | No |  |
| `permissions` | `Roblox.Groups.Api.GroupPermissionsModel` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupPermissionsResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Groups.Api.GroupPermissionsResponse[]` | No |  |

### Roblox.Groups.Api.UpdatePermissionsRequest

A request model for updating a group's roleset's permissions.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `permissions` | `object` | No | The permission-value pairs to be updated. |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.Models.Response.UserModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Api.Models.Response.UserModel[]` | No |  |

### Roblox.Groups.Api.Models.Request.CreateRoleSetRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The name of the roleset. |
| `description` | `string` | No | The description of the roleset. |
| `rank` | `integer` | No | The rank/positioning of the roleset. |
| `usingGroupFunds` | `boolean` | No | Setting to use group funds or not. |
| `isPrivate` | `boolean` | No | Optional. When true the role is only visible to members with permission to see private roles. Defaults to false (public). Only accessible to group owners. |

### Roblox.Groups.Api.GroupRoleResponse

A group role response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The role id |
| `name` | `string` | No | The role name |
| `description` | `string` | No | The role description |
| `rank` | `integer` | No | The role rank |
| `memberCount` | `integer` | No | The number of members in the role. |
| `isBase` | `boolean` | No | Whether or not the role is the base role for the group |
| `color` | `integer enum (17 values)` | No | The role color. ['Invalid' = 0, 'Blue' = 1, 'Green' = 2, 'Purple' = 3, 'Yellow' = 4, 'Orange' = 5, 'Red' = 6, 'Magenta' = 7, 'Teal' = 8, 'Turquoise' = 9, 'Rust' = 10, 'Pistachio' = 11, 'Midnight' = 12, 'Lavender' = 13, 'Pink' = 14, 'Crimson' = 15, 'Plum' = 16] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 |
| `isPrivate` | `boolean` | No | Whether the role is private (only visible to members with permission). Omitted from the response when false. |

### Roblox.Groups.Api.Models.Request.UpdateRoleSetRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The name of the roleset. |
| `description` | `string` | No | The description of the roleset. |
| `rank` | `integer` | No | The rank/positioning of the roleset. |
| `color` | `integer` | No | Optional. The color of the roleset (GroupRoleSetColorType value, e.g. 0 = Invalid, 1 = Blue). When omitted, only name and description are updated and the existing color is left unchanged. When set, name, description, and color are updated via UpdateGroupRoleSetProperties. |
| `isPrivate` | `boolean` | No | Optional. When set, updates the visibility of the roleset. Only accessible to group owners. The base (guest) role cannot be made private. |

### Roblox.Groups.Api.GetSocialLinkResponse

A social link response from a create request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Groups.Api.SocialLinkResponse[]` | No |  |
| `socialLinksVerificationStatus` | `0 \| 1 \| 2 \| 3` | No |  |

### Roblox.Groups.Api.SocialLinkRequest

An update request for a social link

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | `integer enum (9 values)` | No | What type of social media this points to Values: 0, 1, 2, 3, 4, 5, 6, 7, 8 |
| `url` | `string` | No | The url of the link |
| `title` | `string` | No | The title of the link |

### Roblox.Groups.Api.SocialLinkResponse

A social link response from a create request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The id of the social link |
| `type` | `integer enum (9 values)` | No | What type of social media (including Roblox Group) this points to ['Facebook' = 0, 'Twitter' = 1, 'YouTube' = 2, 'Twitch' = 3, 'GooglePlus' = 4, 'Discord' = 5, 'RobloxGroup' = 6, 'Amazon' = 7, 'Guilded' = 8] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8 |
| `url` | `string` | No | The url of the link |
| `title` | `string` | No | The title of the link |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Api.Develop.Models.UniverseModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Api.Develop.Models.UniverseModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.UserGroupRoleResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Api.UserGroupRoleResponse[]` | No |  |

### Roblox.Groups.Api.JoinGroupRequest

A request model for joining group.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sessionId` | `string` | No |  |
| `redemptionToken` | `string` | No |  |
| `captchaId` | `string` | No |  |
| `captchaToken` | `string` | No |  |
| `captchaProvider` | `string` | No |  |
| `challengeId` | `string` | No |  |

### Roblox.Groups.Api.UpdateUserRoleRequest

A request model for setting a users role in a group.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `roleId` | `integer` | No | The role in the group the user should be put into. |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupRoleDetailResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Groups.Api.GroupRoleDetailResponse[]` | No |  |

### PublicAllGroupUniversePayoutsResponseModel

Public response for recurring payouts.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `payouts` | `PublicGroupUniversePayout[]` | No |  |

### PublicUpdateUniverseRecurringPayoutsRequestModel

Request for updating recurring payouts through the public groups API.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `payouts` | `PublicRecurringPayoutRequestModel[]` | Yes | The recurring payout splits to apply. |

### Roblox.Groups.Api.PrimaryGroupRequest

A request model for setting the authenticated user's primary group.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupId` | `integer` | No | The group id. |

### Roblox.Groups.Api.GroupMembershipDetailResponse

A group membership response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `group` | `Roblox.Groups.Api.GroupDetailResponse` | No |  |
| `role` | `Roblox.Groups.Api.GroupRoleResponse` | No |  |
| `isPrimaryGroup` | `boolean` | No | Whether the group is the user's Primary Group |
| `isNotificationsEnabled` | `boolean` | No | Whether the group notification preferences are enabled for the user |
| `notificationPreferences` | `Roblox.Groups.Api.GroupNotificationPreferenceData[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupMembershipDetailResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Groups.Api.GroupMembershipDetailResponse[]` | No |  |

### PrivateServerPermissionsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `clanAllowed` | `boolean` | No |  |
| `enemyClanId` | `integer` | No |  |
| `friendsAllowed` | `boolean` | No |  |
| `users` | `SkinnyUserResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Web.Responses.Groups.GroupResponseV2_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Web.Responses.Groups.GroupResponseV2[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.Models.Response.GroupExperienceResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Api.Models.Response.GroupExperienceResponse[]` | No |  |

### GroupInvitationCursorPageResponse

A page of results using groups-api opaque cursor pagination.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `GroupInvitation[]` | Yes | The items in this page. |
| `nextPageCursor` | `string` | No | Cursor for the next page, if any. |
| `previousPageCursor` | `string` | No | Cursor for the previous page, if any. |

### CreateGroupInvitationRequestModel

Request for inviting a user to a group.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `recipientUserId` | `integer` | Yes | The user to invite. |
| `roleIds` | `integer[]` | No | Group role ids to grant when the invitation is accepted. |

### GroupInvitation

An invitation to join a group.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | Yes | The invitation id. Stringified because it can exceed the 2^53-1 JSON number limit. |
| `groupId` | `integer` | Yes | The group the invitation is for. |
| `recipientUserId` | `integer` | Yes | The invited user. |
| `senderUserId` | `integer` | Yes | The user who sent the invitation. |
| `status` | `GroupInvitationStatus` | Yes |  |
| `roleIds` | `integer[]` | Yes | Every group role id attached to the invitation. |
| `updatedAt` | `string` | Yes | When the invitation was last updated (UTC). |

### UpdateGroupInvitationRequestModel

Request for accepting or declining a group invitation.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | `GroupInvitationStatus` | Yes |  |

### SuccessResponse

Standard success response model.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | Yes | Whether or not the request was successfully executed. |

### TransactionResponseApiPageResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `TransactionResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Groups.Api.GroupMembershipResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Groups.Api.GroupMembershipResponse[]` | No |  |