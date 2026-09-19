# Retentive Relevance: Capturing Long-Term User Value in Recommendation Systems

**Source:** https://arxiv.org/pdf/2510.07621.pdf | **NLM source id:** 3aa276f2-3423-47de-b659-ac3acf484bdc | **Year / venue:** arXiv 2510.07621, 2025 | **Authors / affiliation:** Saeideh Bakhshi, Phuong Mai Nguyen, Cayman Simpson, Qifan Wang (Meta, Menlo Park); Robert Schiller, Tiantian Xu (Meta, New York); Pawan Kodandapani (Meta, Boston); Andrew Levine (Meta, San Francisco) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Recommenders rely on noisy, sparse short-term implicit engagement (clicks, likes) or retrospective satisfaction surveys (Worth Your Time, Interest Matching), which fail to capture forward-looking intent driving long-term retention — especially for cold-start/low-signal users. The paper introduces "Retentive Relevance": a content-level survey item asked immediately after consumption ("How likely are you to return to [Platform] to view more posts like this?"), grounded in the Theory of Planned Behavior (behavioral intentions are the strongest predictor of future behavior). It validates convergent/discriminant validity and shows the signal is nearly orthogonal to traditional engagement (mutual information < 0.15 with likes/saves/reshares/comments).

Unit of credit: per recommended item / user-item pair (u,v) — a proxy logistic-regression model predicts P(RR_{u,v}=1), trained on the survey label, and this is combined into final ranking as score_final = score_base + boost − demote using precision-calibrated thresholds (τ_boost=0.76 at 80% precision, τ_demote=0.38 at 60% precision; neutral zone unadjusted). Outcome attributed: next-day user retention (y_i∈{0,1}, views on day+1 exceeding the 5th-percentile active-user threshold) offline, and sessions-per-user online. Bias handling: Covariate Balancing Propensity Score (CBPS) weighting corrects survey non-response bias (achieving |SMD|<0.1 across covariates); survey triggers appear randomly regardless of prior interaction to avoid selection into the sample; offline retention models control for 28-day historical engagement, same-day activity, and content/user features, and SHAP shows "Very Likely" responses add +8.3pp to retention probability for low-signal users vs. only +0.8pp for likes.

## 2. Evidence
- Survey collection: N=63,708 (Retentive Relevance), 58,872 (Interest Matching), 76,263 (Worth Your Time), Dec 2024–Jan 2025, 18 countries, Meta video feed.
- Next-day retention offline prediction (10-fold CV): overall sample baseline 78.0% acc / 0.830 AUC → +Retentive Relevance 83.0% acc (+5.0pp, p<0.001) / 0.860 AUC (Cohen's d=2.1); neither Worth Your Time (78.0%/0.828) nor Interest Matching (78.2%/0.838) gave significant gains. Low-signal/cold-start users: baseline 73.0%/0.630 → 76.0% (+3.0pp)/0.700 (+0.070), Cohen's d=3.2.
- Live 14-day A/B on Meta's video feed: sessions per user +0.030%±0.026 (p<0.05); communication activity +0.052%; like rate +0.169%; skip rate −0.188%; reported content −1.36%; negative feedback −1.527%; "not interested" −2.6%.
- Baselines: no-survey baseline model, +Worth Your Time, +Interest Matching, traditional implicit engagement features.

## 3. Limitations
- Single-interaction scope: captures value/intent of one recommendation, not broader session context or multi-step sequences (explicitly named as future work).
- Neutral Likert responses (rating 3) excluded from proxy training — including them degraded AUC by 2.3%.
- Requires ongoing survey infrastructure and continuous proxy-model inference in production (operational cost).

## 4. Prior works named
- Ajzen 1991 / Fishbein & Ajzen 1975 — Theory of Planned Behavior (behavioral intent as retention predictor)
- Cai et al. 2023, RLUR — *Reinforcing User Retention in a Billion Scale Short Video Recommender System* (production retention-optimization baseline)
- Joachims, Swaminathan & Schnabel 2017 / Schnabel et al. 2016 — unbiased learning-to-rank / recommendations-as-treatments (propensity debiasing basis for CBPS)
- Cheng et al. 2016 (Wide & Deep) / Covington et al. 2016 (YouTube DNN) — multi-stage ranking architectures the proxy model integrates into
- Lundberg & Lee 2017 — SHAP values (feature-importance interpretability)

## 5. Project Relevance
- **Answers:** Q2
- **Attributes retention to individual interactions?** partly — predicts a per-item (u,v) forward-looking retention-intent proxy and uses it to boost/demote that item in ranking, but does not perform multi-touch sequence credit attribution (e.g., Shapley/counterfactual path masking) across a user's swipe/like/match/message history.
- **Transferable components:** forward-looking behavioral-intent labels as a stronger ground truth than implicit signals (adaptable to "How likely to return after swiping/matching on this profile?"); CBPS propensity debiasing for power-swipers vs. cold-start users; precision-calibrated boost/demote score adjustment at the ranking stage; the finding that intent proxies are disproportionately valuable for low-signal/cold-start users.
- **Required changes:** extend from single-item intent prediction to multi-touch sequence attribution across a full swipe→like→match→message journey; incorporate heterogeneous dating-funnel touch types rather than homogeneous video views; re-anchor the binary next-day retention target to a rolling N7 active-retention indicator.
- **On last-touch:** does not name last-touch/last-click explicitly, but shows short-term implicit engagement signals are nearly orthogonal to actual return intent (MI<0.15) and fail to predict next-day retention, while alternative retrospective surveys also add nothing — evidence that myopic/implicit touchpoint signals (the same class as last-touch) underperform forward-looking intent measures.
- **Transfer rating:** adaptable — a per-item intent-prediction and ranking-adjustment framework, not a multi-touch attribution model, but its intent-based labeling, debiasing, and calibrated score-adjustment architecture transfer well to candidate-profile retention ranking.
