# TSMOO: Solving multi-objective experimentation with constrained Thompson sampling [1]

**Source:** https://www.amazon.science/publications/tsmoo-solving-multi-objective-experimentation-with-constrained-thompson-sampling  
**Date analyzed:** 2026-09-24  
**NLM source id:** `8119ba67-ed0b-427c-9ffe-03ccc1da6d87`  
**Queue id:** G39  
**Q2 class:** NOT

---

## 1. Summary

### **Part 1: Technical Breakdown of *TSMOO: Solving multi-objective experimentation with constrained Thompson sampling***

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *TSMOO: Solving multi-objective experimentation with constrained Thompson sampling* [1]
* **Authors:** **Krishna Chaitanya Kalagarla**, **Yi Liu**, **Lin Chai**, and **Wenyang Liu** [1]
* **Affiliation:** **Amazon** [1]
* **Year & Venue:** Published in **2026** at the *20th ACM Conference on Recommender Systems (RecSys ’26)*, September 27–October 02, 2026, Minneapolis, MN, USA [1]

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Traditional online A/B testing limits the number of treatment variants that can be evaluated concurrently [1]. Bandit-based adaptive experimentation dynamically reallocates traffic across an order of magnitude more treatments, but current algorithms face a structural trade-off: single-metric Thompson Sampling methods are robust to novelty effects but cannot handle multiple launch criteria/constraints, whereas elimination-based multi-objective methods support multiple constraints but risk prematurely eliminating promising treatments due to early noise [1].
* **Key Contribution:**
  1. **TSMOO Framework:** Introduces **Thompson Sampling with Multi-Objective Optimization (TSMOO)**, bridging multi-metric optimization with continuous learning grounded in stochastically constrained best-arm identification [1].
  2. **Feasibility-Preserving Exploration:** Extends single-metric Thompson Sampling to multi-objective batch traffic allocation by estimating multi-constraint feasibility at each step while maintaining exploration across all treatments without premature elimination [1].
  3. **Uplift-Modeled Temporal Control:** Incorporates uplift modeling to isolate temporal and novelty effects shared between treatment and control variants, ensuring Gaussian distribution assumptions hold [1].

---

#### **(3) Proposed Method or Architecture in Detail**

##### **Architectural Components**
* **Stochastically Constrained Best-Arm Identification:** Formulates traffic allocation as a constrained bandit problem to identify top-performing arms satisfying multiple metric thresholds [1].
* **Multi-Constraint Feasibility Estimation:** Evaluates feasibility across all constraint metrics at each batch allocation step, adjusting posterior sampling to balance exploration and constraint satisfaction [1].
* **Uplift Modeling Component:** Subtracts shared baseline temporal variations and novelty effects between treatment and control, stabilizing reward estimates and satisfying Gaussian error assumptions [1].

##### **Credit Assignment Mechanics**
* **Not specified in source / Does NOT perform credit assignment.**
* TSMOO is an adaptive experimentation / multi-armed bandit traffic allocation algorithm for online A/B testing [1]. It does **not** perform multi-touch sequence attribution or assign fractional credit to past user interaction touchpoints.

---

#### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets:** Evaluated in simulations replaying historical real-world experimentation patterns [1]. Specific dataset names are *Not specified in source* (landing page abstract only) [1].
* **Production Deployment:** *Not specified in source* (developed at Amazon; evaluated via historical experiment replay simulations) [1].
* **Comparison Baselines:**
  1. *Single-metric Thompson Sampling baselines* [1].
  2. *Elimination-based multi-objective bandit baselines* [1].

---

#### **(5) Key Quantitative Results with Numbers**
* **Success Rate in Multi-Winner Settings:** Achieves **93–94% success rates** in historical simulation replays [1].
* **Success Rate Under Novelty Effects:** Achieves **63–66% success rates** when novelty effects are present [1].
* **Baseline Superiority:** Outperforms both single-metric Thompson Sampling and elimination-based multi-objective baselines across evaluation scenarios [1].

---

#### **(6) Limitations, Failure Modes, or Negative Results**
* **Not specified in source.** *(Note: The landing page explicitly states that the full PDF text was not publicly posted on the page)* [1].

---

#### **(7) Top 5–7 Most Heavily Cited Prior Works**
* **Not specified in source.** *(Specific prior work citations are omitted on the landing page abstract)* [1].

---

### **Part 2: Dating App Retention Attribution Project Evaluation**

#### **(A) Q1 or Q2 or Both or Neither?**
* **Neither.** [1]
* **Explanation:**
  * **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** While accepted at RecSys 2026 and developed at Amazon, TSMOO is an **adaptive experimentation / multi-armed bandit traffic allocation framework** for online A/B testing under multi-metric launch constraints, not an industry multi-touch attribution (MTA) measurement system [1].
  * **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** TSMOO dynamically reallocates traffic across experimental treatment arms in online A/B tests, rather than attributing user retention or active days back to individual past in-app interaction touchpoints (swipes, matches, messages) across historical logs [1].

---

#### **(B) Q2 Class**
* **Classification:** **NOT** [1]
* **Justification:** TSMOO is a multi-objective bandit-based adaptive experimentation policy algorithm [1]. It does **not** produce or publish a per-exposure retention credit table.

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction credit table.** [1]
* **Target Outcome:** **Multi-Objective Experimentation Traffic Allocation & Best-Arm Identification** (maximizing primary performance metrics subject to multi-metric launch feasibility constraints while remaining robust to novelty/temporal effects) [1].

---

#### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**
* **How it Improves/Informs Experimentation:** TSMOO does **not** provide a post-hoc attribution credit model [1]. However, it offers a framework for **safely running online A/B tests of candidate profile rankers aiming for 7-Day Retention (N7)**:
  1. *Multi-Metric Launch Constraints:* When deploying a new candidate profile ranker to increase N7 retention, platforms must satisfy secondary guardrails (e.g., match rate, chat response rate, unmatch/report rates, latency). TSMOO dynamically reallocates user traffic to top-performing rankers while ensuring all guardrail constraints are met [1].
  2. *Novelty Effect Control:* Uplift modeling filters out temporary spikes caused by UI or algorithm changes, ensuring observed retention gains represent genuine long-term user engagement rather than transient novelty artifacts [1].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  * *Experimental Arms:* Candidate profile ranker variants (e.g., Last-Touch Baseline vs. DDA Model).
  * *Primary Goal & Constraints:* Primary target = N7 Retention; Constraints = Swipe-to-Match Rate, Message Initiation Rate, Infrastructure Latency.
  * *TSMOO Execution:* Dynamically routes user cohorts to top-performing rankers without prematurely eliminating promising variants or violating safety guardrails.

---

#### **(E) Selection-Bias & Confounding Handling**
1. **Novelty & Shared Temporal Effect Mitigation:** Uses uplift modeling to subtract shared temporal trends and novelty spikes between treatment and control variants, ensuring Gaussian error assumptions hold [1].
2. **Continuous Exploration:** Retains all treatments throughout exploration, avoiding premature arm elimination caused by early statistical noise [1].

---

#### **(F) Deployed or Production Dataset Evidence**
* **Production Deployment:** **Not specified in source** (developed by Amazon researchers; evaluated via simulations replaying historical real-world experimentation patterns) [1].
* **Quoted Numbers from Source:**
  * **Success rate in multi-winner settings:** **93–94%** [1].
  * **Success rate under novelty effects:** **63–66%** [1].

---

💡 *Would you like to explore how TSMOO's uplift modeling and multi-metric constraints could be configured for adaptive A/B testing of your new retention-driven profile ranker?*

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

### **Source Evaluation: *TSMOO: Solving multi-objective experimentation with constrained Thompson sampling***
*(Kalagarla, Liu, Chai, & Liu, Amazon, RecSys 2026)* [1]

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**

**Neither.** [1]
* **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** While accepted at RecSys 2026 and developed by researchers at Amazon, TSMOO is an **adaptive experimentation and traffic allocation framework for multi-objective online A/B testing**, not an industry multi-touch attribution (MTA) measurement system [1, 2].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** TSMOO dynamically reallocates traffic across experimental treatment arms in online A/B tests subject to multi-metric constraints, rather than attributing user retention or active days back to individual in-app interaction touchpoints across historical user logs [1].

---

### **(B) Q2 Class**

**NOT.** [1]
* **Justification:** TSMOO is a multi-objective bandit-based adaptive experimentation framework for online A/B testing [1]. It does **not** produce or publish a per-exposure or per-touchpoint retention credit table [1].

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction credit table** [1].
* **Target Outcome:** **Multi-Objective Adaptive Traffic Allocation & Best-Arm Identification** (dynamically reallocating traffic across an order of magnitude more treatment variants while satisfying multi-metric launch feasibility constraints) [1].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**

* **How it Improves/Informs Strategy:** TSMOO is an adaptive experimentation algorithm rather than a post-hoc attribution model [1]. However, it provides an infrastructure solution for **safely running online A/B tests of candidate profile rankers aimed at N7 retention**:
  1. **Multi-Constraint Launch Criteria:** When deploying new profile rankers to boost 7-day retention (N7), platforms must satisfy secondary guardrails (e.g., match rate, message initiation rate, system latency) [1]. Traditional single-metric Thompson Sampling cannot handle multiple launch criteria, while elimination-based methods risk prematurely dropping promising algorithms due to early statistical noise [1].
  2. **Feasibility-Preserving Exploration:** TSMOO estimates multi-constraint feasibility at every batch allocation step, reallocating traffic toward winning rankers while preserving all treatment arms throughout exploration and honoring safety guardrails [1].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  * **Experimental Arms:** Candidate profile rankers (e.g., Last-Touch baseline vs. Removal-Effect attributor vs. DDA model) [1].
  * **Primary Metric & Constraints:** Primary goal = N7 User Retention; Launch Constraints = Minimum Swipe-to-Match Rate, Message Initiation Rate, and Infrastructure Latency [1].
  * **TSMOO Traffic Allocation:** Continuously learns and routes user traffic to the most effective ranker variants without violating platform safety constraints [1].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Uplift Modeling for Temporal & Novelty Bias:** Integrates an uplift modeling component that isolates and subtracts shared temporal trends and novelty spikes between treatment and control variants, ensuring Gaussian error assumptions hold even under volatile real-world conditions [1].
2. **Preservation of Exploration Arms:** Preserves all treatment arms throughout the exploration phase rather than using early elimination, preventing premature removal of promising algorithms caused by early noisy samples [1].

---

### **(F) Deployed or Production Dataset Evidence**

* **Production Deployment / Dataset Evidence:** Tested in **"simulations replaying historical real-world experimentation patterns"** [1]. Live production deployment is **Not specified in source** [1].
* **Quoted Numbers from the Source:**
  * **Multi-Winner Success Rate:** Achieves **93–94%** success rates in multi-winner simulation settings [1].
  * **Success Rate Under Novelty Effects:** Achieves **63–66%** success rates when novelty effects are present [1].
  * **Treatment Scale:** Dynamically reallocates traffic across an **"order of magnitude more treatments"** compared to traditional A/B testing [1].
  * **Other Metrics:** *Not specified in source* [1].

---

🧪 *Would you like to explore how TSMOO's uplift modeling and multi-metric constraints could be configured for adaptive A/B testing of your new retention-driven profile ranker?*

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
**Priority:** see queue.md `G39`
