# T1 — procrastination, open topic, no named lenses

**Case given:** Open Mirror this: "Why do people procrastinate on tasks they actually want to do?"

**Replicator's final message, verbatim:**

---

# OpenMirror v1.3 run

Topic as supplied: "Why do people procrastinate on tasks they actually want to do?"
This output is exploratory. I did not browse, verify claims, or recommend action.

---

## Step 1. Preserve the baseline

**Explicit statements (as supplied)**
- The sentence is a question about people who procrastinate.
- The tasks in question are ones the people "actually want to do."

**Presuppositions inside the question** (treated as supplied, not verified)
- Such procrastination happens.
- "Actually" contrasts wanted tasks with unwanted ones.

**Proposed interpretations:** none supplied.

**Assumptions visible in the wording**
- "Want" is attached to the doing of the task.
- The word "want" is not defined further. It does not say wanting at what moment, or wanting the activity versus its result.

**Open question:** why this happens. No cause, mechanism, or proposal was supplied.

**Instructions embedded in examined material:** none. "Open Mirror this:" is the invocation. The quoted question is the content.

**Does the baseline already answer the question?** No. The run continues.

**Supplied proposals to guard against restating:** none exist, so the NO INCREMENT-by-restatement test applies only to the baseline's own wording and open items.

**Falsifiability answers (step 1)**
- Relationship supplied as a proposal: none.
- Computational analogue supplied: none.
- No twin has been examined, so none is claimed to reveal anything.
- Observable result stated: none. What is not yet specified: any measure of "procrastinate," any definition of "want," and any data.

---

## Step 2. Select distinct lenses

User-named lenses: none. I chose three, each exposing a different function or scale:
- **Lens A, cold start.** Function: initiation, meaning when the delay sits within a task. Reason: the baseline gives no location for the delay.
- **Lens B, release gating.** Function: what finishing exposes, meaning the relationship between completing a wanted thing and its being judged. Reason: the baseline treats "want" and "delay" as the only variables.
- **Lens C, competing schedulers.** Scale: across moments inside one person, meaning several decision rules with different time horizons. Reason: a pair of "wanting" and "not doing" is superficially contradictory and needs a structure that could hold both.

A fourth lens was not added. It would not change a decision.

**Falsifiability answers (step 2)**
- A. Relationship to examine: where in a task's timeline the delay sits. Proposed computational analogue: start-up latency. Observable question: is the delay mostly before the first action? The mapping is incomplete. How to tell a "first action" is absent.
- B. Relationship: delay varies with whether the finished result will be judged. Analogue: a release step that gates a finished product. Observable question: does delay differ between wanted tasks whose results will be judged and wanted tasks whose results will not? The mapping is incomplete. Who counts as the judge is absent.
- C. Relationship: wanting may differ in strength across moments or components. Analogue: a scheduler combining rules with different time horizons. Observable question: is the delay present when the want is the same at every moment? The mapping is incomplete. Nothing in the baseline says the want varies.

---

## Steps 3 to 5, per lens

### Lens A: cold start

*Plain definition: "cold start" is the delay a computing service has before its first response, because it has to load and set up before it can respond. After that it responds quickly while it stays "warm."*

**Step 3: map**
- Elements. Request (the wanting). Idle system (the person not yet engaged). Setup cost (working out the first step and gathering context). Delay before first output. Warm state (the later steps being cheaper).
- Couplings. A request triggers setup. Setup cost produces delay. Warm state lowers the delay of later steps.
- New question. For a wanted task, is the delay concentrated at the very beginning, and does it ease once the person is under way?
- Proposed connection. Delay on wanted tasks corresponds to a setup cost that is large relative to how much the task is wanted. The named respect is timing structure only: where the delay sits.

**Falsifiability (step 3)**
- Relationship: the delay is located before the first action rather than spread across the task.
- Proposed analogue: start-up latency.
- Observable result bearing on the mapping: a record of when, across a task's timeline, the person is delaying.
- Supplied versus proposed: all of this is proposed. The baseline supplies none of it.
- Missing: what counts as "the first action" for a human task.

