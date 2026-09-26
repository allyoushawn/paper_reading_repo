# PROMISE: Process Reward Models Unlock Test-Time Scaling Laws in Generative Recommendations [1, 2]

**Source:** https://arxiv.org/pdf/2601.04674.pdf  
**Date analyzed:** 2026-09-24  
**NLM source id:** `df98b8e9-3fd2-465d-8f1b-23d0c51a8048`  
**Queue id:** G28  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *PROMISE: Process Reward Models Unlock Test-Time Scaling Laws in Generative Recommendations* [1, 2]
* **Authors:** **Chengcheng Guo**\*, **Kuo Cai**\*, **Yu Zhou**, **Qiang Luo**†, **Ruiming Tang**†, **Han Li**, **Kun Gai**, and **Guorui Zhou** (\*Equal contribution, †Corresponding author) [3, 4]
* **Affiliations:** **Kuaishou Inc.**, Beijing, China (*Kun Gai is Unaffiliated, Beijing, China*) [3]
* **Year & Venue:** Published in **2026** (Received/Accepted January 8, 2026; ACM Conference Proceedings format) [3–4, 91].

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Generative recommendation systems reformulate recommendation as sequence-to-sequence generation over hierarchical Semantic IDs (SIDs) [1, 5]. However, existing methods suffer from **Semantic Drift** caused by exposure bias (the discrepancy between teacher forcing during training and autoregressive generation during inference) [1, 6, 7]. When a model makes a prediction error in an early, high-level semantic token (e.g., mistaking the item category), the error propagates and irreversibly diverts the generation trajectory into an irrelevant semantic subspace [1, 8, 9].
* **Key Contributions:**
  1. **Formalization of Semantic Drift:** Draws an explicit parallel between hierarchical Semantic ID generation and Chain-of-Thought (CoT) reasoning in Large Language Models (LLMs), identifying the need for step-by-step intermediate verification [2, 10–13].
  2. **PROMISE Framework:** Introduces a lightweight Path-Level Process Reward Model (PRM) trained end-to-end via InfoNCE loss on positive and negative sampled SID reasoning paths to detect and penalize intermediate generation deviations in real time [2, 12, 26–28].
  3. **PRM-Guided Beam Search:** Implements a test-time search strategy where candidate generation paths are expanded (\\(K^+ \gg K\\)) and scored by the PRM to prune erroneous branches early, keeping decoder-side compute fixed while improving accuracy [2, 12, 33–37].
  4. **Test-Time Scaling Laws for Recommendations:** Demonstrates that increasing test-time compute via PRM-guided search enables smaller generative models to match or surpass much larger models at lower inference FLOPs [2, 13, 63–64].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Architectural Components**
* **Generative Backbone:** Transformer-based Encoder-Decoder model [10]. The encoder transforms user historical behavior \\([x_1, \dots, x_{t-1}]\\) into hidden state \\(E^{(L)}\\) [11]. The decoder autoregressively predicts the target item's \\(d\\)-layer Semantic ID path \\([s_{t,1}, \dots, s_{t,d}]\\) using Next-Token Prediction (NTP) loss \\(\mathcal{L}_{NTP}\\) [15–16].
* **Path-Level PRM:** A lightweight cross-attention module that evaluates intermediate SID prefixes \\(S = [s_{\cdot, 1}, \dots, s_{\cdot, b}]\\) at depth \\(b \in \{1, \dots, d\}\\) [26–27, 30–31].
  * *Input Representation:* Each path \\(S\\) is mapped to a unique single token embedding vector \\(P_S = \text{EmbLookup}([s_{\cdot,1}, \dots, s_{\cdot,b}])\\) to minimize attention overhead [12].
  * *Feature Reuse:* Reuses the encoder output \\(E^{(L)}\\) as key and value in \\(F\\) stacked cross-attention layers, outputting a scalar logit \\(y_S = \text{MLP}(P^{(F)}_S)\\) [31–32].
