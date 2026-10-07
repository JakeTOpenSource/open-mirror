# T5 — sleep debt, bank-account and thermostat lenses

**Case given:** Open Mirror through the "bank account" lens and the "thermostat" lens: "Sleep debt: if I sleep 5 hours a night on weekdays I can pay it back by sleeping 12 hours on Saturday and Sunday, and I'll be fully recovered by Monday."

**Replicator's final message, verbatim:**

---

# OpenMirror v1.3 run: "Sleep debt" claim, bank account lens and thermostat lens

Label: exploratory only. This is a health-adjacent topic, so none of this is a basis for action.

## Step 1. Preserve the baseline

**Explicit statements (supplied):**
- The person sleeps 5 hours a night on weekdays.
- The person would sleep 12 hours on Saturday and 12 hours on Sunday.
- The claim is that this "pays back" the "sleep debt" and leaves them "fully recovered by Monday."

**Proposed interpretations (supplied, untested):**
- A shortfall in sleep is a "debt" that can be "paid back."
- Weekend extra sleep is the payment.
- "Fully recovered by Monday" is the outcome.

**Assumptions (visible in the wording, not stated outright):**
- "Weekdays" means five nights of 5 hours.
- "Saturday and Sunday" means two nights of 12 hours.

**Not specified (these are gaps in the supplied text, not supplied questions):**
- How many hours per night counts as "enough."
- What "fully recovered" means and how it would be observed.
- Which nights are covered, for example whether Sunday night counts toward Monday.
- Whether 12-hour nights are achievable.
- What happens during the weekdays.

**Embedded instructions:** none.

**Does the baseline already answer a question?** No. It is a claim with an undefined outcome, so the run continues.

**Falsifiability answers (Step 1):**
- **Relationship already supplied:** shortfall hours are repaid by surplus hours.
- **Computational analogue already supplied as a proposal:** the "debt / pay it back" ledger wording. It is supplied as a proposal, not a finding.
- **No twin examined yet:** nothing has been revealed.
- **Observable result stated:** "fully recovered by Monday." The measure is not specified.

## Step 2. Select distinct lenses

The user named two lenses, which is within the limit of three. No selection rule was needed.

- **Bank account.** It exposes the "hours are additive and offset each other" relationship.
  - Reason present: the user named it, and it is the shape the supplied claim already uses.
- **Thermostat.** It exposes a "response depends on the current gap from a target, with limited correcting capacity" relationship.
  - Reason present: the user named it, and it is a different function from the ledger (regulating a state versus keeping a running total).

**Falsifiability answers (Step 2):**
- **Bank:**
  - Relationship: shortfalls and surpluses sum across days.
  - Proposed analogue: a running balance.
  - Observable question: does a summed balance predict the Monday outcome? The mapping is incomplete because "enough" per night and the outcome measure are absent.
- **Thermostat:**
  - Relationship: the correction a night delivers depends on the current gap and on a limit.
  - Proposed analogue: a state variable with a target and a bounded correction per step.
  - Observable question: does the Monday state depend only on total hours, or also on the pattern of nights? The mapping is incomplete for the same missing facts.

## Step 3. Map carefully

### Bank account lens

- **Elements:** balance, deposits (weekend nights), withdrawals (weekday shortfall), a zero line.
- **Couplings:** each night adds to or subtracts from one shared total. Deposits cancel withdrawals one-for-one.
- **Pressures and boundaries:** the zero line is the threshold for "recovered."
- **Failure modes:** an unknown threshold, a limit on deposit size, and interim costs.
- **Correspondence:**

| Lens part | Topic part |
|---|---|
| Withdrawal | Each weekday night, 5 h against an unspecified need |
| Deposit | Each weekend night, 12 h against that need |
| Zero balance | "Fully recovered" |

- **New question:** does the topic really behave like one summed total?
- **Proposed connection:** the supplied claim is itself a ledger claim.
- **Computation on the supplied numbers:** 5×5 + 2×12 = 49 h over seven nights, an average of 7 h per night. If the need were n hours per night, the weekday shortfall is 5(n−5) and the weekend surplus is 2(12−n). These are equal when n = 7. This is arithmetic with n left free. The supplied text does not give n.

