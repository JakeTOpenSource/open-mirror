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

## The control, run the same afternoon

The confound named below as "most important" was tested before this report shipped. Four writers, two for metallurgy and two for metamorphosis, got the identical prompt with the skill paragraph replaced by one sentence: "review your explanation carefully for errors, omissions, or ambiguities against the engineer's process, and fix any you find." No skill file, no plain statement first, no stranger framing, no rule-by-rule check. Twelve blind readers, three per write-up, then executed them. The outcome rule was fixed before the run: six of six on both domains under the control would mean structured self-review of any kind is the active ingredient.

**Control: 12 of 12 exact.** All four control write-ups were within the cap and free of figures. Their fix lists show the writers finding the halving ambiguity unprompted: metallurgy copy 1 wrote "the draft said 'halve every crucible', which doesn't say which half gets rounded down. It now says each crucible keeps half, rounded down." Three of the four control write-ups use "keeps half, rounded down"; the fourth, metamorphosis copy 1, uses "halves, rounded down", and all three of its readers still kept the smaller half.

So the comparison stands as: no review, 1 of 6 on these two domains; any review against the source, 6 of 6; the skill's review, 6 of 6. **The skill's seven steps did not add anything a one-sentence review instruction did not.** Record: `evidence/transformation-2026-10-07/control/`. Cost: 16 sessions, 1.04M tokens. One protocol difference: control readers received the write-up inline rather than by file, because the workflow could not write files; the reader wording was otherwise identical.

## The 250-word test, run by the book

Plan committed before the run (`evidence/transformation-2026-10-07/compression-250/PLAN.md`), with a four-row outcome table. Same two domains, one writer per arm per domain, three readers each, cap cut from 400 to 250 words. **Skill arm 3 of 6; generic-review arm 6 of 6.** The pre-registered reading for that row: the skill's text hurts at this compression. Under the cap, the skill-arm metallurgy writer wrote "halve all, removed melt to slag" with a general "splits round down", and all three readers kept the larger half; its own review notes say that rule was "covered once". The generic writer wrote "each keeps half, rounded down" and all three readers were exact. One writer per arm per domain, so one writer's choice; but it is the fourth time the same sentence has decided the outcome, and the skill's rule-by-rule check passed it. Full account: `compression-250/RESULTS.md`.

## What this does and does not show

It shows:

1. Meaning carried into ten parallel analogies can be read back with zero drift, deterministically checked, when the writer reviews the analogy against the source before handing it over. 14 of 14 with the skill; 12 of 12 with a one-sentence review instruction on the two domains that had drifted.
2. The drift seen on 6 October was a writing defect: those writers were given no review instruction at all, and five of six reads on two domains went wrong. Any review pass against the source removed it.
3. The reader-side pre-read, tested the day before, is not where value lies, and the skill's seven steps are not where it lies either. The value is in the review pass, which the skill contains but does not own.

It does not show:

4. That the skill's text matters for this task. The control says it does not. What would still be worth testing is a harder compression, say 250 words, where a one-sentence review might fail and a rule-by-rule check might not; that is a hypothesis, not a result.
5. Zero drift in general. Twenty-six reads across the two runs is a sample, concentrated by design on the two analogies with a history of drift.
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

The outcome rule set before the control said: if generic review also goes six of six, the skill should be cut down to whatever did the work. What did the work, on this evidence, is one instruction: before you hand over an analogy, review it against the thing it describes and fix what it lost. That instruction is inside Open Mirror as steps 4 and 5 applied to your own text, and it is also a sentence anyone could write. At 400 words the two tied. At 250 words the one-sentence review did better, on one writer each. The honest pitch, as of today: Open Mirror has not been shown to beat a plain review instruction on any task tested, and on the hardest one it did worse. The README and changelog say so.

One concrete thing the record does support changing: the specific failure, four times out of four, is a halving rule whose rounding is stated away from the quantity that keeps it. A writer's checklist that says "for every rounding, name which quantity is rounded" would have caught every failure in this study. That is a sentence, not a skill.

## Cost

Control: 16 sessions, 1.04M. 250-word test: 16 sessions, 1.14M. Study 3 total: 76 sessions, 5.05M.
