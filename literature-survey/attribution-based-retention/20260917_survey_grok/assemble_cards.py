#!/usr/bin/env python3
"""Assemble compact read-papers cards from nlm-raw JSON dumps."""
import json, os, re, glob, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "nlm-raw")
OUT = os.path.join(HERE, "read-papers")
os.makedirs(OUT, exist_ok=True)

FILES = {
    "G1": ("2026_CIKM_LOTUS_Meaningful-Touchpoints-Conversion-Attribution.md",
           "https://arxiv.org/pdf/2608.28649.pdf", "118a06c8-9072-4e89-bab7-f1e22de5a51a"),
    "G2": ("2026_arXiv_IMA_Integrated-Marketing-Attribution.md",
           "https://arxiv.org/pdf/2606.16878.pdf", "61bdb620-ede0-430e-a39d-f7888235fd5c"),
    "G3": ("2025_LinkedIn_LiDDA_Buyer-Journey-Data-Driven-Attribution.md",
           "https://www.linkedin.com/blog/engineering/marketing/buyer-journey-insights-with-data-driven-attribution",
           "7a88f033-bb50-43c2-ae8e-f2fd407c8ebb"),
    "G4": ("2024_KDD_FID_Future-Impact-Decomposition.md",
           "https://arxiv.org/pdf/2401.16108.pdf", "088b1ae5-f3f7-4ccc-88db-d6e8408e50f1"),
    "G5": ("2026_AAAI_RevisitMTL_Save-Revisit-Retain.md",
           "https://arxiv.org/pdf/2511.18013.pdf", "6d64098b-cfd7-44cc-9e0d-14a3b30bba04"),
    "G6": ("2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md",
           "https://arxiv.org/pdf/2602.15752.pdf", "da74515a-9d0d-4f88-9161-7aa430fe7686"),
    "G7": ("2023_WWW_RLUR_Reinforcing-User-Retention.md",
           "https://arxiv.org/pdf/2302.01724.pdf", "7d87bba2-fe8d-4f09-87ad-713b22aaca47"),
    "G8": ("2024_KDD_GFN4Retention_Modeling-User-Retention.md",
           "https://arxiv.org/pdf/2406.06043.pdf", "1000111e-44ac-4cc3-a39f-584e06ac7da6"),
    "G9": ("2025_WWW_AURO_Adaptive-User-Retention-Optimization.md",
           "https://arxiv.org/pdf/2310.03984.pdf", "db4edc42-fa93-4822-8a60-f0c7116ffa57"),
    "G10": ("2025_CIKM_SEC_Stratified-Expert-Cloning.md",
            "https://arxiv.org/pdf/2504.05628.pdf", "d9a6d934-5dad-4efc-8e08-c62a0184f137"),
    "G11": ("2026_arXiv_OCARM_Post-Conversion-Content-Retention.md",
            "https://arxiv.org/pdf/2604.25839.pdf", "7f131324-1d54-4dd2-8a1c-98f5f0ce8dfd"),
    "G12": ("2026_ICLR_ALM-MTA_Front-Door-Causal-Multi-Touch-Attribution.md",
            "https://arxiv.org/pdf/2605.08881.pdf", "42ed27d5-3e90-483f-b728-e5cdab72cfcd"),
    "G13": ("2023_RecSys_IURO_Interpretable-User-Retention-Modeling.md",
            "https://dl.acm.org/doi/pdf/10.1145/3604915.3608818", "47cf0db1-92bc-49da-b44f-af65cea80083"),
    "G14": ("2026_TOIS_IURO+_Rethinking-User-Retention-Modeling.md",
            "https://dl.acm.org/doi/pdf/10.1145/3790098", "dc389695-c31e-4eba-a1d2-00268bcf0ac1"),
    "G15": ("2025_KDD_NA_Interleaving-Counterfactual-Airbnb-Search.md",
            "https://arxiv.org/pdf/2508.00751.pdf", "4c1119dd-6713-4864-a194-a53a14065084"),
    "G16": ("2025_JMLR_ImpatientBandits_Optimizing-Recommendations-Long-Term.md",
            "https://arxiv.org/pdf/2501.07761.pdf", "c7d8e9d2-5ee2-4cbf-ab8a-15cba733edc1"),
    "G17": ("2023_WWW_DT4Rec_User-Retention-Oriented-Decision-Transformer.md",
            "https://arxiv.org/pdf/2303.06347.pdf", "cf9de03f-0d61-4f7e-85ee-1cc46fb9ef3c"),
    "G18": ("2026_arXiv_NA_Incremental-Recommendation-Causal-Models.md",
            "https://arxiv.org/pdf/2608.26804.pdf", "15cdd352-b889-48d8-a3d5-4bdabefd67f8"),
    "G19": ("2024_RecSys_LRF_Learned-Ranking-Function-YouTube.md",
            "https://arxiv.org/pdf/2408.06512.pdf", "9a650298-5c0c-48d2-9597-450c32a73457"),
    "G20": ("2022_arXiv_NA_Long-run-User-Value-Optimization-Meta.md",
            "https://arxiv.org/pdf/2204.11421.pdf", "d017d9e2-9833-4411-b351-5d5a4fe920cc"),
    "G21": ("2022_KDD_NA_Surrogate-Long-Term-User-Experience.md",
            "https://dl.acm.org/doi/pdf/10.1145/3534678.3539073", "cb0d9351-5064-4c9b-b669-e5f25fe0203f"),
    "G22": ("2024_arXiv_NA_Sequential-Rec-Immediate-Feedback-Long-term-Retention.md",
            "https://arxiv.org/html/2404.03637", "305cd94b-33e0-46f8-961a-2228a9d46046"),
    "G23": ("2026_arXiv_DownstreamRewards_Long-Term-Engagement-Optimization.md",
            "https://arxiv.org/html/2607.14192", "1a74145c-f8bc-438b-a5ea-965b29abab16"),
    "G24": ("2026_arXiv_DCEO_Direct-Causal-Effect-Optimization.md",
            "https://arxiv.org/html/2608.25635", "d18bf088-6fb0-4082-952c-2a13f61ffc2e"),
    "G25": ("2020_KDD_RDSA_Sleeping-Recovering-Bandit-Notifications.md",
            "https://research.duolingo.com/papers/yancey.kdd20.pdf", "3f40b05f-169b-4e36-b317-fdadf7a86bc1"),
    "G28": ("2026_RecSys_PROMISE_Process-Reward-Generative-Recommendations.md",
            "https://arxiv.org/pdf/2601.04674.pdf", "df98b8e9-3fd2-465d-8f1b-23d0c51a8048"),
    "G29": ("2026_RecSys_ResidualDominance_Last-Item-Reliance-Causal-Attention.md",
            "https://arxiv.org/pdf/2608.14021.pdf", "9dc30dae-7a13-4032-9339-5cf10dc1bc6a"),
    "G30": ("2026_RecSys_STEPS_Self-Triggered-Agentic-Push.md",
            "https://arxiv.org/pdf/2608.01949.pdf", "9419d0b9-b40e-4e9c-8b49-5f24c45408ec"),
    "G31": ("2026_RecSys_UniShare_Joint-Video-Receiver-Recommendation.md",
            "https://arxiv.org/pdf/2602.09618.pdf", "4824001b-1aa6-4c8e-9ff8-b77d45e029b4"),
    "G32": ("2026_RecSys_MODE_Mutual-Optimality-Direct-Effects.md",
            "https://arxiv.org/pdf/2608.01731.pdf", "204da68c-fb51-4df5-bd81-c2cb797e35a9"),
    "G33": ("2026_RecSys_ControlFunction_Mitigating-Position-Bias-LTR.md",
            "https://arxiv.org/pdf/2506.06989.pdf", "7915e99c-f464-494a-9ea5-dfb873b4d91f"),
    "G34": ("2026_RecSys_NA_Spillover-Contained-Social-AB-Testing.md",
            "https://arxiv.org/pdf/2602.08569.pdf", "65d84922-448a-4dd1-950f-148e5c690bc9"),
    "G35": ("2026_RecSys_NA_Convergent-Validity-Offline-Evaluation.md",
            "https://arxiv.org/pdf/2607.25097.pdf", "7fedeced-8eec-409c-adc9-cff816b1f314"),
    "G36": ("2026_RecSys_DeltaGate_Zero-Observation-User-Reactivation.md",
            "https://arxiv.org/pdf/2607.19802.pdf", "5e293de3-47dc-4334-97d6-e9bd99c3bfed"),
    "G37": ("2026_RecSys_NA_Live-Streaming-Multi-Objective-Ranking.md",
            "https://arxiv.org/pdf/2608.04455.pdf", "f678e8c0-439b-4d8b-892f-d9df02becb0a"),
    "G38": ("2026_RecSys_GPBM_Generalized-Position-Based-Model.md",
            "https://www.amazon.science/publications/generalized-position-based-model-rethinking-position-weights-in-ranking-off-policy-evaluation",
            "9473661a-49fd-4ede-9ff0-ba2c686cf56f"),
    "G39": ("2026_RecSys_TSMOO_Multi-Objective-Constrained-Thompson-Sampling.md",
            "https://www.amazon.science/publications/tsmoo-solving-multi-objective-experimentation-with-constrained-thompson-sampling",
            "8119ba67-ed0b-427c-9ffe-03ccc1da6d87"),
    "G40": ("2026_RecSys_CascadeReward_Preranking-Alignment-Accuracy.md",
            "https://raw.githubusercontent.com/pellera9/cascade-reward-preranking/main/main.pdf",
            "62a7348a-4f29-4478-9fd8-8e8ae72cffc9"),
}

