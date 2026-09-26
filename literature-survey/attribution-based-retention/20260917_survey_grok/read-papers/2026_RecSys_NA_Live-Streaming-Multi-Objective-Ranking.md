# Multi-Objective Ranking for Live-Streaming: Balancing Fresh and Delayed Signals with Segment-Aware Targeting [1, 2]

**Source:** https://arxiv.org/pdf/2608.04455.pdf  
**Date analyzed:** 2026-09-24  
**NLM source id:** `f678e8c0-439b-4d8b-892f-d9df02becb0a`  
**Queue id:** G37  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Multi-Objective Ranking for Live-Streaming: Balancing Fresh and Delayed Signals with Segment-Aware Targeting* [1, 2]
* **Authors:** Xiaoyi Gu, Julia Tavares, Eder Santana, Carlos Mendoza-Cardenas, Nikita Mishra\*, and Saad Ali (\*Work performed while at Twitch Interactive) [1, 3]
* **Affiliations:** **Twitch Interactive** (San Francisco, CA, USA) and **Amazon Prime Video** (Sunnyvale, CA, USA) [1–2]
* **Year & Venue:** Published in **2026** at the *20th ACM Conference on Recommender Systems (RecSys ’26)*, September 27–October 02, 2026, Minneapolis, MN, USA [3–4]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Live-streaming recommendation systems face three fundamental challenges when balancing viewer engagement, retention, and creator monetization [2, 4, 5]:
  1. *Target Sparsity:* High-value actions (following, chatting, spending/subscriptions) occur orders of magnitude less frequently than clicks or short views (e.g., chat rates are ~20x lower and follow rates are ~90x lower than clicks) [6–7].
  2. *Delayed Feedback:* High-value user actions occur hours, days, or weeks after exposure; labeling non-responses as negative too early injects noise, while waiting too long makes feature representations stale [5].
  3. *User Segment Bias:* Training data is heavily dominated by highly active users (Dedicated viewers contribute ~4x more training samples than Early viewers), biasing ranking models away from new or less active users who represent critical long-term growth potential [5-7].
* **Key Contributions:**
  1. *Delayed Window Framework:* A 14-day observation window (\\(DW_{v_i, c_j}\\)) that converts sparse, delayed actions into dense binary target labels [2, 10, 22–23].
  2. *Multi-Model Architecture (FSM + DSM):* Separates fresh signals (Fresh Signal Model for immediate shallow engagement like Short-form Minutes Play [SMP]) from sparse delayed signals (Delayed Signal Models for chat, follow, and spend) to keep serving features fresh [2, 10, 25–26].
  3. *Viewer Segment Targeting (VST):* Applies inference-time segment-conditioned objective weighting tailored to Early (E) vs. Dedicated (D) viewers without maintaining separate segment-specific models [2, 10, 27–28].
  4. *MMoE Consolidation:* Consolidates independent DSMs into a Multi-gate Mixture-of-Experts (MMoE) architecture (4 expert networks), reducing delayed-target modeling parameters by **41.9%** while serving live recommendations at **<110ms p99 latency** [4, 8-10].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Architectural Components**
* **Fresh Signal Model (FSM):** Predicts shallow, immediate engagement (Short-form Minutes Play, SMP) using immediate labels, ensuring serving-time features remain up-to-date [25–26].
* **Delayed Window (DW) & Delayed Signal Models (DSM):** For sparse actions \\(a \in \{\text{chat}, \text{follow}, \text{spend}\}\\), aggregates user responses over a \\(\Delta t = 14\\)-day window following exposure timestamp \\(t\\) [22–23]:
  \\[y_{v_i, c_j}^{\text{delayed}} = \mathbb{I}\left[\left|DW_{v_i, c_j}(t, \Delta t)\right| > 0\right]\\]
  Long-form Minutes Play (LMP) uses immediate labels but is grouped with delayed targets due to shared deep-engagement characteristics [11].
