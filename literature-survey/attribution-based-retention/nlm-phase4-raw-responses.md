Date: 2026-04-14  
Notebook: `6a3b8a8e-6f2f-4efe-99eb-283983fc95d9`

# NotebookLM Phase 4-A — Raw `notebook_query` responses

**Settings (all queries):** `notebook_id=6a3b8a8e-6f2f-4efe-99eb-283983fc95d9`, **no** `source_ids` filter (full notebook), **no** `conversation_id` threading on the re-materialization pass.

**API outcome:** Each query body below was taken from a successful NotebookLM MCP response (`status: success`) archived under `~/.cursor/projects/Users-fox-claude/agent-tools/`:

| Query | Archived source file |
|------:|------------------------|
| 1 | `9f358411-0a71-469f-bddc-840bde7c6b06.txt` |
| 2 | `bc3cf765-6679-4c17-a368-c334b1a454f9.txt` |
| 3 | `q3_phase4_open.json` |
| 4 | `b22186d8-952b-4661-bc86-99563054690c.txt` |
| 5 | `67175588-8991-47e3-b5d8-d925f2a690c1.txt` |
| 6 | `b5884988-36d5-4b8f-ad7c-cee96ca3bb35.txt` |
| 7 | `d9657904-d862-462c-a037-8cb5293d8bd4.txt` |


---

## Query 1 — Dominant methodological approaches + representative papers

**Prompt (verbatim):**

> What are the dominant methodological approaches across all papers in this notebook? For each approach, summarize it and list representative papers.

**NLM answer:**

The dominant methodological approaches across the papers in this notebook span the evolution from simple heuristics to advanced causal machine learning, aimed at solving Multi-Touch Attribution (MTA), Conversion Rate (CVR) prediction, and Marketing Mix Modeling (MMM). 

Here is a summary of the dominant methodological approaches and their representative papers:

**1. Traditional Data-Driven and Probabilistic Models**
*   **Summary:** As an upgrade to rigid rule-based heuristics (like last-click or first-click attribution) [1, 2], these methods use statistical models to learn channel contributions directly from historical data. Prominent techniques include bagged logistic regression to model conversion probabilities based on ad counts, Markov chains to model transition probabilities between channels, and Survival Analysis (additive hazard models) to capture the time-decaying effects of ad exposures [3-6].
*   **Representative Papers:** 
    *   *Data-driven multi-touch attribution models* (Shao and Li, 2011) – The foundational bagged logistic regression approach [3, 4].
    *   *Multi-touch attribution in online advertising with survival theory* (Zhang et al., 2014) – Introduces additive hazard models [6, 7].
    *   *A probabilistic multi-touch attribution model for online advertising* (Ji et al., 2016) [6, 8].

**2. Deep Learning and Sequential Modeling (Attention Mechanisms)**
*   **Summary:** Recognizing that customer journeys are complex, time-dependent sequences of interactions, these methods employ deep neural networks—specifically Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) networks—to model sequential behavior [9-11]. They heavily rely on **Attention and Dual-Attention Mechanisms** to dynamically weight the importance of specific touchpoints (e.g., differentiating between ad views and clicks) within a user's unique path to purchase [12-14].
*   **Representative Papers:**
    *   *Deep Neural Net with Attention for Multi-channel Multi-touch Attribution (DNAMTA)* (Li et al., 2018) [15-17].
    *   *Learning Multi-touch Conversion Attribution with Dual-attention Mechanisms for Online Advertising (DARNN)* (Ren et al., 2018) [12, 17].
    *   *Interpretable Deep Learning Model for Online Multi-touch Attribution (DeepMTA)* (Yang et al., 2020) [18, 19].

**3. Causal Inference and Counterfactual Prediction**
*   **Summary:** These approaches treat attribution as estimating the true incremental (causal) lift of a marketing intervention, rather than just correlation. They focus on eliminating confounding variables or selection bias (e.g., highly active users naturally receiving more ads) using techniques like inverse propensity weighting (IPTW), double/debiased machine learning (DML), and **Causal Recurrent Networks (CRNs)**. By learning treatment-invariant representations or utilizing gradient reversal layers, these models simulate unbiased counterfactual predictions [20-24].
*   **Representative Papers:**
    *   *Causally Motivated Attribution for Online Advertising* (Dalessandro et al., 2012) – Early framing of attribution as causal estimation [19, 25].
    *   *CAMTA: Causal Attention Model for Multi-touch Attribution* (Kumar et al., 2020) [26, 27].
    *   *CausalMTA: Eliminating the User Confounding Bias for Causal Multi-touch Attribution* (Yao et al., 2022) [28, 29].
    *   *DCRMTA: Unbiased Causal Representation for Multi-touch Attribution* (Tang et al., 2024) [23, 30].

