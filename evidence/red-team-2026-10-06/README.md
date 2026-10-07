# Red-team runs, 6 October 2026

Five blind runs of the OpenMirror v1.3 method text. Each run was a fresh Claude Sonnet session (claude-sonnet-5-5, default settings, medium effort not explicitly set) given only `00-method-packet-given-to-replicators.md` and one case, with the instruction to apply the method exactly as written and then append honest "REPLICATOR NOTES" on every ambiguity or invented rule. No other files, no web, no tools beyond reading the packet.

The packet is the v1.3 method text (steps 1 to 7 and the four statuses, from pages 3 to 5 of the v1.3 PDF) plus the v1.1 operating rules. It omits the v1.3 opening, the sibling-skill boundary table, the worked examples, and the evaluation record.

| File | Case | Probe |
|---|---|---|
| T1-procrastination.md | Open topic, no named lenses | Non-engineering input, lens selection, "computational analogue" |
| T2-transformer-explain.md | Technical passage, "explain for a student, then show the technical version" | The explanation use |
| T3-five-lenses.md | Five user-named lenses | The acknowledged >3 gap |
| T4-injection-medical.md | Medical claim with an embedded instruction to the AI | Injection resistance, safety label |
| T5-sleep-debt.md | Two user-named lenses, one misleading, metaphor embedded in the claim | Misleading-lens handling, embedded metaphor |

Transcripts are the replicators' final messages, verbatim. Findings drawn from them are in `../../RED-TEAM-REPORT.md`. These are five sessions on one model; they are diagnostic, not a conformance score.
