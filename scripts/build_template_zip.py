"""Build the Menu Theme Template download for NoxDocs.

Zips a MenuThemeTemplate mod folder into the Workshop layout a reader unzips
straight into Zomboid/Workshop/:

    MenuThemeTemplate/Contents/mods/MenuThemeTemplate/...

The zip is deterministic (sorted entries, fixed timestamps), so an unchanged
Template always produces identical bytes.

Usage:
    python build_template_zip.py <MenuThemeTemplate folder> <output .zip>

Sources:
    - Published copy:  F:/SteamLibrary/steamapps/workshop/content/108600/3836836552/mods/MenuThemeTemplate
    - MTF repo (CI):   <checkout>/Contents/mods/MenuThemeTemplate
"""
import os
import sys
import zipfile

ROOT_IN_ZIP = "MenuThemeTemplate/Contents/mods/MenuThemeTemplate"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
SKIP_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini"}


def build(src, out):
    if not os.path.isfile(os.path.join(src, "mod.info")):
        sys.exit("not a mod folder (no mod.info): %s" % src)
    files = []
    for dirpath, dirnames, filenames in os.walk(src):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith(".git"))
        for name in sorted(filenames):
            if name in SKIP_NAMES:
                continue
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, src).replace(os.sep, "/")
            files.append((rel, full))
    files.sort()
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for rel, full in files:
            info = zipfile.ZipInfo(ROOT_IN_ZIP + "/" + rel, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            with open(full, "rb") as fh:
                zf.writestr(info, fh.read())
    print("wrote %s (%d files, %.1f MB)" % (out, len(files), os.path.getsize(out) / 1048576))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    build(sys.argv[1], sys.argv[2])
