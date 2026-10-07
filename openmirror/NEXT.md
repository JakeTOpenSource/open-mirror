# Next tests, not yet run

Recorded 7 October 2026. Jake is low on budget; nothing below runs until he says go, and each run states its cost first.

## 1. Human-proxy readback test (the central claim)

**Question.** When a model explains a real tool output or test result through Open Mirror, can a reader who sees only the explanation answer what the person would need to know: what passed, what failed, what changed, what is unknown, what to do next? Does the picture help beyond the plain statement?

**Design, to be pre-registered before running.** Collect 10 to 15 real tool outputs and test results from Jake's own sessions (raw text, no secrets). For each, two explanations: one with the skill in explanation mode, one with a plain "summarise this for the user" instruction. Blind readers, told they are the user, see one explanation and never the raw output; they answer a fixed question list. Score answers against the raw output by a grader that sees both. Secondary: a readback list check, whether every fact the explanation's own readback list names is recoverable by the reader.

**Cost estimate.** 30 to 40 Opus sessions, about 2.5M tokens. Confine every session to a scratch folder and audit transcripts, as in the clean 250-word rerun.

**Why it matters.** Every result so far has model readers executing a procedure. This is the first test of the skill's stated purpose: accessibility for a person.

## 2. Function match on non-executable theories

Same two-route method, applied to pairs of descriptions that cannot be run (two explanations of a mechanism, two policies, two designs), where only the correspondence route exists. Needs a key built by hand. Smaller: 8 pairs, 2 judges, about 1.2M.

## 3. Open decisions, no tokens needed

License; the Jake/Jacob credit line; repository name; whether "Hold" absorbs "Missing a fact"; the carry-both-results rule; whether the skill text should state its own evidence; adding function match as a third mode and the two rules named in `ARCHITECTURE.md` to the skill text (a v1.5 candidate, to be red-teamed before use).
