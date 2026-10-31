---
title: "In-game HTTP requests"
url: /docs/en-us/cloud-services/http-service
last_updated: 2026-10-30T19:55:40Z
description: "Use HttpService to send HTTP requests to third-party web services and Open Cloud."
---

# In-game HTTP requests

You can use `Class.HttpService` to send generic HTTP requests to third-party web services for use cases like analytics, data storage, or error logging. `Class.HttpService` also supports certain Open Cloud endpoints.

## Enable HTTP requests

The `Class.HttpService:GetAsync()`, `Class.HttpService:PostAsync()`, and `Class.HttpService:RequestAsync()` methods aren't enabled by default. To send requests, you must **Allow HTTP Requests** under **File** ⟩ **Experience Settings** ⟩ **Security** in Studio.

## Use in plugins

You can use `Class.HttpService` in Studio plugins to check for updates, download content, or other business logic. The first time a plugin attempts to use the service, the user might be prompted to give the plugin permission to communicate with the particular web address. Users can accept, deny, and revoke these permissions at any time through the **Plugin Management** window.

Plugins can also communicate with other software running on the same computer through the `localhost` and `127.0.0.1` hosts. By running programs compatible with such plugins, you can extend the functionality of your plugin beyond the normal capabilities of Studio, such as interacting with your computer's file system. Beware that such software must be distributed separately from the plugin itself and can pose security risks.

## Use with Open Cloud

`Class.HttpService` can currently call a subset of the Open Cloud endpoints. You can call these endpoints the same way that you'd call any other endpoint via `HttpService`. The only difference is that you must include an Open Cloud API key in the request:

