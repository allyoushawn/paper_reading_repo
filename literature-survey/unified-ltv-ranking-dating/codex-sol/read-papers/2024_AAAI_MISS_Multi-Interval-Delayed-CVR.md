# Online Conversion Rate Prediction via Multi-Interval Screening and Synthesizing under Delayed Feedback

- **Source index:** 108
- **Source ID:** `8b7867b6-068b-4ebe-8f51-91961aead54f`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Qiming Liu, Xiang Ao, Yuyao Guo, Qing He
- **Affiliations:** Chinese Academy of Sciences and University of Chinese Academy of Sciences
- **Year / venue:** 2024 / AAAI
- **Direction / priority:** D7 delayed feedback / Priority 3
- **URL:** https://ojs.aaai.org/index.php/AAAI/article/view/28756

## 1. Summary

MISS treats different label-waiting windows as complementary views of conversion. A multi-head screening model predicts CVR at several intervals, with global positive weighting intended to reduce bias while retaining head diversity. A small synthesizer learns dynamic weights over those heads from an assembled stream of recent positives and mature real negatives, balancing fresh data with accurate labels.

Hourly replay experiments use Criteo (15,898,863 samples, 30-day attribution) and Tencent 2017 advertising data (22,601,402 samples, 5-day attribution). Performance is normalized between a stale pretrained model (0%) and an oracle trained with mature labels (100%). MISS reaches 83.7/83.9/78.1% of that range on Criteo AUC/NLL/PR-AUC and 86.0/82.8/88.2% on Tencent, statistically better than the best listed baseline at p≤0.05.

## 2. Experiment Critique

The online replay respects information availability at each timestamp, uses two large public datasets with very different base rates, and compares against single-window, duplication, debiasing, and multi-task methods. Reporting oracle-relative performance makes the remaining gap visible.

The “oracle” is not a deployable comparator and the replay is not a live randomized test. Attribution windows define the labels and may censor longer-term value. Results concern predictive CVR, not causal lift. The indexed source states code will be released but does not provide a verified repository link. Sensitivity to window choices, policy shifts, and compute/latency constraints remains important for production.

## 3. Industry Contribution / Project Relevance

Dating outcomes arrive on several clocks: match and reply quickly, conversation quality later, then 7–30-day retention and revenue. MISS offers an architecture for combining maturity-specific heads without collapsing every immature observation into a negative. A synthesizer could learn when early signals reliably forecast mature LTV.

For the project, each head should correspond to a clearly versioned horizon and be evaluated temporally. However, MISS is still a conversion predictor. It does not estimate the incremental effect of showing candidate B, account for reciprocity or congestion, or resolve the success paradox. Its outputs need a causal/policy layer and marketplace constraints.

## 4. Novelty

The contribution is a general multi-window screening-and-synthesis framework that learns relationships among delay-specific predictions rather than choosing one window or directly averaging heads.

## 5. Dataset Availability

Criteo conversion logs and Tencent Advertising Algorithm Competition 2017 data are reported as public. A verified paper-code URL is **Not specified in source**.

## 6. Community Reaction

Not specified in source beyond AAAI 2024 publication.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## 8. Meta Information

- **Outcome:** Delayed advertising conversion
- **Method:** Multi-head waiting-window model plus learned synthesizer
- **Metrics:** AUC, NLL, PR-AUC
- **Evaluation:** Hourly offline streaming replay
- **Causal/interference treatment:** None
- **Project role:** Multi-horizon label-maturity modeling
