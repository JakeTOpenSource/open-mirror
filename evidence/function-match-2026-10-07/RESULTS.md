# Function-match test: results

**Run:** 7 October 2026, 32 Opus 5.5 judge sessions (16 pairs, 2 independent judges each), zero refusals, zero reruns, 2.28M tokens against a stated 2.6M to 3.2M. **Plan:** `PLAN.md`, committed before the run. **Containment:** each session confined to a folder holding only its pair's two documents; all 32 transcripts audited (`judges/audit.json`): no git command, no read outside the folder, no answer string from anything but the session's own script. **Grading:** `grade_fm.py` against `key.json`, with every judge's probe re-executed by the engine; regraded independently by `verify.py` claims FM-1 to FM-9.

## Outcome

| Measure | Result |
|---|---|
| Verdict correct (SAME or DIFFERENT) | **32 of 32** |
| Correspondence-table route correct on its own | 32 of 32 |
| Probe route correct on its own | 32 of 32 |
| Two routes agree within a session | 32 of 32 |
| Two judges agree on a pair | 16 of 16 pairs |
| Probe genuine (judge's reported outputs for its own probe match the engine, both documents) | 32 of 32 |
| Printed-table executions match the engine, both documents | 32 of 32 |
| Probe separates the two functions, on DIFFERENT pairs | 16 of 16 |
| Hidden pairs P15 and P16 (no difference on the printed data) caught | 4 of 4 sessions, each by both routes |
| Differing rule named correctly on DIFFERENT pairs | 16 of 16 (quoted in `judges/*.json`) |

Pre-registered reading: **function matching across lexicons is doable by this method.** Every threshold in the plan's first row was met.

## What the judges did

Each judge built a translation table first (for example "LAMINAR = GREEN, CAVITATING = HOT, inception mark = upper mark, overboard = waste tally") and compared the six rule groups under it. The four reworded-but-identical pairs were all called SAME, and every judge said why: "A computes everything first and applies it all at once; B handles one position at a time in order 1 to 6, but since each transfer goes to a position already handled, the results are identical", and for the restated halving, "closing the larger half rounded up leaves exactly half rounded down." Those are the right proofs, not just the right answers.

For the probes, judges chose inputs that trip the boundaries: totals of exactly 38, positions exactly at a trigger mark, cascades through several positions, position 1 in the raised state. One judge searched 200,000 random tables with both implementations and reported zero mismatches on a SAME pair. On the two hidden pairs, where the printed data gives the same end report under both documents, every judge found the difference in the table ("B halves only the raised positions") and then built a probe on which the two documents diverge, which the engine confirms.

## What this does and does not show

It shows that a model can decide whether two descriptions in unrelated vocabularies compute the same function, with the same switches and breakers, and can prove it two ways that agree with each other and with an independent judge, 32 times out of 32, including the cases where running the printed example would have said "same" for a different function. That is the "mirror the function, not the semantics, and trace it back by different routes" claim, demonstrated on this process.

It does not show this for processes a judge cannot execute. Every document here describes a finite arithmetic procedure, so the probe route has a machine behind it. For theories that are not executable, only the correspondence route exists, and this test says nothing about how reliable it is alone, though here it was correct 32 of 32 on its own. It does not show anything about the Open Mirror skill: the judge prompt was a plain instruction, and the materials were chosen to be hard but fair, with one rule changed per pair. Two or more simultaneous changes, or changes buried in prose rather than in a rule sentence, were not tested. The ten base documents were themselves written by one model from one specification, which is why their vocabularies differ but their structure is parallel; documents written independently by different people would be a harder test.

## Cost

32 sessions, 2.28M tokens. All runs since 6 October: 333 sessions, about 21.5M.
