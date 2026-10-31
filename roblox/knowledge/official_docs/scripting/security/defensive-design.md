---
title: "Defensive design tactics"
url: /docs/en-us/scripting/security/defensive-design
last_updated: 2026-10-30T19:55:56Z
description: "Understand fundamentals of design that help prevent cheaters and exploiters from ruining the playing experience."
---

# Defensive design tactics

> **Warning:** The following content covers various concepts and tactics to improve security and mitigate cheating in your Roblox games. It's highly recommended that all developers read through these to ensure that your games are secure and fair for all users. Check the sidebar for additional security topics.

Basic design decisions can serve as "first step" security measures to discourage exploits. The core principle is to design systems where cheating is either impossible or provides no meaningful advantage, rather than trying to detect and prevent cheating after the fact.

Consider a shooter game where players earn points for kills. An exploiter might create bots that teleport to the same location to be repeatedly killed for easy points. This scenario illustrates the difference between reactive and defensive approaches:

| Approach | Predictable outcome |
| --- | --- |
| Chase down bots by writing code that attempts to detect them (reactive approach). | > **Error:** Exploiters seeking quick points will find a way around your complex detection code and use their bots in a different way. |
| Reduce or outright remove point gains for kills on newly spawned players (defensive approach). | > **Success:** Extra time and friction is now required for exploiters because they get no points for instantly killing their bots. Additionally, "spawn campers" are discouraged because they no longer get points for killing newly spawned players. |

Additional defensive design scenarios:

| Potential exploit scenario | Reactive Approach (less effective) | Defensive approach (more effective) |
| --- | --- | --- |
| (Obby) Exploiter teleports to the end to claim rewards | Only check the player's final position and try to detect impossible completion times | Design with mandatory, sequential checkpoints. Server validates each checkpoint was activated in order before granting rewardsYou can add another layer by flagging players who complete stages faster than humanly possible. The design of the game (requiring checkpoints) is what enables the effective server-side validation. |
| (Combat) Client reports dealing impossible damage amounts | Try to detect and filter out impossible damage values | Server calculates all damage from server-sided weapon stats and validates hits through server-side raycasting |
| (Economy) Exploiter duplicates items through rapid requests | Try to detect duplicate requests or unusual patterns | Implement server-side cooldowns and validate all transactions against current player inventory state |

> **Info:** **Key principle**  When designing a new feature, ask yourself: "How would an exploiter abuse this, and can I change the design to make that abuse impossible or worthless?" Instead of trying to detect cheating after it happens, design your game so that cheating either cannot occur or provides no meaningful advantage.
