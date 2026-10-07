# Coherence study: one process, ten analogies, blind operators

**Date:** 6 October 2026
**Question:** when one exact process is explained to different readers entirely in different analogies, does the process survive, and does the Open Mirror pre-read change anything?
**Evidence:** `evidence/coherence-2026-10-06/`. Inputs hashed in `inputs/`. Every document, operator report, and reviewer analysis is saved verbatim, with the source model of every result labelled.
**Cost:** 166 agent sessions, about 10.0M subagent tokens. Roughly 1.5M of that produced nothing, for reasons that were my fault and are stated below.

## The result, stated first

**The Open Mirror pre-read produced no measurable benefit in this study.** Across 60 blind reports on two conditions, model operators executing a fixed numerical procedure from analogical documents, with scripts, were no more accurate and flagged no more gaps when they ran the pre-read than when they did not. That is the scope of the result. The study did not test a person using Open Mirror to inspect an argument made through metaphor, which is the skill's stated purpose. In the one case where the pre-read named the decisive ambiguity before the work began, the operator resolved it wrong anyway and produced the same wrong figures as the operators who had no pre-read.

**The process itself was robust.** Complete documents were read correctly 30 times out of 30. Compressed 400-word write-ups were read correctly 25 times out of 30. All five failures had one cause: a halving rule the writer had compressed to "halve, rounds down", which two of the ten write-ups made ambiguous about which half is rounded. No operator in 60 was pulled off a stated rule by the analogy's real-world physics, even where that physics flatly contradicts the rule.

Everything below is the support for those two sentences.

## The process

Six positions in a line. Five cycles. Five steps per cycle in fixed order: add inputs with no limit enforced; sweep positions 1 to 6 one at a time and push anything over the limit to the next position, so excess cascades; switch each position's state on a hysteresis pair; release, computed for all six first then applied at once, a quarter to loss when resting and half to the previous position when raised; and halve every position when the total is strictly more than 38. Limits are enforced only in the sweep.

The dataset was tuned so every rule fires in both directions: a four-position cascade, a state that drops and rises again, back-transfers that leave positions over their limits, two resets, and a final total of exactly 38. Two independent implementations agree on the truth: final quantities 6, 10, 9, 7, 4, 2; thirteen state changes; resets in cycles 1 and 4; loss 76.

## The ten analogies

Electrical charge stages with a Schmitt trigger (the control), a concrete pour line, a crucible cascade, plant xylem and phloem, ballast tanks with cavitation, insect metamorphosis, a sewage treatment train, a RAG retrieval tier stack, a constrained-state solver in Lagrangian language, and a ticket pipeline framed by Goodhart's law. Several were chosen because their real physics contradicts a rule: concrete does not un-set, pupae do not revert, melt does not run uphill, a projection discards its excess, a kanban limit is always on.

## Study 1: complete documents

Ten translators each wrote a 700 to 1300 word operating document in their domain's language, forbidden from using abstract terms, required to keep every rule even where the domain disagrees. A strict checker read each document blind and compared it with the process; nine passed first time, one was sent back for a banned word.

Thirty operators then worked the documents, three per domain, each a fresh session that believed it was covering a desk. A was told nothing. B was told the document describes the process in domain terms and every rule applies as written. C was told the same and required to run the pre-read. All used a script for the arithmetic.

| Domain | A | B | C |
|---|---|---|---|
| electrical | exact | exact | exact |
| concrete | exact | exact | exact |
| metallurgy | exact | exact (S) | exact (R) |
| xylem | exact | exact | exact |
| ballast | exact | exact | exact |
| metamorphosis | exact (S) | exact (R) | exact |
| treatment | exact (S) | exact | exact |
| rag | exact | exact | exact |
| lagrangian | exact (S) | exact (R) | exact |
| goodhart | exact (R) | exact | exact (S) |

