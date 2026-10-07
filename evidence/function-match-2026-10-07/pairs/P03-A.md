# Constrained-State Solver: Operating Procedure

Purpose: this is the complete procedure for running the constrained-state solver for five iterations on the data below and delivering the end-of-run report.

## 1. Definitions

- **Component**: one entry of the state vector x = (x_1, x_2, x_3, x_4, x_5, x_6), indexed 1 to 6. Component 1 is first in sweep order and component 6 is last. The next component after component i is component i+1; the previous component is component i-1.
- **Component value x_i**: a whole number, never negative.
- **Box bound c_i**: the fixed upper bound of the box constraint on component i.
- **Upper threshold u_i and lower threshold d_i**: fixed for each component, with d_i < u_i <= c_i.
- **Active-set flag**: each component carries a flag that is either INACTIVE or ACTIVE. All six flags start INACTIVE.
- **Budget B**: one fixed number, 38, against which the 1-norm of x is checked.
- **Slack accumulator s**: one running total, starting at 0. Every amount that leaves the state vector is added to s.
- **Penalty step**: the halving operation in Step 5.
- **Iteration**: one pass through Steps 1 to 5. The run is exactly 5 iterations, numbered 1 to 5.
- **floor(...)**: round down to a whole number. Every division in this procedure is rounded down.

## 2. Data

Fixed parameters and starting vector, components 1 to 6:

| | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Box bound c_i | 10 | 8 | 12 | 6 | 9 | 7 |
| Upper threshold u_i | 7 | 6 | 9 | 5 | 7 | 5 |
| Lower threshold d_i | 3 | 2 | 4 | 2 | 3 | 2 |
| Starting value x_i | 3 | 6 | 6 | 2 | 2 | 1 |

Budget B = 38. Starting slack s = 0.

Input vectors b_k (row = iteration k, column = component i):

| Iteration | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 5 | 3 | 3 |
| 2 | 4 | 2 | 0 | 1 | 1 | 7 |
| 3 | 4 | 4 | 3 | 0 | 0 | 6 |
| 4 | 7 | 6 | 7 | 1 | 3 | 0 |
| 5 | 0 | 6 | 6 | 3 | 3 | 0 |

## 3. Procedure for one iteration

Run iterations 1, 2, 3, 4, 5 in order. Within iteration k, run Steps 1 to 5 in this order. Each step is finished for all six components before the next step begins.

**Step 1: Load input.** For each component i, add the entry of row k, column i of the input table to x_i. The box bound is not enforced in this step: after Step 1 a component may hold more than its box bound c_i.

**Step 2: Gauss-Seidel projection sweep.** Handle the components one at a time, in the order 1, 2, 3, 4, 5, 6. Each component is handled using its value as already updated by the earlier handling in this same sweep. When component i is handled:

- if x_i is more than c_i, compute the violation v = x_i - c_i, set x_i = c_i, and add v to component i+1; for component 6, add v to s instead;
- if x_i is at most c_i, do nothing.

Because the violation from component i is added to component i+1 before component i+1 is handled, it can push component i+1 above its own bound in the same sweep, and that violation then passes on to component i+2, and so on down to component 6. Do not compute the six violations simultaneously from the values before the sweep. Step 2 is the only step in which the box bound is enforced.

**Step 3: Active-set update.** For each component, use its value after Step 2:

- if the flag is INACTIVE and x_i is at least u_i, the flag becomes ACTIVE;
- if the flag is ACTIVE and x_i is at most d_i, the flag becomes INACTIVE;
- in every other case the flag does not change. In particular, a component with d_i < x_i < u_i keeps whichever flag it already has.

A flag changes at most once per iteration. Record every change as (iteration, component, flag before, flag after).

**Step 4: Jacobi transfer step.** First, compute a transfer amount t_i for all six components from their values at the start of this step, using the flags as set in Step 3:

- INACTIVE component: t_i = floor(x_i / 4);
- ACTIVE component: t_i = floor(x_i / 2).

Compute all six amounts before changing any value. Then apply all six at once:

- every component: x_i decreases by its own t_i;
- INACTIVE component: t_i is added to s;
- ACTIVE component i, for i from 2 to 6: t_i is added to component i-1;
- ACTIVE component 1: t_1 is added to s.

The box bound is not enforced in this step. A component may hold more than its box bound after receiving a transfer from component i+1. That excess is corrected only by Step 2 of the next iteration, and is never corrected if it arises in iteration 5.

**Step 5: Penalty step.** Compute the 1-norm of x, which is x_1 + x_2 + x_3 + x_4 + x_5 + x_6. If the 1-norm is strictly more than B (that is, more than 38), every x_i becomes floor(x_i / 2), every amount removed (x_i minus floor(x_i / 2)) is added to s, and you record that the penalty step fired in iteration k. If the 1-norm is 38 or less, nothing happens.

Nothing else changes x, the flags, or s at any time, including between steps and between iterations.

## Report

At the end of Step 5 of iteration 5, deliver:

(a) the six end component values x_1 to x_6, in component order 1 to 6;

(b) the six end active-set flags (INACTIVE or ACTIVE), in component order 1 to 6;

(c) every flag change recorded in Step 3, as (iteration, component, flag before, flag after), across all five iterations;

(d) the list of iterations in which the penalty step fired;

(e) the final value of the slack accumulator s;

(f) the balance check: (sum of the six starting values) + (sum of all thirty input table entries) must equal (sum of the six end component values) + s.
