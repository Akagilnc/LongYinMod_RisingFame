# Game data reference

Game-design tables kept locally as reference for future mod work. **Read-only reference data**,
not consumed by the build.

The single source is **`game-tables/`** — all design tables extracted directly from the shipped
build (`resources.assets`) with UnityPy. These are the **authoritative** values the mod runs
against. See `game-tables/README.md`; regenerate via `tools/dump_textassets.py` after a game
update.

> History: the 特效/词条 table was once cross-checked against the upstream Tencent Docs design
> sheet (`https://docs.qq.com/sheet/DRk9abXBucGZtcnhw`, tab 000029) and found **byte-for-byte
> identical** to the build's `game-tables/SpeAddDataBase.csv` (0 diffs). We now extract from the
> build only; the manual copy was removed.

## SpeAddDataBase — 特效/词条 effect table

`game-tables/SpeAddDataBase.csv` — the master table of combat/cultivation **effects (词条/特效)**:
the attributes that equipment rolls, buffs/debuffs apply, and skills grant. Comma-separated,
16 columns × 215 rows, 序号 (id) contiguous `0..214`. Each row is one effect type keyed by 序号.
In-cell line breaks in 描述 are the literal two-character sequence `\n`.

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

Interpretations for columns 6–10 and 13–16 are inferred from value patterns, not from a doc
legend. Treat the numeric flags as ground truth; treat the *meanings* as provisional — confirm by
reading how the game uses each field (would require decompiling `GameAssembly.dll`).

### Relation to the mod

The current mod (`Plugin.cs`) patches `HeroData` exp/favor/contribution rates and book-writing,
plus the auction/breakthrough/enhance reroll helpers. It does **not** reference these effect ids
today, so there is no field in the code to cross-check against this table yet.

This is the source of truth for any **future** effect-related feature (e.g. tuning equipment
rolls, buff durations, or effect values). When such work starts, key off 序号 — the names are not
stable identifiers.
