# **Documentation**

<div class="section-banner" markdown>

![Documentation Banner](https://i.obnox.dev/NoxDocsDocumentation)

</div>

This section is for Modders and Developers who want to build on top of or integrate into **ObnoxiouslyNoxious's** Project Zomboid Mods. 
Documentation is split into two Categories:

| Category |Purpose| Integration |
|:---|:---|:---|
| **Framework** | Provides the core structure for a Mod to build on, leaving its Author free to focus on content instead of recreating the foundation | Register the Mod with the Framework, then build within the structure it provides |
| **API** | Offers a set of functions that let one Mod use another Mod's features directly | Check the API is loaded, then call its functions from the Mod's own code |

## Framework

<div class="grid cards" markdown>

-   **[Menu Theme Framework](menu-theme-framework/index.md)**
    <span class="pz-tag">B42</span><span class="pz-tag">Framework</span>

    The Framework for building Main Menu Themes with custom Audio, Images and Video. No Java and no manual installation.

</div>

## API

<div class="grid cards" markdown>

-   **[Dynamic Challenges API](api/dynamic-challenges.md)**
    <span class="pz-tag">B42</span><span class="pz-tag">API</span>

    Lets other Mods read Challenge progress and react to Challenge events.

-   **[NPC Tiles API](api/npc-tiles.md)**
    <span class="pz-tag">B42</span><span class="pz-tag">API</span>

    Lets other Mods place and manage persistent NPC Tiles from server-side code.

-   **[XP Ranks API](api/xp-ranks.md)**
    <span class="pz-tag">B42</span><span class="pz-tag">API</span>

    Lets other Mods award Rank XP, read Ranks and react to Rank Ups.

</div>