**4. Cooperative Game Theory (Shapley Values)**
*   **Summary:** This framework treats attribution as a cooperative game where marketing channels are the "players" working together to produce a conversion "payoff." Using the Shapley value (and continuous extensions like the Aumann-Shapley method), these models calculate the fair marginal contribution of each channel to the final outcome by evaluating all possible combinations of channel interactions [19, 31-33]. 
*   **Representative Papers:**
    *   *A Non-parametric Approach to the Multi-channel Attribution Problem* (Yadagiri et al., 2015) [32, 34].
    *   *Shapley meets uniform: An axiomatic framework for attribution in online advertising* (Singal et al., 2019/2022) [19, 35].

**5. Multi-Task Learning (MTL) and Knowledge Distillation**
*   **Summary:** Frequently used for CVR prediction, MTL architectures jointly train on multiple related tasks (like Click-Through Rate [CTR] and CVR) to alleviate data sparsity and selection bias. They utilize hard or soft parameter sharing, Mixture-of-Experts (MoE), or distill knowledge across different attribution views (e.g., learning simultaneously from first-click, last-click, and MTA labels) [36-40].
*   **Representative Papers:**
    *   *Entire Space Multi-Task Model (ESMM)* (Ma et al., 2018) [39, 41].
    *   *Beyond a Single View: Multi-Attribution Learning Leads to Better Conversion Rate Prediction* (Chen and Chan et al., 2025) – Introduces the Multi-Attribution Learning (MAL) framework [42, 43].

**6. Top-Down Marketing Mix Modeling (MMM) & Geo-Experiments**
*   **Summary:** Used when user-level path data is unavailable (due to privacy restrictions like iOS 14/GDPR) or for macro-level budget allocation. These methods operate on aggregate time-series data using regression, Bayesian inference, and inferred causal graphs to measure saturation, carryover effects, and synergies across offline and online channels [44-47].
*   **Representative Papers:**
    *   *Learning Causal Structure for Marketing Mix Modeling (CausalMMM)* (Gong et al., 2024) [44, 48].
    *   *Amazon Ads Multi-Touch Attribution* (Lewis et al., 2025) – Combines Randomized Controlled Trials (RCTs) with ML attribution [45].
    *   Open-source frameworks like *Robyn* (Meta) and *Meridian* (Google) [46].

---

## Query 2 — Evaluation datasets / benchmarks + paper mapping

**Prompt (verbatim):**

> What are the most common evaluation datasets and benchmarks used across these papers? Which papers use which datasets?

**NLM answer:**

Based on the provided literature, the evaluation datasets and benchmarks span public real-world advertising logs, causal inference/uplift modeling benchmarks, and massive proprietary datasets from major tech platforms. 

Here are the most common datasets and the specific papers/models that utilize them:

### 1. Public Real-World Advertising Datasets

**Criteo Datasets**
Criteo has released several of the most heavily adopted public datasets in the field, including the Criteo Attribution Modeling dataset, Criteo Conversion Logs, Criteo Sponsored Search Conversion Log (CSSCL), and Criteo Uplift dataset. These contain millions of impressions, clicks, and conversion events [1-4].
*   **Used by:**
    *   **CAMTA** (Kumar et al., 2020): Uses the attribution dataset to validate its causal attention framework [5, 6].
    *   **CausalMTA** (Yao et al., 2022): Uses the attribution dataset to evaluate conversion prediction and data replay [7, 8].
    *   **DARNN** (Ren et al., 2018): Evaluates dual-attention recurrent neural networks on Criteo live traffic data [2].
    *   **DP Ad Conversion Measurement** (Delaney et al., 2024): Uses the CSSCL dataset to evaluate Differentially Private summary reports [4].
    *   **Numerous CVR Models:** A comprehensive survey notes it is a standard benchmark used by Chapelle (2014), Vasile et al. (2017), Yasui et al. (2020), Gu et al. (2021), and dozens of others [9, 10].

