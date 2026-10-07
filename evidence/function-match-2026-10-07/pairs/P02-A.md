# Charge-Stage Chain: Desk Operating Procedure

Purpose: run the six-stage charge chain through five charge cycles from the stated starting charges, and report the end condition of every stage.

## Definitions

- **Stage**: one of six charge-storage stages in a chain, numbered 1 to 6. Stage 1 is at the source end. Stage 6 is at the load end. For stage n, the next stage down the chain is stage n+1 and the previous stage is stage n-1.
- **Charge**: the units of stored charge a stage holds. It is always a whole number and is never negative.
- **Rated charge**: a stage's fixed rated maximum. The procedure enforces it only in the breakdown shunt step (Step 2).
- **Comparator**: each stage has a comparator with hysteresis (a Schmitt trigger). It has an upper mark and a lower mark. The lower mark is below the upper mark, and the upper mark is at most the rated charge. The comparator is in one of two states, ASSERTED or CLEAR. All six comparators start CLEAR.
- **Breakdown shunt**: the path that passes a stage's excess charge to the next stage down the chain.
- **Return diode**: the path that feeds charge from a stage back to the previous stage.
- **Ground**: charge sent to ground leaves the chain for good.
- **Ground total**: the running total of all charge sent to ground, from any step. It starts at 0.
- **Chain limit**: 38 units of charge, summed over all six stages.
- **Breaker trip**: the event in Step 5 that halves every stage's charge.
- **Cycle**: one complete pass through Steps 1 to 5. There are exactly five cycles, numbered 1 to 5.
- **Rounded down**: whenever a quarter or a half is taken, keep the whole-number part and discard any fraction.

## Stage ratings and starting charge

| Stage | Rated charge | Upper mark | Lower mark | Starting charge |
|---|---|---|---|---|
| 1 | 10 | 7 | 3 | 3 |
| 2 | 8 | 6 | 2 | 6 |
| 3 | 12 | 9 | 4 | 6 |
| 4 | 6 | 5 | 2 | 2 |
| 5 | 9 | 7 | 3 | 2 |
| 6 | 7 | 5 | 2 | 1 |

Chain limit: 38. Starting ground total: 0. Starting state of every stage: CLEAR.

## Procedure for one cycle

Carry out the five steps in the order given. Finish each step for all six stages before you start the next step.

**Step 1: Charge input.** Add that cycle's input for each stage, taken from the Charge input table, to the stage's charge. Rated charge is not enforced in this step. After this step a stage may hold more than its rated charge.

**Step 2: Breakdown shunt.** Take the stages one at a time, strictly in the order 1, 2, 3, 4, 5, 6. For the stage you are working on:
- If its charge is more than its rated charge, the excess (charge minus rated charge) passes through the breakdown shunt and is added to the next stage down the chain (stage n+1). The stage's charge then becomes exactly its rated charge.
- If its charge is equal to or less than its rated charge, nothing happens.
- Excess from stage 6 goes to ground. Add it to the ground total.

Because you work in order, any excess passed from stage 1 is already in stage 2 when you reach stage 2. The same holds for each later stage. One stage's excess can therefore push the next stage over its rated charge within this same step, and that can continue down the chain.

**Step 3: Comparator check.** For each stage, read its charge as it stands after Step 2.
- If the stage is CLEAR and its charge is at least its upper mark, it becomes ASSERTED.
- If the stage is ASSERTED and its charge is at most its lower mark, it becomes CLEAR.
- In every other case the state does not change. A stage whose charge is more than its lower mark and less than its upper mark keeps the state it already had.

Log every state change as (cycle, stage, state before, state after). A stage changes state at most once per cycle.

**Step 4: Discharge.** First work out every stage's discharge amount from the charge it holds at the start of this step, using its state after Step 3:
- CLEAR stage: one quarter of its charge, rounded down.
- ASSERTED stage: one half of its charge, rounded down.

Work out all six amounts before you change any stage's charge. Then apply all six together:
- Reduce every stage's charge by its own discharge amount.
- A CLEAR stage's amount leaks to ground. Add it to the ground total.
- An ASSERTED stage's amount is fed back through the return diode and added to the charge of the previous stage (stage n-1). If stage 1 is ASSERTED, its amount goes to ground instead and is added to the ground total.

Rated charge is not enforced in this step. After receiving feedback through the return diode, a stage may hold more than its rated charge. That excess is handled only at the breakdown shunt step of the next cycle. If it happens in cycle 5, it is never handled and stays in the end figures.

**Step 5: Breaker trip check.** Add up the charge of all six stages.
- If the total is more than 38 (strictly greater), the breaker trips. Every stage's charge becomes one half of its charge, rounded down. The charge removed from each stage goes to ground and is added to the ground total. Log that the breaker tripped in this cycle.
- If the total is 38 or less, the breaker does not trip and nothing changes.

Then start the next cycle at Step 1. Stop after Step 5 of cycle 5.

## Charge input table

Units of charge added in Step 1, by cycle (rows) and stage (columns).

| Cycle | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Stage 5 | Stage 6 |
|---|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 5 | 3 | 3 |
| 2 | 4 | 2 | 0 | 1 | 1 | 7 |
| 3 | 4 | 4 | 3 | 0 | 0 | 6 |
| 4 | 7 | 6 | 7 | 1 | 3 | 0 |
| 5 | 0 | 6 | 6 | 3 | 3 | 0 |

## Report

At the end of cycle 5, deliver the following:

(a) The six end charges, in stage order 1 to 6.

(b) The six end comparator states (ASSERTED or CLEAR), in stage order 1 to 6.

(c) Every state change logged in Step 3 across all five cycles, each given as (cycle, stage, state before, state after), in the order they occurred.

(d) The cycles in which the breaker tripped. If it never tripped, say so.

(e) The ground total.

(f) A balance check. Show that the sum of the six starting charges plus the sum of all thirty charge inputs equals the sum of the six end charges plus the ground total. Give all four figures and confirm that the two sides are equal.