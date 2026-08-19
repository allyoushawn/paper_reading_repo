# Survey Card

| Field | Value |
|-------|-------|
| **Title** | Recommending What Video to Watch Next: A Multitask Ranking System |
| **Authors / Company** | Zhezhao Zhao, Lichan Hong, Li Wei, et al. / Google |
| **Venue / Year** | RecSys 2019 |
| **URL** | https://doi.org/10.1145/3298689.3346997 |
| **Source type** | Industry paper |
| **Direction** | D1 |
| **Problem setting** | YouTube next-video ranking: pointwise multi-objective LTR over hundreds of candidates per query video, trained on logged implicit feedback at billion-user scale |
| **Objective + label + horizon + delay** | Engagement objectives (click classification, watch-time regression) and satisfaction objectives (like classification, survey-rating regression); per-impression labels from user logs; online eval uses time spent and survey ratings |
| **Prediction or incrementality** | Prediction (multi-task pointwise classification/regression heads) |
| **Architecture** | Wide & Deep extended with Multi-gate Mixture-of-Experts (MMoE) soft-parameter sharing plus shallow side-tower for position-bias correction (click position × device) |
| **Credit assignment** | Not specified in source for user-level delayed outcomes; per-item pointwise prediction only |
| **Training / counterfactual** | Sequential temporal training on YouTube logs; position side-tower trained jointly; 10% gating dropout and 10% position feature dropout; serving omits position feature |
| **Offline / online eval** | Offline: AUC (classification), squared error (regression); online: A/B tests on engagement (time spent) and satisfaction (survey ratings) |
| **Reported gains** | Live YouTube A/B (same model complexity): MMoE 4-expert vs shared-bottom 3.7M mults — +0.20% engagement, +1.22% satisfaction; MMoE 8-expert vs shared-bottom 6.1M — +0.45% engagement, +3.07% satisfaction |
| **Dating applicability** | Direct template for multi-objective ranking when short-term engagement (swipe/like) conflicts with longer satisfaction signals. Manual weighted-multiplication fusion of heads is the production pattern to beat when moving toward unified LTV/retention value. |
| **Unverified claims** | None beyond NLM source extraction; Q2/Q3 follow-up queries failed (MCP disconnect). |

**Community Reaction:** No significant community discussion found.

---

## 1. Core Problem and Key Contribution

**Core problem:** Industrial video ranking must balance multiple competing objectives (engagement vs satisfaction), learn from implicitly biased logged feedback (especially position bias), handle multimodal sparse features, and serve pointwise scores in real time at billion-user scale.

**Key contributions:**
- End-to-end multi-objective pointwise ranking system for YouTube next-video recommendation.
- MMoE soft-parameter sharing across engagement and satisfaction task families.
- Wide & Deep–style shallow side-tower for position-bias modeling without random exploration.
- Production deployment with significant online engagement and satisfaction gains.

## 2. Proposed Method or Architecture

Tasks split into engagement (clicks, watch completion/time) and satisfaction (likes, dismissals, survey ratings), trained with cross-entropy or squared loss. MMoE replaces shared-bottom layers: fixed expert MLPs with per-task softmax gating over experts, then task-specific towers. Final ranking score at serving is a **manually tuned weighted multiplication** of task predictions.

Position bias: shallow tower takes click position crossed with device type, adds bias logit to engagement classification during training; position treated as missing at serving. Stabilization: 10% dropout on gating networks (mitigates expert polarization); 10% position feature dropout.

## 3. Datasets and Baselines

**Data:** YouTube production logs (1.9B MAU); sequential temporal training. **Offline metrics:** AUC, squared error. **Online:** A/B on time spent and survey ratings.

**Baselines:**
- Shared-bottom multi-task model (matched complexity: 3.7M or 6.1M multiplications).
- Position bias: position-as-input with fixed/missing value at serve; adversarial position-prediction with negated gradients into main model.

## 4. Key Quantitative Results

| Model | Multiplications | Engagement Δ | Satisfaction Δ |
|-------|-----------------|----------------|----------------|
| Shared-bottom | 6.1M | +0.1% | +1.89% |
| MMoE (4 experts) | 3.7M | +0.20% | +1.22% |
| MMoE (8 experts) | 6.1M | +0.45% | +3.07% |

Shared-bottom 3.7M baseline deltas not reported in source table. Authors report significant offline and live improvements for both MMoE and position-bias correction components.

## 5. Limitations and Failure Modes

- Chose pointwise over pair/listwise ranking for serving scalability (diversity not optimized via listwise loss).
- Final objective weights manually tuned, not learned end-to-end.
- MMoE gating networks exhibit polarization (~20% of distributed runs) without dropout.
- Position-bias method addresses one selection-bias type; broader implicit biases remain an open question per authors.

## 6. Top Cited Prior Works

1. Wide & Deep (Cheng et al.) — base architecture extended.
2. Multi-gate Mixture-of-Experts / MMoE (Ma et al.) — soft-parameter sharing.
3. Mixture-of-Experts (Jacobs et al.) — expert modularization.
4. Learning to rank framework (Liu) — problem formulation.
5. Position bias in implicit feedback (Joachims et al.).
6. YouTube two-stage recommender / candidate generation (Covington et al.).
7. Adversarial domain adaptation / fairness (Ganin et al.; Zhang et al.) — adversarial position baseline.

---

## Project Relevance (Q3)

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | CTR-like engagement proxies (clicks, watch time) plus satisfaction proxies (likes, dismissals, survey ratings). Retention, LTV, and revenue not specified as ranking objectives. |
| **(2) Credit assignment** | Not specified in source for mapping user-level delayed outcomes to item-level decisions. |
| **(3) Label / horizon; delay / sparsity / censoring** | Per-impression implicit feedback labels; sequential training on past days. Delay, sparsity, and censoring of long-term outcomes not specified in source. |
| **(4) Short-term vs long-term head fusion** | **Fixed** (manually tuned weighted multiplication of multiple prediction heads at serving). |
| **(5) Prediction vs incrementality** | **Prediction** (pointwise multi-task supervised learning). |
| **(6) Offline / online eval; delayed retention; two-sided interference** | Offline AUC and squared error; online A/B on time spent and survey ratings. Delayed retention metrics and two-sided interference not specified in source. |
| **(7) Reciprocity, congestion, fairness, revenue vs match quality** | Not specified in source. |
| **(8) Migration path from CTR-like model to unified long-term model** | Not specified in source. |

---

## Reverse Citation Map

*(blank)*

---

## Meta Information

| Field | Value |
|-------|-------|
| **Date analyzed** | 2026-08-16 |
| **Workplace** | cursor-grok |
| **NLM source ID** | a130cd67-9f8e-488b-b844-aa91ba854ef2 |
| **Notebook ID** | 67046a44-7490-4fe5-b54a-3f39ef37fdd3 |