**Alibaba / Taobao / Ali-CCP Datasets**
Collected from Taobao's advertising traffic logs, these datasets (including the Alibaba Click and Conversion Prediction dataset) are foundational for evaluating multi-task learning models and multi-attribution frameworks [11-13].
*   **Used by:**
    *   **MAC Benchmark** (Wu et al., 2024): A newly introduced open-source dataset constructed from Taobao logs that uniquely provides conversion labels from four different attribution mechanisms (last-click, first-click, linear, DDA) [13, 14].
    *   **Multi-Attribution Learning (MAL)** (Chen et al., 2025): Uses Taobao display advertising logs to test joint learning across multiple attribution perspectives [11].
    *   **CausalMTA** (Yao et al., 2022): Uses a real-world dataset of mobile phone shops from Alibaba [15].
    *   **Multi-Task CVR Models:** Ali-CCP is extensively used by models like ESMM (Ma et al., 2018), PLE (Tang et al., 2020), and ESCM2 [12].

**iPinYou Dataset**
Released by a Chinese DSP company, this dataset contains over 64 million bid records and is a foundational benchmark for real-time bidding (RTB) and Click-Through Rate (CTR) estimation [16].
*   **Used by:**
    *   **Bid Landscape Forecasting & Bidding Strategies:** Extensively used to test optimal real-time bidding, Expected Utility models, and Generative Bid Shading [17, 18].
    *   **CVR Prediction:** Used by Shan et al. (2018) for combined regression and triplet-wise learning [19].

**Miaozhen Dataset**
An early but massive dataset from a Chinese marketing tech company containing over 1.2 billion ad logs and 380 million cookies from 2013 [20, 21].
*   **Used by:**
    *   **DARNN** (Ren et al., 2018) [20].
    *   **AMTA** (Ji & Wang, 2017) [22].
    *   **AdditiveHazard** (Zhang et al., 2014) [21, 23].

**Tencent Advertising Datasets**
Datasets such as the Tencent Advertising Algorithm Competition 2017 dataset and the Tenc_UnionAds dataset provide industrial-scale logs for multi-task learning and CVR prediction [24, 25].
*   **Used by:** Li et al. (2021b), Guo et al. (2022), and AECM (Zhang et al., 2024b) [24, 25].

### 2. Causal Inference and Uplift Modeling Benchmarks

Because true causal ground truth is rarely known in real-world advertising data, researchers frequently rely on semi-synthetic datasets from the causal inference community [26, 27].

*   **IHDP (Infant Health and Development Program):** A semi-synthetic dataset based on a randomized experiment, used to evaluate Conditional Average Treatment Effect (CATE) algorithms. It is used by **Dragonnet** (Shi et al., 2019) [28], **Counterfactual Regression (CFR)** (Johansson et al., 2016), and evaluated in comprehensive causal surveys [29, 30].
*   **ACIC 2018 (Atlantic Causal Inference Conference):** A large collection of semi-synthetic datasets used to benchmark models like **Dragonnet** [28].
*   **Jobs / LaLonde (1986) Dataset:** A classic benchmark combining a randomized job training study with observational data, used to evaluate models like **CFR** [31].
*   **Hillstrom’s Email Advertisement Dataset:** A randomized experiment evaluating the uplift of sending merchandise emails, used widely in uplift modeling surveys to compare Qini and uplift curves [32, 33].

### 3. Proprietary Platform Datasets and Simulators

Due to the extreme sensitivity of user journey data, many state-of-the-art models are validated strictly on proprietary logs or Randomized Controlled Trials (RCTs) run internally by major tech platforms [34, 35].

*   **Meta / Facebook:** The **Predicted Incrementality by Experimentation (PIE)** framework was trained and evaluated on a proprietary dataset of 2,226 large-scale Meta ad experiments (RCTs) to scale causal measurement to non-experimental campaigns [34, 36].
*   **Amazon Ads:** Amazon validates its internal **Multi-Touch Attribution (MTA)** system using hundreds of thousands of proprietary RCTs combined with causal machine learning models [35, 37].
*   **JD.com:** Uses internal platform data for training a **bi-directional RNN response model** for attribution [38] and evaluating audiences via **contextual bandit experiments** [39].
*   **eBay:** Uses streaming customer journey logs to evaluate the **DeepMTA** model [40].
*   **Turn Inc.:** Validated multi-touch attribution budget allocation using tens of terabytes of internal user profile data [41, 42].
*   **Simulators (DASS):** The Digital Advertising System Simulation (DASS), originally developed by Google, is frequently modified to simulate user browsing and inject advertising events to benchmark data-driven models with a known ground truth [43, 44].

---

## Query 3 — Open problems / research gaps

