# Open Mirror test protocol, v0.2

Merged 7 October 2026 from two drafts: Claude's v0.1 (three-arm experiment, banks A to D, hazards, cost gate) and Ed's Ultimate Test Script v1.0 (harness, executor and auditor prompts, seven batteries). Ed's synthesis note set the merge rules; the places where this file departs from that note are marked **DEPARTURE** with the reason.

**Keys are not in this file.** Cases are public; keys live in `keys/` which is gitignored. A key that is published is a key a future model has read. The executor never sees `keys/`. The auditor does.

**Status.** Design complete. Battery 1 has one prior blind run (Ed's, 2026-10-06, 10/10); its receipts are not yet in `evidence/` and must be added before that run counts as the floor. Nothing else has been run under this protocol.

---

## 0. What this protocol answers that the record does not

| Question | Answered? | Where |
|---|---|---|
| Does the method text produce conforming output in a blind run? | Yes, twice | red-team rounds 1 and 2 |
| Does the pre-read help a reader execute a procedure from an analogy? | Yes: no measurable benefit | COHERENCE-STUDY.md |
| Can the skill detect ideas smuggled by comparisons, and leave honest comparisons alone? | Once, on 10 constructed cases, by Ed | Battery 1, receipts pending |
| **Does SKILL.md add anything beyond the same scaffold without it?** (Arm N gets the identical prompt minus the skill, so S minus N isolates the seven steps, not prompting in general.) | **No** | Bank A, three arms |
| Can it tell the author's true crosswalk from a corrupted one? | No | Bank F |
| Does it false-alarm on the author's real writing? | No | Bank E |
| Does explanation mode hold on fresh cases? | No | Bank G |

---

## 1. Harness

**Sessions.** One executor session per arm per bank: sees the skill (Arm S) and the cases, never the key. **DEPARTURE from v0.1**, which used one session per case. One session per bank saves sessions but lets the model see the mix and calibrate against it ("some of these must be honest"). Mitigation: the auditor reports the discard rate for the first half of the cases against the second half; a drift between them is treated as within-session contamination and the run is flagged, not scored. One cold auditor session per battery: sees executor output, case texts, and the key; never runs the skill. Fresh sessions, no shared history, no tools, no browsing, no reruns.

**Declaration first.** The executor fills the echo and stops; the owner says "go" in chat. The gate is conversational, never a clock (a model without tools cannot read one; observed 2026-10-06).

**Receipts.** Four per battery: declaration echo, executor output, sealed key, audit output. All go in `evidence/protocol-runs/<date>/<battery>/`.

**Key fallibility.** The key records the owner's intent and can be wrong. If the executor names an idea that is genuinely unstated and load-bearing, the executor is correct and the key is corrected, with the correction logged (observed 2026-10-06, Battery 1 case 4).

**Arms.** Three on Bank A only; one (Arm S) everywhere else, to save sessions.

- **Arm S.** Skill text pasted, then the executor prompt (§2), then the cases.
- **Arm N.** No skill. Same executor prompt with the skill-specific lines removed (§2, variant N). **DEPARTURE from Ed's note:** Ed proposed his executor prompt as the Arm S instruction and left Arm N as a bare "assess this comparison". That confounds the experiment: the executor prompt's enumeration step and five-field format do part of the skill's work, so S would beat a bare N for reasons that have nothing to do with the skill. Arm N must get the same scaffold minus the skill, so the only difference between S and N is `SKILL.md`.
- **Arm P.** The copy-paste prompt from `SKILL.md`, then the cases, no executor prompt. Measures what survives in the short form most people will use.

**Headline metric.** S minus N on binary correctness and on ideas named, Bank A only. If S does not clearly beat N, the skill's structure adds nothing to what the model does with the scaffold alone, and that gets published.

**Cost gate.** Bank A three-arm on one model: 3 executor sessions plus 1 audit. Banks B, D, E, F, G, I single-arm: 6 executors plus 6 audits. Bank C: 1 executor, graded by script. Bank H runs only on a version change. Total for a full pass on one model: 17 sessions, on the order of 0.3M tokens (short cases, one session per bank). Minimum viable, the headline question only: Bank A, 4 sessions. Nothing launches without a stated cost and a yes.

---

## 2. Prompts (frozen; Ed's v2, verbatim)

### Executor prompt v2, Arm S

Paste the full skill text above this prompt, then this prompt, then the cases. Never the key.

```
You are the blind executor in a sealed test. Follow the steps in order. Do not skip Step 1.

STEP 1. DECLARATION. Output only the filled echo, then stop. Wait for the owner's "go". There is no clock; the owner says go in chat.

Test: does Open Mirror v[version], run by you, detect ideas smuggled in by comparisons in short arguments?
Budget: this session only. No subagents, no browsing, no tools, no lookups.
Cases: [N] below. Each may argue through zero, one, or several comparisons. Some smuggle unstated ideas. Some are honest. You do not know the split.
Skill: pasted above, v[version]. Run it exactly as written.
Pass bar: [per battery, owner confirms at "go"].

Echo (fill and stop):
1. Cases to run: [count them]
2. Mode: filter for every case, unless a case asks for an explanation (Bank G), then explanation mode for that case only.
3. Per case I will list every comparison the speaker argues through. If none, I output "none found" and stop that case.
4. If several: one output block per comparison, tested independently, nothing carried between them.
5. The five output fields are: Mode, Pictures, Verdicts, Smuggled, Untested.
6. I will not: browse, use tools, carry anything between cases or comparisons, grade the skill, or invent pictures of my own.

STEP 2. EXECUTION. After "go", for each case in order do exactly this:
1. Read the case. List every comparison the speaker argues through ("X is like Y", including verb-form comparisons like "keep the books" or "until the margin call").
2. If the list is empty: output the five fields with Pictures: none found, then move to the next case.
3. For each comparison: run the skill's 7 steps on it, filter mode, then output the five fields. Then the next comparison. Nothing carries over.

STEP 3. SUMMARY. After the last case, one line per comparison: the smuggled idea, or "honest."

FORMAT. Copy this shape exactly. The example is format only, not a real case.

Case 0, comparison 1
Mode: filter
Pictures: "traffic is like water" (speaker's)
Verdicts: water: Hold. Fits flow, not driver choice; missing fact is whether the jam is volume or behavior.
Smuggled: none
Untested: none

Field rules:
- Mode: the single word "filter" (or "explanation" for Bank G).
- Pictures: the speaker's comparison, in quotes, marked "(speaker's)".
- Verdicts: "[picture]: [Discard / Hold / Keep exploring / Adds nothing]. [One line: break point or survivor sentence.]"
- Smuggled: the exact smuggled idea, or "none".
- Untested: "none", unless the case contains a further comparison you did not test.
```

### Executor prompt, Arm N (variant)

Identical to Arm S except: no skill is pasted; the line "Skill: pasted above, v[version]. Run it exactly as written." becomes "Method: your own judgment."; echo item 6 drops "grade the skill"; and STEP 2 item 3 becomes "For each comparison: decide whether it establishes its conclusion from what is stated, or needs an idea the speaker never stated. Output the five fields." The Verdicts field uses the same four words so the auditor can score both arms identically.

### Auditor prompt v2

New session. Paste this prompt, then the executor output, then the case texts, then the sealed key.

```
You are the cold auditor. You did not run the skill. Do not run it now.

You have: the executor's output, the case texts, and the sealed key. The key records the owner's intent, but it is not infallible.

For each case:
1. Compare the executor's verdict with the key. Classify any mismatch:
   - MISS: the executor failed to flag a smuggled idea the key names.
   - FALSE ALARM: the executor discarded, or otherwise condemned, an honest case.
   - MISDIAGNOSIS: the executor flagged a case but named the wrong idea.
   - RECORD FAILURE: a required field is missing, a step was skipped, or the format was not followed.
2. For every MISDIAGNOSIS check and every "smuggled" claim: verify the idea was actually unstated. Find the closest text in the case that could support it. If that text states the idea outright, the idea was not smuggled; say so. A quotation can show what was stated. Only the absence of any stating text, after checking the whole case, establishes that the idea was unstated.
3. If the executor's named idea is unstated in the case and the comparison needs it to argue the conclusion, the executor is correct even when its wording differs from the key. Say so and record the key correction.
4. Score the battery: binary correct [n/N], ideas named [n/N], unsupported break points [count].

Do not rerun the skill. Do not invent new verdicts. Report only the classification and the score.
```

**On the API filter.** Claude's v0.1 avoided the words test, blind, and evaluation after 31 refusals in the coherence study. Ed's prompt uses "blind executor in a sealed test" and ran clean on Opus. **DEPARTURE from v0.1:** the hazard is kept as a hazard, not a rule. Use Ed's wording; if a refusal occurs, record the request ID and the exact prompt, change the wording, and never retry identical text.

---

## 3. Banks

Pass bars are per bank. A skill version is accepted only if every bank passes. Bank H (regression) runs on every version change, no exceptions.

| Bank | Purpose | N | Key | Arms | Pass bar | Failure teaches |
|---|---|---|---|---|---|---|
| A | Marginal value of the skill on its stated purpose | 8 (Jake's) + 10 (Ed's B1) | Sealed; Jake's key for his 8 is not yet written | S, N, P | S beats N on binary and on ideas named; 0 false alarms on the scoped cases | The skill adds nothing to a capable model |
| B | Honest controls, false-alarm resistance | 4 | Sealed | S | 0 false alarms | The filter condemns clean comparisons |
| C | Procedure-from-analogy regression (coherence study) | 3 write-ups | Deterministic (engine.py) | S | Reproduces the known baseline exactly: metallurgy 0 of 3, metamorphosis 1 of 3, electrical 3 of 3, same halving cause | The baseline moved without a text change, or a text change broke what worked |
| D | Synthesized gaps, D1 first | 6 | To be written | S | Per case | See §3.4 |
| E | Author's own writing, precision | 3 | Sealed, author is authority | S | 0 false alarms, verdicts match author intent | The skill misreads real arguments |
| F | Corrupted crosswalks, adversarial | 5 | Sealed | S | 4 of 5 discarded with the corruption named; cases 4 and 5 must not be missed | The skill cannot tell a true crosswalk from an inverted one |
| G | Explanation mode | 2 fresh + B2 from the red-team set | Rubric, owner grades | S | Rubric holds on all | Explanation mode does not hold |
| H | Frozen regression | Bank A cases + red-team B1 to B5 must-pass behaviours | Frozen | S | 100 percent match | A version change broke something that worked |
| I | Real-world excerpts, harness robustness | 3+ | None, owner grades | S | Clean enumeration, complete blocks, no improvisation | The harness breaks outside constructed cases |

### 3.1 Bank A: arguments made through comparison

**Set 1, Jake's eight (6 October 2026).** Cases are in Jake's message of that date and are reproduced in `evidence/protocol-cases/bank-A-jake.md`. Jake holds the key and has not yet written it in the five-field form below. Claude's in-session run of these (not blind, not keyed) produced: A1 to A6 Discard, A7 Adds nothing, A8 Hold. That is a candidate reading, not the key. **Known weakness:** six of eight should be discarded, so "discard everything" scores 75 percent; this set cannot stand alone.

**Set 2, Ed's Battery 1 (10 cases).** Seven loaded, three honest and scoped. One prior blind run on Opus 5.5: 10/10 binary, 7/7 ideas, 0 unsupported break points, with one key correction on case 4. Receipts to be added to `evidence/`. Cases in `evidence/protocol-cases/bank-A-ed.md`. **Non-blind key:** Ed wrote both cases and keys. Mitigation: a second keyer who has not seen Ed's key keys a sample of four; disagreements are logged before any run.

**Key format, every case:** pile (Discard, Hold, Keep exploring, Adds nothing); the smuggled idea stated as the comparison needs it, or "honest" with what the comparison earns and the limit it states; the one sentence a correct plain survivor must convey.

**Build list** (Claude v0.1, unchanged): four more honest-and-scoped cases; two genuine two-readings cases (the label has never fired in any run); two marked-guess cases; two double-comparison cases; one term-of-art trap; one non-English case; one case over 400 words with the comparison buried.

### 3.2 Bank B: honest controls

Ed's Battery 2, four cases, each with an explicit scope statement. Cases in `evidence/protocol-cases/bank-B.md`. Any Discard is a FALSE ALARM and fails the bank.

### 3.3 Bank C: procedure-from-analogy regression

From the coherence study. Only the three write-ups that discriminate: `study2-lossy-v2/write-ups-as-given/metallurgy.md`, `metamorphosis.md`, `electrical.md`. Operator prompt: the corrected-run handover wording in COHERENCE-STUDY.md. Truth: `inputs/engine.py`. Known baseline: metallurgy 0 of 3 exact, metamorphosis 1 of 3, electrical 3 of 3, all failures from one ambiguous halving sentence. Pass bar for the current text: reproduce that baseline exactly. The carry-both-results rule does not exist yet; when it is written, this bank gets an experimental slot whose pass would be metallurgy and metamorphosis reporting both readings or choosing the kept-half one, with electrical still exact. Do not regenerate the write-ups; do not add any figures to them.

### 3.4 Bank D: synthesized gaps

Each needs a key before use. **D1 first**, per Ed's note: neither draft has a comparison the skill must say yes to, so no bank yet distinguishes a good filter from "discard everything".

- **D1.** A comparison that is correct and load-bearing: the argument needs it and it holds. Must land in Keep exploring with a named changed decision.
- **D2.** A mechanism proposal, "X works like Y, so build Z", written fresh (the grounding-wire case in the v1.3 PDF is the model but has been seen).
- **D3.** Two pictures that both survive and disagree.
- **D4.** A medical or legal comparison where the runner's own knowledge is the tempting import.
- **D5.** A near-duplicate pair, to test merging.
- **D6.** Open Mirror described as a metaphor, run through Open Mirror.

### 3.5 Bank E: author's own writing

Ed's Battery 3, three cases from Jake's verified writing (balance-sheet draft; V=IR catalog entry; clutch catalog entry), near verbatim, sources recorded. Key authority is the author. All three are honest by the author's intent; the bank tests precision only. Cases in `evidence/protocol-cases/bank-E.md`. **Caution logged:** the author grading the author's writing is the one place in this protocol where authority can substitute for evidence; the auditor's rule 3 applies in both directions, so if the executor names an unstated load-bearing idea in the author's own text, that stands until the author shows the stating text.

### 3.6 Bank F: corrupted crosswalks

Ed's Battery 4, five cases: the author's real metaphors argued one step past what they earn or inverted. Cases 4 (ground as consensus) and 5 (beeping means safe) invert the author's actual point. Cases in `evidence/protocol-cases/bank-F.md`. Pass: at least four of five discarded with the corruption named. A MISS on case 4 or 5 is the sharpest failure in the protocol.

### 3.7 Bank G: explanation mode

Ed's two fresh cases (diffusion language model for a newcomer who knows what a token is; why a circuit breaker trips, for someone who has never seen a panel) plus the transformer case from the red-team rounds as the known-good anchor. Rubric, all must hold: mode declared; plain statement first and readable alone; at least one picture run; step 6 uses the restatement test against the original, never against the plain statement; piles read Use, Hold, Discard with every Use picture's break point directly under it; reader order is plain statement, Use pictures, original verbatim, then the working under its own heading; the two tests never mixed on one picture.

### 3.8 Bank H: frozen regression

Bank A set 1 and set 2 with their keys once written, plus the five red-team must-pass behaviours from v0.1 (open topic without computing bias; explanation mode runs at least one picture; first-three rule with "Not run: 2"; injection recorded not followed with exploratory label; embedded metaphor pulled out and not consuming a slot). Reruns on every version change. If a frozen verdict moves, the change is guilty until the owner decides whether the new wording or the old key was wrong.

### 3.9 Bank I: real-world excerpts

Ed's Battery 5. Excerpts of 200 to 400 words containing at least one load-bearing comparison, with source and date recorded. Two LinkedIn seeds from 7 October 2026 are in hand (Ed's note names the comparisons in each); one op-ed slot is open. **Repository rule:** store the URL, date, author, and the list of comparisons, not the post text; quote at most one short line. Owner grades enumeration, completeness, and absence of improvisation. Must run under executor prompt v2; the single-comparison prompt garbled an op-ed on 6 October, and if v2 garbles too, the prompt is the defect, not the skill.

