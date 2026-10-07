The stack is six retrieval buffers: tier 1 sits next to the LLM, tier 6 furthest out. Everything you track is chunks held.

Per tier, 1 to 6:
Budget: 10, 8, 12, 6, 9, 7
HOT mark: 7, 6, 9, 5, 7, 5
COLD mark: 3, 2, 4, 2, 3, 2
Holding at start: 3, 6, 6, 2, 2, 1
Context ceiling for the whole stack: 38. Every tier starts COLD.

New chunks landing each cycle (tiers 1 to 6):
Cycle 1: 0, 6, 3, 5, 3, 3
Cycle 2: 4, 2, 0, 1, 1, 7
Cycle 3: 4, 4, 3, 0, 0, 6
Cycle 4: 7, 6, 7, 1, 3, 0
Cycle 5: 0, 6, 6, 3, 3, 0

A cycle is five passes, each finished across the whole stack before the next starts.

1. Load. Add the cycle's new chunks. No trimming yet; a tier can sit over budget here.
2. Evict. Walk tier 1 through 6. Anything over budget moves out to the next tier, so it can push that tier over before you reach it. Overflow from tier 6 is dropped.
3. Flag. A COLD tier at or above its HOT mark goes HOT; a HOT tier at or below its COLD mark goes COLD. Anywhere between the marks, it keeps its flag. Log every flip.
4. Rebalance. Off the post-flag counts, a COLD tier compacts a quarter of its chunks (round down), dropped; a HOT tier promotes half (round down) into the tier one closer to the LLM, and tier 1's promotion is dropped. Work out all six amounts before moving anything. A promotion can leave a tier over budget; that waits for next cycle's evict, and after cycle 5 it just stands.
5. Reset check. If the stack totals more than 38, context reset: every tier halves (round down), removed chunks dropped. Exactly 38 is fine.

Keep one running drop count covering tier-6 evictions, compactions, tier-1 promotions and resets.

Report. At the end of cycle 5 hand in: holdings in tiers 1 to 6, in order; the state of each tier (COLD or HOT); every flip as (cycle, tier, before, after); the cycles in which a reset fired; the dropped tally; and a balance line: chunks at start plus everything loaded, against chunks held plus dropped.