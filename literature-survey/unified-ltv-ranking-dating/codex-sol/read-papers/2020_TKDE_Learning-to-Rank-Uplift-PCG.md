# Learning to Rank for Uplift Modeling

- **Source index:** 106
- **Source ID:** `9344afc4-f9ef-47db-aa0e-d914576953a3`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Floris Devriendt, Tias Guns, Wouter Verbeke
- **Affiliation:** Vrije Universiteit Brussel
- **Year / venue:** 2020 preprint; later IEEE TKDE
- **Direction / priority:** D6 causal ranking / Priority 3
- **URL:** https://arxiv.org/abs/2002.05897

## 1. Summary

The paper reframes uplift modeling as learning to rank: the operational product is an ordering by incremental treatment response, not necessarily calibrated individual effects. It unifies several uplift/Qini value functions and derives Promoted Cumulative Gain (PCG), a ranking measure exactly corresponding to area under an uplift curve. Unlike DCG’s discounting, PCG promotes useful treated/control response categories early in the list. PCG is optimized with LambdaMART.

Experiments use three public campaign datasets: Information insurance (10,000 records), Hillstrom email marketing (64,000 total; 42,693 in the selected comparison), and Criteo advertising (25.3 million total, heavily subsampled to about 25,310 because of computation). Ten repeated runs compare standard learning-to-rank metrics and uplift baselines. PCG generally improves AUUC over standard ranking metrics and is equal to or better than the uplift baseline. Attempts to optimize only 10%, 30%, or 50% targeting depth create training peaks but do not generalize; smaller k usually lowers test performance.

## 2. Experiment Critique

Strengths include explicit metric formalization, reproducible public datasets, matched tree-based learners, and repeated experiments. The failed top-k result is reported rather than hidden.

The Criteo experiment uses only roughly 0.001% of the available data, weakening conclusions about industrial-scale behavior. Evaluation relies on uplift-curve estimators whose limitations are now better understood, outcomes are binary, and the treatment is binary. Hyperparameters are held fixed rather than tuned per method. No online policy test, delayed outcome, interference correction, or confidence interval is reported in the indexed source.

## 3. Industry Contribution / Project Relevance

PCG is a useful bridge from causal treatment effects to a production ranking loss. A dating system could rank candidate exposures by incremental 7–30-day retention or revenue rather than by predicted likes. The paper also warns that forcing a deployment cutoff into the training loss may overfit; selecting top-k via policy constraints after robust full-ranking training may be safer.

The mapping is incomplete for dating. A “treatment” is a candidate exposure within a slate, and effects depend on the candidate’s reciprocal response, congestion, and later cascade. AUUC over individuals does not optimize marketplace welfare or subscription dynamics. PCG is therefore a component or baseline, not a sufficient unified LTV objective.

## 4. Novelty

The paper provides a unified algebra for uplift metrics and an exact learning-to-rank translation of AUUC that can be plugged into LambdaMART.

## 5. Dataset Availability

All three datasets are reported as public: the Information R package, Hillstrom/MineThatData, and Criteo uplift data. RankLib and XGBoost are used; a paper-specific code release is **Not specified in source**.

## 6. Community Reaction

Not specified in source.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## 8. Meta Information

- **Outcome:** Binary purchase/visit response
- **Treatment:** Binary campaign exposure
- **Model:** LambdaMART with PCG
- **Evaluation:** AUUC under joint/separate uplift definitions
- **Interference:** Not modeled
- **Project role:** Causal-ranking objective baseline
