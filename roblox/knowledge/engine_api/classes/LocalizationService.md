---
name: LocalizationService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "Handles automated translation."
---

# Class: LocalizationService

> Handles automated translation.

## Description

LocalizationService is the service responsible for handling automated
translation.

It is used as a storage for [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) objects used by
automatic text replacement.

LocalizationService will only use its child LocalizationTables for automatic
text replacement unless [GuiBase2d.RootLocalizationTable](/docs/reference/engine/classes/GuiBase2d.md) is specified
on a GUI object or its ancestors.

## Properties

### Property: LocalizationService.RobloxLocaleId

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Localization",
  "capabilities": [
    "Basic"
  ]
}
```

This property shows the locale ID used for the localization of core and
internal features such as [CoreGui](/docs/reference/engine/classes/CoreGui.md). Returns a string with the two
letter code (for example, `en-us`) for the locale.

### Property: LocalizationService.SystemLocaleId

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Localization",
  "capabilities": [
    "Basic"
  ]
}
```

This property shows the locale ID that the local player has set for their
operating system.

This will return a string with the two letter code (for example, "en-us")
for the locale.

See also [Player.LocaleId](/docs/reference/engine/classes/Player.md), the locale ID that a user has set for
their Roblox account which is used for localizing in-experience content.
This will be a different value when that player's account locale isn't
supported for localizing Roblox UI content.

## Methods

### Method: LocalizationService:GetCorescriptLocalizations

**Signature:** `LocalizationService:GetCorescriptLocalizations(): Instances`

Returns a list of [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) objects used for localizing
core scripts.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `Instances` — A list of [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) objects used for localizing
CoreScripts.

### Method: LocalizationService:GetCountryRegionForPlayerAsync

**Signature:** `LocalizationService:GetCountryRegionForPlayerAsync(player: Instance): string`

Returns a country/region code string according to player's client IP
geolocation. The supported country/region codes are as follows:

| Code | Country/Region |
| --- | --- |
| XX | Unknown Country |
| US | United States |
| GB | United Kingdom |
| CA | Canada |
| AF | Afghanistan |
| AX | Aland Islands |
| AL | Albania |
| DZ | Algeria |
| AS | American Samoa |
| AD | Andorra |
| AO | Angola |
| AI | Anguilla |
| AQ | Antarctica |
| AG | Antigua and Barbuda |
| AR | Argentina |
| AM | Armenia |
| AW | Aruba |
| AU | Australia |
| AT | Austria |
| AZ | Azerbaijan |
| BS | Bahamas |
| BH | Bahrain |
| BD | Bangladesh |
| BB | Barbados |
| BY | Belarus |
| BE | Belgium |
| BZ | Belize |
| BJ | Benin |
| BM | Bermuda |
| BT | Bhutan |
| BO | Bolivia |
| BQ | Bonaire, Saint Eustatius and Saba |
| BA | Bosnia and Herzegovina |
| BW | Botswana |
| BV | Bouvet Island |
| BR | Brazil |
| IO | British Indian Ocean Territory |
| BN | Brunei Darussalam |
| BG | Bulgaria |
| BF | Burkina Faso |
| BI | Burundi |
| KH | Cambodia |
| CM | Cameroon |
| CV | Cape Verde |
| KY | Cayman Islands |
| CF | Central African Republic |
| TD | Chad |
| CL | Chile |
| CN | China |
| CX | Christmas Island |
| CC | Cocos Islands |
| CO | Colombia |
| KM | Comoros |
| CG | Congo |
| CD | Congo (DRC) |
| CK | Cook Islands |
| CR | Costa Rica |
| CI | Ivory Coast |
| HR | Croatia |
| CW | Curaçao |
| CY | Cyprus |
| CZ | Czech Republic |
| DK | Denmark |
| DJ | Djibouti |
| DM | Dominica |
| DO | Dominican Republic |
| EC | Ecuador |
| EG | Egypt |
| SV | El Salvador |
| GQ | Equatorial Guinea |
| ER | Eritrea |
| EE | Estonia |
| ET | Ethiopia |
| FK | Falkland Islands (Malvinas) |
| FO | Faroe Islands |
| FJ | Fiji |
| FI | Finland |
| FR | France |
| GF | French Guiana |
| PF | French Polynesia |
| TF | French Southern Territories |
| GA | Gabon |
| GM | Gambia |
| GE | Georgia |
| DE | Germany |