**Prompt (verbatim):**

> What open problems or research gaps are identified most frequently across these papers?

**NLM answer:**

**Integration with Budget Allocation, Bidding, and Reinforcement Learning**
Across the literature, researchers frequently highlight that measuring attribution is only a partial solution; a major open problem is directly integrating multi-touch attribution (MTA) and causal outputs into optimal budget allocation and real-time bidding (RTB) systems [1-3]. There is a strong need to extend these models into reinforcement learning and online learning frameworks, capturing how attribution evolves across repeated auctions [4, 5]. Furthermore, studying multi-agent bidding interactions to understand the equilibrium responses of strategic advertisers remains an unresolved challenge [5]. 

**Privacy Constraints, Obfuscated Data, and Differential Privacy**
Due to strict privacy regulations (e.g., GDPR, CCPA) and the deprecation of third-party cookies or mobile identifiers, models must increasingly operate without deterministic, user-level path data [6]. Specific gaps include:
*   Developing algorithms that optimize differential privacy bounds (such as contribution budgeting in the Attribution Reporting API) purely from privacy-preserving outputs, without relying on non-contribution bounded or noiseless historical data [7, 8].
*   Leveraging alternative signals like event-level reports to optimize summary reports [9].
*   Extending learning from label proportions (or attribution sets) to multi-touch settings and jointly learning both the prior distribution and the conversion model directly from streaming data [10].

**Unobserved Confounding, Spillovers, and Complex Causal Dynamics**
Effectively handling unobserved confounders and the complex realities of marketing remains a significant barrier. 
*   Researchers emphasize the need to explicitly incorporate spillover and carryover mechanisms to better capture the interconnected nature of marketing activities across channels [11].
*   For marketing mix modeling (MMM), open problems include developing dynamic models with long-term decomposition to capture brand decay over time, as well as modeling interactions, synergy effects, and multiplicative models to detect when multiple variables work together [12].
*   In switchback experiments, handling scenarios where the carryover effect is extremely large relative to the experimental time horizon remains an open challenge, as current unrestrictive models incur variances that prohibit meaningful inference [13].

**Uncertainty Quantification, Overlap, and Confidence Intervals**
Estimating Conditional Average Treatment Effects (CATE) accurately requires addressing extremely weak signals and overlap violations. A recurring gap is the need for systematic methods to produce accurate variance estimates and robust confidence intervals for individual treatment effects, especially in challenging circumstances like small sample sizes or a large number of covariates [14, 15]. Furthermore, violations of the overlap condition in observational data can lead to highly unreliable and invalid inferences, highlighting a need for better handling of such scenarios [16].

**Balancing Interpretability with Black-Box Accuracy**
While deep learning and ensemble models provide high accuracy for CATE and conversion rate (CVR) prediction, they often lack the interpretability required by business stakeholders. A major future direction involves finding a balance between the interpretability, ease of use, and accuracy of CATE estimation algorithms [17]. Proposed solutions to explore include constructing transparent tree-based models on top of black-box CATE estimators [18], or integrating reinforcement learning with Shapley value decomposition methods to achieve interpretable predictions [19]. 

**Advanced Architectures: LLMs and Multimodal Data**
As digital advertising evolves, traditional structured features are no longer sufficient. Researchers point to a significant gap in utilizing multimodal data (such as textual and visual elements in micro-video sharing platforms) for CVR prediction [20]. Emerging directions include integrating generative recommendation architectures and leveraging the advanced reasoning and semantic extraction capabilities of Large Language Models (LLMs) to better capture user conversion intent [21-23].

**Strategic Manipulation and Ecosystem Incentives**
Traditional attribution assumes that ad platforms and networks report data truthfully. A growing area of future work involves modeling repeated games with externalities, investigating scenarios where platforms might strategically misreport data or harm peers to manipulate learned priors, steal credit, or dynamically interact with automated bidding budgets in a comprehensive ecosystem [3].

---

## Query 4 — Foundational papers

**Prompt (verbatim):**

> Which papers appear to be the most foundational — cited by or built upon by many others in this notebook? List them with brief explanations.

**NLM answer:**

**Shao and Li (2011) – "Data-driven multi-touch attribution models"**
This paper is consistently cited as the **foundational work for data-driven multi-touch attribution (MTA)**. It introduced a bagged logistic regression methodology to allocate conversion credit based on historical data, establishing the bedrock for moving the industry beyond subjective, heuristic rules like "last-click" or "first-click" [1-12].

