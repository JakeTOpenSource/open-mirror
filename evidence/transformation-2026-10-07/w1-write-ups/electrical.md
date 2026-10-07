Six storage stages in a chain: position 1 at the source end, 6 at the load end. Charge comes in whole units, never negative. Each stage has a rating and a Schmitt-trigger comparator reading ASSERTED or CLEAR.

Rows run position 1 to 6.
Rating: 10, 8, 12, 6, 9, 7
Upper threshold: 7, 6, 9, 5, 7, 5
Lower threshold: 3, 2, 4, 2, 3, 2
Starting charge: 3, 6, 6, 2, 2, 1

Charge input:
Cycle 1: 0, 6, 3, 5, 3, 3
Cycle 2: 4, 2, 0, 1, 1, 7
Cycle 3: 4, 4, 3, 0, 0, 6
Cycle 4: 7, 6, 7, 1, 3, 0
Cycle 5: 0, 6, 6, 3, 3, 0

Breaker trip point: 38. All stages start CLEAR; loss tally starts at zero.

Five cycles, five steps each, in this order. Each step finishes everywhere before the next starts.

1. Charge. Add each stage's input; ratings aren't enforced, so stages can exceed rating.

2. Shunts. Go 1 to 6 in turn. A stage over rating drops to exactly its rating and passes the excess to the next stage toward the load before that one is checked, so excess can cascade in one pass. Stage 6's excess goes to ground.

3. Comparators. On post-shunt charge: CLEAR at or above upper goes ASSERTED; ASSERTED at or below lower goes CLEAR; in between, it holds. States change only here, at most once per cycle. Log each change as (cycle, position, before, after).

4. Leak and feedback. Work out all six amounts from present charges, then move them together. CLEAR leaks a quarter of its charge, rounded down, to ground. ASSERTED instead sends half, rounded down, back through the return diode to the stage just before it, toward the source; stage 1's feedback goes to ground. Ratings aren't enforced: overcharge waits for next cycle's shunts; after cycle 5, none.

5. Breaker. Every cycle, if the six total strictly above 38, it trips: each stage keeps half, rounded down; the rest goes to ground. At 38 or below, nothing.

Everything sent to ground goes on the loss tally.

Report. After cycle 5, hand in: each stage's end charge, source end first; each end state, same order; every state change as (cycle, position, before, after); the cycles the breaker tripped; the loss tally; and the balance check: starting charge plus all input equals end charge plus loss tally.
