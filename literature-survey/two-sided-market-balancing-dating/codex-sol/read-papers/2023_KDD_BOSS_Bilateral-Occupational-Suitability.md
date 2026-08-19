# Paper Analysis: BOSS: A Bilateral Occupational-Suitability-Aware Recommender System for Online Recruitment

**Source:** https://www.kdd.org/kdd2023/wp-content/uploads/2023/08/toc.html  
**Date analyzed:** 2026-08-18

---

## 1. Summary

**Title:** BOSS: A Bilateral Occupational-Suitability-Aware Recommender System for Online Recruitment  
**Authors:** Xiao Hu, Yuan Cheng, Zhi Zheng, Yue Wang, Xinxin Chi, Hengshu Zhu  
**Abstract:** Online recruitment combines different participant roles, reciprocal acceptance, and a multi-stage action funnel. BOSS separates job-seeker and recruiter experts, routes stage-specific tasks through separate gates, and estimates click, apply, review, and accept as a chain of conditional probabilities.

**Key contributions:**
- Models bilateral, reciprocal, and sequential recruitment properties jointly.
- Introduces two independent Mixture-of-Experts groups with task-specific gates.
- Demonstrates offline gains on five domains and an online acceptance-rate lift.

**Methodology:** Profile, context, and successful-history embeddings feed feature-interaction experts. Job-seeker gates support click/apply; recruiter gates support review/accept. The four-stage probabilities multiply through the funnel and train end-to-end with summed binary cross-entropy losses.

**Main results:** With inner-product interactions, Technology AUC is 0.8918 ± 0.0021 versus PLE at 0.8875 ± 0.0030. A live Information Technology test lasting more than half a month reports a 6.15% average lift in job-seeker acceptance rate.

---

## 2. Experiment Critique

**Design:** Five large BOSS Zhipin domains, chronological 90/5/5 splits, 20 repeated runs, multi-task baselines, four feature-interaction variants, and sensitivity tests for expert counts and group counts.

**Statistical validity:** Paired t-tests at 0.01 are reported. BOSS is not uniformly best: Service without feature interaction gives 0.8452 AUC versus ESMM at 0.8454, and Marketing with Cross Network gives 0.7910 versus ESMM at 0.7927.

**Online experiments (if any):** More than half a month in Information Technology; acceptance rate improves 6.15%. Traffic allocation, sample size, confidence interval, randomization details, and guardrails are not specified.

**Reproducibility:** Optimizer, architecture, batch size, initialization, and splits are described. Code and random seeds are not specified; all datasets are proprietary.

**Overall:** Offline and online evidence supports deeper-funnel reciprocal scoring. The online disclosure is too sparse to assess interference or long-term market effects.

---

## 3. Industry Contribution

**Deployability:** The selected two-group, six-expert configuration explicitly balances prediction gain against serving cost.

**Problems solved:** Bilateral feature semantics, sample-selection bias across a sparse action funnel, and task conflict between proactive and reactive decisions.

**Engineering cost:** Multiple experts and gates increase parameters and latency; 12 groups require 42.1M parameters and 210.3 seconds per million samples versus 27.9M and 78.4 seconds for one group.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** A bilateral, multi-group MoE integrated with an entire-space conditional funnel for recruitment recommendation.

**Prior work comparison:** MMoE supplies gated experts; ESMM supplies conditional entire-space training; PLE supplies separated expert routing; DPGNN motivates two-way preference; Factorization Machines and inner products provide feature interactions.

**Verification:** The primary KDD PDF in NotebookLM identifies the title, authors, venue, affiliations, system, datasets, and experiment.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Technology | Not specified in source | No | 7,274,559 training samples. |
| Manufacturing | Not specified in source | No | 5,575,962 training samples. |
| Service | Not specified in source | No | 9,577,657 training samples. |
| Marketing | Not specified in source | No | 7,249,080 training samples. |
| Arts | Not specified in source | No | 3,057,923 training samples. |

**Offline experiment reproducibility:** Architecture is described, but data and code are unavailable in the source.

---

## 6. Community Reaction

No significant community discussion found.

---

## Project Relevance

**Mechanism:** Map the dating journey into view → like → recipient review → like-back/match. Use independent expert groups for sender and recipient behavior and multiply stage-conditional probabilities to score the final reciprocal outcome.

**Metric/effect:** Technology acceptance AUC reaches 0.8918 ± 0.0021, and the live recruitment test reports 6.15% higher acceptance rate. Conversations, match spread, wasted likes, and two-sided retention are not specified.

**Capacity/congestion:** Not specified in source. The model predicts acceptance but does not constrain inbox load, redistribute exposure, measure concentration, or account for feedback/interference.

**Dating mapping:** Click/apply/review/accept map naturally to view/like/review-like/like-back. Recruitment roles are more asymmetric and structured, while every dater can initiate and receive; concurrent conversation capacity is also much tighter.

**Dating fit: Medium.** Strong funnel-aware like-back model with online evidence, but no Layer-2 capacity allocator or Layer-4 ecosystem experiment.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| No verified inbound mentions within the 45-source corpus. | — | — |

---

## Meta Information

**Authors:** Xiao Hu, Yuan Cheng, Zhi Zheng, Yue Wang, Xinxin Chi, Hengshu Zhu  
**Affiliations:** Career Science Lab, BOSS Zhipin; University of Science and Technology of China  
**Venue:** KDD 2023  
**Year:** 2023  
**PDF:** available in the NotebookLM source; queue URL is the KDD 2023 contents page  
**Relevance:** Core  
**Priority:** 1

---

## Annotated Bibliography Fields

**Title:** BOSS: A Bilateral Occupational-Suitability-Aware Recommender System for Online Recruitment  
**Authors/org:** Xiao Hu, Yuan Cheng, Zhi Zheng, Yue Wang, Xinxin Chi, Hengshu Zhu; BOSS Zhipin and University of Science and Technology of China  
**Year:** 2023  
**Venue/type:** KDD 2023; conference paper  
**Verified link:** https://www.kdd.org/kdd2023/wp-content/uploads/2023/08/toc.html  
**Tier:** 1  
**What they did:** BOSS uses separate job-seeker and recruiter expert groups, explicit feature interactions, task-specific gates, and an entire-space conditional chain for click, apply, review, and accept. Five large platform datasets and a live experiment evaluate the system.  
**Mechanism:** Separate sender and receiver experts, then optimize the full view-to-mutual-accept funnel rather than a shallow unilateral action.  
**Metrics/effect:** Technology AUC 0.8918 ± 0.0021 versus PLE 0.8875 ± 0.0030; live Information Technology acceptance rate improves 6.15% over control.  
**Dating fit + reason:** Medium — maps directly to view/like/review/like-back, but does not model reply capacity, congestion, spread, or retention.  
**Confidence:** High — primary paper and source-scoped evidence; online test details are limited.
