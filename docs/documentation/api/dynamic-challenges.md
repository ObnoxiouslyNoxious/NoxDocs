# Dynamic Challenges API

## Dynamic Challenges API

[Dynamic Challenges & Leaderboard](../../mods/daily-challenge-system.md) (DCS) exposes a versioned API (`DCS_ChallengeAPI`, version 1, DCS 2.0.0 and later) for other Mods to read Challenge progress and react to Challenge events. Anything not listed here (DCS globals such as `DCS_Server`, `DCS_Sync` and `DCS_Store`, or its ModData) is internal and may change without notice.

---

## Setup

- **Hard dependency (recommended):** Add `require=[B42]DailyChallengeSystem` to both of the calling Mod's `mod.info` files.
- **Soft dependency:** Only for a Mod where Dynamic Challenges is an optional extra. Leave the `require=` line out. The calling Mod then works with or without DCS.

With either kind, check the API is ready before use:

```lua
local function dcsAvailable()
    return DCS_ChallengeAPI ~= nil
        and DCS_ChallengeAPI.API_VERSION ~= nil
        and DCS_ChallengeAPI.isAvailable()
end
```

`isAvailable()` is `false` until DCS has built the current Rotation's Challenge list. It is also `false` on a remote client and when the Challenge Mode value is invalid. While it is `false`, the Challenge, Rotation and reveal-threshold server functions return safe defaults (`0`, `""` or `false`). A calling Mod that forgets to check still fails closed.

---

## Functions

### Server Functions

These work in the process that runs DCS server logic: Singleplayer, a Hosted server or a Dedicated server. Use them for anything that matters (rewards, unlocks, spawning, permissions).

| Function | Returns |
|:---|:---|
| `getCompletedCount(player)` | Challenges that Player has completed in the current Rotation |
| `getChallengeCount()` | Challenges in the current Rotation |
| `getRotationId()` | An opaque string id for the current Rotation |
| `getRotationIntervalHours()` | The configured Rotation length in hours (1 to 672, default 24) |
| `getVendorRevealThreshold()` | Challenges needed in the current Rotation to reveal Vendor Locations (the "Challenges Completed to Reveal Vendor" setting, clamped to the current Challenge count) |
| `getCurrencyMode()` | `"tokens"`, `"money"` or `"custom"` (`""` when DCS server logic is not running) |
| `getCustomCurrencyItem()` | The full Item type of the Custom Currency (`""` unless the mode is `"custom"`) |
| `getCustomCurrencyName()` | The Admin-chosen Custom Currency name, not translated (`""` unless the mode is `"custom"`) |
| `isAvailable()` | `true` only when the Challenge, Rotation and reveal-threshold values are valid. The currency functions do not depend on it |

### Client Functions

For display only. A modified client can report anything.

| Function | Returns |
|:---|:---|
| `getLocalCompletedCount()` | Completed count from the local DCS state |
| `getLocalChallengeCount()` | Challenge count from the local DCS state |
| `getLocalCurrencyMode()` | The synced Currency mode: `"tokens"`, `"money"` or `"custom"` |
| `getLocalCustomCurrencyItem()` | The synced Custom Currency Item type (`""` unless the mode is `"custom"`) |
| `getLocalCurrencyLabel()` | The Currency as a word in the Player's language: `Tokens` (translated), `Money` or the Custom name |
| `getLocalCurrencyDisplay()` | The Currency as shown beside an amount: `$` in Money mode, otherwise the same as the label |
| `getLocalVendorRevealThreshold()` | The Vendor reveal threshold from the synced DCS settings (clamped, default 3 until settings sync) |

### Rules

