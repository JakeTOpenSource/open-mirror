Six teams, 1 at the front, 6 at the customer. Each holds open tickets against its WIP limit. All start ROUTINE; closed tally starts at 0.

Teams 1 to 6:
WIP limit: 10, 8, 12, 6, 9, 7
Upper mark: 7, 6, 9, 5, 7, 5
Lower mark: 3, 2, 4, 2, 3, 2
Opening tickets: 3, 6, 6, 2, 2, 1
Line target: 38

New tickets, teams 1 to 6:
Cycle 1: 0, 6, 3, 5, 3, 3
Cycle 2: 4, 2, 0, 1, 1, 7
Cycle 3: 4, 4, 3, 0, 0, 6
Cycle 4: 7, 6, 7, 1, 3, 0
Cycle 5: 0, 6, 6, 3, 3, 0

Five cycles, five steps each, in this order; each step finishes for all teams before the next.

1. Arrivals. Teams add their new tickets. Nobody refuses work; teams can sit over limit.

2. Overflow. Team by team, 1 through 6: anything over the limit goes to the next team downstream, leaving exactly the limit. Excess arrives before the receiving team is handled, so it can cascade. Team 6's excess is closed-without-action and tallied.

3. Status check, on post-overflow counts. ROUTINE at or above the upper mark goes ESCALATED. ESCALATED at or below the lower mark goes ROUTINE. Between the marks, status holds. Status changes only here, at most once per team per cycle. Log each as (cycle, team, before, after).

4. Closing. Figure every amount from current counts before changing any: ROUTINE closes a quarter of its tickets, tallied; ESCALATED closes nothing and bounces half back to the team upstream; both round down. Apply all six at once. Bounced tickets join the upstream count; team 1's bounce is closed-without-action and tallied. No limits here: a team can end over its limit until next cycle's overflow; after cycle 5 it stays over.

5. Backlog cut. Total all six counts. Above 38, not at 38, every team is halved, rounding down; removed tickets are closed-without-action and tallied; note the cycle. This runs every cycle; 38 is only a trigger.

Report. After cycle 5 hand in: the six ticket counts, teams 1 to 6; the six statuses, same order; every status change as (cycle, team, before, after); the cycles the backlog cut fired; the closed tally, all routes; and the balance check: opening tickets plus all new tickets equals final counts plus tally.
