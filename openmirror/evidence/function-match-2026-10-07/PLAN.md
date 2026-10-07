# Function-match test: plan, committed before the run

**Date:** 7 October 2026. **Asked for by:** Jake: "map out when a theory becomes an exact match with another theory, even with different wording. Mirroring the function instead of the semantics, and being able to trace it back in different ways but get the same result"; "identifying and reverse engineering when two circuits have the same designed breakers and switches, regardless of the model, semantics, lexicon or user."

## Question

Given two operating documents written in different fields, can a model decide whether they compute the same function, with the same switches (hysteresis triggers), breakers (the global reset), rounding and routing, and show it by two independent routes that reach the same verdict? Not "do they say the same thing" but "would they give the same end report for every possible input".

## Materials, built deterministically (`build_pairs.py`, `fm_engine.py`, `key.json`)

The ten complete analogical documents from the 6 October coherence study, each about 1,150 words, each of which blind operators executed correctly 30 of 30 times. Sixteen pairs, each pair two documents from different fields:

| Class | Pairs | What differs | Truth |
|---|---|---|---|
| Untouched | P01 to P04 | Lexicon only | SAME |
| Reworded rule, identical function | P05 to P07: step 4 restated as one-cell-at-a-time in order 1 to 6 (provably identical, because transfers go to cells already handled). P08: the halving restated as "close the larger half, rounded up, keep the rest" | SAME |
| One switch or breaker changed, visible on the given data | P09 halving keeps the larger half; P10 breaker fires at 38 or more; P11 upper trigger strictly above; P12 lower trigger strictly below; P13 transfers go downstream; P14 triggers read before the spill-over | DIFFERENT |
| One breaker changed, invisible on the given data | P15, P16: the halving skips cells in the resting state. Same end report on the given tables; different function | DIFFERENT |

Every edited document differs from its source by the listed sentences only, in that field's own vocabulary; the build script refuses to run if an edit does not match exactly once. The engine computes each document's true function. Judges never see the repository, the engine, the key, the class labels, or the word "variant".

## Judges

Opus 5.5, one session per pair per judge, confined to a scratch folder holding only that pair's two documents. Prompt, in full, in `judge-prompt.txt`. It asks for:

1. **Route 1, correspondence table.** For each of the five steps and the report: the rule as document A states it, the rule as document B states it, SAME or DIFFERENT, and if different, exactly what differs.
2. **Route 2, probe.** The judge chooses its own starting amounts and five-row input table (whole numbers 0 to 9) designed to expose any difference it suspects, executes both documents on that probe and on their own given tables (a script is fine), and reports all four end reports.
3. **Verdict.** SAME or DIFFERENT, the one differing rule named if DIFFERENT, and whether the two routes agree. If they disagree, which it trusts and why.

No hint of how many pairs are SAME. Two judges per pair, independent sessions, so that agreement between judges is itself measured.

## Scoring, fixed now

Per judge session, from the engine:

- **Verdict correct** against `key.json`.
- **Rule named correctly** for DIFFERENT pairs: the judge's named difference is the edited rule (hand-checked against the key, recorded verbatim).
- **Probe genuine:** the judge's reported end reports for its probe match the engine run of each document's true function on that probe. A judge whose reported outputs do not match the engine did not execute what it claims.
- **Probe separating:** for DIFFERENT pairs, the probe produces different end reports under the two functions.
- **Routes agree:** the table verdict and the probe verdict are the same.
- **Hidden pairs:** for P15 and P16, which route caught the difference, since execution on the given tables cannot.

## Outcome rules

| Result | Reading |
|---|---|
| Verdicts correct in at least 30 of 32 sessions, both hidden pairs caught by both judges, probes engine-verified in at least 28 of 32 | Function matching across lexicons is doable by this method |
| Verdicts correct in at least 30 of 32 but a hidden pair missed | Doable for differences that show on the data; the mapping route is not yet reliable for breakers that the given data never trips |
| Fewer than 30 of 32 correct | Not doable at this reliability by this method; failures listed by class |
| Judges disagree on 4 or more pairs | The method is not deterministic across judges, whatever the accuracy |

The judge prompt is a plain instruction and does not use Open Mirror. If the method works, a second arm with the skill is a separate, later decision. If a judge session is refused by the API, it is rerun once with reworded framing, never with identical text; a refused slot after that is reported as missing.

## Cost, stated before the run

32 sessions. Each judge reads two 1,150-word documents, writes and runs a script, and reports four end reports: estimated 80k to 100k tokens each, so 2.6M to 3.2M in total. A one-judge version is 16 sessions, 1.3M to 1.6M, and loses the agreement measure.

## Containment

Each session starts in its own scratch folder containing only `A.md` and `B.md`. The prompt forbids reading, listing, changing or committing anything outside it and forbids git. All transcripts are audited after the run with the same script used for the clean 250-word rerun (`audit_wf.py`): no git, no reads outside the folder, no answer strings from anything but the session's own script.
