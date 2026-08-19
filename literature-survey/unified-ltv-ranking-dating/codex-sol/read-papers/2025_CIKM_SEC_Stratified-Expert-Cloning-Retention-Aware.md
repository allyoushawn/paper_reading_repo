# Paper Analysis: Stratified Expert Cloning for Retention-Aware Recommendation at Scale

**Source:** https://arxiv.org/html/2504.05628v2  
**Date analyzed:** 2026-08-18  
**Source ID:** a6817bf6-d4cc-4dbd-b56e-5c02533ff462  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** Q1/Q2/Q3 not started after generative-query plateau; source fallback completed

---

## Required Survey Card Fields

- **Title:** Stratified Expert Cloning for Retention-Aware Recommendation at Scale
- **Authors or company:** Not specified in selected-source metadata
- **Venue:** CIKM
- **Year:** 2025
- **URL:** https://arxiv.org/html/2504.05628v2
- **Source type:** industry paper
- **Direction:** D2
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1.
- **Prediction or incrementality:** Not specified in source. The indexed evidence supports outcome/utility prediction or optimization, not exposure-effect identification.
- **Model architecture:** See §1, “Architecture.”
- **Credit assignment:** See §1, “Credit assignment.”
- **Training data and counterfactual handling:** See §1 and the prediction/incrementality field above.
- **Offline and online evaluation:** See §2.
- **Reported gains:** See §2; no metrics are added beyond indexed-source evidence.
- **Applicability to a two-sided dating recommender:** See § Project Relevance.
- **Unverified claims:** All dating transfer statements below are survey inference, not claims made by the source.

---

## 1. Summary

### Core problem and contribution — indexed-source evidence

- Describe the issue below: Description: Submit without GitHub Submit in GitHub arXiv is now an independent nonprofit!
- Report Issue Back to Abstract Download PDF javascript:toggleNavTOC(); javascript:toggleReadingMode(); Abstract.
- User retention is critical in large-scale recommender systems, significantly influencing online platforms' long-term success.

### Objective — indexed-source evidence

- User retention is critical in large-scale recommender systems, significantly influencing online platforms' long-term success.
- Our objective is to learn a recommendation policy π : 𝒮 → 𝒜 \pi:\mathcal{S}\rightarrow\mathcal{A} that maximizes the expected long-term user retention: (1) max π…
- Reinforcement learning (RL) methods, though promising for optimizing long-term rewards, face challenges like delayed credit assignment and sample inefficiency.

### Label definition, horizon, delay, sparsity, and censoring — indexed-source evidence

- User retention is often measured by metrics such as the number of active days within a given time window or the time until the…
- Reinforcement learning (RL) methods, though promising for optimizing long-term rewards, face challenges like delayed credit assignment and sample inefficiency.
- 2024a ) treat user retention as probabilistic flows over sessions, effectively handling sparse and delayed signals.

### Architecture — indexed-source evidence

- We parameterize the policy π k \pi_{k} using a neural network architecture that consists of two main components: a state encoder f ϕ f_{\phi}…
- Reinforcement learning (RL) methods, though promising for optimizing long-term rewards, face challenges like delayed credit assignment and sample inefficiency.
- We introduce Stratified Expert Cloning (SEC), an imitation learning framework that leverages abundant interaction data from high-retention users to learn robust policies.

### Credit assignment — indexed-source evidence

- Reinforcement learning (RL) methods, though promising for optimizing long-term rewards, face challenges like delayed credit assignment and sample inefficiency.
- 2024a ) treat user retention as probabilistic flows over sessions, effectively handling sparse and delayed signals.

### Training data and baselines — indexed-source evidence

- T-SNE visualization of user state embeddings from the KuaiRand dataset, categorized by expert levels based on retention patterns.
- Extensive offline evaluations and online A/B tests on major video platforms (Kuaishou and Kuaishou Lite) with hundreds of millions of users validate SEC's effectiveness.
- Left: During training, the framework learns specialized recommendation policies through behavior cloning from users at multiple high-retention expert levels.
- Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor.

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- Extensive offline evaluations and online A/B tests on major video platforms (Kuaishou and Kuaishou Lite) with hundreds of millions of users validate SEC's effectiveness.
- Through comprehensive offline and extensive online A/B tests on two major video platforms, SEC substantially improves user retention compared to state-of-the-art methods, highlighting its…
- Baselines and Metrics We benchmark against CEM ( Rubinstein and Kroese 2004 ) , DIN ( Zhou et al.
- User retention is critical in large-scale recommender systems, significantly influencing online platforms' long-term success.

### Reported gains — indexed-source evidence

- Results show substantial improvements, achieving cumulative lifts of 0.098% and 0.122% in active days on the two platforms respectively, each translating into over 200,000…
- Together, these components form a comprehensive framework that effectively leverages expert behaviors to improve user retention in large-scale recommender systems.

### Limitations and negative results — indexed-source evidence

- Reinforcement learning (RL) methods, though promising for optimizing long-term rewards, face challenges like delayed credit assignment and sample inefficiency.

**Statistical validity:** Not specified in source beyond the evidence snippets above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - Experimental Setup We deployed SEC on Kuaishou and Kuaishou Lite platforms, each with over 200 million daily active users.
- User retention is critical in large-scale recommender systems, significantly influencing online platforms' long-term success.  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - Imitation Learning Reinforcement Learning (RL), though effective for long-term optimization, faces challenges like high sample complexity and risks from exploration, particularly in recommender systems.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** See the source-grounded contribution and architecture evidence in §1.  
**Prior work comparison:** Not specified in source. Raw indexed content does not establish a defensible top-5–7 citation-frequency ranking.  
**Verification:** No independent novelty verification was performed in this fallback batch.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Dataset or production logs described by the source | Not specified in source. | Not specified in source. | Evidence appears in §1 when available. |

**Offline experiment reproducibility:** Not specified in source.

---

## 6. Community Reaction

Not specified in source.

---

## Project Relevance

**Source-grounded facts:** The indexed-source evidence above identifies the paper's objective, architecture, labels, attribution mechanism, and evaluation where available.

**Survey inference:** The paper may inform long-horizon retention optimization or request-level credit assignment. This transfer is unverified. A dating deployment needs 7–30 day retention and weeks-long revenue labels while preserving like, match, and conversation auxiliaries during migration.

**Prediction vs. incrementality:** Not specified in source. The indexed evidence supports outcome/utility prediction or optimization, not exposure-effect identification.

**Reciprocity and congestion:** Not specified in source unless explicitly present above. Candidate-side capacity and bilateral acceptance require an added reciprocal or marketplace layer.

**Cascade and low base rates:** Mapping the method onto impression → like → match → conversation → retention/revenue is survey inference and requires sparse-label calibration.

**Success paradox:** Not specified in source. A dating system must protect match quality and successful outcomes so retention/revenue optimization does not punish successful matching.

**Evaluation implication:** Where source evidence exists, reproduce its offline/online protocol; add bilateral metrics, candidate exposure concentration, and incrementality validation.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** Not specified in selected-source metadata (individual authors not taken from selected-source metadata)  
**Affiliations:** Not specified in selected-source metadata  
**Venue:** CIKM  
**Year:** 2025  
**PDF:** NotebookLM indexed source available  
**Relevance:** Core  
**Priority:** 1
