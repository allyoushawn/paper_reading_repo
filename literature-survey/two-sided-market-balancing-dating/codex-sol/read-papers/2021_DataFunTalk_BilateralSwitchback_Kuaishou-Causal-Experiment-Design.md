# Paper Analysis: 快手因果推断与实验设计

**Source:** https://hub.baai.ac.cn/view/9770  
**Date analyzed:** 2026-08-19

---

## 1. Summary

**Title:** 快手因果推断与实验设计 (*Kuaishou Causal Inference and Experimental Design*)  
**Authors:** 金雅然 (Dr. Yaran Jin), Kuaishou; edited by 赵一方 (Yifang Zhao), Baidu  
**Abstract:** This technical-talk recap surveys Kuaishou's causal methods for product, recommendation, and live-streaming questions. It covers modified difference-in-differences, synthetic control, double machine learning, causal forests, uplift learners, causal graphs, bilateral experiments, and time-slice switchbacks for network effects.

**Key contributions:**

- Describes how Kuaishou chooses causal tools for observational, randomized, heterogeneous, and network-interference settings.
- Uses bilateral randomization to expose host-viewer spillovers.
- Uses optimized switchback timing when individual interactions create dynamic carryover.

**Methodology:** Modified difference-in-differences estimates user-state strata separately and weights them. Double machine learning uses sample splitting, cross-fitting, and orthogonal residualization for high-dimensional confounding. Causal forests and S/T/X learners estimate heterogeneous effects. Bilateral experiments randomize hosts and viewers, comparing fully treated Y with fully untreated N3; switchbacks alternate policy by time slice and choose intervals from estimated carryover and bias-variance trade-offs.

**Main results:** Quantitative metrics, sample sizes, experiment durations, and effect estimates are not specified in source.

## 2. Experiment Critique

**Design:** The source distinguishes observational adjustment, two-population randomization, and temporal randomization with carryover. It is a methodological overview, not a report of one fully documented experiment.

**Statistical validity:** It discusses confidence intervals, variance, heterogeneous effects, and carryover, but provides no numerical estimates or validation statistics.

**Online experiments:** Real Kuaishou examples include a live-stream red-envelope feature, recommendation diversity, host-viewer widgets, and “Live PK” moments. Sample sizes and durations are not specified.

**Reproducibility:** Conceptual procedures are described; code, assignments, outcomes, data, timing, and exact estimators are absent.

**Overall:** The operational routing among causal designs is valuable. Evidence is insufficient to judge effect magnitude, bias reduction, power, or implementation quality.

## 3. Industry Contribution

**Deployability:** Bilateral experiments require assignment on both populations; switchbacks require time-based policy routing and carryover monitoring.

**Problems solved:** Cross-side spillovers, temporal peer interference, high-dimensional confounding, and heterogeneous responses.

**Engineering cost:** High for bilateral and switchback infrastructure; medium for observational causal pipelines once features and treatment definitions exist.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** A platform practice overview, not a claim to invent the underlying methods.

**Prior work comparison:** The source names Pearl's causal graph framework, Rubin's potential-outcomes framework, the Frisch-Waugh-Lovell theorem, and S-, T-, and X-learners. Specific titles and years are not specified, and three additional prior works are not specified in source.

**Verification:** Limited to concepts explicitly named by the source.

## 5. Dataset Availability

**Datasets mentioned:**

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Kuaishou live-streaming product logs | Not public | No | Covers red envelopes, diversity recommendations, widgets, and Live PK; scale and period absent. |

**Offline experiment reproducibility:** Not reproducible from the article because no data, code, assignment plan, or numeric outcomes are provided.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Exact mechanism:** Randomize both marketplace sides to identify cross-side transfers, or rotate the entire policy through time to prevent interacting users from simultaneously experiencing conflicting treatments. Use causal graphs to map exposure-to-like-to-match-to-conversation pathways.

**Metrics and reported effect:** Not specified in source.

**Capacity/interference relevance:** Capacity limits are not modeled. Marketplace interference is explicit: bilateral designs handle simple host-viewer spillovers, while switchbacks handle dynamic individual-to-individual effects and carryover.

**Practical mapping:** A dating app could independently assign viewers and shown users, compare fully treated and untreated cells, or switch a market-wide ranking policy by region and time. Outcomes should include total matches, conversations, match coverage or Gini, wasted likes, and retention on both sides; the source reports none of these.

**Dating fit: Medium.** The experiment designs transfer to interactive two-sided systems, but Kuaishou is live streaming and supplies no dating or capacity evidence.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| No verified inbound mentions within the 45-source corpus. | — | — |

## Meta Information

**Authors:** 金雅然 (Yaran Jin); editor 赵一方 (Yifang Zhao)  
**Affiliations:** Kuaishou; Baidu  
**Venue:** DataFunTalk technical-talk recap, mirrored by BAAI Hub  
**Year:** 2021  
**PDF:** web source; no PDF required  
**Relevance:** Related  
**Priority:** 1

## Annotated Bibliography Fields

- **Title:** 快手因果推断与实验设计 (*Kuaishou Causal Inference and Experimental Design*)
- **Authors/organization:** Yaran Jin, Kuaishou; edited by Yifang Zhao, Baidu
- **Year:** 2021
- **Venue/type:** DataFunTalk technical-talk recap; BAAI Hub mirror
- **Link:** https://hub.baai.ac.cn/view/9770
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Summarized Kuaishou's causal toolkit for product and recommendation evaluation, including modified difference-in-differences, synthetic control, double machine learning, causal forests, uplift learners, causal graphs, bilateral randomization, and switchback experiments. Live-streaming examples illustrate when cross-side or temporal spillovers make ordinary user-level A/B tests invalid.
- **Mechanism relevant to two-sided balancing (≤50 words):** Randomize both marketplace populations to measure cross-side spillovers, or rotate a market-wide policy across time slices when interacting users contaminate one another's assignments.
- **Metrics and reported effect:** Not specified in source.
- **Dating-app fit:** Medium — interference-aware designs transfer, but capacity, reciprocal matches, and dating outcomes are absent.
- **Confidence:** High on source identity and described methods; low on effect magnitude because no quantitative evidence is reported.
