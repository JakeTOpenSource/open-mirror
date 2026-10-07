# The process (abstract form; never shown to operators)

There are six cells in a line, numbered 1 to 6. Cell 1 is upstream, cell 6 is downstream. Each cell has:
- a level L: a whole number, never negative;
- a fixed capacity C;
- an upper trigger U and a lower trigger D, with D < U <= C;
- a mode, which is either NORMAL or ELEVATED. All cells start NORMAL.

There is one global limit G and one running tally LOST, which starts at 0.

The process runs for exactly 5 periods. Each period has five steps, always in this order. A step finishes for all cells before the next step starts.

STEP 1, INTAKE. Each cell's level increases by that period's intake amount for that cell, read from the intake table. Capacity is NOT enforced in this step; a level may exceed capacity after intake.

STEP 2, SPILL-OVER. Handle the cells one at a time, in the order 1, 2, 3, 4, 5, 6. When a cell is handled: if its level is above its capacity, the excess (level minus capacity) is added to the next cell downstream (cell n+1), and the cell's level becomes exactly its capacity. Excess from cell 6 is added to LOST. Because cells are handled in order, excess from cell 1 arrives in cell 2 before cell 2 is handled, so one cell's excess can push the next cell over capacity in the same step, and so on down the line.

STEP 3, MODE CHECK. For each cell, look at its level now (after spill-over). If the cell is NORMAL and its level is greater than or equal to U, it becomes ELEVATED. If the cell is ELEVATED and its level is less than or equal to D, it becomes NORMAL. In every other case the mode does not change; in particular, a cell whose level is between D and U keeps whatever mode it had. Record every change as (period, cell, old mode, new mode). A cell changes at most once per period.

STEP 4, RELEASE. First, for every cell, compute its release amount from its level at the start of this step: a NORMAL cell's release is floor(level / 4); an ELEVATED cell's release is floor(level / 2). Compute all six amounts before changing anything. Then apply all six at once:
- every cell's level decreases by its own release amount;
- a NORMAL cell's release is added to LOST;
- an ELEVATED cell's release is added to the level of the cell immediately upstream (cell n-1); the release of cell 1, if cell 1 is ELEVATED, is added to LOST.
Capacity is NOT enforced in this step. A cell may hold more than its capacity after receiving an upstream transfer. That is corrected only at the next period's spill-over step (and never, if it happens in period 5).

STEP 5, GLOBAL RESET. Add up all six levels. If the total is strictly greater than G, every cell's level becomes floor(level / 2), and every amount removed is added to LOST; record that a reset happened in this period. If the total is equal to G or less, nothing happens.

After period 5, the output is:
- each cell's final level, in order 1 to 6;
- each cell's final mode, in order 1 to 6;
- the complete list of mode changes as (period, cell, old mode, new mode);
- the list of periods in which a global reset happened;
- the final value of LOST;
- the balance check: (sum of starting levels) + (sum of all intake amounts) must equal (sum of final levels) + LOST.

## Data

Capacity C, cells 1 to 6: 10, 8, 12, 6, 9, 7
Upper trigger U: 7, 6, 9, 5, 7, 5
Lower trigger D: 3, 2, 4, 2, 3, 2
Starting level: 3, 6, 6, 2, 2, 1
Global limit G: 38

Intake table (rows are periods 1 to 5; columns are cells 1 to 6):
Period 1: 0, 6, 3, 5, 3, 3
Period 2: 4, 2, 0, 1, 1, 7
Period 3: 4, 4, 3, 0, 0, 6
Period 4: 7, 6, 7, 1, 3, 0
Period 5: 0, 6, 6, 3, 3, 0
