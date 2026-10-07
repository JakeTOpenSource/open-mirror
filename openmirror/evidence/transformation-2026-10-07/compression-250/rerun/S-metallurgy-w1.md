Every list below runs crucible 1 (charging end) to 6 (tapping end). Whole units of melt, no burn-off. All start BASE, slag tally 0.

Volume: 10, 8, 12, 6, 9, 7
Upper mark: 7, 6, 9, 5, 7, 5
Lower mark: 3, 2, 4, 2, 3, 2
Starting melt: 3, 6, 6, 2, 2, 1

Charges, cycles 1 to 5:
0, 6, 3, 5, 3, 3
4, 2, 0, 1, 1, 7
4, 4, 3, 0, 0, 6
7, 6, 7, 1, 3, 0
0, 6, 6, 3, 3, 0

Five cycles; each step finishes on all six before the next:

Charge: add the cycle's list, even past volume.
Overflow, 1 to 6 in turn: excess over volume runs down the launder into the next crucible before that one's handled; 6's to slag.
State check on melt: BASE at or above upper mark goes SUPERHEATED; SUPERHEATED at or below lower mark goes BASE; otherwise no change.
Return, all figured before anything moves: BASE loses a quarter, rounded down, to slag; SUPERHEATED sends half, rounded down, up the return launder into the previous crucible, crucible 1's to slag. Overfill stays until next cycle's overflow.
Emergency tap: if the six total over 38, each keeps half, rounded down, rest to slag.

Report. At run end hand in: each crucible's end melt and state, in order; every state change as (cycle, position, before, after); tap cycles; slag tally; balance check: starting melt plus charges must equal end melt plus slag.
