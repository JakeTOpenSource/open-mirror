# Transformation study (study 3): results

**Date:** 7 October 2026. **Plan:** `TRANSFORMATION-STUDY-PLAN.md`, written and committed before the run. **Evidence:** `evidence/transformation-2026-10-07/`, every write-up, plain statement, self-check, read, and checklist extraction on file, graded by `grade.py` and re-graded independently by `verify.py` (claims S3-1 to S3-9). **Cost:** 44 sessions, 2.87M subagent tokens, against a plan estimate of 1.5M to 2.0M; the overrun and its cause are in the last section.

## The result, in plain words

Ten writers were given the skill and told to use it on themselves: write the plain statement first, then the 400-word analogy, then reread the analogy as a stranger and fix what it lost. Fourteen blind readers then executed those analogies with no hint that they were analogies. **All fourteen reads reproduced the original process exactly: every quantity, every state, all thirteen state changes, both reset cycles, and the loss tally, as checked by the engine.** That includes all six reads on the two analogies, metallurgy and metamorphosis, that had failed five times out of six when written without the discipline.

The same meaning went into ten different analogies and came back out of each one without drift. That is the demonstration you asked for, with a machine as the judge, and the difference between drift and no drift was the writer's discipline.

## The numbers

| | Undisciplined writers (W0, 6 October) | Disciplined writers (W1, this study) |
|---|---|---|
| Reads exactly right | 25 of 30 | **14 of 14** |
| Reads on metallurgy and metamorphosis | 1 of 6 | **6 of 6** |
| Write-ups within 400 words | 10 of 10 | 10 of 10 |
| Rules recoverable from the write-up alone, fixed 23-rule checklist | 219 of 230 | **226 of 230** |
| Rule most often lost | "quantities are whole and never negative", 8 of 10 | same rule, 4 of 10 |

Same process, same ten domain mappings, same word cap, same reader prompt, same reader model, same grader.

## Where the difference came from

Every baseline failure traced to one compressed sentence about the global halving. The undisciplined metallurgy write-up said "halve every crucible, removed melt to slag" and relied on a general "any split rounds down" elsewhere; readers applied the rounding to the removed melt and kept the larger half. The disciplined metallurgy write-up says "halve every crucible, rounding down, removed melt to slag", which attaches the rounding to what the crucible keeps. Metamorphosis went the same way: "every chamber halves and the shed mass is discarded" became "every chamber is halved, rounded down, the removed mass onto the loss tally". The writers' self-check lists show both of them examining the halving and rounding rules before delivering. Readers of both new write-ups kept the smaller half, as the process requires.

The checklist agrees at the level of the whole text: the disciplined write-ups carried seven more rules across the ten, and no disciplined write-up lost a rule the baseline had kept.

## What this does and does not show

It shows:

1. Meaning carried into ten parallel analogies can be read back with zero drift, deterministically checked, when the writer works the way the skill prescribes.
2. The drift seen on 6 October was a writing defect, and the writer-side discipline removed it on the two analogies where it had occurred.
3. The reader-side pre-read, tested the day before, is not where the skill's value is; the writer side is.

It does not show:

4. That the skill's *text* is what mattered, as opposed to any careful "reread your own draft for lost rules" instruction. The disciplined prompt pointed the writer at the skill's steps 1, 4 and 5; a control with a generic self-review instruction was not run. That is the next cheapest test and the most important remaining confound.
5. Zero drift in general. Fourteen reads is a sample; the two analogies with a history of drift got three reads each and the rest got one, by design, to save sessions.
6. Anything about human readers or writers. Every session was Opus 5.5 or Sonnet 5.5.

## Cost, honestly

| Phase | Sessions | Model | Estimated | Actual |
|---|---|---|---|---|
| 1 Writers | 10 | Opus | 0.2M to 0.3M | 0.77M |
| 2 Readers | 14 | Opus | 1.0M to 1.4M | 0.88M |
| 3 Checklist | 20 | Sonnet | 0.3M | 1.22M |
| **Total** | **44** | | **1.5M to 2.0M** | **2.87M** |

The readers came in under estimate. The writers ran over because they used a shell to count words and iterate under the cap, which was not anticipated. The checklist ran four times over: twenty Sonnet sessions each read two files and wrote 23 quoted answers, and Sonnet's per-session token use was close to Opus's, so "lesser model" saved money but not tokens. Both overruns were foreseeable and are my error in the estimate, not in the design. No session was refused, none was retried, and none produced a placeholder.

## What should change in the skill

Nothing in the seven steps. The study used them as written. What should change is the pitch: the README has said "no measured benefit" since yesterday, and that sentence now needs a second half. The skill's measured value is on the writing side, for a writer who runs it on their own analogy before handing it over. The README and the changelog carry that update; the compiled report carries this file.
