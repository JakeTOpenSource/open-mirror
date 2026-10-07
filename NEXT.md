# Next tests, not yet run

Recorded 7 October 2026. Jake is low on budget; nothing below runs until he says go, and each run states its cost first.

## 1. Human-proxy readback test (the central claim)

**Question.** When a model explains a real tool output or test result through Open Mirror, can a reader who sees only the explanation answer what the person would need to know: what passed, what failed, what changed, what is unknown, what to do next? Does the picture help beyond the plain statement?

**Design, to be pre-registered before running.** Collect 10 to 15 real tool outputs and test results from Jake's own sessions (raw text, no secrets). For each, three explanations, three arms: (P) a plain "summarise this for the user" instruction, the control; (S1) the plain statement alone, layer 1 of the skill with no picture; (S2) the plain statement plus one picture with its break point, layers 1 to 3 in explanation mode. The comparison that answers the central claim is S1 against S2: does the picture help beyond the plain statement? P against S1 and S2 says whether the package beats an ordinary summary. Ed's review named this split; without it the run cannot answer the question the project exists to ask. Blind readers, told they are the user, see one explanation and never the raw output; they answer a fixed question list. Score answers against the raw output by a grader that sees both. Secondary: a readback list check, whether every fact the explanation's own readback list names is recoverable by the reader.

**Cost estimate.** Three arms: 45 to 60 Opus sessions, about 3.5M tokens. Two arms (S1 and S2 only): about 2.5M. Confine every session to a scratch folder and audit transcripts, as in the clean 250-word rerun.

**Why it matters.** Every result so far has model readers executing a procedure. This is the first test of the skill's stated purpose: accessibility for a person.

## 2. Separate the review machinery from the sentence

Ed's first point: the evidence proves a review pass, not the skill's elaborate version of it. Two runs (400 and 250 words) put the elaborate version against the one sentence and found no separation. A direct test needs a task where a one-line review plausibly misses what a rule-by-rule check catches: a longer source (20 or more rules), a tighter cap, or sources with several rounding and threshold rules. Design when there is budget; until then the note says the machinery is unproven.

## 3. Function match on non-executable theories

Same two-route method, applied to pairs of descriptions that cannot be run (two explanations of a mechanism, two policies, two designs), where only the correspondence route exists. Needs a key built by hand. Smaller: 8 pairs, 2 judges, about 1.2M.

## 4. Open decisions, no tokens needed

License and repository name: decided, MIT and `open-mirror`, 7 October 2026. Still open: the Jake/Jacob credit line; whether "Hold" absorbs "Missing a fact"; the carry-both-results rule; whether the skill text should state its own evidence; adding function match as a third mode and the two rules named in `ARCHITECTURE.md` to the skill text (a v1.5 candidate, to be red-teamed before use).

## 5. Mode routing, a v1.5 candidate (text only, not yet in the skill)

Drafted from Gemini's proposal of 7 October 2026 with three corrections: the subjective-comparison fallback goes to filter mode, not explanation mode; "executable" is tested operationally rather than by feel; and the triggers are called operational, not deterministic, because two of them are judgments made explicit.

**Step 1. Count.** How many descriptions did the person supply? One: never function match. Two compared against each other: go to step 2. A comparison inside one description ("X is like Y") counts as one description with an embedded picture.

**Step 2. Can both be run?** Try to write each description as a list of rules so that one probe input gives a definite output under each. If both can be written that way, they are executable. If either cannot, they are not. This is the method's own first move, so it costs nothing extra.

**Step 3. What is the verb?** Understand, explain, summarise, report, "what does this mean", a tool output or test result handed to a person: explanation. "Are these the same thing", "equivalent", "two words for one mechanism": function match. "Does this comparison hold", a picture used as a premise or an argument: filter.

**Routes.**
- **Function match** when there are two descriptions, both executable, and the question is whether they compute the same function. Two routes required, table and probe; they must agree or the disagreement is reported.
- **Filter** when a comparison is being used to argue, or when two descriptions are compared and at least one cannot be run. In that second case the correspondence table is the mapping step, and the verdict is marked "not settled by probe".
- **Explanation** when one thing needs to be made plain for a person, including every tool call and test result, and whenever nothing else fires. It is the default.

**Fallbacks.** A request to compare with only one description supplied: explanation mode on what was supplied; do not invent the second. Two triggers firing: run the one the person's verb asks for and say so at the top, as the skill already requires. Medical, legal, financial, security, safety-critical material: keep the mode, label the output exploratory.