| Code | Country/Region |
| --- | --- |
| GH | Ghana |
| GI | Gibraltar |
| GR | Greece |
| GL | Greenland |
| GD | Grenada |
| GP | Guadeloupe |
| GU | Guam |
| GT | Guatemala |
| GG | Guernsey |
| GN | Guinea |
| GW | Guinea-Bissau |
| GY | Guyana |
| HT | Haiti |
| HM | Heard Island and the McDonald Islands |
| VA | Holy See |
| HN | Honduras |
| HK | Hong Kong |
| HU | Hungary |
| IS | Iceland |
| IN | India |
| ID | Indonesia |
| IQ | Iraq |
| IE | Ireland |
| IM | Isle of Man |
| IL | Israel |
| IT | Italy |
| JM | Jamaica |
| JP | Japan |
| JE | Jersey |
| JO | Jordan |
| KZ | Kazakhstan |
| KE | Kenya |
| KI | Kiribati |
| KR | Korea |
| KW | Kuwait |
| KG | Kyrgyzstan |
| LA | Laos |
| LV | Latvia |
| LB | Lebanon |
| LS | Lesotho |
| LR | Liberia |
| LY | Libya |
| LI | Liechtenstein |
| LT | Lithuania |
| LU | Luxembourg |
| MO | Macao |
| MK | Macedonia |
| MG | Madagascar |
| MW | Malawi |
| MY | Malaysia |
| MV | Maldives |
| ML | Mali |
| MT | Malta |
| MH | Marshall Islands |
| MQ | Martinique |
| MR | Mauritania |
| MU | Mauritius |
| YT | Mayotte |
| MX | Mexico |
| FM | Micronesia |
| MD | Moldova |
| MC | Monaco |
| MN | Mongolia |
| ME | Montenegro |
| MS | Montserrat |
| MA | Morocco |
| MZ | Mozambique |
| MM | Myanmar |
| NA | Namibia |
| NR | Nauru |
| NP | Nepal |
| NL | Netherlands |
| AN | Netherlands Antilles |
| NC | New Caledonia |
| NZ | New Zealand |
| NI | Nicaragua |
| NE | Niger |
| NG | Nigeria |
| NU | Niue |
| NF | Norfolk Island |
| MP | Northern Mariana Islands |
| NO | Norway |
| OM | Oman |

| Code | Country/Region |
| --- | --- |
| PK | Pakistan |
| PW | Palau |
| PS | Palestine |
| PA | Panama |
| PG | Papua New Guinea |
| PY | Paraguay |
| PE | Peru |
| PH | Philippines |
| PN | Pitcairn Islands |
| PL | Poland |
| PT | Portugal |
| PR | Puerto Rico |
| QA | Qatar |
| RE | Reunion |
| RO | Romania |
| RU | Russian Federation |
| RW | Rwanda |
| BL | Saint Barthelemy |
| SH | Saint Helena, Ascension and Tristan da Cunha |
| KN | Saint Kitts and Nevis |
| LC | Saint Lucia |
| MF | Saint Martin |
| PM | Saint Pierre and Miquelon |
| VC | Saint Vincent and the Grenadines |
| WS | Samoa |
| SM | San Marino |
| ST | Sao Tome and Principe |
| SA | Saudi Arabia |
| SN | Senegal |
| RS | Serbia |
| SC | Seychelles |
| SL | Sierra Leone |
| SG | Singapore |
| SX | Sint Maarten |
| SK | Slovakia |
| SI | Slovenia |
| SB | Solomon Islands |
| SO | Somalia |
| ZA | South Africa |
| GS | South Georgia and the South Sandwich Islands |
| SS | South Sudan |
| ES | Spain |
| LK | Sri Lanka |
| SR | Suriname |
| SJ | Svalbard and Jan Mayen |
| SZ | Swaziland |
| SE | Sweden |
| CH | Switzerland |
| TW | Taiwan |
| TJ | Tajikistan |
| TZ | Tanzania |
| TH | Thailand |
| TL | Timor-Leste |
| TG | Togo |
| TK | Tokelau |
| TO | Tonga |
| TT | Trinidad and Tobago |
| TN | Tunisia |
| TR | Türkiye (Turkey) |
| TM | Turkmenistan |
| TC | Turks and Caicos Islands |
| TV | Tuvalu |
| UG | Uganda |
| UA | Ukraine |
| AE | United Arab Emirates |
| UM | United States Minor Outlying Islands |
| UY | Uruguay |
| UZ | Uzbekistan |
| VU | Vanuatu |
| VE | Venezuela |
| VN | Vietnam |
| VG | Virgin Islands (British) |
| VI | Virgin Islands (US) |
| WF | Wallis and Futuna |
| EH | Western Sahara |
| YE | Yemen |
| ZM | Zambia |
| ZW | Zimbabwe |
| CU | Cuba |
| IR | Iran |
| SY | Syria |
| KP | North Korea |

