# Zero-Observation User Reactivation with Gap-Driven Dimensional Gating (DeltaGate) [1]

**Source:** https://arxiv.org/pdf/2607.19802.pdf  
**Date analyzed:** 2026-09-24  
**NLM source id:** `5e293de3-47dc-4334-97d6-e9bd99c3bfed`  
**Queue id:** G36  
**Q2 class:** NOT

---

## 1. Summary

### **Section 1: Detailed Technical Breakdown of *DeltaGate: Zero-Observation User Reactivation with Gap-Driven Dimensional Gating***

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Zero-Observation User Reactivation with Gap-Driven Dimensional Gating* (DeltaGate) [1]
* **Authors:** Jiandong Ding¹*, Tianying Liu², Fuyuan Liu², Huijie Qin², Tiandeng Wu² (*\*Corresponding author: Jiandong Ding*) [1, 2]
* **Affiliations:** ¹**Fudan University** (Shanghai, China); ²**Huawei Technologies** (Shanghai, China) [1]
* **Year & Venue:** Published in **2026** at the *20th ACM Conference on Recommender Systems (RecSys ’26)*, September 27–October 02, 2026, Minneapolis, MN, USA [2]

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Sequential Recommendation (SR) models predict next items from ordered historical interactions, but when a user returns after a long observation-free period (a macro-gap \\(\Delta t\\), e.g., months or years without any in-app activity), the reliability of their stale pre-gap representation is uncertain (**Zero-Observation User Reactivation**) [1, 3]. Standard sequence backbones (recurrent, unidirectional, or bidirectional) experience steep monotonic performance decay across widening gap buckets, and internal time-interval mechanisms (e.g., TiSASRec) fail to recover performance in macro-gap regimes (\\(>365\\) days) [1, 4].
* **Key Contribution:**
  1. **Zero-Observation Reactivation Formalization:** Defines the Zero-Observation Reactivation problem and documents monotonic decay across time-gap buckets across multiple SR backbones [1, 5].
  2. **DeltaGate Architecture:** Proposes **DeltaGate**, a lightweight, backbone-agnostic output-layer plugin (adding only **66K trainable parameters**, a **2–4% parameter overhead**) that keeps the pre-trained SR encoder frozen and uses a two-layer MLP conditioned jointly on the inactivity gap (\\(\log(1+\Delta t)\\)) and personalized user state (\\(\mathbf{h}_{\text{pers}}\\)) to dynamically route each vector dimension between personalized history and a learned, zero-initialized global prior (\\(\mathbf{h}_{\text{global}}\\)) [2, 22–24, 29].
  3. **Zero Backbone Drift:** Preserves **zero backbone/embedding drift** (unlike full end-to-end retraining which causes **139.7% embedding drift**), achieving significant accuracy recovery in macro-gap regimes (\\(>365\text{d}\\)) [6-8].

---

#### **(3) Proposed Method or Architecture in Detail**

##### **Architectural Modules**
* **Frozen Backbone Encoders (\\(\mathbf{h}_{\text{pers}}\\)):** Compatible across three representative paradigm families [19–21]:
  * *Unidirectional Attention (SASRec):* Converts sequence to embeddings \\(\mathbf{E} + \mathbf{P}\\), applies stacked causal MHA and FFN blocks, and extracts the final item hidden state \\(\mathbf{h}_{\text{pers}} \in \mathbb{R}^d\\) (\\(d=128\\)) [19–20].
  * *Recurrent Networks (GRU4Rec):* Processes sequence via GRU units; final hidden state serves as \\(\mathbf{h}_{\text{pers}} = \mathbf{h}_k\\) [20–21].
  * *Bidirectional Transformer (BERT4Rec):* Appends a `[MASK]` token at the chronological end of the pre-gap sequence (\\(\mathbf{S}_{\text{pre}} \oplus [\text{MASK}]\\)) and extracts its final hidden state as \\(\mathbf{h}_{\text{pers}}\\) [9].
