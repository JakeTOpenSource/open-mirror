# Compression test at 250 words: plan, committed before the run

**Date:** 7 October 2026. **Approved by:** Jake ("run it then commit it to the repo. I want it done by the book"). **Cost stated beforehand:** 16 sessions, about 1.0M to 1.1M tokens.

## Question

At 400 words, a one-sentence review instruction matched the skill: both produced zero drift. Does the skill's rule-by-rule self-check beat the one-sentence review when the analogy must fit in 250 words, where there is less room to state every rule and a quick review is more likely to miss a lost one?

## Design

Two domains, the ones with a history of drift: metallurgy and metamorphosis. Two arms:

- **Arm S (skill).** The disciplined writer prompt from phase 1, unchanged except the cap: read `SKILL.md`, plain statement first, write, reread as a stranger checking every rule is recoverable and every domain-misleading point says what the line does, fix, deliver.
- **Arm G (generic).** The control writer prompt, unchanged except the cap: one sentence, review against the engineer's process and fix what you find.

Both: at most 250 words including all numbers, same mapping, same banned words, same no-figures rule, same Report template rule. One writer per domain per arm (4 writers). Three blind readers per write-up, same handover wording as before, write-up inline (12 readers). Opus 5.5 throughout. Graded by the engine on all five fields.

Discipline check on each write-up: cap, no figures, no banned words. One named rerun if a write-up fails; if it fails again, that arm-domain is recorded as "cap not met" and its reads are not run.

## Outcome rules, fixed now

| S reads | G reads | Reading |
|---|---|---|
| 6 of 6 | 6 of 6 | 250 words is not hard enough to separate them; no claim either way |
| 6 of 6 | fewer | The skill's rule-by-rule check holds where a one-line review fails at this compression |
| fewer | 6 of 6 | The skill's text hurts at this compression (its overhead costs rules) |
| fewer | fewer | Neither survives 250 words; the cap, not the method, is the limit |
| either arm cannot meet the cap | | Reported as such; no reads for that arm-domain |

No session retried with identical text. No second attempt beyond the one named rerun. Results go in `RESULTS.md` in this folder and are added to `verify.py`.