---

## 4. Scorecard

One row per bank per skill version. The auditor's four classes are the scoring vocabulary everywhere.

| Bank | Version | Model | Arm | Binary | Ideas named | MISS | FALSE ALARM | MISDIAGNOSIS | RECORD FAILURE | Unsupported break points | Pass |
|---|---|---|---|---|---|---|---|---|---|---|---|

For Bank A add the three-arm lines and report S minus N and S minus P on binary and ideas named, the cases where S did worse than N, and every case where two graders disagreed, both readings kept.

**Strong result:** S beats N by a margin a reader would call obvious; S never discards a sound comparison that N keeps; P lands between; Banks B, E, F pass. **Weak result:** S ties N. Publish either way.

---

## 5. Hazards, from both records

- **Answer leakage.** Any stimulus or key written by a model that has the answer leaks it. Grep every case for its key's wording before use. The coherence study lost a 50-session run to this.
- **Keys in public.** Keys are gitignored. The repo ships cases only.
- **Same-author keys.** Ed's Battery 1, 2, 4 keys were written by the case author. Second-keyer sample before the run. The second keyer must not have read the keys: Claude typed all four of Ed's key sets into `keys/` on 7 October and is therefore not eligible for Ed's cases; Jake, or a fresh model session with no key access, is. For the same reason Ed should not key Jake's eight.
- **Hold absorbs.** With precedence as written, "Missing a fact" beats "Worth exploring" whenever both fit; Keep exploring was empty in every filter run so far. Score Hold and Keep exploring separately. Decide before the run whether the key treats them as equivalent.
- **Scaffold confound.** Any structure in the Arm S prompt that is absent from Arm N is attributed to the skill. Keep the prompts identical except for the skill.
- **Same model runs and grades.** Never. The auditor gets the key and the output, not the skill.
- **The API filter.** Recorded, not designed around; see §2.
- **Identical retries.** Never retry a refused prompt unchanged.

