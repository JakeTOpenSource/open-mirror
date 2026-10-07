# T3 — drive-by pull requests, five user-named lenses

**Case given:** Open Mirror through immune system, supply chain, jazz improvisation, plate tectonics, and parliamentary procedure: "Our open-source project gets lots of drive-by pull requests that each look fine but together the codebase is getting harder to maintain."

**Replicator's final message, verbatim:**

---

# OpenMirror v1.3 output

**Topic:** "Our open-source project gets lots of drive-by pull requests that each look fine but together the codebase is getting harder to maintain."
**User-named lenses:** immune system, supply chain, jazz improvisation, plate tectonics, parliamentary procedure.
**Status:** exploratory only. Nothing here verifies a claim or recommends action.

---

## Step 1. Preserve the baseline

**Explicit statements supplied**
- The project is open source.
- It receives "lots of" drive-by pull requests. "Drive-by" is not defined. I read it as one-off contributions, but that reading is mine.
- Each pull request "looks fine".
- "Together" the codebase is "getting harder to maintain".

**Proposed interpretations supplied**
- None. The user supplied no theory, relationship, or computational analogue. Five lens names were supplied, but each is only a name.

**Assumptions the supplied text leans on (not verified)**
- The pull requests are linked to the maintainability decline. The text states them together but does not say one causes the other. The supplied sequence is not established causation.
- "Looks fine" means the pull requests pass whatever review is currently applied. The review criteria are not described.
- It is not stated whether the pull requests are merged, only opened, or both.

**Open questions**
- What does "harder to maintain" mean in observable terms (review time, defect rate, rework, onboarding difficulty)? No observable result was supplied.
- What does "lots" mean, and over what period?
- Is any question actually being asked? The input is a problem statement with no explicit question.

**Instructions embedded in examined material:** none.

**Does the baseline already answer the question?** No. There is no answer in it, and no question to answer beyond the implied "what is going on here?". The run continues.

**Falsifiability answers at this step**
- Relationship supplied: none beyond the stated co-occurrence of many individually fine pull requests and aggregate difficulty.
- Computational analogue supplied: none.
- No twin domain has been examined, so nothing has been revealed yet.
- Observable result supplied: none. Not yet specified: the measure of "harder to maintain", the time window, and the pull-request population.

---

## Step 2. Select distinct lenses

**Five lenses were named, and the ceiling is three.** The method says the source does not settle how to select among more than three user-named lenses, and that I should expose the gap rather than silently choose a new rule.

- **Gap exposed:** no selection rule exists in the method for this case.
- **Provisional handling, which I invented:** I carried forward the first three in the user's order, so that the choice does not depend on my judgement of relevance. These are immune system, supply chain, and jazz improvisation.
- **Plate tectonics and parliamentary procedure were not evaluated.**
  - They were not graded and not discarded.
  - They are not counted as NO INCREMENT.
  - They do not appear in any disposition list.
  - They remain available to a later run.

**Reason each chosen lens is present**
- **Immune system:** it concerns discriminating acceptable from harmful items. This is the function a pull-request review performs.
- **Supply chain:** it concerns flow of units through stages with limited capacity. It exposes rate and capacity relationships.
- **Jazz improvisation:** it concerns many independent contributors fitting a shared whole. It exposes coordination that is not written down.

**Falsifiability answers at this step**

| Lens | Relationship to examine | Computational analogue (my proposal) | Observable question the mapping must answer |
|---|---|---|---|
| Immune system | Item-by-item screening against a larger body's state | A per-item check versus a monitor of cumulative state | Does anything in the project evaluate the codebase's accumulated state, as distinct from each pull request? |
| Supply chain | Arrival rate of units versus a stage's ability to absorb them | A queue with arrivals, a service capacity, and an unabsorbed residue | Does the difficulty track how many pull requests arrive or merge, or something else? |
| Jazz improvisation | Local fit versus fit with an unwritten shared structure | A conformance check of a change against a set of conventions | Do drive-by pull requests differ from regular contributors' on conventions that are not documented? |