**Falsifiability answers (Step 3):**
- **Relationship:** hours across nights sum and offset.
- **Analogue:** the balance B = Σ(sleep − need).
- **Observable result:** B compared with whatever "fully recovered" is measured by.
- **Supplied versus proposed:** supplied are the hours and the ledger wording. Proposed are the summation rule and the zero-line threshold.
- **Missing:** the need per night and the recovery measure.

### Thermostat lens

- **Elements:** target state, current state, sensor, correcting output, limit on output.
- **Couplings:** the output is driven by the current gap. It carries no memory of past totals, only the present state.
- **Pressures and boundaries:** the output has a maximum. Heat leaks away in the meantime.
- **Failure modes:** saturation (the gap is larger than the output can close in the time allowed), overshoot, and a missing sensor.
- **Correspondence:**

| Lens part | Topic part |
|---|---|
| Target | Rested state |
| Current state | How rested the person is |
| Output | Sleep |
| Output limit | Whether a night can close any size of gap |

- **Respect in which the mapping holds:** only that recovery is something that happens to a state. It is not a respect in which a thermostat mechanism applies to a person.
- **New question:** is Monday's state a function of total hours, or of the gap and a correction limit? The two schedules compared would be the supplied pattern and the same 49 hours spread evenly.
- **Proposed connection:** none beyond shared shape. The mechanism is not shared.

**Falsifiability answers (Step 3):**
- **Relationship:** gap-dependent correction with a limit.
- **Analogue:** a state with a target and a bounded per-night correction.
- **Observable result:** Monday's measured state under the supplied schedule versus under an even-spread schedule of equal total hours, using a defined recovery measure.
- **Supplied versus proposed:** supplied are the two schedules' hours. Proposed are the state, target, and bound.
- **Missing:** the recovery measure, the response rule, whether a bound exists, and what the bound is.

## Step 4. Find the break point

### Bank account

- **Where it hides or distorts:**
  - The lens hides the unknown threshold. A bank balance has a defined unit and a defined zero. Here the zero line (the need) is not supplied.
  - The lens treats the interim weekdays as costless, which is silent on whatever happens before the weekend.
  - The lens treats deposit size as unlimited, which is silent on whether a 12-hour night is achievable.
- **Imported guarantees:**
  - Hours are additive.
  - Hours are fungible across time.
  - Zero balance equals recovered.
  - Deposits are unbounded.
  - The supplied claim already asserts the first three as proposals, so the lens adds no fact beyond them.
- **Relationship in question:** the additivity of hours across nights.
- **Part of the analogue that depends on it:** the whole balance.
- **Observable result that would break it:** unavailable.
- **Missing definitions:** the need per night, the recovery measure, and which nights count.

I am not writing a conditional falsifier, because the behavior is undefined in the specification.

### Thermostat

- **Where it hides, distorts, or cannot carry back:**
  - A thermostat's actuator responds automatically under a known rule. In the topic, the "actuator" is the person choosing to sleep 12 hours, and whether the body will do so is unspecified.
  - The lens has no memory of past totals. That sits against the supplied word "debt," which is a ledger word, although "recovered" is a state word. The baseline contains both words and does not say they coincide.
  - A target state and a bound on correction are imported structure. Nothing supplied says either exists.
- **Imported guarantees:**
  - There is a target.
  - A correction rule exists and is bounded.
- **Relationship in question:** gap-dependent, bounded correction.
- **Part of the analogue that depends on it:** the whole state model.
- **Observable result that would break it:** unavailable.
- **Missing definitions:** the recovery measure, the response rule, and the correction bound.

The lens is not rescued by its elegance. Its content survives only as a question, not as a mechanism.

## Step 5. Return to literal language

**Bank literal return:**
- The claim adds weekday shortfalls and weekend surpluses as hours that offset each other.
- The supplied numbers give 49 hours over seven nights, an average of 7 hours per night.
- Whether that settles recovery depends on the nightly need and on what "fully recovered" means. Neither is supplied.

**Thermostat literal return:**
- Whether two 12-hour nights fully recover five 5-hour nights by Monday may depend on more than the hour total.
- It may depend on how much of a shortfall a single night can close, and on whether the same 49 hours spread evenly would give the same Monday result.
- The claim does not say whether such a limit exists, how Monday recovery is measured, or whether the supplied pattern and an even pattern should be treated as equivalent.
- These items are missing, not answered.

