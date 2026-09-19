#!/usr/bin/env python3
"""Extract a list of (gid, sid, stem) with limited parallelism."""
import subprocess, sys, os
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "nlm_extract_one.py")

BATCH = [
    ("G1", "118a06c8-9072-4e89-bab7-f1e22de5a51a", "LOTUS"),
    ("G2", "61bdb620-ede0-430e-a39d-f7888235fd5c", "IMA"),
    ("G3", "7a88f033-bb50-43c2-ae8e-f2fd407c8ebb", "LinkedInDDA"),
    ("G4", "088b1ae5-f3f7-4ccc-88db-d6e8408e50f1", "FID"),
    ("G5", "6d64098b-cfd7-44cc-9e0d-14a3b30bba04", "RevisitMTL"),
    ("G6", "da74515a-9d0d-4f88-9161-7aa430fe7686", "MRet"),
    ("G7", "7d87bba2-fe8d-4f09-87ad-713b22aaca47", "RLUR"),
    ("G8", "1000111e-44ac-4cc3-a39f-584e06ac7da6", "GFN4Retention"),
    ("G9", "db4edc42-fa93-4822-8a60-f0c7116ffa57", "AURO"),
    ("G10", "d9a6d934-5dad-4efc-8e08-c62a0184f137", "SEC"),
    ("G11", "7f131324-1d54-4dd2-8a1c-98f5f0ce8dfd", "OCARM"),
    ("G12", "42ed27d5-3e90-483f-b728-e5cdab72cfcd", "ALM-MTA"),
    ("G13", "47cf0db1-92bc-49da-b44f-af65cea80083", "IURO"),
    ("G14", "dc389695-c31e-4eba-a1d2-00268bcf0ac1", "IURO-plus"),
    ("G15", "4c1119dd-6713-4864-a194-a53a14065084", "AirbnbInterleave"),
    ("G16", "c7d8e9d2-5ee2-4cbf-ab8a-15cba733edc1", "ImpatientBandits"),
    ("G17", "cf9de03f-0d61-4f7e-85ee-1cc46fb9ef3c", "DT4Rec"),
    ("G18", "15cdd352-b889-48d8-a3d5-4bdabefd67f8", "IncrementalRec"),
    ("G19", "9a650298-5c0c-48d2-9597-450c32a73457", "LRF"),
    ("G20", "d017d9e2-9833-4411-b351-5d5a4fe920cc", "MetaLTV"),
    ("G21", "cb0d9351-5064-4c9b-b669-e5f25fe0203f", "SurrogateLTUX"),
    ("G22", "305cd94b-33e0-46f8-961a-2228a9d46046", "SeqRecRetention"),
    ("G23", "1a74145c-f8bc-438b-a5ea-965b29abab16", "DownstreamRewards"),
    ("G24", "d18bf088-6fb0-4082-952c-2a13f61ffc2e", "DCEO"),
    ("G25", "3f40b05f-169b-4e36-b317-fdadf7a86bc1", "DuolingoBandit"),
]

def run(item):
    gid, sid, stem = item
    p = subprocess.run([sys.executable, SCRIPT, gid, sid, stem], cwd=HERE)
    return gid, p.returncode

def main():
    subset = BATCH
    if len(sys.argv) > 1:
        want = set(sys.argv[1].split(","))
        subset = [x for x in BATCH if x[0] in want]
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    print(f"running {len(subset)} with {workers} workers", flush=True)
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(run, it) for it in subset]
        for f in as_completed(futs):
            gid, rc = f.result()
            print("done", gid, rc, flush=True)

if __name__ == "__main__":
    main()
