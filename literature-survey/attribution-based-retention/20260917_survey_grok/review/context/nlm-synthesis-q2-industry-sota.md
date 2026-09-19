# NLM Phase 4-A — q2-industry-sota

Scoped to this-run source_ids (G1–G25). returncode=0 elapsed=56.6s stdout_bytes=50013

### **Latest Industry-Authored Attribution Systems (2025-01 to 2026-09)**

Among the scoped sources, the latest industry-authored attribution systems published between January 2025 and September 2026 are **LOTUS** (Alibaba, CIKM 2026) and **Integrated Marketing Attribution (IMA)** (Lowe's, June 2026), alongside **ALM-MTA** (Kuaishou, ICLR 2026) and **LinkedIn DDA / LiDDA** (LinkedIn, January 2025).

---

### **Detailed System Breakdowns**

#### **1. LOTUS (LLM-Oriented Touchpoint Understanding and Selection)**
* **Company:** Taobao & Tmall Group of Alibaba [1, 2]
* **Year:** **2026** (CIKM ’26, November 2026) [3, 4]
* **Method Family:** **LLM-Touchpoint** (LLM-driven semantic reasoning selector using pairwise/listwise prompting over multimodal product/behavior metadata) [5-7].
* **Outcome Being Attributed:** **E-commerce Conversions / Purchases (CVR)** [1, 3, 8].
* **Experiment-Calibrated:** **No** (LLM-selected touchpoint labels are used as auxiliary positive signals to train an industrial multi-task CVR prediction model) [1, 8].
* **User-Level Per-Touch Credit:** **Yes** (evaluates individual touchpoints across a user's full 3-day behavior sequence to identify explicit and implicit touchpoints contributing to conversion) [7, 9, 10].

---

#### **2. Integrated Marketing Attribution (IMA)**
* **Company:** Lowe's Companies, Inc. [11]
* **Year:** **2026** (June 2026, `arXiv:2606.16878`) [11]
* **Method Family:** **DDA / Bayesian Regression Anchored in MMM** (Temporal disaggregation using adstock transformations + channel-specific PyMC Bayesian linear regression anchored to MMM priors) [12-15].
* **Outcome Being Attributed:** **Daily Campaign-Level Incremental Sales / Revenue** [12, 13, 16].
* **Experiment-Calibrated:** **No** (anchored strictly to weekly MMM channel-level priors; integrating experimental holdout results into prior updates is noted as future work) [12, 16, 17].
* **User-Level Per-Touch Credit:** **No** (specifically designed to avoid user-level tracking due to cookie deprecation; operates on aggregated daily campaign media series) [11-13, 18].

---

#### **3. ALM-MTA (Adversarial Learning Mediator based Multi-Touch Attribution)**
* **Company:** Kuaishou Technology [19]
* **Year:** **2026** (ICLR 2026) [20]
* **Method Family:** **Front-Door Causal Attribution** (Front-door identification criterion + Adversarial Proxy Mediator + Contrastive InfoNCE overlap control + Inverse Propensity Weighting) [19, 21-23].
* **Outcome Being Attributed:** **Content Creation / User Uploads** (attributing user content creation to prior video consumption touchpoints in a "Consumption-Drives-Production" / CDP setting; *not retention*) [19, 24, 25].
* **Experiment-Calibrated:** **No** (derives causal uplift from observational logs via front-door identification and IPW reweighting, evaluated using a non-RCT propensity-stratified grouped AUUC protocol) [22, 26-28].
* **User-Level Per-Touch Credit:** **Yes** (computes individualized counterfactual removal uplift \\(\Delta(\tau_j \mid X, T) = g_\theta(X, T) - g_\theta(X, T \setminus \{\tau_j\})\\) for each consumed item in a user's sequence) [22, 25, 29].

---

#### **4. LinkedIn Buyer-Journey Data-Driven Attribution (LiDDA)**
* **Company:** LinkedIn [30, 31]
* **Year:** **2025** (January 2025 / `arXiv:2505.09861`) [30, 31]
* **Method Family:** **Data-Driven Attribution (DDA)** (Transformer self-attention neural network with discrete daily interval positional encodings, fine-tuned LLM campaign embeddings, and probabilistic impression imputation) [4–6, 8, 9, 13].
* **Outcome Being Attributed:** **B2B / B2C Marketing Conversions** [30, 32, 33].
* **Experiment-Calibrated:** **Yes** (attention-derived attribution weights are post-calibrated using controlled marketing A/B holdout experiments and Marketing Mix Models [MMM] to align with incrementality) [34-37].
* **User-Level Per-Touch Credit:** **Yes** (models member-level touchpoint sequences and outputs normalized attention weights as fractional credit per touchpoint in the journey) [33, 34, 38].

---

#### **5. Amazon Ads Multi-Touch Attribution (Cited in LOTUS)**
* **Company:** Amazon Ads [39]
* **Year:** **2025** (August 2025, `arXiv:2508.08209`, cited in LOTUS Ref [40]) [39].
* **Method Family:** **DDA / Causal MTA** [39].
* **Outcome Being Attributed:** **Ad Conversions** [39].
* **Experiment-Calibrated:** *Not specified in source* [39].
* **User-Level Per-Touch Credit:** **Yes** (multi-touch ad conversion attribution across user journeys) [39].

---

💡 *Would you like to compare how front-door identification in ALM-MTA versus LLM-based touchpoint selection in LOTUS handle sequence confounding when generating training labels?*
