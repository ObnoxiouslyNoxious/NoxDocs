# **Zombies Have Money**

<div class="mod-hero" markdown>

![Zombies Have Money](../assets/img/mods/Money.png){ .mod-icon }

<span class="pz-tag">B42</span><span class="pz-tag">SP/MP</span>

[:fontawesome-brands-steam-symbol: Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3728275018)

**Recommended Build:** 42.15+

</div>

## Overview

Adds a configurable chance for Zombies to drop Money & Money Bundles on death, on top of vanilla drop behaviour.

## Gallery

<div class="gallery-grid" markdown>
![Zombies Have Money screenshot 1](../assets/img/mods/gallery/zombies-have-Money/ZHM1.png) ![Zombies Have Money screenshot 2](../assets/img/mods/gallery/zombies-have-Money/ZHM2.png) ![Zombies Have Money screenshot 3](../assets/img/mods/gallery/zombies-have-Money/ZHM3.png) ![Zombies Have Money screenshot 4](../assets/img/mods/gallery/zombies-have-Money/ZHMSS1.png) ![Zombies Have Money screenshot 5](../assets/img/mods/gallery/zombies-have-Money/ZHMSS2.png)
</div>


## Features

- Configurable chance for Zombies to drop Money on death
- Adjustable minimum/maximum bill count per drop
- Fully server-side spawning — no client drop logic, no duplication risk

## How It Works

Every time a Zombie is killed, the mod first rolls for a Money Bundle drop. If that roll succeeds, a random number of Money Bundles is added to the Zombie's inventory and the check ends there.

If the Bundle roll fails, the Mod then rolls for individual Money Bills. If that roll succeeds, a random amount of Money between Minimum Bills and Maximum Bills is added instead. A Zombie will never drop both Bundles and individual Bills on the same kill.

The drop rolls only on the Server, preventing item duplication and desync in Multiplayer.

## Installation

**Singleplayer:** Subscribe to the Mod on Steam Workshop and enable it from the 'Choose Mods' screen.

**Multiplayer (Hosted & Dedicated):** Subscribe to the Mod on Steam Workshop and add the below lines to your Server's .ini file

```ini
Mods=ZombiesHaveMoneyB42
WorkshopItems=3728275018
```

## Configuration

Found under the **Zombies Have Money** tab in Custom Sandbox options.

| Setting | Default | Range | Description |
|:---:|:---:|:---:|:---:|
| Money Drop Chance | 50% | 0–100% | Chance a Zombie drops Money on death |
| Minimum Bills | 5 | 1–100 | Minimum Money items dropped |
| Maximum Bills | 30 | 1–100 | Maximum Money items dropped |
| Enable Money Bundles | Off | On/Off | Toggle Money Bundle spawning |
| Money Bundle Drop Chance | 5% | 0-100% | Chance a Zombie drops Money Bundles on death |
| Minimum Bundles | 1 | 1–100 | Minimum Money Bundles dropped |
| Maximum Bills | 1 | 1–100 | Maximum Money Bundles dropped |

!!! note
    If Minimum Bills/Bundles is set higher than Maximum Bills/Bundles by mistake, the mod silently swaps the two values to prevent a crash.

## Compatibility

| Build |  SP | Hosted MP | Dedicated MP
|::---::|::---::|::---::|::---::|
| 42 | ✅ | ✅ | ✅ |
| 41 | ❌ | ❌ | ❌ |

!!! success 

    Safe to add to existing saves and safe to remove, though any Money already looted from Zombies will remain in your save.

!!! success  

    Compatible with all other loot mods. Does not modify any existing loot tables or distributions. 

!!! success 

    Includes Translations for all 28 Supported Project Zomboid languages.

## Credits

This mod was inspired by Chromaa's 'More Money On Zombies' mod which has since been removed from The Workshop.

## Changelog

[:fontawesome-brands-steam-symbol: View Patch Notes](https://steamcommunity.com/sharedfiles/filedetails/changelog/3728275018)