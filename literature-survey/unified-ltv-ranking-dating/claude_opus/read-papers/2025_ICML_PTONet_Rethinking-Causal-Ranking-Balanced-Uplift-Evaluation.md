# Paper Analysis: Rethinking Causal Ranking: A Balanced Perspective on Uplift Model Evaluation

**Source:** Minqin Zhu, Zexu Sun, Ruoxuan Xiong, Anpeng Wu, Baohong Li, Caizhi Tang, Jun Zhou, Fei Wu, Kun Kuang, "Rethinking Causal Ranking: A Balanced Perspective on Uplift Model Evaluation," ICML 2025. https://proceedings.mlr.press/v267/zhu25s.html
**Date analyzed:** 2026-08-16

## 1. Summary

This paper is primarily an evaluation-methodology contribution, not a new ranking model, though it does introduce an illustrative model to demonstrate the metric. The authors show that the standard uplift/Qini curves used to evaluate CATE-ranking quality have a structural flaw: they only explicitly score individuals with a *positive* binary outcome (Y=1), silently ignoring individuals with Y=0. This lets a biased model that ranks Treated-Positive individuals to the top and Control-Positive individuals to the bottom achieve an inflated AUUC/AUQC even when its actual causal-effect ranking is wrong (e.g., ranking a true "sleeping dog," who is harmed by treatment, above a true "persuadable" who is helped). Their fix, the Principled Uplift Curve (PUC), assigns equal weight to individuals with positive and negative outcomes so that Treated-Positive/Control-Negative individuals (the true "persuadable" signal) are ranked ahead of Treated-Negative/Control-Positive individuals (the "sleeping dog" signal) without the asymmetric bias. They derive a corresponding Principled Uplift Loss (PUL) — a binary cross-entropy loss against a proxy label built from the PUC's own ranking rule — and build PTONet (Principled Treatment and Outcome Network), a three-headed variant of DragonNet that adds PUL as a regularizer. On synthetic data with known ground truth, PUC achieves perfect Kendall-tau alignment (1.0) with the unobservable "true" ranking curve (AUTGC), while conventional curves do not; PTONet outperforms eight baselines (S-/T-Learner, TARNet, CFRNet, DragonNet, EUEN, DESCN, EFIN) on the PUC metric on synthetic, Criteo, and Lazada e-commerce data.

## 2. Experiment Critique

One-paragraph summary (priority 3, per depth rule): The core empirical claim — that conventional curves can be gamed by a biased-but-plausible ranking rule — is demonstrated via constructed case studies and a controlled simulation with known ground-truth CATE, which is the right design for a claim that depends on unobservable counterfactuals. The Kendall-tau correlation with AUTGC (1.0 for PUC vs. <1 for SUC/SQC/JUC/JQC) is a clean, well-designed synthetic-data result. On real-world data (Criteo, Lazada), the paper can only report PUC/AUUQC values (since AUTGC is unobservable there), so the real-world claim reduces to "PTONet wins on PUC" — a form of validating the new metric partly by the new model that was built to optimize it, which is a circularity the authors do not flag as a limitation. The authors' own stated limitations are clear and specific: binary-treatment/binary-outcome only, unconfoundedness assumed, and no ability to distinguish "sure things" and "lost causes" from persuadables/sleeping dogs. No online experiment is reported.

## 3. Industry Contribution

The paper is academic in framing (ICML poster, Ant Group co-affiliation for some authors) with no reported production deployment. PTONet's practical value is narrow and specific: teams already running a DragonNet-style uplift pipeline could add the PUL regularizer with modest engineering cost. The larger practical contribution is arguably the PUC *metric* itself, which is a drop-in replacement for AUUC/Qini as a model-selection criterion — useful for any team currently using those curves to pick among uplift models, independent of which model architecture is used.

## 4. Novelty vs. Prior Work