* **Gap-Driven Dimensional Gate (\\(\mathbf{g}\\)):** Computes a dimension-wise gating vector \\(\mathbf{g} \in (0, 1)^d\\) using a two-layer MLP conditioned on the log-transformed gap \\(\log(1 + \Delta t)\\) and personalized state \\(\mathbf{h}_{\text{pers}}\\) [22–23]:
  \\[\mathbf{g} = \sigma\left(\text{MLP}\left([\log(1 + \Delta t) \parallel \mathbf{h}_{\text{pers}}]\right)\right)\\]
  where \\(\Delta t\\) is measured in days, and \\(\text{MLP}: \mathbb{R}^{d+1} \to \mathbb{R}^{2d} \to \mathbb{R}^d\\) uses a ReLU hidden layer [10].
* **Representation Fusion:** Interpolates personalized history \\(\mathbf{h}_{\text{pers}}\\) with a learned global prior \\(\mathbf{h}_{\text{global}}\\) (initialized to 0) via Hadamard product (\\(\odot\\)) [11, 12]:
  \\[\mathbf{h}_{\text{final}} = \mathbf{g} \odot \mathbf{h}_{\text{pers}} + (\mathbf{1} - \mathbf{g}) \odot \mathbf{h}_{\text{global}}\\]
  Item score is predicted via \\(y_j = \mathbf{h}_{\text{final}}^\top \mathbf{e}_j + b_j\\), trained using full-catalog cross-entropy loss \\(\mathcal{L}\\) updating *only* the gate MLP and \\(\mathbf{h}_{\text{global}}\\) [12].
* **Historical Confidence Index (\\(c(\Delta t)\\)):** Defines \\(c(\mathbf{h}_{\text{pers}}, \Delta t) = \frac{1}{d} \sum_{i=1}^d g_i = \frac{1}{d}\|\mathbf{g}\|_1 \in (0, 1)\\) as an interpretable index summarizing the average history retention weight across dimensions [13].

##### **Credit Assignment Mechanics**
* **Not specified / Does NOT perform credit assignment across touchpoints.**
* DeltaGate operates exclusively at the final output user representation layer to fuse vector dimensions for next-item prediction [1, 23–24]. It does **not** perform multi-touch sequence attribution or assign credit to individual past interaction touchpoints.

---

#### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets & Gap-Synthesize Protocol:** Amazon Product Reviews (2018) across 3 categories under 5-core filtering and chronological leave-one-out evaluation over full catalog ranking [14-16]:
  * *Amazon Video Games:* **55,220 users**, **17,408 items**, **387,125 train interactions**, **55,220 test targets** [16].
  * *Amazon CDs & Vinyl:* **112,319 users**, **73,713 items**, **1,218,826 train interactions**, **112,319 test targets** [16].
  * *Amazon Movies & TV:* **297,498 users**, **60,175 items**, **2,814,911 train interactions**, **297,498 test targets** [16].
  * *Gap Buckets:* \\(<30\text{d}\\) (Active), \\(30\text{--}90\text{d}\\), \\(90\text{--}180\text{d}\\), \\(180\text{--}365\text{d}\\), and \\(>365\text{d}\\) (Macro-Gap) [14, 17]. In Video Games, the \\(>365\text{d}\\) cohort contains **10,596 users** (**19.2%** of test users) [17].
* **Production Deployment:** **Not specified in source** (open-source benchmark code provided on GitHub; evaluated on offline Amazon datasets) [6, 16].
* **Comparison Baselines:**
  * *Sequential Backbones:* SASRec, GRU4Rec, BERT4Rec, TiSASRec (time-interval aware self-attention) [18].
  * *End-to-End Retraining Comparator:* TimeConcat E2E (concatenates \\(\log(1+\Delta t)\\) with SASRec input and retrains all ~2.6M parameters) [18, 19].
  * *Ablation Endpoint:* Ablation-Prior (\\(g=0\\), pure global prior endpoint) [19, 20].

---

#### **(5) Key Quantitative Results with Numbers**