In all three cases the user supplied no analogue. These are my proposals, and their parameters are missing.

---

## Step 3. Map carefully

### Lens A: Immune system

- **Elements:**
  - the body is the codebase;
  - a threat or foreign item is a pull request;
  - the detector is the reviewer or CI;
  - a tolerated item is a merged pull request.
- **Couplings:**
  - the detector acts on each item as it arrives;
  - tolerated items remain and change the body's state;
  - the detector's criteria constrain what gets through.
- **Pressures:** many arrivals and limited detector attention.
- **Boundaries:** self versus non-self.
- **Possible failure modes:** over-rejection or under-rejection.
- **New question:** is the failure here a missed threat, or an accumulated effect of items the detector correctly passes?
- **Proposed connection:** the baseline says the pull requests look fine, so per-item detection appears to be working. The residual problem sits outside per-item detection.

**Falsifiability answers**
- Relationship: per-item screening versus cumulative state.
- Analogue (proposed, and its details are missing): per-item classifier versus a cumulative-state monitor.
- Observable result bearing on the mapping: whether any current review step looks at aggregate effects.
- Missing: what the project currently checks beyond each pull request.

### Lens B: Supply chain

- **Elements:**
  - contributors are suppliers;
  - pull requests are delivered parts;
  - maintainers are the assembly stage;
  - the codebase is the assembled product and also the standing inventory;
  - review capacity is the throughput of the assembly stage.
- **Couplings:**
  - supplier output rate affects the assembly stage's load;
  - parts conformant at the part level may not fit at the assembly level;
  - unreconciled parts add to later assembly work.
- **Pressures:** arrival volume against capacity.
- **Boundaries:** a part's specification versus the whole product's fit.
- **Possible failure modes:**
  - the stage is overloaded;
  - parts are individually correct but jointly incompatible.
- **New question:** is the difficulty driven by how many pull requests arrive (a volume and capacity relationship) or by what they contain (a content relationship)?
- **Proposed connection:** these are two different sources of "together", and the baseline does not distinguish them.

**Falsifiability answers**
- Relationship: pull-request arrival and merge rate versus maintainers' integration capacity, and versus some property shared across merged pull requests.
- Analogue (proposed, parameters missing): a queue with arrivals, a service capacity, and a residue of unabsorbed work.
- Observable result bearing on the mapping: the relationship between a defined maintenance-difficulty measure and merged pull-request volume over time, compared with its relationship to a shared content property.
- Missing: the definition of "harder to maintain", the unit of volume, and the population and window.

### Lens C: Jazz improvisation

- **Elements:**
  - the players are contributors;
  - the form or chord changes are the project's conventions and architecture;
  - listening is awareness of the rest of the codebase;
  - the ensemble sound is overall coherence.
- **Couplings:**
  - each player's choices are constrained by the shared form;
  - coherence depends on players hearing each other;
  - a player who joins briefly has less exposure to the form.
- **Pressures:** many short-lived contributors.
- **Boundaries:** the line between convention that is written and convention that is only absorbed by being present.
- **Possible failure modes:** notes that fit the local chord but not the arrangement.
- **New question:** do drive-by pull requests fit the codebase locally but diverge from conventions that are not documented?
- **Proposed connection:** this is a candidate explanation for "each fine, together harder".

**Falsifiability answers**
- Relationship: local fit versus fit with a set of conventions.
- Analogue (proposed, details missing): a conformance check of a change against a convention set.
- Observable result bearing on the mapping: whether drive-by and regular-contributor pull requests differ on a defined set of conventions.
- Missing: whether conventions are documented, what they are, and how conformance would be judged.

---

## Step 4. Find the break point

(Written before any status is assigned.)

### Lens A: Immune system

