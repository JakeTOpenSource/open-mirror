The solver carries an integer state vector x, components 1 to 6, never negative. Each component has a box ceiling c, upper threshold u, lower threshold d (d < u ≤ c) and an active-set flag, INACTIVE or ACTIVE. All start INACTIVE; slack starts at 0.

c: 10, 8, 12, 6, 9, 7
u: 7, 6, 9, 5, 7, 5
d: 3, 2, 4, 2, 3, 2
Starting x: 3, 6, 6, 2, 2, 1
1-norm budget: 38

A run is 5 cycles of five steps, always in this order. Each step finishes on all six components before the next starts.

1. Load. Add the cycle's input row to x, position by position. No box enforcement.

Cycle 1: 0, 6, 3, 5, 3, 3
Cycle 2: 4, 2, 0, 1, 1, 7
Cycle 3: 4, 4, 3, 0, 0, 6
Cycle 4: 7, 6, 7, 1, 3, 0
Cycle 5: 0, 6, 6, 3, 3, 0

2. Projection sweep. Gauss-Seidel, not Jacobi: components 1 to 6 in order. If x_i exceeds c_i, set it to c_i and add the violation to x_(i+1) before handling i+1, so violations cascade; nothing is discarded. Component 6's violation goes to slack. Only the ceiling is projected.

3. Active-set update, on the swept x. INACTIVE with x_i ≥ u_i goes ACTIVE; ACTIVE with x_i ≤ d_i goes INACTIVE; otherwise the flag holds. Thresholds drive the flag, not whether the ceiling binds. Flags change only here, at most once per cycle. Log each change as (cycle, position, before, after).

4. Jacobi transfer. Compute all six amounts from the current x before moving anything: INACTIVE floor(x_i/4), ACTIVE floor(x_i/2). Apply together; each component drops by its own amount. INACTIVE amounts go to slack. ACTIVE amounts go to component i−1; component 1's goes to slack. No box enforcement: a component can sit above its ceiling until next cycle's sweep, or permanently after cycle 5.

5. Penalty reset. If the 1-norm is strictly above 38, floor-halve every component, everything removed to slack, and log the cycle. At 38 or below, nothing.

Report. After cycle 5 hand in: the six end quantities, positions 1 to 6; the six end flags, positions 1 to 6; every flag change as (cycle, position, before, after); the cycles where the penalty reset fired; the slack accumulator; and the balance check: starting sum plus total input equals end sum plus slack.