def parse_answer(stdout):
    stdout = stdout.strip()
    if not stdout:
        return ""
    try:
        obj = json.loads(stdout)
        if isinstance(obj, dict):
            v = obj.get("value") or obj
            if isinstance(v, dict) and "answer" in v:
                return v["answer"]
            if "answer" in obj:
                return obj["answer"]
    except json.JSONDecodeError:
        pass
    return stdout

def title_from(facts, fallback):
    m = re.search(r"\*\*Title:\*\*\s*\*?(.+?)(?:\n|$)", facts)
    if m:
        return re.sub(r"[*_]", "", m.group(1)).strip().strip("*")
    m = re.search(r"#+\s*(.+)", facts)
    return (m.group(1).strip() if m else fallback)

def q2_class(proj):
    m = re.search(r"\b(TRUE|PARTIAL|NOT)\b", proj)
    return m.group(1) if m else "UNSPECIFIED"

def assemble(gid, path):
    data = json.load(open(path))
    facts = proj = ""
    for q in data.get("queries") or []:
        ans = parse_answer(q.get("stdout") or "")
        if q.get("tag") == "facts":
            facts = ans
        else:
            proj = ans
    if not facts and not proj:
        return None
    fn, url, sid = FILES.get(gid, (f"{gid}.md", "", data.get("source_id", "")))
    title = title_from(facts, gid)
    cls = q2_class(proj)
    body = f"""# {title}

**Source:** {url}  
**Date analyzed:** 2026-09-24  
**NLM source id:** `{sid}`  
**Queue id:** {gid}  
**Q2 class:** {cls}

---

## 1. Summary

{facts or "Not specified in source."}

---

## 2. Evidence

See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

## 3. Limitations

See limitations in §1 if present. Replace any NLM refusal with: Not specified in source.

---

## 4. Prior works named

See cited prior works in §1.

---

## 5. Project Relevance

{proj or "Not specified in source."}

---

## 6. Community Reaction

No significant community discussion searched at card-write time; extraction is NLM-scoped.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**PDF:** ingested via NotebookLM  
**Relevance:** Core if Q2 class is TRUE or PARTIAL or Q1 industry system; else Related  
**Priority:** see queue.md `{gid}`
"""
    outp = os.path.join(OUT, fn)
    open(outp, "w").write(body)
    return outp

def main():
    n = 0
    only = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    for p in sorted(glob.glob(os.path.join(RAW, "G*_*.json"))):
        gid = os.path.basename(p).split("_")[0]
        if only and gid not in only:
            continue
        if not only:
            try:
                n_id = int(gid[1:])
            except ValueError:
                n_id = 0
            if n_id < 28:
                continue
        out = assemble(gid, p)
        if out:
            print("wrote", out)
            n += 1
    print("cards", n)

if __name__ == "__main__":
    main()
