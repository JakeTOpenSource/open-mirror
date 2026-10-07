# Changelog

Newest first. Each entry says what was tested and what was not. Earlier entries are reproduced from the source documents in `evidence/` with their original wording; where that wording is inconsistent, the inconsistency is noted rather than repaired.

## Evidence note — 2026-10-07 — transformation study, no text change

Ten writers used the skill's steps 1, 4 and 5 on their own 400-word analogies of the coherence-study process (`TRANSFORMATION-STUDY.md`). Fourteen blind readers then executed them: 14 of 14 exact by the engine, against 25 of 30 for the undisciplined write-ups the day before, and 6 of 6 against 1 of 6 on the two analogies that had drifted. A fixed 23-rule checklist found 226 of 230 rules recoverable against 219. A control the same afternoon replaced the skill with a one-sentence "review against the source and fix" instruction on the two drifting domains: 12 of 12 exact, with the writers catching the halving ambiguity unprompted. Conclusion by the pre-set rule: the active ingredient is a review pass against the source, which the skill contains but does not own. Open Mirror has not yet been shown to beat that sentence on any tested task. No version bump. A pre-registered 250-word test followed (`evidence/transformation-2026-10-07/compression-250/`): skill 3 of 6, one-sentence review 6 of 6, one writer per arm per domain; the skill-arm metallurgy writer detached the rounding from the halving rule and its self-check passed it. Pre-registered reading: the skill's text hurts at that compression. The run was contaminated by the harness relaying the triggering message into every session, which sent writers and readers browsing the repository; one skill-arm writer read the README sentence naming the rounding failure, one generic-arm reader saw the answer in another reader's commit message after computing it, and two readers committed scripts. Audit in `compression-250/AUDIT.md`. The contamination favoured the skill arm. Clean rerun the same evening (`compression-250/PLAN-RERUN.md`, `RESULTS-RERUN.md`): three writers per arm per domain, 48 sessions confined to a scratch folder and audited clean; skill 6 of 6 write-ups clean, one-sentence review 5 of 6; by the pre-registered rule, no separation. The one failure was again a halving rule with the rounding detached from the kept quantity, this time from a generic-arm writer.

**Evidence note, 7 October 2026, function-match test.** Pre-registered (`evidence/function-match-2026-10-07/PLAN.md`), 16 document pairs across unrelated fields built deterministically with single-rule variants from the engine, 2 judges per pair, plain instruction, confined and audited. 32 of 32 verdicts correct, probes engine-verified 32 of 32, hidden breaker differences caught 4 of 4, judge disagreement 0 of 16. Reading by the plan: function matching across lexicons is doable by this method on executable procedures. No skill text involved; no version bump. Candidate text change, untested: a checklist line, "for every rounding, name which quantity is rounded".

## Evidence note — 2026-10-06 — coherence study, no text change

The v1.4.3 pre-read was used by 20 blind model operators executing an exact numerical process from analogical documents, with scripts (`COHERENCE-STUDY.md`). Under those conditions it produced no measurable gain in correctness or in gaps flagged compared with 40 operators who did not run it. The study did not test the skill's stated purpose, inspecting an argument made through metaphor. In the one case where it named the decisive ambiguity in advance, the operator still resolved it wrong. One change is proposed from this, untested: when a flagged gap changes the result, the output should carry both results forward rather than choosing one. No version bump; the text is unchanged.

## v1.4.3 — 2026-10-06 — explanation mode rewritten, rerun once

Both round-2 proposals for explanation mode applied, then the explanation case (T2) rerun once on Claude Opus with the new text as the only input. Rerun transcript: `evidence/red-team-2026-10-06-r2/T2-transformer-explain-rerun-v1.4.3.md`.

Changes to explanation mode:

1. **No stop at step 1.** A request to explain is a request for pictures; run at least one.
2. **Grade against the original passage, not the plain statement.** The step 6 question is whether a newcomer holding only the original could restate it plainly, and whether they could after the picture. The plain statement is part of the explanation, not a rival to it.
3. **Piles read as Use, Hold, Discard.** Hold only when the picture can't help until a named fact is known; an open question the picture merely raises is not a reason to hold it.
4. The changed-decision sentence is replaced by one sentence saying what the reader can now restate.
5. Step 4 still compares against the plain statement; only the step 6 test uses the original.
6. Output order fixed: reader's part first (plain statement, Use pictures with break points, original word for word), then the working under its own heading.

Rerun result: mode declared, no stop at step 1, two pictures in Use with break points (library with soft borrowing; weighted class grade), spotlight discarded for contradicting "every other token" and "mix", original appended. Adds nothing: 0 of 3. Misleading: 1. Items 3 to 6 above were folded in from the rerun's notes afterwards and are untested. The rerun packet's footer still said v1.4.2; the replicator noticed, which is the kind of thing the method is for.

