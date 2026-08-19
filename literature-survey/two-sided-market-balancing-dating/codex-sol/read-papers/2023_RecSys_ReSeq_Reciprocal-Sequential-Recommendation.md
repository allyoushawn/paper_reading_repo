# Paper Analysis: Reciprocal Sequential Recommendation

**Source:** https://arxiv.org/abs/2306.14712  
**Date analyzed:** 2026-08-18

---

## 1. Summary

**Title:** Reciprocal Sequential Recommendation  
**Authors:** Bowen Zheng, Yupeng Hou, Wayne Xin Zhao, Yang Song, Hengshu Zhu  
**Abstract:** Static reciprocal recommenders miss preference drift and the dual role of every market participant. ReSeq encodes active preference histories causally, passive-feature histories bidirectionally, performs time-sensitive cross-sequence matching, and distills the expensive micro matcher into a low-latency dot-product model.

**Key contributions:**
- Formulates reciprocal recommendation as bilateral sequence matching.
- Introduces dual active/passive sequence encoders and time-sensitive co-attention.
- Distills fine-grained micro matching into a deployable macro scorer.

**Methodology:** Shared decomposed embeddings align both sides. Transformers use a unidirectional mask for evolving active taste and a bidirectional mask for passive traits. Cross-sequence co-attention provides a micro teacher; Margin-MSE transfers its ranking margins to the macro student used online.

**Main results:** ReSeq improves both perspectives on five datasets. On Technology, candidate/recruiter HR@5 is 0.7597/0.7809 versus DPGNN/FMLP-Rec at 0.4521/0.5206. Distillation reduces prediction latency from about 8.7 ms to 0.28 ms per batch.

---

## 2. Experiment Critique

**Design:** Three BOSS Zhipin recruitment datasets and two Stack Exchange datasets compare ReSeq against 13 CF, sequential, and person-job-fit baselines. Temporal splits and component ablations reduce leakage and isolate the masks, shared embedding, time attention, and distillation.

**Statistical validity:** Paired t-tests at 0.01 are reported. ReSeq loses to FMLP-Rec on StackOverflow questioner MRR@5 (0.3235 vs. 0.3428) and NDCG@5 (0.3640 vs. 0.3718).

**Online experiments (if any):** Not specified in source.

**Reproducibility:** Code is available at https://github.com/RUCAIBox/ReSeq/. Temporal splits, loss weights, learning-rate ranges, and early stopping are reported; seeds are not specified.

**Overall:** Strong offline evidence for temporally adaptive bilateral ranking and serving efficiency, but no evidence for market-wide allocation or downstream outcomes.

---

## 3. Industry Contribution

**Deployability:** The distilled macro scorer uses dot products at serving time, making the temporal reciprocal signal compatible with retrieval-scale systems.

**Problems solved:** Preference drift, bilateral sequence sparsity, and prohibitive pairwise cross-sequence latency.

**Engineering cost:** Requires active/passive histories, Transformer training, an expensive teacher, distillation, chronological feature correctness, and monitoring for drift.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First reciprocal sequential recommender with a micro-to-macro distillation design.

**Prior work comparison:** RECON and LFRR model static reciprocal preference; SASRec and BERT4Rec model unilateral sequences; DPGNN models two-way graph preference; BPR supplies the ranking loss.

**Verification:** The primary arXiv paper identifies RecSys 2023 metadata, method, code, datasets, and experiments.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Design/Sale/Technology recruitment | Not specified in source | No | BOSS Zhipin logs; 99.88%-99.97% sparse. |
| StackOverflow | Stack Exchange data | Yes | 42,381 questioners, 25,004 answerers. |
| AskUbuntu | Stack Exchange data | Yes | 6,030 questioners, 3,415 answerers. |

**Offline experiment reproducibility:** Public code and public Q&A data support partial reproduction; recruitment logs are proprietary.

---

## 6. Community Reaction

No significant community discussion found.

---

## Project Relevance

**Mechanism:** Encode evolving outgoing taste and more stable incoming appeal separately, use time-sensitive co-attention to learn the bilateral interaction, then distill it into a cheap macro reciprocal scorer.

**Metric/effect:** Technology candidate/recruiter HR@5 is 0.7597/0.7809; Design is 0.4435/0.3722. Only offline HR/MRR/NDCG and latency are reported—not match volume, conversations, match spread, wasted likes, or retention.

**Capacity/congestion:** Individual temporal preference feedback is modeled, but market-wide feedback is not. Capacity, congestion, exposure concentration, and interference are not specified.

**Dating mapping:** Recruitment interview sequences map to chronological match histories; active encoders model evolving swipe taste and passive encoders model observed appeal. Modern dating histories are noisier, roles are symmetric, and successful matches do not guarantee conversation capacity.

**Dating fit: Medium.** Valuable for recency-aware like-back prediction, but it does not allocate impressions under reply constraints.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| No verified inbound mentions within the 45-source corpus. | — | — |

---

## Meta Information

**Authors:** Bowen Zheng, Yupeng Hou, Wayne Xin Zhao, Yang Song, Hengshu Zhu  
**Affiliations:** Renmin University of China; BOSS Zhipin; Beijing Academy of Artificial Intelligence  
**Venue:** RecSys 2023  
**Year:** 2023  
**PDF:** available via arXiv  
**Relevance:** Core  
**Priority:** 1

---

## Annotated Bibliography Fields

**Title:** Reciprocal Sequential Recommendation  
**Authors/org:** Bowen Zheng, Yupeng Hou, Wayne Xin Zhao, Yang Song, Hengshu Zhu; Renmin University of China and BOSS Zhipin  
**Year:** 2023  
**Venue/type:** RecSys 2023; conference paper  
**Verified link:** https://arxiv.org/abs/2306.14712  
**Tier:** 1  
**What they did:** ReSeq aligns active and passive embedding spaces, encodes chronological bilateral histories with specialized Transformer masks, matches histories through time-sensitive co-attention, and distills the expensive micro model into a dot-product macro scorer. Five real datasets test accuracy and latency.  
**Mechanism:** Model preference drift in both directions, learn fine-grained sequence compatibility offline, and serve a distilled bilateral score at retrieval latency.  
**Metrics/effect:** Technology HR@5 reaches 0.7597 candidate-side and 0.7809 recruiter-side; macro latency is about 0.28 ms/batch versus about 8.7 ms for micro matching.  
**Dating fit + reason:** Medium — strong dynamic reciprocal scorer, but no inbox capacity, congestion cooling, exposure allocation, or retention outcome.  
**Confidence:** High — primary paper, public code, and source-scoped evidence; live dating transfer is untested.