* **Macro-Gap (\\(>365\text{d}\\)) Reactivation Recovery (Table 3):**
  * *Amazon Video Games:* DG-SASRec reaches **0.047 Hit@10** (vs. SASRec **0.031**, +51.6% lift) and **0.023 NDCG@10** (vs. **0.015**); DG-BERT4Rec reaches **0.046 Hit@10** (vs. BERT4Rec **0.025**, +84.0% lift, \\(p < 0.01\\)) and **0.023 NDCG@10** (vs. **0.012**) [6, 21].
  * *Amazon CDs & Vinyl:* DG-SASRec reaches **0.040 Hit@10** (vs. SASRec **0.022**); DG-BERT4Rec reaches **0.041 Hit@10** (vs. BERT4Rec **0.026**, \\(p < 0.01\\)) [21].
  * *Amazon Movies & TV:* DG-SASRec reaches **0.034 Hit@10** (vs. SASRec **0.021**); DG-BERT4Rec reaches **0.035 Hit@10** (vs. BERT4Rec **0.024**, \\(p < 0.01\\)) [21].
* **Adaptation Strategy Trade-Offs (Table 5 & Table 6 - Video Games \\(>365\text{d}\\)):**
  * *DeltaGate Plugin (Frozen Backbone):* **Hit@10 = 0.047**, **66K trainable parameters**, **0% embedding drift**, **Gain/1M = 0.245** [7].
  * *TimeConcat E2E (Full Retraining):* **Hit@10 = 0.080**, **2.6M trainable parameters**, **139.7% embedding L2 drift**, **Gain/1M = 0.018** [7, 8].
  * *DeltaGate E2E (Joint Retraining):* **Hit@10 = 0.057**, **2.6M parameters**, **103.4% embedding drift**, **82.0% gate saturation** [7, 22].
* **Routing Component Controls (Table 4):**
  * Ablation-Prior (\\(g=0\\)) achieves only **0.005–0.008 Hit@10**, proving that performance gain stems from learned dimension-wise interpolation rather than replacing history with a single global vector [19, 20].
* **Catalog Coverage & Exclusive Hits (Tables 8 & 9):**
  * Catalog coverage increases from **43.97% to 59.75%** (Video Games), **46.71% to 67.73%** (CDs & Vinyl), and **51.63% to 73.37%** (Movies & TV), demonstrating that DeltaGate does not collapse into a pure popularity list [23, 24].

---

#### **(6) Limitations, Failure Modes, or Negative Results**
1. **End-to-End Retraining Superiority in Absolute Accuracy:** Full end-to-end retraining (TimeConcat E2E) achieves higher absolute accuracy than the frozen plugin (**0.080 vs. 0.047 Hit@10** in \\(>365\text{d}\\) Video Games), though it requires **~40\\(\times\\) more trainable parameters** (2.6M vs. 66K) and causes **139.7% embedding drift** [7, 8, 25].
2. **Gate Saturation in End-to-End Training:** Under joint end-to-end training (DeltaGate E2E), **82.0% of gate values exceed 0.9**, as the retraining backbone absorbs temporal information, rendering the explicit gate mechanism inactive unless frozen [7, 22].
3. **Single Shared Global Prior:** Uses one fixed global vector \\(\mathbf{h}_{\text{global}}\\) for all users, which cannot represent distinct fallback profiles for different user archetypes or adapt to rapid multi-year catalog drift without periodic retraining [26, 27].
4. **Vulnerability to Pre-Gap History Sparsity:** Gate quality relies on the frozen backbone's personalized representation \\(\mathbf{h}_{\text{pers}}\\). For users with sparse pre-gap histories, representation staleness compounds with history sparsity [27].
5. **No Causal / Popularity Debiasing:** The authors explicitly state that DeltaGate does *not* estimate a causal recommendation effect or remove popularity bias; the controlled diagnostic is an input sensitivity test, not a causal population effect estimate [28-30].

---

#### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Kang & McAuley (2018) [Ref 11]:** *Self-Attentive Sequential Recommendation* (SASRec, IEEE ICDM) [31].
2. **Sun et al. (2019) [Ref 23]:** *BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer* (ACM CIKM) [32].
3. **Hidasi et al. (2016) [Ref 8]:** *Session-based recommendations with recurrent neural networks* (GRU4Rec, ICLR) [33].
4. **Li, Wang, & McAuley (2020) [Ref 14]:** *Time Interval Aware Self-Attention for Sequential Recommendation* (TiSASRec, ACM WSDM) [34].
5. **Houlsby et al. (2019) [Ref 9] & Hu et al. (2022) [Ref 10]:** *Parameter-Efficient Transfer Learning for NLP* & *LoRA: Low-Rank Adaptation of Large Language Models* (PEFT foundation) [33].
6. **Krichene & Rendle (2020) [Ref 12]:** *On sampled metrics for item recommendation* (ACM SIGKDD) [31].
7. **Kumar, Zhang, & Leskovec (2019) [Ref 13]:** *Predicting dynamic embedding trajectory in temporal interaction networks* (JODIE, ACM SIGKDD) [31].

