# Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?

**Source:** https://arxiv.org/pdf/2608.28649.pdf  
**Date analyzed:** 2026-09-18  
**NLM source id:** `118a06c8-9072-4e89-bab7-f1e22de5a51a`  
**Queue id:** G1  
**Q2 class:** NOT

---

## 1. Summary

Here is the detailed breakdown for the paper **"Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?"** (from source `https://arxiv.org/pdf/2608.28649.pdf`).

---

### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?*
* **Authors:** **Jinqi Wu**\*¹, **Sishuo Chen**\*², **Zhangming Chan**², **Yong Bai**², **Chao Yi**², **Han Zhu**², **Shuodian Yu**², **Lei Zhang**², **Sheng Chen**², **Chenghuan Hou**², **Jian Xu**†², and **Chaoyou Fu**¹ (*Co-first authors, †Corresponding author)
* **Author Affiliations:**
  1. **State Key Laboratory for Novel Software Technology, Nanjing University**, Nanjing, China & **School of Intelligence Science and Technology, Nanjing University**, Suzhou, China (`jinqiwu001@gmail.com`, `bradyfu24@gmail.com`)
  2. **Taobao & Tmall Group of Alibaba**, Beijing, China (`{chensishuo, zhangming.czm, baiyong.by, yunan.yc, zhuhan.zh, yushuodian.ysd, zl165646, chensheng.cs, jinyao, xiyu.xj}@alibaba-inc.com`)
* **Year:** 2026
* **Venue:** *Proceedings of the 35th ACM International Conference on Information and Knowledge Management (CIKM ’26), November 07–11, 2026, Rome, Italy*

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** Standard conversion attribution relies on heuristic, rule-based touchpoint selection (e.g., matching exact product taxonomies or collaborative filtering [CF] signals). These mechanical rules fail to align with human semantic intent and miss a vast space of **implicitly-related touchpoints**—interactions that are semantically relevant to the purchased item but lack explicit metadata or historical engagement overlaps (e.g., buying a camera after browsing memory cards, or buying anime merchandise across different product categories).
* **Key Contribution:**
  1. **SILVA Benchmark:** Constructs **SILVA** (*Selection In fuLl-path conVersion Attribution*), the first human-annotated benchmark for full-path touchpoint selection, revealing that implicitly-related touchpoints constitute **14.91%** of all conversion path touchpoints.
  2. **Systematic Evaluation of LLMs:** Conducts a comprehensive evaluation of flagship proprietary (e.g., GPT-5.5, Gemini 3.1 Pro, Claude Opus 4.7) and open-weight LLMs (e.g., GLM-5.1, DeepSeek V4-Pro, Qwen3.5) across listwise vs. pairwise prompting protocols and thinking modes.
  3. **LOTUS Framework:** Proposes **LOTUS** (*LLM-Oriented Touchpoint Understanding and Selection*), which uses LLM-identified implicit touchpoints as auxiliary labels to train industrial CVR models, achieving significant GAUC gains on an e-commerce platform with hundreds of millions of users.

---

### **(3) Proposed Method or Architecture in Detail**

* **Two-Stage Conversion Attribution Paradigm:**
  * **Stage 1 (Touchpoint Selection - Paper Focus):** Given a conversion event \\(C\\) and preceding touchpoint sequence \\(\{t_1, t_2, \dots, t_n\}\\) within a 3-day lookback window, the system selects relevant touchpoints and classifies them into three classes:
    * *Explicitly-Related:* Same item/shop/brand/category or CF-based similar leaf category.
    * *Implicitly-Related:* Semantic relationships missed by rules, such as **Functional Complementarity** (e.g., camera \\(\leftrightarrow\\) memory card) or **Scenario/Audience Alignment** (e.g., shared anime IP or outdoor activity theme).
    * *Irrelevant:* Weak or unrelated touchpoints.
  * **Stage 2 (Weight Allocation):** Distributes normalized credit \\(\sum w_i = 1\\) among the selected touchpoints.
* **LLM Selection Protocols:**
  * **Pairwise Reasoning:** Evaluates \\((t_i, C)\\) pairs individually alongside the user profile. Decomposes sequence noise into targeted candidate-level judgments.
  * **Listwise Reasoning:** Evaluates the entire behavior log \\(\{t_1, \dots, t_n\}\\) alongside \\(C\\) in a single prompt call.
