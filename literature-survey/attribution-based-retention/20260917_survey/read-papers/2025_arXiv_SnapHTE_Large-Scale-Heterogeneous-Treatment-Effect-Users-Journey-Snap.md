# A Large Scale Heterogeneous Treatment Effect Estimation Framework and Its Applications of Users' Journey at Snap

**Source:** https://arxiv.org/pdf/2512.03060.pdf | **NLM source id:** 59173a97-7b15-4ae3-a813-1e80790cddf1 | **Year / venue:** 2025-12, arXiv:2512.03060, Snap (retrieved paper text carries an unedited "CJO2022" ACM template placeholder venue string, treated as a template artifact rather than the actual venue) | **Authors / affiliation:** Li Shi, Jing Pan, Paul Lo, Jonathan Grotts, Crystal Pan, Ben Thompson, Mattia Fumagalli, Amit Adur — Snap Inc., Santa Monica, CA | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Standard ranking/targeting labels are merely correlated with desired outcomes (e.g. clicks), not causal, and industrial CATE/uplift estimation at hundreds-of-millions-of-users scale faces low signal-to-noise A/B logs, concept drift, and slow retraining. The paper presents a production HTE framework: a T-learner (two-model) meta-learner trained on randomized Intent-To-Treat A/B experiment data (guaranteeing unconfoundedness by design) over ~1,000 user features, using a Deep & Cross Network as the base learner, deployed on TFX with weekly incremental training (not full retrain-from-scratch). Two applications: **User Influenceability** (incremental ad-conversion probability from seeing ads) and **User Sensitivity** (incremental drop in engagement metrics from ad exposure, via no-ads holdout experiments). **Unit of credit:** per user (individual CATE/ITE score), not per touchpoint. **Outcome:** incremental ad conversion (Influenceability) and incremental engagement/retention-type metrics (Sensitivity). **Bias handling:** randomized-experiment (ITT) training data plus the T-learner's separate treatment/control models directly subtract out "activity bias" — organic conversion/engagement a hyperactive user would show regardless of treatment.

## 2. Evidence
Data selection tuned via 160 real experiments; best rule (V5: ≤90-day recency, >10k control users, >3δ relative lift) maximized AUUC. Base-learner comparison over 35 studies: DCN 0.59±0.11 AUUC vs DNN 0.51±0.10 vs Wide&Deep 0.50±0.11. Incremental weekly training beat full weekly retraining by >100% in AUUC after 2+ weeks online (evaluated on 18 production models, 1.2B observations). Live A/B test of User Influenceability scores in targeting drove a 6x improvement over standard significance thresholds on key business metrics; 18 User Sensitivity models showed a 20% average AUUC gain over random targeting.

## 3. Limitations
Old (>180-day) or small-control-group experiments introduce noise/concept drift and must be filtered out. Standard weekly batch retraining from scratch forgets historical patterns and underperforms incremental training by >50% AUUC after two weeks. Mobile OS privacy restrictions (e.g. App Tracking Transparency) degrade deterministic user-level conversion tracking, reducing training-label quality/quantity.

## 4. Prior works named
- Künzel et al. (2019) — meta-learners (S/T/X/R-learner) for HTE
- Wang et al. (2017) — Deep & Cross Network
- Cheng et al. (2016) — Wide & Deep learning
- Gutierrez & Gérardy (2017) / Sołtys et al. (2015) — uplift modeling / AUUC review
- Chen et al. (2020) — CausalML package

## 5. Project Relevance
- **Answers:** Q1 (also touches Q2 via the User Sensitivity application)
- **Attributes retention to individual interactions?** Partly — User Sensitivity estimates incremental engagement/retention-type impact per user from ad-exposure holdouts, but it is a user-level uplift score, not a per-touchpoint/sequence credit decomposition.
- **Transferable components:** T-learner with randomized-holdout debiasing to isolate true incremental lift from organic ("would-happen-anyway") activity; DCN base architecture; incremental (non-catastrophic-forgetting) weekly retraining pipeline; AUUC-based uplift evaluation.
- **Required changes:** Move from a single scalar per-user CATE to per-swipe/per-touchpoint fractional credit; ingest heterogeneous, multi-stage event types (swipe, match, message) with temporal structure rather than static user features; retarget from ad-conversion/engagement-drop to a recurring N7 active-on-day-7 label.
- **On last-touch:** Not addressed directly; the paper's broader critique is that correlated (non-causal) labels generally mislead ranking/targeting systems, which is consistent with the last-touch critique but not phrased that way.
- **Transfer rating:** adaptable — the T-learner/holdout-debiasing and incremental-training machinery transfer well; the credit unit needs to shift from per-user to per-interaction.
