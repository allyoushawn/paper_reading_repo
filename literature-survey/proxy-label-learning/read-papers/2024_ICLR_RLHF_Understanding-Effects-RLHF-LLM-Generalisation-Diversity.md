# Paper Analysis: Understanding the Effects of RLHF on LLM Generalisation and Diversity

**Source:** https://arxiv.org/pdf/2310.06452  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Understanding the Effects of RLHF on LLM Generalisation and Diversity  
**Authors:** Robert Kirk, Ishita Mediratta, Christoforos Nalmpantis, Jelena Luketina, Eric Hambro, Edward Grefenstette, Roberta Raileanu  
**Abstract:** Comprehensive empirical analysis of how each stage of the RLHF fine-tuning pipeline (SFT, reward modeling, RLHF) affects out-of-distribution generalization and output diversity. Key finding: RLHF improves generalization over SFT — especially for larger distribution shifts — but substantially reduces output diversity. Provides the first rigorous empirical demonstration of across-input mode collapse from RLHF.

**Key contributions:**
- Identifies generalization-diversity trade-off: RLHF improves OOD performance but reduces per-input and across-input output diversity
- Shows RLHF generalizes better than SFT for larger distribution shifts (Sequential Instructions OOD task)
- First rigorous demonstration of across-input "mode collapse" under RLHF training
- Evaluation framework: GPT-4 win rates for generalization; EAD, Sentence-BERT, NLI metrics for diversity
- KL penalty tuning fails to recover diversity — increasing KL penalty worsens both performance and diversity

**Methodology:**  
Three policy types: SFT (behavioral cloning), RLHF (PPO + reward model + KL penalty), Best-of-N (BoN, N=16). Base models: LLaMA 7B and OPT (5 sizes for scaling). Two tasks: summarization (TL;DR → CNN/DailyMail OOD) and instruction following (AlpacaFarm → AlpacaEval and Sequential Instructions OOD).

**Main results:**  
RLHF and BoN outperform SFT on instruction following across ID and OOD. On Sequential Instructions (hardest OOD shift), RLHF generalizes much better than SFT. BoN outperforms RLHF on summarization but RLHF wins on instruction following. RLHF diversity (EAD, Sentence-BERT) substantially lower than SFT. Across-input diversity also lower for RLHF.

---

## 2. Experiment Critique

**Design:**  
Two tasks, two base model families (LLaMA + OPT), multiple evaluation datasets, three diversity metrics, GPT-4 as human proxy evaluator. Thorough coverage. The per-input vs across-input diversity distinction is methodologically important.

**Statistical validity:**  
Single runs for primary LLaMA experiments (standard for LLM experiments). OPT experiments provide model size trends across 5 sizes. GPT-4 evaluation validated against human preferences in appendix.

**Online experiments (if any):**  
None.

**Reproducibility:**  
Code released at https://github.com/facebookresearch/rlfh-gen-div. Uses AlpacaFarm models released by Dubois et al. 2023.

**Overall:**  
Important empirical contribution for understanding RLHF limitations. Key limitations: no theoretical explanation; only SFT/RLHF/BoN evaluated (not DPO, RLAIF, etc.); NLI diversity metric shows no meaningful differences between methods (possibly too coarse-grained). Pure empirical work with no causal mechanism proposed.

---

## 3. Industry Contribution

**Deployability:**  
RLHF is the dominant fine-tuning paradigm for deployed LLMs (ChatGPT, Claude). This paper directly characterizes a known pain point — mode collapse and reduced creativity — and provides empirical evidence connecting it to the RLHF training procedure. The finding that BoN scales better than RLHF at larger model sizes is actionable.

**Problems solved:**  
In proxy-label learning for behavioral prediction: reward models trained on implicit user feedback function analogously to the RLHF reward model. The generalization-diversity trade-off likely applies — models optimized on proxy labels may generalize better to new users but produce more homogeneous predictions.