- **Where it breaks:**
  - The immune lens's core function is detecting harmful items. The baseline says no individual pull request is flagged as harmful.
  - The lens therefore has no mechanism for harm that arises only from accumulation, except by importing further biological ideas such as chronic effects of tolerated items. Those would be imported mechanisms, not supplied facts.
  - Self versus non-self is well defined in the body. In the project, what counts as "self" is exactly what is unspecified.
- **Imported facts or guarantees:** that a screening system reliably discriminates, and that over-rejection has a known cost.
- **Relationship in question and dependent analogue:** the "cumulative-state monitor" depends on the project defining what state to monitor. That definition is missing.
- **Observable result that would break the mapping:** none can be stated without the missing definition of "state".
- **Missing definitions:** what accumulated property is meant, and how it would be read from the codebase. No test has been run.

### Lens B: Supply chain

- **Where it breaks:**
  - The pull-request-as-part analogy assumes parts are comparable units. Pull requests vary in size and kind, so counting them may not measure load.
  - Supply chains have demand signals and contractual control of suppliers. Drive-by contributors have neither.
  - Parts are consumed in assembly, whereas merged code persists and is touched again.
- **Imported facts and guarantees:**
  - the idea of a constraint stage that limits system throughput;
  - the idea that variability amplifies along a chain;
  - the guarantee that regulating arrivals would stabilize the system. None of these is supplied by the baseline.
- **Relationship in question and dependent analogue:** the volume and capacity relationship depends on the queue analogue, which needs defined arrival units and a capacity measure.
- **Observable result that would break the mapping:** the comparison of a maintenance-difficulty measure against volume versus against content. What outcome would count as breaking the mapping cannot be stated without those definitions. Writing a threshold here would supply the missing rule.
- **Missing definitions:** the maintenance-difficulty measure, the unit and window of volume, and the capacity measure. No test has been run.

### Lens C: Jazz improvisation

- **Where it breaks:**
  - Jazz coherence is judged by listeners, aesthetically and in real time. Maintainability has no equivalent real-time audience.
  - The lens presumes a shared form exists and is partly unwritten. That is an imported assumption about this project.
  - Jazz tolerates and prizes deviation. A convention violation here is not obviously a virtue or a flaw.
- **Imported facts and guarantees:** that unwritten conventions exist, that drive-by contributors are less exposed to them, and that conformance and maintainability are related.
- **Relationship in question and dependent analogue:** the conformance check depends on a convention set that is not supplied.
- **Observable result that would break the mapping:** none can be stated until the convention set and the conformance judgement are defined.
- **Missing definitions:** the convention set, the conformance rule, and what counts as drive-by. No test has been run.

---

## Step 5. Return to literal language

### Lens A literal return
The pull requests pass per-item review, and the project's difficulty arises in aggregate. This depends on whether anything currently examines the codebase's accumulated state. The analogue is a per-item check versus a cumulative-state check, and its definition of "state" is missing. The observable result is whether any current review step looks beyond the single pull request. This reads as the same as the baseline sentence.

### Lens B literal return
It is not established whether the growing maintenance difficulty tracks how many pull requests are merged (volume relative to maintainer capacity), or tracks a property that the merged pull requests share (content), or both. The analogue is a queue of arrivals, a capacity, and a residue. The observable result is the relationship of a defined difficulty measure to volume over time, compared with its relationship to a shared content property. The measure, the unit and window, and the capacity are all missing.

### Lens C literal return
Drive-by pull requests may each fit the code around them while diverging from conventions that are not written down. If so, the aggregate effect could come from that divergence. This depends on whether such conventions exist, and the project's convention set is missing. The observable result is whether drive-by and regular-contributor pull requests differ on a defined set of conventions. The set and the conformance rule are missing. This is a candidate mechanism, not a finding.

---

## Step 6. Grading pass (separate review)

I reread the three maps as if someone else wrote them, looking for reasons to reject them.

### Lens A, Immune system
- **NO INCREMENT (considered first).**
  - Removing the metaphor words leaves "per-item checks pass, and the aggregate is the problem". That restates the baseline's "each look fine but together... harder to maintain".
  - A reader holding only the baseline would make the same decision.
  - **Firing test met. Status: NO INCREMENT.**
