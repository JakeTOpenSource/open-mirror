Six chambers, 1 first, 6 last, holding whole units of nutrient mass. All start LARVAL; loss tally at 0.

Chambers 1 to 6:
Capacity: 10, 8, 12, 6, 9, 7
Upper mark: 7, 6, 9, 5, 7, 5
Lower mark: 3, 2, 4, 2, 3, 2
Start: 3, 6, 6, 2, 2, 1
Global limit: 38

Feed, rows are cycles 1 to 5:
0, 6, 3, 5, 3, 3
4, 2, 0, 1, 1, 7
4, 4, 3, 0, 0, 6
7, 6, 7, 1, 3, 0
0, 6, 6, 3, 3, 0

Each cycle, in order, each step finished on all chambers before the next:

Feed: add the row, ignoring capacity.
Carry: chambers 1 to 6 in turn; excess over capacity moves into the next chamber before its turn. Chamber 6's goes to the tally.
States: LARVAL at or above upper mark turns PUPAL; PUPAL at or below lower mark returns LARVAL, routinely. Otherwise unchanged. Log changes.
Metabolise: figure all amounts from current mass, then apply together, rounding down. LARVAL metabolises a quarter to the tally; PUPAL passes half into the chamber numbered one lower (chamber 1's to the tally). Overfull chambers wait for next cycle's carry.
Moult: if the six total over 38, halve each, rounding down; removed mass to the tally.

Report. After cycle 5: end quantities and states, positions 1 to 6; every state change as (cycle, position, before, after); moult cycles; loss tally; balance check: start total plus all feed equals end total plus tally.
