"""Grade the function-match judges from the workflow journal against key.json and the engine.
usage: python grade_fm.py <workflow dir> <out dir>"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fm_engine import run
HERE = os.path.dirname(os.path.abspath(__file__))
wf, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
key = {p["id"]: p for p in json.load(open(os.path.join(HERE, "key.json"), encoding="utf-8"))["pairs"]}
def norm(x): return re.sub(r"[^a-z]", "", str(x).lower())
def same_report(rep, truth):
    """Compare a judge-reported end report with an engine report, ignoring state vocabulary:
    quantities, reset periods, loss, number of changes, and the (period, position) of every change."""
    if not rep: return False
    chg = sorted((c["period"], c["position"]) for c in rep.get("stateChanges", []))
    tchg = sorted((c[0], c[1]) for c in truth["changes"])
    return rep.get("finalQuantities") == truth["final"] and sorted(rep.get("resetPeriods", [])) == sorted(truth["purges"]) and rep.get("lossTotal") == truth["lost"] and chg == tchg
lab, res = {}, {}
for line in open(os.path.join(wf, "journal.jsonl"), encoding="utf-8"):
    d = json.loads(line)
    if d.get("type") == "started": lab[d["agentId"]] = d["label"]
    if d.get("type") == "result": res[lab[d["agentId"]]] = d["result"]
rows = []
for label, r in sorted(res.items()):
    m = re.match(r"judge-(\d):(P\d\d)", label)
    if not m: continue
    j, pid = int(m.group(1)), m.group(2); k = key[pid]
    row = {"pair": pid, "judge": j, "truth": k["truth"], "visible": k["visible_on_given_data"], "result": r}
    if r:
        va, vb = k["A"]["variant"], k["B"]["variant"]
        ta_p, tb_p = run(va), run(vb)
        ta_q, tb_q = run(va, r["probeStart"], r["probeInput"]), run(vb, r["probeStart"], r["probeInput"])
        row.update({
            "verdict_correct": r["verdict"] == k["truth"],
            "table_correct": r["tableVerdict"] == k["truth"],
            "probe_correct": r["probeVerdict"] == k["truth"],
            "routes_agree": r["routesAgree"],
            "printed_A_engine_ok": same_report(r["aOnPrinted"], ta_p), "printed_B_engine_ok": same_report(r["bOnPrinted"], tb_p),
            "probe_A_engine_ok": same_report(r["aOnProbe"], ta_q), "probe_B_engine_ok": same_report(r["bOnProbe"], tb_q),
            "probe_separates_truth": ta_q != tb_q,
            "probe_separates_as_reported": r["aOnProbe"] != r["bOnProbe"],
            "differing_rule_reported": r.get("differingRule", ""), "differing_rule_truth": k["differing_rule"], "found_by": r.get("foundBy"),
        })
        row["probe_genuine"] = row["probe_A_engine_ok"] and row["probe_B_engine_ok"]
    rows.append(row)
    json.dump(row, open(os.path.join(out, f"{pid}-judge{j}.json"), "w", encoding="utf-8", newline="\n"), indent=1)
json.dump({"rows": rows}, open(os.path.join(out, "result.json"), "w", encoding="utf-8", newline="\n"), indent=1)
ok = [r for r in rows if r.get("result")]
print(f"sessions {len(rows)}, with result {len(ok)}")
print(f"verdict correct {sum(r['verdict_correct'] for r in ok)} of {len(ok)}; table correct {sum(r['table_correct'] for r in ok)}; probe-route correct {sum(r['probe_correct'] for r in ok)}; routes agree {sum(r['routes_agree'] for r in ok)}")
print(f"probe genuine (engine-verified on both docs) {sum(r['probe_genuine'] for r in ok)}; printed tables engine-verified both {sum(r['printed_A_engine_ok'] and r['printed_B_engine_ok'] for r in ok)}")
print(f"DIFFERENT pairs: probe truly separates {sum(r['probe_separates_truth'] for r in ok if r['truth']=='DIFFERENT')} of {sum(1 for r in ok if r['truth']=='DIFFERENT')}")
for r in ok:
    if r["visible"] is False: print(f"  hidden {r['pair']} judge {r['judge']}: verdict {r['result']['verdict']} found_by {r['found_by']} probe_separates {r['probe_separates_truth']}")
pairs = sorted(set(r["pair"] for r in ok))
dis = [p for p in pairs if len(set(r["result"]["verdict"] for r in ok if r["pair"] == p)) > 1]
print(f"judges disagree on {len(dis)} pairs: {dis}")
for r in ok:
    flag = "" if r["verdict_correct"] else "  <-- WRONG"
    print(f"{r['pair']} j{r['judge']} truth {r['truth']:9s} verdict {r['result']['verdict']:9s} table {r['result']['tableVerdict']:9s} probe {r['result']['probeVerdict']:9s} genuine {r['probe_genuine']!s:5s} | {r['differing_rule_reported'][:90]}{flag}")