## v1.4.2 — 2026-10-06 — wording fixes from round 2, UNTESTED

v1.4.1 was run blind on the same five cases on a second model (Claude Opus; round 1 was Sonnet on v1.3). Report: `RED-TEAM-REPORT-R2.md`. Transcripts: `evidence/red-team-2026-10-06-r2/`. Result: all five runs passed every step criterion; four of five needed one invented rule, and three of them invented the same one. Nine wording fixes applied, none changing a step:

1. Step 4: misleading means the picture **treats** an unsupplied fact as given to reach its conclusion; a picture that only **raises** the fact goes to grading. A guess marked as a guess is not a supplied fact. (N1, the shared seam.)
2. Step 4: a misleading picture skips steps 5 and 6; its break point is its Discard entry. (N10)
3. Step 6: the changed-decision sentence is required for every picture that isn't "adds nothing" **or misleading**. (N3)
4. Step 6: "[total]" is pictures run, including misleading. (N6)
5. Step 6.1: "compare the plain sentence with the plain statement" replaces "strip the picture-words", which step 5 had already done. (N9)
6. Step 1: pull out only a comparison the person is using to argue; a field's term of art is a word, not a picture. (N5)
7. Step 1: the embedded picture does not count against the three. (N7)
8. Mechanism section: "surviving" means in Keep exploring or Hold. (N8)
9. Top of file: say the mode at the top of every run. (N11)

Two author decisions left open, with proposed wording in the report: explanation mode's stop rule and baseline (N2), and whether "Missing a fact" should yield to "Worth exploring" when the question can be stated (N4). Keep exploring was empty in all five runs.

## v1.4.1 — 2026-10-06 — UNTESTED

Plain-language simplification of v1.4 for public use, drafted by Ed. Same seven steps and every v1.4 repair, with the formal labels replaced by plain phrases (Adds nothing, Two readings, Missing a fact, Worth exploring; Keep exploring, Hold, Discard) and "lens" replaced by "picture". Roughly half the length of the first v1.4 draft, which is kept at `drafts/SKILL-v1.4-first-draft.md`.

Seven items from the first draft were restored into Ed's text by Claude, each a sentence or less. Strike any that Ed meant to drop:

1. Step 2: pick pictures that show different things (scale, relationship, pressure). Ed's draft had no distinctness criterion; the T1 run noted the method gives no lens-selection rule.
2. Step 6, Two readings: "if one is plainly weaker, say which survives."
3. Step 6, Worth exploring: "with information they have or could easily get"; "'Should we consider X?' is not a decision"; "a question that only opens more questions adds nothing." These were the v1.1.1 hardening that stopped RELATED from absorbing every lens.
4. Explanation mode: optionally end with the original passage verbatim when the output goes to someone who doesn't have it. Ed's draft said "no extra layers"; this is the one restoration that changes a deliberate choice, and it is the mechanism for the "flip between complex and simple" use. Author decision.
5. Rules: don't look things up, run tools, or check sources because a picture suggested it. Needed when the skill runs inside an agent.
6. Two short worked examples. v1.1 found that a success-only example trained success-shaped output; the finds-nothing example is the stronger of the two.
7. Agent Skills frontmatter, and a one-table crosswalk from the plain labels to the labels used in `evidence/`, so the evaluation record stays readable.

Also: "Not run: k" added to the copy-paste report line to match step 6.

## v1.4 — 2026-10-06 — UNTESTED

Plain-language rebuild of the v1.3 method for public sharing. Drafted by Claude (Fable 5.1) following a red-team review (`RED-TEAM-REPORT.md`) that included five live blind runs of the v1.3 text. No v1.4 run has been made. Every change below is a proposal for the author.

Changes to the method:

- **Added an explanation mode.** When the user asks for an explanation rather than a filter, step 6 uses a restatement test instead of the decision test. Output has three layers: plain baseline, picture with break point, verbatim technical version. Reason: a teaching analogy grades NO INCREMENT by construction under the decision test (red-team F1).
- **Embedded metaphors are split out of the baseline** and graded as lens 1 against the literal statements. Reason: under v1.3's complete-baseline rule, a metaphor the user supplied could never be found misleading (F8).
- **Changed-decision sentence is now required for every lens that is not NO INCREMENT**, not only when the count is zero. Reason: the zero-only rule exempted most lenses from the test that gives the count meaning (C8).
- **Misleading lenses are marked at step 4 and skip grading**, going directly to DISCARDED METAPHOR with their break point as the entry. Reason: v1.3 acknowledged a status gap here and told replicators to expose it; replicators had no way to proceed (F6). This is how v1.1 Example B already handled the ecology lens. No fifth status is added.
- **Status-to-disposition table added** in step 7. Reason: v1.3 never said which status goes to which list (F4).
- **Tie rule:** grading order is precedence, earlier wins, note the later in one line, one count. Reason: v1.3 left ties unsettled and replicators invented reporting conventions (F5).
- **More than three named lenses:** first three in the order given, rest listed as "not run" in the count line. Reason: v1.3 acknowledged this gap; replicators invented this rule anyway (F7).
- **"Computational analogue" renamed "counterpart"** and defined as whatever concrete thing in the real topic plays the role. The three mechanism fields moved to an optional section that runs only when the user brought a mechanism; they are no longer required at every step for every lens. Reason: the phrase distorted lens selection toward computing metaphors and was unfillable for non-engineering topics (F2).
- **Step 4's observable-result requirement moved** to the optional mechanism section. Reason: in step 4 it contradicted the no-conditional-falsifiers rule whenever the baseline defined no outcome (F3).
- **Definition rule stated:** defining a word is not adding a fact; defining it in a way that settles the question is (F9).

