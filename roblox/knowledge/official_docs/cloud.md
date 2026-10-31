---
title: "Cloud API reference"
url: /docs/en-us/cloud
last_updated: 2026-10-30T19:55:39Z
description: "Get comprehensive API reference documentation for Open Cloud."
---

# Cloud API reference

With Open Cloud, you can access Roblox resources through standard [REST](https://en.wikipedia.org/wiki/REST) APIs, which lets you build everything from command line automation tools to complex web apps. You can update games, restart servers, work with your data stores and memory stores, manage user restrictions, list inventory items, and much, much more.

This reference is broken into two sections:

- A [section that separates endpoints by feature](/docs/en-us/cloud/reference/features/accounts.md) (Avatars, Game Passes, Users, etc.)
- A [section that separates endpoints by domain](/docs/en-us/cloud/reference/domains/apis.md) (base URL)

**Both sections** contain the full list of available API endpoints. We recommend the [features section](/docs/en-us/cloud/reference/features/accounts.md) since it helps consolidate endpoints by use case, but experienced Open Cloud developers might prefer to browse by domain.

- Whenever possible, use endpoints that support [API keys](/docs/en-us/auth/api-keys.md) or [OAuth 2.0](/docs/en-us/auth/oauth2-overview.md) for authentication. They have strong stability guarantees and receive regular updates.
- Legacy APIs use cookie-based authentication, can incorporate breaking changes without notice, and have minimal stability guarantees. We don't recommend them for production applications.

> **Info:** Roblox also offers [webhooks](/docs/en-us/webhooks/webhook-notifications.md), which can notify your applications when certain events occur, such as refunds or changes to subscriptions.
## Get started with Open Cloud

1. Set up authentication for your application. See the documentation for how to use [API keys](/docs/en-us/auth/api-keys.md) or [OAuth 2.0](/docs/en-us/auth/oauth2-overview.md). API keys are the easiest way to get started.
2. Test API calls using tools like [Postman](https://www.postman.com) with [OpenAPI descriptions](/docs/en-us/reference/openapi.md) or the [OAuth 2.0 sample app](/docs/en-us/auth/oauth2-sample.md).
3. Review the [resource guides](/docs/en-us/guides.md) for end-to-end walkthroughs of using certain APIs.
4. Explore the left navigation for the full list of features, [common API patterns](/docs/en-us/reference/patterns.md), [types](/docs/en-us/reference/types.md), and [error codes](/docs/en-us/reference/errors.md).

## Make requests within games

`Class.HttpService` lets you make HTTP requests to a subset of the Open Cloud endpoints. For more information, see [In-game HTTP requests](/docs/en-us/cloud-services/http-service.md).
