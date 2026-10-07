# Rearing Line Operating Sheet

Purpose: run the six-chamber rearing line for five cycles from the starting masses and feed schedule below, then deliver the end-of-run report.

## Definitions

- **Chamber**: one of the six rearing chambers in the line, numbered 1 to 6. Chamber 1 is first in the line and chamber 6 is last. The "next chamber" after chamber n is chamber n+1. The "previous chamber" before chamber n is chamber n-1.
- **Mass**: the nutrient mass a chamber holds, counted in whole units. Mass is always a whole number and is never negative. Whenever this sheet tells you to take a quarter or a half of a mass, divide and round down to a whole number. For example, a quarter of 7 is 1 and half of 7 is 3.
- **Holding limit**: each chamber's fixed maximum mass. The limit is applied only in step 2.
- **Pupation mark**: the mass at or above which a LARVAL chamber becomes PUPAL.
- **Return mark**: the mass at or below which a PUPAL chamber goes back to LARVAL. In every chamber the return mark is below the pupation mark, and the pupation mark is no higher than the holding limit.
- **Stage**: every chamber is either LARVAL or PUPAL. All six chambers start LARVAL. A return from PUPAL to LARVAL is ordinary, and you make it whenever the rule in step 3 calls for it.
- **Feed charge**: the units of nutrient mass added to a chamber in a given cycle, read from the feed schedule.
- **Moult limit**: a single figure for the whole line, 38 units.
- **Moult**: the halving of the whole line in step 5.
- **Waste tally**: the running total of all mass that is discarded or metabolised away. It starts at 0.
- **Cycle**: one full pass through steps 1 to 5. The run has exactly 5 cycles, numbered 1 to 5.

## Chamber settings

| Chamber | Holding limit | Pupation mark | Return mark | Starting mass |
|---|---|---|---|---|
| 1 | 10 | 7 | 3 | 3 |
| 2 | 8 | 6 | 2 | 6 |
| 3 | 12 | 9 | 4 | 6 |
| 4 | 6 | 5 | 2 | 2 |
| 5 | 9 | 7 | 3 | 2 |
| 6 | 7 | 5 | 2 | 1 |

Moult limit: 38 units. Waste tally at the start: 0. Stage at the start: LARVAL in all six chambers.

## Procedure for one cycle

Carry out the five steps in the order 1, 2, 3, 4, 5. Finish each step for all six chambers before you begin the next step.

**Step 1: Feeding.** Add this cycle's feed charge from the feed schedule to each chamber's mass. The holding limit is not enforced in this step. After feeding, a chamber may hold more than its holding limit.

**Step 2: Carry-forward.** Go through the chambers one at a time, in the order 1, 2, 3, 4, 5, 6. When you reach a chamber, check whether its mass is more than its holding limit. If it is, work out the excess (mass minus holding limit), add that excess to the next chamber, and set this chamber's mass to exactly its holding limit. If the mass is at most the holding limit, leave the chamber alone. Excess from chamber 6 is discarded and added to the waste tally. Because you work in order, excess carried out of chamber 1 is already in chamber 2 by the time you reach chamber 2. That excess can push chamber 2 over its limit in the same step, and the same can happen to each chamber further down the line.

**Step 3: Stage check.** For each chamber, read its mass as it stands now, after step 2.
- If the chamber is LARVAL and its mass is at least its pupation mark, it becomes PUPAL.
- If the chamber is PUPAL and its mass is at most its return mark, it becomes LARVAL.
- In every other case the stage does not change. In particular, a chamber whose mass is more than its return mark and less than its pupation mark keeps the stage it already had.

Record every stage change as (cycle, chamber, stage before, stage after). A chamber changes stage at most once per cycle.

**Step 4: Metabolism and reabsorption.** First work out an amount for every chamber, using its mass at the start of this step and its stage as it stands after step 3:
- LARVAL chamber: a quarter of its mass, rounded down.
- PUPAL chamber: half of its mass, rounded down.

Work out all six amounts before you change any mass. Then apply all six at the same time:
- Take each chamber's own amount away from its mass.
- A LARVAL chamber's amount is metabolised away and added to the waste tally.
- A PUPAL chamber's amount is reabsorbed into the previous chamber (chamber n-1) and added to that chamber's mass. If chamber 1 is PUPAL, its amount is discarded and added to the waste tally.

The holding limit is not enforced in this step. A chamber may hold more than its holding limit after it receives reabsorbed mass. That excess is only corrected in step 2 of the next cycle. If it happens in cycle 5, it is never corrected.

**Step 5: Moult check.** Add up the masses of all six chambers. If the total is more than the moult limit of 38, the line moults: every chamber's mass becomes half of its mass, rounded down. All mass removed from every chamber is discarded and added to the waste tally, and you record this cycle as a moult cycle. If the total is 38 or less, nothing happens.

## Feed schedule

Units of nutrient mass added in step 1, by cycle and chamber:

| Cycle | Chamber 1 | Chamber 2 | Chamber 3 | Chamber 4 | Chamber 5 | Chamber 6 |
|---|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 5 | 3 | 3 |
| 2 | 4 | 2 | 0 | 1 | 1 | 7 |
| 3 | 4 | 4 | 3 | 0 | 0 | 6 |
| 4 | 7 | 6 | 7 | 1 | 3 | 0 |
| 5 | 0 | 6 | 6 | 3 | 3 | 0 |

## Report

When step 5 of cycle 5 is complete, deliver the following:

(a) The six end masses, in chamber order 1 to 6.

(b) The six end stages (LARVAL or PUPAL), in chamber order 1 to 6.

(c) The complete list of stage changes, each given as (cycle, chamber, stage before, stage after).

(d) The cycles in which the line moulted.

(e) The final waste tally.

(f) A balance check showing that the starting total mass (the sum of the six starting masses) plus the sum of all feed charges across the five cycles equals the end total mass (the sum of the six end masses) plus the final waste tally.