Six teams: team 1 takes new work in, team 6 faces the customer. We watch open tickets per team.

Per team, 1 to 6:
WIP limit: 10, 8, 12, 6, 9, 7
Escalate at: 7, 6, 9, 5, 7, 5
Stand down at: 3, 2, 4, 2, 3, 2
Open at start: 3, 6, 6, 2, 2, 1

Everyone starts ROUTINE. The board target is 38 open tickets.

Each cycle runs five steps, each finished board-wide before the next.

1. New tickets land (per cycle, teams 1 to 6):
C1: 0, 6, 3, 5, 3, 3
C2: 4, 2, 0, 1, 1, 7
C3: 4, 4, 3, 0, 0, 6
C4: 7, 6, 7, 1, 3, 0
C5: 0, 6, 6, 3, 3, 0
Limits don't bite yet.

2. Walk the line, team 1 to team 6. A team's excess goes to the next team down, counting when you reach them. Team 6's overflow is closed-without-action.

3. Status check. A ROUTINE team at or above its escalation mark goes ESCALATED; an ESCALATED team at or below its stand-down mark goes back to ROUTINE. In between, status holds. Log every flip.

4. Work the queues off one snapshot. A ROUTINE team closes a quarter of its tickets, rounded down. An ESCALATED team bounces half, rounded down, to the team upstream; team 1 has nobody upstream, so its bounce is closed. Bounced tickets can leave a team over its limit until the next walk; after cycle 5 they stay.

5. Backlog cut. Total the board. Strictly over 38, every team keeps half its tickets, rounded down, and the rest are closed-without-action. At 38 or under, leave it.

Every closure, by any route, goes on one closed tally, from zero.

Report (end of cycle 5)
Open tickets, teams 1 to 6: 6, 10, 9, 7, 4, 2.
Status: ESCALATED, ESCALATED, ESCALATED, ESCALATED, ESCALATED, ROUTINE.
Status changes (cycle, team, before, after): (1, 2, ROUTINE, ESCALATED), (1, 3, ROUTINE, ESCALATED), (1, 4, ROUTINE, ESCALATED), (1, 5, ROUTINE, ESCALATED), (2, 1, ROUTINE, ESCALATED), (2, 3, ESCALATED, ROUTINE), (2, 5, ESCALATED, ROUTINE), (2, 6, ROUTINE, ESCALATED), (3, 3, ROUTINE, ESCALATED), (3, 4, ESCALATED, ROUTINE), (4, 4, ROUTINE, ESCALATED), (4, 5, ROUTINE, ESCALATED), (5, 6, ESCALATED, ROUTINE).
Backlog cut fired: cycles 1 and 4.
Closed tally: 76.
Balance: 20 at start + 94 arrived = 114 = 38 open + 76 closed.