* **MMoE Task Grouping:** Replaces independent DSMs with an MMoE model (\\(K=4\\) expert networks) that jointly predicts \\(\{LMP, \text{chat}, \text{follow}, \text{spend}\}\\) [29–31]. The MMoE uses 3 shared-bottom layers (size 1000), 4 expert networks (2 layers: 512, 256), task-specific gating networks (4 layers: 128 each), and 1-layer task towers (size 64) [12].
* **Viewer Segment Targeting (VST):** Categorizes viewers at inference time into **Early (E)** (account age \\(\le M\\) days or visit/chat days \\(\le N\\)) vs. **Dedicated (D)** [13]. Applies segment-conditioned weights \\(w_{a,s}\\) to assemble the final ranking score [28, 31–32]:
  \\[F_{\text{FSM-MMoE-VST}}(x_{v_i, c_j}, s) = w_{\text{smp}, s} \cdot p_{\text{smp}}^{\text{FSM}}(x_{v_i, c_j}) + \sum_{a} w_{a,s} \cdot p_a^{\text{MMoE}}(x_{v_i, c_j})\\]
  E viewers prioritize immediate engagement (SMP), whereas D viewers balance monetization (spend) and community engagement [38–39].

#### **Credit Assignment Mechanics**
* **Does NOT perform multi-touch attribution or per-touchpoint sequence credit assignment.**
* The framework uses a **14-day delayed window binary indicator** (\\(y^{\text{delayed}} \in \{0, 1\}\\)) to construct training labels for multi-task candidate ranking models [22–23]. It does not output or publish a per-touchpoint attribution credit table.

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets & Offline Setup:**
  * *Training Set:* 7 days of historical impression logs from 6 million viewers [35–36].
  * *Evaluation Set:* 1 day of impression data from 1 million viewers, evaluated against a **35-day forward window** for ground-truth delayed labels [14].
* **Production Deployment:** Fully deployed in live production at **Twitch** on the primary live-stream channel recommendation surface and Twitch mobile live feed, serving millions of daily active viewers at **<110ms p99 latency** [4, 8, 10].
* **Comparison Baselines:**
  * **YouTube DNN / Single-Objective Point-wise Model:** Previous production baseline predicting SMP with a monetization heuristic feature (Monetization Attach Ratio, MAR) [15, 16].
  * **Single Unified Multi-Task Models:** Single Shared-Bottom, Single MMoE, and Single CGC (PLE core extraction module) jointly modeling all 5 targets (including SMP) in a single unified architecture [12, 16, 17].
  * **Alternative FSM + Multi-Task Backbones:** FSM + Shared-Bottom + VST, FSM + CGC + VST [12, 16].

---

### **(5) Key Quantitative Results with Numbers**

* **Live Production Online A/B Test Results (14-Day Tests, Table 2):**
  * **Exp 1 (Multi-Model with 14-Day Delayed Window vs. Baseline):**
    * *Daily Active Viewers (DAV):* **+0.09%** overall (\\(p < 0.01\\); **+0.10%** E viewers, **+0.08%** D viewers) [18, 19].
    * *Long Minutes Play (LMP):* **+0.16%** overall (\\(p < 0.01\\); **+0.17%** D viewers) [18, 19].
    * *Capped ARPU (Revenue):* **+0.56%** for Dedicated (D) viewers (\\(p < 0.05\\)) [4, 18, 19].
  * **Exp 2 (Viewer Segment Targeting VST vs. Exp 1 Winner):**
    * *Early (E) Viewer Engagement:* **+0.15%** DAV (\\(p < 0.05\\)), **+0.25%** LMP (\\(p < 0.01\\)) [2, 49–50].
  * **Exp 3 (MMoE Consolidation vs. Independent DSMs):**
    * *New Follows:* **+0.27%** overall (\\(p < 0.01\\); **+0.44%** D viewers) [4, 19, 20].
    * *Overall DAV & LMP:* **+0.08%** DAV (\\(p < 0.05\\)), **+0.10%** LMP (\\(p < 0.05\\)) [4, 19, 20].
  * **Mobile Live Feed Generalization:** **+1.12%** increase in positive user-channel interactions (clicks, follows, likes; \\(p < 0.001\\)) [4, 10].
  * **System Efficiency Gains:** Reduced delayed-target model parameters from 26.7M to 15.5M (**41.9% reduction**) while maintaining <110ms p99 latency [4, 9].

