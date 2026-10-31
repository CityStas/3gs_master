---
name: "Groups Api v2"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://groups.roblox.com"
versions: [v2, v1]
endpoints: 87
auth: [cookie]
---

# Groups Api v2

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://groups.roblox.com`
**Versions:** v2, v1

## V2

### GET `/v2/groups`

Multi-get groups information by Ids.

If a group comes back as null, it will not be returned in the response.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupIds` | query | `array` | Yes | The group Ids. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Groups.GroupResponseV2]`
- `400`: 2: Too many ids in request. 3: Ids could not be parsed from request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Groups.GroupResponseV2]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Groups.GroupResponseV2]](#roblox-web-webapi-models-apiarrayresponse-roblox-web-responses-groups-groupresponsev2-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v2/groups?groupIds={VALUE}"
```

### GET `/v2/groups/{groupId}/experiences`

Gets experiences created by the specified group id.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id |
| `accessFilter` | query | `integer (int32)` | No | The access type of the experiences. Valid values: `1`, `2`, `4` |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.Models.Response.GroupExperienceResponse]`
- `501`: 47: Code path is not implemented.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.Models.Response.GroupExperienceResponse]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.Models.Response.GroupExperienceResponse]](#roblox-web-webapi-models-apipageresponse-roblox-groups-api-models-response-groupexperienceresponse-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v2/groups/{GROUPID}/experiences"
```

### GET `/v2/groups/{groupId}/relationships/{groupRelationshipType}`

Gets a group's relationships with cursor-based pagination.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |
| `groupRelationshipType` | path | `string` | Yes | The group relationship type, enemies or allies. |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.Models.Response.GroupRelationshipsV2Response`
- `400`: 1: Group is invalid or does not exist. 4: Group relationship type or request type is invalid. 8: Invalid or missing pagination parameters

**Response fields** (`Roblox.Groups.Api.Models.Response.GroupRelationshipsV2Response`)

See [Roblox.Groups.Api.Models.Response.GroupRelationshipsV2Response](#roblox-groups-api-models-response-grouprelationshipsv2response) in Models.

**Response example:**
```json
{
  "groupId": 0,
  "relationshipType": 1,
  "groupResponses": {
    "previousPageCursor": "string",
    "nextPageCursor": "string",
    "data": [
      "..."
    ]
  }
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v2/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}"
```

### GET `/v2/groups/{groupId}/relationships/{groupRelationshipType}/requests`

Gets a group's relationship requests with cursor-based pagination.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |
| `groupRelationshipType` | path | `string` | Yes | The group relationship type of the request, only allies are supported. |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.Models.Response.GroupRelationshipsV2Response`
- `400`: 1: Group is invalid or does not exist. 4: Group relationship type or request type is invalid. 8: Invalid or missing pagination parameters
- `401`: 0: Authorization has been denied for this request.
- `403`: 5: You don't have permission to manage this group's relationships.

**Response fields** (`Roblox.Groups.Api.Models.Response.GroupRelationshipsV2Response`)

See [Roblox.Groups.Api.Models.Response.GroupRelationshipsV2Response](#roblox-groups-api-models-response-grouprelationshipsv2response) in Models.

**Response example:**
```json
{
  "groupId": 0,
  "relationshipType": 1,
  "groupResponses": {
    "previousPageCursor": "string",
    "nextPageCursor": "string",
    "data": [
      "..."
    ]
  }
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v2/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}/requests"
```

### GET `/v2/users/{userId}/groups/roles`

Gets a list of all group roles for groups the specified user is in.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user id. |
| `includeLocked` | query | `boolean` | Yes |  |
| `includeNotificationPreferences` | query | `boolean` | Yes |  |
| `discoveryType` | query | `integer (int32)` | Yes | Valid values: `0`, `1`, `2` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupMembershipResponse]`
- `400`: 3: The user is invalid or does not exist.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupMembershipResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupMembershipResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-groups-api-groupmembershipresponse-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v2/users/{USERID}/groups/roles?includeLocked={VALUE}&includeNotificationPreferences={VALUE}&discoveryType={VALUE}"
```

## Models

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

### Roblox.Groups.Api.GroupMembershipResponse

A basic group membership response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `group` | `Roblox.Web.Responses.Groups.GroupBasicResponse` | No |  |
| `role` | `Roblox.Web.Responses.Groups.GroupRoleBasicResponse` | No |  |
| `isNotificationsEnabled` | `boolean` | No | Whether the group notification preferences are enabled for the user TODO: Deprecate this field - it only returns if announcement notifications are enabled and that information is already returned in the NotificationPreferences list below |
| `notificationPreferences` | `Roblox.Groups.Api.GroupNotificationPreferenceData[]` | No |  |

### Roblox.Groups.Api.GroupNotificationPreferenceData

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | `0 \| 1 \| 2 \| 3 \| 4` | No | ['AnnouncementCreatedNotification' = 0, 'ForumPostCreatedNotification' = 1, 'ForumCommentCreatedNotification' = 2, 'ForumCommentReplyCreatedNotification' = 3, 'ForumSubscriberNotification' = 4] |
| `enabled` | `boolean` | No |  |
| `name` | `string` | No |  |
| `description` | `string` | No |  |

### Roblox.Groups.Api.Models.Response.GroupExperienceResponse

A response model representing an experience/game.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The game (universe) Id. |
| `name` | `string` | No | The game name. |
| `description` | `string` | No | The game description. |
| `creator` | `Roblox.Web.Responses.RelatedEntityTypeResponse[Roblox.Platform.Core.CreatorType]` | No |  |
| `rootPlace` | `Roblox.Web.Responses.RelatedEntityTypeResponse[Roblox.Platform.Assets.AssetType]` | No |  |
| `created` | `string` | No | When the game was created. |
| `updated` | `string` | No | When the game was last updated. |
| `placeVisits` | `integer` | No | The number of place visits for this game. |

### Roblox.Groups.Api.Models.Response.GroupRelationshipsV2Response

A group relationships response model for V2 endpoints with cursor-based pagination.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupId` | `integer` | No | The group id. |
| `relationshipType` | `1 \| 2` | No | The group relationship type. ['Allies' = 1, 'Enemies' = 2] |
| `groupResponses` | `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.GroupDetailResponse]` | No |  |

### Roblox.Groups.Api.Models.Response.UserModel

A model representing data about an Roblox.Platform.Membership.IUser

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `buildersClubMembershipType` | `0 \| 1 \| 2 \| 3 \| 4` | No | The user's builders club membership type |
| `hasVerifiedBadge` | `boolean` | No | The user's verified badge status. |
| `userId` | `integer` | No |  |
| `username` | `string` | No |  |
| `displayName` | `string` | No |  |

### Roblox.Groups.Api.ShoutResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `body` | `string` | No | The shout's message |
| `poster` | `Roblox.Groups.Api.Models.Response.UserModel` | No |  |
| `created` | `string` | No | The shout's created time |
| `updated` | `string` | No | The shout's last updated time |

### Roblox.Groups.Client.CommunityTierInfoResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupId` | `integer` | Yes |  |
| `currentTier` | `integer` | Yes |  |
| `previousTier` | `integer` | No |  |
| `tierUpdatedTime` | `string` | No |  |
| `lastEvaluatedTime` | `string` | No |  |
| `requirements` | `Roblox.Groups.Client.TierRequirement[]` | No |  |
| `capabilities` | `Roblox.Groups.Client.TierCapabilities` | No |  |

### Roblox.Groups.Client.TierCapabilities

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isEligibleForUnrestrictedMessages` | `boolean` | Yes |  |

### Roblox.Groups.Client.TierRequirement

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `key` | `1 \| 2 \| 3 \| 4 \| 5` | Yes | ['OwnerModerationStatusOk' = 1, 'OwnerAgeEstimationVerified' = 2, 'OwnerIdVerified' = 3, 'OwnerTwoStepVerified' = 4, 'CommunityMeetsPlayerRequirement' = 5] |
| `satisfied` | `boolean` | Yes |  |

### Roblox.Web.Responses.Groups.GroupBasicResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `memberCount` | `integer` | No |  |
| `hasVerifiedBadge` | `boolean` | No |  |

### Roblox.Web.Responses.Groups.GroupResponseV2

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `description` | `string` | No |  |
| `owner` | `Roblox.Web.Responses.RelatedEntityTypeResponse[Roblox.Web.Responses.Groups.GroupOwnerType]` | No |  |
| `memberCount` | `integer` | No |  |
| `created` | `string` | No |  |
| `hasVerifiedBadge` | `boolean` | No |  |

### Roblox.Web.Responses.Groups.GroupRoleBasicResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `rank` | `integer` | No |  |

### Roblox.Web.Responses.RelatedEntityTypeResponse[Roblox.Platform.Assets.AssetType]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `type` | `integer enum (89 values)` | No | ['Image' = 1, 'TShirt' = 2, 'Audio' = 3, 'Mesh' = 4, 'Lua' = 5, 'HTML' = 6, 'Text' = 7, 'Hat' = 8, 'Place' = 9, 'Model' = 10, 'Shirt' = 11, 'Pants' = 12, 'Decal' = 13, 'Avatar' = 16, 'Head' = 17, 'Face' = 18, 'Gear' = 19, 'Badge' = 21, 'GroupEmblem' = 22, 'Animation' = 24, 'Arms' = 25, 'Legs' = 26, 'Torso' = 27, 'RightArm' = 28, 'LeftArm' = 29, 'LeftLeg' = 30, 'RightLeg' = 31, 'Package' = 32, 'YouTubeVideo' = 33, 'GamePass' = 34, 'App' = 35, 'Code' = 37, 'Plugin' = 38, 'SolidModel' = 39, 'MeshPart' = 40, 'HairAccessory' = 41, 'FaceAccessory' = 42, 'NeckAccessory' = 43, 'ShoulderAccessory' = 44, 'FrontAccessory' = 45, 'BackAccessory' = 46, 'WaistAccessory' = 47, 'ClimbAnimation' = 48, 'DeathAnimation' = 49, 'FallAnimation' = 50, 'IdleAnimation' = 51, 'JumpAnimation' = 52, 'RunAnimation' = 53, 'SwimAnimation' = 54, 'WalkAnimation' = 55, 'PoseAnimation' = 56, 'LocalizationTableManifest' = 59, 'LocalizationTableTranslation' = 60, 'EmoteAnimation' = 61, 'Video' = 62, 'TexturePack' = 63, 'TShirtAccessory' = 64, 'ShirtAccessory' = 65, 'PantsAccessory' = 66, 'JacketAccessory' = 67, 'SweaterAccessory' = 68, 'ShortsAccessory' = 69, 'LeftShoeAccessory' = 70, 'RightShoeAccessory' = 71, 'DressSkirtAccessory' = 72, 'FontFamily' = 73, 'FontFace' = 74, 'MeshHiddenSurfaceRemoval' = 75, 'EyebrowAccessory' = 76, 'EyelashAccessory' = 77, 'MoodAnimation' = 78, 'DynamicHead' = 79, 'CodeSnippet' = 80, 'AdsVideo' = 81, 'OtaUpdate' = 82, 'Screenshot' = 83, 'RuntimePropertySet' = 84, 'StorePreviewVideo' = 85, 'GamePreviewVideo' = 86, 'CreatorExperienceConfig' = 87, 'FaceMakeup' = 88, 'LipMakeup' = 89, 'EyeMakeup' = 90, 'VoxelFragment' = 91, 'AvatarBackground' = 92, 'TextDocument' = 93, 'Post' = 94, 'AnimatedImage' = 95, 'ComputeFunction' = 96] Values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 |
| `name` | `string` | No |  |

### Roblox.Web.Responses.RelatedEntityTypeResponse[Roblox.Platform.Core.CreatorType]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `type` | `0 \| 1 \| 2` | No | ['User' = 0, 'Group' = 1, 'Experience' = 2] |
| `name` | `string` | No |  |

### Roblox.Web.Responses.RelatedEntityTypeResponse[Roblox.Web.Responses.Groups.GroupOwnerType]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `type` | `0` | No | ['User' = 0] |
| `name` | `string` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupMembershipResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Groups.Api.GroupMembershipResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Groups.GroupResponseV2]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Web.Responses.Groups.GroupResponseV2[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.GroupDetailResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Api.GroupDetailResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.Models.Response.GroupExperienceResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Api.Models.Response.GroupExperienceResponse[]` | No |  |

## V1

### GET `/v1/featured-content/event`

Gets the featured event for a group

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | query | `integer (int64)` | Yes | The group Id. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/featured-content/event?groupId={VALUE}"
```

### POST `/v1/featured-content/event`

Sets the featured event for a group

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | query | `integer (int64)` | Yes | The group Id. |
| `eventId` | query | `integer (int64)` | Yes | The event Id. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/featured-content/event?groupId={VALUE}&eventId={VALUE}"
```

### DELETE `/v1/featured-content/event`

Deletes the featured event for a group

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | query | `integer (int64)` | Yes | The group Id. |
| `eventId` | query | `integer (int64)` | Yes | The event Id. |

**Responses:**

- `200`: OK
- `403`: 0: Token Validation Failed 3: User is not authorized to set featured content for this group.

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/featured-content/event?groupId={VALUE}&eventId={VALUE}"
```

### GET `/v1/groups/{groupId}`

Gets group information

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}"
```

### GET `/v1/groups/{groupId}/audit-log`

Gets the Group's audit log

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The id of the group the user is in. |
| `actionType` | query | `string` | No | Filter for specific type of action performed Valid values: `DeletePost`, `RemoveMember`, `AcceptJoinRequest`, `DeclineJoinRequest`, `PostStatus`, `ChangeRank`, `BuyAd`, `SendAllyRequest`, `CreateEnemy`, `AcceptAllyRequest`, `DeclineAllyRequest`, `DeleteAlly`, `DeleteEnemy`, `AddGroupPlace`, `RemoveGroupPlace`, `CreateItems`, `ConfigureItems`, `SpendGroupFunds`, `ChangeOwner`, `Delete`, `AdjustCurrencyAmounts`, `Abandon`, `Claim`, `Rename`, `ChangeDescription`, `InviteToClan`, `KickFromClan`, `CancelClanInvite`, `BuyClan`, `CreateGroupAsset`, `UpdateGroupAsset`, `ConfigureGroupAsset`, `RevertGroupAsset`, `CreateGroupDeveloperProduct`, `ConfigureGroupGame`, `CreateGroupDeveloperSubscriptionProduct`, `Lock`, `Unlock`, `CreateGamePass`, `CreateBadge`, `ConfigureBadge`, `SavePlace`, `PublishPlace`, `UpdateRolesetRank`, `UpdateRolesetData`, `UpdateRoleSetPosition`, `BanMember`, `UnbanMember`, `CreateForumCategory`, `UpdateForumCategory`, `ArchiveForumCategory`, `DeleteForumCategory`, `DeleteForumPost`, `DeleteForumComment`, `PinForumPost`, `UnpinForumPost`, `LockForumPost`, `UnlockForumPost`, `CreateRoleset`, `DeleteRoleset`, `CreateCommerceProduct`, `SetCommerceProductActive`, `ArchiveCommerceProduct`, `AcceptCommerceProductBundlingFee`, `SetCommerceProductInactive`, `ConnectMerchant`, `DisconnectMerchant`, `JoinGroup`, `LeaveGroup`, `UpdateGroupIcon`, `UpdateGroupCoverPhoto`, `AssignRole`, `UnassignRole`, `PublishAnnouncement`, `DeleteAnnouncement`, `UpdateRoleSetPermissions`, `UpdateGroupSecuritySettings`, `GrantEnterpriseTier`, `RevokeEnterpriseTier`, `DeactivateGroup` |
| `userId` | query | `integer (int64)` | No | Filter for specific user id |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupAuditLogPageResponse[Roblox.Groups.Api.Models.Response.GroupAuditLogResponseItem]`
- `400`: 1: Group is invalid or does not exist. 8: Invalid or missing pagination parameters
- `401`: 0: Authorization has been denied for this request.
- `403`: 23: Insufficient permissions to complete the request.

**Response fields** (`Roblox.Groups.Api.GroupAuditLogPageResponse[Roblox.Groups.Api.Models.Response.GroupAuditLogResponseItem]`)

See [Roblox.Groups.Api.GroupAuditLogPageResponse[Roblox.Groups.Api.Models.Response.GroupAuditLogResponseItem]](#roblox-groups-api-groupauditlogpageresponse-roblox-groups-api-models-response-groupauditlogresponseitem-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/audit-log"
```

### GET `/v1/groups/{groupId}/bans`

Gets the bans for the group

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.GroupBanMemberResponse]`
- `401`: 0: Authorization has been denied for this request.
- `403`: 19: You have insufficient permissions for this request.
- `404`: 1: The group is invalid or does not exist.
- `405`: 18: The operation is temporarily unavailable. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.GroupBanMemberResponse]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.GroupBanMemberResponse]](#roblox-web-webapi-models-apipageresponse-roblox-groups-api-groupbanmemberresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "user": "...",
      "actingUser": "...",
      "created": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/bans"
```

### GET `/v1/groups/{groupId}/bans/{userId}`

Fetch the group ban of a user from a group

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |
| `userId` | path | `integer (int64)` | Yes | The user Id. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupBanMemberResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 19: You have insufficient permissions for this request.
- `404`: 1: The group is invalid or does not exist. 3: The user is invalid or does not exist.
- `405`: 18: The operation is temporarily unavailable. Please try again later.

**Response fields** (`Roblox.Groups.Api.GroupBanMemberResponse`)

See [Roblox.Groups.Api.GroupBanMemberResponse](#roblox-groups-api-groupbanmemberresponse) in Models.

**Response example:**
```json
{
  "user": {
    "buildersClubMembershipType": 0,
    "hasVerifiedBadge": false,
    "userId": 0,
    "username": "string",
    "displayName": "string"
  },
  "actingUser": {
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
  "created": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/bans/{USERID}"
```

### POST `/v1/groups/{groupId}/bans/{userId}`

Bans a user from a group

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |
| `userId` | path | `integer (int64)` | Yes | The Id of the user being banned. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupBanMemberResponse`
- `400`: 28: The user is already banned from the group. 31: You cannot perform this action against the group owner.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 19: You have insufficient permissions for this request.
- `404`: 1: The group is invalid or does not exist. 3: The user is invalid or does not exist. 3: The user is invalid or does not exist. 15: User is not a member of the group.
- `405`: 18: The operation is temporarily unavailable. Please try again later.

**Response fields** (`Roblox.Groups.Api.GroupBanMemberResponse`)

See [Roblox.Groups.Api.GroupBanMemberResponse](#roblox-groups-api-groupbanmemberresponse) in Models.

**Response example:**
```json
{
  "user": {
    "buildersClubMembershipType": 0,
    "hasVerifiedBadge": false,
    "userId": 0,
    "username": "string",
    "displayName": "string"
  },
  "actingUser": {
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
  "created": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/bans/{USERID}"
```

### DELETE `/v1/groups/{groupId}/bans/{userId}`

Unbans a user from a group

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |
| `userId` | path | `integer (int64)` | Yes | The Id of the user being unbanned. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 29: The user is not banned from the group.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 19: You have insufficient permissions for this request.
- `404`: 1: The group is invalid or does not exist.
- `405`: 18: The operation is temporarily unavailable. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/bans/{USERID}"
```

### GET `/v1/groups/{groupId}/blocked-keywords`

Retrieves a paginated list of blocked keywords for a specific Group.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes |  |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.BlockedKeywordPageResponse[Roblox.Groups.Client.BlockedKeywordModel]`
- `400`: 1: Group is invalid or does not exist. 6: Limit is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 9: User is invalid or does not exist. 10: Insufficient permissions to complete the request.
- `405`: 31: Service is currently unavailable.

**Response fields** (`Roblox.Groups.Api.BlockedKeywordPageResponse[Roblox.Groups.Client.BlockedKeywordModel]`)

See [Roblox.Groups.Api.BlockedKeywordPageResponse[Roblox.Groups.Client.BlockedKeywordModel]](#roblox-groups-api-blockedkeywordpageresponse-roblox-groups-client-blockedkeywordmodel-) in Models.

**Response example:**
```json
{
  "totalActiveKeywordsCount": 0,
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "keyword": "...",
      "createdBy": "...",
      "isPrivate": "...",
      "createdAt": "...",
      "updatedAt": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/blocked-keywords"
```

### POST `/v1/groups/{groupId}/blocked-keywords`

Adds new blocked keyword(s) to the specified Group.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes |  |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.CreateBlockedKeywordsRequest`

See [Roblox.Groups.Api.CreateBlockedKeywordsRequest](#roblox-groups-api-createblockedkeywordsrequest) in Models.

**Request example:**
```json
{
  "keywords": "string",
  "isPrivate": false
}
```

**Responses:**

- `200`: OK → `Roblox.Groups.Client.CreateBlockedKeywordsResponse`
- `400`: 1: Group is invalid or does not exist. 2: One or more keywords are invalid. 4: Invalid request. 12: The provided content was moderated.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 8: Insufficient permissions to complete the request. 9: User is invalid or does not exist. 10: Insufficient permissions to complete the request.
- `405`: 31: Service is currently unavailable.
- `409`: 11: There was a conflict in your request.

**Response fields** (`Roblox.Groups.Client.CreateBlockedKeywordsResponse`)

See [Roblox.Groups.Client.CreateBlockedKeywordsResponse](#roblox-groups-client-createblockedkeywordsresponse) in Models.

**Response example:**
```json
{
  "createdKeywords": [
    {
      "id": "...",
      "keyword": "...",
      "createdBy": "...",
      "isPrivate": "...",
      "createdAt": "...",
      "updatedAt": "..."
    }
  ],
  "hadModeratedKeywords": false,
  "hadDuplicateKeywords": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/blocked-keywords" \
  -H "Content-Type: application/json" \
  -d '{
  "keywords": "string",
  "isPrivate": false
}'
```

### GET `/v1/groups/{groupId}/community-feature-freezes`

Gets the freeze status of the community features for a group.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes |  |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/community-feature-freezes"
```

### GET `/v1/groups/{groupId}/configuration`

Gets group configuration information

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/configuration"
```

### GET `/v1/groups/{groupId}/emotes`

Gets a groups emote sets.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes |  |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/emotes"
```

### GET `/v1/groups/{groupId}/features`

Gets the freeze status of all features and the lock status for a group.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes |  |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/features"
```

### PATCH `/v1/groups/{groupId}/features`

Sets the desired status of group features.
Currently only removes active freezes for features set to Roblox.Groups.Api.FeatureStatus.On.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes |  |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes |  |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/features/status"
```

### GET `/v1/groups/{groupId}/join-requests`

Gets a page of Group Join Requests for a group.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.GroupJoinRequestResponse]`
- `400`: 1: The group is invalid or does not exist. 36: The pagination cursor is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 19: You have insufficient permissions for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.GroupJoinRequestResponse]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.GroupJoinRequestResponse]](#roblox-web-webapi-models-apipageresponse-roblox-groups-api-groupjoinrequestresponse-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/join-requests"
```

### POST `/v1/groups/{groupId}/join-requests`

Batch accepts group join requests

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.MembersRequest`

See [Roblox.Groups.Api.MembersRequest](#roblox-groups-api-membersrequest) in Models.

**Request example:**
```json
{
  "UserIds": [
    0
  ]
}
```

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/join-requests" \
  -H "Content-Type: application/json" \
  -d '{
  "UserIds": [
    0
  ]
}'
```

### DELETE `/v1/groups/{groupId}/join-requests`

Batch declines group join requests

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.MembersRequest`

See [Roblox.Groups.Api.MembersRequest](#roblox-groups-api-membersrequest) in Models.

**Request example:**
```json
{
  "UserIds": [
    0
  ]
}
```

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
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/join-requests" \
  -H "Content-Type: application/json" \
  -d '{
  "UserIds": [
    0
  ]
}'
```

### GET `/v1/groups/{groupId}/join-requests/users/{userId}`

Gets a group join request by userId.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |
| `userId` | path | `integer (int64)` | Yes | The user Id. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/join-requests/users/{USERID}"
```

### POST `/v1/groups/{groupId}/join-requests/users/{userId}`

Accepts a group join request.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |
| `userId` | path | `integer (int64)` | Yes | The user Id. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/join-requests/users/{USERID}"
```

### DELETE `/v1/groups/{groupId}/join-requests/users/{userId}`

Declines/cancels a group join request.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |
| `userId` | path | `integer (int64)` | Yes | The user Id. |

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
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/join-requests/users/{USERID}"
```

### GET `/v1/groups/{groupId}/membership`

Gets group membership information in the context of the authenticated user

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |
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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/membership?includeNotificationPreferences={VALUE}"
```

### GET `/v1/groups/{groupId}/name-history`

Gets the Group's name change history.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The id of the group. |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.Models.Response.GroupNameHistoryResponseItem]`
- `400`: 1: Group is invalid or does not exist.
- `403`: 23: Insufficient permissions to complete the request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.Models.Response.GroupNameHistoryResponseItem]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.Models.Response.GroupNameHistoryResponseItem]](#roblox-web-webapi-models-apipageresponse-roblox-groups-api-models-response-groupnamehistoryresponseitem-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/name-history"
```

### GET `/v1/groups/{groupId}/payout-restriction`

Gets a value indicating whether the group can use payout feature

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/payout-restriction"
```

### GET `/v1/groups/{groupId}/payouts`

Gets a list of the group payout percentages

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupPayoutResponse]`
- `400`: 1: Group is invalid or does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 9: You don't have permission to view this group's payouts.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupPayoutResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupPayoutResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-groups-api-grouppayoutresponse-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/payouts"
```

### POST `/v1/groups/{groupId}/payouts`

Pays out a user in Robux.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.PayoutRequest`

See [Roblox.Groups.Api.PayoutRequest](#roblox-groups-api-payoutrequest) in Models.

**Request example:**
```json
{
  "PayoutType": 1,
  "Recipients": [
    {
      "recipientId": "...",
      "recipientType": "...",
      "amount": "..."
    }
  ],
  "IdempotencyKey": "string",
  "WatermarkContributions": [
    {
      "balanceKey": "...",
      "amount": "..."
    }
  ]
}
```

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/payouts" \
  -H "Content-Type: application/json" \
  -d '{
  "PayoutType": 1,
  "Recipients": [
    {
      "recipientId": "...",
      "recipientType": "...",
      "amount": "..."
    }
  ],
  "IdempotencyKey": "string",
  "WatermarkContributions": [
    {
      "balanceKey": "...",
      "amount": "..."
    }
  ]
}'
```

### GET `/v1/groups/{groupId}/relationships/{groupRelationshipType}`

Gets a group's relationships

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |
| `groupRelationshipType` | path | `string` | Yes | The group relationship type, enemies or allies. |
| `StartRowIndex` | query | `integer (int32)` | Yes | The start index of the page request |
| `MaxRows` | query | `integer (int32)` | Yes | The maximum number of rows for the page request, should be at least 1. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}?StartRowIndex={VALUE}&MaxRows={VALUE}"
```

### GET `/v1/groups/{groupId}/relationships/{groupRelationshipType}/requests`

Gets a group's relationship requests

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |
| `groupRelationshipType` | path | `string` | Yes | The group relationship type of the request, only allies are supported. |
| `StartRowIndex` | query | `integer (int32)` | Yes | The start index of the page request |
| `MaxRows` | query | `integer (int32)` | Yes | The maximum number of rows for the page request, should be at least 1. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}/requests?StartRowIndex={VALUE}&MaxRows={VALUE}"
```

### POST `/v1/groups/{groupId}/relationships/{groupRelationshipType}/requests`

Batch accepts group affiliate requests

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |
| `groupRelationshipType` | path | `string` | Yes | The type of group relationship being made |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.RelationshipsRequest`

See [Roblox.Groups.Api.RelationshipsRequest](#roblox-groups-api-relationshipsrequest) in Models.

**Request example:**
```json
{
  "GroupIds": [
    0
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}/requests" \
  -H "Content-Type: application/json" \
  -d '{
  "GroupIds": [
    0
  ]
}'
```

### DELETE `/v1/groups/{groupId}/relationships/{groupRelationshipType}/requests`

Batch declines group affiliate requests

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |
| `groupRelationshipType` | path | `string` | Yes | The type of group relationship being made |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.RelationshipsRequest`

See [Roblox.Groups.Api.RelationshipsRequest](#roblox-groups-api-relationshipsrequest) in Models.

**Request example:**
```json
{
  "GroupIds": [
    0
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}/requests" \
  -H "Content-Type: application/json" \
  -d '{
  "GroupIds": [
    0
  ]
}'
```

### GET `/v1/groups/{groupId}/roles`

Gets a list of the rolesets in a group.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |
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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/roles?includePrivate={VALUE}"
```

### GET `/v1/groups/{groupId}/roles/{roleSetId}/permissions`

Gets the permissions for a group's roleset. The authorized user must either be the group owner or the roleset being requested, except for guest roles, which can be viewed by all (members and guests).

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |
| `roleSetId` | path | `integer (int64)` | Yes | The group's role set id. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/roles/{ROLESETID}/permissions"
```

### PATCH `/v1/groups/{groupId}/roles/{roleSetId}/permissions`

Updates the permissions for a group's roleset. The authorized user must be the group owner.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group's id. |
| `roleSetId` | path | `integer (int64)` | Yes | The roleset's id. |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |
| `roleSetId` | path | `integer (int64)` | Yes | The group's role set id. |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.Models.Response.UserModel]`
- `400`: 1: The group is invalid or does not exist. 36: The pagination cursor is invalid.
- `403`: 2: The roleset is invalid or does not exist. 35: You do not have permission to view this group's member list.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.Models.Response.UserModel]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.Models.Response.UserModel]](#roblox-web-webapi-models-apipageresponse-roblox-groups-api-models-response-usermodel-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/roles/{ROLESETID}/users"
```

### GET `/v1/groups/{groupId}/roles/guest/permissions`

Gets the permissions for a group's guest roleset. These can be viewed by all (members and guests) users.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/roles/guest/permissions"
```

### GET `/v1/groups/{groupId}/roles/permissions`

Gets all permissions for each role

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupPermissionsResponse]`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupPermissionsResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupPermissionsResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-groups-api-grouppermissionsresponse-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/roles/permissions"
```

### GET `/v1/groups/{groupId}/settings`

Gets the Group's settings

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The id of the group the user is in. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/settings"
```

### PATCH `/v1/groups/{groupId}/settings`

Updates the group's settings

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The id of the group the user is in. |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The Id of the game |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/social-links"
```

### POST `/v1/groups/{groupId}/social-links`

Posts a social links

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The id of the group |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/social-links" \
  -H "Content-Type: application/json" \
  -d '{
  "type": 0,
  "url": "string",
  "title": "string"
}'
```

### GET `/v1/groups/{groupId}/users`

Gets a list of users in a group.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.UserGroupRoleResponse]`
- `400`: 1: The group is invalid or does not exist. 36: The pagination cursor is invalid.
- `403`: 35: You do not have permission to view this group's member list.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.UserGroupRoleResponse]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.UserGroupRoleResponse]](#roblox-web-webapi-models-apipageresponse-roblox-groups-api-usergrouproleresponse-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/users"
```

### POST `/v1/groups/{groupId}/users`

Joins a group

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |
| `Roblox-Place-Id` | header | `integer (int64)` | No | The place ID of the experience the player is in. |
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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

### GET `/v1/groups/{groupId}/users/{userId}/permissions`

Gets the permissions a user has in a group. Only available to group owner and RCC

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |
| `userId` | path | `integer (int64)` | Yes | The user id. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/users/{USERID}/permissions"
```

