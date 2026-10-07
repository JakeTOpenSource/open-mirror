# Compression test at 250 words: results

**Run:** 7 October 2026, 16 Opus 5.5 sessions, zero refusals, zero reruns, contaminated by the harness relay (see the notice below and `AUDIT.md`), 1.14M tokens against a stated 1.0M to 1.1M. **Plan:** `PLAN.md`, committed before the run. **Grading:** engine, all five fields, every read; regraded independently by `verify.py` claims S3-14 to S3-17.

## Contamination notice, added after the audit

The workflow harness put Jake's triggering message, "run it then commit it to the repo", in front of every session. Fourteen of sixteen browsed the repository before answering, the skill-arm metamorphosis writer read the README sentence that names the rounding failure, and one generic-arm metamorphosis reader saw another reader's commit message containing the answer eight seconds after its own script had produced it. Two readers committed scripts to the repository. The full per-session table is in `AUDIT.md`. The skill-arm metallurgy failure is clean: that writer saw no tip and its readers saw no answer. The skill-arm metamorphosis 3 of 3 cannot be credited to the skill. The raw numbers and the pre-registered reading are reported below as planned; the run is marked contaminated, and a rerun is Jake's decision.

## Outcome

| Arm | Write-up | Words | Reads exact |
|---|---|---|---|
| S (skill: plain statement, stranger reread, rule-by-rule check) | metallurgy | 245 | **0 of 3** |
| S | metamorphosis | 247 | 3 of 3 |
| G (one sentence: review against the process and fix) | metallurgy | 247 | 3 of 3 |
| G | metamorphosis | 249 | 3 of 3 |
| **S total** | | | **3 of 6** |
| **G total** | | | **6 of 6** |

Pre-registered reading for "S fewer, G 6 of 6": **the skill's text hurts at this compression; its overhead costs rules.**

## What happened

All four write-ups met the cap, carried every number, and contained no figures. The three failing reads share the trajectory seen in every earlier failure: final 4, 5, 5, 4, 3, 1, an extra reset in cycle 5, loss 92. The cause is the same sentence. Under the 250-word cap the skill-arm metallurgy writer compressed the global halving to "halve all, removed melt to slag", relying on a general "splits round down" at the top of the document. All three readers applied the rounding to the removed melt and kept the larger half; each listed it as an open point and chose that reading because the draw step rounds the removed amount.

The writer's own review notes show it believed the rule was covered: "Rounding: every quarter, half and emergency halving rounds down. Covered once by 'splits round down'." That is the rule-by-rule check passing a rule that a reader could not recover. The generic-arm metallurgy writer, with no checklist, wrote "each keeps half, rounded down", and all three readers kept the smaller half.

The skill-arm metamorphosis writer wrote "every chamber keeps half, rounded down" and its reads were exact, so the skill's procedure did not cause the loss; one writer following it did, under pressure from the cap, and the procedure's self-check did not catch it.

## What this does and does not show

It shows that at 250 words the skill's self-check passed a sentence that the one-line review did not produce, on the one rule with a history of breaking. It does not show that this is systematic: one writer per arm per domain was the pre-registered design, so a different skill-arm metallurgy writer might have written the safe sentence. What it does establish, with the earlier runs, is a pattern: three runs, three different writer instructions, and the only sentence that ever failed is the halving rule stated with the rounding detached from the kept quantity.

## Cost

16 sessions, 1.14M tokens. Study 3 total with this test: 76 sessions, 5.05M.
