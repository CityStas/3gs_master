---
title: "Choose between cloud services"
url: /docs/en-us/cloud-services/data-stores-vs-memory-stores
last_updated: 2026-10-30T19:55:40Z
description: "When to use standard data stores, ordered data stores, memory stores, secrets stores, and configs."
---

# Choose between cloud services

Roblox offers several options for data storage. Each storage option has pros and cons and is appropriate for different use cases. This table summarizes the available options and provides the closest points of comparison from standard web services.

| Service | Persistence | Scope | In-game access | Cloud comparison |
| --- | --- | --- | --- | --- |
| **Data stores** | Permanent | Cross-server | Read-write | NoSQL database |
| **Memory stores** | 45 day maximum | Cross-server | Read-write | In-memory cache |
| **Configs** | Permanent | Cross-server | Read-only | App configuration and feature flags |
| **Secrets stores** | Permanent | Cross-server | Read-only | Secrets management |
| **Luau in-memory** | Session duration | Single server | Read-write | Server RAM |

> **Success:** Within Roblox games, cloud services are only accessible from server scripts.
## When to use data stores

`Class.DataStoreService` stores long-term data that needs to last between sessions, such as user progress or inventory items. Data stores are consistent per game, so every server for every place within a game can access and change the same data. There are two types of data stores: standard and ordered.

- **Standard data stores** can store data like numbers, strings, and tables that don't need to be ranked or sorted. They store data as key-value pairs; each entry is stored under a key that is unique within its data store and that you can retrieve, update, or delete. For more information, see [Data stores](/docs/en-us/cloud-services/data-stores.md).
- **Ordered data stores** can only store numbers. Each entry is stored under a key that is unique within its data store and that you can retrieve, update, or delete. You can rank and sort this data numerically and retrieve it in ascending or descending order based on stored numerical values. For more information, see [Ordered data stores](/docs/en-us/cloud-services/data-stores.md#ordered-data-stores).

 | **Standard data stores** | **Ordered data stores**
| **Data type** | Numbers, strings, booleans, and tables. | Only numbers. |
| --- | --- | --- |
| **Common use cases** | User progress, inventory items, and game settings. | All-time, persistent ranking systems and leaderboards. Unlike leaderboards in memory stores, this leaderboard data is permanent. |
| **Past version backup** | Automatically manages previous versions of your data for 30 days. | Does not manage previous versions of your data. |

> **Info:** If you want to add granular permission control to your data stores and access them outside of Studio or Roblox servers, use the [Open Cloud APIs for data stores](/docs/en-us/cloud/reference/features/storage.md).
## When to use memory stores

`Class.MemoryStoreService` is a high throughput and low latency service that stores temporary data that needs to be updated or accessed frequently, such as global leaderboards or matchmaking queues. With memory stores, every server for every place within a game can access and change the same data quickly and frequently. Data in a memory store expires after a certain period of time, up to 45 days.

If you need to quickly read (not write to) a small number of values across all servers, [configs](#when-to-use-configs) are the better choice. Memory stores are not as performant as configs when frequently accessing a single key or partition.

Although memory stores store temporary data, they also support permanent features like a global marketplace. The marketplace is permanent, but the items for sale inside it have an expiration date.

 | **Memory stores**
| **Data type** | Numbers, strings, booleans, and tables that don't need to persist for over 45 days. |
| --- | --- |
| **Common use cases** | Skill-based matchmaking, match states for multiplayer games. |
| Daily and monthly leaderboards. |

## When to use configs

[Configs](/docs/en-us/production/configs.md) let you update in-game variables in real time without restarting servers. They are ideal for feature flags and any in-game values you hope to tune over time or [experiment](/docs/en-us/production/experiments.md) with.

- Configs are read-only from within a game—you modify them on Creator Hub or in Roblox Studio—so they don't serve the same use cases as data stores and memory stores.
- Changes to configs deploy over the course of five minutes; changes to data and memory stores are more instantaneous.

 | **Configs**
| **Data type** | Numbers, strings, booleans, and JSON objects. |
| --- | --- |
| **Common use cases** | Enabling a new dungeon, disabling a limited-time game mode, starting a holiday event. |
| Enemy health, weapon damage, item prices, game multipliers, welcome messages. |

## When to use secrets stores

Use the [secrets store](/docs/en-us/cloud-services/secrets.md) for your game to store any API keys, passwords, and access tokens that you use to authenticate with external services. Storing these values in a data store presents unnecessary security risks.

 | **Secrets stores**
| **Data type** | Strings. |
| --- | --- |
| **Common use cases** | API keys, passwords, and access tokens for analytics or music services. |

## When to use in-memory storage in Luau

Use in-memory storage in Luau to store temporary data that needs to be accessed with minimal latency and without the cost of making external service calls. This storage is built into Luau and requires no setup.

 | **In-memory storage in Luau**
| **Data type** | Numbers, strings, booleans, and tables. |
| --- | --- |
| **Common use cases** | Data that is only relevant to a single server session and doesn't need to be persisted, such as status effects or temporary points that reset when the user leaves the game. |
| Values that change frequently, like counters, timers, state flags, or a health bar. |
| Data that drives game logic, which needs to be accessible instantly, like temporary variables or an enemy's current health. |
