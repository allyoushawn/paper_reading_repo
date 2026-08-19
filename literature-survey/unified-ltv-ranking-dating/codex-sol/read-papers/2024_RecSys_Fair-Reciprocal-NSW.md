# Fair Reciprocal Recommendation in Matching Markets

- **Source index:** 113
- **Source ID:** `9f98f857-7140-4fc0-9f17-cde7028d8fa6`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Yoji Tomita, Tomohiko Yokoyama
- **Affiliations:** CyberAgent; University of Tokyo
- **Year / venue:** 2024 / RecSys
- **Direction / priority:** D8 reciprocal recommendation and fairness / Priority 3 (core)
- **URL:** https://doi.org/10.1145/3640457.3688130

## 1. Summary

The paper treats recommendation positions as opportunities allocated to agents on both sides of a matching market. A policy is unfair when an agent would prefer another agent’s exposure allocation—envy-freeness from fair division. Maximizing expected matches by alternating social-welfare optimization can create substantial envy when preferences concentrate on popular users. The proposed alternative maximizes Nash social welfare (NSW) on both sides with an alternating Frank–Wolfe procedure.

Synthetic experiments vary market balance, examination curves, and popularity concentration. NSW produces almost zero envy while retaining competitive expected matches, including imbalanced cases where a heuristic leaves one side envious. A real-data simulation uses a dense 200×200 sample from a Japanese dating platform with millions of cumulative members; preferences come from ALS over like/dislike and match/sorry actions. NSW again has the fewest envies and competitive expected matches, but the experiment is not an online test.

## 2. Experiment Critique

The work defines fairness in terms of each person’s own opportunity preferences, evaluates both market sides, and explicitly tests imbalance. Comparisons include naive, product, matching, social-welfare, and heuristic policies.

The platform sample is selected for relatively dense interactions, which may overrepresent active/popular users. Preference scores are estimated, so expected-match and envy measurements inherit model error. Figures rather than tables carry most quantitative results. Most importantly, the NSW algorithm has `n²m + nm²` variables and is acknowledged as impractical at large scale. No retention, message, revenue, or live fairness outcome is measured.

## 3. Industry Contribution / Project Relevance

The paper makes exposure fairness a first-class two-sided objective instead of an after-the-fact popularity diagnostic. A dating LTV ranker could use NSW or its log-utility intuition as a regularizer so long-term value is not gained by starving a user cohort of meaningful opportunity.

Fairness and retention may reinforce each other, but the evidence does not show that envy reduction increases LTV. Production needs scalable approximations, time-amortized opportunity accounting, protected-group audits, and minimum-quality constraints. Matching probability alone is also too shallow for the project’s success paradox and downstream conversations.

## 4. Novelty

The novelty is a two-sided envy-freeness definition for reciprocal recommendation and an alternating Nash-social-welfare optimizer that balances match count and each side’s opportunity utility.

## 5. Dataset Availability

The dating data are proprietary. Code is available at https://github.com/CyberAgentAILab/FairReciprocalRecommendation.

## 6. Community Reaction

Not specified in source beyond RecSys 2024 publication.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## 8. Meta Information

- **Domain:** Online dating
- **Objective:** Expected mutual matches plus envy-free exposure opportunity
- **Method:** Alternating Nash social welfare via Frank–Wolfe
- **Evaluation:** Synthetic and proprietary-data simulation
- **Primary limitation:** Cubic-scale variable count and no online test
- **Project role:** Two-sided opportunity/fairness regularization