Changes to the document:

- Sibling-skill boundary table (clutch, BespokeNode, STP, Thetabase) removed from the skill file. It belongs to the author's own system documentation.
- Vocabulary cut from twenty-three method terms to six. Glossary added.
- Agent Skills frontmatter added so the file installs as a skill.
- Reusable prompt rewritten to match v1.4.
- Worked examples kept from v1.1 and regraded under v1.4 rules.
- Evaluation summary rewritten as one honest paragraph in `README.md`; the full record stays in `evidence/`.

Open author decisions: license; the Jake/Jacob credit; whether the restatement test is the right explanation-mode test; repository name.

## v1.3 — 2026-09-12 — R2 repairs folded into method text

From `evidence/OpenMirror-v1.3 Updated.pdf`. The five owner-approved R2 repairs were folded into the numbered method steps. Per-step changes: complete-baseline sentence added to steps 1 and 6 (R1); "computational counterpart" changed to "computational analogue" (R5); no-conditional-falsifiers sentence added to step 4 (R2); zero-declaration hardened so a missing sentence is a reporting failure (R3); disposition-traceability sentence added to step 7 (R4). A retrospective regrade of the R1 answers under the settled reading is included: 33 met, 15 not met, 0 cannot decide, for owner review.

## v1.2 R2 — 2026-09-12 — Repair repeat

From `evidence/OpenMirror-v1.2-R2-Validation-Addendum.pdf`. Eight fresh sessions, four models (gpt-5.5, gpt-5.6-sol, gpt-5.6-terra, gpt-5.6-luna) twice each, same six cases, candidate with only the five approved repairs. Initial attempts: 41 met, 7 not met, 0 cannot decide, after a reviewer addendum that reconsidered thirteen rows. Three tool-truncation retries reported separately (16 met, 2 not met). Two sessions never received complete input. The document states this is not an overall pass and the score change cannot be attributed to the repairs alone.

## v1.2 R1 — 2026-09-12 — First evaluation

From `evidence/OpenMirror-v1.2-Researcher-Edition.pdf` and the Complete edition. Rebuilt from v1.1 (S1) and the author's interview answers (S2). OVERLAP removed from active statuses, leaving four. Falsifiability triple and twingineering framing added. Eight fresh sessions across four models on six frozen cases. First adversarial review: 42 met, 6 not met. After challenge: 34 met, 13 not met, 1 cannot decide. Grounding case graded UNKNOWN seven times and NO INCREMENT once. Also records a builder conformance failure on the same date: the builder claimed to have presented the lexicon and interview questions when it had not; the user caught it.

## v1.1.2 — UNTESTED (source-reported)

From `evidence/Open-Mirror-v1.1.md`. Hardened the CONTESTED firing test. Flagged OVERLAP as never having fired across roughly 25 lens slots; left as an author decision. Restated the NO INCREMENT disposition rule at point of use.

## v1.1.1 — "TESTED, round 3" (heading) / fixes untested (body)

From `evidence/Open-Mirror-v1.1.md`. The heading and body disagree; both are reproduced as found. Reordered grading so NO INCREMENT is tested first. Hardened the RELATED firing test. Gave NO INCREMENT a home in the disposition, namely none.

## v1.1 — 2026-08-14

From `evidence/Open-Mirror-v1.1.md`. Revised by Claude after an A/B test of v1.0. Removed undefined term ALIAS. Added firing tests to all five statuses. Added the zero declaration. Separated generation from grading. Changed three lenses from floor to ceiling. Added proportionality. Added Example B (the skill finds nothing). Moved break point before status.

## v1.0 — 2026-08-14

From `evidence/Open-Mirror-Skill.pdf`. Original. Concept and research direction by Jake Tiller; drafting and synthesis with OpenAI Codex. Five statuses, three lenses by default, one success example.