**Step 4: break point**
- Where the metaphor hides: a server's start-up cost can be measured independently of whether it starts. A person's "setup cost" cannot be observed apart from the delay it is meant to explain. So the lens risks circularity, where delay is explained by setup cost and setup cost is evidenced by delay.
- Where it distorts: a server has no reluctance. The lens carries no emotion or avoidance, so it says nothing about why the setup is heavy.
- Imported facts and guarantees: that the delay is a cost and not an avoidance, and that the warm state persists once reached.
- Concrete limit: the lens locates the delay but does not explain it. The "why" in the baseline is still open.

**Falsifiability (step 4)**
- Relationship in question: delay is concentrated before the first action.
- Dependent part of the analogue: the idea that later steps are cheap once started.
- Observable result that would break the mapping: delay is just as present during the task as before it.
- Missing definitions: what counts as the start and as a stall, and how delay is measured.
- I have not run this test.

**Step 5: literal return**
For a wanted task, the delay may be concentrated before the person takes the first action, with the reluctance mostly easing afterward. This is a claim about where the delay sits, not why it exists. It would be wrong if people delay about as much in the middle of a wanted task as before it. Missing: what counts as the first action, and any data.

### Lens B: release gating

*Plain definition: "release gating" means a finished product is held back because releasing it lets others judge it. The product stays in a private state until the step is taken.*

**Step 3: map**
- Elements. Work the owner values. A completion step that exposes the work. Judgment from others or from oneself. A private state in which the work is not yet judged.
- Couplings. Caring about the work raises the cost of a poor result. Completing exposes the work to judgment. The private state keeps the possibility of the work being good.
- New question. Is the delay on wanted tasks larger when the finished result will be judged?
- Proposed connection. Wanted tasks are ones whose results matter, and mattering raises the stakes of finishing. The named respect is the link between finishing and exposure to judgment.

**Falsifiability (step 3)**
- Relationship: delay rises with how judged the finished result will be.
- Proposed analogue: a release step that gates a valued product.
- Observable result bearing on the mapping: compare delay on wanted tasks with a judged result against wanted tasks with an unjudged result.
- Supplied versus proposed: all proposed.
- Missing: whether self-judgment counts as judgment.

**Step 4: break point**
- Where the metaphor hides: a software release has a defined moment, an audience, and a rollback. Many wanted tasks, such as a private hobby, have no audience or moment of exposure.
- Imported facts: that wanting a task means caring how the result is judged. The baseline says only "want to do."
- Concrete limit: if self-judgment counts as judgment, nothing is unjudged and the lens can never be contradicted. If it does not count, the lens contradicts the baseline's own cases of private wanted tasks that still get delayed.

**Falsifiability (step 4)**
- Relationship in question: delay depends on judgment of the result.
- Dependent part of the analogue: the gate, meaning the completion step.
- Observable result that would break the mapping: no difference in delay between judged and unjudged wanted tasks. That result cannot be observed yet.
- Missing definitions: whether self-judgment counts, who the judge can be, and how to pair comparable tasks.
- Not run.

**Step 5: literal return**
Delay on a wanted task may depend on whether the finished result will be judged. Whether this can be tested depends on whether judgment by oneself counts. The baseline does not say whether the tasks in question have a judged result at all.

### Lens C: competing schedulers

*Plain definition: a "scheduler" in computing decides which job runs when, combining several rules. Here the picture is one rule favoring immediate payoff and another favoring later payoff.*

**Step 3: map**
- Elements. A short-horizon rule. A long-horizon rule. A dispatcher that chooses.
- Couplings. Each rule pushes a task up or down the queue. The dispatcher combines them.
- New question. Is the wanting the same at every horizon?
- Proposed connection. A person may want a task in one sense or at one moment but not in another.

**Falsifiability (step 3)**
- Relationship: wanting varies across moments.
- Proposed analogue: a scheduler with differing time horizons.
- Observable result: delay when the wanting is held equal.
- Missing: the baseline does not say the wanting varies. That is supplied by the lens, not the topic.

**Step 4: break point**
- If both rules favor the task, the lens predicts no delay. That contradicts the baseline's stated observation unless the wanting is split.
- The split is an imported fact. It is not in the baseline.
- Rescuing the lens requires adding that people decide by weighing time horizons, which is imported theory.
- The lens fails to carry anything back unless that import is allowed.

