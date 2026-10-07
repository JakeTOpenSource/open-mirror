Six crucibles in a cascade: 1 at the charging end, 6 at the tapping end. Melt counts in whole units. Every row reads positions 1 to 6.

Capacity: 10 8 12 6 9 7
Upper mark: 7 6 9 5 7 5
Lower mark: 3 2 4 2 3 2
Starting melt: 3 6 6 2 2 1

All start BASE. Loss tally, everything sent to slag, starts at 0. Global reset limit: 38.

Charges by cycle:
Cycle 1: 0 6 3 5 3 3
Cycle 2: 4 2 0 1 1 7
Cycle 3: 4 4 3 0 0 6
Cycle 4: 7 6 7 1 3 0
Cycle 5: 0 6 6 3 3 0

Five cycles, five steps each, in order; each step finishes on all six before the next.

1. Charge. Add each crucible's charge. It may sit above capacity until step 2.

2. Overflow. Walk 1 to 6. Excess over capacity runs down the launder to the next crucible; this one stays exactly full. It lands before you reach that crucible, so overflow can carry down the line. From 6 it goes to the slag pit, not a ladle.

3. State check, on contents after overflow. Melt quantity decides state, not the pyrometer. BASE at or above its upper mark goes SUPERHEATED. SUPERHEATED at or below its lower mark goes back to BASE. Between the marks, state carries over unchanged. State changes only here, at most once per crucible per cycle.

4. Draw-off. Figure all six amounts from current contents before moving anything, rounding down. BASE: a quarter to slag. SUPERHEATED: half back up the return launder into the previous crucible, toward the charging end, none to slag; crucible 1's half goes to slag. Then move all at once. Returned melt can put a crucible over capacity; it stays until next cycle's overflow, or for good after cycle 5.

5. Global reset. Total all six. Strictly above 38: emergency tap, halve every crucible, rounding down, removed melt to slag; note the cycle. At 38 or below, nothing.

Report. At the end of cycle 5 hand in: the six end quantities, positions 1 to 6; the six end states, same order; every state change as (cycle, position, before, after); the cycles the global reset fired; the loss tally; and the balance check: starting melt plus all charges must equal end melt plus loss tally.