### GET `/v1/groups/configuration/metadata`

Gets Group configuration contextual information

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/configuration/metadata"
```

### GET `/v1/groups/metadata`

Gets Groups contextual information:
Max number of groups a user can be part of.
Current number of groups a user is a member of.
Whether to show/hide certain features based on device type.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/metadata"
```

### GET `/v1/groups/search`

Search for groups by keyword.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `keyword` | query | `string` | Yes | The keyword or phrase to use as the search parameter. |
| `prioritizeExactMatch` | query | `boolean` | No | Whether or not to prioritize the exact match for the keyword (optional, defaults to false). |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupSearchPageResponse`
- `400`: 2: Search term not appropriate for Roblox. 3: Search term was left empty. 4: Search terms can be 2 to 50 characters long.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/search?keyword={VALUE}"
```

### GET `/v1/groups/search/lookup`

Looks up groups by a name. Prioritizes an exact match as the first result.

Should only be used for direct lookups where a user is inputting a group name, shouldn't be used for search pages.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupName` | query | `string` | Yes | The group name. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Groups.GroupBasicResponse]`
- `400`: 1: Name is missing or has invalid characters.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Groups.GroupBasicResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Groups.GroupBasicResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-web-responses-groups-groupbasicresponse-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/search/lookup?groupName={VALUE}"
```

### GET `/v1/groups/search/metadata`

Get suggested groups and other miscellaneous information needed for the group/join page like flags

Although there is no reason for this to require an authenticated user right now, in the future,
we will use coco to return different suggested groups based upon that user's request context

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/search/metadata"
```

