Six tanks in series, tank 1 at the inlet, tank 6 at the outfall. Liquor is counted in whole units, never below zero.

Tank:            1  2  3  4  5  6
Volume:         10  8 12  6  9  7
Upper mark:      7  6  9  5  7  5
Lower mark:      3  2  4  2  3  2
Opening liquor:  3  6  6  2  2  1

All tanks open STEADY. Loss tally opens at 0. Storm bypass limit: 38.

Feed, tanks 1 to 6:
Cycle 1: 0 6 3 5 3 3
Cycle 2: 4 2 0 1 1 7
Cycle 3: 4 4 3 0 0 6
Cycle 4: 7 6 7 1 3 0
Cycle 5: 0 6 6 3 3 0

Five cycles, five jobs each, in order; finish each job on all six tanks first.

1. Feed. Each tank takes its own delivery directly, even past volume.

2. Weirs. Go tank 1 to 6. Anything over volume passes the weir into the next tank, leaving it exactly full. Overflow lands before the next tank's turn and can push that one over too. Tank 6 overflows to outfall.

3. States. After the weirs, a STEADY tank at or above its upper mark goes OVERLOADED; an OVERLOADED tank at or below its lower mark goes STEADY. Between the marks it keeps its state. Log each change as (cycle, position, before, after); at most one per tank per cycle.

4. Discharge. Using those states, work out all six amounts from current contents before moving anything, rounding down. STEADY: a quarter to outfall. OVERLOADED: half back through the return line to the tank just upstream; tank 1 sends its half to outfall. Then move all at once. No volume cap here; an overfull tank waits for next cycle's weirs, and after cycle 5 it stays overfull.

5. Storm bypass. If the six tanks total more than 38, each keeps half, rounded down, and the rest goes to outfall; log the cycle. At 38 or under, nothing happens.

Everything reaching outfall goes on the loss tally. Nothing else leaves the line.

Report
At the end of cycle 5, hand in: the six end quantities and six end states, positions 1 to 6; every state change as (cycle, position, before, after); the cycles the storm bypass fired; the loss tally; and the balance check: opening liquor plus all feed must equal end quantities plus the loss tally.
