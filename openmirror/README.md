# Open Mirror

**Borrow a picture to understand something hard. Then put the picture down.**

Open Mirror is a written procedure for using metaphors without being fooled by them. You bring a topic, a claim, or a passage. It restates what you brought in plain words, looks at it through up to three borrowed pictures, marks exactly where each picture stops fitting, and hands back only what survives in plain language.

It works in two directions:

- **Complex to simple.** A technical passage comes back as a plain restatement plus a picture that helps a newcomer hold it, with the places the picture lies clearly marked.
- **Simple to complex.** A comparison you already use ("the body is like a garden", "sleep is like a bank account") gets tested against the real thing, and you find out what it was quietly adding.

Most pictures do not survive. Finding nothing is a valid result, and the procedure says so out loud.

## Try it in thirty seconds

Paste the copy-paste version from [SKILL.md](SKILL.md#copy-paste-version) into any AI assistant, or install the skill and type:

    Open Mirror: [your topic]

## What you get back

1. A plain-language baseline of what you supplied, with nothing added.
2. One to three lens maps: what maps to what, and where the picture breaks.
3. A grading pass that counts how many lenses added nothing.
4. Three lists: keep exploring, hold as unknown, discarded metaphor. Any may be empty.

## What it is not

- Not a fact checker. It never verifies anything.
- Not a decision maker. It ends at three lists.
- Not a claim that metaphors prove things. They raise questions; they do not answer them.

## Files

| File | What it is |
|---|---|
| [SKILL.md](SKILL.md) | The method, v1.4.3 (Ed's plain-language draft plus the round-2 and explanation-mode fixes). Install this as a skill or paste the prompt from it. |
| `drafts/` | The longer first v1.4 draft, kept for comparison. Superseded; do not copy from it. |
| [CLAIMS.md](CLAIMS.md), [MANIFEST.json](MANIFEST.json), [verify.py](verify.py) | The claims register, file hashes, and the script that regenerates both from the raw records. Run `python verify.py`. |

**Which copy of the skill to use.** Only `SKILL.md` is current. The evidence folders contain older copies on purpose, because they are what was tested: `evidence/red-team-2026-10-06/00-method-packet-given-to-replicators.md` is the v1.3 method text, `evidence/red-team-2026-10-06-r2/00-method-packet-given-to-replicators.md` is v1.4.1, and `evidence/red-team-2026-10-06-r2/00b-method-packet-explanation-rerun.md` is a v1.4.3 draft with a v1.4.2 footer. None of those is the skill. Do not copy from them.
| [CHANGELOG.md](CHANGELOG.md) | Every version, including what was tested and what was not. |
| [RED-TEAM-REPORT.md](RED-TEAM-REPORT.md) | October 2026 coherence and functionality review of v1.3, with five live test runs. |
| [RED-TEAM-REPORT-R2.md](RED-TEAM-REPORT-R2.md) | Round 2: the same five cases on v1.4.1, second model. Scorecard and what the repairs did. |
| [COHERENCE-STUDY.md](COHERENCE-STUDY.md) | One exact process written in ten analogies, worked by blind operators. Where coherence held, where it broke, and what the pre-read changed. Includes what went wrong and what it cost. |
| `evidence/` | The v1.0 through v1.3 documents and the full evaluation record (eight model sessions, adversarial review, lexicon review, retained failures). |

## Evidence, honestly

Versions 1.2 and 1.3 were evaluated in eight fresh model sessions across six fixed cases, with a separate adversarial reviewer and a separate vocabulary checker. The written-conformance record was 34 of 48 case judgments met in the first round and 41 of 48 after five repairs. The grading step was where most failures happened. The full record, including reviewer corrections and the builder's own logged failure, is in `evidence/`. These are judgments about written outputs, not a reliability guarantee.

Version 1.4 (this repository) is a plain-language rebuild for sharing. Its v1.4.1 text was run blind on five fixed cases on two Claude models, one round each ([RED-TEAM-REPORT.md](RED-TEAM-REPORT.md) on the v1.3 text, [RED-TEAM-REPORT-R2.md](RED-TEAM-REPORT-R2.md) on v1.4.1). Every step-level criterion passed in round 2; one shared gap was found and closed in v1.4.2. Explanation mode was then rewritten and rerun once on its test case. The remaining v1.4.2 and v1.4.3 wording is untested.

A separate coherence study ([COHERENCE-STUDY.md](COHERENCE-STUDY.md)) put one exact process into ten analogies and had 60 blind operators execute it. Complete documents were read correctly 30 of 30 times; compressed write-ups 25 of 30, with all five failures caused by one ambiguous rounding sentence. **Model operators executing a fixed numerical procedure from analogical documents, with scripts, got no measurable benefit from the pre-read: no more accurate, no more gaps flagged.** That is a null result inside that scope. The study did not test a person using Open Mirror to inspect an argument made through metaphor, which is the skill's stated purpose.

The next day's study ([TRANSFORMATION-STUDY.md](TRANSFORMATION-STUDY.md)) moved the skill to the writer's side. Writers who ran it on their own 400-word analogies before handing them over produced ten analogies that fourteen blind readers executed with zero drift, 14 of 14 exact by the engine, including 6 of 6 on the two analogies that had failed 5 of 6 times without the discipline. A control run the same afternoon then replaced the skill with one sentence, "review your explanation against the engineer's process and fix what you find", on the two analogies that had drifted: 12 of 12 exact. **So far, Open Mirror has not been shown to beat a plain review instruction on any task tested.** The zero-drift result is real and repeatable; the skill's seven steps are not what produced it. All Claude and GPT runs so far are one provider each; no cross-provider replication has been done on the same text.

## Installing as a skill

Copy the `openmirror` folder into your skills directory (for Claude Code: `~/.claude/skills/open-mirror/`). The `SKILL.md` frontmatter makes it discoverable by its description.

## Credits

Concept and research direction: Jake Tiller. Drafting and evaluation assisted by OpenAI Codex and Claude across versions; see the changelog for who did what.

**License: not yet chosen.** Earlier versions say "intended for open educational reuse" and defer to a repository license that was never written. The author's other public work uses CC BY 4.0. Until a `LICENSE` file is added, treat this as all rights reserved.