- **Authority:** Pass the server-owned `IsoPlayer` to server functions (for example the `player` from `OnClientCommand`). Never build it from client-supplied data.
- **Rotation id:** Treat it as opaque and only compare it for equality. Its format depends on the Rotation interval.
- **Counting:** Only Challenges in the current Rotation's list count. A Player whose record has not been reset since the last Rotation boundary reads as `0`.
- **Currency:** The three server currency functions return the mode and raw settings, not display text, because the server does not know a Player's language. Use the `getLocal...` label and display functions on the client for text.
- **Vendor reveal threshold:** `0` is a real value meaning Vendor Locations are always revealed, not a fail-closed default. Check `isAvailable()` before trusting `getVendorRevealThreshold()`. A Player has unlocked the reveal when `getCompletedCount(player) >= getVendorRevealThreshold()`. Reading a Vendor Location Map also reveals Locations for the current Rotation. That is not exposed here.

---

## Events

Both events fire only in the process that runs DCS server logic. They never fire on a remote client. A client cannot trigger them.

### `DCS_OnChallengeCompleted`

Fires once for each newly recorded completion, after DCS has recorded it, paid rewards and updated the Streak and Leaderboard. A listener sees the final values.

Arguments: `(player, data)`

| `data` field | Type | Meaning |
|:---|:---|:---|
| `challengeId` | string | The Challenge that was completed |
| `completedCount` | number | Challenges this Player has completed in the current Rotation, including this one |
| `challengeCount` | number | Challenges in the current Rotation |
| `rotationId` | string | The current Rotation id |

Completing the same Challenge again in the same Rotation does not fire it again.

### `DCS_OnRotationReset`

Fires when DCS begins a new Rotation: after the Challenges are rebuilt at the Rotation boundary, or after the rebuild at server start when the saved Rotation was out of date.

Arguments: `(data)`

| `data` field | Type | Meaning |
|:---|:---|:---|
| `rotationId` | string | The new Rotation id |
| `challengeCount` | number | Challenges in the new Rotation |

It does **not** fire when a server restarts inside the same Rotation. A Mod that keeps its own per-Rotation state should compare `getRotationId()` with the id it last saw (for example at server start) instead of relying only on this event.

---

## Subscribing

DCS registers the events in its shared Lua. They exist only after DCS has loaded. Subscribe from a `client/` or `server/` file (or an `OnGameBoot` / `OnServerStarted` handler), not at the top level of a `shared/` file: shared files from different Mods can load in any order.

```lua
if isClient() and not isServer() then return end

local function onChallengeCompleted(player, data)
    if not data or not data.challengeId then return end
    -- Server-authoritative: safe to reward or unlock here.
    print("DCS: " .. tostring(data.challengeId) .. " completed, "
        .. tostring(data.completedCount) .. "/" .. tostring(data.challengeCount))
end

local function onRotationReset(data)
    print("DCS: new Rotation " .. tostring(data and data.rotationId))
end

local function subscribe()
    if Events and Events.DCS_OnChallengeCompleted then
        Events.DCS_OnChallengeCompleted.Add(onChallengeCompleted)
    end
    if Events and Events.DCS_OnRotationReset then
        Events.DCS_OnRotationReset.Add(onRotationReset)
    end
end

Events.OnGameBoot.Add(subscribe)
```

---

## Example

Gate a feature on Challenge progress, on the server, inside an `OnClientCommand` handler:

```lua
local function playerHasEarnedIt(player, required)
    if not (DCS_ChallengeAPI and DCS_ChallengeAPI.isAvailable()) then
        return false -- DCS missing or not ready: fail closed
    end
    return DCS_ChallengeAPI.getCompletedCount(player) >= required
end
```

---

## Topology

| Topology | Server Functions and Events | Client Functions |
|:---|:---|:---|
| Singleplayer | Work (the one process runs DCS server logic) | Work |
| Hosted MP | Work in the server process | Work on the host and remote clients |
| Dedicated MP | Work in the server process | Work on each client |

On a remote client the server functions return their safe defaults and the events never fire. Make every authoritative decision on the server.

---

## Versioning

- Version 1 only grows. New functions and new `data` fields may be added without a version change. Existing names, argument order and meanings will not change within version 1.
- A breaking change raises `DCS_ChallengeAPI.API_VERSION`. Check it before relying on a newer function.
- Never call a function without checking it exists. Ignore unknown `data` fields.

---
