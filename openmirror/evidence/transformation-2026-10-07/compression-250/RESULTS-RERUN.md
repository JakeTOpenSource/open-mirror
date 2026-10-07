# Compression test at 250 words: clean rerun, results

**Run:** 7 October 2026, 48 Opus 5.5 sessions (12 writers, 36 readers), zero refusals, zero reruns, 3.28M tokens against a stated 3.2M to 3.6M. **Plan:** `PLAN-RERUN.md`, committed before the run. **Containment:** every session confined to a scratch folder holding only a copy of `SKILL.md`; all 48 transcripts audited afterward (`audit_wf.py`, `audit.json`, `audit-summary.txt`): no git command, no read or listing outside the folder, and every answer string in any tool result came from a script the session wrote and ran there. **Grading:** engine, all five fields, every read; regraded independently by `verify.py` claims S3-18 to S3-25.

## Outcome

| Arm | Write-up | Words | Reads exact | Clean write-up |
|---|---|---|---|---|
| S (skill) | metallurgy w1 | 247 | 3 of 3 | yes |
| S | metallurgy w2 | 249 | 3 of 3 | yes |
| S | metallurgy w3 | 247 | 3 of 3 | yes |
| S | metamorphosis w1 | 249 | 3 of 3 | yes |
| S | metamorphosis w2 | 247 | 3 of 3 | yes |
| S | metamorphosis w3 | 248 | 3 of 3 | yes |
| G (one-sentence review) | metallurgy w1 | 248 | **0 of 3** | **no** |
| G | metallurgy w2 | 247 | 3 of 3 | yes |
| G | metallurgy w3 | 248 | 3 of 3 | yes |
| G | metamorphosis w1 | 249 | 3 of 3 | yes |
| G | metamorphosis w2 | 245 | 3 of 3 | yes |
| G | metamorphosis w3 | 250 | 3 of 3 | yes |
| **S total** | | | **18 of 18** | **6 of 6** |
| **G total** | | | **15 of 18** | **5 of 6** |

Pre-registered reading for a difference of one clean write-up: **250 words does not separate them on six write-ups each; no claim either way.**

## The one failure

All twelve write-ups met the cap, carried every number, and contained no figures or banned words. The three failing reads share the trajectory of every earlier failure: final 4, 5, 5, 4, 3, 1, an extra reset in cycle 5, loss 92. The generic-arm metallurgy writer 1 wrote "emergency tap halves every crucible, removed melt to slag" and relied on "Halves and quarters round down" in its first line. All three readers listed the rounding as an open point and chose to round the removed amount, keeping the larger half, because the draw step rounds what moves. The writer's own notes say: "Added 'halves and quarters round down' near the top so it covers the BASE quarter, the SUPERHEATED half and the tap halving." That is the same mistake the skill-arm writer made in the contaminated run, and the same sentence that failed on 6 October.

One other write-up used the same detached form: generic-arm metamorphosis writer 1, "halves every chamber, removed mass discarded" with "splits round down" at the top. Its three readers all kept the smaller half. So the detached form is not a guaranteed failure; it is a coin the reader flips. The other ten write-ups attached the rounding to the kept quantity ("each keeps half, rounded down") or to the halving itself ("halves every chamber, rounded down"), and all thirty of their reads were exact.

## How each write-up stated the halving

| Write-up | Sentence | Reads |
|---|---|---|
| S metallurgy w1 | "each keeps half, rounded down, rest to slag" | 3 of 3 |
| S metallurgy w2 | "each keeps half, rounded down; rest to slag" | 3 of 3 |
| S metallurgy w3 | "each keeps half rounded down, rest to slag" | 3 of 3 |
| S metamorphosis w1 | "each chamber keeps half, rounded down, the rest discarded" | 3 of 3 |
| S metamorphosis w2 | "halves every chamber, rounded down, removed mass discarded" | 3 of 3 |
| S metamorphosis w3 | "halves every chamber, rounded down, removed mass tallied" | 3 of 3 |
| G metallurgy w1 | "halves every crucible, removed melt to slag" + "Halves and quarters round down" at the top | 0 of 3 |
| G metallurgy w2 | "Every crucible keeps half, rounded down; the rest is slag" | 3 of 3 |
| G metallurgy w3 | "every crucible keeps half, rounded down; rest to slag" | 3 of 3 |
| G metamorphosis w1 | "halves every chamber, removed mass discarded" + "splits round down" at the top | 3 of 3 |
| G metamorphosis w2 | "halve every chamber, rounding down, removed mass to the tally" | 3 of 3 |
| G metamorphosis w3 | "halve each, rounding down; removed mass to the tally" | 3 of 3 |

All six skill-arm writers attached the rounding to the halving sentence. Four of six generic-arm writers did. That is the only visible difference between the arms, and on six writers each it is not a separation by the rule fixed in advance.

## What this does and does not show

It shows, cleanly this time, that at 250 words both methods produce write-ups that blind readers execute without drift almost every time: 33 of 36 reads exact, and the three misses came from one write-up. It shows that the contaminated run's reading, "the skill's text hurts at this compression", does not survive a clean rerun with three times the writers. It does not show that the skill beats the one-sentence review: 6 of 6 against 5 of 6 is inside the "no claim" band that was set before the run. It confirms, for the fifth time across every run since 6 October, that the only sentence that has ever failed is the halving rule with its rounding detached from the kept quantity.

## Cost

48 sessions, 3.28M tokens. Study 3 total: 124 sessions, 8.33M. All runs: 301 sessions, about 19.2M.
