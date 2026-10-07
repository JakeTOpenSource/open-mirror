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
Hand in: open tickets for teams 1 to 6, in order; each team's status (ROUTINE or ESCALATED); every status change as (cycle, team, before, after); the cycles in which the backlog cut fired; the closed tally; and a balance line: tickets at start plus everything that arrived, against tickets open plus tickets closed.