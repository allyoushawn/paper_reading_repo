# Reciprocal Recommender Systems: Analysis of State-of-Art Literature, Challenges and Opportunities towards Social Recommendation

- **Source index:** 119
- **Source ID:** `e3edec23-9654-4bd7-a26c-99f06b789464`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Iván Palomares, Carlos Porcel, Luiz Pizzato, Ido Guy, Enrique Herrera-Viedma
- **Affiliations:** University of Granada, Commonwealth Bank of Australia, eBay Research
- **Year / venue:** 2020 preprint / Information Fusion survey
- **Direction / priority:** D8 reciprocal recommendation / Priority 3 (core survey)
- **URL:** https://arxiv.org/abs/2007.16120

## 1. Summary

This survey characterizes reciprocal recommender systems (RRS): users are both consumers and recommended entities, and success requires bilateral acceptance. It organizes the pipeline into unilateral preference prediction followed by fusion into mutual compatibility, surveys methods across dating, recruitment, learning, social networks, and other domains, and reviews reciprocal evaluation measures.

Common fusion approaches include product, harmonic/weighted means, and hybrid aggregation over content, collaborative, contextual, and social signals. The survey emphasizes that ordinary precision is not enough: success and failure rates should reflect known bilateral outcomes. It identifies popularity bias, sparsity, cold start, scammers, privacy-driven dataset scarcity, underexplored fusion operators, multi-source information, and collective people-to-people recommendation as major gaps. This is a narrative/state-of-the-art survey, not a systematic meta-analysis with pooled effect sizes.

## 2. Experiment Critique

The paper’s strength is taxonomy and conceptual synthesis across domains, including both algorithms and evaluation. It distinguishes reciprocal from merely user-to-user recommendation and surfaces operational issues often omitted in one-sided work.

The indexed source does not describe a preregistered search protocol, inclusion/exclusion flow, quality scoring, or quantitative evidence synthesis. Coverage ends around 2020, before much recent work on causal ranking, congestion-aware optimization, and marketplace experiments. The recommended metrics focus largely on immediate bilateral interactions, not long-term welfare.

## 3. Industry Contribution / Project Relevance

The survey provides vocabulary and a baseline architecture for the dating project. Its most important lesson is that reciprocity is not just multiplying A→B and B→A probabilities; fusion choices, popularity, trust, and negative feedback materially change results. Success rate and failure rate are better funnel checks than one-sided CTR.

The project should go beyond the survey’s standard RRS framing. A unified LTV policy must model attention capacity, congestion, delayed retention/revenue, incrementality, and successful exits. The survey is best used as the historical map and gap baseline against which newer market-level methods are assessed.

## 4. Novelty

The paper offers an early comprehensive formal characterization and literature map of RRS, centered on preference fusion and social recommendation opportunities.

## 5. Dataset Availability

No new dataset is introduced. The survey notes that public reciprocal datasets are scarce because of privacy. Supplementary extraction files or code are **Not specified in source**.

## 6. Community Reaction

Not specified in source.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## 8. Meta Information

- **Paper type:** Narrative/state-of-the-art survey
- **Core domains:** Dating, recruitment, learning, social networks
- **Pipeline:** Preference prediction → bilateral fusion → reciprocal evaluation
- **Named risks:** Popularity bias, sparsity, cold start, scams, privacy
- **Long-term/casual evaluation:** Limited
- **Project role:** Historical taxonomy and terminology
