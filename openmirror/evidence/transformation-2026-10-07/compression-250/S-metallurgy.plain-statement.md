Mode: explanation mode (step 1 only, as instructed). Plain statement of the engineer's process, every rule and number, nothing added or dropped:

Six cells in a line, numbered 1 to 6; cell 1 is upstream, cell 6 downstream. Each cell has a level L (a whole number, never negative), a fixed capacity C, an upper trigger U and a lower trigger D with D < U <= C, and a mode, NORMAL or ELEVATED. All cells start NORMAL. There is one global limit G and one running tally LOST, starting at 0.

The process runs exactly 5 periods. Each period has five steps, always in this order, and each step finishes for all cells before the next step starts.

Step 1, intake: each cell's level increases by that period's intake amount for that cell, from the intake table. Capacity is not enforced; a level may exceed capacity after intake.

Step 2, spill-over: handle cells one at a time in order 1, 2, 3, 4, 5, 6. If a cell's level is above its capacity, the excess (level minus capacity) is added to cell n+1 and the cell's level becomes exactly its capacity. Excess from cell 6 is added to LOST. Because of the order, excess from one cell arrives in the next before that next cell is handled, so it can push the next cell over capacity in the same step, and so on down the line.

Step 3, mode check, on the level after spill-over: a NORMAL cell with level >= U becomes ELEVATED; an ELEVATED cell with level <= D becomes NORMAL; in every other case the mode does not change (a cell between D and U keeps its mode). Record every change as (period, cell, old mode, new mode). A cell changes at most once per period.

Step 4, release: first compute every cell's release amount from its level at the start of this step: NORMAL gives floor(level / 4), ELEVATED gives floor(level / 2). Compute all six before changing anything, then apply all six at once: every cell's level decreases by its own release amount; a NORMAL cell's release is added to LOST; an ELEVATED cell's release is added to cell n-1, except that cell 1's release, if cell 1 is ELEVATED, is added to LOST. Capacity is not enforced; a cell may hold more than capacity after receiving an upstream transfer, corrected only at the next period's spill-over step, and never if it happens in period 5.

Step 5, global reset: add up all six levels. If the total is strictly greater than G, every cell's level becomes floor(level / 2), every amount removed is added to LOST, and the reset is recorded for this period. If the total is equal to G or less, nothing happens.

After period 5, output: each cell's final level in order 1 to 6; each cell's final mode in order 1 to 6; the complete list of mode changes as (period, cell, old mode, new mode); the list of periods in which a global reset happened; the final value of LOST; and the balance check: (sum of starting levels) + (sum of all intake amounts) must equal (sum of final levels) + LOST.

Data. Capacity C, cells 1 to 6: 10, 8, 12, 6, 9, 7. Upper trigger U: 7, 6, 9, 5, 7, 5. Lower trigger D: 3, 2, 4, 2, 3, 2. Starting level: 3, 6, 6, 2, 2, 1. Global limit G: 38. Intake table (rows periods 1 to 5, columns cells 1 to 6): period 1: 0, 6, 3, 5, 3, 3; period 2: 4, 2, 0, 1, 1, 7; period 3: 4, 4, 3, 0, 0, 6; period 4: 7, 6, 7, 1, 3, 0; period 5: 0, 6, 6, 3, 3, 0.

The process text contains no instructions aimed at the writer. If this plain statement were the whole answer, no picture would be needed; the explanation is a translation into the line's own terms under the given mapping, not a picture being tested.