See also:

- [PolicyService:GetPolicyInfoForPlayerAsync()](/docs/reference/engine/classes/PolicyService.md), returns policy
  information about a player which is based on geolocation, age group and
  platform

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The player that you are getting country/region information for. |

**Returns:** `string` — A string indicating the country/region code of a player.

**Getting Country/Region Code for a Player**

This code sample gets the country/region code for a local player and prints
"Hello, friend from Canada!" if the player's client IP geolocation is Canada.

```lua
local LocalizationService = game:GetService("LocalizationService")
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local result, code = pcall(LocalizationService.GetCountryRegionForPlayerAsync, LocalizationService, player)

if result and code == "CA" then
	print("Hello, friend from Canada!")
else
	print("GetCountryRegionForPlayerAsync failed: " .. code)
end
```

### Method: LocalizationService:GetTableEntries

**Signature:** `LocalizationService:GetTableEntries(instance?: Instance): Array`

Returns an `Array`, where each element of the returned `Array` is itself
an `Array` of entries in the same format as described in
[LocalizationTable:GetEntries()](/docs/reference/engine/classes/LocalizationTable.md). The order of the elements in the
returned `Array` is the same order that the
[LocalizationTables](/docs/reference/engine/classes/LocalizationTable.md) will be searched through to
attempt automated localization for the provided [Instance](/docs/reference/engine/classes/Instance.md). The
entry elements within a particular [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) are returned
in an unspecified order.

This function returns entries regardless of whether the object is a
[GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md) with [GuiBase2d.AutoLocalize](/docs/reference/engine/classes/GuiBase2d.md) enabled. An object
that is a [GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md) will not actually be automatically localized
unless [GuiBase2d.AutoLocalize](/docs/reference/engine/classes/GuiBase2d.md) is enabled.

The ordering of the tables is as follows:

- First, it looks for the earliest [GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md) ancestor of the
  object (including the provided object) that has a
  [GuiBase2d.RootLocalizationTable](/docs/reference/engine/classes/GuiBase2d.md). Tables then append in the same
  order as described in [GuiBase2d.RootLocalizationTable](/docs/reference/engine/classes/GuiBase2d.md) by going
  up through the [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) ancestors of that
  [GuiBase2d.RootLocalizationTable](/docs/reference/engine/classes/GuiBase2d.md). If no such
  [GuiBase2d.RootLocalizationTable](/docs/reference/engine/classes/GuiBase2d.md) is found, no tables append in
  this step. If `instance` is `nil`, no tables append in this step.
- Next, tables from the [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) hierarchy under
  [LocalizationService](/docs/reference/engine/classes/LocalizationService.md) append. For each child
  [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) of [LocalizationService](/docs/reference/engine/classes/LocalizationService.md), it appends
  tables going up from the lowest descendant [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) of
  the tables parented to the service, all the way up to the children of
  the service. If there are no children of [LocalizationService](/docs/reference/engine/classes/LocalizationService.md)
  that are [LocalizationTables](/docs/reference/engine/classes/LocalizationTable.md), then no tables
  append in this step.
- Finally, the cloud [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) appends to the array. If
  there is no cloud [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md), or the cloud
  [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) has not yet loaded, then no table appends in
  this step.

This function does not yield. It will not wait until the cloud
[LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) has loaded.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `instance` | `Instance` | `nil` | The [Instance](/docs/reference/engine/classes/Instance.md) for which to retrieve the ordered localization table entries. If nil, only entries from the [LocalizationService](/docs/reference/engine/classes/LocalizationService.md) hierarchy and the cloud [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) are returned. |

**Returns:** `Array` — An array of arrays, where each array is in the same format as
described in [LocalizationTable:GetEntries()](/docs/reference/engine/classes/LocalizationTable.md).