---

### **Section 2: Dating App Retention Attribution Project Evaluation**

#### **(A) Q1 or Q2 or Both or Neither?**
* **Neither.** [1, 2]
* **Explanation:**
  * **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** While published in RecSys 2026, DeltaGate is a parameter-efficient sequential recommendation output-layer plugin (using dimensional gating conditioned on observation-free gaps) for user reactivation, not an industry multi-touch attribution (MTA) measurement system [1, 2].
  * **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** DeltaGate recalibrates user representations for next-item prediction after long inactivity periods (\\(\Delta t\\)), rather than attributing N7 retention, active days, or revisitation back to individual past interaction touchpoints (swipes, matches, or messages) across historical logs [1, 35, 36].

---

#### **(B) Q2 Class**
* **Classification:** **NOT** [1, 23–24]
* **Justification:** DeltaGate is a sequential recommendation representation-routing architecture (frozen backbone + gap-driven dimensional gating + global prior interpolation) for next-item recommendation [2, 23–24]. It does **not** produce or publish a per-exposure retention credit table.

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction credit table.** [1, 23–24]
* **Target Outcome:** Next-item recommendation accuracy (**Hit@10**, **NDCG@10**) upon user reactivation after an observation-free inactivity gap (\\(\Delta t\\)) [21, 36].

---

#### **(D) How This Replaces or Improves Last-Touch N7 → Latest Swipes**
* **How it Improves/Informs Ranking/Reactivation:** DeltaGate does **not** provide a post-hoc attribution credit model [1, 23–24]. However, for a user returning after an inactivity gap \\(\Delta t\\) (e.g., returning to the dating app after weeks or months), standard sequential rankers suffer severe accuracy degradation if they treat stale pre-gap swiping history as current [1, 3]. DeltaGate improves recommendation quality upon reactivation by using a lightweight gate \\(\mathbf{g} = \sigma(\text{MLP}([\log(1+\Delta t) \parallel \mathbf{h}_{\text{pers}}]))\\) to route uncertain preference dimensions toward a global prior \\(\mathbf{h}_{\text{global}}\\), preventing stale swiping histories from corrupting initial recommendations upon return [2, 23–24].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  * **Pre-Gap Swiping/Matching History (\\(\mathbf{S}_{\text{pre}}\\)):** Encodes the user's past swipes, matches, and chat sessions up until their hiatus into a dense representation \\(\mathbf{h}_{\text{pers}}\\) [15, 20–21].
  * **Inactivity Gap (\\(\Delta t\\)):** The number of days between the user's last app session and their return session [35, 36].
  * **Reactivation Profile Scoring (\\(\mathbf{h}_{\text{final}}\\)):** Fuses the stale user profile embedding \\(\mathbf{h}_{\text{pers}}\\) with global population trends \\(\mathbf{h}_{\text{global}}\\) dimension-by-dimension based on \\(\Delta t\\), ensuring candidate profile ranking upon return balances historical user taste with baseline appeal [23–24].

---

#### **(E) Selection-Bias & Confounding Handling**
1. **Addresses Representation Staleness & Temporal Gap Decay:** Directly models macro-gap inactivity (\\(\Delta t \ge 30\text{d}\\) to \\(>365\text{d}\\)) to prevent stale user embeddings from degrading next-session recommendation accuracy [17, 36].
2. **Gap-Synthesize Protocol Evaluation:** Evaluates naturally observed terminal inactivity gaps using user-level chronological leave-one-out targets and full catalog ranking (avoiding sampled metric biases) [16–18].
3. **Controls for Popularity Collapse:** Demonstrates through catalog coverage and method-exclusive hit analysis that routing to a global prior increases catalog coverage (from 43.97% to 59.75% on Video Games) rather than collapsing into a pure popularity list [23, 24].

