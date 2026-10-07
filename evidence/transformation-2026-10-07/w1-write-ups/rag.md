Six retrieval buffers in a stack, positions 1 to 6: tier 1 nearest the LLM, tier 6 furthest. Counts are whole chunks. Every tier starts COLD.

Tiers 1 to 6:
Chunk budget: 10, 8, 12, 6, 9, 7
Upper mark: 7, 6, 9, 5, 7, 5
Lower mark: 3, 2, 4, 2, 3, 2
Starting chunks: 3, 6, 6, 2, 2, 1
Stack ceiling: 38.

A run is five cycles, five steps each, in this order. Each step finishes on every tier before the next starts.

1. Ingest. Add that cycle's new chunks, tiers 1 to 6. Budgets aren't enforced here.
Cycle 1: 0, 6, 3, 5, 3, 3
Cycle 2: 4, 2, 0, 1, 1, 7
Cycle 3: 4, 4, 3, 0, 0, 6
Cycle 4: 7, 6, 7, 1, 3, 0
Cycle 5: 0, 6, 6, 3, 3, 0

2. Eviction. Walk tiers 1 to 6. Over-budget chunks move to the next tier out; the tier sits exactly at budget. Evicted chunks arrive before the receiving tier is checked, so overflow cascades. Tier 6's overflow is dropped.

3. State check, on post-eviction counts. A COLD tier at or above its upper mark goes HOT. A HOT tier at or below its lower mark goes COLD. Between the marks, no change. At most one flip per tier per cycle. Log every flip as (cycle, position, before, after).

4. Compaction and promotion. Compute all six amounts from current counts first, then apply together. A COLD tier compacts away a quarter, rounded down; those are dropped. A HOT tier moves half, rounded down, out of itself into the tier one closer to the LLM; tier 1's promoted chunks are dropped. No budget check: a tier pushed over budget stays over until next cycle's eviction or, after cycle 5, for good.

5. Context reset. If the six-tier total is strictly above 38, halve every tier, rounded down, dropping what's removed, and note the cycle. At 38 or below, nothing.

Promotion here isn't hit-driven. HOT means only that the tier crossed its upper mark.

Report. After cycle 5, hand in: chunks held, tiers 1 to 6 in order; each tier's state, same order; every flip as (cycle, position, before, after); the cycles where the context reset fired; the loss tally, every chunk dropped; and the balance check: starting chunks plus all ingested chunks must equal end chunks plus the loss tally.