### Method: LocalizationService:GetTranslatorForLocaleAsync

**Signature:** `LocalizationService:GetTranslatorForLocaleAsync(locale: string): Instance`

This function takes a locale code as an argument and yields until the
cloud [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) for that locale has been loaded, if
available. It then returns a [Translator](/docs/reference/engine/classes/Translator.md) object which can be used
to perform translations for that locale if any are available. The entries
used for localization are the entries provided by the
[LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) hierarchy under [LocalizationService](/docs/reference/engine/classes/LocalizationService.md) as
well as the cloud table (if available). This will be the same set of
entries returned by [LocalizationService:GetTableEntries(nil)](/docs/reference/engine/classes/LocalizationService.md).

This function can error and thus should be wrapped in a `pcall()`.

See also:

- [LocalizationService:GetTranslatorForPlayer()](/docs/reference/engine/classes/LocalizationService.md) gets the translator
  corresponding to the locale of the provided player. This function is
  deprecated and should not be used in new work.
- [LocalizationService:GetTranslatorForPlayerAsync()](/docs/reference/engine/classes/LocalizationService.md) yields until
  the cloud [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) for the locale of the provided
  player has loaded and then gets the translator corresponding to the
  locale of the provided player.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `locale` | `string` |  | A Roblox supported language or locale code. |

**Returns:** `Instance` — The [Translator](/docs/reference/engine/classes/Translator.md) instance for the specified locale.

**Getting and Using a Translator for a Locale**

This code sample attempts to retrieve a `Translator` object for the locale
"fr" (French).

[LocalizationService:GetTranslatorForLocaleAsync()](/docs/reference/engine/classes/LocalizationService.md) is wrapped in a
pcall because it may error. If it does not error and returns a Translator,
prints "Hello in French:" followed by the French translation of "Hello
World!". If the function errors, it prints "GetTranslatorForLocaleAsync
failed:" followed by the error message.

```lua
local LocalizationService = game:GetService("LocalizationService")

local textLabel = script.Parent

local success, translator = pcall(function()
	return LocalizationService:GetTranslatorForLocaleAsync("fr")
end)

if success then
	local result = translator:Translate(textLabel, "Hello World!")
	print("Hello in French: " .. result)
else
	print("GetTranslatorForLocaleAsync failed: " .. translator)
end
```

### Method: LocalizationService:GetTranslatorForPlayerAsync

**Signature:** `LocalizationService:GetTranslatorForPlayerAsync(player: Instance): Instance`

This function takes a player as an argument and yields until the cloud
[LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) for that player's locale has been loaded, if
available. It then returns a [Translator](/docs/reference/engine/classes/Translator.md) object which can be used
to perform translations for that locale if any are available. The entries
used for localization are the entries provided by the
[LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) hierarchy under [LocalizationService](/docs/reference/engine/classes/LocalizationService.md) as
well as the cloud table (if available). This will be the same set of
entries returned by [LocalizationService:GetTableEntries(nil)](/docs/reference/engine/classes/LocalizationService.md).

This function can error and thus should be wrapped in a `pcall()`.

See also:

- [LocalizationService:GetTranslatorForPlayer()](/docs/reference/engine/classes/LocalizationService.md), same functionality
  as this function except that it does not yield and does not wait until
  the cloud [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) for the player's locale has been
  loaded. This function is deprecated and should not be used in new work.
- [LocalizationService:GetTranslatorForLocaleAsync()](/docs/reference/engine/classes/LocalizationService.md), returns a
  Translator to be used for translations using the provided locale.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The [Player](/docs/reference/engine/classes/Player.md) that you are getting the [Translator](/docs/reference/engine/classes/Translator.md) for. |

**Returns:** `Instance` — The [Translator](/docs/reference/engine/classes/Translator.md) instance for the specified locale.

**Getting and Using a Translator for a Player**

This code sample attempts to retrieve a `Translator` object for the local
player. [LocalizationService:GetTranslatorForPlayerAsync()](/docs/reference/engine/classes/LocalizationService.md) is wrapped
in a pcall because it may error. If it does not error and returns a
Translator, it translates and prints "Hello World!" in the player's language.
If the function errors, it prints "GetTranslatorForLocaleAsync failed:"
followed by the error message.

