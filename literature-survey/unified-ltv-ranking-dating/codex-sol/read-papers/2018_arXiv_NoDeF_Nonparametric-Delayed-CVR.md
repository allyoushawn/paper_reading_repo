# A Nonparametric Delayed Feedback Model for Conversion Rate Prediction

- **Source index:** 111
- **Source ID:** `3509eb18-a2a8-4240-bb4d-71f76f3529aa`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Yuya Yoshikawa, Yusaku Imai
- **Affiliations:** Chiba Institute of Technology; CyberAgent
- **Year / venue:** 2018 / arXiv preprint
- **Direction / priority:** D7 delayed feedback / Priority 3
- **URL:** https://arxiv.org/abs/1802.00255

## 1. Summary

NoDeF relaxes the exponential-delay assumption in classic conversion models. It represents the conversion-time distribution as a feature-conditioned weighted sum of kernels centered at pseudo-points on the time axis. A latent variable indicates whether a click will eventually convert, and an EM procedure jointly learns eventual CVR and the nonparametric delay density.

Synthetic tests show recovery of complicated multi-peak delays. On six temporal periods of Criteo data, NoDeF improves recent-campaign log loss to 0.2575 versus 0.2818 for naive training and 0.3689 for exponential DFM; AUC is 0.7242 versus 0.7187 and 0.7213. On all campaigns, NoDeF has the best log loss and accuracy but lower AUC than exponential DFM (0.7387 versus 0.7423), so dominance is not uniform.

## 2. Experiment Critique

The method directly tests the parametric assumption it challenges, uses synthetic ground truth for density recovery, and evaluates repeated temporal slices. Reporting the AUC exception is important.

The real-data comparison uses only two baselines and relatively small 50,000-sample training windows after reducing 2,594 features to 100 PCA components. EM with many kernel points can be computationally heavier and sensitive to bandwidth/pseudo-point choices. The model assumes eventual conversion and delay are adequately captured by observed features; it remains predictive and has no online experiment.

## 3. Industry Contribution / Project Relevance

Dating retention and purchase delays are unlikely to follow one exponential law; weekly cycles, billing periods, and reactivation campaigns can create multimodal hazards. NoDeF is a useful baseline for estimating label maturity and the probability that a currently negative example will later turn positive.

It does not optimize ranking or incrementality. A later subscription may have multiple contributing exposures, and leaving after a successful match makes “conversion” semantics non-monotone. The most credible use is to build horizon-aware sample weights or survival heads for the unified model, validated against simpler parametric hazards.

## 4. Novelty

The paper is an early feature-conditioned nonparametric survival treatment of delayed recommender feedback, avoiding a fixed exponential or Weibull shape.

## 5. Dataset Availability

Criteo Conversion Logs are public. A code release is **Not specified in source**.

## 6. Community Reaction

Not specified in source.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## 8. Meta Information

- **Outcome:** Eventual conversion
- **Delay model:** Kernel-based feature-conditioned density
- **Estimator:** EM with latent eventual-conversion indicator
- **Evaluation:** Synthetic density recovery and Criteo temporal periods
- **Causal/interference treatment:** None
- **Project role:** Flexible label-maturity / survival baseline