### GET `/v1/roles`

Gets the Roles by their ids.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `ids` | query | `array` | Yes | A list of role ids |
| `includePrivate` | query | `boolean` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupRoleDetailResponse]`
- `400`: 1: Ids could not be parsed from request. 2: Too many ids in request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupRoleDetailResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupRoleDetailResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-groups-api-grouproledetailresponse-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/roles?ids={VALUE}&includePrivate={VALUE}"
```

### GET `/v1/user/groups/pending`

Gets groups that the authenticated user has requested to join

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupDetailResponse]`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupDetailResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupDetailResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-groups-api-groupdetailresponse-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/user/groups/pending"
```

### GET `/v1/users/{userId}/friends/groups/roles`

Gets a list of all groups the specified users' friends are in.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.UserGroupMembershipResponse]`
- `400`: 3: The user is invalid or does not exist.
- `403`: 3: The user is invalid or does not exist.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.UserGroupMembershipResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.UserGroupMembershipResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-groups-api-usergroupmembershipresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "user": "...",
      "groups": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/users/{USERID}/friends/groups/roles"
```

### GET `/v1/users/{userId}/groups/primary/role`

Gets a user's primary group.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user id. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/users/{USERID}/groups/primary/role"
```

### GET `/v1/users/{userId}/groups/roles`

