Six stages in a chain: 1 at the source, 6 at the load. Every cycle runs five moves in order, each finished chain-wide before the next. Everything starts CLEAR; ground tally starts at zero.

Ratings, stages 1 to 6: 10, 8, 12, 6, 9, 7. Upper thresholds: 7, 6, 9, 5, 7, 5. Lower thresholds: 3, 2, 4, 2, 3, 2. Starting charge: 3, 6, 6, 2, 2, 1. Breaker setting: 38 total.

1. Charge in. Add the cycle's feed to each stage; ratings aren't enforced here.
Cycle 1: 0, 6, 3, 5, 3, 3
Cycle 2: 4, 2, 0, 1, 1, 7
Cycle 3: 4, 4, 3, 0, 0, 6
Cycle 4: 7, 6, 7, 1, 3, 0
Cycle 5: 0, 6, 6, 3, 3, 0

2. Shunts. Walk 1 to 6. A stage over rating dumps the excess into the next stage down and sits at exactly rating; stage 6's excess goes to ground. Walking in order, 1's excess can tip 2 before you reach 2.

3. Comparators. Read each stage now. CLEAR goes ASSERTED at or above its upper threshold; ASSERTED goes CLEAR at or below its lower. In between it holds. Log every flip.

4. Bleed. Take all six readings first, then move everything at once. A CLEAR stage leaks a quarter, rounded down, to ground. An ASSERTED stage sends half, rounded down, back through its return diode to the stage before; stage 1's goes to ground. Ratings aren't checked here, so a stage can sit over until next cycle's shunts, or for good after cycle 5.

5. Breaker. Sum the chain. Strictly over 38, every stage halves, rounded down, the difference to ground; note the cycle. At 38 or under, nothing.

Report. End of cycle 5, charge 1 to 6: 6, 10, 9, 7, 4, 2. States: ASSERTED, ASSERTED, ASSERTED, ASSERTED, ASSERTED, CLEAR. Flips (cycle, position, before, after): (1,2,CLEAR,ASSERTED) (1,3,CLEAR,ASSERTED) (1,4,CLEAR,ASSERTED) (1,5,CLEAR,ASSERTED) (2,1,CLEAR,ASSERTED) (2,3,ASSERTED,CLEAR) (2,5,ASSERTED,CLEAR) (2,6,CLEAR,ASSERTED) (3,3,CLEAR,ASSERTED) (3,4,ASSERTED,CLEAR) (4,4,CLEAR,ASSERTED) (4,5,CLEAR,ASSERTED) (5,6,ASSERTED,CLEAR). Breaker tripped cycles 1 and 4 (cycle 5 closed at exactly 38). Ground tally: 76. Balance: 20 starting plus 94 fed is 114; 38 on the chain plus 76 to ground is 114. Stage 2 at 10 over its 8 rating is cycle-5 diode return; report it as read.