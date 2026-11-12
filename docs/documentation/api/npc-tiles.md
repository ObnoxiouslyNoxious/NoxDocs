# NPC Tiles API

## NPC Tiles API

[NPC Tiles](../../mods/npc-tiles.md) exposes a versioned, server-authoritative API (`NPCTiles_API`, version 1) for other Build 42 Mods to place and manage persistent NPC Tiles. NPC Tiles owns the visible NPC object, its invisible collision companion, persistence, chunk-load reconciliation, cleanup and client sync. The calling Mod only says what to place and where.

---

## Setup

1. Choose how the calling Mod depends on NPC Tiles:

    - **Hard dependency:** add NPC Tiles as a requirement in both of the calling Mod's `mod.info` files. The calling Mod then cannot be enabled without NPC Tiles.

        ```ini
        require=[B42]NPCTiles
        ```

    - **Soft dependency:** leave the `require=` line out and check that `NPCTiles_API` is not `nil` before calling it. The calling Mod then works with or without NPC Tiles, and its NPC Tile features stay off when NPC Tiles is not enabled.

2. Call the API only from server-authoritative code: Singleplayer, a Hosted server's logic or a Dedicated server. On a remote client every mutating call returns `false, "server_only"`.
3. With a hard dependency, `require "NPCTiles_API"`. With either kind, check `NPCTiles_API.isAvailable(1)` at server start. If it returns `false`, log one line and leave the feature off.

!!! warning "Leave the Internals Alone"
    Never read or write `TilesNPC_Placements`, `NPCTiles_Server`, `NPCTiles_Placement` or the placed objects' ModData directly. Go through the API.

---

## Calls

Every mutating call returns `true, result` on success or `false, reason` on failure. Normal rejections never throw. A failed call never leaves persistence half-changed.

| Call | Purpose |
|:---|:---|
| `getVersion()` / `isAvailable(version)` | Version query. `isAvailable` returns `false, "api_version_too_old"` when the requested version is newer than the installed one |
| `isValidSprite(sprite)` / `isValidIcon(icon)` | Check a sprite name or Container Icon key. Safe in every Lua environment |
| `place(options)` | Register a Tile and create it if its square is loaded |
| `unregister(options)` / `remove(options)` | Remove a Tile the Mod owns. `remove` is an alias of `unregister` |
| `relocate(options)` | Move a Tile with a stable `sourceId` to new coordinates |
| `setSprite` / `setIcon` / `setCapacity` / `setShadow` / `setSourceData(options)` | Change one field of a Tile the Mod owns |
| `getAt(x, y, z)` / `getBySourceId(sourceMod, sourceId)` | A copy of the stored data, or `nil` |

---

## Placing a Tile

```lua
local ok, result = NPCTiles_API.place({
    x = 12345, y = 6789, z = 0,          -- required, integers
    sprite = "f_TilesNPC_Nox_02_32",     -- required, must be a known NPC Tiles sprite
    sourceMod = "MyModId",               -- required, [A-Za-z0-9_.-], max 64
    sourceId = "vendor-01",              -- optional, [A-Za-z0-9_.:/-], max 128
    placedBy = "server",                 -- optional audit text, defaults to sourceMod
    icon = "cabinet",                    -- optional Container Icon key
    capacity = 50,                       -- optional, kept within 1 to 10000
    shadow = true,                       -- optional, draws a Shadow under the Tile (default false)
    sourceData = { side = "east" },      -- optional, see Source Data below
})
```

| Option | Required | Notes |
|:---|:---|:---|
| `x`, `y`, `z` | yes | Whole numbers |
| `sprite` | yes | Must pass `isValidSprite` |
| `sourceMod` | yes | The calling Mod's stable name. Letters, digits, `_`, `.` and `-`, up to 64 characters |
| `sourceId` | no | A stable id for this Tile. Letters, digits, `_`, `.`, `:`, `/` and `-`, up to 128 characters. Makes repeated calls safe and enables `getBySourceId` and `relocate` |
| `placedBy` | no | Audit text. Defaults to `sourceMod` |
| `icon` | no | A Container Icon key that passes `isValidIcon` |
| `capacity` | no | Container Capacity, kept within 1 to 10000 |
| `shadow` | no | `true` draws a Shadow under the Tile. Defaults to `false` |
| `sourceData` | no | The calling Mod's own data (see [Source Data](#source-data)) |

On success `result` is `{ key, x, y, z, sprite, icon, capacity, shadow, placedBy, sourceMod, sourceId, sourceData, state }`. `state` is one of:

| State | Meaning |
|:---|:---|
| `materialized` | The object exists on a loaded square |
| `pending` | Registered, but the square is not loaded yet. This is a success. The object appears 30 ticks after the square loads |
| `cleanup_pending` | Lookups only. A removed Tile's old object is waiting to be cleared when its square next loads |