Gets a list of all group roles for groups the specified user is in.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user id. |
| `includeLocked` | query | `boolean` | No |  |
| `includeNotificationPreferences` | query | `boolean` | No |  |
| `discoveryType` | query | `integer (int32)` | No | Valid values: `0`, `1`, `2` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupMembershipDetailResponse]`
- `400`: 3: The user is invalid or does not exist.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupMembershipDetailResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupMembershipDetailResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-groups-api-groupmembershipdetailresponse-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/users/{USERID}/groups/roles"
```

### POST `/v1/groups/{groupId}/change-owner`

Changes the group owner to another user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/change-owner" \
  -H "Content-Type: application/json" \
  -d '{
  "userId": 0
}'
```

### POST `/v1/groups/{groupId}/claim-ownership`

Claims ownership of the group as the authenticated user

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/claim-ownership"
```

### POST `/v1/groups/{groupId}/community-tier/evaluate`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/community-tier/evaluate"
```

### POST `/v1/groups/{groupId}/deactivate`

Deactivates the group as its owner.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/deactivate"
```

### POST `/v1/groups/{groupId}/payouts/recurring`

Updates recurring payouts.

This endpoint will remove any recipients not sent in the request.
If a recipient in the request is not a valid member in the group they will not be added to the recurring payouts.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.PayoutRequest`

See [Roblox.Groups.Api.PayoutRequest](#roblox-groups-api-payoutrequest) in Models.

**Request example:**
```json
{
  "PayoutType": 1,
  "Recipients": [
    {
      "recipientId": "...",
      "recipientType": "...",
      "amount": "..."
    }
  ],
  "IdempotencyKey": "string",
  "WatermarkContributions": [
    {
      "balanceKey": "...",
      "amount": "..."
    }
  ]
}
```

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/payouts/recurring" \
  -H "Content-Type: application/json" \
  -d '{
  "PayoutType": 1,
  "Recipients": [
    {
      "recipientId": "...",
      "recipientType": "...",
      "amount": "..."
    }
  ],
  "IdempotencyKey": "string",
  "WatermarkContributions": [
    {
      "balanceKey": "...",
      "amount": "..."
    }
  ]
}'
```