Claimed novelty: identifying and formally proving that conventional uplift/Qini curves can rank a biased estimator above an unbiased one, and proposing PUC/PUL/PTONet as the fix. The single most relevant prior work, repeatedly cited, is Devriendt et al. 2020 ("Learning to rank for uplift modeling" — the same paper as file #1 in this batch), whose helper-function/L2R formalization the authors explicitly build on and critique ("inspired by [Devriendt et al.]... we design distinct helper functions to demonstrate that helper functions that maximize the uplift and Qini curve can lead to biased estimates"). Other heavily cited works: Shalit et al. 2017 (TARNet/CFRNet/PEHE), Shi et al. 2019 (DragonNet, PTONet's backbone), Künzel et al. 2019 (S-/T-Learner), Diemert et al. 2018/2021 (Criteo benchmark, SUC definition), Radcliffe 2007 / Radcliffe & Surry 2011 (Qini curve origin), and Yadlowsky et al. 2024 (TOC/AUTOC, a related metric the authors position against).

## 5. Dataset Availability

| Dataset | Size | Treatment | Outcome | Public? |
|---|---|---|---|---|
| Synthetic | 10,000 units, 10 covariates | Simulated binomial (p=0.1) | Simulated binary, sine/cosine potential outcomes | Generated (code at github.com/euzmin/PUC) |
| Criteo | 25,309,483 instances, 11 features | Binary advertising treatment | Visit (binary; conversion also available) | Yes |
| Lazada | High-dimensional, production-scale | Voucher distribution | Binary | No (industrial, e-commerce voucher business) |

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

1. **Title, authors, venue, year, URL:** "Rethinking Causal Ranking: A Balanced Perspective on Uplift Model Evaluation," Minqin Zhu, Zexu Sun, Ruoxuan Xiong, Anpeng Wu, Baohong Li, Caizhi Tang, Jun Zhou, Fei Wu, Kun Kuang, ICML 2025 (Poster). https://proceedings.mlr.press/v267/zhu25s.html
2. **Source type:** Academic (ICML poster; co-affiliation includes Ant Group).
3. **Direction:** D6.
4. **Problem setting:** Evaluation methodology for uplift/CATE-ranking models — how to score a model's ability to rank individuals by causal treatment effect, given that individual causal effects are never directly observable; secondarily, how to train a model directly against the corrected metric.
5. **Objective and label definition:** PTONet's training objective is a joint loss L = L_ty (treatment reconstruction + binary outcome prediction + propensity balance + targeted regularizer) + α·L_PUL (binary cross-entropy against a proxy persuadable/sleeping-dog label). Label Y is a **binary** outcome (e.g., purchase, visit). **Not specified in source:** no time horizon and no delay/censoring handling are described anywhere in the retrievable text — outcomes are treated as immediately observed post-treatment binaries.
6. **Prediction or incrementality:** Incrementality. The paper's stated core objective is explicit: "Uplift modeling aims to rank individuals based on CATE, prioritizing persuadables over others... This indicates the core objective of uplift modeling lies in the ranking of CATE values rather than their precise estimation." PUL is a regularizer trained specifically to rank by the CATE-derived persuadable/sleeping-dog contrast, not by predicted outcome level.
7. **Model architecture:** PTONet — a three-headed neural network, a DragonNet variant with propensity, treatment-reconstruction, and outcome-prediction heads, plus the PUL regularizer and Shi et al.'s (2019) targeted regularizer for treatment-assignment-bias correction.
8. **Credit assignment:** Not specified in source. Decisions and outcomes are both at the individual/user level (e.g., whether to deliver an advertisement, whether the product was purchased); no mapping from a delayed or aggregate outcome to an item-level or impression-level decision is present.
9. **Training data and counterfactual handling:** RCT-style binary-treatment data (synthetic RCT design; Criteo is an RCT-style incrementality test; Lazada is production voucher-distribution data). The method explicitly assumes unconfoundedness and does not extend to observational-data confounding adjustment beyond the targeted regularizer inherited from DragonNet.
10. **Offline and online evaluation:** Offline only. Metrics: PEHE (only computable on synthetic data with known ground truth), Area Under True Gain Curve (AUTGC, synthetic-only), Kendall-tau correlation between AUUQC variants and AUTGC, and the AUUQC values of five curve definitions (SUC, SQC, JUC, JQC, PUC) on synthetic, Criteo, and Lazada data. No online/live evaluation is reported.
11. **Reported gains:** On synthetic data, PUC achieves Kendall-tau = 1.0 with AUTGC vs. <1.0 for all conventional curves. PTONet outperforms all eight baselines on PEHE, PUC-AUUQC, and AUTGC on synthetic data; on the real-world Lazada dataset, DESCN wins on SUC/SQC/JUC/JQC but PTONet wins on the authors' own PUC metric. Adding PUL alone to a plain S-Learner ("S-Learner (PU)") already beats all other baselines except PTONet on PUC and AUTGC.
12. **Applicability to a two-sided dating recommender:** Not addressed — no reciprocal-market, congestion, or fairness-across-sides discussion anywhere in the retrievable text. The paper's core insight (conventional uplift-evaluation curves can prefer a biased-but-plausible ranking) is a useful methodological caution for *any* uplift-ranking evaluation the project might design, independent of the two-sided setting.
13. **Unverified claims:** The claim that PTONet's real-world (Criteo/Lazada) superiority on PUC demonstrates genuine improvement is partly self-referential — PUC is the paper's own proposed metric, and PTONet is explicitly built to optimize a proxy of it, so "PTONet wins on PUC" is closer to a consistency check than independent validation; the paper does not have an independent, non-authored evaluation criterion to confirm real-world gains (AUTGC, the only unbiased ground-truth metric, is unavailable outside the synthetic setting).

## Project Relevance

This paper speaks to **Q5** (where incrementality sits inside a ranking objective/evaluation) and, more specifically, to a *methodological gap* the project's own evaluation plan (deliverable 6, "surrogate validation") should be aware of: standard AUUC/Qini-style curves used to validate any uplift-based ranking component can silently favor a biased model. This is a caution for the project's planned offline-evaluation design, not a candidate architecture. It does not address **Q1** (no time horizon; binary immediate outcome), **Q2** (no item-level credit assignment; individual-to-individual only), or **Q7** (no two-sided/reciprocal-market treatment). Because the paper's central contribution is an evaluation curve/loss rather than a production ranking model, and its outcome is an unhorizoned binary conversion, it does not challenge the survey's provisional conclusion.

**Counterexample verdict: NO — ranks by a genuine CATE estimate via the PUL regularizer (Q1 = incrementality), but the outcome is an immediate binary conversion with no stated time horizon (Q2), the treatment is a generic marketing/advertising intervention rather than an item exposure within a ranking (Q3), and the paper's primary contribution is an evaluation metric, not a production ranking model.**

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `PTONet`._

## Meta Information

- **Authors:** Minqin Zhu, Zexu Sun, Ruoxuan Xiong, Anpeng Wu, Baohong Li, Caizhi Tang, Jun Zhou, Fei Wu, Kun Kuang
- **Affiliations:** Includes Ant Group (co-affiliation for several authors); other affiliations not fully specified in retrievable text
- **Venue:** ICML 2025 (Poster), PMLR volume 267
- **Year:** 2025
- **Relevance:** Core
- **Priority:** 3
- **NotebookLM source:** nlm:c4848299-fb1a-4ff6-a732-61282faada22