**Falsifiability (step 4)**
- Relationship in question: wanting differs across moments.
- Dependent analogue part: the split rules.
- Observable result that would break it: delay occurring when the wanting is the same across moments. This cannot be observed without a definition of "want" and of "moment."
- Missing definitions: want at which time, and of the activity or the result.

**Step 5: literal return**
The wording "actually want" leaves open whether the task is wanted in the same way at every moment and in the same respect, either as an activity or as an outcome. This is a point about the baseline's own undefined term.

---

## Step 6. Grade in a separate pass

I reread each lens looking for reasons to reject it. NO INCREMENT is considered first and RELATED last. The writing is separated, but this is not proof of an independent mental process.

### Lens C

- **NO INCREMENT.** The literal return, with the metaphor removed, says the baseline's term "want" is undefined. Step 1 already recorded that. A reader holding only the baseline would make the same decision. The contradiction found in step 4 only shows the lens fails unless a theory is imported.
- **Status assigned: NO INCREMENT.**
- **CONTESTED checked.** The readings are wanting the activity versus wanting the result. The baseline says "want to do," which supports the first. The second needs imported facts, and is a conceivable alternative only. It does not qualify.
- **UNKNOWN is arguable.** The missing fact would be the sense and moment of "want." I preserve that as a supported alternative the spec does not settle. See Notes.

### Lens B

- **NO INCREMENT checked.** The literal return adds a variable (whether the result is judged) that is not in the baseline, so it does not simply restate the baseline.
- **CONTESTED:** not applicable, with no two conflicting readings.
- **UNKNOWN.** The missing fact is whether the wanted tasks in question have a result that someone, possibly the person, judges. Without it the lens cannot be classified.
- **RELATED checked and rejected.** A concrete decision cannot be named without supplying the rule for self-judgment, which step 4 forbids.
- **Status assigned: UNKNOWN.**

### Lens A

- **NO INCREMENT.** The remainder, "check where in the task the delay sits," is not in the baseline. A reader holding only the baseline would not have this variable.
- **CONTESTED:** no.
- **UNKNOWN checked.** "First action" is undefined. But a reader can use their own recollection of whether they stall after beginning, so the lens is not blocked.
- **RELATED.** The question: after a person begins a wanted task, does the reluctance mostly end? The decision a reader could change using information already held: whether to sort their own case as a start-problem or a whole-task problem, and so which family of "why" to examine first. Weakness: this is a classification decision, and the question is partly "asking whether to consider something."
- **Status assigned: RELATED,** with that weakness recorded.

### Reporting

- **Number of NO INCREMENT lenses: 1** (Lens C).
- The count is not zero, so the one-sentence-per-lens requirement does not apply.
- **Falsifiability answers (step 6).**
  - A. The relationship adds a variable to the baseline. The analogue depends on a missing definition of the first action. The observable result would bear on the mapping, but I have not run it.
  - B. The relationship adds a variable. The analogue depends on missing definitions of the judge and of self-judgment. The observable result does not yet bear on the mapping.
  - C. The relationship adds nothing beyond the baseline's undefined term. The analogue depends on imported theory.
  - No grading decision here establishes that any test passed.

---

## Step 7. Leave the user in control

**Cross-lens synthesis.** Lenses A and B are independent observations and do not merge. Lens C repeats an open item already in the baseline, and repetition is not verification. No disagreement between lenses needs preserving. Nothing here forces consensus.

**KEEP EXPLORING**
- **Lens A.** Candidate question: is delay on wanted tasks mostly before the first action, and does reluctance ease once the person begins?
  - Relationship: the delay is located at the start.
  - Computational analogue: start-up latency.
  - Observable result: a record of when across the task the delay occurs.
  - Missing information: what counts as the first action, how delay is measured, and any data.

**HOLD AS UNKNOWN**
- **Lens B.** Candidate: delay depends on whether the result will be judged.
  - Relationship: delay varies with judgment of the result.
  - Computational analogue: a release step gating a valued product.
  - Observable result: unavailable.
  - Specific missing information: whether self-judgment counts as judgment, who the judge can be, and whether the wanted tasks in question have a judged result at all.
  - This is not a completed executable crosswalk.

**DISCARDED METAPHOR:** empty. No graded lens other than C had a mapping that broke, and C is NO INCREMENT, which appears only in the count. C's break point (the lens predicts no delay unless "want" is split by an imported theory) is preserved in step 4 only.