### POST `/v1/groups/{groupId}/relationships/{groupRelationshipType}/{relatedGroupId}`

Create a group relationship.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |
| `groupRelationshipType` | path | `string` | Yes | The group relationship type, enemies or allies. |
| `relatedGroupId` | path | `integer (int64)` | Yes | The id of the group you want to create a relationship with. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}/{RELATEDGROUPID}"
```

### DELETE `/v1/groups/{groupId}/relationships/{groupRelationshipType}/{relatedGroupId}`

Deletes a group relationship.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |
| `groupRelationshipType` | path | `string` | Yes | The group relationship type, enemies or allies. |
| `relatedGroupId` | path | `integer (int64)` | Yes | The id of the group you want to delete the relationship with. |

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
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}/{RELATEDGROUPID}"
```

### POST `/v1/groups/{groupId}/relationships/{groupRelationshipType}/requests/{relatedGroupId}`

Accepts a group relationship request.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |
| `groupRelationshipType` | path | `string` | Yes | The group relationship type, enemies or allies, only allies are supported. |
| `relatedGroupId` | path | `integer (int64)` | Yes | The id of the group you want to accept the relationship request with. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}/requests/{RELATEDGROUPID}"
```

### DELETE `/v1/groups/{groupId}/relationships/{groupRelationshipType}/requests/{relatedGroupId}`

Declines a group relationship request.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |
| `groupRelationshipType` | path | `string` | Yes | The group relationship type, enemies or allies. |
| `relatedGroupId` | path | `integer (int64)` | Yes | The id of the group you want to accept the relationship request with. |

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
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/relationships/{GROUPRELATIONSHIPTYPE}/requests/{RELATEDGROUPID}"
```

### POST `/v1/groups/{groupId}/rolesets/create`

Creates new group roleset.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |

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
- `409`: 28: Migration in progress. Please try again in a moment.

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

### POST `/v1/groups/create`

Creates a new group.

This endpoint will charge Robux for the group purchase.
Accepts "icon" and "coverPhoto" in Files object. Defaults to first file if "icon" is not present.
Http status code 413 is thrown when the group icon file size is too large.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `name` | formData | `string` | No | The name of the group. |
| `description` | formData | `string` | No | The group description. |
| `publicGroup` | formData | `boolean` | No | Whether or not the group is open for anyone to join. |
| `buildersClubMembersOnly` | formData | `boolean` | No | Whether or not the group is only open to join for builders club members. |
| `Files` | formData | `file` | No |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/create"
```

### POST `/v1/groups/policies`

Gets group policy info used for compliance.

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/policies" \
  -H "Content-Type: application/json" \
  -d '{
  "groupIds": [
    0
  ]
}'
```

### POST `/v1/user/groups/primary`

Sets the authenticated user's primary group

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/user/groups/primary" \
  -H "Content-Type: application/json" \
  -d '{
  "groupId": 0
}'
```

### DELETE `/v1/user/groups/primary`

Removes the authenticated user's primary group

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/user/groups/primary"
```

### PATCH `/v1/groups/{groupId}/blocked-keywords/{keywordId}`

Updates an existing blocked keyword for the specified Group.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes |  |
| `keywordId` | path | `string` | Yes |  |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.UpdateBlockedKeywordRequest`

See [Roblox.Groups.Api.UpdateBlockedKeywordRequest](#roblox-groups-api-updateblockedkeywordrequest) in Models.

**Request example:**
```json
{
  "keyword": "string",
  "isPrivate": false
}
```

**Responses:**

- `200`: OK → `Roblox.Groups.Client.BlockedKeywordModel`
- `400`: 1: Group is invalid or does not exist. 3: KeywordId is invalid. 4: Invalid request. 12: The provided content was moderated.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 8: Insufficient permissions to complete the request. 9: User is invalid or does not exist. 10: Insufficient permissions to complete the request.
- `404`: 7: Not found.
- `405`: 31: Service is currently unavailable.
- `409`: 11: There was a conflict in your request.

**Response fields** (`Roblox.Groups.Client.BlockedKeywordModel`)

See [Roblox.Groups.Client.BlockedKeywordModel](#roblox-groups-client-blockedkeywordmodel) in Models.

**Response example:**
```json
{
  "id": "string",
  "keyword": "string",
  "createdBy": 0,
  "isPrivate": false,
  "createdAt": "2024-01-01T00:00:00Z",
  "updatedAt": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/blocked-keywords/{KEYWORDID}" \
  -H "Content-Type: application/json" \
  -d '{
  "keyword": "string",
  "isPrivate": false
}'
```

### DELETE `/v1/groups/{groupId}/blocked-keywords/{keywordId}`

Deletes a specific blocked keyword from the specified Group.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes |  |
| `keywordId` | path | `string` | Yes |  |

**Responses:**

- `200`: OK
- `400`: 1: Group is invalid or does not exist. 3: KeywordId is invalid. 4: Invalid request.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 9: User is invalid or does not exist. 10: Insufficient permissions to complete the request.
- `404`: 7: Not found.
- `405`: 31: Service is currently unavailable.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/blocked-keywords/{KEYWORDID}"
```

### PATCH `/v1/groups/{groupId}/description`

Updates the groups description

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The id of the group the user is in. |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/description" \
  -H "Content-Type: application/json" \
  -d '{
  "description": "string"
}'
```

### PATCH `/v1/groups/{groupId}/name`

Updates the group's name.

This endpoint will charge Robux for the group rename.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The id of the group the user is in. |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/name" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string"
}'
```

### PATCH `/v1/groups/{groupId}/notification-preference`

Updates the group's settings

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The id of the group the user is in. |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/notification-preference" \
  -H "Content-Type: application/json" \
  -d '{
  "notificationsEnabled": false,
  "type": 0
}'
```

### PATCH `/v1/groups/{groupId}/rolesets/{rolesetId}`

Updates existing group roleset.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |
| `rolesetId` | path | `integer (int64)` | Yes | The roleset Id. |

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
- `409`: 28: Migration in progress. Please try again in a moment.

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |
| `rolesetId` | path | `integer (int64)` | Yes | The roleset Id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 10: This group does not exist. 15: This role does not exist. 17: Cannot remove any more roles 18: Cannot delete this role.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 9: You do not have permissions to perform this action. 16: There are users in this role.
- `409`: 28: Migration in progress. Please try again in a moment.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/rolesets/{ROLESETID}"
```

### PATCH `/v1/groups/{groupId}/social-links/{socialLinkId}`

Updates a social link

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The id of the universe |
| `socialLinkId` | path | `integer (int64)` | Yes | The id of the social link being updated |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The id of the game you are editing, required for permissions checking |
| `socialLinkId` | path | `integer (int64)` | Yes | The id of the social link |

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
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/social-links/{SOCIALLINKID}"
```

### PATCH `/v1/groups/{groupId}/status`

Sets group status

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |

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

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/status" \
  -H "Content-Type: application/json" \
  -d '{
  "message": "string"
}'
```

