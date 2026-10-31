---
title: "Matchmaking glossary"
url: /docs/en-us/matchmaking/glossary
last_updated: 2026-10-30T19:55:45Z
description: "Glossary of matchmaking terms."
---

# Matchmaking glossary

| **General terms** | |
| --- | --- |
| **Joining player** | The player being matched to a server in your game. |
| **Common device** | The device type shared between existing players in the server and the joining player. Can be a mobile device, a desktop, a laptop, a tablet, or a console. |
| **Common language** | The language shared between existing players in the server and the joining player. |
| **Scoring** | |
| **Server** | An RCC instance hosting a place. |
| **Signal weight** | A non-negative number that describes the importance of a signal relative to other signals. |
| **Weighted sum** | The sum of all weighted signal scores for a server. The basis for picking the best server for a player. |
| **Server score** | The final matchmaking score for a server, based on the weighted sum of its signals. Players are matched to the server with the highest score. |
| **Weighted signal score** | The value after multiplying the signal score by its weight. |
| **Signals** | |
| **Signal** | The processed version of an attribute. A signal is created when an attribute is transformed to fit the matchmaking scoring system. |
| **Signal score** | The value of a signal after transformations, ranging between 0 and 1. |
| **Weight** | Describes the importance of a signal in the scoring process. Signals with higher weights have a bigger impact in matchmaking. |
| **Weighted signal score** | The result of multiplying a signal's score by its weight. Reflects both the value and importance of the signal. |
| **Numerical custom signal** | The difference between the joining player's attribute and the server's average. |
| **Categorical custom signal** | How common the joining player's attribute is when compared to the other players in the server. |
| **Attributes** | |
| **Attribute** | A property used in matchmaking scoring. Represents “raw signal values” before they're processed.<br><br> Can be a number or a string. |
| **Custom attribute** | A universe-level property defined by creators. Can be a **player attribute** or a **server attribute**. |
| **Player attribute** | A characteristic of a player, like their preferred game mode or skill level. |
| **Server attribute** | A characteristic of a server, like the server's response time or active game mode. |