**Removed entries.** I removed one entry. It was "the term 'want' in the question is undefined." It traces to Lens C, which is NO INCREMENT and so cannot appear in a list, and to the baseline itself, which is not a lens. Its removal is reported here.

**Carried to the next workflow.** Lens A and Lens B travel with the falsification fields above. OpenMirror does not execute them or approve consequences. No answer to "why" has been produced. A and B only change which questions are asked.

---

# REPLICATOR NOTES

1. **Invocation wrapper.** "Open Mirror this:" is not addressed by the method. I treated it as an invocation and the quoted question as the topic.
2. **Presupposition classification.** The method does not say whether the presuppositions inside a question count as explicit statements or as assumptions. I recorded them as presuppositions treated as supplied.
3. **Lens selection with no named lenses.** The method says only that each lens needs "a reason to be present." It has no rule for choosing among candidates. I invented my own criterion (distinct function or scale) and a stopping point (a fourth would not change a decision).
4. **"Computational analogue."** The falsifiability fields at every step require one, but the method does not say whether the twin must be computational. I made all three lenses computing metaphors to satisfy the wording. A non-computational twin would have left those fields unfillable, and the method does not say what to do then.
5. **Step 4 falsifier rule is thin.** It forbids conditional falsifiers for undefined behavior and forbids "supplying the missing rule." Yet I still had to write an observable result in terms like "delay before the first action." That already partitions the task into start versus rest. I could not tell where naming a missing definition ends and supplying one begins. The Lens A wording is the most exposed.
6. **RELATED versus UNKNOWN boundary.** A was RELATED because the reader can use their own sense of "started." B was UNKNOWN because the term "judged" would have to be defined by me. The method does not say when a reader may supply a definition from their own information and when that counts as a failure. The A/B split depends on my judgment and could be argued the other way.
7. **"Concrete decision" has no natural content here.** This is a pure why-question with no action context, and the method forbids recommending consequential action. The only decisions I could name were classification choices about one's own case. That is my invented reading of "decision," and A's RELATED status rests on it.
8. **NO INCREMENT for Lens C depends on what I put in step 1.** I recorded the undefined term "want" as an open item in the baseline, so Lens C's return restated it. Had I left that out of step 1, C would plausibly be UNKNOWN or RELATED. The method does not say how much to list as "not specified" in step 1, so the outcome is sensitive to that choice.
9. **Misleading lens that is also NO INCREMENT.** Lens C's break point is a contradiction with the baseline (misleading), but its status is NO INCREMENT, and NO INCREMENT lenses are barred from the disposition lists. The method says to record a break point and disposition for a misleading lens, and also says NO INCREMENT appears only in the count. The two conflict, and the "why it broke" content for C survives only in step 4.
10. **No mapping from statuses to dispositions.** The method gives four statuses and three dispositions but never says which goes where. I mapped RELATED to KEEP EXPLORING and UNKNOWN to HOLD AS UNKNOWN by inference. CONTESTED has no stated destination, and I had none in this case.
11. **Merged entries versus "traces to one lens."** Step 7 says to merge duplicate observations across lenses, and also that every entry traces to one graded lens. I could not see how a merged entry satisfies both, so I kept entries separate and put the merging discussion in prose.
12. **The three falsifiability fields at step 7 are not named there.** I inferred them as relationship, computational analogue, and observable result, from the step 5 wording.
13. **Tie handling.** The method preserves a supported disagreement when ties are unsettled. I used that for C (NO INCREMENT versus UNKNOWN), but how a preserved disagreement should be reported is not specified, so I put it in the grading text.
14. **No answer to the question.** The TL;DR says a direct answer can stop early, but nothing says what a good output is when the run ends with candidate questions and no answer. This run produced none for "why."
15. **Grading separation.** The method asks me to "stop generating maps and reread them as if someone else wrote them." I can only do that in writing, and the method concedes this. My grading text was written in the same session as the maps.
16. **Imported domain knowledge.** Building any lens required imported facts about the twin domain (what a cold start is, what a release gate is). The method treats the twin as a temporary viewpoint but also bars importing facts. I defined the technical terms in plain language but could not avoid the import.
17. **Delivery.** I read only the method file, as instructed. I used the final-report call that this harness requires to return the output. That call is a delivery mechanism and was not used for any research.
