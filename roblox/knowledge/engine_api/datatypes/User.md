---
name: User
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Represents a user's domain-scoped identity within a specific domain."
---

# User

Represents a user's domain-scoped identity within a specific domain.

**Type:** datatype

## Description

The **User** data type represents a user's scoped identity within a specific
domain, such as an experience or OAuth application. It encapsulates a domain
user ID alongside the domain metadata that uniquely identifies that user
within that domain.

Unlike a numeric user ID alone, a [User](/docs/reference/engine/datatypes/User.md) value carries its domain
context, making it unambiguous across experiences and apps. It is the standard
identifier for referencing users in new experience code and is available from
[Player.User](/docs/reference/engine/classes/Player.md).

#### Domain User IDs

User IDs on Roblox are **domain-scoped**: a single account has a unique domain
user ID for each experience or app it interacts with. This ensures that user
activity in one experience cannot be correlated with activity in another by a
third party using the user ID alone.

A domain user ID is an integer that is unique within a given domain
(identified by [DomainType](/docs/reference/engine/enums/DomainType.md) and domain ID). Domain user IDs are
guaranteed not to collide with existing global user IDs.

#### Serialization

[User](/docs/reference/engine/datatypes/User.md) supports round-trip string serialization via
[ToString()](/docs/reference/engine/datatypes/User.md) and
[fromString()](/docs/reference/engine/datatypes/User.md). A [User](/docs/reference/engine/datatypes/User.md) serialized with
`ToString()` and deserialized with `fromString()` produces an identical value.
The encoded string is stable, URL-safe, and compact. Use it when persisting or
transmitting user identity across systems.

#### Users vs. Players

A [User](/docs/reference/engine/datatypes/User.md) represents persistent identity, not live server presence. It
can reference any account in the domain, whether or not that user is currently
connected. Use [Player](/docs/reference/engine/classes/Player.md) when you need the in-server instance.

## Code Samples

**User Serialize Roundtrip**

Demonstrates the `User` datatype.

```lua
-- Serialize
local encoded = player.User:ToString()

-- Deserialize
local user = User.fromString(encoded)
```

## Constructors

### User.fromId

**Signature:** `User.fromId(domainUserId: int64)`

Creates a new [User](/docs/reference/engine/datatypes/User.md) from the given domain user ID, using the
current experience as the domain. The ID must be a valid domain user ID
(above the global user ID range).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `domainUserId` | `int64` |  | The domain-scoped user ID to construct the User from. Must be above the global user ID range. |

**User fromId**

Demonstrates `User.fromId`.

```lua
local user = User.fromId(domainUserId)
print(user.Id)         -- domainUserId
print(user.DomainType) -- Enum.DomainType.EXPERIENCE
```

### User.fromString

**Signature:** `User.fromString(userString: string)`

Deserializes a [User](/docs/reference/engine/datatypes/User.md) from a string previously produced by
[ToString()](/docs/reference/engine/datatypes/User.md).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userString` | `string` |  | A string previously produced by [ToString()](/docs/reference/engine/datatypes/User.md). |

**User fromString**

Demonstrates `User.fromString`.

```lua
local encoded = player.User:ToString()
local restored = User.fromString(encoded)
print(restored.Id == player.User.Id) -- true
```

## Properties

### User.Id

**Type:** `int64`

The domain user ID for this user within the associated domain. This is an
integer that uniquely identifies the user within the specific domain type
and domain ID combination.

### User.DomainType

**Type:** `DomainType`

The [DomainType](/docs/reference/engine/enums/DomainType.md) that identifies the kind of domain this domain user
ID belongs to. Currently supported values are [DomainType.EXPERIENCE](/docs/reference/engine/enums/DomainType.md)
and [DomainType.OAUTH](/docs/reference/engine/enums/DomainType.md).

### User.DomainId

**Type:** `int64`

The identifier of the specific domain instance that this user ID is scoped
to. For [DomainType.EXPERIENCE](/docs/reference/engine/enums/DomainType.md), this is the universe ID. For
[DomainType.OAUTH](/docs/reference/engine/enums/DomainType.md), this is the application ID.

## Methods

### User:ToString

**Signature:** `User:ToString(): string`

Serializes this [User](/docs/reference/engine/datatypes/User.md) into a string that encodes the domain
type, domain ID, and domain user ID. The result is stable, URL-safe, and
compact. Use this when storing or transmitting user identity.

The string can be converted back to a [User](/docs/reference/engine/datatypes/User.md) via
[fromString()](/docs/reference/engine/datatypes/User.md).

**Returns:** `string` — A stable, URL-safe encoded string representing the domain type, domain
ID, and domain user ID that can be deserialized back with
[fromString()](/docs/reference/engine/datatypes/User.md).

**User ToString For Storage**

Demonstrates `User.ToString`.

```lua
local encoded = player.User:ToString()
-- Store in a data store, send over a remote, etc.
DataStore:SetAsync("last_visitor", encoded)
```