30 of 30. Unmarked cells are Opus 5.5 first attempts; (R) is an Opus rerun with the document supplied by file; (S) is a Sonnet fallback with the same prompt, used after the Opus filter refused the slot twice. The ten reviewer analyses for this study were written before the reruns and fallbacks, so in five of them (metallurgy, metamorphosis, treatment, lagrangian, goodhart) the reviewer describes operators as null or placeholder; the table above is the deterministic grading of what actually ran, and the reviewer texts are labelled accordingly in the evidence. The reviewers found no translation loss in any document. Every operator C pre-read named the domain's real-physics traps before the work. Nobody fell for any of them, with or without the pre-read.

What this shows: a complete document survives any of these analogies when read by a careful model with a script. It says nothing in the pre-read's favour, because there was nothing for the pre-read to prevent.

## Study 2: compressed write-ups

The same ten domains, but the writer was told to explain the line the way a senior person would to a new colleague, in at most 400 words, trusting the reader's domain sense, with no completeness check. The writers admitted compressing 11 to 15 rules each. Reviewers counted 7 to 14 real losses per write-up after the Report paragraph was excluded (see "What went wrong" for why). Operators were additionally asked to list open points: anything the write-up left unsettled, with the assumption they used. Pre-read notes were a required field for C, so no C could skip it.

| Domain | A | B | C | Real losses | Flagged by A, B, C |
|---|---|---|---|---|---|
| electrical | exact | exact | exact | 8 | 3, 3, 4 |
| concrete | exact | exact | exact | 10 | 6, 4, 5 |
| metallurgy | **wrong** | **wrong** | **wrong** | 12 | 6, 8, 5 |
| xylem | exact | exact | exact | 8 | 3, 3, 3 |
| ballast | exact | exact | exact | 7 | 2, 4, 3 |
| metamorphosis | **wrong** | exact | **wrong** | 10 | 4, 3, 5 |
| treatment | exact | exact | exact | 14 | 7, 6, 8 |
| rag | exact | exact | exact | 9 | 6, 4, 5 |
| lagrangian | exact | exact | exact | 12 | 3, 4, 4 |
| goodhart | exact | exact | exact | 8 | 3, 4, 3 |
| **total** | 8/10 | 9/10 | 8/10 | 98 | 43, 43, 45 |

All 30 are Opus 5.5 first attempts; no slot was refused.

**The five failures are one failure.** All five produced the identical wrong trajectory: final 4, 5, 5, 4, 3, 1, an extra reset in cycle 5, loss 92. The cause in every case was the halving rule. The abstract process says each position *becomes* floor(level/2), so an odd position keeps the smaller half. The metallurgy write-up said "halve every crucible, removed melt to slag" under a general "any split rounds down"; the metamorphosis write-up said "every chamber halves and the shed mass is discarded" under "any split rounds down". Both make the removed quantity the salient object, and all five failing operators applied the rounding to it, keeping the larger half. The electrical write-up said "every stage halves, rounded down, the difference to ground", which attaches the rounding to the kept quantity, and all three of its operators got it right. Metamorphosis B, reading the same ambiguous sentence as A and C, chose the other reading and was exactly right. The ambiguity was genuine, and the reviewers classified all five as rule-ambiguous-in-document plus rounding, not as domain intuition.

**The pre-read did not help.** On correctness, C went 8 of 10, the same as A and one worse than B. On gap flagging, C covered 45 of 98 real losses against 43 and 43; within the reviewers' counting error that is no difference. In metallurgy, C's pre-read notes said before any work began: "The one thing it leaves open is how the halving rounds." C then listed that point as an open point, wrote out both readings, chose the wrong one, and delivered the wrong report. Naming the gap did not change the outcome. In metamorphosis, C's pre-read said the write-up "leaves some rounding and timing details open" and did not name which half; C was wrong, B without the pre-read was right.

**Domain physics never won.** In all ten cases the reviewer found that operator A, who had no warning that the write-up was an analogy, resolved every silent gap toward the engineer's process rather than toward real concrete, biology, metallurgy, or kanban practice. The quoted examples are in `study2-lossy-v2/reviews/`.

