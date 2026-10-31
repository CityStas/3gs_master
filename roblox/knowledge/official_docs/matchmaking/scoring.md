---
title: "Server scoring"
url: /docs/en-us/matchmaking/scoring
last_updated: 2026-10-30T19:55:45Z
description: "How matchmaking uses scoring to match players to servers."
---

# Server scoring

## The scoring formula

Servers are scored using a weighted sum formula. There are four parts to this formula:

- [Attributes](#attributes), which are data that describe players and servers, such as player age or server occupancy.
- [Signals](#signals), which transform attributes into numbers between 0 and 1.
- [Weights](#weights), which describe the relative importance of signals.
- The [server score](#server-score), which measures the server's compatibility with the joining player.

The joining player is matched to the server with the highest server score.

### Attributes

Attributes are data that describe players and servers. An attribute's value can be a number or a string. When an attribute's value is a string, it's called a categorical attribute. When an attribute's value is a number, it's called a numerical attribute.

For a full list of all available Roblox attributes, see [Existing attributes](/docs/en-us/matchmaking/attributes-and-signals.md#existing-attributes). For more information about custom attributes, see [Custom attributes](/docs/en-us/matchmaking/attributes-and-signals.md#custom-attributes).

##### Example: Categorical and numerical attributes

| **Categorical attributes** |
| --- |
| **Has Friends** is a categorical attribute because its value is the string "true" when there is a preferred player on this server, and "false" when there are no preferred players on this server. |
| **Language** is a categorical attribute because its value is the player's language setting, such as "Japanese". |
| **Numerical attributes** |
| **Age** is a numerical attribute because its value is the player's age. |
| **Occupancy** is a numerical attribute because its value is the number of players currently in this server. |

### Signals

Signals transform attribute values into numbers between 0 and 1, called signal scores. A signal score of 1 predicts high player compatibility, while a signal score of 0 predicts low player compatibility. Depending on the attribute, transformations can include different aggregations, comparisons, and normalizations.

For a full list of existing Roblox signals, see [Existing signals](/docs/en-us/matchmaking/attributes-and-signals.md#existing-signals). For more information about custom signals, see [Custom signals](/docs/en-us/matchmaking/attributes-and-signals.md#custom-signals).

##### Example: Two servers with different signal scores

The following table calculates Occupancy signal scores for two different server with capacity for 8 players:

|  | **Players in server** | **Occupancy score** |
| --- | --- | --- |
| **Server A** | 2 | 2/8 = 0.25 |
| **Server B** | 6 | 6/8 = 0.75 |

The Occupancy signal scores Server B higher and considers it a better fit for the joining player.

### Weights

A signal's weight describes that signal's importance relative to other signals. A higher weight increases the signal's contribution to the server score. The value after multiplying a signal score by its weight is called a **weighted signal**.

Signals can't have negative weights. If a signal's weight is 0, that signal is not considered for scoring.

##### Example: Weighting the Occupancy score

The following table calculates weighted Occupancy signal scores for a place with capacity for 8 players and an Occupancy signal weight of 2:

|  | **Players in server** | **Occupancy score** | **Weighted occupancy score** |
| --- | --- | --- | --- |
| **Server A** | 2 | 2/8 = 0.25 | 0.25 * 2 = 0.5 |
| **Server B** | 6 | 6/8 = 0.75 | 0.75 * 2 = 1.5 |

##### Example: Two configurations with different weights

Different weights can also make matchmaking choose different servers. The following table calculates the server scores of two servers with different matchmaking configurations. Configuration 2 has a higher weight for its Occupancy signal, and Server A has a friend of the joining player in it.

|  |  | **Friends** | **Occupancy** | |
| --- | --- | --- | --- | --- |
|  |  | **Weight** | **Score** | **Weight** | **Score** | **Total score** |
| **Config 1** | **Server A** | 1 | 1 | 5 | 0.25 | 1 * 1 + 5 * 0.25 = 2.25 |
| **Server B** | 1 | 0 | 5 | 0.75 | 1 * 0 + 5 * 0.75 = 3.75 |
| **Config 2** | **Server A** | 3 | 1 | 5 | 0.25 | 3 * 1 + 5 * 0.25 = 4.25 |
| **Server B** | 3 | 0 | 5 | 0.75 | 3 * 0 + 5 * 0.75 = 3.75 |

### Server score

The server score is calculated by the following weighted sum formula, which sums a server's weighted signal scores:

ServerScore = WeightedSignalScore 1 + WeightedSignalScore 2 + … + WeightedSignalScore n \text{ServerScore} = \text{WeightedSignalScore}_1 + \text{WeightedSignalScore}_2 + \ldots + \text{WeightedSignalScore}_nServerScore=WeightedSignalScore1​+WeightedSignalScore2​+…+WeightedSignalScoren​

ServerScore = Weight 1 × SignalScore 1 + Weight 2 × SignalScore 2 + … + Weight n × SignalScore n \phantom{\text{ServerScore}} = \text{Weight}_1 \times \text{SignalScore}_1 + \text{Weight}_2 \times \text{SignalScore}_2 + \ldots + \text{Weight}_n \times \text{SignalScore}_nServerScore=Weight1​×SignalScore1​+Weight2​×SignalScore2​+…+Weightn​×SignalScoren​

### Matchmaking configurations

A matchmaking configuration is the set of signals and weights used to score servers of a place. By default, all servers of all places are scored by the Roblox default configuration, meaning you don't need to customize or enable any settings in order to use it.

The Roblox default configuration includes the following signals and weights:

| **Signal** | **Weight** |
| --- | --- |
| Friends | 15 |
| Latency | 3 |
| Text Chat | 3 |
| Occupancy | 2 |
| Play History | 2 |
| Language | 2 |
| Age | 1 |
| Voice Chat | 1 |
| Device Type | 0 |

In the default Roblox configuration, the Friends signal's weight is greater than the sum of the weights of every other signal. This means that, if available, the joining player is always matched to servers with friends (or players on the same IP address) in them.

The Device Type signal exists in the default configuration but has a weight of 0, so it doesn't affect matchmaking decisions. You can adjust this weight when you [customize matchmaking](/docs/en-us/matchmaking/customize-matchmaking.md).

For more information about each Roblox signal, see [Existing signals](/docs/en-us/matchmaking/attributes-and-signals.md#existing-signals).

## Advanced concepts

The following are more advanced concepts about the matchmaking process.

### Normalization

Signals normalize attribute values to be numbers between 0 and 1. Numerical signals can be normalized by any positive number, called the **normalizing factor**. If the normalized value is greater than 1, it is clamped down to 1.

##### Example: Designing the Age signal

The Age signal measures the difference between the average age of players in the server and the joining player's age.

ageDifference = ∣ avgServerAge − joiningPlayerAge ∣ \text{ageDifference} = |\text{avgServerAge} - \text{joiningPlayerAge}|ageDifference=∣avgServerAge−joiningPlayerAge∣

Servers with age differences beyond 25 are all considered equally incompatible with the player. For example, an age difference of 25 is no worse for a player than an age difference of 26, so both values should take the signal score to 0. In this case, 25 is considered the normalizing factor.

normAgeDifference = min ⁡ ( 1, ∣ avgServerAge − joiningPlayerAge ∣ / 25) \text{normAgeDifference} = \min(1, |\text{avgServerAge} - \text{joiningPlayerAge}| / 25)normAgeDifference=min(1,∣avgServerAge−joiningPlayerAge∣/25)

The signal score is inversely related to the age difference, meaning that the signal score is higher when the age difference is smaller.

ageDifferenceSignalScore = 1 − normAgeDifference \text{ageDifferenceSignalScore} = 1 - \text{normAgeDifference}ageDifferenceSignalScore=1−normAgeDifference

The following table shows Age signal scores with two different normalizing factors:

| **Age** | **Normalizing factor: 100** | **Normalizing factor: 25** |
| --- | --- | --- |
| 50 | 0.5 | 0 |
| 25 | 0.75 | 0 |
| 12 | 0.88 | 0.52 |
| 5 | 0.95 | 0.8 |
| 0 | 1 | 1 |

The signal with a normalizing factor of 25 considers the 5-year and 12-year age differences to be farther apart. Smaller normalizing factors have the effect of amplifying marginal increases or decreases in age difference.

### Weight magnitudes

A weight indicates the importance of a signal relative to other signals in a configuration. The relative magnitudes of weights determine signal importance, not their absolute magnitudes.

##### Example: Relative vs absolute magnitude

The table below calculates the server scores of two servers with two different matchmaking configurations. Configuration 5 and Configuration 6 have Occupancy weights higher than their respective Friends weights. Server A has a friend of the joining player in it.

|  |  | **Friends** | **Occupancy** | |
| --- | --- | --- | --- | --- |
|  |  | **Weight** | **Score** | **Weight** | **Score** | **Total score** |
| **Config 5** | **Server A** | 10,000 | 1 | 15,000 | 0.25 | 10,000 * 1 + 15,000 * 0.25 = 13,750 |
| **Server B** | 10,000 | 0 | 15,000 | 0.75 | 10,000 * 0 + 15,000 * 0.75 = 11,250 |
| **Config 6** | **Server A** | 0.01 | 1 | 0.05 | 0.25 | 0.01 * 1 + 0.05 * 0.25 = 0.0225 |
| **Server B** | 0.01 | 0 | 0.05 | 0.75 | 0.01 * 0 + 0.05 * 0.75 = 0.0375 |

Server A wins with Configuration 5 while Server B wins with Configuration 6. This is because Configuration 5's Occupancy weight is only 1.5x its Friends weight, while Configuration 6's Occupancy weight is 5x its Friends weight.

Despite differences in absolute magnitudes, Configuration 6 prioritizes Occupancy over Friends more than Configuration 5 does.
