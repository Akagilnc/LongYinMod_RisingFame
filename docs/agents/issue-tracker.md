# Issue tracker: GitHub (fork)

Issues and PRDs for this repo live as GitHub issues on the fork **`Akagilnc/LongYinMod_RisingFame`**, not on `origin` (`Cooper-X-Oak/LongYinMod_RisingFame`). Use the `gh` CLI for all operations, and **always pass `-R Akagilnc/LongYinMod_RisingFame`** so commands don't default to `origin`.

## Conventions

- **Create an issue**: `gh issue create -R Akagilnc/LongYinMod_RisingFame --title "..." --body "..."`. Use a heredoc for multi-line bodies.
- **Read an issue**: `gh issue view <number> -R Akagilnc/LongYinMod_RisingFame --comments`, filtering comments by `jq` and also fetching labels.
- **List issues**: `gh issue list -R Akagilnc/LongYinMod_RisingFame --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'` with appropriate `--label` and `--state` filters.
- **Comment on an issue**: `gh issue comment <number> -R Akagilnc/LongYinMod_RisingFame --body "..."`
- **Apply / remove labels**: `gh issue edit <number> -R Akagilnc/LongYinMod_RisingFame --add-label "..."` / `--remove-label "..."`
- **Close**: `gh issue close <number> -R Akagilnc/LongYinMod_RisingFame --comment "..."`

This repo has two remotes (`origin` → upstream `Cooper-X-Oak`, `fork` → `Akagilnc`). The `-R` flag is what keeps issue operations on your fork.

## When a skill says "publish to the issue tracker"

Create a GitHub issue on `Akagilnc/LongYinMod_RisingFame`.

## When a skill says "fetch the relevant ticket"

Run `gh issue view <number> -R Akagilnc/LongYinMod_RisingFame --comments`.