* **Downstream CVR Enhancement (LOTUS):** LLM-selected implicit touchpoints are fed as positive training instances for an auxiliary indirect-conversion prediction task inside an internal foundation model on Taobao & Tmall.

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Benchmark Dataset (SILVA):**
  * Collected from Taobao & Tmall (Alibaba); contains **1,000 unique conversion events** and **69,680 preceding touchpoints** (3-day lookback window) annotated by human experts (Fleiss’ \\(\kappa > 0.70\\)).
  * Touchpoint Breakdown: **19.09% Explicit**, **14.91% Implicit**, **66.00% Irrelevant**.
* **Production Deployment:**
  * Evaluated on a production CVR prediction model serving hundreds of millions of daily active users at Alibaba.
* **Baselines:**
  * *Selection Baselines:* Rule-based Taxonomy Matching, Collaborative-Filtering (CF) Similarity rules.
  * *Evaluated LLMs:* GPT-5.5, Gemini-3.1-Pro, Claude-Opus-4.7, GLM-5.1, DeepSeek-V4-Pro, DeepSeek-V4-Flash, Qwen3.5-27B, Qwen3.5-30B-A3B.
  * *CVR Prediction Baselines:*
    * **Base (Chen et al., 2025):** Production in-shop attribution baseline.
    * **CABB (Zeng et al., 2026 / Meta):** Heuristic cross-shop selection based on CF rules.

---

### **(5) Key Quantitative Results with Numbers**

* **Touchpoint Selection Benchmark Performance (SILVA, Table 1):**
  * **Explicit F1:** Strong LLMs reach **0.897–0.909 F1** (Pairwise Gemini-3.1-Pro reaches 0.9095; GLM-5.1 reaches 0.9092).
  * **Implicit F1:** Significantly lower across all models, peaking at **0.5426** (GPT-5.5 Pairwise) and **0.5293** (Gemini-3.1-Pro Pairwise).
  * **Pairwise vs. Listwise Gain:** Pairwise prompting raises average Overall F1 from **0.6490 to 0.6954 (+4.64 pp)**. The gap narrows for flagship models (3.0 pp for GPT-5.5) but expands for smaller models (11.9 pp for Qwen3.5-30B-A3B).
