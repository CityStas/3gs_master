---
title: "Monitor performance"
url: /docs/en-us/performance-optimization/monitor
last_updated: 2026-10-30T19:55:46Z
description: "Explains how to use the Performance Dashboard to monitor your games."
---

# Monitor performance

The [Performance Dashboard](/docs/en-us/production/analytics/performance.md) is the best way to monitor the performance of your published games. The two tabs include real-time performance information for both clients and servers, and you can use date ranges to track the impact of your changes over time.

For example, imagine you've just added a new place to your game:

1. You publish the updated game, and hours later, you notice a distinct uptick in client crash rate on the Performance Dashboard that seems to correlate with client memory usage.
2. You test the new place in Studio and don't see any issues. Memory usage seems similar to other places in your game.
3. You note that average player session time has increased dramatically since your update.
4. You test again, but this time, you spend more time in the game and keep a closer eye on memory usage over time. Sure enough, usage is growing over time and could cause crashes on lower-end devices.
5. You check the server tab and notice that server memory usage is growing over time, too. It's not a problem yet, but could become a problem soon.
6. Under the **Memory** tab of the Developer Console, in the **PlaceScriptMemory** breakdown, you notice that the memory usage for one of your new scripts grows each time you interact with some key objects in the world. The script runs on both the client and the server.
7. You check the script, which adds some user data to a large table, but never cleans the data up—it's growing infinitely.
8. You fix the problem, publish the updated game, and client crash rate returns to its previous value.

Comparing the Performance Dashboard to other dashboards can help you correlate performance improvements (or regressions) to business metrics for a more complete idea of how a performant game impacts your bottom line. For more information, see [Analytics](/docs/en-us/production/analytics.md).