### PATCH `/v1/groups/{groupId}/users/{userId}`

Updates a users role in a group.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The id of the group the user is in. |
| `userId` | path | `integer (int64)` | Yes | The id of the user being updated. |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/users/{USERID}" \
  -H "Content-Type: application/json" \
  -d '{
  "roleId": 0
}'
```

### DELETE `/v1/groups/{groupId}/users/{userId}`

Removes a user from a group

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group Id. |
| `userId` | path | `integer (int64)` | Yes | The Id of the user being removed. |

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
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/users/{USERID}"
```

### PATCH `/v1/groups/icon`

Updates the group icon.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | query | `integer (int64)` | Yes | The group Id. |
| `Files` | formData | `file` | No |  |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://groups.roblox.com/v1/groups/icon?groupId={VALUE}"
```

## Models

### Roblox.Groups.Api.BlockedKeywordPageResponse[Roblox.Groups.Client.BlockedKeywordModel]

ApiPageResponse for blocked keywords

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `totalActiveKeywordsCount` | `integer` | No | Total number of active keywords in the group |
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Client.BlockedKeywordModel[]` | No |  |

### Roblox.Groups.Api.ChangeOwnerRequest

A request model for changing the group owner.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | `integer` | No | The user id. |

### Roblox.Groups.Api.CommunityFeatureFreezeStatus

Response model representing the freeze status of a community feature.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `feature` | `string` | No | The community feature. |
| `isDisabled` | `boolean` | No | Whether the feature is currently disabled. |

### Roblox.Groups.Api.CreateBlockedKeywordsRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `keywords` | `string` | No |  |
| `isPrivate` | `boolean` | No |  |

### Roblox.Groups.Api.GetCommunityFeatureFreezesResponse

Response model for the community feature freezes endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `features` | `Roblox.Groups.Api.CommunityFeatureFreezeStatus[]` | No | The freeze status of each community feature. |

### Roblox.Groups.Api.GetGroupFeaturesResponse

Response model for the group features endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isLocked` | `boolean` | No | Whether the group is currently locked. |
| `features` | `Roblox.Groups.Api.GroupFeatureResponse[]` | No | The freeze status of each feature for the group. |

### Roblox.Groups.Api.GetSocialLinkResponse

A social link response from a create request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Groups.Api.SocialLinkResponse[]` | No |  |
| `socialLinksVerificationStatus` | `0 \| 1 \| 2 \| 3` | No |  |

### Roblox.Groups.Api.GroupAllRolesResponse

A group roles response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupId` | `integer` | No | The group id |
| `roles` | `Roblox.Groups.Api.GroupRoleResponse[]` | No | The roles in the group |

### Roblox.Groups.Api.GroupAuditLogPageResponse[Roblox.Groups.Api.Models.Response.GroupAuditLogResponseItem]

ApiPageResponse for group audit log

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Api.Models.Response.GroupAuditLogResponseItem[]` | No |  |

### Roblox.Groups.Api.GroupBanMemberResponse

A ban member from group response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `user` | `Roblox.Groups.Api.Models.Response.UserModel` | No |  |
| `actingUser` | `Roblox.Groups.Api.UserGroupRoleResponse` | No |  |
| `created` | `string` | No | The group ban's created time |

### Roblox.Groups.Api.GroupChannelPermissionsModel

A model for communication channel permissions.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `channelId` | `string` | No | Group Channel Id |
| `groupForumsPermissions` | `Roblox.Groups.Api.GroupForumsPermissionsModel` | No |  |

### Roblox.Groups.Api.GroupConfigurationDetailsResponse

A detailed group response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupId` | `integer` | No | The group id |
| `emblemId` | `integer` | No | The group emblem id |
| `coverPhotoId` | `integer` | No | The group cover photo id |

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

### Roblox.Groups.Api.GroupConfigurationResponse

A response model for group configuration

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `nameMaxLength` | `integer` | No | The maximum length of a group name |
| `descriptionMaxLength` | `integer` | No | The maximum length of a group description |
| `iconMaxFileSizeMb` | `integer` | No | The maximum file size of the group icon in megabytes |
| `coverPhotoMaxFileSizeMb` | `integer` | No | The maximum file size of the group cover photo in megabytes |
| `validCoverPhotoDimensions` | `string` | No | The valid dimensions of the group cover photo in CSV format |
| `cost` | `integer` | No | The cost of purchasing a group |
| `isUsingTwoStepWebviewComponent` | `boolean` | No | Should the frontend use the 2sv webview component (as opposed to the built-in 2sv pop up) |

### Roblox.Groups.Api.GroupContentModerationPermissionsModel

A model representing group content moderation permissions

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `manageKeywordBlockList` | `boolean` | No | Manage keyword block list permission |
| `viewKeywordBlockList` | `boolean` | No | View keyword block list permission |

### Roblox.Groups.Api.GroupDescriptionResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `newDescription` | `string` | No | The new description returned |

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

### Roblox.Groups.Api.GroupEconomyPermissionsModel

A model representing data about an Roblox.Platform.Membership.IUser

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `spendGroupFunds` | `boolean` | No | Spend group funds permission |
| `advertiseGroup` | `boolean` | No | Advertise group permission |
| `createItems` | `boolean` | No | Create items permission |
| `manageItems` | `boolean` | No | Manage items permission |
| `addGroupPlaces` | `boolean` | No | Add group places permission |
| `manageGroupGames` | `boolean` | No | Manage group games permission |
| `viewGroupPayouts` | `boolean` | No | Manage group games permission |
| `viewAnalytics` | `boolean` | No | Permission to view universe analytics from the creator dashboard. |

### Roblox.Groups.Api.GroupFeatureResponse

Response model representing the freeze status of a group feature.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `feature` | `string enum (6 values)` | No | The feature type. ['Payouts' = 0, 'ContentUpload' = 1, 'GroupOwnershipTransfer' = 2, 'GameOwnershipTransfer' = 3, 'ForumRead' = 4, 'ForumWrite' = 5] Values: Payouts, ContentUpload, GroupOwnershipTransfer, GameOwnershipTransfer, ForumRead, ForumWrite |
| `isFeatureBlocked` | `boolean` | No | Whether the feature is currently frozen. |
| `expiration` | `string` | No | The UTC time at which the moderator-force expires, allowing the freeze to be deactivated upon request. Only present when the feature is forced frozen. |

### Roblox.Groups.Api.GroupForumsPermissionsModel

A model representing group posts permissions

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `viewForums` | `boolean` | No | View forums permission |
| `manageCategories` | `boolean` | No | Manage categories permission |
| `createPosts` | `boolean` | No | Create posts permission |
| `removePosts` | `boolean` | No | Remove posts permission |
| `lockPosts` | `boolean` | No | Lock posts permission |
| `pinPosts` | `boolean` | No | Pin posts permission |
| `createComments` | `boolean` | No | Create comments permission |
| `removeComments` | `boolean` | No | Remove comments permission |
| `createBugReports` | `boolean` | No | Create bug reports (support ticket) permission. Only emitted when the permission is exposed (Roblox.Groups.Api.Properties.IGroupsApiSettings.ExposeCreateBugReportsPermission). |

### Roblox.Groups.Api.GroupJoinRequestResponse

Response model for a group join request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `requester` | `Roblox.Groups.Api.Models.Response.UserModel` | No |  |
| `created` | `string` | No | The DateTime the request was created |

### Roblox.Groups.Api.GroupManagementPermissionsModel

A model representing data about an Roblox.Platform.Membership.IUser

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `manageRelationships` | `boolean` | No | Manage group relationships permission |
| `manageClan` | `boolean` | No | Manage clan permission |
| `viewAuditLogs` | `boolean` | No | View audit logs permission |
| `bypassSlowmode` | `boolean` | No | Bypass slowmode permission. |
| `viewCommunityAnalytics` | `boolean` | No | View community analytics permission. |

### Roblox.Groups.Api.GroupMembershipDetailResponse

A group membership response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `group` | `Roblox.Groups.Api.GroupDetailResponse` | No |  |
| `role` | `Roblox.Groups.Api.GroupRoleResponse` | No |  |
| `isPrimaryGroup` | `boolean` | No | Whether the group is the user's Primary Group |
| `isNotificationsEnabled` | `boolean` | No | Whether the group notification preferences are enabled for the user |
| `notificationPreferences` | `Roblox.Groups.Api.GroupNotificationPreferenceData[]` | No |  |

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

### Roblox.Groups.Api.GroupMembershipPermissionsModel

A model representing data about an Roblox.Platform.Membership.IUser

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `changeRank` | `boolean` | No | Update a member's role |
| `inviteMembers` | `boolean` | No | Invite members to the group |
| `removeMembers` | `boolean` | No | Remove from group permission |
| `banMembers` | `boolean` | No | Ban from group permission |

### Roblox.Groups.Api.GroupNameChangeConfigurationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `cost` | `integer` | No | The cost of renaming a group |
| `cooldownInDays` | `integer` | No | The cooldown for group name changes in days |
| `ownershipCooldownInDays` | `integer` | No | The ownership cooldown for group name changes in days |

### Roblox.Groups.Api.GroupNotificationPreferenceData

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | `0 \| 1 \| 2 \| 3 \| 4` | No | ['AnnouncementCreatedNotification' = 0, 'ForumPostCreatedNotification' = 1, 'ForumCommentCreatedNotification' = 2, 'ForumCommentReplyCreatedNotification' = 3, 'ForumSubscriberNotification' = 4] |
| `enabled` | `boolean` | No |  |
| `name` | `string` | No |  |
| `description` | `string` | No |  |

### Roblox.Groups.Api.GroupOpenCloudPermissionsModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `useCloudAuthentication` | `boolean` | No | Permission to create and use API keys on the group's resources. |
| `administerCloudAuthentication` | `boolean` | No | Permission to administer all of the group's API keys. |

### Roblox.Groups.Api.GroupPayoutResponse

A group payout response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `user` | `Roblox.Groups.Api.Models.Response.UserModel` | No |  |
| `percentage` | `integer` | No | The group payout percentage for the user |

### Roblox.Groups.Api.GroupPayoutRestrictionResponse

Response model for Group Payout Restriction

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `canUseRecurringPayout` | `boolean` | No | Whether the group can use recurring payout feature. |
| `canUseOneTimePayout` | `boolean` | No | Whether the group can use one-time payout feature. |

### Roblox.Groups.Api.GroupPermissionsModel

A model for group permissions.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupPostsPermissions` | `Roblox.Groups.Api.GroupPostsPermissionsModel` | No |  |
| `groupForumsPermissions` | `Roblox.Groups.Api.GroupForumsPermissionsModel` | No |  |
| `groupContentModerationPermissions` | `Roblox.Groups.Api.GroupContentModerationPermissionsModel` | No |  |
| `groupMembershipPermissions` | `Roblox.Groups.Api.GroupMembershipPermissionsModel` | No |  |
| `groupManagementPermissions` | `Roblox.Groups.Api.GroupManagementPermissionsModel` | No |  |
| `groupEconomyPermissions` | `Roblox.Groups.Api.GroupEconomyPermissionsModel` | No |  |
| `groupOpenCloudPermissions` | `Roblox.Groups.Api.GroupOpenCloudPermissionsModel` | No |  |