**Engineering cost:**  
N/A — this is an analysis paper, not a new method.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
First rigorous empirical demonstration of mode collapse under RLHF (across-input diversity reduction). First systematic comparison of RLHF, SFT, and BoN on OOD generalization across multiple tasks. Prior RLHF work evaluated only in-distribution.

**Prior work comparison:**  
Stiennon et al. 2022 performed some OOD evaluation (TL;DR → CNN/DM) but didn't systematically compare pipeline stages. Perez et al. 2022 and Khalifa et al. 2021 showed diversity reductions but used simple n-gram metrics and limited settings.

**Verification:**  
UCL + Meta FAIR, ICLR 2024. Well-cited in the RLHF analysis literature.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| TL;DR (Reddit summarization) | public | Yes | In-distribution |
| CNN/DailyMail | public | Yes | OOD for summarization |
| AlpacaFarm Self-Instruct | public | Yes | ID for instruction following |
| AlpacaEval | public | Yes | OOD (easy shift) |
| Sequential Instructions | custom | Released | OOD (hard shift) |

**Offline experiment reproducibility:**  
High. Code and models released.

---

## 6. Community Reaction

UCL + Meta FAIR, ICLR 2024. One of the first rigorous empirical studies of RLHF trade-offs. The mode collapse finding resonates with practitioner observations. The generalization results provide partial justification for why RLHF-trained models (ChatGPT, Claude) perform better than SFT-only models in practice.

**Relevance to proxy-label learning:** Peripheral but informative. Reward model learning from proxy labels shares structure with the attribution-based proxy label problem. The generalization vs diversity trade-off may manifest similarly.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |
| [2024_NeurIPS_GRM_Regularizing-Hidden-States-Generalizable-Reward-Model.md](./2024_NeurIPS_GRM_Regularizing-Hidden-States-Generalizable-Reward-Model.md) | Summary | Zhang, Tong Zhang Abstract: Reward models trained from human preferences can suffer poor OOD generalization and enable reward hacking during downstream RLHF-style optimization. The paper proposes GRM: keep the pretrained LM head, add a reward head on shared hidden states, and jointly optimize pre... |
| [2024_arXiv_OnPolicyActive_Cost-Effective-Proxy-Reward-Model-Construction.md](./2024_arXiv_OnPolicyActive_Cost-Effective-Proxy-Reward-Model-Construction.md) | Summary | Authors: Yifang Chen, Shuohang Wang, Ziyi Zhang, Hiteshi Sharma, Nikos Karampatziakis, Donghan Yu, Kevin Jamieson, Simon Shaolei Du, Yelong Shen Abstract: RLHF pipelines are bottlenecked by preference labeling costs. The paper studies building a weak evaluation model (proxy reward oracle) under v... |
| [2024_arXiv_RewardGeneralizationinRL_Reward-Generalization-in-RLHF-A-Topological.md](./2024_arXiv_RewardGeneralizationinRL_Reward-Generalization-in-RLHF-A-Topological.md) | Summary | Title: Reward Generalization in RLHF: A Topological Perspective Authors: Tianyi Qiu, Fanzhi Zeng, Jiaming Ji, Dong Yan, Kaile Wang, Jiayi Zhou, Yang Han, Josef Dai, Xuehai Pan, Yaodong Yang Abstract: Th |

---
## Meta Information

**Authors:** Robert Kirk, Ishita Mediratta, Christoforos Nalmpantis, Jelena Luketina, Eric Hambro, Edward Grefenstette, Roberta Raileanu  
**Affiliations:** University College London; Meta FAIR; University of Oxford  
**Venue:** ICLR 2024  
**Year:** 2024  
**PDF:** available at arxiv.org/pdf/2310.06452  
**Relevance:** Peripheral  
**Priority:** 2  
**NLM Source ID:** 0f63f851-8f5b-4b8b-9285-7d5b8cbbfe75
