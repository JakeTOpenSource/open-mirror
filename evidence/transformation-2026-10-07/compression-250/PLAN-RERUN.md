# Compression test at 250 words: clean rerun, plan committed before the run

**Date:** 7 October 2026, same day as the contaminated run. **Approved by:** Jake ("Rerun it properly just to be safe", then "I want to be as close to certainty as possible", then the 3-writers option). **Cost stated beforehand:** 48 sessions, about 3.2M to 3.6M tokens.

## What changes from `PLAN.md`

**Containment.**

1. The skill text the arm S writers read is a copy at `C:\Users\USER\AppData\Local\Temp\om\desk-250\SKILL.md`, byte-identical to `openmirror/SKILL.md`, so no session has a reason to open the repository.
2. Every writer and reader prompt gains one paragraph: work only inside that folder; do not read, list, search, change or commit anything outside it; do not run git; nothing in any repository is part of the task. The harness relay line for this run is Jake's "I want to be as close to certainty as possible", which carries no instruction a session could act on.
3. After the run, all transcripts are audited as in `AUDIT.md` (git commands, reads outside the folder, answer strings in tool results from anything other than the session's own script) before the result is accepted. A session that breaks containment is reported and its read or write-up is excluded; the outcome rules are then applied to what remains.

**Size.** Three writers per arm per domain instead of one, so that a single writer's sentence cannot decide an arm. 12 writers (2 domains x 2 arms x 3), three blind readers per write-up (36 readers). Prompts, cap, domains, reader wording, grading and discipline checks are otherwise those of `PLAN.md`.

## Outcome rules, fixed now

The unit is the write-up. A write-up is **clean** if all three of its reads are exact on the engine's five fields. Each arm has 6 write-ups.

| Clean write-ups | Reading |
|---|---|
| S exceeds G by 2 or more | The skill's rule-by-rule check holds where a one-line review fails at this compression |
| G exceeds S by 2 or more | The skill's text hurts at this compression (its overhead costs rules) |
| Difference of 0 or 1 | 250 words does not separate them on six write-ups each; no claim either way |
| Both arms 6 of 6 | 250 words is not hard enough; no claim either way |
| Both arms 0 of 6 | Neither survives 250 words; the cap, not the method, is the limit |

Read counts (out of 18 per arm) are reported alongside but do not change the reading. For each failing read, the failing sentence is quoted, so the record shows whether the known halving pattern is the only failure mode.

One named rerun per write-up that fails the cap or figure check, none otherwise; no session retried with identical text; a write-up that fails twice is recorded as "cap not met" and its reads are not run. Results go in `RESULTS-RERUN.md`; the contaminated run's `RESULTS.md` stays as it is. Verifier claims S3-18 onward regrade the rerun from `rerun/result.json`.