- The other statuses were not reached.

### Lens B, Supply chain
- **NO INCREMENT considered.** "Lots of" and "together" are in the baseline, and I considered whether volume is merely restated. The baseline does not distinguish a volume-driven aggregate from a content-driven aggregate, so the distinction is not a restatement. **NO INCREMENT not licensed.**
- **CONTESTED considered.** Volume and content are competing hypotheses, not conflicting readings of supplied words. No baseline words support the content reading specifically, and it needs imported facts. **Rejected.**
- **UNKNOWN considered.** The measure of "harder to maintain" is a named missing fact. It blocks testing the question, but it does not block stating the question or naming the decision. **Not required.**
- **RELATED (considered last).**
  - **Question:** does the maintenance difficulty track volume merged relative to maintainer capacity, or a property that the merged pull requests share?
  - **Decision a reader could change:** which of two investigations to start first, a count and rate analysis of merged pull requests against maintainer time, or a content review of what the merged pull requests have in common. The project's own history holds the information. This is the decision, not a recommendation.
  - **Firing test met. Status: RELATED.**

### Lens C, Jazz improvisation
- **NO INCREMENT considered.** Removing the metaphor leaves a candidate mechanism, unwritten conventions that drive-by contributors do not follow. The baseline does not contain this. It is not a restatement. It does import a fact (that such conventions exist), so this is a narrow call. **NO INCREMENT not licensed.**
- **CONTESTED considered.** There is no second plausible interpretation of baseline words that conflicts with this one. **Rejected.**
- **UNKNOWN considered.** The question has no content if the project has no identifiable shared conventions. A missing fact blocks classification: whether the project has conventions, written or unwritten, that drive-by pull requests could diverge from, and what they are. **Supported.**
- **RELATED (considered last).** The question is stated above. The decision is whether to examine documented versus undocumented conventions as a source of the difficulty. That is also arguably supported.
- **Preserved disagreement.** The method says UNKNOWN is considered before RELATED but does not settle ties. I assign **UNKNOWN** and preserve that RELATED is also supported.

**NO INCREMENT count: 1** (Lens A). Lenses B and C received other statuses. Two named lenses were not evaluated (see Step 2) and are not counted.

Because the count is not zero, the per-lens "decision changed" sentences are not required by the method.

**Falsifiability check at grading**
- Lens A: the named relationship adds nothing beyond the baseline.
- Lens B: the analogue depends on missing definitions of difficulty, volume, and capacity. The observable result bears on the mapping only once those are defined.
- Lens C: the analogue depends on a missing convention set and on an imported assumption. The observable result bears on the mapping only once those are defined.
- No proposed test is established as passed.

---

## Step 7. Cross-lens synthesis and disposition

**Merged observations**
- Lenses B and C both locate the problem at the gap between per-item acceptability and aggregate state. That is the baseline itself, so the overlap is not independent support and is not verification.
- The disagreement is preserved. Lens B frames the aggregate effect as a volume and capacity relationship, or a shared-content one. Lens C frames it as divergence from conventions that may not exist. These are not forced into consensus, and nothing here shows they are exclusive.

**Number of NO INCREMENT lenses: 1.** It appears only in this count and in no disposition list.

### KEEP EXPLORING
- **Candidate (Lens B, supply chain):** is the maintenance difficulty tied to merged-pull-request volume relative to maintainer capacity, or to a property the merged pull requests share, or both?
  - **Relationship:** pull-request arrival and merge rate versus maintainers' integration capacity, and versus a shared content property.
  - **Computational analogue (proposed):** a queue with arrivals, a capacity, and a residue of unabsorbed work. It is not a completed crosswalk, because its parameters are missing.
  - **Observable result:** the relationship of a defined maintenance-difficulty measure to merged volume over time, versus its relationship to a shared content property.
  - **Missing information carried forward:** the definition of "harder to maintain", the unit and window for volume, the capacity measure, and the pull-request population (merged or opened).

