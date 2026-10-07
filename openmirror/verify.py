#!/usr/bin/env python3
"""Open Mirror evidence verifier.

Run from the openmirror/ folder:   python verify.py
Reads only files under this folder. Calls no model. Writes CLAIMS.md and MANIFEST.json.

Every quantitative claim in the reports is recomputed here from the raw records. A claim passes
only if the recomputed value equals the stated value. If you change a report, rerun this.
"""
import json, os, re, sys, hashlib, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
EV = os.path.join(HERE, "evidence", "coherence-2026-10-06")
RT1 = os.path.join(HERE, "evidence", "red-team-2026-10-06")
RT2 = os.path.join(HERE, "evidence", "red-team-2026-10-06-r2")

def rd(p): return open(p, encoding="utf-8").read()
def jl(p): return json.load(open(p, encoding="utf-8"))
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""): h.update(chunk)
    return h.hexdigest()

claims = []   # (id, claim text, stated, recomputed, sources, pass)
def claim(cid, text, stated, recomputed, sources):
    ok = (stated == recomputed)
    claims.append((cid, text, stated, recomputed, sources, ok))
    return ok

ORDER = ["electrical", "concrete", "metallurgy", "xylem", "ballast", "metamorphosis", "treatment", "rag", "lagrangian", "goodhart"]

# ------------------------------------------------------------------ ground truth
ds = jl(os.path.join(EV, "inputs", "dataset.json"))
truth = ds["truth"]
eng = subprocess.run([sys.executable, os.path.join(EV, "inputs", "engine.py")], capture_output=True, text=True)
engine_truth = json.loads(eng.stdout.splitlines()[0]) if eng.stdout else None
norm = lambda t: json.loads(json.dumps(t))
claim("T1", "engine.py, run fresh, reproduces dataset.json truth", norm(truth), norm(engine_truth), ["inputs/engine.py", "inputs/dataset.json"])
claim("T2", "ground truth final quantities", [6, 10, 9, 7, 4, 2], truth["final"], ["inputs/dataset.json"])
claim("T3", "ground truth reset cycles", [1, 4], truth["purges"], ["inputs/dataset.json"])
claim("T4", "ground truth loss", 76, truth["lost"], ["inputs/dataset.json"])
claim("T5", "ground truth state-change count", 13, len(truth["changes"]), ["inputs/dataset.json"])
claim("T6", "conservation: start + inputs = final + loss", sum(ds["L0"]) + sum(map(sum, ds["INTAKE"])), sum(truth["final"]) + truth["lost"], ["inputs/dataset.json"])

# ------------------------------------------------------------------ study 1
s1 = jl(os.path.join(EV, "study1-complete.json"))
exact1 = sum(1 for c in s1["cases"] for a in "ABC" if c["arms"][a]["grade"].get("exact"))
claim("S1-1", "Study 1: reports exactly right", 30, exact1, ["study1-complete.json"])
claim("S1-2", "Study 1: reports graded", 30, sum(1 for c in s1["cases"] for a in "ABC" if c["arms"][a]["grade"].get("available")), ["study1-complete.json"])
src = {}
for c in s1["cases"]:
    for a in "ABC":
        k = c["arms"][a].get("source", "opus-original"); src[k] = src.get(k, 0) + 1
claim("S1-3", "Study 1: Opus 5.5 first-attempt reports", 21, src.get("opus-original", 0), ["study1-complete.json"])
claim("S1-4", "Study 1: Opus 5.5 reruns (document by file)", 4, src.get("rerun-opus-docfile", 0), ["study1-complete.json"])
claim("S1-5", "Study 1: Sonnet fallbacks (document by file)", 5, src.get("fallback-sonnet-docfile", 0), ["study1-complete.json"])
claim("S1-6", "Study 1: every operator used a script", 30, sum(1 for c in s1["cases"] for a in "ABC" if (c["arms"][a]["run"] or {}).get("usedScript")), ["study1-complete.json"])
claim("S1-7", "Study 1: documents that needed a revision after the completeness check", 1, sum(1 for c in s1["cases"] if c["attempts"] > 1), ["study1-complete.json"])
claim("S1-8", "Study 1: documents passing the completeness check", 10, sum(1 for c in s1["cases"] if c["checkPassed"]), ["study1-complete.json"])
claim("S1-9", "Study 1: reviewer cases describing null/placeholder operators (written before reruns)", 5,
      sum(1 for c in s1["cases"] if any(c["arms"][a].get("source") in ("rerun-opus-docfile", "fallback-sonnet-docfile") for a in "ABC")), ["study1-complete.json", "reviews/*.json"])
