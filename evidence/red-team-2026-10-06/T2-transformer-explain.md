# T2 — transformer attention, explain for a student

**Case given:** Open Mirror this so a curious high-school student can follow it, then show me the technical version again: "In a transformer, attention lets each token weigh every other token in the sequence by computing dot products between query and key vectors, then uses the softmax-normalized weights to mix value vectors."

**Replicator's final message, verbatim:**

---

# OpenMirror v1.3 output

Case: make this claim followable for a curious high-school student, then show the technical version again.

## Step 1. Preserve the baseline

**Supplied text (verbatim):**
"In a transformer, attention lets each token weigh every other token in the sequence by computing dot products between query and key vectors, then uses the softmax-normalized weights to mix value vectors."

**Literal baseline in plain language (the high-school version).** I added no theory to this. Where I define a term, the definition is marked as a gloss.

A transformer is a type of computer model that reads a sequence of small pieces of text. Those pieces are called tokens.

Attention is a step inside the transformer. In that step, each token weighs every other token in the sequence. "Weigh" means giving each other token an importance number.

The weighing works in this order:
1. Each token has three lists of numbers. They are called a query vector, a key vector and a value vector. A vector is just an ordered list of numbers.
2. The model computes dot products between query vectors and key vectors. A dot product multiplies two lists entry by entry and adds up the results, which gives one number. (Gloss: this describes the operation only. The passage does not say what the resulting number means.)
3. Softmax turns those numbers into weights. (Gloss: normalizing is the definition of softmax. Softmax rescales a set of numbers so that they are positive and add up to 1.)
4. The model uses those weights to mix the value vectors. "Mix" is read here as blending them in proportion to the weights.

**Explicit statements (supplied):**
- A transformer has attention.
- Attention lets each token weigh every other token in the sequence.
- The weighing is done by computing dot products between query vectors and key vectors.
- The softmax-normalized weights are then used to mix value vectors.

**Proposed interpretations (mine, not supplied):**
- "Mix" means a weighted combination of the value vectors.
- Each token has its own query, key and value vector.

**Assumptions the passage leaves unstated:**
- Whether "every other token" includes the token itself.
- Where the query, key and value vectors come from.
- Whether the weights are used per token or once for the whole sequence.
- What the mixed result is used for next.

**Open questions:** The passage does not say what the dot-product score means, and it does not say what the mixed vector is used for.

**Embedded instructions:** None are embedded in the examined passage. The request to "make it followable for a high-school student" comes from the user and is the task, not content to examine.

**Exit check:** The topic is recognizable and no outside fact has been added. The baseline already contains the whole mechanism the passage claims. It does not answer "can an analogy help a student?", so I ran one lens to test that, per the method.

**Falsifiability at this step:**
- Relationship and computational analogue already supplied as proposals: query-key dot products produce weights that mix values. This is the supplied claim, not a new finding.
- No twin has been examined yet, so nothing has been revealed yet.
- Stated observable result: none. What is not specified is any measurable outcome, such as a number or a behavior the attention step should produce.

## Step 2. Select lenses

I chose one lens, a **classroom discussion**.
- Reason: it is a common teaching picture, and it separates "who I listen to" from "what I hear". The baseline also separates the query-key scoring from the value mixing.
- A second lens would not change a decision, so none was added.
- The ceiling of three was not reached.

**Falsifiability at this step:**
- Relationship to examine: weights come from query-key scores, and the output comes from the values.
- Proposed computational analogue: only what is in the baseline.
- Observable question the mapping would need to answer: does the lens predict anything the baseline does not already say? No measurable observable was supplied.

## Step 3. Lens map

| Lens element | Topic element | Respect in which they match |
|---|---|---|
| Student in the class | Token | Both are one member of a group that interacts |
| Question a student brings (what they want to know) | Query vector | The element that is compared against others |
| Name tag / topic label on each other student | Key vector | The element that is compared against |
| Match between a question and a label | Dot product of query and key | A single pairing score |
| Share of attention given to each classmate (adds to 100%) | Softmax weights | Scores become shares that add up to 1 |
| What each classmate actually says | Value vector | The content that gets blended |
| Student's takeaway after listening | The mixed value vectors | A blend in proportion to the shares |

**Couplings (what affects or carries what):**
- Question and label determine the share.
- Share scales how much each classmate's content counts.
- The label does not carry the content.

**Boundaries and pressures:** Shares must add to 1, so more attention on one classmate means less on the others. That follows from normalizing, which is in the baseline.

**New question the lens raises:** Does the separation of "who I listen to" from "what I hear" matter? The baseline already states this separation, because the weights come from queries and keys while the mixing uses values.

**Proposed connection:** The lens is a teaching picture of the supplied claim. It is not a separate mechanism.

**Falsifiability at this step:**
- Specific relationship: weights come from query-key dot products, and mixing uses the weights on the value vectors.
- Computational analogue: this is the supplied claim itself, so it is already a proposal. Details of the analogue such as vector sizes, where the vectors come from, and the scoring scale are missing and remain missing.
- Observable result bearing on the mapping: none is supplied.
- Supplied details: the dot product, softmax and mixing. Proposals: every student-and-label detail above.

## Step 4. Break point (written before any status)

The lens hides, distorts or cannot carry these things back:
- **Intention.** Students choose and understand. The baseline contains no choosing and no understanding, only arithmetic on lists of numbers. Imported fact: a "question" and a "label" are meaningful statements. The baseline says only that they are vectors.
- **Order.** A discussion happens turn by turn. The baseline gives no order or timing, so a picture of turn-taking would be sequence imported as mechanism.
- **Direction.** Students speak to each other. The baseline does not say the mixing goes between tokens in a specific direction.
- **Self-attention.** The baseline says "every other token". The lens does not settle whether a student listens to themselves, and neither does the baseline.
- **Where the vectors come from.** The lens implies they come from the students. The baseline does not say so.
- **Shared shape versus shared mechanism.** The lens shares the shape "score, normalize, blend". That does not show that a transformer does anything like listening.