---

#### **(F) Deployed or Production Dataset Evidence**
* **Production Deployment:** **Not specified in source** (open-source benchmark code provided on GitHub; tested on offline Amazon product review datasets) [6, 16].
* **Datasets & Numbers Quoted from Source:**
  * **Amazon Video Games:** **55,220 users**, **17,408 items**, **387,125 train interactions** (**10,596 users** or **19.2%** in \\(>365\text{d}\\) macro-gap cohort) [16, 17].
  * **Amazon CDs & Vinyl:** **112,319 users**, **73,713 items**, **1,218,826 train interactions** [16].
  * **Amazon Movies & TV:** **297,498 users**, **60,175 items**, **2,814,911 train interactions** [16].
  * **Key Metrics (\\(>365\text{d}\\) Macro-Gap Bucket):**
    * *DG-SASRec Hit@10:* **0.047** (Video Games), **0.040** (CDs & Vinyl), **0.034** (Movies & TV) vs. SASRec **0.031**, **0.022**, **0.021** [21].
    * *DG-BERT4Rec Hit@10:* **0.046** (Video Games), **0.041** (CDs & Vinyl), **0.035** (Movies & TV) vs. BERT4Rec **0.025**, **0.026**, **0.024** (\\(p < 0.01\\)) [21].
    * *Trainable Parameters:* **66K parameters** (~2–4% overhead relative to 1.7M–3.0M backbones) vs. **2.6M parameters** for full retraining [7, 37].
    * *Embedding L2 Drift:* **0%** for DeltaGate plugin vs. **139.7%** for TimeConcat E2E full retraining [7].

---

💡 *Would you like to explore how DeltaGate's gap-driven dimensional gating could be integrated into your dating app's candidate ranker to improve profile recommendations for returning dormant users?*

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

### **Source Evaluation: *Zero-Observation User Reactivation with Gap-Driven Dimensional Gating* (DeltaGate)**  
*(Ding et al., Fudan University & Huawei Technologies, RecSys ’26)* [1]

---

### **(A) Q1 or Q2 or Both or Neither?**

**Neither.** [1, 2]  
* **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** While accepted at RecSys ’26 (September 2026), DeltaGate is a parameter-efficient sequential recommendation output-layer plugin designed for user reactivation following an observation-free inactivity gap, rather than an industry multi-touch attribution (MTA) measurement system [1, 3, 4].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** DeltaGate recalibrates user representations for next-item recommendation upon user return after a macro-gap (\\(\Delta t\\)), rather than attributing overall retention, active days, or revisitation back to individual past interaction touchpoints (e.g., swipes or messages) across historical logs [1, 2, 5].

---

### **(B) Q2 Class**

**NOT.** [1, 4, 6]  
* **Justification:** DeltaGate is a sequential recommendation representation-routing architecture (frozen backbone + gap-driven dimensional gating + global prior interpolation) for next-item recommendation [4, 6, 7]. It does **not** produce or publish a per-exposure retention credit table.

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction credit table.** [1, 6]
* **Target Outcome:** Next-item recommendation accuracy (**Hit@10**, **NDCG@10**) upon user reactivation after an observation-free inactivity gap (\\(\Delta t\\)) [1, 8, 9].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**