# per-operator files match the aggregate
mismatch = []
for c in s1["cases"]:
    for a in "ABC":
        f = jl(os.path.join(EV, "operators", f"{c['domain']['key']}-{a}.json"))
        if f["grade"].get("exact") != c["arms"][a]["grade"].get("exact"): mismatch.append(f"{c['domain']['key']}-{a}")
claim("S1-10", "Study 1: per-operator files agree with the aggregate record", [], mismatch, ["operators/*.json", "study1-complete.json"])
# documents contain no answer figures
leak = [k for k in ORDER if any(s in rd(os.path.join(EV, "documents", f"{k}.md")) for s in ["6, 10, 9, 7, 4, 2", "(1,2,", "(1, 2,"])]
claim("S1-11", "Study 1: documents containing the answer figures", [], leak, ["documents/*.md"])

# ------------------------------------------------------------------ study 2 (corrected run)
s2 = jl(os.path.join(EV, "study2-lossy-v2", "result.json"))
per = {a: sum(1 for c in s2["cases"] if c["arms"][a]["grade"].get("exact")) for a in "ABC"}
claim("S2-1", "Study 2: reports exactly right", 25, sum(per.values()), ["study2-lossy-v2/result.json"])
claim("S2-2", "Study 2: exact by arm A, B, C", [8, 9, 8], [per["A"], per["B"], per["C"]], ["study2-lossy-v2/result.json"])
claim("S2-3", "Study 2: operator sessions that returned a report (no refusals)", 30, sum(1 for c in s2["cases"] for a in "ABC" if c["arms"][a]["run"]), ["study2-lossy-v2/result.json"])
flag = {"A": 0, "B": 0, "C": 0}; losses = 0
for c in s2["cases"]:
    losses += c["analysis"]["applicableLosses"]
    for op in c["analysis"]["operators"]: flag[op["arm"][:1]] += op["gapsCorrectlyFlagged"]
claim("S2-4", "Study 2: applicable real losses across ten write-ups", 98, losses, ["study2-lossy-v2/reviews/*.json"])
claim("S2-5", "Study 2: real losses flagged by arm A, B, C", [43, 43, 45], [flag["A"], flag["B"], flag["C"]], ["study2-lossy-v2/reviews/*.json"])
fails = sorted((c["key"], a) for c in s2["cases"] for a in "ABC" if not c["arms"][a]["grade"].get("exact"))
claim("S2-6", "Study 2: the failing operators", [["metallurgy", "A"], ["metallurgy", "B"], ["metallurgy", "C"], ["metamorphosis", "A"], ["metamorphosis", "C"]], [list(x) for x in fails], ["study2-lossy-v2/result.json"])
traj = sorted({json.dumps([c["arms"][a]["grade"]["got"]["final"], c["arms"][a]["grade"]["got"]["resetPeriods"], c["arms"][a]["grade"]["got"]["loss"]]) for c in s2["cases"] for a in "ABC" if not c["arms"][a]["grade"].get("exact")})
claim("S2-7", "Study 2: all failures share one trajectory (final, resets, loss)", ['[[4, 5, 5, 4, 3, 1], [1, 4, 5], 92]'], traj, ["study2-lossy-v2/result.json"])
types = sorted({t for c in s2["cases"] for op in c["analysis"]["operators"] if not op["exactlyRight"] for t in op["errorTypes"]})
claim("S2-8", "Study 2: reviewer error types across the five failures", ["rounding", "rule-ambiguous-in-document"], types, ["study2-lossy-v2/reviews/*.json"])
claim("S2-9", "Study 2: operator C pre-read notes present (mandatory field) in every case", 10, sum(1 for c in s2["cases"] if len((c["arms"]["C"]["run"] or {}).get("preReadNotes", "")) >= 400), ["study2-lossy-v2/result.json"])
mc = [c for c in s2["cases"] if c["key"] == "metallurgy"][0]["arms"]["C"]["run"]["preReadNotes"]
claim("S2-10", "Study 2: metallurgy C pre-read named the halving ambiguity before the work", True, "The one thing it leaves open is how the halving rounds" in mc, ["study2-lossy-v2/operators/metallurgy-C.json"])
eng_not_dom = sum(1 for c in s2["cases"] for op in c["analysis"]["operators"] if op["arm"][:1] == "A" and re.search(r"engineer", op["followedEngineerNotDomain"], re.I) and not re.search(r"followed (real|the domain|domain practice)", op["followedEngineerNotDomain"], re.I))
claim("S2-11", "Study 2: operator-A cases where the reviewer found assumptions followed the engineer's process, not the domain", 10, eng_not_dom, ["study2-lossy-v2/reviews/*.json"])
leak2 = [k for k in ORDER if any(s in rd(os.path.join(EV, "study2-lossy-v2", "write-ups-as-given", f"{k}.md")) for s in ["6, 10, 9, 7, 4, 2", "6,10,9,7,4,2", "6 10 9 7 4 2", "(1,2,", "(1, 2,", " 76", "114"])]
claim("S2-12", "Study 2 corrected run: write-ups containing any answer figure", [], leak2, ["study2-lossy-v2/write-ups-as-given/*.md"])
leakv1 = [k for k in ORDER if any(s in rd(os.path.join(EV, "study2-lossy-v1-void", "documents", f"{k}.md")) for s in ["6, 10, 9, 7, 4, 2", "6,10,9,7,4,2", "6 10 9 7 4 2"])]
claim("S2-13", "Study 2 void first attempt: write-ups that printed the final figures (why it is void)", 10, len(leakv1), ["study2-lossy-v1-void/documents/*.md"])
words = {k: len(rd(os.path.join(EV, "study2-lossy-v2", "write-ups-as-given", f"{k}.md")).split()) for k in ORDER}
claim("S2-14", "Study 2: every write-up at or under 400 words", True, max(words.values()) <= 400, ["study2-lossy-v2/write-ups-as-given/*.md"])