[LocalizationService:GetTranslatorForPlayer()](/docs/reference/engine/classes/LocalizationService.md) can also be used if you'd
like to get the player's translator without yielding until the function
returns.

```lua
local LocalizationService = game:GetService("LocalizationService")
local Players = game:GetService("Players")

local textLabel = script.Parent

local success, translator = pcall(function()
	return LocalizationService:GetTranslatorForPlayerAsync(Players.LocalPlayer)
end)

if success then
	local result = translator:Translate(textLabel, "Hello World!")
	print(result)
else
	print("GetTranslatorForPlayerAsync failed: " .. translator)
end
```

### Method: LocalizationService:GetTranslatorForPlayer

**Signature:** `LocalizationService:GetTranslatorForPlayer(player: Instance): Instance`

> **Deprecated:** This function has been deprecated by [LocalizationService:GetTranslatorForPlayerAsync()](/docs/reference/engine/classes/LocalizationService.md), which functions similarly except that it yields until the cloud table has loaded. Please use it in new work instead.

This function takes a player as an argument and returns a
[Translator](/docs/reference/engine/classes/Translator.md) instance which can be used to perform translations for
that locale if any are available. The entries used for localization are
the entries provided by the [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) hierarchy under
[LocalizationService](/docs/reference/engine/classes/LocalizationService.md) as well as the cloud
[LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md), if it is available and already loaded. This
will be the same set of entries returned by
[LocalizationService:GetTableEntries(nil)](/docs/reference/engine/classes/LocalizationService.md).

This function does not yield. It will not wait until the cloud
[LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) has loaded.

See also:

- [LocalizationService:GetTranslatorForPlayerAsync()](/docs/reference/engine/classes/LocalizationService.md) has the same
  functionality as this function, except that it yields until the cloud
  [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) has been loaded.
- [LocalizationService:GetTranslatorForLocaleAsync()](/docs/reference/engine/classes/LocalizationService.md), returns a
  Translator to be used for translations using the provided locale.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The [Player](/docs/reference/engine/classes/Player.md) that you are getting the [Translator](/docs/reference/engine/classes/Translator.md) for. |

**Returns:** `Instance` — The [Translator](/docs/reference/engine/classes/Translator.md) instance for the specified locale.

**Getting and Using a Translator for a Player**

This code sample attempts to retrieve a `Translator` object for the local
player. [LocalizationService:GetTranslatorForPlayerAsync()](/docs/reference/engine/classes/LocalizationService.md) is wrapped
in a pcall because it may error. If it does not error and returns a
Translator, it translates and prints "Hello World!" in the player's language.
If the function errors, it prints "GetTranslatorForLocaleAsync failed:"
followed by the error message.

[LocalizationService:GetTranslatorForPlayer()](/docs/reference/engine/classes/LocalizationService.md) can also be used if you'd
like to get the player's translator without yielding until the function
returns.

```lua
local LocalizationService = game:GetService("LocalizationService")
local Players = game:GetService("Players")

local textLabel = script.Parent

local success, translator = pcall(function()
	return LocalizationService:GetTranslatorForPlayerAsync(Players.LocalPlayer)
end)

if success then
	local result = translator:Translate(textLabel, "Hello World!")
	print(result)
else
	print("GetTranslatorForPlayerAsync failed: " .. translator)
end
```

## Inherited Members

### From [Instance](/docs/reference/engine/classes/Instance.md)