**Dalessandro et al. (2012) – "Causally motivated attribution for online advertising"**
This work is foundational for **framing attribution as a causal estimation problem**. It pioneered the application of cooperative game theory to digital marketing by using the Shapley value to calculate the additive marginal lift of each advertisement, ensuring a fair and causally-motivated distribution of conversion credit among channels [9, 13-26].

**Shapley (1953) – "A value for n-person games"**
While originally a classical mathematics and economics paper, this work serves as the **theoretical bedrock for game-theoretic attribution models**. It is cited extensively for defining the Shapley value, which mathematically guarantees a fair allocation of a total "payoff" (a conversion) among a coalition of "players" (marketing touchpoints) based on their marginal contributions [1, 3, 6, 7, 27-34].

**Xu et al. (2014) – "Path to purchase: A mutually exciting point process model..."**
This paper is the foundational text for **temporal point process modeling in digital attribution**. It was the first to treat ad clicks and purchases as dependent stochastic events in continuous time, capturing the dynamic, "mutually exciting" effects of different advertising channels on the user's path to purchase [35-43].

**Zhang et al. (2014) – "Multi-touch attribution in online advertising with survival theory"**
This paper is heavily cited for introducing **survival analysis and additive hazard models** to the MTA problem. It provided a principled way to model the temporal influence of an advertising channel, specifically addressing the fact that the effect of an ad exposure naturally fades over time [18, 39, 44-51].

**Anderl et al. (2014/2016) – "Mapping the customer journey..."**
This work is frequently referenced as the benchmark for **graph-based and Markov Chain attribution models**. It models the customer journey as a sequence of transitions between channels, providing a computationally attractive method for evaluating channel influence based on transition probabilities [36, 52-61].

**Rosenbaum and Rubin (1983) – "The central role of the propensity score in observational studies for causal effects"**
These foundational statistics papers established the **potential outcomes framework and propensity score matching**. Though not originally about digital advertising, they are widely cited as the theoretical bedrock for models attempting to eliminate user selection bias and unobserved confounding in causal marketing attribution and uplift modeling [62-69].

---

## Query 5 — Baseline map

**Prompt (verbatim):**

> Is any paper's method used as a direct baseline by other papers in this notebook? Map method name → list of papers that use it as a baseline.

**NLM answer:**

Based on the provided sources, the development of new models in this field heavily relies on benchmarking against preceding state-of-the-art methods. Below is a mapping of methods proposed in these papers and the subsequent papers in the notebook that use them as direct comparison baselines.

### 1. Multi-Touch Attribution (MTA) Models

**Data-Driven MTA / Logistic Regression (Shao and Li, 2011)**
*   *Causally Motivated Attribution* (Dalessandro et al., 2012) [1, 2]
*   *Deep Neural Net with Attention (DNAMTA)* (Li et al., 2018) [3]
*   *Learning Multi-Touch Conversion Attribution with Dual-Attention (DARNN)* (Ren et al., 2018) [4, 5]
*   *Causal Attention Model for Multi-touch Attribution (CAMTA)* (Kumar et al., 2020) [6]
*   *CausalMTA* (Yao et al., 2022) [7-9]
*   *DCRMTA* (Tang et al., 2024) [10, 11]
*   *Att-TCN / Stage-TCN* (Agrawal et al., 2022; Xie et al., 2022) [3, 6]
*   *Graphical MTA* (2023) [12]

**Simple Probabilistic Model (SP) (Shao and Li, 2011)**
*   *Additional Multi-Touch Attribution (AMTA)* (Ji and Wang, 2017) [13, 14]
*   *DARNN* (Ren et al., 2018) [4, 5]
*   *CausalMTA* (Yao et al., 2022) [7-9]
*   *DCRMTA* (Tang et al., 2024) [10]

**Additive Hazard (AH) (Zhang et al., 2014)**
*   *Additional Multi-Touch Attribution (AMTA)* (Ji and Wang, 2017) [13, 14]
*   *DARNN* (Ren et al., 2018) [4, 5]
*   *CAMTA* (Kumar et al., 2020) [6]
*   *CausalMTA* (Yao et al., 2022) [7-9]

**Probabilistic Multi-Touch Attribution (PMTA) (Ji et al., 2016)**
*   *Additional Multi-Touch Attribution (AMTA)* (Ji and Wang, 2017) [13, 14]