* **Industrial CVR Model Gains (Table 3):**
  * **CABB (Explicit Rules) vs. Base:** **+0.20 pp GAUC**.
  * **LOTUS (LLM Explicit + Implicit) vs. Base:** **+0.35 pp GAUC** absolute improvement over the production baseline.
  * **LOTUS vs. CABB:** **+0.15 pp GAUC** incremental gain purely from capturing implicit semantic touchpoints (an absolute gain of 0.10 pp GAUC is considered commercially significant in large-scale e-commerce).

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Persistent Gap in Implicit Reasoning:** The best LLM implicit F1 score (0.5426) lags far behind explicit F1 (~0.91), showing that functional complementarity and scenario alignment remain difficult for current foundation models.
2. **Listwise Over-Filtering / Low Recall:** Listwise prompting suffers from lower recall because LLMs tend to over-filter touchpoints when processing long, noisy behavior logs in a single prompt.
3. **Underperformance of Smaller Models (<100B):** Open-weight models below 100B parameters (e.g., Qwen3.5-27B) lag heavily behind flagship models on implicit touchpoint detection.
4. **Marginal Impact of Chain-of-Thought / Thinking Mode:** Enabling Chain-of-Thought ("think" mode) provided minimal average F1 gains (+0.0082 in pairwise; +0.0196 in listwise), indicating that general CoT reasoning patterns are not yet tailored for nuanced touchpoint attribution judgments.

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Zeng et al. (2026) [CABB / Meta]:** *Click A, Buy B: Rethinking Conversion Attribution in E-Commerce Recommendations* (established cross-item heuristic touchpoint selection).
2. **Chen et al. (2025) [Multi-Attribution Learning]:** *See Beyond a Single View: Multi-Attribution Learning Leads to Better Conversion Rate Prediction* (CIKM '25, established CVR model training with attribution labels).
3. **Yao et al. (2022) [CausalMTA]:** *CausalMTA: Eliminating the User Confounding Bias for Causal Multi-touch Attribution* (KDD '22).
4. **Bencina et al. (2025) [LiDDA]:** *LiDDA: Data Driven Attribution at LinkedIn*.
5. **Lewis et al. (2025) [Amazon Ads MTA]:** *Amazon Ads Multi-Touch Attribution*.
6. **Wei et al. (2022) [Chain-of-Thought]:** *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* (NeurIPS '22).
7. **Liu et al. (2026) [ALM-MTA]:** *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization* (ICLR '26).

---

## 2. Evidence

See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

## 3. Limitations

See limitations in §1 if present. Replace any NLM refusal with: Not specified in source.

---

## 4. Prior works named

See cited prior works in §1.

---

## 5. Project Relevance

**(A) Q1 or Q2 or both or neither?**  
**Q1 only** [1-3]. The paper (*"Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?"*, Wu et al., CIKM 2026) covers industrial production conversion attribution at Taobao & Tmall Group of Alibaba [1, 3, 4]. It does **not** cover Q2, as it focuses strictly on e-commerce purchase conversion attribution rather than user retention, engagement, or active-day attribution [2, 5, 6].

---

**(B) Q2 Class**  
**NOT** [2, 5, 6]. The paper does not publish per-touch retention or active-day credit tables; its target outcome is e-commerce product purchase conversion [2, 5, 6].

---

**(C) Does it produce per-interaction credit? For what outcome?**  
**Yes** [2, 6, 7]. It produces fractional credit weights (\\(\sum w_i = 1\\)) across selected touchpoints for **e-commerce purchase conversion events** (\\(C\\)) [6, 7]. The system operates in two stages: Stage 1 selects meaningful touchpoints (categorized as Explicit, Implicit, or Irrelevant), and Stage 2 distributes normalized credit weights across the selected touchpoints [6, 7]. It does not attribute retention or active days [5, 6].

---

**(D) How would this replace or improve last-touch N7→latest swipes?**  
Instead of using rigid last-touch rules that assign credit solely to the latest interaction, this framework uses an LLM-driven semantic selector (**LOTUS**) with pairwise prompting to inspect full behavior sequences and recover **implicitly-related touchpoints** (such as functional complementarity or scenario alignment) [3, 5-8].  
* **Mapping to Dating Context:** Applied to dating retention, an LLM-based selector would evaluate the full interaction sequence (earlier swipes, mutual matches, and 4-way messaging conversations) rather than defaulting to the most recent swipe [6, 7]. It would identify semantically meaningful interactions—such as deep messaging exchanges or matches based on shared interests—and allocate fractional credit across all contributing touchpoints rather than crediting only the latest swipe [6-8].

---

**(E) Selection-bias handling?**  
**Not specified in source** [3, 5, 9]. The paper focuses on evaluating LLM semantic reasoning and prompting protocols (pairwise vs. listwise) for touchpoint selection rather than applying propensity weighting, inverse-propensity scoring, or causal debiasing for user swiping/activity selection bias [5, 9, 10].

---

**(F) Deployed or production dataset?**  
**Yes, both a benchmark dataset and a production deployment are reported** [3, 11, 12]:
* **SILVA Benchmark Dataset:** Constructed from Taobao & Tmall (Alibaba); contains **1,000 unique conversion events** and **69,680 preceding touchpoints** collected within a **3-day lookback window** [12]. Human annotations achieved Fleiss’ \\(\kappa > 0.70\\) [13].
* **Annotated Touchpoint Distribution:** **19.09% Explicitly-related**, **14.91% Implicitly-related**, and **66.00% Irrelevant** touchpoints [12, 14].
* **LLM Selection Benchmark Performance:** Pairwise prompting achieved an average explicit F1 of **0.8979** and implicit F1 of **0.4929** (highest implicit F1: **0.5426** by GPT-5.5; highest explicit F1: **0.9095** by Gemini-3.1-Pro) [15, 16]. Pairwise prompting outperformed listwise prompting, raising overall F1 from **0.6490 to 0.6954 (+4.64 pp gain)** [10].
* **Production Deployment & CVR Model Gains:** Tested on a production CVR prediction model serving **hundreds of millions of daily active users** at Alibaba [3, 11, 12]. LOTUS achieved an absolute **+0.35 pp GAUC gain** over the production in-shop baseline (`Base`) and **+0.15 pp GAUC gain** over the heuristic rule-based competitor (`CABB`) [3, 11]. The authors note that an absolute GAUC improvement of **0.1 pp** is empirically sufficient to drive substantial growth in online sales and ad revenue [3, 17].

---

💡 *Would you like to explore how an LLM-driven pairwise selection protocol could be adapted to identify implicit high-value interactions (e.g., messaging engagement or match quality) for your dating platform's N7 retention ranker?*

---

## 6. Community Reaction

No significant community discussion searched at card-write time; extraction is NLM-scoped.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**PDF:** ingested via NotebookLM  
**Relevance:** Core if Q2 class is TRUE or PARTIAL or Q1 industry system; else Related  
**Priority:** see queue.md `G1`
