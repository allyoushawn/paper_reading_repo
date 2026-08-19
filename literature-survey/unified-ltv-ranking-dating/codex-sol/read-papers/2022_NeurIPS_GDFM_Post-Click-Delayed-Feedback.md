# Generalized Delayed Feedback Model with Post-Click Information in Recommender Systems

- **Source index:** 109
- **Source ID:** `3e6b9c81-c1f1-4601-8363-9e215d7395b0`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Jia-Qi Yang, De-Chuan Zhan
- **Affiliation:** Nanjing University
- **Year / venue:** 2022 / NeurIPS
- **Direction / priority:** D7 delayed feedback / Priority 3
- **URL:** https://proceedings.neurips.cc/paper_files/paper/2022/hash/9d8e45dc01e35a5d79ea672c4de1a415-Abstract-Conference.html

## 1. Summary

GDFM generalizes delayed-conversion modeling to stochastic post-click signals such as cart and favorite actions observed at different times. It frames each signal’s usefulness as a balance between a sampling gap—conditional entropy/sample complexity when inferring conversion from the proxy—and a temporal gap caused by using older distributions. The streaming loss reweights actions by informativeness and recency and adds a regularizer to control variance.

Hourly streaming replay uses public Criteo (about 16 million samples) and Taobao (over 70 million interactions, one million users). Relative to a stale pretrained model and a mature-label oracle, GDFM recovers 74.9% AUC, 68.1% PR-AUC, and 72.4% NLL of the Criteo gap; on Taobao it recovers 79.4%, 80.7%, and 49.6%. Five-seed standard deviations are reported. An ablation supports the entropy and stabilization terms; the combined weight peaks around day seven in the Criteo analysis.

## 2. Experiment Critique

The paper offers a principled account of why an early proxy can be both fresher and noisier, evaluates with timestamp-correct replay, uses two large public datasets, and reports variability. It also shows that fake-negative methods can severely hurt Taobao NLL.

The stability of the action–conversion relationship is an assumption that may fail when product or ranking policies change. The added synthetic action used in one capacity test is not real behavior. Training cost grows linearly with the number of reveal times, as the authors note. The evaluation remains predictive and offline; it does not identify whether inducing a proxy action improves the final outcome.

## 3. Industry Contribution / Project Relevance

The method maps naturally to dating cascades: view → like → match → reply → sustained conversation → later retention/revenue. It supplies a defensible way to weight early behaviors by both predictive information and age instead of treating all proxies equally. The observed seven-day optimum also illustrates that the newest label is not automatically the best label.

For the unified LTV ranker, proxy stability should be monitored by cohort and policy version. GDFM can make long-horizon training timely, but it does not solve incrementality, reciprocal choice, congestion, or the possibility that successful users leave. Those require causal outcomes and two-sided constraints outside this model.

## 4. Novelty

The paper unifies early conversions and arbitrary post-click behaviors under one delayed-feedback model and explicitly separates temporal and sampling gaps when weighting proxies.

## 5. Dataset Availability

Criteo Conversion Logs and Taobao User Behavior are public. Code is available at https://github.com/ThyrixYang/gdfm_nips22.

## 6. Community Reaction

Not specified in source beyond NeurIPS 2022 publication.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## 8. Meta Information

- **Outcome:** Delayed binary conversion
- **Auxiliary signals:** Early conversion and post-click behaviors
- **Evaluation:** Hourly streaming replay, five seeds
- **Causal identification:** None
- **Main scaling limit:** Cost grows with reveal-time count
- **Project role:** Cascade/proxy weighting for mature LTV labels
