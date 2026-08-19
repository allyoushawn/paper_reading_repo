# Phase 4 NotebookLM Query 1 — Dominant Methodological Approaches

**Query:** Across all notebook sources, identify the dominant methodological approaches. For each, give a brief source-grounded description and representative full paper/source titles. Do not infer; write Not specified when absent.

## Response

The following are the dominant methodological approaches utilized across the sources in this notebook to model, optimize, and evaluate reciprocal recommendations and two-sided matching markets:

### 1. Content-Based (CB) Recommendation & Semantic Matching

This approach matches users or entities by computing similarity scores across explicit profile fields, textual metadata, or questionnaires (e.g., resumes, job descriptions, or personal questionnaires). CB models typically evaluate profile-to-profile similarities, multi-criteria match weights, or semantic embeddings to estimate unilateral compatibility without requiring dense historical interaction logs from other users.

Representative sources: *A Challenge-Based Survey of E-Recruitment Recommendation Systems*; *Reciprocal Recommender Systems: Analysis of State-of-Art Literature, Challenges and Opportunities towards Social Recommendation*; *RECON: A Reciprocal Recommender for Online Dating*; *CCR — A Content-Collaborative Reciprocal Recommender for Online Dating*.

### 2. Collaborative Filtering (CF) & Latent Factor Models

Collaborative filtering models learn implicit user preferences by projecting historical transaction records such as clicks, applies, or likes into low-dimensional latent embedding spaces. In reciprocal systems, unilateral preference embeddings are learned independently for both sides of the market and then aggregated, for example with harmonic, arithmetic, or geometric means, to calculate mutual-interest scores.

Representative sources: *Matrix Factorization Techniques for Recommender Systems*; *BPR: Bayesian Personalized Ranking from Implicit Feedback*; *Collaborative Filtering for Implicit Feedback Datasets*.

### 3. Graph Neural Networks (GNNs) & Bipartite/Heterogeneous Graph Learning

This methodology models two-sided marketplaces as structural graphs such as bipartite interaction graphs, hypergraphs, or text-attributed graphs. Graph convolutional networks recursively propagate and aggregate topological neighborhood representations and textual embeddings across graph nodes to learn bidirectional, dual-perspective representations.

Representative sources: *Modeling Two-Way Selection Preference for Person-Job Fit*; *LinkSAGE: Optimizing Job Matching Using Graph Neural Networks*; *LightGCN: Simplifying and Powering Graph Convolution Network for Recommendation*; *Bilateral Sequential Hypergraph Convolution Network for Reciprocal Recommendation*.

### 4. Matching-Theoretic & Economic Optimization Models

Grounded in market design, this methodology frames recommendation as a centralized, two-sided market-clearing problem under physical capacity limits such as finite dater reply capacity or company headcount. Rather than ranking by unilateral preference scores alone, these systems solve linear programs, stable-matching algorithms such as Gale–Shapley or Choo–Siow transferable utility, or Nash-social-welfare formulations to maximize global objectives and flatten popularity skews.

Representative sources: *College Admissions and the Stability of Marriage*; *Who Marries Whom and Why*; *Fast and Examination-Agnostic Reciprocal Recommendation in Matching Markets*; *Balancing Fairness and High Match Rates in Reciprocal Recommender Systems: A Nash Social Welfare Approach*; *MODE: Mutual Optimality in Direct Effects of Reciprocal Recommendations in Matching Markets*.

### 5. Counterfactual Causal Inference & Off-Policy Evaluation (OPE)

Because historical interaction logs are biased by past exposures and marketplace spillovers, this approach uses causal estimators to debias offline learning and policy evaluation. It applies inverse-propensity scoring, doubly robust estimation, and dual-constraint shadow prices to estimate rewards such as successful matches for new recommendation policies from logged data.

Representative sources: *Off-Policy Evaluation and Learning for Matching Markets*; *Counterfactual Reciprocal Recommender Systems for User-to-User Matching*; *Reducing Marketplace Interference Bias Via Shadow Prices*; *Recommendations as Treatments: Debiasing Learning and Evaluation*.

### 6. Sequential, Session-Based, & Time-Aware Sequence Modeling

This approach captures chronological progression in user histories. Rather than treating profiles as static, it employs sequential networks such as RNNs, LSTMs, GRUs, or self-attentive Transformers on both active and passive interaction timelines to predict next-step bilateral matches.

Representative sources: *Reciprocal Sequential Recommendation*; *Beyond Matching: Modeling Two-Sided Multi-Behavioral Sequences for Dynamic Person-Job Fit*; *STAMP: Short-Term Attention/Memory Priority Model for Session-Based Recommendation*; *BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer*.

### 7. Reinforcement Learning (RL) & Bandit Frameworks

This methodology formulates matching, dispatching, and pricing decisions as sequential Markov decision processes or multi-agent contextual bandits. It uses online value models to adapt to dynamic marketplace variables such as driver–rider alignment, geographical supply repositioning, and long-term participation incentives.

Representative sources: *A Better Match for Drivers and Riders: Reinforcement Learning at Lyft*; *Reinforcement Learning for Modeling Marketplace Balance*; *Deep Reinforcement Learning for Multi-Driver Vehicle Dispatching and Repositioning Problem*.

### 8. Multi-Task & Multi-Label Deep Learning

This approach integrates multiple downstream interaction targets such as clicks, applies, recruiter reviews, and hiring approvals into unified multi-objective architectures such as MMOE or PLE. Shared representations predict multi-stage conversion outcomes while addressing selection across funnel stages.

Representative sources: *BOSS: A Bilateral Occupational-Suitability-Aware Recommender System for Online Recruitment*; *Optimizing Airbnb Search Journey with Multi-Task Learning*; *Progressive Layered Extraction: A Novel Multi-Task Learning Model for Personalized Recommendations*.

NotebookLM ended by offering to generate a simulation; no such simulation was requested or used.
