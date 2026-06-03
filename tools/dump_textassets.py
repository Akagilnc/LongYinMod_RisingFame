"""Dump named TextAssets (game design tables) from resources.assets to files."""
import sys
import os
import UnityPy

ASSETS = r"D:\SteamLibrary\steamapps\common\LongYinLiZhiZhuan\LongYinLiZhiZhuan_Data\resources.assets"
OUTDIR = r"D:\WorkSpace\LongYinMod_RisingFame\docs\reference\game-tables"

# Names to dump. If empty, dump every TextAsset whose content looks like a
# CSV/JSON design table (has a BOM/Chinese header or starts with [ or {).
WANT = set(sys.argv[1:])

os.makedirs(OUTDIR, exist_ok=True)
env = UnityPy.load(ASSETS)

def get_text(obj):
    data = obj.read()
    name = getattr(data, "m_Name", None) or getattr(data, "name", "")
    script = getattr(data, "m_Script", None)
    if script is None:
        script = getattr(data, "script", b"")
    # Recover raw bytes: UnityPy may hand back a surrogate-escaped str for
    # non-UTF-8 (GBK) assets — encode it back to get the original bytes.
    if isinstance(script, bytes):
        raw = script
    else:
        raw = str(script).encode("utf-8", "surrogateescape")
    # Some tables are UTF-8, some are GBK. Try UTF-8 first, fall back to GBK.
    for enc in ("utf-8-sig", "gbk"):
        try:
            return name, raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return name, raw.decode("utf-8", "replace")

def is_design_table(name, text):
    """Heuristic: keep CSV/JSON design tables, drop Spine/binary/blobs."""
    n = str(name).lower()
    if "skeleton" in n or n.endswith(".atlas") or n.endswith(".skel"):
        return False
    if not text:
        return False
    # Drop binary-ish content (lots of U+FFFD replacement chars).
    if text.count("�") > max(4, len(text) * 0.005):
        return False
    body = text.lstrip("﻿")  # strip BOM
    first = body.split("\n", 1)[0]
    # JSON array, or a CSV row (has an ASCII comma in the first line).
    if body[:1] in "[{":
        return True
    if "," in first:
        return True
    return False

count = 0
for obj in env.objects:
    if obj.type.name != "TextAsset":
        continue
    name, text = get_text(obj)
    if WANT:
        if name not in WANT:
            continue
    elif not is_design_table(name, text):
        continue
    safe = "".join(c if c.isalnum() or c in "._-" else "_" for c in str(name))
    if not safe:
        safe = f"obj_{obj.path_id}"
    path = os.path.join(OUTDIR, safe + ".csv")
    # If the same name appears twice, suffix with path_id.
    if os.path.exists(path):
        path = os.path.join(OUTDIR, f"{safe}_{obj.path_id}.csv")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    count += 1
    print(f"dumped -> {os.path.basename(path).encode('ascii', 'backslashreplace').decode()} ({len(text)} chars)")

print(f"total dumped: {count}")
