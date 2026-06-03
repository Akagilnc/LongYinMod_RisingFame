# Game data reference

Captured game-design tables kept locally as reference for future mod work. These are
**read-only reference data**, not consumed by the build.

Two sources, which have been cross-checked against each other:

- **`game-tables/`** — all design tables extracted directly from the shipped build
  (`resources.assets`) with UnityPy. **Authoritative** — these are the values the mod runs
  against. See `game-tables/README.md`. Regenerate via `tools/dump_textassets.py`.
- **`special-effects-tab000029.tsv`** — the 特效/词条 table as pasted from the upstream
  Tencent Docs design sheet (tab 000029). Kept for provenance; **verified byte-for-byte
  identical** to the build's `game-tables/SpeAddDataBase.csv` (0 diffs), so the design doc and
  the shipped build agree for this table.

## special-effects-tab000029.tsv — 特效/词条定义表

- **Source:** Tencent Docs spreadsheet `https://docs.qq.com/sheet/DRk9abXBucGZtcnhw`, tab `000029`.
- **Captured:** 2026-06-03 (pasted by maintainer; the doc site is not machine-fetchable).
- **Shape:** 16 columns × 215 rows. 序号 (id) is contiguous `0..214`, no gaps. Tab-separated,
  UTF-8. In-cell line breaks in 描述 are stored as the literal two-character sequence `\n`.

This is the master table of combat/cultivation **effects (词条/特效)** — the attributes that
equipment rolls, buffs/debuffs apply, and skills grant. Each row is one effect type keyed by 序号.

### Column dictionary

| # | Column | Meaning (best interpretation — verify against game before relying) |
|---|--------|--------|
| 1 | 序号 | Effect id / index (0–214). Stable key. |
| 2 | 特效 | Effect name. |
| 3 | 数值1% | Base unit value. e.g. `0.01` = 1 point is worth 1%; `1` = flat per-point. |
| 4 | 正面词缀 | Positive affix label shown when the rolled effect is beneficial; `无` = none. |
| 5 | 负面词缀 | Negative affix label; `无` = none. |
| 6 | 百分比显示 | Display as a percentage (1/0). |
| 7 | 非随机特效 | Excluded from random rolls (1/0). |
| 8 | 必须随机正数 | Must roll positive (1/0). |
| 9 | 持续时间 | Duration in turns. `0` = instant/permanent stat; positive = N turns; `-1` = special/until-removed. |
| 10 | 自身持续特效 | Buff sustained on self (1) vs. applied to enemy (0) — correlates with 特效价值类别 我方/敌方. |
| 11 | 描述 | Description (in-cell line breaks as literal `\n`). |
| 12 | 特效价值类别 | Valuation category: `伤害` (120) / `我方` ally-buff (59) / `敌方` enemy-debuff (36). |
| 13 | 不自动升级 | Do not auto-upgrade (1/0). |
| 14 | 触发时机 | Trigger timing: `0` passive/always (117), `1` on-attack (73), `2` on-defense (25). |
| 15 | 计算战斗分 | Counts toward combat score (1/0). |
| 16 | 特殊介绍 | Has special intro text (1/0). |

Interpretations for columns 6–10 and 13–16 are inferred from value patterns, not from the doc's
own legend. Treat the numeric flags as ground truth; treat the *meanings* as provisional.

### Relation to the mod

The current mod (`Plugin.cs`) patches `HeroData` exp/favor/contribution rates and book-writing,
plus the auction/breakthrough/enhance reroll helpers. It does **not** reference these effect ids
today, so there is no field in the code to cross-check against this table yet.

This table is captured ahead of time as the source of truth for any **future** effect-related
feature (e.g. tuning equipment rolls, buff durations, or effect values). When such work starts,
key off 序号 — the names are not stable identifiers.

### Caveats

- Only tab `000029` was captured. The source spreadsheet has other tabs (items, kungfu, heroes,
  …) that are **not** here yet — add them as separate files under this folder when needed.
- This is a snapshot; if the upstream doc changes, re-paste and re-validate (row count + contiguous
  序号 + 16 cols per row).
