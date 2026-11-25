# Unsent — The Micro-Confession Sprint

[![Make.fun Bounty](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/slyfunds-commits/unsent-confession-01/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/slyfunds-commits/unsent-confession-01/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

Entry for the [make.fun bounty "Unsent — The Micro-Confession Sprint"](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba): one two-part micro-confession — a `To:` line and the unsent message itself, written exactly as it was typed.

## The entry

> **To: my grandfather**
> I knew you forgot my name at Christmas. I introduced myself like we'd never met.

99 bytes total; message 80 characters. Built from 360 fresh candidates across 12 premise families, screened through judge-list-max (all 12 checklist items + 5/5 likes + zero dislikes + P7/P9) and the five Unsent-specific tests (addressee-swap, felt-reason, typed-not-sent, joke test, size). The keeper's felt reason is kindness — protecting a grandfather from his own forgetting — never stated, felt in the last words.

## Run

```sh
python3 main.py
```

Writes the entry to `output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). Pure stdlib, deterministic — byte-identical on every run, no trailing newline.