**Additional Multi-Touch Attribution (AMTA) (Ji and Wang, 2017)**
*   *DARNN* (Ren et al., 2018) [5, 15]
*   *CAMTA* (Kumar et al., 2020) [6]
*   *Att-TCN / Stage-TCN* (Agrawal et al., 2022; Xie et al., 2022) [3, 6]

**Deep Neural Net with Attention (DNAMTA) (Li et al., 2018 / Arava et al., 2018)**
*   *CAMTA* (Kumar et al., 2020) [6]
*   *CausalMTA* (Yao et al., 2022) [7-9]
*   *DCRMTA* (Tang et al., 2024) [10, 11]
*   *Graphical MTA* (2023) [12]
*   *Deep Journey Hierarchical Attention Networks (DJHAN)* (Ban et al., 2024b) [16]

**Dual-Attention Recurrent Neural Network (DARNN) (Ren et al., 2018)**
*   *CAMTA* (Kumar et al., 2020) [6]
*   *CausalMTA* (Yao et al., 2022) [7-9]

**Interpretable Deep Learning Model for Online MTA (DeepMTA) (Yang et al., 2020)**
*   *CausalMTA* (Yao et al., 2022) [7-9]

**Causal Attention Model for Multi-touch Attribution (CAMTA) (Kumar et al., 2020)**
*   *CausalMTA* (Yao et al., 2022) [7, 9, 17]

**CausalMTA (Yao et al., 2022)**
*   *DCRMTA* (Tang et al., 2024) [10, 11]

### 2. Multi-Task Learning (MTL) & CVR Prediction Models

**Entire Space Multi-Task Model (ESMM) (Ma et al., 2018)**
*(Extensively used as a baseline in the CVR prediction survey [18-33])*
*   *ESCM2* (Wang et al., 2022) 
*   *UKD* (Xu et al., 2022) 
*   *TAML* (Liu et al., 2023b) 
*   *DCMT* (Zhu et al., 2023) 
*   *NISE* (Huang et al., 2024) 
*   *ChorusCVR* (Cheng et al., 2025) 
*   *EVI* (Fei et al., 2025) 

**Multi-gate Mixture-of-Experts (MMoE) (Ma et al., 2018)**
*   *Progressive Layered Extraction (PLE)* (Tang et al., 2020) [21]
*   *AutoFuse* (Jin et al., 2023) [34]
*   *TAML* (Liu et al., 2023b) [35]
*   *NISE* (Huang et al., 2024) [36]
*   *MAC Benchmark / MoAE* (Chen et al., 2025) [37-39]

**Progressive Layered Extraction (PLE) (Tang et al., 2020)**
*   *TAML* (Liu et al., 2023b) [35]
*   *MCAC* (Guo et al., 2024) [40]
*   *MAC Benchmark / MoAE* (Chen et al., 2025) [37, 39]

**NATAL (Chen et al., 202X)**
*   *MAC Benchmark / MoAE* (Chen et al., 2025) [37, 39]

### 3. Causal Inference and Heterogeneous Treatment Effects

**TARNet (Shalit et al., 2017)**
*   *Dragonnet* (Shi et al., 2019) [41, 42]

**Counterfactual Regression (CFR) (Johansson et al., 2016)**
*   *Dragonnet* (Shi et al., 2019) [43]

**Causal Forests (Wager & Athey, 2018)**
*   *X-learner* (Künzel et al., 2019) [44, 45]

**Meta-Learners (S-learner, T-learner, X-learner) (Künzel et al., 2019)**
*   *Quasi-oracle estimation of heterogeneous treatment effects (R-learner)* (Nie & Wager, 2020) [46]

**Augmented Synthetic Control Method (ASC)**
*   *Panel-Aware Double Machine Learning* (2025) [47]

### 4. Mechanism Design & Game Theory

**Last-Click Mechanism (LCM)**
*   *Peer-Validated Mechanism (PVM)* (Zhang et al., 2025) [48-50]

---

## Query 6 — Project Context (continuous labels / per-touch credit)

**Prompt (verbatim):**

> Across all sources in this notebook, which attribution or incrementality methods can produce per-touchpoint fractional credit suitable as supervised training labels when the conversion is a continuous engagement outcome (e.g., user-days-active) rather than a single binary purchase, and what caveats do the sources raise about using such scores as labels?

**NLM answer:**