- **Property `Archivable`** (`boolean`): Determines if an Instance and its descendants can be cloned using
- **Property `archivable`** (`boolean`):  *(deprecated, hidden)*
- **Property `Capabilities`** (`SecurityCapabilities`): The set of capabilities allowed to be used for scripts inside this
- **Property `IsInSandbox`** (`boolean`): Indicates whether the instance is inside a sandboxed container.
- **Property `Name`** (`string`): A non-unique identifier of the Instance.
- **Property `Parent`** (`Instance`): Determines the hierarchical parent of the Instance.
- **Property `PredictionMode`** (`PredictionMode`): Reflects the client-side prediction mode applied to the instance under
- **Property `RobloxLocked`** (`boolean`): A deprecated property that used to protect CoreGui objects. *(hidden)*
- **Property `Sandboxed`** (`boolean`): When enabled, the instance can only access abilities in its `Capabilities`
- **Property `UniqueId`** (`UniqueId`): A unique identifier for the instance.
- **Method `AddTag(tag: string): ()`**: Applies a tag to the instance.
- **Method `children(): Instances`**: Returns an array of the object's children. *(deprecated)*
- **Method `ClearAllChildren(): ()`**: This method destroys all of an instance's children.
- **Method `Clone(): Instance`**: Create a copy of an instance and all its descendants, ignoring instances
- **Method `clone(): Instance`**:  *(deprecated)*
- **Method `Destroy(): ()`**: Sets the Instance.Parent property to `nil`, locks the
- **Method `destroy(): ()`**:  *(deprecated)*
- **Method `FindFirstAncestor(name: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorOfClass(className: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorWhichIsA(className: string): Instance?`**: Returns the first ancestor of the Instance for whom
- **Method `FindFirstChild(name: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance found with the given name.
- **Method `findFirstChild(name: string, recursive?: boolean): Instance`**:  *(deprecated)*
- **Method `FindFirstChildOfClass(className: string): Instance?`**: Returns the first child of the Instance whose
- **Method `FindFirstChildWhichIsA(className: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance for whom
- **Method `FindFirstDescendant(name: string): Instance?`**: Returns the first descendant found with the given Instance.Name.
- **Method `GetActor(): Actor?`**: Returns the Actor associated with the Instance, if any.
- **Method `GetAttribute(attribute: string): Variant`**: Returns the value which has been assigned to the given attribute name.
- **Method `GetAttributeChangedSignal(attribute: string): RBXScriptSignal`**: Returns an event that fires when the given attribute changes.
- **Method `GetAttributes(): Dictionary`**: Returns a dictionary of the instance's attributes.
- **Method `GetChildren(): Instances`**: Returns an array containing all of the instance's children.
- **Method `getChildren(): Instances`**:  *(deprecated)*
- **Method `GetDebugId(scopeLength?: int): string`**: Returns a coded string of the debug ID used internally by Roblox.
- **Method `GetDescendants(): Instances`**: Returns an array containing all of the descendants of the instance.
- **Method `GetFullName(): string`**: Returns a string describing the instance's ancestry.
- **Method `GetStyled(name: string, selector: string?): Variant`**: Returns the styled or explicitly modified value of the specified property,
- **Method `GetStyledPropertyChangedSignal(property: string): RBXScriptSignal`**: Returns an event that fires when the given style property changes on the
- **Method `GetTags(): Array`**: Gets an array of all tags applied to the instance.
- **Method `HasTag(tag: string): boolean`**: Check whether the instance has a given tag.
- **Method `IsAncestorOf(descendant: Instance): boolean`**: Returns true if an Instance is an ancestor of the given
- **Method `IsDescendantOf(ancestor: Instance): boolean`**: Returns `true` if an Instance is a descendant of the given
- **Method `isDescendantOf(ancestor: Instance): boolean`**:  *(deprecated)*
- **Method `IsPropertyModified(property: string): boolean`**: Returns `true` if the value stored in the specified property is not equal
- **Method `QueryDescendants(selector: string): Instances`**: Returns an array containing all descendants of the instance that match the
- **Method `Remove(): ()`**: Sets the object's `Parent` to `nil`, and does the same for all its *(deprecated)*
- **Method `remove(): ()`**:  *(deprecated)*
- **Method `RemoveTag(tag: string): ()`**: Removes a tag from the instance.
- **Method `ResetPropertyToDefault(property: string): ()`**: Resets a property to its default value.
- **Method `SetAttribute(attribute: string, value: Variant): ()`**: Sets the attribute with the given name to the given value.
- **Method `WaitForChild(childName: string, timeOut: double): Instance`**: Returns the child of the Instance with the given name. If the
- **Event `AncestryChanged`**: Fires when the Instance.Parent property of this object or one of
- **Event `AttributeChanged`**: Fires whenever an attribute is changed on the Instance.
- **Event `ChildAdded`**: Fires after an object is parented to this Instance.
- **Event `childAdded`**:  *(deprecated)*
- **Event `ChildRemoved`**: Fires after a child is removed from this Instance.
- **Event `DescendantAdded`**: Fires after a descendant is added to the Instance.
- **Event `DescendantRemoving`**: Fires immediately before a descendant of the Instance is removed.
- **Event `Destroying`**: Fires immediately before (or is deferred until after) the instance is
- **Event `StyledPropertiesChanged`**: Fires whenever any style property is changed on the instance, including

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some