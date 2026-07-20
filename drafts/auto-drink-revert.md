# **Auto-Drink Revert**

<div class="mod-hero" markdown>

![Auto-Drink Revert](../assets/img/mods/auto-drink.png){ .mod-icon }

<span class="pz-tag">B42.19+</span><span class="pz-tag">SP/MP</span>

*God Drink, Fight Milk, Combat Drink — if it's mostly water, auto-drink it. Just like old times.*

**Build:** 42.19+ only | **SP/MP:** Singleplayer & Multiplayer

[:fontawesome-brands-steam-symbol: Steam Workshop](#)

</div>

## Overview

In Build 42.19, The Indie Stone changed the vanilla auto-drink system: `getWaterSource()` now calls `isWaterOnlySource()` instead of `isWaterSource()`, meaning auto-drink only triggers from containers where **every** fluid present is water — effectively requiring 100% water-only contents. Previously, `isWaterSource()` only required water to be the *primary* fluid by volume, so a bottle that was 51% water and 49% another fluid still qualified.

This mod reverts that change, restoring the pre-42.19 behavior: your character auto-drinks from any container where water is the primary fluid by volume again.

## Gallery

<!--
<div class="gallery-grid" markdown>
![Caption 1](../assets/img/mods/gallery/auto-drink-revert/1.png) ![Caption 2](../assets/img/mods/gallery/auto-drink-revert/2.png)
</div>
-->

## Features

- Restores pre-42.19 auto-drink behavior (primary-fluid-by-volume, not water-only)
- Standalone, clean fix using existing game functions — no other mod dependencies
- Preserves all other vanilla behavior, including the minimum fluid amount threshold
- Multiplayer-safe: calls `syncItemFields()` after drinking so the item stays in sync

## How It Works

The mod hooks into the `AutoDrink` function in `IsoGameCharacter.java`, suppressing the vanilla auto-drink logic entirely and replacing it with a re-implementation that uses `isWaterSource()` instead of `isWaterOnlySource()`.

## Installation

Subscribe to the mod on Steam Workshop and add it to your mod list — no server-side files are required:

```ini
Mods=AutoDrinkRevert
```

## Configuration

No configuration required — this mod has no Sandbox options.

## Compatibility

| Build |  SP | Hosted MP | Dedicated MP
|:---:|:---:|:---:|:---:|
| 42.19+ | ✅ | ✅ | ✅ |
| Build 42 < 42.19, or Build 41 | ❌ | ❌ | ❌ |

This mod does not alter any game files and should be compatible with any other mod that doesn't also hook into `AutoDrink`. Safe to add or remove mid-save.

## FAQ / Troubleshooting

!!! question "Will this let me auto-drink from something like pure orange juice?"

    No — unlike some other auto-drink mods, this one still requires water to be the *primary* fluid. A 100% non-water container (e.g. pure orange juice) will never trigger auto-drink.

!!! question "Why does this exist if the vanilla behavior is intentional?"

    It restores the pre-42.19 behavior for players who preferred the old, more permissive auto-drink threshold.

## Credits

- [Steam Workshop](#)

## Changelog

See the mod's Steam Workshop page for the full version history.
