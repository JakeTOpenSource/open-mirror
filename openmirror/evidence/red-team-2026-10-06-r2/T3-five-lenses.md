# T3 (round 2, v1.4.1, Opus) — drive-by pull requests, five user-named pictures

**Case given:** Open Mirror through immune system, supply chain, jazz improvisation, plate tectonics, and parliamentary procedure: "Our open-source project gets lots of drive-by pull requests that each look fine but together the codebase is getting harder to maintain."

**Replicator's final message, verbatim:**

---

# Open Mirror v1.4.1: drive-by pull requests

**Mode:** Filter mode, the default. The person did not ask for an explanation for a newcomer, so step 6 asks whether each picture changed a decision.

---

## 1. Say it plainly

An open-source project receives many pull requests from "drive-by" contributors. In open source this is the usual term for people who send a change and then do not stay with the project. When each pull request is looked at by itself, it looks acceptable. Over time, with many of them merged, the codebase is becoming harder to maintain.

What the person said, and how sure they are:
- **Stated as observation, with no hedge:** there are many drive-by pull requests; each looks fine; the codebase is getting harder to maintain.
- **Stated as their explanation:** the difficulty comes from these pull requests "together", meaning the combined effect of individually acceptable changes. They state this link as fact, but they don't show it or say how they know.
- **Not stated:** what specifically makes the code harder to maintain; how review is done or what it checks against; whether the project has written conventions or architecture rules; whether any merged change later needed maintainer work; how big the project is or how many maintainers it has.
- **"Look fine":** they chose the word "look", not "are". I keep it as said.

There is no embedded comparison to pull out. I treat "drive-by" as a term of art, not as a picture (see notes). There are no instructions aimed at me.

Does the restatement answer the question? No question is stated. The implied question is why individually acceptable changes add up to a maintenance problem, or what to do about it. The restatement doesn't answer either, so the run continues.

## 2. Pictures

The person named five. Per the rule I use the first three in the order given:
1. Immune system
2. Supply chain
3. Jazz improvisation

**Not run:** plate tectonics, parliamentary procedure.

## 3. Map each picture

**Picture 1: Immune system**
- Matches:
  - Incoming pull requests ↔ material entering the body.
  - Code review ↔ immune recognition, where each item is checked as it arrives.
  - "Looks fine" ↔ the item passes the check and is tolerated.
  - Maintainability ↔ overall health.
- The way they match: a screening process that judges items one at a time against a per-item test. Damage that comes only from the total of tolerated items isn't what that test looks at.
- Question it makes easier to ask: does anything in the project evaluate the accumulated whole, rather than each pull request as it arrives?

**Picture 2: Supply chain**
- Matches:
  - Drive-by contributors ↔ many small, one-off suppliers.
  - Pull requests ↔ delivered parts.
  - Maintainers ↔ the integrator who owns the finished product for its whole life.
  - Maintenance difficulty ↔ the ongoing cost of supporting parts after delivery.
- The way they match: the supplier delivers and leaves. Acceptance inspection asks whether the part works on arrival. The cost of keeping it working falls on the integrator later, and that cost isn't the same thing as the acceptance test.
- Question it makes easier to ask: when a drive-by pull request is merged, who maintains that code afterwards, and was that ongoing cost weighed at merge time or only "does it look fine now"?

**Picture 3: Jazz improvisation**
- Matches:
  - Each pull request ↔ a phrase played by a musician sitting in.
  - The codebase ↔ the performance.
  - The project's intended structure ↔ the tune's form and chord changes.
  - Maintainers ↔ the bandleader or rhythm section holding the form.
- The way they match: phrases that are fine on their own sound coherent together only if the players share and follow a common structure. Someone sitting in for one tune may not know the band's habits.
- Question it makes easier to ask: "looks fine" judged against what? Is there a stated structure or set of conventions that each pull request is checked against?

A shared shape is not a shared mechanism. None of these pictures shows how the project works.

## 4. Where each picture breaks

**Immune system**
- **Adversarial framing.** The picture brings in hostility: contributors as invaders, maintainers as defenders. Nothing in the topic says the pull requests are harmful in intent or that contributors are a threat. That idea comes from the picture, not the topic.
- **Learning and memory.** Immune systems learn from what they meet. Nothing stated says the project's review does or doesn't learn.
- **Its core idea is already in the topic.** The topic already says "each look fine but together", so the per-item versus aggregate point isn't new.
- Verdict: it doesn't *only* work by adding hostility. The per-item screening match stands without it. **Not marked misleading.**

