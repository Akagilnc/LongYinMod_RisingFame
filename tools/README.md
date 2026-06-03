# tools

Local helper scripts for extracting game data. Not part of the mod build.

## Game-table extraction

The game's design tables live as `TextAsset`s inside
`<GameDir>/LongYinLiZhiZhuan_Data/resources.assets`. These scripts pull them out into
`docs/reference/game-tables/`.

### Setup

Requires Python 3 and [UnityPy](https://github.com/K0lb3/UnityPy):

```
pip install --user UnityPy
```

### Scripts

- **`dump_textassets.py`** — extract design tables to `docs/reference/game-tables/`.
  - No args: dumps every TextAsset that looks like a CSV/JSON design table (skips Spine
    `skeleton`/`.atlas`/`.skel` binaries and other non-tabular blobs).
  - With args: dumps only the named TextAssets, e.g.
    `python tools/dump_textassets.py SpeAddDataBase KungFuData`.
  - Auto-detects UTF-8 vs GBK encoding per table.

- **`explore_textassets.py`** — write an index of all 568 TextAssets (name, size, first line)
  to `tools/_textasset_index.txt`, sorted by size. Use it to discover table names.

### Paths

Both scripts hard-code the Steam install path
`D:\SteamLibrary\steamapps\common\LongYinLiZhiZhuan`. Edit the `ASSETS` constant at the top of
each script if the game lives elsewhere.

### Refreshing after a game update

```
python tools/dump_textassets.py
```

Then `git diff --stat docs/reference/game-tables/` to see which tables changed, and
sanity-check the effect table's integrity (header + 215 contiguous rows, 16 cols each):

```
python -c "rows=[r.split(',') for r in open('docs/reference/game-tables/SpeAddDataBase.csv',encoding='utf-8-sig').read().splitlines() if r.strip()]; ids=[int(r[0]) for r in rows[1:]]; print('rows', len(rows), 'cols', {len(r) for r in rows}, 'ids', ids[0], '..', ids[-1], 'contiguous', ids==list(range(ids[0],ids[-1]+1)))"
```