**Falsifiability answers (Step 5), restated in language about the problem:**
- **Bank:**
  - Relationship: hours offset across nights.
  - Analogue: a running total of hours against a per-night need.
  - Observable result: that total compared with a defined Monday recovery measure. Both the need and the measure are unavailable.
- **Thermostat:**
  - Relationship: recovery may depend on the size of the gap and on a per-night limit.
  - Analogue: a state with a target and a bounded per-night correction.
  - Observable result: the Monday measure after the supplied schedule versus after an even schedule of equal total hours. The measure is unavailable.

## Step 6. Grade in a separate pass

This pass rereads the maps as if someone else wrote them, looking for reasons to reject them. NO INCREMENT is considered first and RELATED last.

### Bank account

- **NO INCREMENT firing test:** remove the metaphor words from the literal return. What remains is that shortfall hours are offset by surplus hours, that 49 hours over seven nights averages 7, and that the need and the outcome measure are unspecified. The first part restates the supplied proposal ("pay it back"). The 49-hour and 7-hour arithmetic comes straight from the supplied numbers. The missing items were already gaps in the baseline. A reader holding only the baseline would make the same decision. **Status: NO INCREMENT.**
- CONTESTED, UNKNOWN, and RELATED are not reached.

### Thermostat

- **NO INCREMENT considered first:**
  - The literal return does not restate a supplied proposal. It questions the supplied outcome.
  - The skeptic's objection is that any reader could already ask whether the claim is just about hours, and so the lens adds nothing.
  - The counter-point is that the baseline does not contain the specific distinctions of equal totals versus equal recovery, or of a per-night limit.
  - The disagreement is recorded, not settled (see below).
- **CONTESTED firing test:**
  - There are two readings of the baseline words. "Pay it back" supports ledger. "Fully recovered" supports state.
  - They do not conflict in the supplied text, because the user treats them as the same thing.
  - The state-dependent reading's key content, a per-night limit, requires imported facts.
  - CONTESTED is therefore not established.
- **UNKNOWN firing test:**
  - Missing context prevents classification.
  - The specific missing facts are the measure by which "fully recovered" is judged, and the per-night correction rule or bound.
  - **Status: UNKNOWN.**
- **RELATED firing test:**
  - The question is whether equal-total schedules give equal Monday results.
  - A concrete decision would be whether to treat the hour arithmetic as sufficient evidence for the claim.
  - A reader could change that decision using their own readily available past Monday observations.
  - This is weak. A reader with the baseline could make that decision unaided, and the decision does not become answerable until the recovery measure is defined.
  - I do not assign RELATED. The specification does not settle the tie between UNKNOWN and RELATED, and I preserve that disagreement.

### Reporting

- **NO INCREMENT count: 1** (bank account). Dissent preserved: the skeptic reading above would make the thermostat a second NO INCREMENT, which would make the count 2. The specification does not settle this.
- Because the count is not zero, the one-sentence-per-lens requirement does not apply.

**Falsifiability answers (Step 6):**
- **Does the relationship add beyond the baseline?**
  - Bank: no.
  - Thermostat: marginally (the equal-totals-versus-equal-recovery distinction), with the dissent noted.
- **Does the analogue depend on missing or imported facts?** Yes, in both lenses. The need, the measure, and the response rule are missing.
- **Does the observable result bear on the mapping?** Only once the recovery measure is defined. No test has been run or passed.

## Step 7. Leave the user in control

**Cross-lens synthesis:**
- There is nothing to merge. Only one lens survives grading above NO INCREMENT.
- No disagreement between graded lenses exists. The bank and thermostat lenses were not forced into consensus.
- Repetition is not verification.

### KEEP EXPLORING
None.

### HOLD AS UNKNOWN
**Entry 1 (from the thermostat lens):** recovery by Monday may depend on the size of the shortfall and a per-night correction limit, not only on total hours.

