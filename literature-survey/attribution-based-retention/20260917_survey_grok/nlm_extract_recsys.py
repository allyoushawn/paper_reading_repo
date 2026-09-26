#!/usr/bin/env python3
"""Extract RecSys 2026 addendum sources sequentially (NLM rate-friendly)."""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
JOBS = [
    ("G28", "df98b8e9-3fd2-465d-8f1b-23d0c51a8048", "PROMISE"),
    ("G29", "9dc30dae-7a13-4032-9339-5cf10dc1bc6a", "ResidualDominance"),
    ("G30", "9419d0b9-b40e-4e9c-8b49-5f24c45408ec", "STEPS"),
    ("G31", "4824001b-1aa6-4c8e-9ff8-b77d45e029b4", "UniShare"),
    ("G32", "204da68c-fb51-4df5-bd81-c2cb797e35a9", "MODE"),
    ("G33", "7915e99c-f464-494a-9ea5-dfb873b4d91f", "ControlFunction"),
    ("G34", "65d84922-448a-4dd1-950f-148e5c690bc9", "SpilloverAB"),
    ("G35", "7fedeced-8eec-409c-adc9-cff816b1f314", "ConvergentValidity"),
    ("G36", "5e293de3-47dc-4334-97d6-e9bd99c3bfed", "DeltaGate"),
    ("G37", "f678e8c0-439b-4d8b-892f-d9df02becb0a", "LiveStreamMOR"),
    ("G38", "9473661a-49fd-4ede-9ff0-ba2c686cf56f", "GPBM"),
    ("G39", "8119ba67-ed0b-427c-9ffe-03ccc1da6d87", "TSMOO"),
    ("G40", "62a7348a-4f29-4478-9fd8-8e8ae72cffc9", "CascadeReward"),
]

def main():
    only = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    script = os.path.join(HERE, "nlm_extract_one.py")
    for gid, sid, stem in JOBS:
        if only and gid not in only:
            continue
        print("====", gid, stem, flush=True)
        p = subprocess.run([sys.executable, script, gid, sid, stem], cwd=HERE)
        if p.returncode != 0:
            print("FAILED", gid, p.returncode, flush=True)

if __name__ == "__main__":
    main()
