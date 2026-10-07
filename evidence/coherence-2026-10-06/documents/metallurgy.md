# Crucible Cascade: Desk Operating Document

Purpose: run the six-crucible cascade through five cycles using the data below, then deliver the Report.

## Definitions

- **Crucibles.** The cascade has six crucibles, numbered 1 to 6. Crucible 1 is at the charging end. Crucible 6 is at the tapping end. The "next crucible" is the one numbered one higher, towards the tapping end. The "previous crucible" is the one numbered one lower, towards the charging end.
- **Melt.** The contents of a crucible, counted in units of melt. Melt is always a whole number and is never negative.
- **Working volume.** Each crucible's fixed capacity.
- **Upper mark and lower mark.** Two fixed figures for each crucible, used only in Step 3.
- **State.** Each crucible is always either BASE or SUPERHEATED. All six crucibles start the run BASE.
- **Cascade melt limit.** 38 units of melt. It applies to the combined melt of all six crucibles and is used only in Step 5.
- **Slag total.** A running count of all melt sent to slag, whether it goes over the end of the cascade into the slag pit or is drawn off to slag. It starts at 0.
- **Emergency tap.** The halving of every crucible described in Step 5.
- **Rounding.** Whenever this document says to take a quarter or a half, divide and round down to a whole number by dropping any fraction.

## Crucible data

| | Crucible 1 | Crucible 2 | Crucible 3 | Crucible 4 | Crucible 5 | Crucible 6 |
|---|---|---|---|---|---|---|
| Working volume | 10 | 8 | 12 | 6 | 9 | 7 |
| Upper mark | 7 | 6 | 9 | 5 | 7 | 5 |
| Lower mark | 3 | 2 | 4 | 2 | 3 | 2 |
| Starting melt | 3 | 6 | 6 | 2 | 2 | 1 |

Cascade melt limit: 38. Starting state: BASE for all six crucibles. Slag total at start: 0.

## Procedure for one cycle

The run is exactly five cycles, numbered 1 to 5. Each cycle has five steps, always in the order below. Finish each step for all six crucibles before you start the next step.

**Step 1: Charge.** Add to each crucible's melt the charge shown for that crucible in this cycle's row of the charge table. Working volume is not enforced in this step. After charging, a crucible may hold more melt than its working volume.

**Step 2: Overflow.** Handle the crucibles one at a time, in the order 1, 2, 3, 4, 5, 6. For the crucible you are handling:
- If its melt is more than its working volume, the excess (melt minus working volume) runs down the launder into the next crucible and is added to that crucible's melt. This crucible's melt then becomes exactly its working volume.
- If its melt is equal to or less than its working volume, nothing happens to it.
- Excess from crucible 6 goes to the slag pit and is added to the slag total.

Because you handle the crucibles in order, overflow from crucible 1 is already in crucible 2 before you handle crucible 2. The same holds for every later crucible. One crucible's overflow can push the next crucible over its working volume in this same step, and that can carry on down the cascade.

**Step 3: State check.** For each crucible, read its melt as it stands after Step 2.
- If the crucible is BASE and its melt is at least its upper mark, it becomes SUPERHEATED.
- If the crucible is SUPERHEATED and its melt is at most its lower mark, it becomes BASE.
- In every other case the state stays the same. A crucible whose melt is above its lower mark and below its upper mark keeps the state it already had.

Log every change as (cycle, crucible, state before, state after). A crucible changes state at most once per cycle.

**Step 4: Draw-off.** First, work out a draw-off amount for every crucible, using each crucible's melt at the start of this step and its state after Step 3:
- A BASE crucible draws off one quarter of its melt, rounded down.
- A SUPERHEATED crucible draws off one half of its melt, rounded down.

Work out all six amounts before you change any melt. Then apply all six at once:
- Every crucible's melt goes down by its own draw-off amount.
- A BASE crucible's draw-off goes to slag and is added to the slag total.
- A SUPERHEATED crucible's draw-off runs up the return launder into the previous crucible and is added to that crucible's melt. If crucible 1 is SUPERHEATED, its draw-off goes to slag and is added to the slag total.

Working volume is not enforced in this step. A crucible that receives melt from the return launder may hold more than its working volume. Between this step and the next cycle's Step 2, a crucible can stay above its working volume. That excess is dealt with only at Step 2 of the next cycle. If it arises in cycle 5, it is never dealt with.

**Step 5: Emergency tap check.** Add up the melt in all six crucibles.
- If the total is more than 38 (strictly greater), fire the emergency tap. Every crucible's melt becomes half of its melt, rounded down. All melt removed goes to slag and is added to the slag total. Log this cycle number as an emergency tap cycle.
- If the total is 38 or less, nothing happens.

Once Step 5 is finished, the cycle is complete. Start the next cycle at Step 1. Stop after cycle 5.

## Charge table

Units of melt charged into each crucible at Step 1 of each cycle:

| Cycle | Crucible 1 | Crucible 2 | Crucible 3 | Crucible 4 | Crucible 5 | Crucible 6 |
|---|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 5 | 3 | 3 |
| 2 | 4 | 2 | 0 | 1 | 1 | 7 |
| 3 | 4 | 4 | 3 | 0 | 0 | 6 |
| 4 | 7 | 6 | 7 | 1 | 3 | 0 |
| 5 | 0 | 6 | 6 | 3 | 3 | 0 |

## Report

When Step 5 of cycle 5 is finished, deliver the following:

(a) The end melt of each crucible, in order from crucible 1 to crucible 6.

(b) The end state of each crucible (BASE or SUPERHEATED), in order from crucible 1 to crucible 6.

(c) Every state change logged in Step 3 across all five cycles, each given as (cycle, crucible, state before, state after).

(d) The cycles in which the emergency tap fired.

(e) The slag total.

(f) A balance check. Add the six starting melts to the sum of every charge in the charge table. This must equal the six end melts added together plus the slag total. Show both sides of the check.