- **Relationship:** gap-dependent, bounded correction compared with a summed total.
- **Proposed computational analogue:** a state variable with a target and a bounded per-night correction. Its details are not defined.
- **Observable result:** the Monday measure after 5×5 + 2×12 hours compared with the same 49 hours spread evenly across seven nights.
- **Missing information:**
  - The definition and measure of "fully recovered."
  - The nightly need.
  - The per-night response rule and any bound.
  - Which nights count toward Monday.
- This is not a completed executable crosswalk. It carries these falsification conditions to the next workflow. OpenMirror does not execute them or approve consequences.

### DISCARDED METAPHOR
None. The bank lens is NO INCREMENT, which is merely unhelpful, not misleading. It appears only in the count.

**Removed entries:** none.

---

## REPLICATOR NOTES

These are the points where the method text was ambiguous, impossible to satisfy, or where I had to invent a rule.

1. **Supplied proposal versus user-named lens.**
   - Step 1 says to identify any "computational analogue already supplied." The user named lenses but supplied no mapping.
   - I treated the claim's own "debt / pay it back" wording as the supplied analogue. The text does not say whether a user-named lens counts as a supplied analogue.
   - This choice drove the bank lens to NO INCREMENT.

2. **Arithmetic on supplied numbers.**
   - I computed 49 hours, an average of 7, and the break-even n = 7 with n free.
   - The method forbids adding facts but does not say whether derived arithmetic counts. I judged it derived, not added.
   - It could be read as supplying a rule (a threshold) that the Step 4 "missing rule" clause prohibits.

3. **Observable result at Step 4 versus the ban on conditional falsifiers.**
   - Step 4 requires "the observable result that would break the mapping," but forbids conditional falsifiers for behavior left undefined, and forbids a falsifier that supplies the missing rule.
   - In practice both lenses' observable results are undefined, so I wrote "unavailable" plus the missing definitions. The method allows this only implicitly.

4. **Falsifiability fields at steps where the lens is later graded NO INCREMENT.**
   - The method requires the fields at every step, but the NO INCREMENT lens is excluded from the dispositions.
   - I filled the fields anyway. The method does not say whether this is padding under the proportionality rule.

5. **The NO INCREMENT / UNKNOWN / RELATED tie for the thermostat lens.**
   - "NO INCREMENT first, RELATED last" is ambiguous. It could mean order of consideration or order of precedence.
   - The tie rule says to preserve a supported disagreement but does not say how to count a disagreement for the NO INCREMENT count.
   - I reported "1, with dissent that it could be 2." This is an invented reporting convention.

6. **The RELATED "decision" test in a health topic.**
   - RELATED needs a concrete decision, but the operating rules forbid recommending consequential action.
   - I could not name a decision that is both concrete and non-consequential without the test turning trivial. I used this to withhold RELATED.

7. **The count-zero sentence.** The rule applies only when the count is zero. It is unclear whether providing the sentences otherwise is allowed or discouraged. I omitted them.

8. **"All three fields" in Step 7.** The three fields are never enumerated. I assumed they were relationship, computational analogue, and observable result.

9. **CONTESTED.** The baseline contains both a ledger word and a state word. I judged that they do not conflict because the user equates them. The method gives no rule for a supplied equivalence that may itself be the contested point.

10. **Imported structure is unavoidable in the map.**
    - Step 3 requires elements, couplings, and boundaries for the lens. Describing a thermostat inherently imports regulator structure (target, limit, leakage).
    - I labeled the structure as proposed. The "no theory added" exit criteria of Step 1 apply only to the baseline, and the method does not say how far a lens's own structure may go.

11. **Literal return that keeps the analogue visible without the metaphor.** Step 5 asks for this. I found it hard to state a "bounded correction" or "ledger" analogue without metaphor-adjacent words. I used "running total" and "per-night limit" and cannot tell whether this meets the criterion.

12. **Domain ambiguity in the topic.** "Weekdays," "Saturday and Sunday," and "by Monday" leave open which nights count. The method has no step for resolving ambiguity in the supplied text other than listing it as unspecified, which I did.

13. **Thermostat's "memoryless" feature versus the baseline's "debt" word.** I described this as a conflict with the baseline. The method's wording on "contradiction with the baseline" does not say whether a word-choice tension counts as a contradiction.

14. **Proportionality.** The method lets a direct answer stop the run early. Here the baseline does not answer. I ran all steps, though a run could arguably have been shorter.
