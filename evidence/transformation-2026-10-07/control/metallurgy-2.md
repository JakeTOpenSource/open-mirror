Six crucibles: 1 at the charging end, 6 at the tapping end. Melt counts in whole units.

Crucible: 1, 2, 3, 4, 5, 6
Working volume: 10, 8, 12, 6, 9, 7
Upper mark: 7, 6, 9, 5, 7, 5
Lower mark: 3, 2, 4, 2, 3, 2
Starting melt: 3, 6, 6, 2, 2, 1

All start BASE. The slag tally starts at zero and counts everything sent to slag. Emergency tap limit, whole line: 38.

Five cycles, five steps each, in this order; each step finishes on all six before the next starts.

1. Charge. Add the cycle's charge from the table (positions 1 to 6). A crucible can stand over working volume here.

Cycle 1: 0, 6, 3, 5, 3, 3
Cycle 2: 4, 2, 0, 1, 1, 7
Cycle 3: 4, 4, 3, 0, 0, 6
Cycle 4: 7, 6, 7, 1, 3, 0
Cycle 5: 0, 6, 6, 3, 3, 0

2. Overflow. One crucible at a time, 1 through 6: anything above working volume runs down the launder into the next crucible, leaving this one exactly full. Overflow from 6 goes to the slag pit. Overflow from upstream arrives before you check a crucible, so it can cascade down the line.

3. State check, after overflow. BASE at or above the upper mark goes SUPERHEATED. SUPERHEATED at or below the lower mark returns to BASE. Between the marks, no change. At most one change per crucible per cycle. Log each as (cycle, position, before, after).

4. Draw-down. Figure all six amounts from current melt before moving anything. BASE gives a quarter, rounded down, to slag. SUPERHEATED sends half, rounded down, up the return launder into the crucible before it; crucible 1's half goes to slag. Then move all six at once. Returned melt can leave a crucible over working volume until the next cycle's overflow; after cycle 5 it stays over.

5. Emergency tap. Total the six. Strictly over 38: every crucible keeps half, rounded down, the rest to slag; note the cycle. At 38 or under, nothing.

Report. At the end of cycle 5 hand in: the six end quantities, positions 1 to 6; the six end states, same order; every state change as (cycle, position, before, after); the cycles the emergency tap fired; the slag tally; and the balance check: starting melt plus all charges equals end melt plus slag tally.
