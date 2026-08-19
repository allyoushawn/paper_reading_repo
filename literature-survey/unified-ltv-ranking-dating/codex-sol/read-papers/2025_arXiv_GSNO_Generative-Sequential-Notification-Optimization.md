# Paper Analysis: Generative Sequential Notification Optimization via Multi-Objective Decision Transformers

**Source:** https://arxiv.org/pdf/2509.02458  
**Date analyzed:** 2026-08-18  
**Source ID:** a52e5813-8f51-4e6e-b04d-c12674797c5d  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** Q1/Q2/Q3 not started after generative-query plateau; source fallback completed

---

## Required Survey Card Fields

- **Title:** Generative Sequential Notification Optimization via Multi-Objective Decision Transformers
- **Authors or company:** LinkedIn
- **Venue:** arXiv
- **Year:** 2025
- **URL:** https://arxiv.org/pdf/2509.02458
- **Source type:** industry paper
- **Direction:** D2
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1.
- **Prediction or incrementality:** Not specified in source. The indexed evidence supports outcome/utility prediction or optimization, not exposure-effect identification.
- **Model architecture:** See §1, “Architecture.”
- **Credit assignment:** See §1, “Credit assignment.”
- **Training data and counterfactual handling:** See §1 and the prediction/incrementality field above.
- **Offline and online evaluation:** See §2.
- **Reported gains:** See §2; no metrics are added beyond indexed-source evidence.
- **Applicability to a two-sided dating recommender:** See § Project Relevance.
- **Unverified claims:** All dating transfer statements below are survey inference, not claims made by the source.

---

## 1. Summary

### Core problem and contribution — indexed-source evidence

- Generative Sequential Notification Optimization via Multi-Objective Decision Transformers Borja Ocejo∗ Ruofan Wang∗ Ke Liu∗† bocejo@linkedin.com LinkedIn Mountain View, USA Rohit Patra Haotian Shen David…
- Optimizing their delivery involves addressing complex sequential decision-making challenges under constraints such as message utility and user fatigue.
- Of-fline reinforcement learning (RL) methods, such as Conservative Q-Learning (CQL), have been applied to this problem but face practical challenges at scale, including instability,…

### Objective — indexed-source evidence

- Decisions on when and what to send influence both immediate user interactions and long-term platform value.
- Generative Sequential Notification Optimization via Multi-Objective Decision Transformers Borja Ocejo∗ Ruofan Wang∗ Ke Liu∗† bocejo@linkedin.com LinkedIn Mountain View, USA Rohit Patra Haotian Shen David…

### Label definition, horizon, delay, sparsity, and censoring — indexed-source evidence

- balance requires models that account for sequential user interactions and long-horizon objectives.
- Unlike [7], we model conditional return-to-go distributions as planning targets, providing increased flexibility and interpretability compared to point estimates.

### Architecture — indexed-source evidence

- HDT approaches [1, 9, 25] often use separate models for goal learning, whereas our method and [7, 11, 20] adopt a unified architecture for…
- Generative Sequential Notification Optimization via Multi-Objective Decision Transformers Borja Ocejo∗ Ruofan Wang∗ Ke Liu∗† bocejo@linkedin.com LinkedIn Mountain View, USA Rohit Patra Haotian Shen David…
- Of-fline reinforcement learning (RL) methods, such as Conservative Q-Learning (CQL), have been applied to this problem but face practical challenges at scale, including instability,…
- This write-back step allows rewards, actions, and features to evolve sequentially with every inference call, minimizing overhead while preserving 84c17711-62e5-4fbe-a665-875ee59c6627 15e438c2-6ba2-415c-b964-6768aeffbe41 c9a762a7-9127-4e14-bdb8-f66e84093e1c 46b37105-9f74-4984-b95f-9861a27478f8 Generative…

### Credit assignment — indexed-source evidence

- We use a carefully engineered set of features to represent the state, including the number and types of notifications sent in the past x…
- Extensive offline and online experiments in a deployed notification system show that our approach improves notification utility and overall session activity while minimizing user…