### HOLD AS UNKNOWN
- **Candidate (Lens C, jazz improvisation):** do drive-by pull requests diverge from conventions that are not documented?
  - **Missing context:** whether the project has such conventions, what they are, and how drive-by is defined. A graded disagreement (RELATED also supported) is preserved.
  - **Relationship:** local fit versus fit with a convention set.
  - **Computational analogue (proposed, incomplete):** a conformance check against a convention set that is not specified.
  - **Observable result:** whether drive-by and regular-contributor pull requests differ on a defined convention set. This is unavailable until the set and the conformance rule are defined.

### DISCARDED METAPHOR
- None. Lens A was graded NO INCREMENT, not misleading. Per the method, an unhelpful lens is not thereby a misleading one.

**Entries removed for lacking a lens:** none.

OpenMirror does not run these tests. Both candidates pass to a research or domain workflow with their falsification conditions attached.

---

# REPLICATOR NOTES

1. **More than three named lenses.** The method says to expose the gap, but it also requires me to proceed. I invented the "first three in the user's order" rule to continue. This is a rule I made up and is exactly what the text warns against doing silently. I flagged it, but the method does not say what to do instead of picking.
2. **Unevaluated lenses have no home.** Plate tectonics and parliamentary procedure fit none of the four statuses, the three dispositions, or the NO INCREMENT count. I reported them as "not evaluated". The method has no category for this.
3. **No question in the case.** The case is a problem statement, and Step 1's "If the baseline already answers the question" assumes a question exists. I treated it as "no answer, continue".
4. **"Computational analogue" is undefined.** Every falsifiability field asks for one. The user supplied none, and the method does not say whether to propose one or leave it blank. I proposed lightweight ones (queue, per-item check versus state monitor, conformance check) and labelled them as proposals. This may violate the "do not add theory" spirit of Step 1, but those fields come in later steps.
5. **Tension in Step 4.** The method requires "the observable result that would break the mapping". It also forbids a falsifier that supplies a missing rule or a conditional falsifier for undefined behavior. Because "harder to maintain" is undefined, I could not state any threshold or direction. I named the comparison and listed missing definitions. A reader may fairly say this is not a falsifier at all.
6. **Ordering.** The method says to write the literal return before grading, but also says the break point is written "before assigning a status". Step 5's literal return comes after Step 4's break point. I followed the numbered order, with the grading last.
7. **UNKNOWN versus RELATED ordering.** The method says RELATED goes last, but ties are explicitly unresolved. For Lens C both seemed supported. I assigned UNKNOWN by the ordering and preserved RELATED, but the disposition list wants one entry, so I picked HOLD AS UNKNOWN.
8. **The NO INCREMENT call on Lens C was marginal.** Whether a candidate mechanism built on an imported fact (unwritten conventions) "restates the baseline" is a judgement call. Reasonable graders could disagree.
9. **What "readily available information" means for RELATED.** I used "the project's own history" as information already held by the user. Naming a "decision a reader could change" comes close to recommending action. I described the decision without recommending, but the line is thin.
10. **Whether "volume versus content" is genuinely distinct from the baseline.** I judged it was, but a strict reader could say "lots of... together" already encodes both.
11. **"Drive-by" is undefined.** I recorded it as an assumption. The method gives no rule on how much definition-supplying is allowed at Step 1.
12. **Imported vocabulary.** For supply chain, terms like bottleneck and inventory are imported but needed. The method says to define terms that change interpretation. I defined a few inline and treated the rest as vocabulary.
13. **The immune lens grading required judging "restates baseline".** I said the literal return restated the baseline, which also meant I did not need to list its imported biology mechanisms. I noted them in Step 4 only.
14. **The "decision changed" sentences.** These were not required because the NO INCREMENT count was one. I did not write them. Under a count of zero they would have been mandatory.
