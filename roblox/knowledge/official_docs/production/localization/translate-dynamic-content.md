---
title: "Translate dynamic content"
url: /docs/en-us/production/localization/translate-dynamic-content
last_updated: 2026-10-30T19:55:48Z
description: "Explains how to use Parameters in localization tables to translate specific parts of content."
---

# Translate dynamic content

You can use **parameters** in your [localization table](/docs/en-us/production/localization/manual-translations.md#cloud-localization-table) when only part of the displayed string requires translation, such as localizing a unit of measurement after a number value, referencing a username, or displaying time and date.

_Displaying an amount of in-game items._

_Showing a player's Roblox username in a message._

_Displaying a high score using localized separators._

Parameters consist of a **parameter value** and an optional **format specifier** enclosed in braces.

In the following example, a game has the following entries in its localization table:

| Source | es |
| --- | --- |
| Hello {Player_Name}! | Hola {Player_Name}! |
| My name is {NPC_Name} | Me llamo {NPC_Name} |

If a user has their locale set to **es**, the translation output would be as follows:

| Original in-game text | Spanish translation |
| --- | --- |
| Hello new_storm! | Hola new_storm! |
| My name is Diva Dragonslayer | Me llamo Diva Dragonslayer |

In some cases, you may want to use format specifiers to control how the parameter value is formatted in the localized string.

The available format specifiers are as follows:

| Specifier | Type | Description | Example output |
| --- | --- | --- | --- |
| int | number | Integer with optional negative sign; no thousand separators. | 1234 |
| fixed | number | Two decimals with decimal indicator, optional negative sign, and no thousand separators. | 1234.50<br>1234,50 |
| num | number | Two decimals with decimal indicator, optional negative sign, and thousand separators. | 1,234.50<br>1234,50 |
| HEX | number | Integer converted to hex; negative is converted to 64-bit two's complement. | 3FF |
| hex | number | Same as HEX, but lowercase. | 3ff |
| datetime | number | UTC timestamp as a number to universal user-readable format. | 2017-10-10 13:38:10 |
| iso8601 | number | UTC timestamp as a number to ISO-8601 format UTC time. | 2017-10-12T22:02:38Z |
| shorttime | number | UTC timestamp to local "hour:minute" format. | 1:45 PM<br>13:45 |
| shortdatetime | number | UTC timestamp to general date+time pattern with short time. | 10/10/2017 1:45 PM |
| shortdate | number | UTC timestamp to short date pattern. | 10/10/2017<br>2017-10-10 |
| translate | string | Looks for a literal **Source** string match in the localization table and uses available locale translation. | |

## Translate substrings

Use the **translate** specifier when requiring a direct translation from your localization table. The localization will search for an exact match of the parameter in the Source column of your localization table.

In the following example, a game has the following rows in its localization table:

| Source | es |
| --- | --- |
| I am from {Place_Name:translate}. | Soy de {Place_Name:translate}. |
| Brazil | Brasil |
| London | Londres |
| Germany | Alemania |

If a user has their locale set to 'es', the translation output displays as follows:

| Original in-game text | Spanish translation |
| --- | --- |
| I am from Brazil. | Soy de Brasil. |
| I am from London. | Soy de Londres. |
| I am from Germany. | Soy de Alemania. |

## Translate with numbers

You can use a specifier to format your numerical values to match the context within your game.

In the following example, a game has the following number related entries in their localization table:

| Source | es |
| --- | --- |
| {race_time:fixed} seconds | {race_time:fixed} segundos |
| ${1:num} cash and {2:int} jewels | ${1:num} dinero y {2:int} joyas |

If a user has their locale set to **es**, the translation output displays as follows:

| Original in-game text | Spanish translation |
| --- | --- |
| 75.202844 seconds | 75,20 segundos |
| $2500.5 cash and 99.8 jewels | $2.500,50 dinero y 100 joyas |

> **Warning:** When using multiple parameters on a single entry, you must use either all strings or all numbers for parameter specifiers.