### Training data and baselines — indexed-source evidence

- We compute the average action prediction accuracy on the evaluation dataset over five different training random seeds as well as the standard deviation.
- 3 Problem Setup We operate a nearline system for notification decision-making that processes hundreds of notification candidates per user for millions of users.
- Optimizing their delivery involves addressing complex sequential decision-making challenges under constraints such as message utility and user fatigue.
- Off-policy actor-critic for recommender systems.

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- Extensive offline and online experiments in a deployed notification system show that our approach improves notification utility and overall session activity while minimizing user…
- At LinkedIn, offline RL approaches such as Conservative Q-Learning (CQL) [18] have been deployed to support notification send/drop decisions, improving notification relevance while respecting…
- 6 Experimental Results In this section, we present the performance of DT against its CQL baseline from both offline and online experiment results.
- Generative Sequential Notification Optimization via Multi-Objective Decision Transformers Borja Ocejo∗ Ruofan Wang∗ Ke Liu∗† bocejo@linkedin.com LinkedIn Mountain View, USA Rohit Patra Haotian Shen David…

### Reported gains — indexed-source evidence

- Compared to a multi-objective CQL-based agent, the DT-based approach achieved a +0.72% increase in sessions for notification decision-making at LinkedIn by making notification recommendation…
- We present a De-cision Transformer (DT) based framework that reframes policy learning as return-conditioned supervised learning, improving robustness, scalability, and modeling flexibility.

### Limitations and negative results — indexed-source evidence

- Optimizing their delivery involves addressing complex sequential decision-making challenges under constraints such as message utility and user fatigue.

**Statistical validity:** Not specified in source beyond the evidence snippets above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - Our contributions include a real-world comparison with CQL, a multi-reward design suitable for non-episodic tasks, a quantile regression approach to return-to-go conditioning, and a…
- 5 Production Setup 5.1 Background Within the LinkedIn notifications ecosystem, the core serving infrastructure is powered by the Air Traffic Controller (ATC) [22], a…
- Of-fline reinforcement learning (RL) methods, such as Conservative Q-Learning (CQL), have been applied to this problem but face practical challenges at scale, including instability,…  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - Optimizing their delivery involves addressing complex sequential decision-making challenges under constraints such as message utility and user fatigue.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** See the source-grounded contribution and architecture evidence in §1.  
**Prior work comparison:** Not specified in source. Raw indexed content does not establish a defensible top-5–7 citation-frequency ranking.  
**Verification:** No independent novelty verification was performed in this fallback batch.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Dataset or production logs described by the source | Not specified in source. | Not specified in source. | Evidence appears in §1 when available. |

**Offline experiment reproducibility:** Not specified in source.

---

## 6. Community Reaction

Not specified in source.

---

## Project Relevance

**Source-grounded facts:** The indexed-source evidence above identifies the paper's objective, architecture, labels, attribution mechanism, and evaluation where available.

**Survey inference:** The paper may inform long-horizon retention optimization or request-level credit assignment. This transfer is unverified. A dating deployment needs 7–30 day retention and weeks-long revenue labels while preserving like, match, and conversation auxiliaries during migration.

**Prediction vs. incrementality:** Not specified in source. The indexed evidence supports outcome/utility prediction or optimization, not exposure-effect identification.

**Reciprocity and congestion:** Not specified in source unless explicitly present above. Candidate-side capacity and bilateral acceptance require an added reciprocal or marketplace layer.

**Cascade and low base rates:** Mapping the method onto impression → like → match → conversation → retention/revenue is survey inference and requires sparse-label calibration.

**Success paradox:** Not specified in source. A dating system must protect match quality and successful outcomes so retention/revenue optimization does not punish successful matching.

**Evaluation implication:** Where source evidence exists, reproduce its offline/online protocol; add bilateral metrics, candidate exposure concentration, and incrementality validation.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** LinkedIn (individual authors not taken from selected-source metadata)  
**Affiliations:** LinkedIn  
**Venue:** arXiv  
**Year:** 2025  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 1