## What went wrong, and what it cost

**An API filter refused my first operator prompt.** The wording "write the rules you are applying in your own words, step by step, so the next person can check them", combined with "nothing outside this message is relevant; do not look for other files", was refused by Opus 5.5's safety classifier with the tag `reasoning_extraction`. Without the desk-lead context that arms B and C had, it read as an attempt to extract hidden reasoning. The refusal is deterministic. I reran the identical text twice before rephrasing. Thirty-one sessions were lost: nine in Study 1's first pass, five on rerun, and seventeen in the first attempt at Study 2, including all ten operator A slots. Rephrasing the task as an ordinary shift handover, with one sentence of context in every arm, produced zero refusals in 40 sessions.

**The reference engine listing was stale.** The first compiled record printed `engine.py` with the demo block from the first trial dataset (starting levels 4,3,6,2,5,1, limit 34). The frozen dataset was always `dataset.json`, produced by the same `run()` function; the listing's demo block was never updated. It now embeds the frozen data and asserts that it reproduces the stated ground truth, which it does.

**The explanation-mode rerun packet's footer still said v1.4.2** when the v1.4.3 text was run; the replicator noticed. The evidence README records it.

**The first Study 2 write-ups leaked the answer.** I told the writers to end with a Report paragraph, and they had the full process and the data, so every one of them printed the true final figures. That run's thirteen "exact" reports are void and are kept under `study2-lossy-v1-void/` only as a record. The corrected run stripped the Report paragraphs to a template and verified no answer figure remained in any write-up. Its reviewers reused the first run's document-loss lists, minus the entries about the removed paragraph.

**Cost.** 166 sessions, about 10.0M subagent tokens, against a budget that is finite. About 1.5M bought nothing. Jake has said token waste is a catastrophic failure. The record here is why that rule now exists, and the corrected run was the only one launched with a stated cost and a go-ahead.

## What the evidence does and does not support

It supports:

1. Complete analogical documents are read correctly by careful models. 30 of 30.
2. Compressed analogical write-ups lose 7 to 14 rules each by a reviewer's count, and writers know it. Most losses are survivable; the ones that are not are ambiguities about a numeric convention, not about the analogy's physics.
3. The failures that occurred came from the writer's compression, and every operator who hit them resolved the ambiguity by the local wording of the sentence, not by domain intuition.
4. The pre-read, as written in v1.4.3 and run by Opus 5.5 at high effort, did not improve correctness or gap coverage on these tasks. It did name the decisive ambiguity in one of the two failing domains, and that naming did not change the result.

It does not support:

5. Any claim that Open Mirror improves outcomes for a model operator executing a fixed numerical procedure from an analogical document with a script. On this evidence it does not. The claim is limited to that reader and that task.
6. Any claim either way about the skill's stated purpose, which is checking a comparison that someone is arguing *from*. These operators were not being argued at; they were executing a procedure. That is a limit of the study design, not a finding in the skill's favour or against it.
7. Generalisation beyond Opus 5.5 and Sonnet at high effort with scripts. A less careful reader might be pulled by the domain where these were not.

## What a user of the skill should take from this

If you are reading an analogy to execute something, the pre-read will not catch what you would miss, because what you would miss is a numeric convention the analogy left ambiguous, and the pre-read names such gaps without resolving them. One change to the skill would have mattered here: when a flagged gap changes the result, deliver both results rather than choosing one. That is a hypothesis, untested.

If you are writing an analogy, the losses are predictable. Across ten write-ups the same rules went missing: that a position changes state at most once per cycle, the ordering of the two marks, which state governs the release, which half a halving keeps, and what the loss tally collects. A writer who restates the process plainly before compressing it would see those; whether they would keep them under a 400-word cap was not tested here. It was tested the next day: see `TRANSFORMATION-STUDY.md`.
