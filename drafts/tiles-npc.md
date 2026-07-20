# **NPC Tiles**

<div class="mod-hero" markdown>

![NPC Tiles](../assets/img/mods/npc-tiles.png){ .mod-icon }

<span class="pz-tag">B42</span><span class="pz-tag">SP/MP</span>

*Place static human-figure tiles for decoration, dioramas, or staged scenes — plus a storage variant.*

**Build:** 42.0+ | **SP/MP:** Singleplayer & Multiplayer

[:fontawesome-brands-steam-symbol: Steam Workshop](#)

</div>

## Overview

NPC Tiles is a **Build 42 compatibility port** of [Destiny & Vass's original NPC Tiles mod](https://steamcommunity.com/sharedfiles/filedetails/?id=3344981715), ported for B42 by ObnoxiouslyNoxious. It adds placeable, static human-figure tile objects — useful for decoration, dioramas, or staging a scene — plus a container variant with 50 storage capacity for hiding loot or props in plain sight. A Military texture set is included alongside the standard set.

## Gallery

<!--
<div class="gallery-grid" markdown>
![Caption 1](../assets/img/mods/gallery/tiles-npc/1.png) ![Caption 2](../assets/img/mods/gallery/tiles-npc/2.png)
</div>
-->

## Features

- Placeable static human-figure tiles via a right-click context menu
- Container variant (50 storage capacity) alongside the plain decorative tile
- Standard and Military texture packs
- Tile picker window with a scrollable sprite grid for choosing which figure to place
- Placed tiles are protected from the standard destroy tool — removal is a deliberate, separate action
- Translations for all 28 PZ-supported languages

## Installation

Subscribe to the mod on Steam Workshop and add it to your mod list — no server-side files are required:

```ini
Mods=[B42]NPCTiles
```

## How It Works

Right-click a tile in the world to bring up **Place NPC Tile** or **Place NPC Container Tile** in the context menu. This opens a picker window showing every available sprite in a scrollable grid — click one to place it at the target square.

!!! note "Placement is staff/admin-gated"
    The context menu options only appear for players with admin tools (or admin status) in multiplayer — this is intended as a building/decoration tool for server staff and map builders, not a general player-facing feature. In singleplayer it's available to everyone.

Once placed, a tile is protected from the normal destroy-object tool. To remove one, right-click it and use **Remove NPC Tile** from the context menu instead.

## Configuration

No Sandbox options — the mod has no configurable settings.

## Compatibility

| Build |  SP | Hosted MP | Dedicated MP
|:---:|:---:|:---:|:---:|
| 42.0+ | ✅ | ✅ | ✅ |
| 41 | ❌ | ❌ | ❌ |

## FAQ / Troubleshooting

!!! question "I don't see the 'Place NPC Tile' option in my context menu."

    In multiplayer, only players with admin tools or admin status can place tiles. Check your permissions, or try in singleplayer.

!!! question "I can't destroy a placed tile with the normal destroy tool."

    That's intentional — placed tiles are protected from accidental destruction. Right-click the tile and choose **Remove NPC Tile** instead.

## Credits

- Original mod and sprite work by [Destiny](https://steamcommunity.com/id/destinyy55) and [Vass](https://steamcommunity.com/profiles/76561198003329839) — [original Workshop page](https://steamcommunity.com/sharedfiles/filedetails/?id=3344981715)
- Build 42 compatibility port by ObnoxiouslyNoxious

## Changelog

**v1.0.1**

- Added NPC Container Tiles with 50 storage capacity, placeable via **Place NPC Container Tile**
- Added translations for all 28 PZ-supported languages
- Added context menu and container icons

See the mod's Steam Workshop page for the full version history.