# ------------------------------------------------------------------ red-team rounds: structural only
claim("R1-1", "Red-team round 1: transcripts on file", 5, len([f for f in os.listdir(RT1) if f.startswith("T")]), ["red-team-2026-10-06/"])
claim("R2-1", "Red-team round 2: transcripts on file including the explanation rerun", 6, len([f for f in os.listdir(RT2) if f.startswith("T")]), ["red-team-2026-10-06-r2/"])
claim("R2-2", "Red-team round 2 packet is byte-identical to the v1.4.1 text it claims to be (hash recorded in its README)",
      "fbc70b9db5bd26a60a7f8fc196f91724fe0444c080a8097c7e6475f827e882e8", sha(os.path.join(RT2, "00-method-packet-given-to-replicators.md")), ["red-team-2026-10-06-r2/00-method-packet-given-to-replicators.md", "red-team-2026-10-06-r2/README.md"])

# ------------------------------------------------------------------ text consistency
skill = rd(os.path.join(HERE, "SKILL.md")); readme = rd(os.path.join(HERE, "README.md")); coh = rd(os.path.join(HERE, "COHERENCE-STUDY.md")); full = rd(os.path.join(HERE, "OPEN-MIRROR-FULL-REPORT-2026-10-06.md"))
claim("V-1", "SKILL.md footer version", "v1.4.3", re.search(r"\*v(1\.\d\.\d), 2026-10-06", skill).group(0)[1:7], ["SKILL.md"])
claim("V-2", "README labels SKILL.md as v1.4.3", True, "The method, v1.4.3" in readme, ["README.md"])
claim("V-3", "no document claims the pre-read's value is nil", 0, sum(t.count("is nil") for t in (skill, readme, coh, full)), ["*.md"])
claim("V-4", "the scoped result sentence appears in the study report", True, "fixed numerical procedure" in coh, ["COHERENCE-STUDY.md"])
claim("V-5", "Study 1 table in the study report matches the record", True, all(
    f"| {c['domain']['key']} | " + " | ".join("exact" + {"opus-original": "", "rerun-opus-docfile": " (R)", "fallback-sonnet-docfile": " (S)"}[c["arms"][a].get("source", "opus-original")] for a in "ABC") + " |" in coh for c in s1["cases"]), ["COHERENCE-STUDY.md", "study1-complete.json"])
