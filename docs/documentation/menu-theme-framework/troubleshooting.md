# Troubleshooting

## Troubleshooting

Where to look when a Theme misbehaves, the fixes for the common symptoms and the checklists to run before and after uploading.

---

## Debugging

Problems a Player should put in a bug report (a Video that cannot open, a missing Logo or font, a Track that will not play, an unknown blend mode) print as `[MTF][WARNING]` lines **even with debug off**. `MTF_warn` and `MTF_warnOnce` do this for MTF. Give the Theme the same helper. Never hide a real warning behind a debug flag.

Set `MenuThemeFramework.Config.DEBUG = true` while developing and read the console (`Zomboid/console.txt`). MTF logs registration, the Main Menu lifecycle, holds and releases, the Buttons panel, Music, Video and Settings as `[MTF][DEBUG][SUBSYSTEM]` lines. Errors and warnings print as `[MTF][ERROR]` and `[MTF][WARNING]` regardless of the switch. `DEBUG` cannot be set through `registerTheme`'s `config` table.

Print the Theme's own debug lines through the same switch with `ctx.dprint(fmt, ...)`. For a tag of its own, give the Theme an `[ABBR]_Config.DEBUG` flag and an `[ABBR]_dprint` helper (RDR Menu Theme's `shared/RMT_Config.lua` is a small example).

!!! warning "Ship with Debug Off"
    `DEBUG = false` in anything uploaded.

---

## Symptoms and Fixes

| Symptom | Likely cause |
|:---|:---|
| **Main Menu is blank, or the Buttons never appear** | `holdUntilReady` is set and the Theme never released, or an error is repeating in a callback. Check the console. Release before anything that can fail |
| **No Music** | The Sound name does not match the Sound Script, the script has a comment in it, or the path in `file =` is wrong |
| **Music never advances** | That Track has no `lengthMs`, or the Theme sets `musicRepeatOne` |
| **Music keeps playing after removing the Theme** | Report it. MTF stops Music when the Theme is removed in the Mods screen |
| **Image missing, or a 1x1 placeholder** | Check the path and extension exactly. Avoid generic names such as `blank.png` (the game may supply its own placeholder) |
| **The Theme is ignored** | Another Theme registered first. Only one Theme runs; the Menu Theme Settings window lists the ignored ones as inactive |
| **Frame hitch when something first appears** | Preload it with `getTexture(path)` at file load |
| **Video shows a still Image** | The game is older than 42.22, Video Effects is off, the file is missing or invalid, or `srcW`/`srcH` is wrong. See [Video](video.md) |
| **A style value does nothing** | It was reported and ignored, with an `[MTF][WARNING]` line in the console naming the field |
| **Buttons jump or grow after appearing** | `reveal.waitForLayout` was turned off |
| **Something repeats an error every frame** | A callback has a `nil` it did not guard. MTF does not catch errors in Theme callbacks |
| **Cards show a default Graphic** | The convention name is wrong (it is `<assetPrefix>_Card_<BUTTONID>.png` in `media/ui/cards/backgrounds/`) |
| **A Main Menu Button is missing** | The Player hid it in the Menu Theme Settings window (UI tab) |

Large Image sets use a lot of video memory. See [Memory Usage](images.md#memory-usage).

---

## Reloading While Working

With the game in Debug Mode, the **Reload Lua** button becomes available. Reloading re-registers the Theme in place (same `id`). Values can be tuned without restarting the game.

### Turning On Debug Mode

Debug Mode is turned on by starting Project Zomboid with the `-debug` launch option.

**Through Steam:**

1. Open the Steam **Library**.
2. Right-click **Project Zomboid** and choose **Properties**.
3. On the **General** tab, add `-debug` to **Launch Options**.
4. Start the game as normal. Remove `-debug` again to play without it.

**Through a Windows shortcut:**

1. Right-click `ProjectZomboid64.exe` in the game's install folder (`Steam/steamapps/common/ProjectZomboid/`) and choose **Create shortcut**.
2. Right-click the shortcut, choose **Properties** and add ` -debug` to the end of **Target**, after the closing quote.
3. Start the game from that shortcut whenever Debug Mode is needed.

!!! note "Two Different Debug Switches"
    The game's Debug Mode (`-debug`) and MTF's `Config.DEBUG` are separate. `-debug` unlocks the game's developer tools such as Reload Lua. `Config.DEBUG` only adds MTF's `[MTF][DEBUG]` lines to the console.

---

## Before Uploading

- [ ] `Config.DEBUG` is `false`.
- [ ] `42/mod.info` matches the root `mod.info`.
- [ ] `require=ObnoxMenuThemeFrameworkB42` is set in both.
- [ ] Every Sound Script is free of comments.
- [ ] Every texture path includes its extension and matches the file on disk.
- [ ] Files use the Theme's own Prefix.
- [ ] The files MTF finds by name match [Files MTF Finds by Name](reference.md#files-mtf-finds-by-name).
- [ ] Release calls for a held Main Menu happen before anything that can fail.
- [ ] The Theme has been tested with the Menu Theme Settings window open and with each of its Layouts.
- [ ] Video Themes: tested with Video Effects on and off.
- [ ] Video Themes: a fallback `.png` is shipped for every Video.

---

## After Uploading

- [ ] Menu Theme Framework is listed as a Required Item on the Theme's Workshop page.

---