**Continuous-Time Causal Modeling with "Ad Stock"** natively supports continuous, rate-based outcomes while directly generating fractional credits for each interaction. Rather than treating interactions as discrete static events, this approach translates touchpoints into a continuous "ad stock" that accumulates and decays over time `[1, 2]`. Because the model evaluates the outcome as a continuous expected rate, it natively supports ongoing metrics like user-days-active `[1]`. It produces a specific "incrementality share" for each touchpoint, calculating fractional credit as the ratio of an individual interaction's expected causal effect to the expected total outcome at that specific time `[3]`.

**Time-to-Event and Temporal Point Processes** treat engagement as an instantaneous rate or intensity function, making them perfectly suited for ongoing, continuous outcomes `[4]`. 
*   **TEDDA (Time to Event Data Driven Attribution)** models outcomes as occurrences in an inhomogeneous Poisson process where the intensity function varies based on prior touches `[4, 5]`. It generates per-interaction fractional credit via a "backwards elimination" algorithm, iteratively removing the last interaction in a path to measure the precise difference in the continuous conversion intensity `[6-8]`.
*   **Graphical Point Processes** model streams of user interactions as multivariate temporal point processes to capture dynamic inter-dependencies and exciting effects `[9, 10]`. They calculate fractional path-level attribution scores using the "direct removal effect" or the "total removal effect" (via score backpropagation), capturing the marginal lift of continuous engagement intensity while accounting for indirect synergistic effects between different touches `[11-13]`.
*   **AMTA (Additional Multi-Touch Attribution)** applies survival theory and additive hazard rates to reflect the time-decaying influence of multiple exposures, calculating the combined continuous effect of ads to generate a survival function `[14-16]`.

**Deep Sequence Models with Causal Attention** provide highly scalable per-interaction fractional credits while actively correcting for user selection bias. Architectures such as **DARNN**, **DNAMTA**, **CAMTA**, **CausalMTA**, **DCRMTA**, and **LiDDA** process the user's sequential journey through recurrent networks or Transformers `[17-22]`. Their attention mechanisms natively learn normalized weights for each specific interaction in the sequence `[23, 24]`. These attention weights sum to 1.0 and are directly interpreted as the fractional percentage contribution of that specific touchpoint `[25, 26]`. 
*   *Adaptation for your pipeline:* While often optimized for binary log-loss, their final classification layers can be readily swapped for standard continuous regression objectives. 
*   *Selection Bias Correction:* Crucially for your dating platform context, the causal variants in this group (**CAMTA**, **CausalMTA**, **DCRMTA**) actively use gradient reversal and adversarial learning to decorrelate a user's natural baseline activity from the treatment exposures. This residualizes out the confounding activity bias before generating the fractional attention weights `[27-31]`.

**Causal Meta-Learners Paired with Shapley Values** handle continuous outcomes robustly if you aggregate sequence interactions into feature counts. 
*   Causal frameworks like the **X-learner**, **TARNet/CFR**, or Double Machine Learning are explicitly designed to estimate the Conditional Average Treatment Effect (CATE) using any underlying continuous regression algorithm `[32-34]`. 
*   Once the unbiased continuous lift of a user's bundle of features is estimated (controlling for covariates), the predictions are passed through a **Shapley Value** algorithm to distribute fair, axiomatic fractional credit back to individual interactions based on their marginal contributions to the continuous lift `[35-38]`.

---

## Query 7 — Project Context (selection bias / heterogeneous touches)

**Prompt (verbatim):**

> Across all sources in this notebook, what approaches explicitly address user-level selection bias or confounding where more active users receive more touchpoints (heterogeneous interaction types on the same path), and how do they compare for dating-style retention measurement versus standard ad MTA?

**NLM answer:**

**Approaches Addressing User-Level Selection Bias and Confounding**

In observational data, highly active users naturally generate more touchpoints and have higher baseline conversion rates, leading to what the literature terms **"activity bias"** or "user-induced endogeneity" [1, 2]. To prevent models from falsely attributing a user's natural baseline activity to the causal effect of a touchpoint, the literature proposes several explicit debiasing approaches:

*   **Causal Recurrent Networks (CRNs) with Adversarial Learning:** This is the dominant deep-learning strategy for handling dynamic, time-varying confounding where a user's past activity dictates future touchpoints. 
    *   **Gradient Reversal Layers (GRL):** Models like **CAMTA** [3-5], **CausalMTA** [6-8], and **DCRMTA** [9, 10] use adversarial learning via a GRL. This forces the recurrent network to learn representations that successfully predict the outcome but are mathematically incapable of predicting the channel assignment, effectively isolating the true lift from the user's baseline trajectory [11, 12].
    *   **Decomposing Static vs. Dynamic Bias:** **CausalMTA** explicitly separates user preference into static attributes (e.g., demographics) and dynamic features (e.g., interaction history) [13, 14]. It applies Variational Recurrent Auto-encoders (VRAE) for journey reweighting to eliminate static bias, and a GRL to eliminate dynamic bias [7, 15, 16].
    *   **Causal Attention Modules:** **DCRMTA** builds on this by intervening in attention maps to generate counterfactual predictions, abandoning "stylized representations" that correlate with the user but are not causally related to the outcome [17-19].
*   **Representation Learning for Counterfactuals:** Models like **Counterfactual Regression (CFR)** and **TARNet** learn balanced representations by minimizing Integral Probability Metrics (like the Wasserstein distance) between the treated and control distributions, adjusting for the bias induced by treatment group imbalance [20-22]. 
*   **Inverse Propensity Weighting (IPW) and Journey Reweighting:** Methods apply propensity scores or density ratio estimation to reweight observed journeys, effectively up-weighting journeys that approximate random assignment and down-weighting those heavily driven by natural user preferences to emulate a randomized trial [1, 23-26].
*   **Observational Control (Selection on Observables):** Some RNN approaches (like the JD.com model) attempt to absorb activity bias by flooding the model with extensive user features and historical counts, shifting the mathematical "intercept" of the baseline prediction to convert "selection on unobservables" into "selection on observables" [27-29].
*   **Causal Meta-Learners:** Algorithms like the S-learner, T-learner, and X-learner combine existing supervised base-learners to estimate the Conditional Average Treatment Effect (CATE), natively modeling heterogeneous treatment effects across different user populations [30-34].

***

**Comparison: Dating-Style Retention vs. Standard Ad MTA**

Applying these causal debiasing methods to your dating platform (where touchpoints are heterogeneous organic interactions and the outcome is continuous days-active) requires translating them across several key dimensions:

**1. Nature of the Outcome (Continuous vs. Binary)**
*   **Standard Ad MTA:** Designed to predict a discrete binary conversion event (e.g., purchase = 1, no purchase = 0). Consequently, architectures like CAMTA, CausalMTA, and DCRMTA optimize for binary cross-entropy (BCE) or log-loss [35-38].
*   **Dating Retention:** Your conversion metric is continuous and non-negative (user-days-active) [39]. 
*   *Adaptation:* While the adversarial representation learning structures (like the GRL in CRNs) transfer perfectly to your sequence data, the final prediction heads must be swapped. You must replace BCE classification loss with a continuous regression objective (like Mean Squared Error). Alternatively, Meta-learners naturally accommodate continuous outcomes by wrapping standard regression base-learners [34, 40].

**2. Source of Confounding (Organic Activity vs. Algorithmic Targeting)**
*   **Standard Ad MTA:** Selection bias is bipartite. It is driven by ad platforms algorithmically targeting users with high conversion propensity (to maximize ROI) combined with the user's organic browsing habits [41-43]. 
*   **Dating Retention:** Confounding is a pure, closed-loop organic feedback cycle. Highly sociable users inherently generate more bidirectional touchpoints (likes, matches) and inherently stick around longer on the platform ("activity bias") [1, 2].
*   *Adaptation:* Because dating bias is tightly coupled to sequential user actions rather than an external ad-bidder, the **Adversarial CRN approach** is exceptionally well-suited. By penalizing the network for guessing the user's baseline "sociability" from their sequence of likes and matches, the GRL strictly isolates the *incremental retention lift* caused by those interactions [7, 12]. 

**3. Utilization of the Output (Label Generation vs. Budget Allocation)**
*   **Standard Ad MTA:** The ultimate goal is financial. Attribution credits are used to compute Return on Investment (ROI) and inform macro-level budget allocation across different marketing channels (e.g., search vs. social) [14, 44, 45]. 
*   **Dating Retention:** Your goal is Phase 1 supervision: generating granular, per-interaction fractional credits to serve as training labels for a downstream model. 
*   *Adaptation:* The extraction mechanisms in the literature apply directly. You can extract the **causal attention weights** natively produced by CAMTA [46, 47] or DCRMTA [19], or compute **Shapley values** over the debiased predictions of CausalMTA [48, 49]. Instead of translating these into ad dollars, you multiply the debiased fractional weight of each touchpoint by the user's actual continuous outcome (total days-active) to construct your continuous training labels.
