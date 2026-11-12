# XP Ranks API

## XP Ranks API

[XP Ranks](../../mods/xp-ranks.md) exposes a small API (`XPR_API`, in `shared/XPR_API.lua`) for other Mods to award Rank XP, read Ranks and react to Rank Ups. Everything else in XP Ranks (`XPR_RankData`, `XPR_RankCurve`, `XPR_Categories` and so on) is internal and may change without notice.

---

## Setup

- **Hard dependency (recommended):** Add `require=[B42]XPRanks` to both of the calling Mod's `mod.info` files.
- **Soft dependency:** Only for a Mod where XP Ranks is an optional extra. Leave XP Ranks out of `mod.info` and check that `XPR_API` (and the function) is not `nil` before calling. The calling Mod works with or without XP Ranks. Its integration stays off without it.

With either kind, check the function exists before calling it:

```lua
if XPR_API and XPR_API.AwardXp then
    XPR_API.AwardXp(player, 25, "Challenge Complete", "MyModId")
end
```

---

## Topologies

| Topology | `isServer()` | `isClient()` | Runs XP Ranks Server Logic |
|:---|:---:|:---:|:---:|
| Singleplayer | `false` | `false` | Yes (client and server share one Lua state) |
| Hosted MP (host) | `true` | `true` | Yes |
| Dedicated server | `true` | `false` | Yes (no local Player) |
| MP client | `false` | `true` | No |

Most functions only give real answers where XP Ranks runs its server logic. On an MP client they return a safe default instead of an error.

---

## Awarding XP

### `XPR_API.AwardXp(player, amount, tickerLabel, categoryKey)`

Awards flat Rank XP to a Player and shows them a Ticker Feed entry.

| Parameter | Type | Required | Description |
|:---|:---|:---:|:---|
| `player` | `IsoPlayer` | yes | The Player to award. **Must** come from the calling Mod's own server-side event or state, never from client-supplied input |
| `amount` | number | yes | Flat Rank XP, above 0. Anything else does nothing |
| `tickerLabel` | string | no | The text the Player sees, for example `"Streak Retention"` shows as `Streak Retention +20 XP`. Defaults to `"Bonus"`. Display only |
| `categoryKey` | string | no | The storage bucket (and with it the Leaderboard category) the XP counts towards. Several labels can share one key. Defaults to `tickerLabel` |

Returns `true` when XP was awarded, `false` when nothing happened (an MP client, bad arguments, or XP Ranks' server files not loaded). The caller does not need to check the topology first: on an MP client it simply returns `false`. Call it from the calling Mod's server-side code.

---

## Reading Ranks

### Server Functions

These read the real Player data. They only return real values where XP Ranks runs its server logic. On an MP client they return `0` or `false`. Use them for every gate or check that matters.

| Function | Returns |
|:---|:---|
| `GetRank(player)` | The Player's current Rank, or `0` if unavailable |
| `IsRankOrAbove(player, requiredRank)` | `true` when the Player's Rank is at least `requiredRank`. `false` on any failure (including a non-number `requiredRank`) |
| `GetTotalXp(player)` | The Player's total Rank XP (all time), or `0` if unavailable |
| `GetXpToNextRank(player)` | XP still needed for the next Rank (for example 450 more XP to Rank 11). `0` if unavailable or the Player is at the maximum Rank (999) |

`player` follows the same rule as `AwardXp`: it must come from the calling Mod's own server-side state.

### Anywhere

| Function | Returns |
|:---|:---|
| `GetXpForRank(rank)` | The total XP needed to reach `rank` (for example Rank 10 needs 200 XP). `0` for a non-number. A pure calculation with no Player lookup: it works the same on every topology, including client UI |

### Client Only

| Function | Returns |
|:---|:---|
| `GetLocalRank()` | The local Player's own Rank, with no network round-trip. `0` if unavailable. Always `0` on a Dedicated server (no local Player) |

`GetLocalRank()` is for display only, such as greying out a buy button. A modified client can report anything. Check with `GetRank` or `IsRankOrAbove` on the server before granting anything it gated.

---

## Events

XP Ranks registers both events in shared Lua: `.Add()` works everywhere. They only **fire** where XP Ranks runs its server logic, at the moment XP is awarded (not delayed like the Rank Up notification). An MP client can subscribe but is never called. To react on a client, subscribe on the server side of the calling Mod and send the client a command.

Each event passes the Player and one data table.

### `Events.XPR_OnRankUp`

```lua
Events.XPR_OnRankUp.Add(function(player, data)
    -- data.oldRank, data.newRank
end)
```

| Field | Type | Meaning |
|:---|:---|:---|
| `data.oldRank` | number | The Rank before this award |
| `data.newRank` | number | The Rank after. A large award can cross several Ranks in one event |

### `Events.XPR_OnXpGained`

Fires on **every** XP award, not just Rank Ups.

```lua
Events.XPR_OnXpGained.Add(function(player, data)
    -- data.oldXp, data.newXp, data.category, data.amount
end)
```

| Field | Type | Meaning |
|:---|:---|:---|
| `data.oldXp` | number | Total Rank XP before this award |
| `data.newXp` | number | Total Rank XP after (`oldXp + amount`) |
| `data.category` | string | The category the XP counted towards (for example `"Combat - Firearms"`, `"Zombie Kill"` or a calling Mod's `categoryKey`) |
| `data.amount` | number | The XP awarded (capped at 100,000 per award) |

---

## Quick Reference

| Function | Kind | Works on an MP Client? |
|:---|:---|:---|
| `AwardXp(player, amount, tickerLabel, categoryKey)` | Write | No, returns `false` |
| `GetRank(player)` | Server read | No, returns `0` |
| `IsRankOrAbove(player, requiredRank)` | Server read | No, returns `false` |
| `GetTotalXp(player)` | Server read | No, returns `0` |
| `GetXpToNextRank(player)` | Server read | No, returns `0` |
| `GetXpForRank(rank)` | Pure | **Yes** |
| `GetLocalRank()` | Client read | **Yes** (`0` on a Dedicated server) |
| `Events.XPR_OnRankUp` | Event | Can subscribe, only fires on the server |
| `Events.XPR_OnXpGained` | Event | Can subscribe, only fires on the server |

---