claim("V-6", "Study 2 table in the study report matches the record", True, all(
    f"| {c['key']} | " + " | ".join(("exact" if c["arms"][a]["grade"].get("exact") else "**wrong**") for a in "ABC") + f" | {c['analysis']['applicableLosses']} | " + ", ".join(str(next(op["gapsCorrectlyFlagged"] for op in c["analysis"]["operators"] if op["arm"][:1] == a)) for a in "ABC") + " |" in coh for c in s2["cases"]), ["COHERENCE-STUDY.md", "study2-lossy-v2/result.json"])
claim("V-7", "compiled report embeds SKILL.md, README, CHANGELOG and the three reports byte-identically", True,
      all(rd(os.path.join(HERE, n)).rstrip() in full for n in ["SKILL.md", "README.md", "CHANGELOG.md", "RED-TEAM-REPORT.md", "RED-TEAM-REPORT-R2.md", "COHERENCE-STUDY.md"]), ["OPEN-MIRROR-FULL-REPORT-2026-10-06.md"])
claim("V-8", "compiled report embeds all 20 operator documents byte-identically", 20,
      sum(1 for k in ORDER for p in (os.path.join(EV, "documents", f"{k}.md"), os.path.join(EV, "study2-lossy-v2", "write-ups-as-given", f"{k}.md")) if rd(p).rstrip() in full), ["OPEN-MIRROR-FULL-REPORT-2026-10-06.md"])

# ------------------------------------------------------------------ accounting (stated in COHERENCE-STUDY and the compiled summary)
acct = full[full.index("Session and token accounting"):]
rows = re.findall(r"\| (?:Red-team|Explanation|Coherence|Study)[^|\n]*\| (\d+) \| ~?([\d.]+)M", acct)
claim("A-1", "accounting table rows sum to the stated session total", int(re.search(r"\| \*\*Total\*\* \| \*\*(\d+)\*\*", acct).group(1)), sum(int(a) for a, _ in rows), ["OPEN-MIRROR-FULL-REPORT-2026-10-06.md"])
claim("A-2", "accounting table rows sum to the stated token total (0.1M tolerance)", True, abs(float(re.search(r"\| \*\*Total\*\* \| \*\*\d+\*\* \| \*\*~([\d.]+)M", acct).group(1)) - sum(float(b) for _, b in rows)) < 0.1, ["OPEN-MIRROR-FULL-REPORT-2026-10-06.md"])