### Roblox.Groups.Api.GroupPermissionsResponse

A group role's permissions response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupId` | `integer` | No | The group id |
| `role` | `Roblox.Groups.Api.GroupRoleResponse` | No |  |
| `permissions` | `Roblox.Groups.Api.GroupPermissionsModel` | No |  |

### Roblox.Groups.Api.GroupPoliciesResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groups` | `Roblox.Groups.Api.GroupPolicyResponse[]` | No |  |

### Roblox.Groups.Api.GroupPolicyRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupIds` | `integer[]` | No |  |

### Roblox.Groups.Api.GroupPolicyResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `canViewGroup` | `boolean` | No |  |
| `groupId` | `integer` | No |  |

### Roblox.Groups.Api.GroupPostsPermissionsModel

A model representing group posts permissions

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `viewStatus` | `boolean` | No | View status permission |
| `postToStatus` | `boolean` | No | Post to status permission |

### Roblox.Groups.Api.GroupRelationshipsResponse

A group relationships response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupId` | `integer` | No | The group id |
| `relationshipType` | `1 \| 2` | No | The group relationship type ['Allies' = 1, 'Enemies' = 2] |
| `totalGroupCount` | `integer` | No | The total number of groups for this relationship type |
| `relatedGroups` | `Roblox.Groups.Api.GroupDetailResponse[]` | No | The related or requested groups |
| `nextRowIndex` | `integer` | No | The index for the next page of related groups |

### Roblox.Groups.Api.GroupRoleDetailResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupId` | `integer` | No | The id of the group the role belongs to |
| `id` | `integer` | No | The role id |
| `name` | `string` | No | The role name |
| `description` | `string` | No | The role description |
| `rank` | `integer` | No | The role rank |
| `memberCount` | `integer` | No | The number of members in the role. |
| `isBase` | `boolean` | No | Whether or not the role is the base role for the group |
| `color` | `integer enum (17 values)` | No | The role color. ['Invalid' = 0, 'Blue' = 1, 'Green' = 2, 'Purple' = 3, 'Yellow' = 4, 'Orange' = 5, 'Red' = 6, 'Magenta' = 7, 'Teal' = 8, 'Turquoise' = 9, 'Rust' = 10, 'Pistachio' = 11, 'Midnight' = 12, 'Lavender' = 13, 'Pink' = 14, 'Crimson' = 15, 'Plum' = 16] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 |
| `isPrivate` | `boolean` | No | Whether the role is private (only visible to members with permission). Omitted from the response when false. |

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

### Roblox.Groups.Api.GroupSearchMetadataResponse

Response Model For Group Search Metadata Endpoint

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `SuggestedGroupKeywords` | `string[]` | No | Suggested Group Category translation keys |
| `ShowFriendsGroupsSort` | `boolean` | No | Whether or not the Friends' Groups sort should show for the authenticated user |

### Roblox.Groups.Api.GroupSearchPageResponse

ApiPageResponse for catalog search

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `keyword` | `string` | No | Keyword used for search query |
| `totalResults` | `integer` | No |  |
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Api.GroupSearchResponseItem[]` | No |  |

### Roblox.Groups.Api.GroupSearchResponseItem

A group search response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The group id |
| `name` | `string` | No | The group name |
| `description` | `string` | No | The group description |
| `memberCount` | `integer` | No | The number of members in the group |
| `previousName` | `string` | No | The previous name of the group |
| `publicEntryAllowed` | `boolean` | No | When true anyone can join the group. When false manual approval is required to join the group |
| `created` | `string` | No | When the group was created |
| `updated` | `string` | No | When the group was last updated |
| `hasVerifiedBadge` | `boolean` | No | The group's verified badge status |

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

### Roblox.Groups.Api.HasGroupFeaturesBlockedResponse

Response model for the features/status endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `hasFeaturesBlocked` | `boolean` | No | Whether the group has any active feature freezes. |

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

### Roblox.Groups.Api.MembersRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `UserIds` | `integer[]` | No | The user ids being either accepted or declined |

### Roblox.Groups.Api.Models.Request.CreateRoleSetRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The name of the roleset. |
| `description` | `string` | No | The description of the roleset. |
| `rank` | `integer` | No | The rank/positioning of the roleset. |
| `usingGroupFunds` | `boolean` | No | Setting to use group funds or not. |
| `isPrivate` | `boolean` | No | Optional. When true the role is only visible to members with permission to see private roles. Defaults to false (public). Only accessible to group owners. |

### Roblox.Groups.Api.Models.Request.UpdateRoleSetRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The name of the roleset. |
| `description` | `string` | No | The description of the roleset. |
| `rank` | `integer` | No | The rank/positioning of the roleset. |
| `color` | `integer` | No | Optional. The color of the roleset (GroupRoleSetColorType value, e.g. 0 = Invalid, 1 = Blue). When omitted, only name and description are updated and the existing color is left unchanged. When set, name, description, and color are updated via UpdateGroupRoleSetProperties. |
| `isPrivate` | `boolean` | No | Optional. When set, updates the visibility of the roleset. Only accessible to group owners. The base (guest) role cannot be made private. |

### Roblox.Groups.Api.Models.Response.GroupAuditLogResponseItem

A group audit log response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `actor` | `Roblox.Groups.Api.UserGroupRoleResponse` | No |  |
| `actionType` | `string` | No | The action type |
| `description` | `any` | No | Information on the action performed |
| `created` | `string` | No | Date the group action was performed |

### Roblox.Groups.Api.Models.Response.GroupNameHistoryResponseItem

A group name history response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The group name before the change |
| `created` | `string` | No | Date the name change was applied |

### Roblox.Groups.Api.Models.Response.UserModel

A model representing data about an Roblox.Platform.Membership.IUser

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `buildersClubMembershipType` | `0 \| 1 \| 2 \| 3 \| 4` | No | The user's builders club membership type |
| `hasVerifiedBadge` | `boolean` | No | The user's verified badge status. |
| `userId` | `integer` | No |  |
| `username` | `string` | No |  |
| `displayName` | `string` | No |  |

### Roblox.Groups.Api.OneTimePayoutResponse

Response model for one-time payout requests.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | `0 \| 1` | No | One-time payout status. ['NotHeld' = 0, 'Held' = 1] |

### Roblox.Groups.Api.PayoutRecipientRequest

A request model for paying out Robux.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `recipientId` | `integer` | No | The recipient id. |
| `recipientType` | `0 \| 1` | No | The recipient type. ['User' = 0, 'Group' = 1] |
| `amount` | `integer` | No | The amount to payout. |

### Roblox.Groups.Api.PayoutRequest

Multi-payout request information.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `PayoutType` | `1 \| 2` | No | The Roblox.Groups.Api.PayoutType. ['FixedAmount' = 1, 'Percentage' = 2] |
| `Recipients` | `Roblox.Groups.Api.PayoutRecipientRequest[]` | No | The recipients of the payouts. |
| `IdempotencyKey` | `string` | No | The idempotency key of the payout request. |
| `WatermarkContributions` | `Roblox.Groups.Api.WatermarkContributionRequest[]` | No | Optional watermark contributions for DevEx attribution tracking. |

### Roblox.Groups.Api.PostGroupStatusRequest

A request model for setting the authenticated user's primary group.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | `string` | No | The message to set the group status to. |

### Roblox.Groups.Api.PrimaryGroupRequest

A request model for setting the authenticated user's primary group.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupId` | `integer` | No | The group id. |

