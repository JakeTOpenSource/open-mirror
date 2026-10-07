"""Build the 16 document pairs for the function-match test from the study 1 documents.
Each edited document differs from its source by the sentences listed in EDITS, nothing else.
Writes pairs/P01-A.md ... and key.json (the truth; never shown to judges).
Every edit must match exactly once, or the build stops."""
import os, json, hashlib, sys
sys.path.insert(0, os.path.dirname(__file__))
from fm_engine import run, VARIANTS
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "coherence-2026-10-06", "documents")

EDITS = {
 ("metamorphosis", "release_sequential"): [
  ("First work out an amount for every chamber, using its mass at the start of this step and its stage as it stands after step 3:",
   "Go through the chambers one at a time, in the order 1, 2, 3, 4, 5, 6. When you reach a chamber, work out its amount from the mass it holds at that moment and its stage as it stands after step 3:"),
  ("Work out all six amounts before you change any mass. Then apply all six at the same time:",
   "Apply that chamber's amount as soon as you have worked it out, before moving on to the next chamber:")],
 ("treatment", "release_sequential"): [
  ("First figure the amount for every one of the six tanks, using each tank's contents at the start of this step, and write all six amounts down before changing any tank:",
   "Handle the tanks one at a time, in the order 1, 2, 3, 4, 5, 6. For the tank in hand, figure its amount from the contents it holds when you reach it:"),
  ("Then apply all six amounts at once:", "Apply that tank's amount straight away, before moving to the next tank:")],
 ("ballast", "release_sequential"): [
  ("First work out the pumped amount for every one of the six compartments, using each compartment's contents at the start of this step:",
   "Work through the compartments one at a time, in the order 1, 2, 3, 4, 5, 6. For the compartment in hand, work out its pumped amount from the contents it holds when you reach it:"),
  ("Work out all six amounts before changing any contents. Then apply all six together:",
   "Apply that compartment's pumped amount at once, before moving on to the next compartment:")],
 ("goodhart", "reset_restated"): [
  ("every team's open tickets become one half of its current count, rounded down.",
   "every team closes the larger half of its open tickets (half of the count, rounded up) and keeps the rest.")],
 ("metallurgy", "reset_keep_larger"): [
  ("Every crucible's melt becomes half of its melt, rounded down.", "Every crucible's melt becomes half of its melt, rounded up.")],
 ("rag", "reset_inclusive"): [
  ("If the total is more than 38, a context reset fires", "If the total is 38 or more, a context reset fires"),
  ("If the total is 38 or less, nothing happens.", "If the total is less than 38, nothing happens.")],
 ("ballast", "upper_strict"): [
  ("A LAMINAR pump whose contents are at least its inception mark becomes CAVITATING.", "A LAMINAR pump whose contents are above its inception mark becomes CAVITATING."),
  ("above its desinence mark and below its inception mark keeps whatever state it had", "above its desinence mark and at or below its inception mark keeps whatever state it had")],
 ("goodhart", "lower_strict"): [
  ("An ESCALATED team whose open tickets are at most its lower mark becomes ROUTINE.", "An ESCALATED team whose open tickets are below its lower mark becomes ROUTINE."),
  ("a team whose count is above its lower mark and below its upper mark keeps the status it had", "a team whose count is at or above its lower mark and below its upper mark keeps the status it had")],
 ("lagrangian", "release_downstream"): [
  ("- ACTIVE component i, for i from 2 to 6: t_i is added to component i-1;\n- ACTIVE component 1: t_1 is added to s.",
   "- ACTIVE component i, for i from 1 to 5: t_i is added to component i+1;\n- ACTIVE component 6: t_6 is added to s."),
  ("after receiving a transfer from component i+1", "after receiving a transfer from component i-1")],
 ("xylem", "mode_before_spill"): [
  ("**Step 3: State check.** Use each segment's sap as it stands after step 2.", "**Step 3: State check.** Use each segment's sap as it stood after step 1, before the xylem push of step 2.")],
 ("treatment", "reset_skip_normal"): [
  ("every tank's contents become half of its contents, rounded down, and all liquor removed from every tank goes to outfall",
   "every OVERLOADED tank's contents become half of its contents, rounded down, while STEADY tanks are left as they are, and all liquor removed goes to outfall")],
 ("rag", "reset_skip_normal"): [
  ("every tier's chunk count becomes its chunk count divided by 2, rounded down, and every chunk removed this way is dropped",
   "every HOT tier's chunk count becomes its chunk count divided by 2, rounded down, while COLD tiers are left as they are, and every chunk removed this way is dropped")],
}