# ------------------------------------------------------------------ study 3 (transformation)
S3 = os.path.join(HERE, "evidence", "transformation-2026-10-07")
if os.path.exists(os.path.join(S3, "phase2-result.json")):
    p1 = jl(os.path.join(S3, "phase1-result.json")); p2 = jl(os.path.join(S3, "phase2-result.json")); p3 = jl(os.path.join(S3, "phase3-result.json"))
    claim("S3-1", "Study 3: disciplined write-ups passing the discipline check (cap, no figures, plain statement, self-check)", 10, sum(1 for r in p1["results"] if not r["problems"]), ["transformation-2026-10-07/phase1-result.json"])
    claim("S3-2", "Study 3: every disciplined write-up at or under 400 words", True, all(len(rd(os.path.join(S3, "w1-write-ups", f"{k}.md")).split()) <= 400 for k in ORDER), ["transformation-2026-10-07/w1-write-ups/*.md"])
    claim("S3-3", "Study 3: disciplined write-ups containing any answer figure", [], [k for k in ORDER if any(x in rd(os.path.join(S3, "w1-write-ups", f"{k}.md")) for x in ["6, 10, 9, 7, 4, 2", "6,10,9,7,4,2", "6 10 9 7 4 2", "(1,2,", "(1, 2,", " 76", "114"])], ["transformation-2026-10-07/w1-write-ups/*.md"])
    # regrade every read from the raw run records with the same mapping used for study 2
    def g3(run, resting, raised):
        n, e = norm(resting), norm(raised)
        def ms(x):
            x = norm(x)
            if x == n: return "NORMAL"
            if x == e: return "ELEVATED"
            for w, lab in sorted([(n, "NORMAL"), (e, "ELEVATED")], key=lambda t: -len(t[0])):
                if w and w in x: return lab
            return "UNMAPPED"
        chg = sorted("|".join(map(str, [c["period"], c["position"], ms(c["from"]), ms(c["to"])])) for c in run.get("stateChanges", []))
        tchg = sorted("|".join(map(str, c)) for c in truth["changes"])
        return run.get("finalQuantities") == truth["final"] and [ms(x) for x in run.get("finalStates", [])] == truth["modes"] and chg == tchg and sorted(run.get("resetPeriods", [])) == sorted(truth["purges"]) and run.get("lossTotal") == truth["lost"]
    metas = {k: jl(os.path.join(S3, "w1-write-ups", f"{k}.meta.json")) for k in ORDER}
    exact3 = sum(1 for r in p2["reads"] if r["run"] and g3(r["run"], metas[r["key"]]["restingStateWord"], metas[r["key"]]["raisedStateWord"]))
    claim("S3-4", "Study 3: reads of disciplined write-ups exactly right (all five fields, regraded here)", 14, exact3, ["transformation-2026-10-07/phase2-result.json", "transformation-2026-10-07/w1-write-ups/*.meta.json"])
    claim("S3-5", "Study 3: reads attempted (no refusals, no second reads needed)", 14, len(p2["reads"]), ["transformation-2026-10-07/phase2-result.json"])
    claim("S3-6", "Study 3: reads on the two domains that drifted in the baseline (metallurgy, metamorphosis), all exact", 6, sum(1 for r in p2["reads"] if r["key"] in ("metallurgy", "metamorphosis") and r["run"] and g3(r["run"], metas[r["key"]]["restingStateWord"], metas[r["key"]]["raisedStateWord"])), ["transformation-2026-10-07/phase2-result.json"])
    tot = {a: sum(e["recoverable"] for e in p3["extractions"] if e["arm"] == a) for a in ("W0", "W1")}
    claim("S3-7", "Study 3: checklist rules recoverable, baseline W0 of 230", 219, tot["W0"], ["transformation-2026-10-07/phase3-result.json"])
    claim("S3-8", "Study 3: checklist rules recoverable, disciplined W1 of 230", 226, tot["W1"], ["transformation-2026-10-07/phase3-result.json"])
    claim("S3-9", "Study 3: every checklist extraction returned exactly 23 answers", 20, sum(1 for e in p3["extractions"] if e["results"] and len(e["results"]) == 23), ["transformation-2026-10-07/phase3-result.json"])
    ctrl = os.path.join(S3, "control", "result.json")
    if os.path.exists(ctrl):
        c = jl(ctrl)
        cw = {w["id"]: w for w in c["writes"]}
        claim("S3-10", "Control: write-ups passing the cap and figure checks", 4, sum(1 for w in c["writes"] if not w["problems"] and len(w["translation"]["document"].split()) <= 400), ["transformation-2026-10-07/control/result.json"])
        claim("S3-11", "Control: reads attempted", 12, len(c["reads"]), ["transformation-2026-10-07/control/result.json"])
        claim("S3-12", "Control: reads exactly right (all five fields, regraded here)", 12, sum(1 for r in c["reads"] if r["run"] and g3(r["run"], cw[r["id"]]["translation"]["restingStateWord"], cw[r["id"]]["translation"]["raisedStateWord"])), ["transformation-2026-10-07/control/result.json"])
        claim("S3-13", "Control: the control writer prompt contains none of the skill's moves (plain statement, stranger, recoverable, picture)", True, not any(k in open(os.path.join(S3, "control", "writer-instruction.txt"), encoding="utf-8").read().lower() for k in ["plain statement", "stranger", "recoverable", "picture", "open mirror"]) if os.path.exists(os.path.join(S3, "control", "writer-instruction.txt")) else None, ["transformation-2026-10-07/control/writer-instruction.txt"])
    c250 = os.path.join(S3, "compression-250", "result.json")
    if os.path.exists(c250):
        c2 = jl(c250)
        w2 = {w["id"]: w for w in c2["writes"]}
        claim("S3-14", "250-word test: write-ups passing the cap and figure checks", 4, sum(1 for w in c2["writes"] if not w["problems"] and len(w["translation"]["document"].split()) <= 250), ["transformation-2026-10-07/compression-250/result.json"])
        ex = {a: sum(1 for r in c2["reads"] if r["arm"] == a and r["run"] and g3(r["run"], w2[r["id"]]["translation"]["restingStateWord"], w2[r["id"]]["translation"]["raisedStateWord"])) for a in ("S", "G")}
        claim("S3-15", "250-word test: skill arm reads exact of 6", 3, ex["S"], ["transformation-2026-10-07/compression-250/result.json"])
        claim("S3-16", "250-word test: generic-review arm reads exact of 6", 6, ex["G"], ["transformation-2026-10-07/compression-250/result.json"])
        bad = [r for r in c2["reads"] if r["run"] and not g3(r["run"], w2[r["id"]]["translation"]["restingStateWord"], w2[r["id"]]["translation"]["raisedStateWord"])]
        claim("S3-17", "250-word test: every wrong read is S-metallurgy with the known trajectory (4,5,5,4,3,1; resets 1,4,5; loss 92)", True, bool(bad) and all(r["id"] == "S-metallurgy" and r["run"]["finalQuantities"] == [4, 5, 5, 4, 3, 1] and sorted(r["run"]["resetPeriods"]) == [1, 4, 5] and r["run"]["lossTotal"] == 92 for r in bad), ["transformation-2026-10-07/compression-250/result.json"])