Calling `place` again with the same `sourceMod`, `sourceId` and equivalent options succeeds without placing a second Tile.

---

## Ownership and Collisions

- `unregister`, `relocate` and the `set` calls find a Tile by coordinates (`x, y, z`) or by `sourceId`. They always need `sourceMod`. When both a `sourceId` and a stored id exist, they must match.
- A Mod can only change or remove the Tiles it placed. Tiles placed with the NPC Tiles admin tools (or from Saves made before the API) are admin-owned. A Mod gets `not_owner` for those.
- The NPC Tiles admin tools can still change or remove any Tile, including those a Mod placed.
- The API never replaces another Mod's object. A loaded square holding an NPC Tiles sprite that NPC Tiles did not place returns `occupied_by_other_object`.
- Any existing registration at the coordinates returns `npc_tile_exists` (unless it is the repeat-call case above).
- The same `sourceId` registered at other coordinates returns `source_id_conflict`. Use `relocate` to move it.
- If saved data holds the same `sourceId` twice, every call for that id fails with `source_id_conflict`. One log line names both coordinates for repair.

---

## Removing and Moving

- `unregister` removes the registration at once. On a loaded square the object is cleared immediately (`state = "removed"`). On an unloaded square the old object is cleared when the square next loads (`state = "cleanup_pending"`). Either way, success means the registration is gone.
- `relocate({ sourceMod, sourceId, x, y, z, sprite?, shadow?, sourceData? })` checks the destination first, creates the new Tile, then removes the old one. On any failure the old Tile is left untouched. Relocating recreates the object, so a Container Tile's contents do not move with it.

---

## Updating a Tile

| Call | Option |
|:---|:---|
| `setSprite` | `sprite` |
| `setIcon` | `icon` (`false` clears it) |
| `setCapacity` | `capacity` |
| `setShadow` | `shadow` (`true` or `false`) |
| `setSourceData` | `sourceData` (`false` clears it) |

Each one updates the stored record, the live object if its square is loaded and every connected client.

---

## Source Data

`sourceData` is the calling Mod's own data, stored with the Tile. It accepts strings (up to 256 characters), finite numbers, booleans and nested tables (up to 4 levels deep, 64 entries and 2048 bytes in total). Table keys must be identifier-style strings (up to 32 characters) or small positive integers. Functions, userdata, cycles and oversized data return `invalid_source_data`.

Clients read it from the placed object as `obj:getModData().NPCTilesSource`, which holds `{ mod, id, data }`. Check `mod` before reading `data`. Use it for display and interaction routing only. Make every permission decision on the server.

---

## Actions Started by a Player

The calling Mod's client sends a command to the calling Mod's own server handler. That handler takes the Player from `OnClientCommand`, checks permission, range, cooldown and game state, works out `sourceMod`, `sourceId`, sprite and coordinates from trusted server state, then calls the API. The NPC Tiles `place` command for its own UI stays admin-only.

---

## Failure Reasons

| Reason | Meaning |
|:---|:---|
| `server_only` | Called on a remote client |
| `not_ready` | The server side of the API has not loaded yet |
| `invalid_options` | A missing or malformed option |
| `invalid_coordinates` | Coordinates that are not whole numbers or are out of range |
| `invalid_sprite` | The sprite is not an NPC Tiles sprite |
| `invalid_icon` | The icon is not a Container Icon key |
| `invalid_source_data` | `sourceData` breaks the limits above |
| `npc_tile_exists` | A Tile is already registered at the coordinates |
| `occupied_by_other_object` | Another object using an NPC Tiles sprite is on the square |
| `source_id_conflict` | The `sourceId` is already used at other coordinates, or twice in saved data |
| `object_creation_failed` | The game could not create the object |
| `not_found` | No matching Tile |
| `not_owner` | The Tile belongs to another Mod or to the admin tools |

---

## Example

A vendor Mod that makes sure each vendor has its NPC Tile:

```lua
if isClient() and not isServer() then return end
require "NPCTiles_API"

local function ensureVendor(vendor)
    local available, reason = NPCTiles_API.isAvailable(1)
    if not available then return false, reason end
    local existing = NPCTiles_API.getBySourceId("MyModId", vendor.id)
    if existing then return true, existing end
    return NPCTiles_API.place({
        x = vendor.x, y = vendor.y, z = vendor.z,
        sprite = vendor.sprite,
        sourceMod = "MyModId",
        sourceId = vendor.id,
        sourceData = { side = vendor.side },
    })
end
```

---

## Compatibility

Version 1 only grows: its functions and results will not change within version 1. Existing NPC Tiles Saves load unchanged. The `sourceMod`, `sourceId` and `sourceData` fields are added only to Tiles placed through the API.

---
