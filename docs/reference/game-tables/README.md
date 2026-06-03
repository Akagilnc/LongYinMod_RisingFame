# Game design tables (extracted from the build)

The game's design tables, extracted directly from the shipped Unity build. These are the
**authoritative** values the mod actually runs against — preferred over the design doc when they
disagree.

## Provenance

- **Source:** `LongYinLiZhiZhuan_Data/resources.assets` (Unity serialized asset container).
  Each table is a `TextAsset` (raw CSV/JSON) embedded in that file — it is *not* in the IL2CPP
  code (`Assembly-CSharp.dll` / `global-metadata.dat`), which is why source analysis can't
  reproduce the numbers.
- **Tool:** [`UnityPy`](https://github.com/K0lb3/UnityPy) via `tools/dump_textassets.py`.
- **Captured:** 2026-06-03, game version per the then-current Steam build.

To refresh after a game update, re-run `python tools/dump_textassets.py` (see `tools/README.md`).

## Format notes

- Comma-separated, UTF-8 (a leading BOM, if any, is stripped on export). A few tables were
  **GBK**-encoded in the build (e.g. `SpeHeroFaceData`); the extractor auto-detects and converts
  them to UTF-8.
- In-cell line breaks are stored as the literal two-character sequence `\n` in most tables.
  `PlotData` is the exception — it uses *real* newlines inside quoted fields, so parse it with a
  proper CSV reader, not line-by-line.
- JSON tables (`PoetryData`) are stored as a JSON array, not CSV.

## Key tables

| File | Rows* | Contents |
|------|------:|----------|
| `SpeAddDataBase.csv` | 215 | 特效/词条 effect definitions (= the design-doc tab 000029; **verified identical**) |
| `ForceSpeAddDataBase.csv` | 65 | 势力特效 force-level effects |
| `KungFuData.csv` / `SummonKungFuData.csv` | — | 武学 / 召唤武学 |
| `HeroTagData.csv` | 391 | 角色标签 hero tags |
| `SpeHeroData.csv` / `SpeHeroFaceData.csv` | — | named heroes / their portraits |
| `WeaponData.csv` `ArmorData.csv` `MedData.csv` `FoodData.csv` `HorseData.csv` | — | equipment / consumables / mounts |
| `BuildingData.csv` `AreaData.csv` `ForceData.csv` `ResourcePointData.csv` | — | map / factions / resources |
| `PlotData.csv` | — | story/plot script (1.3 MB, multiline cells) |
| `PoetryData.csv` | — | poetry (JSON) |
| `TechDataBase.csv` `AchievementData.csv` `NameData.csv` `Localization*.csv` | — | tech / achievements / names / localization |
| `<city/sect>.csv` (丐帮, 京城, 少林寺, …) + `*Default.csv` | 15 | per-entity relation/attitude matrices |

\* Logical record counts; `wc -l` over-counts tables with multiline cells.

## Caveats

- This is a snapshot. After a game patch, re-extract and re-verify.
- Column *meanings* are not documented by the build; infer them from usage. For the effect table,
  see the column dictionary in `../README.md`.
- These files are reference data only — nothing in the build consumes them from here.
