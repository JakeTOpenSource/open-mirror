Welcome to the desk. The state is x, six nonnegative integer components, positions 1 to 6, starting at x0 = (3, 6, 6, 2, 2, 1). Box bounds c = (10, 8, 12, 6, 9, 7). Activation thresholds u = (7, 6, 9, 5, 7, 5); deactivation thresholds d = (3, 2, 4, 2, 3, 2). Budget on the 1-norm: 38. Slack s starts at 0, and every component starts INACTIVE.

A run is five cycles. Each cycle is five steps, and each step finishes across the whole vector before the next one starts.

1. Load. Add the cycle's row of b to x. Bounds are not enforced here. Rows, cycles 1 to 5: (0,6,3,5,3,3), (4,2,0,1,1,7), (4,4,3,0,0,6), (7,6,7,1,3,0), (0,6,6,3,3,0).

2. Projection sweep, Gauss-Seidel, 1 through 6. Clip x_i to c_i and push the violation into x_{i+1} before you visit it, so overflow cascades down the vector. Component 6's violation goes to s.

3. Active-set update on the projected x. INACTIVE goes ACTIVE at x_i >= u_i; ACTIVE drops back to INACTIVE at x_i <= d_i. Anywhere in between, the flag holds. Log every flip as (cycle, position, before, after).

4. Jacobi shed. Compute all six amounts from the same x before anything moves. An INACTIVE component sheds floor(x_i/4) to s. An ACTIVE component moves floor(x_i/2) up to x_{i-1}; component 1 sends its share to s. No projection after this step: a component can sit over its bound until the next sweep, and after cycle 5 it simply stays there.

5. Penalty. If the 1-norm is strictly above 38, halve every component with floor and book what came off to s. Note the cycle.

Report. At the end of cycle 5 hand in: the vector x, components 1 to 6, in order; each component's flag (INACTIVE or ACTIVE); every flip as (cycle, component, before, after); the cycles in which the penalty fired; the slack s; and a balance line: the starting 1-norm plus everything loaded, against the final 1-norm plus s.