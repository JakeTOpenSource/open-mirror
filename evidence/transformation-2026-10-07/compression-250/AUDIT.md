# Audit of the 250-word run: what the sessions saw that they should not have

Written after the run, from the sixteen session transcripts, before the result was accepted. The transcripts are outside this repository (Claude Code session store, workflow `wf_ff54c9a7-b56`); the per-session facts below are copied from them.

## What went wrong

The workflow harness prepends the user's triggering message to every session it spawns. For this run that message was Jake's "i agree. run it then commit it to the repo. I want it done by the book". The sessions in the two earlier reader runs received "go". Writers and readers in this run took "commit it to the repo" as addressed to them, and the sessions were started with the repository as their working directory. Fourteen of sixteen ran `git show` or `git log` or listed the evidence folders before answering. Two readers committed their arithmetic scripts to the repository, one on a new branch, with commit messages that state the full answer. Neither the plan nor the prompts asked for any of this.

The earlier runs did not have this problem. In the phase 2 reader run and the control run, no session touched git or any file beyond the one it was given. In the 6 October coherence runs, operators read only the document path they were given.

## Per session

| Session | Browsed | What it saw | Effect on the result |
|---|---|---|---|
| write-S:metallurgy | git log, git show --stat of the plan commit, SKILL.md as instructed | File names only | None. Its write-up is the one that failed; the writer saw no tip. |
| write-S:metamorphosis | git log, the full plan commit, `TRANSFORMATION-STUDY-PLAN.md`, `README.md` | The README sentence "all five failures caused by one ambiguous rounding sentence" and the study plan's note that every earlier failure was "one sentence about rounding" | **Tainted.** This writer was told, in effect, which rule breaks. It wrote the safe form, "every chamber keeps half, rounded down", and its three reads were exact. That cannot be credited to the skill. |
| write-G:metallurgy | git log, git status | Nothing | None. |
| write-G:metamorphosis | nothing | Nothing | None. |
| read-1:S-metallurgy | git show --stat, `compression-250/PLAN.md` | Study design, no rules, no answer | Wrong read; no help received. |
| read-2:S-metallurgy | git show --stat, folder listings | File names | Wrong read; no help received. |
| read-3:S-metallurgy | git show --stat, `PLAN.md` | Study design | Wrong read; no help received. |
| read-1:G-metallurgy | git show --stat, folder listings; then created branch `crucible-cascade-handover` and committed its script and output | File names. Its answer was computed by its own script before the commit. | Exact read, own arithmetic. The commit is a protocol breach, not a leak into this read. |
| read-2:G-metallurgy | git log | Nothing | Exact read, own arithmetic. |
| read-3:G-metallurgy | git show --stat, `PLAN.md`, folder README | Study design | Exact read, own arithmetic. |
| read-1:S-metamorphosis | git show --stat, folder listings | File names | Exact read, own arithmetic. |
| read-2:S-metamorphosis | nothing | Nothing | Exact read, own arithmetic. |
| read-3:S-metamorphosis | git show --stat, folder listing | File names | Exact read, own arithmetic. |
| read-1:G-metamorphosis | git show --stat, `PLAN.md` | Study design | Exact read, own arithmetic. |
| read-2:G-metamorphosis | git show --stat, `PLAN.md`, folder README | Study design | Exact read, own arithmetic. |
| read-3:G-metamorphosis | git show of HEAD at 16:42:03 UTC, after read-1:G-metallurgy's commit at 16:41:52 | **The crucible commit message, which states the end quantities, the reset cycles, the loss and the balance.** Its own script had printed the same answer at 16:41:55, eight seconds earlier; it then committed its own script and output. | **Not clean.** The answer was computed before the leak was seen, and the transcript shows that order, but a read that saw the key before reporting cannot be counted as blind. |

"Own arithmetic" means every tool result containing the answer in that session's transcript came from the session's own script run, and no foreign content containing the answer appeared before its report. The scan looked for the end quantities, the loss total, the commit phrases, and the folder names.

## What is left standing

- **Clean:** Arm S metallurgy, 0 of 3 (writer untipped, readers unhelped). Arm G metallurgy, 3 of 3. Arm G metamorphosis, 2 of 3 clean, 1 not blind.
- **Not usable as evidence for the skill:** Arm S metamorphosis, 3 of 3, because the writer had read the sentence naming the failure.

Raw scores, as pre-registered: S 3 of 6, G 6 of 6. Clean scores: S 0 of 3 on the one usable arm-domain, G 5 of 5 on reads not exposed to the answer. The pre-registered row "S fewer, G 6 of 6" is the one that applies on the raw numbers, and it still applies after removing the tainted parts, because the taint helped the skill arm, not the generic arm. The run is nevertheless reported as contaminated, and `RESULTS.md` says so above its table. Whether to rerun with the harness relay removed is Jake's call; the cost would be the same 16 sessions.

## The two reader commits

They are kept in the history as they happened (commits `4fe4b47` and `ce3b2fc`, authored by the sessions, co-signed "Claude Opus 5.5"). Their files were moved into `reader-committed/` in a later commit so that the evidence tree stays organised. The branch the first reader created, `crucible-cascade-handover`, was left in place; `main` was moved forward to include the commits made while it was checked out.

## Fix for future runs

Start writer and reader sessions in a scratch directory, not the repository, and keep the triggering message free of instructions that a session could take as its own.
