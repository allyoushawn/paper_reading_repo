# Paper Analysis: Leveraging Dwell Time to Improve Member Experiences on the LinkedIn Feed

**Source:** https://www.linkedin.com/blog/engineering/feed/leveraging-dwell-time-to-improve-member-experiences-on-the-linkedin-feed  
**Date analyzed:** 2026-08-18  
**Source ID:** e19bb1d6-433d-460d-a8f5-2b0a2eed5b07  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** Q1/Q2/Q3 not started after generative-query plateau; source fallback completed

---

## Required Survey Card Fields

- **Title:** Leveraging Dwell Time to Improve Member Experiences on the LinkedIn Feed
- **Authors or company:** LinkedIn
- **Venue:** LinkedIn-Engineering
- **Year:** 2020
- **URL:** https://www.linkedin.com/blog/engineering/feed/leveraging-dwell-time-to-improve-member-experiences-on-the-linkedin-feed
- **Source type:** company blog
- **Direction:** D1
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1, “Objective and labels.”
- **Prediction or incrementality:** Not specified in source. The indexed evidence supports outcome/utility prediction or optimization, not exposure-effect identification.
- **Model architecture:** See §1, “Architecture.”
- **Credit assignment:** See §1, “Credit assignment.”
- **Training data and counterfactual handling:** See §1, “Training evidence,” and the prediction/incrementality field above.
- **Offline and online evaluation:** See §2.
- **Reported gains:** See §2; no metrics are added beyond indexed-source evidence.
- **Applicability to a two-sided dating recommender:** See § Project Relevance.
- **Unverified claims:** All dating transfer statements below are survey inference, not claims made by the source.

---

## 1. Summary

### Core problem and contribution — indexed-source evidence

- As members come across content in their feed that they are curious or interested in, they have multiple ways to engage with that content.
- They may take explicit actions by commenting on or resharing posts.
- They might also choose to passively consume the content by reading it (i.e.

### Objective — indexed-source evidence

- However, the work described in this post is just one part of a broader strategy to incorporate dwell time into our AI models and…
- Here alpha, beta, gamma and W are all MOO hyper-parameters that are finely tuned to balance tradeoffs and returns from each aspect of the…
- Figure 2: Feed Multi-Objective Optimization (MOO) function used by Feed Models for ranking the updates for members Dwell Time is Important Dwell time refers…
- We leverage a multi-objective , multi-task framework for second pass systems combining predictive likelihoods from different models into a single combined score for ranking.

### Label definition, horizon, delay, sparsity, and censoring — indexed-source evidence

- For instance, we found that a significant portion of our weekly active users are passive consumers who spend time on the LinkedIn Feed without…
- As depicted in Figure 8 , the previously mentioned challenges caused our initial approaches - directly modeling dwell time values, modeling dwell time percentiles,…
- Modeling only P(skip) is inadequate because the fixed threshold Tskip becomes less effective as user time on the platform increases, leading to a sparse…

### Architecture — indexed-source evidence

- Over the years, our team has continuously evolved different aspects of the systems from large scale modeling architectures , to serving infrastructure and optimizing…
- We leverage a multi-objective , multi-task framework for second pass systems combining predictive likelihoods from different models into a single combined score for ranking.

### Credit assignment — indexed-source evidence

- By identifying the top-K attributes that significantly influence dwell time, such as content type, creator type, and distribution method , we calculated the percentile…
- Through rigorous online A/B testing, we observed an enhancement in user engagement metrics, including sessions, overall time spent, and time spent per post on…

### Training data and baselines — indexed-source evidence

- Topics: Feed Artificial intelligence Machine Learning Related articles High-Signal AI Code Review That Adapts to Your Codebase at Scale Min Chen Aug 13, 2026…

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- Through rigorous online A/B testing, we observed an enhancement in user engagement metrics, including sessions, overall time spent, and time spent per post on…
- Lack of Adaptive Threshold: Utilizing a universal, static threshold for determining "long dwell" could not effectively capture user preferences relative to inherent dwell time…
- These systems maximize for recall, supplying a large set of potential updates to show viewers.

### Reported gains — indexed-source evidence

- Recently, we have used member time spent behavior ( dwell time ) to improve LinkedIn Feed ranking by predicting when members will have a…

### Limitations and negative results — indexed-source evidence

- Figure 3: Distribution of LinkedIn Weekly Active Users: A significant portion passively consumes content in the Feed, a majority actively engage with content in…

**Statistical validity:** Not specified in source beyond the evidence snippets above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - Over the years, our team has continuously evolved different aspects of the systems from large scale modeling architectures , to serving infrastructure and optimizing…
- Topics: Feed Artificial intelligence Machine Learning Related articles High-Signal AI Code Review That Adapts to Your Codebase at Scale Min Chen Aug 13, 2026…  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - Here alpha, beta, gamma and W are all MOO hyper-parameters that are finely tuned to balance tradeoffs and returns from each aspect of the…

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

**Survey inference:** The paper can inform replacing a hand-tuned score blend with learned multi-objective fusion, a delayed-value head, or a staged auxiliary-head design. A dating deployment would need labels at 7–30 day retention and weeks-long revenue horizons and must retain like, match, and conversation heads as stabilizing auxiliaries during migration.

**Prediction vs. incrementality:** Not specified in source. The indexed evidence supports outcome/utility prediction or optimization, not exposure-effect identification.

**Reciprocity and congestion:** Not specified in source unless explicitly present in the evidence above. Candidate-side capacity and bilateral acceptance therefore require an added reciprocal or marketplace layer.

**Cascade and low base rates:** The method may be mapped to impression → like → match → conversation → retention/revenue, but that mapping is survey inference and requires sparse-label calibration.

**Success paradox:** Not specified in source. A dating system must separately guard match quality and successful off-platform outcomes so retention/revenue optimization does not punish successful matching.

**Evaluation implication:** Reproduce the source's offline/online pattern where stated, then add dating-specific bilateral metrics, candidate exposure concentration, and incrementality validation.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** LinkedIn (individual authors not taken from selected-source metadata)  
**Affiliations:** LinkedIn  
**Venue:** LinkedIn-Engineering  
**Year:** 2020  
**PDF:** NotebookLM indexed source available  
**Relevance:** Core  
**Priority:** 1
