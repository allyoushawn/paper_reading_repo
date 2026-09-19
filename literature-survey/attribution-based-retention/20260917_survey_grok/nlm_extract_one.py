#!/usr/bin/env python3
"""Run 2 NotebookLM queries per source and dump raw JSON under nlm-raw/."""
import json, os, subprocess, sys, time

NB = "6a3b8a8e-6f2f-4efe-99eb-283983fc95d9"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "nlm-raw")
os.makedirs(OUT, exist_ok=True)

Q1 = """For THIS source only, provide clearly labeled sections:
(1) Title, authors, affiliations, year, venue
(2) Core problem and key contribution
(3) Proposed method or architecture in detail, including how (if at all) credit is assigned to individual touchpoints/items/actions
(4) Datasets, production deployment, and comparison baselines
(5) Key quantitative results with numbers
(6) Limitations, failure modes, or negative results
(7) Top 5–7 most heavily cited prior works named in related work or introduction
If a field is not in the source, write: Not specified in source."""

Q2 = """Project: dating-app retention attribution. Product: users swipe profiles; mutual like = match; matches lead to conversations. Goal: attribute a user's N7 retention (active on day 7) to particular swipes so scores become training labels for ranking. Current production: last-touch — N7 assigned to the most recent swipes. Weaknesses: ignores earlier swipes, later matches/conversations, selection bias (engaged users swipe more), no fractional credit. 2026-06-13 plan: binary N7; v1 interpretable removal-effect attributor; v2 calibrated deep DDA + survival head.

For THIS source only, answer:
(A) Q1 or Q2 or both or neither? Q1 = industry/production attribution 2025-01 to 2026-09. Q2 = attributing retention/engagement/days-active to individual in-app interactions.
(B) Q2 class MUST be exactly one of TRUE / PARTIAL / NOT. TRUE = publishes per-touch credit of retention/active-days to individual actions with causal or explicit multi-touch decomposition. PARTIAL = item/action-level retention scores or surrogate linkage, confounders acknowledged, not identified causal MTA. NOT = RL/LTR/bandit/surrogate policy optimization without a per-exposure retention credit table.
(C) Does it produce per-interaction credit? For what outcome?
(D) How would this replace or improve last-touch N7→latest swipes? Map onto swipe / match / conversation if possible.
(E) Selection-bias handling?
(F) Deployed or production dataset?
Quote numbers from the source. If not in the source, write Not specified in source."""

def query(sid, question, tag):
    cmd = [
        "nlm", "notebook", "query", NB, question,
        "--source-ids", sid,
        "--timeout", "180",
        "--json",
    ]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
    return {"returncode": p.returncode, "stdout": p.stdout, "stderr": p.stderr, "tag": tag}

def main():
    # args: gid sid filename_stem
    if len(sys.argv) < 4:
        print("usage: nlm_extract_one.py GID SOURCE_ID STEM")
        sys.exit(2)
    gid, sid, stem = sys.argv[1], sys.argv[2], sys.argv[3]
    path = os.path.join(OUT, f"{gid}_{stem}.json")
    if os.path.exists(path) and os.path.getsize(path) > 200:
        print("skip existing", path)
        return
    rec = {"gid": gid, "source_id": sid, "stem": stem, "queries": []}
    for tag, q in [("facts", Q1), ("project", Q2)]:
        print(f"{gid} {tag} ...", flush=True)
        rec["queries"].append(query(sid, q, tag))
        time.sleep(1)
    with open(path, "w") as f:
        json.dump(rec, f, indent=2)
    print("wrote", path, "rc", [x["returncode"] for x in rec["queries"]])

if __name__ == "__main__":
    main()