1. [Create an Open Cloud API key](/docs/en-us/cloud/auth/api-keys.md#create-api-keys).
2. [Save the API key to your secrets store](/docs/en-us/cloud-services/secrets.md#add-secrets).
3. Make the request.

The following code sample demonstrates how to update a user's group membership from within a game:

```lua
local HttpService = game:GetService("HttpService")

local groupId = "your_group_id"
local membershipId = "your_membership_id"
local roleId = "your_role_id"

local function request()
	local response = HttpService:RequestAsync({
		Url = \`https://apis.roblox.com/cloud/v2/groups/{groupId}/memberships/{membershipId}\`,
		Method = "PATCH",
		Headers = {
			["Content-Type"] = "application/json", -- When sending JSON, set this!
			["x-api-key"] = HttpService:GetSecret("APIKey"), -- Set in Creator Hub
		},
		Body = HttpService:JSONEncode({ role = \`groups/{groupId}/roles/{roleId}\` }),
	})

	if response.Success then
		print("The response was successful:", response.StatusCode, response.StatusMessage)
	else
		print("The response returned an error:", response.StatusCode, response.StatusMessage)
	end
	print("Response body:\n", response.Body)
	print("Response headers:\n", HttpService:JSONEncode(response.Headers))
end

-- Wrap the function in pcall() for safety
local success, errorMessage = pcall(request)
if not success then
	print("The HTTP request failed to send:", errorMessage)
end
```

### Supported Open Cloud endpoints

The following endpoints are supported. Due to current limitations on `Class.HttpService`, the `..` string is not allowed in URL path parameters to Roblox domains. This means, for example, that data stores and entries containing this string are currently inaccessible from `Class.HttpService`.

#### Assets

- [GetAsset](/docs/en-us/cloud/features/assets.md#/default/Assets_GetAsset)
- [ListAssetVersions](/docs/en-us/cloud/features/assets.md#/default/listAssetVersions)
- [GetAssetVersion](/docs/en-us/cloud/features/assets.md#/default/Assets_GetAssetVersion)

#### Bans and blocks

- [ListUserRestrictions (Place)](/docs/en-us/cloud/features/bans-and-blocks.md#/UserRestriction/Cloud_ListUserRestrictions__Using_Universes)
- [GetUserRestriction (Place)](/docs/en-us/cloud/features/bans-and-blocks.md#/UserRestriction/Cloud_GetUserRestriction__Using_Universes_Places)
- [UpdateUserRestriction (Place)](/docs/en-us/cloud/features/bans-and-blocks.md#/UserRestriction/Cloud_UpdateUserRestriction__Using_Universes_Places)
- [ListUserRestrictions (Universe)](/docs/en-us/cloud/features/bans-and-blocks.md#/UserRestriction/Cloud_ListUserRestrictions)
- [GetUserRestriction (Universe)](/docs/cloud/features/bans-and-blocks#/UserRestriction/Cloud_GetUserRestriction__Using_Universes)
- [UpdateUserRestriction (Universe)](/docs/en-us/cloud/features/bans-and-blocks.md#/UserRestriction/Cloud_UpdateUserRestriction__Using_Universes)
- [ListUserRestrictionLogs (Universe)](/docs/en-us/cloud/features/bans-and-blocks.md#/UserRestriction/Cloud_ListUserRestrictionLogs)

#### Configs

- [GetConfigRepositoryValues](/docs/en-us/cloud/reference/features/configs.md#CreatorConfigsPublicApi_GetConfigRepositoryValues)
- [GetConfigRepositoryDraft](/docs/en-us/cloud/reference/features/configs.md#CreatorConfigsPublicApi_GetConfigRepositoryDraft)
- [UpdateDraft](/docs/en-us/cloud/reference/features/configs.md#CreatorConfigsPublicApi_UpdateDraft)
- [DeleteDraft](/docs/en-us/cloud/reference/features/configs.md#CreatorConfigsPublicApi_DeleteDraft)
- [OverwriteDraft](/docs/en-us/cloud/reference/features/configs.md#CreatorConfigsPublicApi_OverwriteDraft)
- [GetConfigRepositoryFull](/docs/en-us/cloud/reference/features/configs.md#CreatorConfigsPublicApi_GetConfigRepositoryFull)
- [PublishDraft](/docs/en-us/cloud/reference/features/configs.md#CreatorConfigsPublicApi_PublishDraft)
- [ListRevisions](/docs/en-us/cloud/reference/features/configs.md#CreatorConfigsPublicApi_ListRevisions)
- [RestoreRevision](/docs/en-us/cloud/reference/features/configs.md#CreatorConfigsPublicApi_RestoreRevision)

#### Creator Store

- [CreateCreatorStoreProduct](/docs/en-us/cloud/features/creator-store.md#/CreatorStoreProduct/Cloud_CreateCreatorStoreProduct)
- [GetCreatorStoreProduct](/docs/en-us/cloud/features/creator-store.md#/CreatorStoreProduct/Cloud_GetCreatorStoreProduct)
- [UpdateCreatorStoreProduct](/docs/en-us/cloud/features/creator-store.md#/CreatorStoreProduct/Cloud_UpdateCreatorStoreProduct)
- [CreatorStoreAssetsSearch](/docs/en-us/cloud/features/creator-store.md#toolbox-service)

#### Developer products

- [CreateDeveloperProduct](/docs/en-us/cloud/reference/features/developer-products.md#DeveloperProducts_CreateDeveloperProductV2)
- [UpdateDeveloperProduct](/docs/en-us/cloud/reference/features/developer-products.md#DeveloperProducts_UpdateDeveloperProductV2)
- [GetDeveloperProductConfig](/docs/en-us/cloud/reference/features/developer-products.md#DeveloperProducts_GetDeveloperProductConfigV2)
- [ListDeveloperProductConfigsByUniverse](/docs/en-us/cloud/reference/features/developer-products.md#DeveloperProducts_ListDeveloperProductConfigsByUniverseV2)

#### Game passes

- [CreateGamePass](/docs/en-us/cloud/reference/features/game-passes.md#GamePasses_CreateGamePass)
- [UpdateGamePass](/docs/en-us/cloud/reference/features/game-passes.md#GamePasses_UpdateGamePass)
- [GetGamePassConfig](/docs/en-us/cloud/reference/features/game-passes.md#GamePasses_GetGamePassConfig)
- [ListGamePassConfigsByUniverse](/docs/en-us/cloud/reference/features/game-passes.md#GamePasses_ListGamePassConfigsByUniverse)

#### Data and memory stores

Data stores:

- [ListDataStores](/docs/en-us/cloud/reference/DataStore.md#Cloud_ListDataStores)
- [SnapshotDataStores](/docs/en-us/cloud/features/storage.md#/DataStore/Cloud_SnapshotDataStores)
- [ListDataStoreEntries](/docs/en-us/cloud/reference/DataStoreEntry.md#Cloud_ListDataStoreEntries__Using_Universes)
- [CreateDataStoreEntry](/docs/en-us/cloud/reference/DataStoreEntry.md#Cloud_CreateDataStoreEntry__Using_Universes)
- [GetDataStoreEntry](/docs/en-us/cloud/reference/DataStoreEntry.md#Cloud_GetDataStoreEntry__Using_Universes_DataStores)
- [DeleteDataStoreEntry](/docs/en-us/cloud/reference/DataStoreEntry.md#Cloud_DeleteDataStoreEntry__Using_Universes_DataStores)
- [UpdateDataStoreEntry](/docs/en-us/cloud/reference/DataStoreEntry.md#Cloud_UpdateDataStoreEntry__Using_Universes_DataStores)
- [IncrementDataStoreEntry](/docs/en-us/cloud/reference/DataStoreEntry.md#Cloud_IncrementDataStoreEntry__Using_Universes_DataStores)
- [ListDataStoreEntryRevisions](/docs/en-us/cloud/features/storage.md#/DataStoreEntry/Cloud_ListDataStoreEntryRevisions__Using_Universes_DataStores)
- [ListDataStoreEntries (With Scope)](/docs/en-us/cloud/features/storage.md#/DataStoreEntry/Cloud_ListDataStoreEntries__Using_Universes_DataStores)
- [CreateDataStoreEntry (With Scope)](/docs/en-us/cloud/features/storage.md#/DataStoreEntry/Cloud_CreateDataStoreEntry__Using_Universes_DataStores)
- [GetDataStoreEntry (With Scope)](/docs/en-us/cloud/features/storage.md#/DataStoreEntry/Cloud_GetDataStoreEntry__Using_Universes_DataStores_Scopes)
- [DeleteDataStoreEntry (With Scope)](/docs/en-us/cloud/features/storage.md#/DataStoreEntry/Cloud_DeleteDataStoreEntry__Using_Universes_DataStores_Scopes)
- [UpdateDataStoreEntry (With Scope)](/docs/en-us/cloud/features/storage.md#/DataStoreEntry/Cloud_UpdateDataStoreEntry__Using_Universes_DataStores_Scopes)
- [IncrementDataStoreEntry (With Scope)](/docs/en-us/cloud/features/storage.md#/DataStoreEntry/Cloud_IncrementDataStoreEntry__Using_Universes_DataStores_Scopes)
- [ListDataStoreEntryRevisions (With Scope)](/docs/en-us/cloud/features/storage.md#/DataStoreEntry/Cloud_ListDataStoreEntryRevisions__Using_Universes_DataStores_Scopes)

Memory stores:

- [CreateMemoryStoreQueueItem](/docs/en-us/cloud/features/storage.md#/MemoryStoreQueueItem/Cloud_CreateMemoryStoreQueueItem)
- [DiscardMemoryStoreQueueItems](/docs/en-us/cloud/features/storage.md#/MemoryStoreQueueItem/Cloud_DiscardMemoryStoreQueueItems)
- [ReadMemoryStoreQueueItems](/docs/en-us/cloud/features/storage.md#/MemoryStoreQueueItem/Cloud_ReadMemoryStoreQueueItems)
- [ListMemoryStoreSortedMapItems](/docs/en-us/cloud/features/storage.md#/MemoryStoreSortedMapItem/Cloud_ListMemoryStoreSortedMapItems)
- [CreateMemoryStoreSortedMapItem](/docs/en-us/cloud/features/storage.md#/MemoryStoreSortedMapItem/Cloud_CreateMemoryStoreSortedMapItem)
- [GetMemoryStoreSortedMapItem](/docs/en-us/cloud/features/storage.md#/MemoryStoreSortedMapItem/Cloud_GetMemoryStoreSortedMapItem)
- [DeleteMemoryStoreSortedMapItem](/docs/en-us/cloud/features/storage.md#/MemoryStoreSortedMapItem/Cloud_DeleteMemoryStoreSortedMapItem)
- [UpdateMemoryStoreSortedMapItem](/docs/en-us/cloud/features/storage.md#/MemoryStoreSortedMapItem/Cloud_UpdateMemoryStoreSortedMapItem)
- [FlushMemoryStore](/docs/en-us/cloud/features/storage.md#/MemoryStore/Cloud_FlushMemoryStore)

Ordered data stores:

- [ListOrderedDataStoreEntries](/docs/en-us/cloud/features/storage.md#/OrderedDataStoreEntry/Cloud_ListOrderedDataStoreEntries)
- [CreateOrderedDataStoreEntry](/docs/en-us/cloud/features/storage.md#/OrderedDataStoreEntry/Cloud_CreateOrderedDataStoreEntry)
- [GetOrderedDataStoreEntry](/docs/en-us/cloud/features/storage.md#/OrderedDataStoreEntry/Cloud_GetOrderedDataStoreEntry)
- [DeleteOrderedDataStoreEntry](/docs/en-us/cloud/features/storage.md#/OrderedDataStoreEntry/Cloud_DeleteOrderedDataStoreEntry)
- [UpdateOrderedDataStoreEntry](/docs/en-us/cloud/features/storage.md#/OrderedDataStoreEntry/Cloud_UpdateOrderedDataStoreEntry)
- [IncrementOrderedDataStoreEntry](/docs/en-us/cloud/features/storage.md#/OrderedDataStoreEntry/Cloud_IncrementOrderedDataStoreEntry)

#### Groups

- [GetGroup](/docs/en-us/cloud/reference/Group.md#Cloud_GetGroup)
- [ListGroupJoinRequests](/docs/en-us/cloud/reference/GroupJoinRequest.md#Cloud_ListGroupJoinRequests)
- [AcceptGroupJoinRequest](/docs/en-us/cloud/reference/GroupJoinRequest.md#Cloud_AcceptGroupJoinRequest)
- [DeclineGroupJoinRequest](/docs/en-us/cloud/reference/GroupJoinRequest.md#Cloud_DeclineGroupJoinRequest)
- [ListGroupMemberships](/docs/en-us/cloud/reference/GroupMembership.md#Cloud_ListGroupMemberships)
- [UpdateGroupMembership](/docs/en-us/cloud/reference/GroupMembership.md#Cloud_UpdateGroupMembership)
- [ListGroupRoles](/docs/en-us/cloud/reference/GroupRole.md#Cloud_ListGroupRoles)
- [GetGroupRole](/docs/en-us/cloud/reference/GroupRole.md#Cloud_GetGroupRole)
- [GetGroupShout](/docs/en-us/cloud/reference/GroupShout.md#Cloud_GetGroupShout)

#### Inventories

- [ListInventoryItems](/docs/en-us/cloud/reference/InventoryItem.md#Cloud_ListInventoryItems)

#### Luau execution

- [CreateLuauExecutionSessionTaskBinaryInput](/docs/en-us/cloud/features/luau-execution.md#/LuauExecutionSessionTaskBinaryInput/Cloud_CreateLuauExecutionSessionTaskBinaryInput)
- [CreateLuauExecutionSessionTask](/docs/en-us/cloud/features/luau-execution.md#/LuauExecutionSessionTask/Cloud_CreateLuauExecutionSessionTask__Using_Universes)
- [CreateLuauExecutionSessionTask (with version)](/docs/en-us/cloud/features/luau-execution.md#/LuauExecutionSessionTask/Cloud_CreateLuauExecutionSessionTask__Using_Universes_Places)
- [GetLuauExecutionSessionTask](/docs/en-us/cloud/features/luau-execution.md#/LuauExecutionSessionTask/Cloud_GetLuauExecutionSessionTask)
- [ListLuauExecutionSessionTaskLogs](/docs/en-us/cloud/features/luau-execution.md#/LuauExecutionSessionTaskLog/Cloud_ListLuauExecutionSessionTaskLogs)

#### Notifications

- [CreateUserNotification](/docs/en-us/cloud/features/notifications.md#/UserNotification/Cloud_CreateUserNotification)

#### Places

- [GetPlace](/docs/en-us/cloud/features/places.md#/Place/Cloud_GetPlace)
- [UpdatePlace](/docs/en-us/cloud/features/places.md#/Place/Cloud_UpdatePlace)
- [GetInstance](/docs/en-us/cloud/features/places.md#/Instance/Cloud_GetInstance)
- [UpdateInstance](/docs/en-us/cloud/features/places.md#/Instance/Cloud_UpdateInstance)

#### Universes

- [UpdateUniverse](/docs/en-us/cloud/features/universes.md#/Universe/Cloud_UpdateUniverse)
- [GetUniverse](/docs/en-us/cloud/features/universes.md#/Universe/Cloud_GetUniverse)
- [PublishUniverseMessage](/docs/en-us/cloud/features/universes.md#/Universe/Cloud_PublishUniverseMessage)
- [RestartUniverseServers](/docs/en-us/cloud/features/universes.md#/Universe/Cloud_RestartUniverseServers)

#### Users

- [GetUser](/docs/en-us/cloud/features/users.md#/User/Cloud_GetUser)
- [GenerateUserThumbnail](/docs/en-us/cloud/features/users.md#/User/Cloud_GenerateUserThumbnail)

## Limitations

- Only the `x-api-key` and `content-type` headers are allowed.
- The `x-api-key` header must be a `Datatype.Secret`. See [Secrets stores](/docs/en-us/cloud-services/secrets.md).
- The `".."` string is not allowed in URL path parameters.
- Only the HTTPS protocol is supported.
- You cannot use port `1194` or any port below `1024`, except `80` and `443`. If you try to use a blocked port, you receive either a `403 Forbidden` or `ERR_ACCESS_DENIED` error.

## Rate limits

For each Roblox game server, there is a limit of 2500 Open Cloud requests per minute. Exceeding this can cause request-sending methods to stall for around 30 seconds. Your `Global.LuaGlobals.pcall()` may also fail with a message of `Number of Open Cloud requests exceeded limit`.

- Open Cloud requests **do not** consume the same overall limit of 500 HTTP requests per minute enforced on all other requests.
- Each endpoint has its own limit per API key owner (can be a user or a group) that is enforced no matter where the calls come from (`Class.HttpService`, the web, etc.).

For detailed information about Open Cloud rate limits, authentication-based rate limiting, and best practices, see [Rate Limits](/docs/en-us/cloud/reference/rate-limits.md).

## Best practices

To optimize your `Class.HttpService` usage and avoid exceeding the limits, apply the following best practices:

- **Handle errors gracefully**. Web requests can fail for many reasons. Use `Global.LuaGlobals.pcall()` and have a plan for when requests fail. Furthermore, strictly validate and sanitize all received data from external APIs, ensuring correct data where you can.
- Use [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) to stay below limits. If a request returns a recoverable error, instead of immediately retrying, wait for two seconds, then four, eights, etc. between attempts. This helps limit congestion and improves the chance of a successful request by giving the endpoint time to "cool off."
- Aggregate and send data in bulk. When possible, it's recommended to let your server collect all necessary data in order to send one HTTP request, rather than multiple small requests. For example, if you are sending an HTTP request for every player in your server, check if the API has a bulk/batch endpoint and, if so, collect the information from all players and send it all in one request. In some cases you may have to use `Class.HttpService:RequestAsync()` to include data in the body of the request.
- **Use HTTP/2 endpoints**. HTTP/2 provides significant performance benefits through features such as header compression and request/response multiplexing over a single connection. `Class.HttpService` automatically uses HTTP/2 when available. Note that the HTTP/2 specification requires all header names to be sent in lowercase.

## Observability

The **Observability Dashboard** provides insights and analytics for monitoring and troubleshooting your `Class.HttpService` usage. The dashboard features two primary charts: **Request Count** which tracks the volume of `Class.HttpService` requests from your game, and **Response Time** which measures the latency for endpoints to respond.

The available dimensions for filtering and breakdown are defined as follows:

### Request Type

- `GET`
- `POST`
- `PUT`
- `PATCH`
- `DELETE`
- `Other` (for non-specified request types)

### Status

- Success (HTTP 1xx and 2xx status codes)
- Redirect (HTTP 3xx status codes)
- 400 (Bad Request)
- 401 (Unauthorized)
- 403 (Forbidden)
- 404 (Not Found)
- 429 (Too Many Requests)
- 500 (Internal Server Error)
- 503 (Service Unavailable)
- ExternalError (any other non-specified error codes returned from the external service)
- InternalError (an issue returned from `Class.HttpService` within Roblox)

The **Response Time** chart is not correlated with status data. If you select "Status" as a breakdown or filter, this chart will not display data.

## Additional considerations

- Requests should provide a secure form of authentication, such as a pre-shared secret key, so that bad actors cannot pose as one of your Roblox servers.
- Be aware of the general capacity and rate-limiting policies of the web servers to which requests are being sent.