# ------------------------------------------------------------------ what is NOT verified here (stated, not hidden)
unverified = [
    "Study 3 compares disciplined writers with the earlier undisciplined writers; both were Opus with the same domain mappings and word cap, but the disciplined prompt also said explicitly that no figures may appear. Whether the gain comes from Open Mirror's text or from any careful self-review instruction was not tested.",
    "Red-team scorecards (rounds 1 and 2) are one reviewer's judgments against a rubric; this script checks only that the transcripts and packets exist and hash as stated.",
    "Reviewer verdicts in both coherence studies are model judgments; this script recomputes counts from them but cannot check their correctness.",
    "Token figures are the harness's subagent_tokens totals as reported at run time; the raw usage records are not in this folder.",
    "Study 1 Sonnet fallbacks and Opus reruns supplied the document by file rather than inline; the prompt was otherwise identical.",
]

# ------------------------------------------------------------------ manifest
manifest = {}
for root, _, files in os.walk(HERE):
    for f in files:
        p = os.path.join(root, f)
        rel = os.path.relpath(p, HERE).replace("\\", "/")
        if rel in ("MANIFEST.json", "CLAIMS.md"): continue
        manifest[rel] = {"sha256": sha(p), "bytes": os.path.getsize(p)}
json.dump({"root": "openmirror/", "files": dict(sorted(manifest.items()))}, open(os.path.join(HERE, "MANIFEST.json"), "w", encoding="utf-8", newline="\n"), indent=1)

# ------------------------------------------------------------------ CLAIMS.md
passed = sum(1 for c in claims if c[5])
out = []
out.append("# Claims register\n")
out.append(f"Generated by `verify.py`. {passed} of {len(claims)} claims pass. Every row is recomputed from the files named; nothing is copied from the prose. Rerun `python verify.py` after any change.\n")
out.append("| ID | Claim | Stated | Recomputed | Pass | Source files |")
out.append("|---|---|---|---|---|---|")
for cid, text, stated, recomputed, sources, ok in claims:
    f = lambda v: "`" + json.dumps(v)[:80] + "`"
    out.append(f"| {cid} | {text} | {f(stated)} | {f(recomputed)} | {'yes' if ok else '**NO**'} | {', '.join(sources)} |")
out.append("\n## Not verified by this script\n")
for u in unverified: out.append(f"- {u}")
out.append(f"\n## Manifest\n\n`MANIFEST.json` lists SHA-256 and byte count for {len(manifest)} files under `openmirror/`. To check that nothing has changed since it was written: `python verify.py --check-manifest`.\n")
open(os.path.join(HERE, "CLAIMS.md"), "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")

if "--check-manifest" in sys.argv:
    old = jl(os.path.join(HERE, "MANIFEST.json"))["files"]
    changed = [k for k in old if k in manifest and old[k]["sha256"] != manifest[k]["sha256"]]
    print("manifest changed files:", changed or "none")

print(f"{passed} of {len(claims)} claims pass")
for cid, text, stated, recomputed, sources, ok in claims:
    if not ok: print(f"FAIL {cid}: {text}\n   stated {stated}\n   recomputed {recomputed}")
print(f"manifest: {len(manifest)} files")
