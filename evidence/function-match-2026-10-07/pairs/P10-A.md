# Pour Line Operating Sheet

**Purpose.** This sheet is the complete procedure for running the six-form pour line through five cycles and reporting its end condition.

## Definitions

- **Forms.** Six pour forms sit along the chute, numbered 1 to 6. Form 1 is nearest the hopper; form 6 is at the end of the chute. "Down the chute" means toward form 6 (from form n to form n+1). "Up the chute" means toward the hopper (from form n to form n-1).
- **Mix.** The contents of each form are counted in units of mix. Amounts are always whole numbers, and a form never holds a negative amount.
- **Volume.** Each form has a fixed volume. It is the most mix the form keeps after the overtop step.
- **Upper mark and lower mark.** Each form has an upper mark and a lower mark. The lower mark is always below the upper mark, and the upper mark is never above the form's volume.
- **GREEN and HOT.** Every form is either GREEN or HOT at all times. All six forms start the run GREEN. A HOT form can go back to GREEN.
- **Waste pit and waste tally.** Mix that leaves the line goes to the waste pit. The waste tally is the running total of all mix sent to the waste pit. It starts at 0.
- **Line limit.** 38 units of mix, counted across all six forms together.
- **Washout.** The halving of every form described in Step 5.
- **Rounding.** Wherever this sheet says "rounded down", drop any fraction and keep the whole number below (for example, 7 halved is 3; 11 quartered is 2).

## Form data

| | Form 1 | Form 2 | Form 3 | Form 4 | Form 5 | Form 6 |
|---|---|---|---|---|---|---|
| Volume | 10 | 8 | 12 | 6 | 9 | 7 |
| Upper mark | 7 | 6 | 9 | 5 | 7 | 5 |
| Lower mark | 3 | 2 | 4 | 2 | 3 | 2 |
| Starting mix | 3 | 6 | 6 | 2 | 2 | 1 |

Line limit: 38. Waste tally at start: 0. All forms start GREEN.

## Procedure for one cycle

Run exactly five cycles, numbered 1 to 5. Each cycle has five steps, always in the order below. Finish each step for all six forms before starting the next step. Mix moves only as these steps say.

**Step 1: Charge.** Add to each form the units of mix shown for this cycle and that form in the charge table. Volume is not enforced in this step: after charging, a form may hold more than its volume.

**Step 2: Overtop.** Handle the forms one at a time, in the order 1, 2, 3, 4, 5, 6. When you handle a form:
- If it holds more than its volume, the overtop (contents minus volume) runs down the chute and is added to the next form (form n+1), and the form is left holding exactly its volume.
- Overtop from form 6 goes to the waste pit; add it to the waste tally.
- If the form holds its volume or less, nothing happens to it in this step.

Because the forms are handled in order, overtop from form 1 lands in form 2 before form 2 is handled. One form's overtop can therefore push the next form over its volume in this same step, and so on down to form 6.

**Step 3: Status check.** For each form, read its contents now, after Step 2.
- A GREEN form holding at least its upper mark becomes HOT.
- A HOT form holding at most its lower mark becomes GREEN.
- In every other case the status does not change. In particular, a form holding more than its lower mark and less than its upper mark keeps whatever status it had.

Record every change as (cycle, form, status before, status after). A form changes status at most once per cycle.

**Step 4: Settle.** First work out every form's settle amount from its contents at the start of this step:
- a GREEN form's settle amount is one quarter of its contents, rounded down;
- a HOT form's settle amount is one half of its contents, rounded down.

Work out all six amounts before changing any form. Then apply all six together:
- every form loses its own settle amount;
- a GREEN form's settle amount evaporates; add it to the waste tally;
- a HOT form's settle amount bleeds back up the chute and is added to the previous form (form n-1). If form 1 is HOT, its bleed goes to the waste pit; add it to the waste tally.

A form may lose its own amount and receive bleed from the form after it in the same step. Volume is not enforced in this step: a form that receives bleed may hold more than its volume afterward. That excess is dealt with only at the next cycle's Step 2. If it happens in cycle 5, it is never dealt with and stays in the form.

**Step 5: Washout check.** Add up the contents of all six forms.
- If the total is more than 38, a washout fires: every form's contents becomes half its contents, rounded down. Every unit removed goes to the waste pit; add it to the waste tally. Record that a washout fired in this cycle.
- If the total is 38 or less, nothing happens.

## Charge table

Units of mix added to each form in Step 1. Rows are cycles 1 to 5; columns are forms 1 to 6.

| Cycle | Form 1 | Form 2 | Form 3 | Form 4 | Form 5 | Form 6 |
|---|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 5 | 3 | 3 |
| 2 | 4 | 2 | 0 | 1 | 1 | 7 |
| 3 | 4 | 4 | 3 | 0 | 0 | 6 |
| 4 | 7 | 6 | 7 | 1 | 3 | 0 |
| 5 | 0 | 6 | 6 | 3 | 3 | 0 |

## Report

At the end of cycle 5 (after its Step 5), deliver:

(a) The mix in each form at the end, in form order 1 to 6.

(b) The status of each form at the end (GREEN or HOT), in form order 1 to 6.

(c) Every status change from all five cycles, each as (cycle, form, status before, status after).

(d) The cycles in which a washout fired.

(e) The final waste tally.

(f) The balance check: the starting mix total (all six forms) plus every unit in the charge table must equal the end mix total (all six forms) plus the waste tally.