### Roblox.Groups.Api.RecurringPayoutsConfigurationResponse

A response model for recurring payout configuration

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `maxPayoutPartners` | `integer` | No | The maximum number of recurring payout partners |

### Roblox.Groups.Api.RelationshipsRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `GroupIds` | `integer[]` | No | The group ids being either accepted or declined |

### Roblox.Groups.Api.RoleConfigurationResponse

A response model for role configuration

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `nameMaxLength` | `integer` | No | The maximum length of a role name |
| `descriptionMaxLength` | `integer` | No | The maximum length of a role description |
| `limit` | `integer` | No | The maximum number of roles in a group |
| `cost` | `integer` | No | The cost of purchasing a role |
| `minRank` | `integer` | No | The minimum rank a role can have |
| `maxRank` | `integer` | No | The maximum rank a role can have |

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

### Roblox.Groups.Api.ShoutResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `body` | `string` | No | The shout's message |
| `poster` | `Roblox.Groups.Api.Models.Response.UserModel` | No |  |
| `created` | `string` | No | The shout's created time |
| `updated` | `string` | No | The shout's last updated time |

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

### Roblox.Groups.Api.UpdateBlockedKeywordRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `keyword` | `string` | No |  |
| `isPrivate` | `boolean` | No |  |

### Roblox.Groups.Api.UpdateGroupDescriptionRequest

A request model for setting a description for the group

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | `string` | No | The group description being set. |

### Roblox.Groups.Api.UpdateGroupNameRequest

A request model for setting a name for the group

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The group name being set. |

### Roblox.Groups.Api.UpdateGroupNameResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `newName` | `string` | No | The new description returned |

### Roblox.Groups.Api.UpdateGroupNotificationPreferenceRequest

A request model for updating a group's notification preference.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `notificationsEnabled` | `boolean` | No | Whether the user wants to receive notifications from the group. |
| `type` | `0 \| 1 \| 2 \| 3 \| 4` | No | ['AnnouncementCreatedNotification' = 0, 'ForumPostCreatedNotification' = 1, 'ForumCommentCreatedNotification' = 2, 'ForumCommentReplyCreatedNotification' = 3, 'ForumSubscriberNotification' = 4] |

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

### Roblox.Groups.Api.UpdatePermissionsRequest

A request model for updating a group's roleset's permissions.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `permissions` | `object` | No | The permission-value pairs to be updated. |

### Roblox.Groups.Api.UpdateUserRoleRequest

A request model for setting a users role in a group.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `roleId` | `integer` | No | The role in the group the user should be put into. |

### Roblox.Groups.Api.UserGroupMembershipResponse

A users group membership response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `user` | `Roblox.Groups.Api.Models.Response.UserModel` | No |  |
| `groups` | `Roblox.Groups.Api.GroupMembershipDetailResponse[]` | No | The list of group memberships |

### Roblox.Groups.Api.UserGroupRoleResponse

A user group role response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `user` | `Roblox.Groups.Api.Models.Response.UserModel` | No |  |
| `role` | `Roblox.Groups.Api.GroupRoleResponse` | No |  |

### Roblox.Groups.Api.WatermarkContributionRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `balanceKey` | `Standard \| O18Boosted` | No | ['Standard' = 1, 'O18Boosted' = 2] |
| `amount` | `integer` | No |  |

### Roblox.Groups.Client.BlockedKeywordModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No |  |
| `keyword` | `string` | No |  |
| `createdBy` | `integer` | No |  |
| `isPrivate` | `boolean` | No |  |
| `createdAt` | `string` | No |  |
| `updatedAt` | `string` | No |  |

### Roblox.Groups.Client.CommunityTierInfoResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupId` | `integer` | Yes |  |
| `currentTier` | `integer` | Yes |  |
| `previousTier` | `integer` | No |  |
| `tierUpdatedTime` | `string` | No |  |
| `lastEvaluatedTime` | `string` | No |  |
| `requirements` | `Roblox.Groups.Client.TierRequirement[]` | No |  |
| `capabilities` | `Roblox.Groups.Client.TierCapabilities` | No |  |

### Roblox.Groups.Client.CreateBlockedKeywordsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `createdKeywords` | `Roblox.Groups.Client.BlockedKeywordModel[]` | No |  |
| `hadModeratedKeywords` | `boolean` | No |  |
| `hadDuplicateKeywords` | `boolean` | No |  |

### Roblox.Groups.Client.EmoteModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No |  |
| `name` | `string` | No |  |

### Roblox.Groups.Client.EmoteSetModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No |  |
| `name` | `string` | No |  |
| `emotes` | `Roblox.Groups.Client.EmoteModel[]` | No |  |

### Roblox.Groups.Client.GetGroupEmoteSetsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `emoteSets` | `Roblox.Groups.Client.EmoteSetModel[]` | No |  |

### Roblox.Groups.Client.GroupFeaturedContentResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groupId` | `integer` | No |  |
| `contentType` | `string` | No |  |
| `contentId` | `string` | No |  |

### Roblox.Groups.Client.TierCapabilities

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isEligibleForUnrestrictedMessages` | `boolean` | Yes |  |

### Roblox.Groups.Client.TierEvaluationResultResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tierInfo` | `Roblox.Groups.Client.CommunityTierInfoResponse` | Yes |  |
| `passedSignals` | `string[]` | Yes |  |
| `requirements` | `Roblox.Groups.Client.TierRequirement[]` | No |  |

### Roblox.Groups.Client.TierRequirement

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `key` | `1 \| 2 \| 3 \| 4 \| 5` | Yes | ['OwnerModerationStatusOk' = 1, 'OwnerAgeEstimationVerified' = 2, 'OwnerIdVerified' = 3, 'OwnerTwoStepVerified' = 4, 'CommunityMeetsPlayerRequirement' = 5] |
| `satisfied` | `boolean` | Yes |  |

### Roblox.Web.Responses.Groups.GroupBasicResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `memberCount` | `integer` | No |  |
| `hasVerifiedBadge` | `boolean` | No |  |

### Roblox.Web.Responses.Groups.GroupResponseV2

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `description` | `string` | No |  |
| `owner` | `Roblox.Web.Responses.RelatedEntityTypeResponse[Roblox.Web.Responses.Groups.GroupOwnerType]` | No |  |
| `memberCount` | `integer` | No |  |
| `created` | `string` | No |  |
| `hasVerifiedBadge` | `boolean` | No |  |

### Roblox.Web.Responses.RelatedEntityTypeResponse[Roblox.Web.Responses.Groups.GroupOwnerType]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `type` | `0` | No | ['User' = 0] |
| `name` | `string` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupDetailResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Groups.Api.GroupDetailResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupMembershipDetailResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Groups.Api.GroupMembershipDetailResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupPayoutResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Groups.Api.GroupPayoutResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupPermissionsResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Groups.Api.GroupPermissionsResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.GroupRoleDetailResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Groups.Api.GroupRoleDetailResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Groups.Api.UserGroupMembershipResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Groups.Api.UserGroupMembershipResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Groups.GroupBasicResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Web.Responses.Groups.GroupBasicResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.GroupBanMemberResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Api.GroupBanMemberResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.GroupJoinRequestResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Api.GroupJoinRequestResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.Models.Response.GroupNameHistoryResponseItem]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Api.Models.Response.GroupNameHistoryResponseItem[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.Models.Response.UserModel]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Api.Models.Response.UserModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Groups.Api.UserGroupRoleResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Api.UserGroupRoleResponse[]` | No |  |