* **How it Improves/Informs Ranking/Reactivation:** DeltaGate does **not** provide a post-hoc attribution credit model [1, 6]. However, for a user returning to a dating app after an inactivity gap \\(\Delta t\\) (e.g., returning after weeks or months), standard sequential rankers suffer severe accuracy degradation if they treat stale pre-gap swiping history as current [1, 2]. DeltaGate improves recommendation quality upon reactivation by using a lightweight gate \\(\mathbf{g} = \sigma(\text{MLP}([\log(1+\Delta t) \parallel \mathbf{h}_{\text{pers}}]))\\) to route uncertain preference dimensions toward a learned global prior \\(\mathbf{h}_{\text{global}}\\), preventing stale swiping histories from corrupting initial recommendations upon return [2, 22–24].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  * **Pre-Gap Swiping/Matching History (\\(\mathbf{S}_{\text{pre}}\\)):** Encodes the user's past swipes, matches, and chat sessions up until their hiatus into a dense representation \\(\mathbf{h}_{\text{pers}}\\) [15, 20–21].
  * **Inactivity Gap (\\(\Delta t\\)):** The number of days between the user's last app session and their return session [15–16].
  * **Reactivation Profile Scoring (\\(\mathbf{h}_{\text{final}}\\)):** Fuses the stale user profile embedding \\(\mathbf{h}_{\text{pers}}\\) with global population trends \\(\mathbf{h}_{\text{global}}\\) dimension-by-dimension based on \\(\Delta t\\), ensuring candidate profile ranking upon return balances historical user taste with baseline appeal [23–24].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Addresses Representation Staleness & Temporal Gap Decay:** Directly models macro-gap inactivity (\\(\Delta t \ge 30\text{d}\\) to \\(>365\text{d}\\)) to prevent stale user embeddings from degrading next-session recommendation accuracy [1, 10, 11].
2. **Gap-Synthesize Protocol Evaluation:** Evaluates naturally observed terminal inactivity gaps using user-level chronological leave-one-out targets and full catalog ranking (avoiding sampled metric biases) [16–18].
3. **Controls for Popularity Collapse:** Demonstrates through catalog coverage and method-exclusive hit analysis that routing to a global prior increases catalog coverage rather than collapsing into a pure popularity list [12, 43–44].
4. **Causal Clarification:** The authors explicitly note that DeltaGate *"does not estimate a causal recommendation effect or remove popularity bias"* [12].

---

### **(F) Deployed or Production Dataset Evidence**

* **Production Deployment:** **Not specified in source** for live deployment (open-source benchmark code provided on GitHub; tested on offline Amazon product review datasets) [7, 8].
* **Quoted Dataset Statistics (Table 1 & Table 2):**
  * **Amazon Video Games:** **55,220 users**, **17,408 items**, **387,125 train interactions** (**10,596 test users** or **19.2%** in the \\(>365\text{d}\\) macro-gap cohort) [8, 10].
  * **Amazon CDs & Vinyl:** **112,319 users**, **73,713 items**, **1,218,826 train interactions** [8].
  * **Amazon Movies & TV:** **297,498 users**, **60,175 items**, **2,814,911 train interactions** [8].
* **Quoted Quantitative Results (Table 3, Table 5, Table 8):**
  * **Macro-Gap (\\(>365\text{d}\\)) Reactivation Recovery (Table 3):**
    * *DG-SASRec Hit@10:* **0.047** (Video Games), **0.040** (CDs & Vinyl), **0.034** (Movies & TV) vs. SASRec **0.031**, **0.022**, **0.021** [9].
    * *DG-BERT4Rec Hit@10:* **0.046** (Video Games), **0.041** (CDs & Vinyl), **0.035** (Movies & TV) vs. BERT4Rec **0.025**, **0.026**, **0.024** (\\(p < 0.01\\)) [9].
  * **Adaptation Strategy Trade-Offs (Table 5):**
    * *DeltaGate Plugin (Frozen Backbone):* **Hit@10 = 0.047**, **66K trainable parameters** (~2–4% overhead), **0% embedding drift**, **Gain/1M = 0.245** [7, 13, 14].
    * *TimeConcat E2E (Full Retraining):* **Hit@10 = 0.080**, **2.6M trainable parameters**, **139.7% embedding L2 drift**, **Gain/1M = 0.018** [14].
    * *DeltaGate E2E (Joint Retraining):* **Hit@10 = 0.057**, **2.6M parameters**, **103.4% embedding drift**, **82.0% gate saturation** [38–39].
  * **Catalog Coverage Expansion (Table 8):**
    * *Video Games:* **43.97% \\(\to\\) 59.75%** [15].
    * *CDs & Vinyl:* **46.71% \\(\to\\) 67.73%** [15].
    * *Movies & TV:* **51.63% \\(\to\\) 73.37%** [15].

---

💡 *Would you like to explore how DeltaGate's gap-driven dimensional gating could be integrated into your dating app's candidate ranker to improve profile recommendations for returning dormant users?*

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
**Priority:** see queue.md `G36`