* **Negative Sampling Strategy:** For a ground-truth path prefix \\(S^{\text{pos}}_{x_t, b}\\) at depth \\(b\\), samples \\(N\\) distinct valid negative paths \\(S^{\text{neg}} \sim \text{Uniform}(\mathcal{V}_b \setminus \{S^{\text{pos}}_{x_t, b}\})\\) from the catalog valid path set \\(\mathcal{V}_b\\) [21, 25–26].
* **InfoNCE Optimization:** Maximizes the logit of positive paths relative to sampled negative paths at each layer \\(b\\):
  \\[\mathcal{L}^{\text{InfoNCE}}_{x_t, b} = -\log \frac{\exp\{y_{S^{\text{pos}}_{x_t, b}}\}}{\exp\{y_{S^{\text{pos}}_{x_t, b}}\} + \sum_{S^{\text{neg}}} \exp\{y_{S^{\text{neg}}}\}} \quad [13]\\]
  Jointly trained end-to-end: \\(\mathcal{L}_{\text{Total}} = \mathcal{L}_{NTP} + \mathcal{L}_{\text{InfoNCE}}\\) [28–29].
* **PRM-Guided Beam Search:** At step \\(b\\), expands candidate beam paths to \\(K^+\\) candidates, evaluates them with the Path-level PRM, and selects the top \\(K' \ll K^+\\) paths (where \\(K' = K\\)) to pass to the next decoder step [2, 34–37].

#### **Credit Assignment Mechanics**
* **No Multi-Touch Sequence Attribution:** Does **not** perform multi-touch sequence attribution or fractional credit assignment across historical user interaction logs [10, 14].
* **Token/Step-Level Process Verification:** Credit is assigned at the **intermediate Semantic ID token/path level** (\\(b=1 \dots d\\)) during generative decoding by evaluating candidate SID prefix paths against user context via InfoNCE loss (\\(\mathcal{L}_{\text{InfoNCE}}\\)) [26–28].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets & Scale:**
  1. **Amazon Review Dataset:** *Beauty* and *Sports and Outdoors* categories (quantized via RQ-VAE into \\(d=3\\) codebook layers, \\(M=256\\)) [15, 16].
  2. **Kuaishou Industrial Dataset:** Real-world user logs from Kuaishou app covering **>400 million DAUs**, **~50 billion daily interactions**, and **>100 million daily items** (quantized via Residual K-means into \\(d=3\\) layers, \\(M=8192\\)) [17].
* **Production Deployment:** Fully deployed in live online A/B testing on **Kuaishou** and **Kuaishou Lite** apps (allocating 5% traffic / **~20 million users** per group for 7 days) [52–53].
* **Comparison Baselines:**
  * *Public Baselines:* Traditional sequential models (GRU4REC, Caser, HGN, \\(S^3\\)-Rec, Bert4Rec, SASRec) and Generative models (TIGER, HSTU, ActionPiece) [39–40, 42–43].
  * *Industrial Baselines:* GRank, MPFormer, MISS, GPRP, Kuaiformer, CRM [18, 19].

---

### **(5) Key Quantitative Results with Numbers**
* **Public Amazon Benchmark (Table 1):**
  * *Sports and Outdoors:* **Recall@5 = 0.0450** (+42.41% over ActionPiece), **NDCG@5 = 0.0296** (+44.39%), **Recall@10 = 0.0689** (+37.80%), **NDCG@10 = 0.0373** (+42.19%) [20, 21].
  * *Beauty:* **Recall@5 = 0.0536** (+4.90%), **NDCG@5 = 0.0345** (+1.47%), **Recall@10 = 0.0821** (+5.60%), **NDCG@10 = 0.0437** (+3.07%) [20, 21].
* **Industrial Dataset Benchmark (\\(K=1000\\), Table 2):**
  * *\\(K^+ = 4000\\):* **Recall@100 = 0.1494** (+47.92% vs. GRank), **NDCG@100 = 0.00652** (+38.14%), **Recall@500 = 0.2836** (+18.36%), **NDCG@500 = 0.01231** (+13.04%), **Recall@1000 = 0.3358** (+5.66%) [18].
  * *\\(K^+ = 6000\\):* **Recall@100 = 0.1609** (+59.31%), **NDCG@100 = 0.00663** (+40.47%), **Recall@500 = 0.3017** (+25.92%), **NDCG@500 = 0.01272** (+16.80%), **Recall@1000 = 0.3637** (+14.44%) [21].