**Supply chain**
- **Commerce and choice.** Supply chains involve ordering, contracts, payment and supplier selection. Drive-by pull requests are unsolicited and unpaid, and maintainers don't choose who sends them. The picture brings in "the project ordered this", which the topic doesn't support.
- **Uniformity.** It tempts a reading that the trouble is mixed parts that don't fit together. The topic doesn't say what makes the code harder to maintain.
- **What holds.** The core match, author leaves and upkeep falls on the recipient, rests on "drive-by", which the topic supplies.
- Verdict: **not marked misleading.**

**Jazz improvisation**
- **Nothing persists.** A performance is real-time and gone a moment later. A bad phrase leaves no maintenance burden. The topic's central feature, a codebase that gets *harder over time* because changes persist and pile up, has nothing to match it in jazz. The picture can't carry the accumulation back.
- **It assumes a form exists.** The topic doesn't say whether the project has a stated architecture or conventions. It also brings in the idea that the problem is clashing (incoherence), not volume or per-change cost.
- **Why it isn't misleading.** The incoherence reading is one reading of "together", not a contradiction. And the question "fine against what?" stands even if no stated structure exists.
- Verdict: it doesn't only work by an added fact. **Not marked misleading.**

## 5. What survives, in plain words

- **Immune system:** Each pull request is judged on its own, and the problem shows up only in the combined result. The topic doesn't say whether anything in the project judges the combined result.
- **Supply chain:** Because drive-by contributors don't stay, maintainers carry the ongoing cost of each merged change. Whether a change looks fine at merge time is a separate question from what it will cost to maintain afterwards, and the topic doesn't say whether review asks the second one.
- **Jazz improvisation:** "Looks fine" only means something relative to a standard. The topic doesn't say whether the project has a written structure or set of conventions that each pull request is checked against.

## 6. Grade it like a stranger

**Immune system → Adds nothing.**
- With the picture-words stripped: "each change is judged alone; the problem is in the combination." That restates the person's own phrase "each look fine but together".
- The follow-up ("does anything judge the combination?") is the same call anyone would make from the plain statement.
- Its sneaked-in adversarial framing is noted, but it doesn't rise to misleading under step 4.

**Supply chain → Missing a fact.**
- **Adds nothing?** No. It moves part of the problem from "the combination" to "an unexamined cost in each change, borne by someone other than the author". The topic's "together" doesn't contain that move.
- **Two readings?** Considered: (A) harm only emerges from how changes interact, versus (B) each change carries a small maintenance cost that adds up. Both fit "each look fine but together". But they can both be true at once, and neither is plainly weaker. I judged this imaginable rather than a genuine conflict, so it isn't graded Two readings (see notes).
- **Missing a fact:** whether merged drive-by changes have later needed maintainer work, such as bug reports, questions or fixes on code whose author is gone. The project can get this from its own history.
- **Decision it changes:** whether to add "who will maintain this, and at what cost?" to the merge criteria for pull requests from contributors who won't stay.
- **Other label that also fits:** Worth exploring, with the same question and decision. The earlier label wins.

