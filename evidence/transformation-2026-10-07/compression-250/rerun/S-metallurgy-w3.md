Crucibles 1 (charging end) to 6 (tapping end) cascade. Melt is whole units. All start BASE; slag tally 0.

By position: capacity 10 8 12 6 9 7; upper mark 7 6 9 5 7 5; lower mark 3 2 4 2 3 2; starting melt 3 6 6 2 2 1.

Charges, cycle 1 first:
0 6 3 5 3 3
4 2 0 1 1 7
4 4 3 0 0 6
7 6 7 1 3 0
0 6 6 3 3 0

Five cycles of these steps, each step finished line-wide before the next:

1. Charge per the table, even past capacity.
2. Overflow, 1 to 6 in turn: excess over capacity runs down the launder into the next, possibly overfilling it; 6's to slag.
3. State check: BASE at or above upper mark goes SUPERHEATED; SUPERHEATED at or below lower mark goes BASE; otherwise unchanged. States change only here.
4. Draws, all figured before moving: BASE sends a quarter, rounded down, to slag; SUPERHEATED sends half, rounded down, up the return launder to the previous crucible, crucible 1's to slag. Overfill waits for next cycle's overflow, or stays after cycle 5.
5. Line total over 38: global reset, each keeps half rounded down, rest to slag.

Report, after cycle 5: end quantities and states, positions 1 to 6; every state change as (cycle, position, before, after); global reset cycles; slag tally; balance check: starting melt plus charges equals end melt plus slag.
