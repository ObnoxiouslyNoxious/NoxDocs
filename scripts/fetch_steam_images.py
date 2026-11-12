"""Download each Mod's Steam Workshop images into docs/assets/img/mods/steam/<slug>/.

Steam is the one place images are managed; NoxDocs pages point at the files this script writes.

    python scripts/fetch_steam_images.py              every Mod listed in scripts/steam_mods.json
    python scripts/fetch_steam_images.py --mod zombies-have-money
    python scripts/fetch_steam_images.py --force      download again even if unchanged
    python scripts/fetch_steam_images.py --live-only  only Mods that have a page (used by the deploy workflow)

A Mod that has a page (docs/mods/<slug>.md) is written to docs/assets/img/mods/steam/<slug>/. Any other Mod goes to
drafts/img/mods/steam/<slug>/ (outside docs, gitignored), so nothing unpublished is deployed; run the script again once the
page exists and the images move across.

Output per Mod: preview.<ext> (the Workshop item's main image, often an animated GIF) and 1.<ext>, 2.<ext> ... (the gallery,
in Steam's order). manifest.json beside them records the Steam source of each file so an unchanged image is skipped.

It reads the public Workshop page (no API key). If Steam changes that page, the gallery list comes back empty and the script
stops with an error instead of leaving a half-updated folder.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIVE_ROOT = os.path.join(ROOT, 'docs', 'assets', 'img', 'mods', 'steam')
DRAFT_ROOT = os.path.join(ROOT, 'drafts', 'img', 'mods', 'steam')
MODS_FILE = os.path.join(ROOT, 'scripts', 'steam_mods.json')
PAGE = 'https://steamcommunity.com/sharedfiles/filedetails/?id={id}'
FULL = '?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36'
UGC = r'https://images\.steamusercontent\.com/ugc/[0-9]+/[0-9A-F]+/'


def get(url, tries=6):
    wait = 10
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'en-US,en;q=0.9'})
            return urllib.request.urlopen(req, timeout=60).read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < tries - 1:
                print('  Steam answered %d, waiting %d s before retrying' % (e.code, wait), flush=True)
                time.sleep(wait)
                wait = min(wait * 2, 60)
                continue
            raise SystemExit('Steam refused the request (HTTP %d) for %s; wait a few minutes and run again' % (e.code, url))
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
            if attempt < tries - 1:
                print('  network problem (%s), waiting %d s before retrying' % (type(e).__name__, wait), flush=True)
                time.sleep(wait)
                wait = min(wait * 2, 60)
                continue
            raise SystemExit('network problem for %s: %s' % (url, e))
    raise RuntimeError('unreachable')


def ext_of(data):
    if data[:6] in (b'GIF87a', b'GIF89a'):
        return 'gif'
    if data[:8] == b'\x89PNG\r\n\x1a\n':
        return 'png'
    if data[:3] == b'\xff\xd8\xff':
        return 'jpg'
    if data[:4] == b'RIFF' and data[8:12] == b'WEBP':
        return 'webp'
    raise ValueError('unknown image format')


def tail(url):
    return url.rstrip('/').rsplit('/', 1)[-1]


def read_page(item_id):
    html = get(PAGE.format(id=item_id)).decode('utf-8', 'replace')
    gallery = re.findall(r'id="thumb_screenshot_\d+"\s*>\s*<img src="(' + UGC + r')', html)
    main = re.search(r"ShowEnlargedImagePreview\(\s*'(" + UGC + r")", html)
    return gallery, (main.group(1) if main else None)


def sync_mod(slug, item_id, force):
    gallery, main = read_page(item_id)
    if not gallery and not main:
        raise SystemExit('%s (%s): no images found on the Workshop page; Steam may have changed it' % (slug, item_id))
    if not gallery:
        print('  no gallery screenshots on the Workshop page yet, taking the main image only')
    live = os.path.exists(os.path.join(ROOT, 'docs', 'mods', slug + '.md'))
    folder = os.path.join(LIVE_ROOT if live else DRAFT_ROOT, slug)
    other = os.path.join(DRAFT_ROOT if live else LIVE_ROOT, slug)
    if os.path.isdir(other) and not os.path.isdir(folder):
        os.makedirs(os.path.dirname(folder), exist_ok=True)
        os.replace(other, folder)
        print('  moved the images from %s' % os.path.relpath(other, ROOT))
    os.makedirs(folder, exist_ok=True)
    manifest_path = os.path.join(folder, 'manifest.json')
    old = {}
    if os.path.exists(manifest_path):
        old = json.load(open(manifest_path, encoding='utf-8'))
    manifest = {}
    entries = []
    if main:
        entries.append(('preview', main))
    n = 0
    for url in gallery:
        if main and tail(url) == tail(main):
            continue
        n += 1
        entries.append((str(n), url))
    for key, url in entries:
        prev = old.get(key)
        if prev and prev['url'] == url and not force and os.path.exists(os.path.join(folder, prev['file'])):
            manifest[key] = prev
            print('  %-8s unchanged  %s' % (key, prev['file']))
            continue
        data = get(url + FULL)
        name = '%s.%s' % (key, ext_of(data))
        for stale in os.listdir(folder):
            if stale.rsplit('.', 1)[0] == key and stale != 'manifest.json':
                os.remove(os.path.join(folder, stale))
        open(os.path.join(folder, name), 'wb').write(data)
        manifest[key] = {'file': name, 'url': url}
        print('  %-8s downloaded %s (%d KB)' % (key, name, len(data) // 1024))
        time.sleep(0.4)
    keep = {m['file'] for m in manifest.values()} | {'manifest.json'}
    for f in os.listdir(folder):
        if f not in keep:
            os.remove(os.path.join(folder, f))
            print('  removed  %s (no longer on Steam)' % f)
    json.dump(manifest, open(manifest_path, 'w', encoding='utf-8'), indent=2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mod')
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--live-only', action='store_true', help='skip Mods without a page in docs/mods/')
    args = ap.parse_args()
    mods = json.load(open(MODS_FILE, encoding='utf-8'))
    if args.mod:
        if args.mod not in mods:
            sys.exit('%s is not in scripts/steam_mods.json' % args.mod)
        mods = {args.mod: mods[args.mod]}
    if args.live_only:
        mods = {s: i for s, i in mods.items() if os.path.exists(os.path.join(ROOT, 'docs', 'mods', s + '.md'))}
    for slug, item_id in mods.items():
        print(slug, item_id)
        sync_mod(slug, item_id, args.force)
        time.sleep(1.5)


if __name__ == '__main__':
    main()
