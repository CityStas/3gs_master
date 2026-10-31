---
name: Secret
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Stores secret non-printable content."
---

# Secret

Stores secret non-printable content.

**Type:** datatype

## Description

The [Secret](/docs/reference/engine/datatypes/Secret.md) data type stores the secret content returned by
[HttpService:GetSecret()](/docs/reference/engine/classes/HttpService.md). It cannot be printed or logged, but can be
modified using built-in functions:

## Code Samples

**Secret**

Demonstrates the `Secret` datatype.

```lua
local HttpService = game:GetService("HttpService")

local mySiteApiKey = HttpService:GetSecret("my_site")
local url = "https://apis.mysite.com?apiKey="
local urlWithKey = mySiteApiKey:AddPrefix(url)
local params = "&request=join&user=myname"
local resultingUrl = urlWithKey:AddSuffix(params)
```

## Methods

### Secret:AddPrefix

**Signature:** `Secret:AddPrefix(prefix: string): Secret`

Returns a secret formed by concatenating the supplied string to the secret
content, for example prepending `"Bearer"` to the API key.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `prefix` | `string` |  | The string to prepend to the secret content. |

**Returns:** `Secret` — A new Secret with the prefix prepended to the original secret value.

**Secret AddPrefix**

Demonstrates `Secret.AddPrefix`.

```lua
local HttpService = game:GetService("HttpService")

local secret = HttpService:GetSecret("yelp")
local authHeader = secret:AddPrefix("Bearer ")
```

### Secret:AddSuffix

**Signature:** `Secret:AddSuffix(suffix: string): Secret`

Returns a secret formed by concatenating the original secret and the
supplied string parameter. Useful when creating a URL containing a key and
query parameters.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `suffix` | `string` |  | The string to append to the secret content. |

**Returns:** `Secret` — A new Secret with the suffix appended to the original secret value.

**Secret AddSuffix**

Demonstrates `Secret.AddSuffix`.

```lua
local HttpService = game:GetService("HttpService")

local googleMapsApiKey = HttpService:GetSecret("google_map")

local baseUrl = "https://maps.googleapis.com/maps/api/distancematrix/json?key="
local queryParams = "&destinations=" .. destination .. "&origins=" .. origin .. "&departure_time=now&units=imperial"
local authedUrl = googleMapsApiKey:AddPrefix(baseUrl)
local queryUrl = authedUrl:AddSuffix(queryParams)
```