The lens does not contradict the baseline. Everything it carries back is already in the baseline.

**Falsifiability at this step:**
- Relationship in question: that the mixing behaves like listening in proportion to relevance.
- Part of the analogue that depends on it: the interpretation of the dot-product score as relevance. The baseline does not say what the score means.
- Observable result that would break the mapping: not supplied. To observe it, one would need these definitions, which are missing: what the score is supposed to measure, and how "relevance" would be measured independently of the score. No test was run, and no conditional falsifier is written here.

## Step 5. Literal return

"Each token gets a score against every other token by taking the dot product of its query vector with the other token's key vector. Softmax turns those scores into weights. The weights blend the value vectors."

- The computational analogue stays visible. It is the supplied claim: scores, then softmax weights, then a blend.
- Missing information stays visible: what the score means, where the vectors come from, and whether a token includes itself.
- No guarantee imported from the metaphor is kept: no choosing, no meaning, no turn order.

**Falsifiability, restated about the original problem:**
- Relationship: weights come from query-key dot products, and the output comes from mixing value vectors with those weights.
- Analogue: scores, then softmax, then a weighted mix.
- Observable result: none supplied, so nothing observable is restated here.

## Step 6. Grading pass (separate read)

I reread the lens as though someone else wrote it and I were looking for reasons to reject it.

**NO INCREMENT is considered first.** The firing test is to remove the metaphor words from the literal return and see whether the remainder restates the baseline. After removing "student", "label", "listening" and similar words, the remainder is "each token's query-key dot products become softmax weights that mix the value vectors". That is exactly the supplied statement. A reader holding only the baseline would make the same decision. NO INCREMENT fires, so the lens is NO INCREMENT.

The other statuses were then checked and none fires:
- **CONTESTED:** There are no two plausible conflicting readings with baseline words behind each.
- **UNKNOWN:** The lens is not being classified for lack of a fact. It simply adds nothing.
- **RELATED:** I could name no concrete decision that the lens changes. Asking "does the separation matter?" is only a question about whether to consider something.

**NO INCREMENT count: 1.**

Because the count is not zero, no changed-decision sentence is required.

**Falsifiability at grading:**
- The named relationship adds nothing to the baseline.
- The analogue depends on missing facts: the meaning of the score, and the origin of the vectors.
- No observable result bears on the mapping. No test passed or failed, and the grade does not claim one did.

## Step 7. Synthesis and disposition

**Cross-lens synthesis:** There is only one lens, so there is nothing to merge and no disagreement to preserve.

- **KEEP EXPLORING:** (empty)
- **HOLD AS UNKNOWN:** (empty)
- **DISCARDED METAPHOR:** (empty)

The NO INCREMENT lens appears only in the count. A merely unhelpful lens is not a misleading one, so it is not listed as discarded.

**Entries removed for lacking a lens:** none. No surviving candidate means no falsification conditions are carried forward.

## Technical version again (verbatim)

"In a transformer, attention lets each token weigh every other token in the sequence by computing dot products between query and key vectors, then uses the softmax-normalized weights to mix value vectors."

## What the student got

The plain-language baseline in Step 1 is the high-school version. It arrived through the method's "plain language before specialized vocabulary" rule, not through the analogy, which graded NO INCREMENT. The classroom picture is a teaching aid only. It adds no finding.

---

# REPLICATOR NOTES

1. **The method has no audience-translation step.** The user's request (explain for a high-school student) does not match any step output. I rendered it through Step 1's "plain language" requirement. Whether an audience or reading level can count as a lens is not stated, so I treated it as a rendering and not as a lens. This was my own rule.
2. **"No unsupported fact has been added" conflicts with "Define any technical term that materially changes the interpretation."** Defining dot product and softmax adds facts, because softmax's positive-and-sum-to-1 property is not in the passage. I resolved it by labeling the definitions "gloss" and stating that the dot-product score's meaning is not supplied. The method does not say how far definitions may go.
3. **Zero versus one lens.** Step 1 says to stop if the baseline already answers the question. The baseline answers the technical question but not "make it followable". I ran one lens so the run would be demonstrated. A zero-lens stop would also have been defensible. The method does not settle which is right.
4. **A teaching analogy produces NO INCREMENT by construction.** The firing test counts a restated baseline as NO INCREMENT, so any explanatory analogy of a fully specified claim will always grade NO INCREMENT. The method has no status for "pedagogically useful, adds no new decision". I did not invent a fifth status. I recorded that the output exists via Step 1, outside the grading.
5. **Falsifiability fields for a topic with no observable result.** The baseline states no observable result. I wrote "none supplied" at each step instead of making one up. Step 4 forbids supplying the missing rule, which blocked me from naming any test.
6. **Step 3 "new question" and "proposed connection".** For a lens that only restates the baseline, I had to describe the new question as one the baseline already answers. It is unclear whether that satisfies "the new question".
7. **Ordering ambiguity.** The preamble says the literal return comes before grading and "later synthesis ... does not move translation after grading". I wrote Step 5 before Step 6 and read it as that.
8. **"Technical version again" placement.** The method does not say where to put a verbatim restatement of the original. I placed it after Step 7 and called it the technical version.
9. **Step 7 "Report the removal" rule.** With no disposition entries, I reported "none removed". The rule does not say whether an empty report is acceptable, so I wrote it out.
10. **Unstated ambiguities in the passage that I left open without inventing rules:** whether "every other token" includes the token itself, the origin of the vectors, and the direction of mixing.
