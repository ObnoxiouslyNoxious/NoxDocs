# **<Mod Name>**

<div class="mod-hero" markdown>

![<Mod Name>](../assets/img/mods/<slug>.png){ .mod-icon }

<span class="pz-tag">B42</span><span class="pz-tag">SP/MP</span>

[:fontawesome-brands-steam-symbol: Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=<WorkshopID>)

**Recommended Build:** 42.x+

</div>

## Overview

2-4 sentences: what the mod does and why it exists.

## Gallery

<div class="gallery-grid" markdown>
![<Mod Name> screenshot 1](../assets/img/mods/gallery/<slug>/1.png) ![<Mod Name> screenshot 2](../assets/img/mods/gallery/<slug>/2.png)
</div>

## Features

- Feature one
- Feature two

## How It Works

Explain the core mechanic — what triggers it, the order rolls/checks happen in, and a note that spawning/logic runs server-side only (if applicable) to reassure multiplayer safety.

## Installation

**Singleplayer:** Subscribe to the Mod on Steam Workshop and enable it from the 'Choose Mods' screen.

**Multiplayer (Hosted & Dedicated):** Subscribe to the Mod on Steam Workshop and add the below lines to your Server's .ini file

```ini
Mods=<ModID>
WorkshopItems=<WorkshopID>
```

## Configuration

Found under the **<Mod Name>** tab in Custom Sandbox options.

| Setting | Default | Range | Description |
|:---:|:---:|:---:|:---:|
| Example Setting | `true` | — | Description |

## Compatibility

| Build |  SP | Hosted MP | Dedicated MP
|:---:|:---:|:---:|:---:|
| 42.x | ✅ | ✅ | ✅ |
| 41 | ❌ | ❌ | ❌ |

!!! success "Is this Mod safe to add/remove to existing Saves?"

    Yes, it is safe to add to existing saves and safe to remove, though any items already spawned by the mod will remain in your save.

!!! success "Is this Mod compatible with 'X' Mod?"

    Yes, compatible with all other loot mods. Does not modify any existing loot tables or distributions.

!!! success "Does this Mod support 'X' Language?"

    Yes, this Mod has translations for all 28 Supported Project Zomboid languages.

## FAQ / Troubleshooting

!!! question "Question?"

    Answer.

## Credits

- Credit or inspiration notes go here.

## Changelog

[:fontawesome-brands-steam-symbol: View Patch Notes](https://steamcommunity.com/sharedfiles/filedetails/changelog/<WorkshopID>)