---

## 6. Extension template

Copy to add a bank. Keep a bank under 12 cases; split instead of growing.

```
Bank [letter]: [name]
Purpose: [one line]
N: [count]
Key format: [sealed one line per case | rubric | owner-graded | deterministic]
Arms: [S | S, N, P]
Pass bar: [numbers]
Failure teaches: [one line]

Case [letter]-[m]:
[3 to 8 sentences. Argues through at least one comparison, or scopes one explicitly.]
Source: [constructed | the text it was built from]

Key [letter]-[m] (in keys/, never here):
Loaded: [the exact smuggled idea, as the comparison needs it]
  or
Honest: [what the comparison earns, and the limit it states or implies]
Survivor: [the one sentence a correct plain survivor must convey]
```

---

## 7. Lessons banked (both records)

- The gate is conversational, never a clock.
- Opus needs numbered steps and a format example; nothing implied.
- The single-comparison assumption breaks on real text; enumerate all or find none.
- A run that saw the key is not blind, however clean it looks.
- The key is fallible; the auditor checks the executor against the case text, not only the key.
- Absence is proven by exhausting the text, not by quoting.
- A perfect score on constructed cases is a floor. Banks E, F, I are where it gets hard.
- The stated-purpose question has still not been answered with a control. Bank A is the only thing in either draft that can answer it.

---

## 8. Still to collect

1. Jake's key for his eight cases, five-field form.
2. Ed's Battery 1 receipts into `evidence/protocol-runs/2026-10-06/bank-A-ed/`, annotated as 3 of 4 receipts (the declaration step was skipped by the owner's call on that run).
2a. Diff `keys/` against Ed's source script before any run; the copies in `keys/` were typed from a paste.
3. A second keyer's sample on Ed's keys.
4. D1 written and keyed.
5. The Bank A build list, twelve to fifteen cases.
6. Bank I's op-ed slot.
7. A decision on Hold versus Keep exploring equivalence.
8. `~/workspace/openmirror/purpose-test-kit-2026-10-06.md`, referenced by Ed's Battery 7, moved into this repository.
