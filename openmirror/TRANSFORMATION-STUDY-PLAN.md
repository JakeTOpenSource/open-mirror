# Transformation study: plan (study 3)

**Date:** 7 October 2026. **Project manager:** Claude (Fable 5.1). **Auditors:** Jake and Ed, in parallel, outside the run. **Status:** plan only; nothing has run.

## The goal, in plain words

Show, with a deterministic check, that one piece of meaning can be carried into many different analogies and read back out with nothing lost. "Deterministic" means a machine, not a judge, says whether each read-back is right. "Parallel" means the same meaning goes into ten analogies at once. "Mirrored" means each analogy is read back into action and compared with the original.

The meaning is the six-position, five-cycle process from the coherence study. The machine check is `evidence/coherence-2026-10-06/inputs/engine.py`. The ten analogies are the ten domains already used. None of that is new, so none of it costs anything.

## What the record already shows

- When the analogy is written out in full, the meaning survives: 30 of 30 reads correct.
- When the analogy is compressed to 400 words with no discipline, the meaning mostly survives but drifts in two of ten analogies: 25 of 30 reads correct, every failure from one sentence about rounding that the writer compressed ambiguously.
- Giving the *reader* the Open Mirror pre-read did not stop that drift.

So the untested lever is the *writer*. The drift entered when the writer compressed. The question this study answers:

**Does a writer who uses Open Mirror's discipline (plain statement first, then the analogy, then check your own analogy for break points and lost rules) produce 400-word analogies that read back with zero drift, where undisciplined writers did not?**

If yes: that is the deterministic demonstration you asked for, and the skill's contribution to it is isolated. If no: the skill does not help the writing side either, and that gets published.

## What will not be run, and why

- No pre-read arm for readers. Already tested; no benefit. Rerunning it is waste.
- No "told it is an analogy" arm. It behaved the same as telling the reader nothing.
- No rerun of the undisciplined write-ups. They exist, with 30 graded reads. They are the baseline.
- No Bank A (judging arguments made through metaphor). It answers a different question. It stays on file in TEST-PROTOCOL.md for later.
- No model reviewers writing free-form loss lists. Replaced by a fixed checklist (below) applied identically to both arms.

## Design

**Arm W0, baseline (exists).** Ten 400-word analogies written without the skill, by Opus. Reads: 25 of 30 correct. Files: `evidence/coherence-2026-10-06/study2-lossy-v2/write-ups-as-given/`.

**Arm W1, disciplined (new).** Ten 400-word analogies, same ten domains, same mapping hints, same word cap, same ban on abstract words, same rule that the process is what the line does. One change: the writer gets `SKILL.md` and must (1) write the plain statement first, every rule and every number, nothing added; (2) write the analogy; (3) reread the analogy as a stranger and, for every rule in the plain statement, check it is recoverable from the analogy alone, and for every place the domain's real behaviour would mislead, check the analogy says what the line does; (4) fix what that finds; (5) deliver only the analogy. The plain statement and the self-check findings are returned separately as evidence and never shown to readers. No final figures anywhere; the Report paragraph is a template. Every write-up is grepped for answer figures before use, the hazard that voided the first attempt last time.

**Readers.** Same handover prompt that drew zero refusals in the corrected run, Arm A wording (reader told nothing), same structured deliverable, graded by the engine. Adaptive sampling to save sessions: one read per write-up to start; a second read where the first is wrong; three reads regardless for metallurgy and metamorphosis, the two domains where the baseline drifted. Expected 14 to 16 reads.

**Rule-recovery checklist (new, cheap).** A fixed list of the process's atomic rules, written once by me from `plain-spec.md`. A Sonnet session reads one write-up alone and answers, per rule, recoverable or not, with the quote. Applied identically to all twenty write-ups, W0 and W1. This replaces the free-form reviewer loss lists with a comparable count. It is not fully deterministic; it is structured, quoted, and the same instrument on both arms.

**Models.** Writers: Opus 5.5, because the baseline writers were Opus and the writer is the variable under test; changing the model would confound it. Readers: Opus 5.5 for the same reason. Checklist extractor: Sonnet 5.5, since it is a lookup task. If quota requires all-Sonnet, say so; the price is that W1 is then not directly comparable to W0 and a 9-session Sonnet calibration on the baseline would be needed first.

## Pass and fail, decided before the run

- **Primary, deterministic:** W1 reads correct. Target 100 percent. Baseline 25 of 30 (83 percent). Any W1 read that is wrong is reported with its cause from the reader's own procedure summary.
- **Secondary:** rules recoverable per write-up, W1 against W0, same checklist.
- **Discipline check:** every W1 write-up at or under 400 words, free of answer figures, with a plain statement and a non-empty self-check on file. A write-up that fails this is rerun once with the defect named; a second failure is reported as a writer-prompt defect and not patched silently.

**Stop rules.** If three or more W1 write-ups fail the discipline check, stop after the writers and report. If W1 drifts in the same two domains for the same reason, stop after the reads and report; the skill does not fix the writing side. No session is ever retried with identical text after a refusal.

## Cost

| Phase | Sessions | Model | Tokens, estimate |
|---|---|---|---|
| 1. Writers | 10, plus up to 3 reruns | Opus | 0.2M to 0.3M |
| 2. Readers | 14 to 16, adaptive, cap 20 | Opus | 1.0M to 1.4M |
| 3. Checklist | 20 | Sonnet | 0.3M |
| **Total** | **44 to 53** | | **1.5M to 2.0M** |

Compared with the last run, which was 40 sessions and 2.66M, this is cheaper per answer and asks a sharper question. Nothing launches without a "go". I will report at the end of each phase without asking again unless a stop rule fires.

## What success and failure each mean for the skill

- **Success** (W1 at or near 100 percent, more rules recoverable): the first evidence that Open Mirror does what the pitch says, on the writing side, with a machine as judge. The README changes from "no measured benefit" to "measured benefit for writers; none for readers".
- **Failure** (W1 no better than W0): the skill's discipline does not survive a word cap any better than good intent does. The README says so, and the next step is changing the skill, not more testing.
