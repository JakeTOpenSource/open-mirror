Open Mirror, step 1 only (plain statement of the engineer's process; nothing added, nothing dropped). Note from the source: this abstract form is never shown to operators.

There are six cells in a row, numbered 1 to 6, with 1 upstream and 6 downstream. Each cell has a level L, which is a whole number and never negative. It also has a fixed capacity C, an upper trigger U and a lower trigger D, where D < U <= C, and a mode, which is NORMAL or ELEVATED. All cells start NORMAL. There is one global limit G and one running tally LOST, which starts at 0.

The process runs exactly 5 periods. Each period has five steps, always in the order below. Each step finishes for all cells before the next step starts.

Step 1, intake: each cell's level rises by that period's amount for that cell, taken from the intake table. Capacity is not enforced, so a level may end up above capacity.

Step 2, spill-over: handle cells one at a time, in order 1 to 6. If a cell's level is above its capacity, the excess (level minus capacity) is added to cell n+1 and the cell's level is set to exactly its capacity. Excess from cell 6 is added to LOST. Because the order is 1 to 6, excess reaches the next cell before that cell is handled, so it can push that cell over capacity in the same step, and so on down the line.

Step 3, mode check: use each cell's level after spill-over. A NORMAL cell with level >= U becomes ELEVATED. An ELEVATED cell with level <= D becomes NORMAL. In every other case the mode stays as it is, so a cell with a level between D and U keeps its mode. Record every change as (period, cell, old mode, new mode). A cell changes at most once per period.

Step 4, release: first compute every cell's release amount from its level at the start of this step. A NORMAL cell releases floor(level/4) and an ELEVATED cell releases floor(level/2). All six amounts are computed before anything changes, and then all six are applied at once. Every cell's level drops by its own amount. A NORMAL cell's amount is added to LOST. An ELEVATED cell's amount is added to cell n-1, except that cell 1's amount (if cell 1 is ELEVATED) is added to LOST. Capacity is not enforced, so a cell may hold more than its capacity after receiving a transfer. This is corrected only at the next period's spill-over, and never if it happens in period 5.

Step 5, global reset: add up all six levels. If the total is strictly greater than G, every level becomes floor(level/2), every removed amount is added to LOST, and the period is recorded as a reset. If the total is equal to or less than G, nothing happens.

Output after period 5: each cell's final level (1 to 6); each cell's final mode (1 to 6); the full list of mode changes as (period, cell, old, new); the periods in which a reset happened; the final LOST; and the balance check, which is sum of starting levels + sum of all intake amounts = sum of final levels + LOST.

Data. Capacity C, cells 1 to 6: 10, 8, 12, 6, 9, 7. Upper trigger U: 7, 6, 9, 5, 7, 5. Lower trigger D: 3, 2, 4, 2, 3, 2. Starting level: 3, 6, 6, 2, 2, 1. Global limit G: 38. Intake table (rows are periods 1 to 5, columns are cells 1 to 6): P1: 0, 6, 3, 5, 3, 3. P2: 4, 2, 0, 1, 1, 7. P3: 4, 4, 3, 0, 0, 6. P4: 7, 6, 7, 1, 3, 0. P5: 0, 6, 6, 3, 3, 0.
