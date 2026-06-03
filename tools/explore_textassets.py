"""Enumerate TextAssets in resources.assets to locate the design tables."""
import sys
import UnityPy

ASSETS = r"D:\SteamLibrary\steamapps\common\LongYinLiZhiZhuan\LongYinLiZhiZhuan_Data\resources.assets"

env = UnityPy.load(ASSETS)
rows = []
for obj in env.objects:
    if obj.type.name != "TextAsset":
        continue
    try:
        data = obj.read()
        name = getattr(data, "m_Name", None) or getattr(data, "name", "")
        script = getattr(data, "m_Script", None)
        if script is None:
            script = getattr(data, "script", "")
        # m_Script may be bytes or str
        if isinstance(script, bytes):
            text = script.decode("utf-8", "replace")
        else:
            text = str(script)
        first = text.split("\n", 1)[0][:60].replace("\t", "\\t")
        rows.append((name, len(text), first))
    except Exception as e:
        rows.append((f"<err:{e}>", -1, ""))

rows.sort(key=lambda r: -r[1])
out = r"D:\WorkSpace\LongYinMod_RisingFame\tools\_textasset_index.txt"
with open(out, "w", encoding="utf-8", errors="backslashreplace") as f:
    f.write(f"TextAsset count: {len(rows)}\n")
    f.write(f"{'name':<40} {'chars':>8}  first-line\n")
    f.write("-" * 100 + "\n")
    for name, n, first in rows:
        f.write(f"{str(name):<40} {n:>8}  {first}\n")
print(f"wrote {len(rows)} rows to {out}")
