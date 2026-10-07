Mode: explanation mode (step 1 plain statement only; the domain picture is fixed by the brief).

Six cells in a line, numbered 1 (upstream) to 6 (downstream). Each cell has a level L (whole number, never negative), a fixed capacity C, an upper trigger U and a lower trigger D with D < U <= C, and a mode, NORMAL or ELEVATED. All cells start NORMAL. One global limit G. One running tally LOST, starting at 0.

The process runs exactly 5 periods. Each period has five steps in this fixed order; each step finishes for all cells before the next step starts.

Step 1, intake: each cell's level rises by that period's intake for that cell from the intake table. Capacity is not enforced; a level may exceed capacity after intake.

Step 2, spill-over: handle cells one at a time in order 1, 2, 3, 4, 5, 6. If a cell's level is above its capacity, the excess (level minus capacity) is added to cell n+1 and the cell's level becomes exactly its capacity. Excess from cell 6 is added to LOST. Because of the order, excess arriving from cell n-1 is in place before cell n is handled, so excess can cascade down the line in the same step.

Step 3, mode check, using the level after spill-over: a NORMAL cell with level >= U becomes ELEVATED; an ELEVATED cell with level <= D becomes NORMAL; in every other case the mode is unchanged (a cell between D and U keeps its mode). Record every change as (period, cell, old mode, new mode). A cell changes at most once per period.

Step 4, release: first compute every cell's release from its level at the start of this step, all six before changing anything: NORMAL release = floor(level/4); ELEVATED release = floor(level/2). Then apply all at once: each cell's level falls by its own release; a NORMAL cell's release is added to LOST; an ELEVATED cell's release is added to cell n-1, except that cell 1's release (if ELEVATED) is added to LOST. Capacity is not enforced; a cell may exceed capacity after receiving a transfer, corrected only at the next period's spill-over, and never if this happens in period 5.

Step 5, global reset: sum the six levels. If the total is strictly greater than G, every level becomes floor(level/2), every removed amount is added to LOST, and the period is recorded as a reset period. If the total is G or less, nothing happens.

Output after period 5: each cell's final level in order 1 to 6; each cell's final mode in order 1 to 6; the complete list of mode changes as (period, cell, old mode, new mode); the list of periods with a global reset; the final LOST; the balance check: (sum of starting levels) + (sum of all intake amounts) must equal (sum of final levels) + LOST.

Data. Capacity C, cells 1 to 6: 10, 8, 12, 6, 9, 7. Upper trigger U: 7, 6, 9, 5, 7, 5. Lower trigger D: 3, 2, 4, 2, 3, 2. Starting level: 3, 6, 6, 2, 2, 1. Global limit G: 38. Intake table (rows periods 1 to 5, columns cells 1 to 6): period 1: 0, 6, 3, 5, 3, 3; period 2: 4, 2, 0, 1, 1, 7; period 3: 4, 4, 3, 0, 0, 6; period 4: 7, 6, 7, 1, 3, 0; period 5: 0, 6, 6, 3, 3, 0.