**Jazz improvisation → Missing a fact.**
- **Adds nothing?** No. The topic says changes "look fine" but never says against what. The picture makes the missing standard visible, which the plain statement leaves implicit.
- **Two readings?** No.
- **Missing a fact:** whether the project has a written structure (architecture, conventions, what does and doesn't belong) that review actually applies to drive-by pull requests.
- **Decision it changes:** whether to write down the project's structural conventions and make conformance to them an explicit review criterion, rather than "looks fine".
- **Other label that also fits:** none.

**Adds nothing: 1 of 3. Misleading: 0. Not run: 2.**

## 7. Sort what's left

**Keep exploring:** (empty)

**Hold:**
- **Supply chain.**
  - Missing fact: whether merged drive-by changes have later needed maintainer work.
  - Question: is "looks fine at merge" the wrong test, rather than just a test that misses the combined effect?
- **Jazz improvisation.**
  - Missing fact: whether the project has a written structure or conventions that review applies.
  - Question: "fine" relative to what?
- **Disagreement, kept as one:** the supply chain picture puts the problem in each change's unexamined carrying cost. The jazz picture puts it in how changes fit together against a shared structure. These point to different fixes (a per-change cost criterion versus a written standard to check against), and I haven't reconciled them.
- **Partial overlap with immune system:** jazz partly overlaps the immune system picture's "does anything judge the combination?" A written structure is one way of judging the combination. The immune system picture isn't in a pile because it added nothing, so this is noted rather than merged.

**Discard:** (empty)

Open Mirror ends here. It hasn't checked any facts or recommended any action. The two missing facts and their questions go to whatever does that work.

---

## REPLICATOR NOTES

1. **"Of [total]".** The count template doesn't say whether the total is pictures run (3) or pictures named (5). I used 3 and reported the 2 unrun separately.

2. **Is "drive-by" an embedded comparison?** Step 1 says to pull out any comparison in the topic. "Drive-by" is a figure of speech, but in open source it's ordinary jargon for a one-time contributor. The method has no rule for dead or conventional metaphors. I treated it as a term of art and defined it, after checking the definition doesn't settle the question. Another replicator could pull it out as picture zero, which would change the count.

3. **No explicit question.** Step 1's stop rule ("if the plain restatement already answers the question") assumes there is a question. This topic is a complaint with an implied cause and no question. I had to infer one (why, or what to do) to apply the stop test.

4. **The person named five pictures.** The first-three rule handled it. But step 2's guidance to choose pictures that show different things doesn't say whether to check the person's first three for diversity. I didn't check or swap them.

5. **What counts as "genuinely conflict" in Two readings.** The method doesn't say whether two readings that can both be true, but imply different responses, count as a conflict. I ruled they don't. Ruling the other way would move supply chain to Keep exploring as Two readings. This was the most consequential judgment call in the run.

6. **"Same call without the picture" has no baseline decision.** The plain statement names no decision, so there's nothing to compare against. I had to imagine what a reasonable maintainer would conclude from the plain statement alone. That is subjective and decided immune system (adds nothing) versus jazz (missing a fact).

7. **Missing a fact and the changed-decision sentence.** Step 6 requires every picture not graded "adds nothing" to name a decision it changed. For pictures graded Missing a fact, it's unclear whether that means the decision would change *once the fact is known*. That's how I wrote it.

8. **Misleading threshold.** Step 4 says to mark a picture misleading if it "only works by" adding a fact. All three pictures brought in something (hostility, commercial ordering, a pre-existing form), but each had a core match that didn't depend on it. "Only" carries all the weight and has no test attached. A stricter replicator could discard immune system for its adversarial framing, or jazz because it can't carry accumulation.

9. **"Can't carry back" versus misleading.** Jazz can't represent the topic's central feature, accumulation over time. Step 4 lists "simply can't carry something back" as a break, but the misleading rule covers only contradiction or an added fact. A picture that fails on the topic's core feature therefore isn't misleading. That may be intended, but it felt odd.

10. **Merging duplicates when one picture isn't in a pile.** Step 7 says to merge duplicates across pictures and name both. It doesn't cover an overlap between a pile entry and an "adds nothing" picture, which appears only in the count. I noted the overlap in one line rather than merging.

11. **Mode declaration.** "Say which mode you're in at the top" appears only in the explanation mode section. I declared filter mode anyway, which may go beyond what the text requires.

12. **Proposed mechanism section.** The person implies a cause (drive-by pull requests cause the decline) but doesn't propose a mapping of the "X works like Y, so build Z" form. I skipped the section. Whether an implied cause counts as a "mechanism" isn't defined.

13. **Exploratory label.** The topic isn't medical, legal, financial or safety-critical. Maintainability touches security only indirectly, so I didn't apply the label. That's a borderline call the method doesn't help with.

14. **Step 3 versus step 6 for each picture's question.** Step 3 asks for "one question the picture makes easier to ask", and step 6's Worth exploring also asks for a question. It's unclear whether the step 6 question must be the step 3 question. I used the same one.

15. **Biology and music claims.** Mapping the pictures required claims about how immune systems and jazz ensembles work. The method forbids checking facts, so those claims are unverified. The method doesn't say whether that weakens a picture.

16. **The evidence folder.** The file references an evidence folder and a CHANGELOG.md. Per instructions I didn't read them. Nothing in the method depended on them.