* **Offline Benchmark Metrics (NDCG@6, Table 1):**
  * *FSM + MMoE + VST:* **Spend NDCG@6 = 0.0739** (+1.79% over YouTube DNN baseline 0.0726), **LMP NDCG@6 = 0.2462** (+0.12% over baseline 0.2459) [16].
  * *Single Unified MTL Failure:* Single MMoE (**LMP = 0.2347**, -4.55% drop), Single Shared-Bottom (**LMP = 0.2355**, -4.23% drop), Single CGC (**LMP = 0.2355**, -4.23% drop) [16].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Failure of Single Unified Multi-Task Models:** Jointly modeling shallow engagement (SMP) alongside deeper/delayed targets in a single unified architecture (Single MMoE, Single Shared-Bottom, Single CGC) severely degraded LMP performance (**-4.2% to -4.6%**) because the extremely dense SMP signal dominated gradient updates [43, 54, 56–57].
2. **Signal Staleness in Extended Windows:** Extending the delayed window beyond 14 days (e.g., 21–35 days) yielded diminishing returns for spend and caused engagement metrics (LMP NDCG) to decline due to attributing actions to stale, unassociated impressions [21-23].
3. **Failure of Training-Time Loss Weighting:** Applying higher loss weights to Early (E) viewer samples during model training failed to improve performance and increased training complexity; segment bias was only successfully resolved via inference-time weight scalarization [23, 24].
4. **Manual Segment Weight Configuration:** Segment-conditioned weights (\\(w_{a,s}\\)) were selected manually via offline grid search and A/B guardrails rather than learned dynamically via online adaptive scalarization [23, 24].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Ma et al. (2018) [Ref 20 / MMoE]:** *Modeling task relationships in multi-task learning with multi-gate mixture-of-experts* (ACM SIGKDD '18) [25-27].
2. **Tang et al. (2020) [Ref 28 / PLE & CGC]:** *Progressive layered extraction (ple): A novel multi-task learning (mtl) model for personalized recommendations* (ACM RecSys '20) [25, 26, 28].
3. **Chapelle (2014) [Ref 5 / Delayed Feedback]:** *Modeling delayed feedback in display advertising* (ACM SIGKDD '14) [29, 30].
4. **Covington, Adams, & Sargin (2016) [Ref 8 / YouTube DNN]:** *Deep neural networks for youtube recommendations* (ACM RecSys '16) [25, 31, 32].
5. **Zhao et al. (2019) [Ref 37 / YouTube Multitask RecSys]:** *Recommending what video to watch next: a multitask ranking system* (ACM RecSys '19) [25, 33, 34].
6. **Ma et al. (2018) [Ref 21 / ESMM]:** *Entire space multi-task model: An effective approach for estimating post-click conversion rate* (ACM SIGIR '18) [12, 25, 27].
7. **Xi et al. (2021) [Ref 32 / AITM]:** *Modeling the sequential dependence among audience multi-step conversions with multi-task learning in targeted display advertising* (ACM SIGKDD '21) [12, 25, 35].

---

💡 *Would you like to explore how Twitch's fresh/delayed signal separation or segment-aware targeting could be adapted to balance immediate profile swipes with delayed conversation/match retention in your dating app?*

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

### **Section 1: Detailed Breakdown of *LiveStreamMOR_2608.04455.pdf***

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Multi-Objective Ranking for Live-Streaming: Balancing Fresh and Delayed Signals with Segment-Aware Targeting* [1]
* **Authors:** **Xiaoyi Gu**, **Julia Tavares**, **Eder Santana**, **Carlos Mendoza-Cardenas**, **Nikita Mishra**\*, and **Saad Ali** (\*Work performed while at Twitch Interactive) [1]
* **Affiliations:** **Twitch Interactive** (San Francisco, CA, USA) and **Amazon Prime Video** (Sunnyvale, CA, USA) [1]
* **Year & Venue:** Published in **2026** at the *20th ACM Conference on Recommender Systems (RecSys ’26)*, September 27–October 02, 2026, Minneapolis, MN, USA [3–4]

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Live-streaming recommendation systems face three fundamental challenges when balancing viewer engagement, retention, and creator monetization [2, 6–8]:
  1. *Target Sparsity:* High-value actions (following, chatting, spending/subscriptions) occur orders of magnitude less frequently than clicks or short views (e.g., chat rates are ~20x lower and follow rates are ~90x lower than clicks) [6–7].
  2. *Delayed Feedback:* High-value user actions occur hours, days, or weeks after exposure; labeling non-responses as negative too early injects noise, while waiting too long makes feature representations stale [2].
  3. *User Segment Bias:* Training data is heavily dominated by highly active users (Dedicated viewers contribute ~4x more training samples than Early viewers), biasing ranking models away from new or less active users who represent critical long-term growth potential [2, 3].
* **Key Contributions:**
  1. *Delayed Window Framework:* A 14-day observation window (\\(DW_{v_i, c_j}\\)) that converts sparse, delayed actions into dense binary target labels [2, 10, 22–23].
  2. *Multi-Model Architecture (FSM + DSM):* Separates fresh signals (Fresh Signal Model for immediate shallow engagement like Short-form Minutes Play [SMP]) from sparse delayed signals (Delayed Signal Models for chat, follow, and spend) to keep serving features fresh [2, 10, 25–26].
  3. *Viewer Segment Targeting (VST):* Applies inference-time segment-conditioned objective weighting tailored to Early (E) vs. Dedicated (D) viewers without maintaining separate segment-specific models [2, 10, 27–28].
  4. *MMoE Consolidation:* Consolidates independent DSMs into a Multi-gate Mixture-of-Experts (MMoE) architecture (4 expert networks), reducing delayed-target modeling parameters by **41.9%** while serving live recommendations at **<110ms p99 latency** [4-6].

---

#### **(3) Proposed Method or Architecture in Detail**

##### **Architectural Components**
* **Fresh Signal Model (FSM):** Predicts shallow, immediate engagement (Short-form Minutes Play, SMP) using immediate labels, ensuring serving-time features remain up-to-date [25–26].
* **Delayed Window (DW) & Delayed Signal Models (DSM):** For sparse actions \\(a \in \{\text{chat}, \text{follow}, \text{spend}\}\\), aggregates user responses over a \\(\Delta t = 14\\)-day window following exposure timestamp \\(t\\) [22–23]:
  \\[y_{v_i, c_j}^{\text{delayed}} = \mathbb{I}\left[\left|DW_{v_i, c_j}(t, \Delta t)\right| > 0\right]\\]
  Long-form Minutes Play (LMP) uses immediate labels but is grouped with delayed targets due to shared deep-engagement characteristics [7].
* **MMoE Task Grouping:** Replaces independent DSMs with an MMoE model (\\(K=4\\) expert networks) that jointly predicts \\(\{LMP, \text{chat}, \text{follow}, \text{spend}\}\\) [29–31]. The MMoE uses 3 shared-bottom layers (size 1000), 4 expert networks (2 layers: 512, 256), task-specific gating networks (4 layers: 128 each), and 1-layer task towers (size 64) [8].
* **Viewer Segment Targeting (VST):** Categorizes viewers at inference time into **Early (E)** (account age \\(\le M\\) days or visit/chat days \\(\le N\\)) vs. **Dedicated (D)** [9]. Applies segment-conditioned weights \\(w_{a,s}\\) to assemble the final ranking score [28, 31–32]:
  \\[F_{\text{FSM-MMoE-VST}}(x_{v_i, c_j}, s) = w_{\text{smp}, s} \cdot p_{\text{smp}}^{\text{FSM}}(x_{v_i, c_j}) + \sum_{a} w_{a,s} \cdot p_a^{\text{MMoE}}(x_{v_i, c_j})\\]
  E viewers prioritize immediate engagement (SMP), whereas D viewers balance monetization (spend) and community engagement [38–39].

##### **Credit Assignment Mechanics**
* **Does NOT perform multi-touch attribution or per-touchpoint sequence credit assignment.**
* The framework uses a **14-day delayed window binary indicator** (\\(y^{\text{delayed}} \in \{0, 1\}\\)) to construct training labels for multi-task candidate ranking models [22–23]. It does not output or publish a per-touchpoint attribution credit table.

---

#### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets & Offline Setup:**
  * *Training Set:* 7 days of historical impression logs from 6 million viewers [35–36].
  * *Evaluation Set:* 1 day of impression data from 1 million viewers, evaluated against a **35-day forward window** for ground-truth delayed labels [10].
* **Production Deployment:** Fully deployed in live production at **Twitch** on the primary live-stream channel recommendation surface and Twitch mobile live feed, serving millions of daily active viewers at **<110ms p99 latency** [4, 5, 11].
* **Comparison Baselines:**
  * **YouTube DNN / Single-Objective Point-wise Model:** Previous production baseline predicting SMP with a monetization heuristic feature (Monetization Attach Ratio, MAR) [12, 13].
  * **Single Unified Multi-Task Models:** Single Shared-Bottom, Single MMoE, and Single CGC (PLE core extraction module) jointly modeling all 5 targets (including SMP) in a single unified architecture [14, 15].
  * **Alternative FSM + Multi-Task Backbones:** FSM + Shared-Bottom + VST, FSM + CGC + VST [14, 15].

---

#### **(5) Key Quantitative Results with Numbers**

* **Live Production Online A/B Test Results (14-Day Tests, Table 2):**
  * **Exp 1 (Multi-Model with 14-Day Delayed Window vs. Baseline):**
    * *Daily Active Viewers (DAV):* **+0.09%** overall (\\(p < 0.01\\); **+0.10%** E viewers, **+0.08%** D viewers) [4, 5, 16, 17].
    * *Long Minutes Play (LMP):* **+0.16%** overall (\\(p < 0.01\\); **+0.17%** D viewers) [16, 17].
    * *Capped ARPU (Revenue):* **+0.56%** for Dedicated (D) viewers (\\(p < 0.05\\)) [4, 5, 16, 17].
  * **Exp 2 (Viewer Segment Targeting VST vs. Exp 1 Winner):**
    * *Early (E) Viewer Engagement:* **+0.15%** DAV (\\(p < 0.05\\)), **+0.25%** LMP (\\(p < 0.01\\)) [2, 10, 49–50].
  * **Exp 3 (MMoE Consolidation vs. Independent DSMs):**
    * *New Follows:* **+0.27%** overall (\\(p < 0.01\\); **+0.44%** D viewers) [4, 5, 17, 18].
    * *Overall DAV & LMP:* **+0.08%** DAV (\\(p < 0.05\\)), **+0.10%** LMP (\\(p < 0.05\\)) [5, 17, 18].
  * **Mobile Live Feed Generalization:** **+1.12%** increase in positive user-channel interactions (clicks, follows, likes; \\(p < 0.001\\)) [4, 11].
  * **System Efficiency Gains:** Reduced delayed-target model parameters from 26.7M to 15.5M (**41.9% reduction**) while maintaining <110ms p99 latency [4-6].

* **Offline Benchmark Metrics (NDCG@6, Table 1):**
  * *FSM + MMoE + VST:* **Spend NDCG@6 = 0.0739** (+1.79% over YouTube DNN baseline 0.0726), **LMP NDCG@6 = 0.2462** (+0.12% over baseline 0.2459) [15, 19].
  * *Single Unified MTL Failure:* Single MMoE (**LMP = 0.2347**, -4.55% drop), Single Shared-Bottom (**LMP = 0.2355**, -4.23% drop), Single CGC (**LMP = 0.2355**, -4.23% drop) [14, 15].

---

#### **(6) Limitations, Failure Modes, or Negative Results**

1. **Failure of Single Unified Multi-Task Models:** Jointly modeling shallow engagement (SMP) alongside deeper/delayed targets in a single unified architecture (Single MMoE, Single Shared-Bottom, Single CGC) severely degraded LMP performance (**-4.2% to -4.6%**) because the extremely dense SMP signal dominated gradient updates [43, 54, 56–57].
2. **Signal Staleness in Extended Windows:** Extending the delayed window beyond 14 days (e.g., 21–35 days) yielded diminishing returns for spend and caused engagement metrics (LMP NDCG) to decline due to attributing actions to stale, unassociated impressions [20-22].
3. **Failure of Training-Time Loss Weighting:** Applying higher loss weights to Early (E) viewer samples during model training failed to improve performance and increased training complexity; segment bias was only successfully resolved via inference-time weight scalarization [22, 23].
4. **Manual Segment Weight Configuration:** Segment-conditioned weights (\\(w_{a,s}\\)) were selected manually via offline grid search and A/B guardrails rather than learned dynamically via online adaptive scalarization [22, 23].

---

#### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Ma et al. (2018) [Ref 20 / MMoE]:** *Modeling task relationships in multi-task learning with multi-gate mixture-of-experts* (ACM SIGKDD '18) [9, 24-26].
2. **Tang et al. (2020) [Ref 28 / PLE & CGC]:** *Progressive layered extraction (ple): A novel multi-task learning (mtl) model for personalized recommendations* (ACM RecSys '20) [8, 15, 24, 25, 27, 28].
3. **Chapelle (2014) [Ref 5 / Delayed Feedback]:** *Modeling delayed feedback in display advertising* (ACM SIGKDD '14) [29, 30].
4. **Covington, Adams, & Sargin (2016) [Ref 8 / YouTube DNN]:** *Deep neural networks for youtube recommendations* (ACM RecSys '16) [15, 31, 32].
5. **Zhao et al. (2019) [Ref 37 / YouTube Multitask RecSys]:** *Recommending what video to watch next: a multitask ranking system* (ACM RecSys '19) [8, 24, 33, 34].
6. **Ma et al. (2018) [Ref 21 / ESMM]:** *Entire space multi-task model: An effective approach for estimating post-click conversion rate* (ACM SIGIR '18) [8, 24, 26].
7. **Xi et al. (2021) [Ref 32 / AITM]:** *Modeling the sequential dependence among audience multi-step conversions with multi-task learning in targeted display advertising* (ACM SIGKDD '13) [8, 24, 35].

---

### **Section 2: Dating App Retention Attribution Project Evaluation**

#### **(A) Q1 or Q2 or Both or Neither?**
* **Neither.**
* **Explanation:**
  * **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** While published in RecSys 2026 and deployed in live production at Twitch, it presents a **multi-objective live-streaming candidate channel ranking system** (FSM + MMoE + VST with 14-day delayed target aggregation), not an industry multi-touch attribution (MTA) measurement system [2, 10, 25–28].
  * **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** It predicts candidate channel engagement/retention probabilities for live-stream ranking, rather than attributing overall user retention or active days back to individual interaction touchpoints (swipes, matches, messages) across historical logs [17, 21–23].

---

#### **(B) Q2 Class**
* **Classification:** **NOT**
* **Justification:** It is a multi-objective multi-task ranking policy framework (FSM + MMoE with 14-day delayed target aggregation and inference-time segment scalarization) [2, 10, 25–28]. It does **not** produce or publish a per-exposure retention credit table.

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction sequence attribution credit table.**
* **Target Outcome:** Multi-target probabilities for channel ranking—Short-form Minutes Play (SMP), Long-form Minutes Play (LMP), Chatting, Following, and Spending—evaluated over immediate and 14-day delayed observation windows [18, 22–23].

---

#### **(D) How This Replaces or Improves Last-Touch N7 → Latest Swipes**
* **How it Improves/Informs Ranking Strategy:** It does **not** provide a post-hoc attribution model to replace last-touch N7 [22–23]. However, it offers two key architectural strategies for balancing immediate interactions with delayed retention/conversion goals in ranking models:
  1. *Fresh vs. Delayed Signal Separation:* Shallow immediate actions (swipes) should be handled by a Fresh Signal Model (FSM) to keep serving features up-to-date, while sparse, delayed deeper actions (matches, deep conversations, retention) are aggregated over a delayed window (e.g., 14 days) and modeled jointly via an MMoE [25–26, 29–31]. This prevents dense immediate signals from overpowering sparse retention/monetization signals in gradient updates [43, 56–57].
  2. *Viewer Segment Targeting (VST):* Applies inference-time segment-conditioned weights (\\(w_{a,s}\\)) based on user lifecycle stage—e.g., prioritizing immediate profile swiping engagement for Early (E) users to encourage habituation, while up-weighting deep messaging and match retention for Dedicated (D) users [27–28, 38–39].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  * *Fresh Signal Model (FSM):* Predicts immediate shallow engagement—e.g., Right-Swipes or Profile Clicks [18, 25–26].
  * *Delayed Signal Models (MMoE):* Predicts sparse, delayed actions over a 14-day window following profile exposure—e.g., Mutual Matches, 14-day Messaging Continuity, and Retained Active Days [18, 22–23, 29–31].
  * *Segment Targeting (VST):* Early users (new account / low swipe activity) are ranked prioritizing immediate swipe matchability; Dedicated users are ranked prioritizing long-term chat depth and match retention [20, 27–28, 38–39].

---

#### **(E) Selection-Bias & Confounding Handling**
1. *Viewer Segment Bias Handling:* Dedicated (D) users contribute 4x more training data than Early (E) users [2, 3]. To prevent ranking models from over-indexing on established user behavior, VST applies segment-conditioned objective scalarization (\\(w_{a,s}\\)) at inference time without maintaining separate models [27–28, 38–39].
2. *Delayed Feedback Labeling Noise:* Aggregates sparse user actions over a 14-day window (\\(DW_{v_i, c_j}\\)) following exposure, converting unobserved/delayed responses into positive binary target indicators (\\(y^{\text{delayed}} \in \{0, 1\}\\)) to avoid mislabeling delayed actions as negative [22–23, 35].
3. *Forward Evaluation Window:* Evaluates offline models against a 35-day forward observation window to account for long observation delays [10].

---

#### **(F) Deployed or Production Dataset Evidence**
* **Production Deployment:** Fully deployed live in production at **Twitch** on the primary live-stream channel recommendation surface and Twitch mobile live feed, serving millions of daily active viewers at **<110ms p99 latency** [4, 5, 11].
* **Quoted Numbers from Source:**
  * *Training/Evaluation Dataset Scale:* Trained on 7 days of historical impression data from **6 million viewers**; evaluated on 1 day of historical data from **1 million viewers** with a **35-day forward window** [35–36].
  * *Action Density Progression:* Short watch rates were ~**2.5x lower** than CTR, longer watch rates **3.4x lower**, chat rates ~**20x lower**, and follow rates nearly **90x lower** than CTR [36]. D viewers contribute roughly **4x more training samples** than E viewers [2, 3].
  * *Live Online A/B Test Results (Table 2):*
    * *Exp 1 (Multi-Model with 14-day Delayed Window):* Daily Active Viewers (DAV) **+0.09%** overall (\\(p < 0.01\\); **+0.10%** E viewers, **+0.08%** D viewers); Long Minutes Play (LMP) **+0.16%** overall (\\(p < 0.01\\); **+0.17%** D viewers); Capped ARPU **+0.56%** for Dedicated (D) viewers (\\(p < 0.05\\)) [4, 5, 16, 17].
    * *Exp 2 (Viewer Segment Targeting VST):* Early (E) viewer engagement **+0.15%** DAV (\\(p < 0.05\\)), **+0.25%** LMP (\\(p < 0.01\\)) [2, 10, 49–50].
    * *Exp 3 (MMoE Consolidation):* New Follows **+0.27%** overall (\\(p < 0.01\\); **+0.44%** D viewers); overall DAV **+0.08%** (\\(p < 0.05\\)), overall LMP **+0.10%** (\\(p < 0.05\\)) [5, 17, 18].
    * *Mobile Live Feed Generalization:* **+1.12%** increase in positive user-channel interactions (clicks, follows, likes; \\(p < 0.001\\)) [4, 11].
    * *System Efficiency:* Reduced delayed-target model parameters from 26.7M to 15.5M (**41.9% reduction**) while serving at **<110ms p99 latency** [4-6].
  * *Offline Benchmark Metrics (NDCG@6, Table 1):*
    * *FSM + MMoE + VST:* **Spend NDCG@6 = 0.0739** (+1.79% over YouTube DNN baseline 0.0726), **LMP NDCG@6 = 0.2462** (+0.12% over baseline 0.2459) [15, 19].
    * *Single Unified MTL Degradation:* Single MMoE (**LMP = 0.2347**, -4.55% drop), Single Shared-Bottom (**LMP = 0.2355**, -4.23% drop), Single CGC (**LMP = 0.2355**, -4.23% drop) [14, 15].

---

💡 *Would you like to explore how Twitch's fresh/delayed signal separation or segment-aware targeting could be adapted to balance immediate profile swipes with delayed conversation/match retention in your dating app?*

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
**Priority:** see queue.md `G37`
