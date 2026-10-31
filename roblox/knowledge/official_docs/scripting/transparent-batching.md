---
title: "Transparent batching"
url: /docs/en-us/scripting/transparent-batching
last_updated: 2026-10-30T19:55:56Z
description: "Learn how to optimize concurrent API calls by letting the engine automatically batch them into fewer HTTP requests."
---

# Transparent batching

Some APIs are capable of **transparent batching**, meaning the engine can automatically combine multiple concurrent API calls into fewer HTTP requests behind the scenes.

You don't need to use a different API or supply different arguments. Simply start multiple calls concurrently instead of waiting for each one to finish before starting the next.

## Why use transparent batching

Many Roblox APIs communicate with backend services over HTTP and are subject to rate limits. Making many requests in a short period of time can increase latency and may cause some requests to be throttled or fail.

Transparent batching reduces the number of HTTP requests sent by the engine. Instead of sending a separate HTTP request for every API call, the engine groups nearby concurrent calls into fewer network requests automatically. This improves performance for your players and reduces the likelihood of hitting rate limits.

For example, if your code performs 20 product lookups at the same time, transparent batching can combine those calls into just one or two HTTP requests instead of sending 20 separate requests.

## Use concurrent calls

Transparent batching only works when multiple calls to the same supported API are started concurrently. If each call waits for the previous one to finish, the engine sends a separate HTTP request for each call instead of batching them together.

Instead of starting calls one at a time:

```lua
-- Serial: slow, one HTTP request at a time
local MarketplaceService = game:GetService("MarketplaceService")

for _, productId in productIds do
    local info = MarketplaceService:GetProductInfoAsync(productId, Enum.InfoType.Product)
    print(info.Name)
end
```

Start them concurrently:

```lua
-- Concurrent: the engine combines these into fewer HTTP requests
local MarketplaceService = game:GetService("MarketplaceService")

local results = {}
local remaining = #productIds

local function fetch(productId)
    local success, info = pcall(function()
        return MarketplaceService:GetProductInfoAsync(productId, Enum.InfoType.Product)
    end)

    if success then
        results[productId] = info
    else
        warn("Failed:", productId, info)
    end

    remaining -= 1
end

for _, productId in productIds do
    task.spawn(fetch, productId)
end

while remaining > 0 do
    task.wait()
end
```

Both examples produce the same results, but the concurrent version allows the engine to automatically batch multiple API calls into fewer HTTP requests, making the operation faster and reducing the likelihood of hitting rate limits.

## Supported methods

The following methods currently support transparent batching:

| Service | Method |
| --- | --- |
| `Class.MarketplaceService` | `Class.MarketplaceService:GetProductInfoAsync()\|GetProductInfoAsync` (`Enum.InfoType.Product`, `Enum.InfoType.GamePass`, and `Enum.InfoType.Bundle`) |
| `Class.MarketplaceService` | `Class.MarketplaceService:UserOwnsGamePassAsync()\|UserOwnsGamePassAsync` |
| `Class.AvatarEditorService` | `Class.AvatarEditorService:GetItemDetailsAsync()\|GetItemDetailsAsync` |
| `Class.AssetService` | `Class.AssetService:GetBundleDetailsAsync()\|GetBundleDetailsAsync` |

## Best practices

- **Start calls close together.** The engine batches calls that begin within a short time window. Calls started much later are sent in a separate batch.
- **Use `pcall()`.** Network requests can fail. Wrapping calls in `pcall()` prevents a single failure from stopping the entire operation.
- **Let the engine manage batching.** Don't try to manually group requests or optimize batch sizes. The engine automatically chooses the most efficient batching strategy.
- **Take advantage of caching.** Repeated requests for the same data return from cache whenever possible instead of making another network request.