PAIRS = [
 ("P01", ("ballast", None), ("concrete", None)),
 ("P02", ("electrical", None), ("goodhart", None)),
 ("P03", ("lagrangian", None), ("rag", None)),
 ("P04", ("treatment", None), ("xylem", None)),
 ("P05", ("metallurgy", None), ("metamorphosis", "release_sequential")),
 ("P06", ("concrete", None), ("treatment", "release_sequential")),
 ("P07", ("electrical", None), ("ballast", "release_sequential")),
 ("P08", ("lagrangian", None), ("goodhart", "reset_restated")),
 ("P09", ("xylem", None), ("metallurgy", "reset_keep_larger")),
 ("P10", ("concrete", None), ("rag", "reset_inclusive")),
 ("P11", ("ballast", "upper_strict"), ("electrical", None)),
 ("P12", ("treatment", None), ("goodhart", "lower_strict")),
 ("P13", ("metamorphosis", None), ("lagrangian", "release_downstream")),
 ("P14", ("xylem", "mode_before_spill"), ("metallurgy", None)),
 ("P15", ("electrical", None), ("treatment", "reset_skip_normal")),
 ("P16", ("rag", "reset_skip_normal"), ("ballast", None)),
]

def doc(domain, variant):
    text = open(os.path.join(SRC, f"{domain}.md"), encoding="utf-8").read()
    if variant:
        for old, new in EDITS[(domain, variant)]:
            assert text.count(old) == 1, f"edit does not match exactly once: {domain} {variant}: {old[:60]}"
            text = text.replace(old, new)
    return text

out = os.path.join(HERE, "pairs"); os.makedirs(out, exist_ok=True)
key = {"pairs": []}
base = run("base")
for pid, a, b in PAIRS:
    ta, tb = doc(*a), doc(*b)
    for side, t in (("A", ta), ("B", tb)):
        open(os.path.join(out, f"{pid}-{side}.md"), "w", encoding="utf-8", newline="\n").write(t)
    va, vb = a[1] or "base", b[1] or "base"
    ra, rb = run(va), run(vb)
    same = (va in ("base", "release_sequential", "reset_restated")) and (vb in ("base", "release_sequential", "reset_restated"))
    key["pairs"].append({"id": pid, "A": {"domain": a[0], "variant": va, "sha256": hashlib.sha256(ta.encode()).hexdigest()},
                         "B": {"domain": b[0], "variant": vb, "sha256": hashlib.sha256(tb.encode()).hexdigest()},
                         "truth": "SAME" if same else "DIFFERENT", "differing_rule": None if same else VARIANTS[va if va != "base" else vb],
                         "visible_on_given_data": None if same else (ra != rb)})
json.dump(key, open(os.path.join(HERE, "key.json"), "w", encoding="utf-8", newline="\n"), indent=1)
for p in key["pairs"]:
    print(p["id"], p["A"]["domain"], p["A"]["variant"], "|", p["B"]["domain"], p["B"]["variant"], "|", p["truth"], "" if p["visible_on_given_data"] is None else ("visible" if p["visible_on_given_data"] else "HIDDEN"))
print("built", len(key["pairs"]), "pairs")
