# **NPC Tiles**

<div class="mod-hero" markdown>

![NPC Tiles](../assets/img/mods/steam/npc-tiles/preview.gif){ .mod-icon }

<span class="pz-tag">B42</span><span class="pz-tag">SP/MP</span>

[:fontawesome-brands-steam-symbol: Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3759853561)

**Recommended Build:** 42.15+

</div>

## Overview

NPC Tiles is a **Build 42 compatibility port** of [Destiny and Vass's original NPC Tiles Mod](https://steamcommunity.com/sharedfiles/filedetails/?id=3344981715). It provides 532 placeable, static human NPC Tiles for roleplay servers, events, missions, screenshots, storytelling, map making, base building and NPC-themed decoration. The collection includes the original 84 Tiles, 384 Tiles by Nox and 64 Tiles by Creator.

The Mod also provides NPC Container Tiles with configurable storage Capacity, selectable Container Icons, an optional Shadow under each Tile, Multiplayer-safe persistence and a [public API](../documentation/api/npc-tiles.md) for other Mods to place and manage NPC Tiles from server-side code.

## Gallery

<div class="gallery-grid" markdown>
![NPC Tiles screenshot 1](../assets/img/mods/steam/npc-tiles/1.jpg) ![NPC Tiles screenshot 2](../assets/img/mods/steam/npc-tiles/2.jpg) ![NPC Tiles screenshot 3](../assets/img/mods/steam/npc-tiles/3.jpg) ![NPC Tiles screenshot 4](../assets/img/mods/steam/npc-tiles/4.jpg) ![NPC Tiles screenshot 5](../assets/img/mods/steam/npc-tiles/5.jpg) ![NPC Tiles screenshot 6](../assets/img/mods/steam/npc-tiles/6.jpg) ![NPC Tiles screenshot 7](../assets/img/mods/steam/npc-tiles/7.jpg) ![NPC Tiles screenshot 8](../assets/img/mods/steam/npc-tiles/8.jpg) ![NPC Tiles screenshot 9](../assets/img/mods/steam/npc-tiles/9.jpg) ![NPC Tiles screenshot 10](../assets/img/mods/steam/npc-tiles/10.jpg) ![NPC Tiles screenshot 11](../assets/img/mods/steam/npc-tiles/11.jpg) ![NPC Tiles screenshot 12](../assets/img/mods/steam/npc-tiles/12.jpg) ![NPC Tiles screenshot 13](../assets/img/mods/steam/npc-tiles/13.jpg) ![NPC Tiles screenshot 14](../assets/img/mods/steam/npc-tiles/14.jpg) ![NPC Tiles screenshot 15](../assets/img/mods/steam/npc-tiles/15.jpg) ![NPC Tiles screenshot 16](../assets/img/mods/steam/npc-tiles/16.jpg) ![NPC Tiles screenshot 17](../assets/img/mods/steam/npc-tiles/17.jpg) ![NPC Tiles screenshot 18](../assets/img/mods/steam/npc-tiles/18.jpg) ![NPC Tiles screenshot 19](../assets/img/mods/steam/npc-tiles/19.jpg) ![NPC Tiles screenshot 20](../assets/img/mods/steam/npc-tiles/20.jpg) ![NPC Tiles screenshot 21](../assets/img/mods/steam/npc-tiles/21.jpg)
</div>

## Features

- 532 placeable static human NPC Tiles
- The original Destiny and Vass Tiles, plus collections by Nox and Creator
- Creator tabs and category tabs for organising the Tilesheets
- Standard, civilian, suit, coverall, homesteader, gang and military NPC characters
- Placeable NPC Container Tiles with a default Capacity of 50
- 48 selectable Container Icons when placing a Container Tile
- Configurable Container Capacity from 1 to 10000
- Change the Container Icon or edit the Capacity of an existing NPC Container Tile
- An optional Shadow drawn under the NPC Tile
- Tile picker windows with scrollable sprite grids
- Griefer-resistant Tiles that cannot be set on fire, dismantled, picked up, destroyed or Sledgehammered
- Tiles that persist through Multiplayer server restarts
- Safe to add to or remove from existing Saves
- Translations for all supported Project Zomboid languages
- A [public API](../documentation/api/npc-tiles.md) for other Mods to place and manage NPC Tiles

## Installation

**Singleplayer:** Subscribe to the Mod on the Steam Workshop and enable it from the 'Choose Mods' screen.

**Multiplayer (Hosted and Dedicated):** Subscribe to the Mod on the Steam Workshop and add the lines below to the server's `.ini` file.

```ini
Mods=[B42]NPCTiles
WorkshopItems=3759853561
```

## How It Works

Right-click anywhere in the World and select **Place NPC Tile** or **Place NPC Container Tile** from the Context menu. Confirm the placement location, then choose a creator tab and (where available) a category tab before selecting the NPC Tile to place. The picker also offers an optional Shadow under the Tile.

For a Container Tile, select a Container Icon and set its Capacity after choosing the NPC Tile. The default Capacity is 50, with a range of 1 to 10000.

Right-click an existing NPC Container Tile and select **Change NPC Container Icon** to change its icon, or **Edit NPC Container Capacity** to change its Capacity.

Once placed, a Tile is protected from fire, being dismantled, picked up, destroyed or Sledgehammered. Tiles persist through Multiplayer server restarts.

To remove an NPC Tile, right-click it and select **Remove NPC Tile** from the Context menu.

Place NPC Tiles through the Context menu. The Debug Mode Brush Tool creates a destructible version.

!!! note "Multiplayer Placement Needs Admin Access"
    In Multiplayer, the Context menu options only appear for Players with Admin access.

## Public API

Other Build 42 Mods can place and manage persistent NPC Tiles from server-side code through `NPCTiles_API` (version 1). See the [NPC Tiles API](../documentation/api/npc-tiles.md) page for the full reference.

## Compatibility

| Build | SP | Hosted MP | Dedicated MP |
|:---:|:---:|:---:|:---:|
| 42.15+ | ✅ | ✅ | ✅ |
| 41 | ❌ | ❌ | ❌ |

!!! note "Multiplayer Capacity Support"
    Capacities from 1 to 100 work directly. Capacities above 100 (up to 10000) need [Multiplayer Weight Limit Breaker](https://steamcommunity.com/sharedfiles/filedetails/?id=3641432632) in Multiplayer. Singleplayer supports the full range without it.

!!! success "Is this Mod safe to add to or remove from existing Saves?"
    Yes. NPC Tiles can be added to and removed from existing Saves. Tiles already placed by the Mod are removed with the Mod's data when they are cleaned up.

## FAQ / Troubleshooting

!!! question "I don't see the 'Place NPC Tile' option in my Context menu."
    In Multiplayer, only Players with Admin access can place Tiles. Check the account's access level, or try in Singleplayer.

!!! question "How many NPC Tiles are included?"
    532 human NPC Tiles: the 84 original Tiles, 384 Tiles by Nox and 64 Tiles by Creator.

!!! question "Why do larger Container Capacities need another Mod in Multiplayer?"
    Multiplayer Capacities above 100 need [Multiplayer Weight Limit Breaker](https://steamcommunity.com/sharedfiles/filedetails/?id=3641432632). Singleplayer supports Capacities up to 10000 without it.

!!! question "Why use the Context menu instead of the Debug Brush Tool?"
    Placing through the Context menu creates the protected, persistent version of the NPC Tile. The Debug Brush Tool creates a destructible version.

!!! question "Can another Mod place NPC Tiles?"
    Yes, through the server-authoritative `NPCTiles_API` (version 1). The other Mod must require NPC Tiles and can only edit or remove the Tiles it placed itself. See the [NPC Tiles API](../documentation/api/npc-tiles.md).

## Credits

- Build 42 compatibility work and framework by [ObnoxiouslyNoxious](https://steamcommunity.com/id/ObnoxiouslyNoxious)
- Original Mod and Sprites by [Destiny](https://steamcommunity.com/id/destinyy55) and [Vass](https://steamcommunity.com/profiles/76561198003329839): [Original Mod's Workshop Page](https://steamcommunity.com/sharedfiles/filedetails/?id=3344981715)
- Additional Tiles by Creator
- Special thanks to RedChili for the [PZ Survivor Studio Tool](https://pz-icon-maker.vercel.app/)

## Changelog

[:fontawesome-brands-steam-symbol: View Patch Notes](https://steamcommunity.com/sharedfiles/filedetails/changelog/3759853561)