* **Live Production Online A/B Test Results (7-day test vs. Control, 95% CI, Table 3):**
  * *Kuaishou App:* Total App Usage Time **+0.121%** [CI: +0.04%, +0.20%], App Usage Time Per User **+0.120%** [CI: +0.06%, +0.18%], Total Video Watch Time **+0.431%**, Watch Time per Video View **+0.440%** [22].
  * *Kuaishou Lite App:* Total App Usage Time **+0.131%** [CI: +0.03%, +0.23%], App Usage Time Per User **+0.160%** [CI: +0.07%, +0.25%], Total Video Watch Time **+0.398%**, Watch Time per Video View **+0.296%** [53–54].
* **System Deployment Efficiency:** Total parameter size increases by **only 15%**, and inference latency increases by **only 10%** (utilizing 1 PRM block, 1/4 attention heads, and GPU Radix Top-K optimization) [23].

---

### **(6) Limitations, Failure Modes, or Negative Results**
1. **Failure of Brute-Force Beam Scaling:** Simply increasing global beam size \\(K\\) in traditional beam search yields marginal metric improvements (HRecall@3@1000 stays around ~25.14%–25.97%) while drastically increasing decoder self/cross-attention compute [24, 25].
2. **Inefficiency of Parameter Scaling vs. Test-Time Scaling:** Increasing model parameters up to 5\\(\times\\) achieves lower accuracy at equal FLOPs (26.67% HRecall@3@1000) compared to test-time candidate expansion (\\(K^+=6000\\), achieving 34.37%) [62–64].
3. **Performance Degradation with Partial PRM Step Activation:** Applying PRM at only 1 or 2 decoding steps is inferior to active step-wise verification across all 3 steps (HRecall@3@1000 drops from 0.3358 for all 3 steps to 0.2322–0.2650 for a single step) [54–55, 57].
4. **Exposure Bias / Semantic Drift Vulnerability:** Without dense intermediate PRM verification, standard NTP models revert to training marginal distributions when early prediction errors occur, exacerbating popularity bias toward generic items [17–18].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Rajput et al. (2023) [Ref 26 / TIGER]:** *Recommender systems with generative retrieval* (NeurIPS '23) [14, 26].
2. **Lightman et al. (2023) [Ref 17 / OpenAI PRM]:** *Let’s verify step by step* (ICLR '23) [7, 27].
3. **Zhai et al. (2024) [Ref 40 / HSTU]:** *Actions speak louder than words: trillion-parameter sequential transducers for generative recommendations* (ICML '24) [28, 29].
4. **Snell et al. (2024) [Ref 30 / Test-Time Compute Scaling]:** *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters* [12, 30].
5. **Wang et al. (2024) [Ref 36 / Math-Shepherd]:** *Math-shepherd: Verify and reinforce llms step-by-step without human annotations* (ACL '24) [31, 32].
6. **Lee et al. (2022) [Ref 14] & Luo et al. (2025) [Ref 22]:** *Autoregressive image generation using residual quantization* (RQ-VAE) & *Quantitative alignment multi-modal recommendation at Kuaishou* (Residual K-means) [33-36].
7. **Zhou et al. (2025) [Refs 46, 47, 48 / OneRec Series]:** *OneRec Technical Report* & *OneRec-v2 Technical Report* [46–48, 89–90].

---

💡 *Would you like to explore how PROMISE's Path-Level Process Reward Model or PRM-guided beam search could be adapted to prevent semantic drift in candidate profile token generation for your dating app?*

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

### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *PROMISE: Process Reward Models Unlock Test-Time Scaling Laws in Generative Recommendations* [1]
* **Authors:** **Chengcheng Guo**\*, **Kuo Cai**\*, **Yu Zhou**, **Qiang Luo**†, **Ruiming Tang**†, **Han Li**, **Kun Gai**, and **Guorui Zhou** (\*Equal contribution, †Corresponding author) [1–2]
* **Affiliations:** **Kuaishou Inc.**, Beijing, China (*Kun Gai is Unaffiliated, Beijing, China*) [1–2]
* **Year & Venue:** Published in **2026** (Received/Accepted January 8, 2026; ACM Conference Proceedings format) [2, 3].

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Generative recommendation reformulates item retrieval as sequence-to-sequence generation over hierarchical Semantic IDs (SIDs) [2, 5–6]. However, existing methods suffer from **Semantic Drift** caused by exposure bias (the discrepancy between teacher forcing during training and autoregressive generation during inference) [4, 5]. When a model makes a prediction error in an early, high-level semantic token (e.g., mistaking the item category), the error propagates and irreversibly diverts the generation trajectory into an irrelevant semantic subspace [4, 6, 7].
* **Key Contributions:**
  1. **Formalization of Semantic Drift:** Draws an explicit parallel between hierarchical Semantic ID generation and Chain-of-Thought (CoT) reasoning in Large Language Models (LLMs), identifying the need for step-by-step intermediate verification [2, 10–13].
  2. **PROMISE Framework:** Introduces a lightweight Path-Level Process Reward Model (PRM) trained end-to-end via InfoNCE loss on positive and negative sampled SID reasoning paths to detect and penalize intermediate generation deviations in real time [2, 12, 26–28].
  3. **PRM-Guided Beam Search:** Implements a test-time search strategy where candidate generation paths are expanded (\\(K^+ \gg K\\)) and scored by the PRM to prune erroneous branches early, keeping decoder-side compute fixed while improving accuracy [2, 12, 33–37].
  4. **Test-Time Scaling Laws for Recommendations:** Demonstrates that increasing test-time compute via PRM-guided search enables smaller generative models to match or surpass much larger models at lower inference FLOPs [2, 13, 63–64].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Architectural Components**
* **Generative Backbone:** Transformer-based Encoder-Decoder model [8]. The encoder transforms user historical behavior \\([x_1, \dots, x_{t-1}]\\) into hidden state \\(E^{(L)}\\) [9]. The decoder autoregressively predicts the target item's \\(d\\)-layer Semantic ID path \\([s_{t,1}, \dots, s_{t,d}]\\) using Next-Token Prediction (NTP) loss \\(\mathcal{L}_{\text{NTP}}\\) [10].
* **Path-Level PRM:** A lightweight cross-attention module that evaluates intermediate SID prefixes \\(S = [s_{\cdot, 1}, \dots, s_{\cdot, b}]\\) at depth \\(b \in \{1, \dots, d\}\\) [26–27, 30–31].
  * *Input Representation:* Each path \\(S\\) is mapped to a unique single token embedding vector \\(P_S = \text{EmbLookup}([s_{\cdot,1}, \dots, s_{\cdot,b}])\\) to minimize attention overhead [11].
  * *Feature Reuse:* Reuses the encoder output \\(E^{(L)}\\) as key and value in \\(F\\) stacked cross-attention layers, outputting a scalar logit \\(y_S = \text{MLP}(P^{(F)}_S)\\) [31–32].
* **Negative Sampling Strategy:** For a ground-truth path prefix \\(S^{\text{pos}}_{x_t, b}\\) at depth \\(b\\), samples \\(N\\) distinct valid negative paths \\(S^{\text{neg}} \sim \text{Uniform}(\mathcal{V}_b \setminus \{S^{\text{pos}}_{x_t, b}\})\\) from the catalog valid path set \\(\mathcal{V}_b\\) [21, 25–26].
* **InfoNCE Optimization:** Maximizes the logit of positive paths relative to sampled negative paths at each layer \\(b\\):
  \\[\mathcal{L}^{\text{InfoNCE}}_{x_t, b} = -\log \frac{\exp\{y_{S^{\text{pos}}_{x_t, b}}\}}{\exp\{y_{S^{\text{pos}}_{x_t, b}}\} + \sum_{S^{\text{neg}}} \exp\{y_{S^{\text{neg}}}\}}\\]
  Jointly trained end-to-end: \\(\mathcal{L}_{\text{Total}} = \mathcal{L}_{\text{NTP}} + \mathcal{L}_{\text{InfoNCE}}\\) [28–29].
* **PRM-Guided Beam Search:** At step \\(b\\), expands candidate beam paths to \\(K^+ \gg K\\) candidates, evaluates them with the Path-level PRM, and selects the top \\(K' \ll K^+\\) paths (where \\(K' = K\\)) to pass to the next decoder step [2, 34–37].

#### **Credit Assignment Mechanics**
* **No Multi-Touch Sequence Attribution:** Does **not** perform multi-touch sequence attribution or fractional credit assignment across historical user interaction logs.
* **Token/Step-Level Process Verification:** Credit is assigned at the **intermediate Semantic ID token/path level** (\\(b=1 \dots d\\)) during generative decoding by evaluating candidate SID prefix paths against user context via InfoNCE loss (\\(\mathcal{L}_{\text{InfoNCE}}\\)) [26–28].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets & Scale:**
  1. **Amazon Review Dataset:** *Beauty* and *Sports and Outdoors* categories (quantized via RQ-VAE into \\(d=3\\) codebook layers, \\(M=256\\)) [12, 13].
  2. **Kuaishou Industrial Dataset:** Real-world user logs from Kuaishou app covering **>400 million DAUs**, **~50 billion daily interactions**, and **>100 million daily items** (quantized via Residual K-means into \\(d=3\\) layers, \\(M=8192\\)) [14].
* **Production Deployment:** Fully deployed in live online A/B testing on **Kuaishou** and **Kuaishou Lite** apps (allocating 5% traffic / **~20 million users** per group for 7 days) [52–53].
* **Comparison Baselines:**
  * *Public Baselines:* Traditional sequential models (GRU4REC, Caser, HGN, \\(S^3\\)-Rec, Bert4Rec, SASRec) and Generative models (TIGER, HSTU, ActionPiece) [39–40, 42–43].
  * *Industrial Baselines:* GRank, MPFormer, MISS, GPRP, Kuaiformer, CRM [15, 16].

---

### **(5) Key Quantitative Results with Numbers**
* **Public Amazon Benchmark (Table 1):**
  * *Sports and Outdoors:* **Recall@5 = 0.0450** (+42.41% over ActionPiece), **NDCG@5 = 0.0296** (+44.39%), **Recall@10 = 0.0689** (+37.80%), **NDCG@10 = 0.0373** (+42.19%) [39–40].
  * *Beauty:* **Recall@5 = 0.0536** (+4.90%), **NDCG@5 = 0.0345** (+1.47%), **Recall@10 = 0.0821** (+5.60%), **NDCG@10 = 0.0437** (+3.07%) [39–40].
* **Industrial Dataset Benchmark (\\(K=1000\\), Table 2):**
  * *\\(K^+ = 4000\\):* **Recall@100 = 0.1494** (+47.92% vs. GRank), **NDCG@100 = 0.00652** (+38.14%), **Recall@500 = 0.2836** (+18.36%), **NDCG@500 = 0.01231** (+13.04%), **Recall@1000 = 0.3358** (+5.66%) [15].
  * *\\(K^+ = 6000\\):* **Recall@100 = 0.1609** (+59.31%), **NDCG@100 = 0.00663** (+40.47%), **Recall@500 = 0.3017** (+25.92%), **NDCG@500 = 0.01272** (+16.80%), **Recall@1000 = 0.3637** (+14.44%) [17].
* **Live Production Online A/B Test Results (7-day test vs. Control, 95% CI, Table 3):**
  * *Kuaishou App:* Total App Usage Time **+0.121%** [CI: +0.04%, +0.20%], App Usage Time Per User **+0.120%** [CI: +0.06%, +0.18%], Total Video Watch Time **+0.431%**, Watch Time per Video View **+0.440%** [18].
  * *Kuaishou Lite App:* Total App Usage Time **+0.131%** [CI: +0.03%, +0.23%], App Usage Time Per User **+0.160%** [CI: +0.07%, +0.25%], Total Video Watch Time **+0.398%**, Watch Time per Video View **+0.296%** [18].
* **System Deployment Efficiency:** Total parameter size increases by **only 15%**, and inference latency increases by **only 10%** (utilizing 1 PRM block, 1/4 attention heads, and GPU Radix Top-K optimization) [19].

---

### **(6) Limitations, Failure Modes, or Negative Results**
1. **Failure of Brute-Force Beam Scaling:** Simply increasing global beam size \\(K\\) in traditional beam search yields marginal metric improvements (HRecall@3@1000 stays around ~25.14%–25.97%) while drastically increasing decoder self/cross-attention compute [20, 21].
2. **Inefficiency of Parameter Scaling vs. Test-Time Scaling:** Increasing model parameters up to \\(5\times\\) achieves lower accuracy at equal FLOPs (26.67% HRecall@3@1000) compared to test-time candidate expansion (\\(K^+=6000\\), achieving 34.37%) [62–64].
3. **Performance Degradation with Partial PRM Step Activation:** Applying PRM at only 1 or 2 decoding steps is inferior to active step-wise verification across all 3 steps (HRecall@3@1000 drops from 0.3358 for all 3 steps to 0.2322–0.2650 for a single step) [54–55, 57].
4. **Exposure Bias / Semantic Drift Vulnerability:** Without dense intermediate PRM verification, standard NTP models revert to training marginal distributions when early prediction errors occur, exacerbating popularity bias toward generic items [17–18].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Rajput et al. (2023) [Ref 26 / TIGER]:** *Recommender systems with generative retrieval* (NeurIPS '23) [22].
2. **Lightman et al. (2023) [Ref 17 / OpenAI PRM]:** *Let’s verify step by step* (ICLR '23) [23].
3. **Zhai et al. (2024) [Ref 40 / HSTU]:** *Actions speak louder than words: trillion-parameter sequential transducers for generative recommendations* (ICML '24) [24].
4. **Snell et al. (2024) [Ref 30 / Test-Time Compute Scaling]:** *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters* [25].
5. **Wang et al. (2024) [Ref 36 / Math-Shepherd]:** *Math-shepherd: Verify and reinforce llms step-by-step without human annotations* (ACL '24) [26].
6. **Lee et al. (2022) [Ref 14] & Luo et al. (2025) [Ref 22]:** *Autoregressive image generation using residual quantization* (RQ-VAE) & *Quantitative alignment multi-modal recommendation at Kuaishou* (Residual K-means) [27, 28].
7. **Zhou et al. (2025) [Refs 46, 47, 48 / OneRec Series]:** *OneRec Technical Report* & *OneRec-v2 Technical Report* [89–90].

---

### **Part 2: Dating App Retention Attribution Project Evaluation**

#### **(A) Q1 or Q2 or Both or Neither?**
* **Neither.**
* **Explanation:**
  * **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** PROMISE is a generative recommendation framework that uses a Path-level Process Reward Model (PRM) to supervise intermediate Semantic ID (SID) generation steps during autoregressive decoding to mitigate "Semantic Drift" [6, 29]. It is not an industry multi-touch attribution (MTA) measurement system.
  * **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** It evaluates intermediate candidate Semantic ID path token prefixes (\\(S = [s_{\cdot, 1}, \dots, s_{\cdot, b}]\\)) during candidate item generation, rather than attributing overall retention, active days, or revisitation across historical user interaction logs [2, 12, 26–28].

---

#### **(B) Q2 Class**
* **Classification:** **NOT**
* **Justification:** PROMISE is a generative recommendation retrieval/ranking policy framework (Encoder-Decoder with Path-level PRM and PRM-guided Beam Search) [2, 12, 33–37]. It does **not** produce or publish a per-exposure retention credit table.

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction sequence attribution credit table.**
* **Target Outcome:** Next-item candidate retrieval accuracy (Recall@k, NDCG@k) and online video watch time / total app usage time in generative recommendation [13, 18, 30].

---

#### **(D) Replacing Last-Touch N7 → Latest Swipes**
* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% of an N7 retention label to recent swipes post-hoc, ignoring early interaction context and suffering from exposure bias. PROMISE replaces un-verified autoregressive decoding with **step-by-step process verification**. It uses a Path-level PRM to evaluate candidate token paths during generation, pruning erroneous reasoning branches early (\\(K^+ \gg K\\)) so generated recommendations remain aligned with user preferences rather than drifting into irrelevant semantic subspaces [2, 12, 33–37].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *User History Context (Encoder):* The user's historical profile swiping, matching, and messaging actions \\([x_1, \dots, x_{t-1}]\\) are encoded into hidden state \\(E^{(L)}\\) [9].
  2. *Candidate Profile Tokenization (Semantic IDs):* Candidate profile cards are tokenized into hierarchical Semantic IDs \\([s_1, s_2, s_3]\\) (e.g., \\(s_1\\) = coarse user demographic/interest cluster, \\(s_2\\) = sub-community/style, \\(s_3\\) = specific profile ID) [31].
  3. *Intermediate Verification (PRM-Guided Beam Search):* At each decoding step, the PRM evaluates expanded candidate profile token paths (\\(K^+ = 4000\\)) using cross-attention over user history \\(E^{(L)}\\) and prunes erroneous branches early (\\(K' = 1000\\)), ensuring generated profile recommendations stay aligned with true user preferences rather than drifting into irrelevant categories [26–28, 34–37].

---

#### **(E) Selection-Bias & Confounding Handling**
1. **Addresses Exposure Bias / Semantic Drift:** Resolves the discrepancy between teacher-forcing training and autoregressive inference where early errors accumulate [6, 17–18].
2. **Negative Sampling Strategy:** Uniformly samples \\(N\\) valid negative paths \\(S^{\text{neg}} \sim \text{Uniform}(\mathcal{V}_b \setminus \{S^{\text{pos}}_{x_t, b}\})\\) from the catalog valid path set \\(\mathcal{V}_b\\) at each depth \\(b\\), training the PRM via InfoNCE loss (\\(\mathcal{L}_{\text{InfoNCE}}\\)) on both positive and negative trajectories [21, 25–28].
3. **GPU-Parallel Radix Top-K Optimization:** Fast Top-K selection handles computational overhead when scaling candidate evaluation to \\(K^+ = 4000\\) or \\(6000\\) [19].

---

#### **(F) Deployed or Production Dataset Evidence**
* **Production Deployment:** Fully deployed in live online A/B testing on **Kuaishou** and **Kuaishou Lite** short-video apps (allocating 5% of total users / **~20 million users** per group for 7 days) [52–53].
* **Production Datasets & Numbers Quoted from Source:**
  * **Industrial Scale Dataset:** Real user logs covering **>400 million DAUs**, **~50 billion daily interactions**, and **>100 million daily items** (Residual K-means quantization \\(d=3, M=8192\\)) [14].
  * **Live Production Online A/B Test Results (Table 3):**
    * *Kuaishou App:* Total App Usage Time **+0.121%** [CI: +0.04%, +0.20%], App Usage Time Per User **+0.120%** [CI: +0.06%, +0.18%], Total Video Watch Time **+0.431%**, Watch Time per Video View **+0.440%** [18].
    * *Kuaishou Lite App:* Total App Usage Time **+0.131%** [CI: +0.03%, +0.23%], App Usage Time Per User **+0.160%** [CI: +0.07%, +0.25%], Total Video Watch Time **+0.398%**, Watch Time per Video View **+0.296%** [18].
  * **Industrial Dataset Benchmark (\\(K=1000\\), Table 2):**
    * *PROMISE (\\(K^+=4000\\)):* **Recall@100 = 0.1494** (+47.92% vs GRank), **NDCG@100 = 0.00652** (+38.14%), **Recall@500 = 0.2836** (+18.36%), **NDCG@500 = 0.01231** (+13.04%), **Recall@1000 = 0.3358** (+5.66%) [15].
    * *PROMISE (\\(K^+=6000\\)):* **Recall@100 = 0.1609** (+59.31%), **NDCG@100 = 0.00663** (+40.47%), **Recall@500 = 0.3017** (+25.92%), **NDCG@500 = 0.01272** (+16.80%), **Recall@1000 = 0.3637** (+14.44%) [17].
  * **Public Amazon Review Benchmark (Table 1):**
    * *Sports and Outdoors:* **Recall@5 = 0.0450** (+42.41%), **NDCG@5 = 0.0296** (+44.39%), **Recall@10 = 0.0689** (+37.80%), **NDCG@10 = 0.0373** (+42.19%) [39–40].
    * *Beauty:* **Recall@5 = 0.0536** (+4.90%), **NDCG@5 = 0.0345** (+1.47%), **Recall@10 = 0.0821** (+5.60%), **NDCG@10 = 0.0437** (+3.07%) [39–40].
  * **System Efficiency Overhead:** Parameter size increases by **only 15%**, and inference latency increases by **only 10%** [19].

---

💡 *Would you like to explore how PROMISE's Path-Level Process Reward Model or PRM-guided beam search could be adapted to prevent semantic drift in candidate profile token generation for your dating app?*

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
**Priority:** see queue.md `G28`
