# Paper Analysis: Model-based Recall in Momo Social Recommendation

**Source:** https://www.infoq.cn/article/7s6oqecgk8bmckobj0ud  
**Date analyzed:** 2026-08-18  
**Source ID:** a00fc94f-2ad8-4fa6-b6d9-9c8970cb527e  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** notebook_query intentionally not called; source_get_content success

---

## Required Survey Card Fields

- **Title:** Model-based Recall in Momo Social Recommendation
- **Authors or company:** Momo / InfoQ China
- **Venue:** InfoQ-China
- **Year:** 2021
- **URL:** https://www.infoq.cn/article/7s6oqecgk8bmckobj0ud
- **Source type:** company blog
- **Direction:** D8
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1, “Objective” and “Labels.”
- **Prediction or incrementality:** Not specified in source. Indexed evidence does not establish exposure-effect identification; treat the method as prediction or optimization unless validated experimentally.
- **Model architecture:** See §1, “Architecture.”
- **Credit assignment:** See §1, “Credit assignment.”
- **Training data and counterfactual handling:** See §1, “Training evidence,” and prediction/incrementality above.
- **Offline and online evaluation:** See §2.
- **Reported gains:** See §2; no metric is added beyond indexed-source evidence.
- **Applicability to a two-sided dating recommender:** See § Project Relevance.
- **Unverified claims:** Dating transfer statements are explicitly labeled as survey inference.

---

## 1. Summary

### Core problem and contribution — indexed-source evidence

- 首页 AI会议 hot AI课程 hot AI应用 hot 报告 HarmonyOS Snowflake new 更多    写点什么  创作场景  记录自己日常工作的实践、心得 发表对生活和职场的感悟 针对感兴趣的事件发表随笔或者杂谈 从 0 到 1 详细介绍你掌握的一门语言、一个技术，或者一个兴趣、爱好…
- 关于陌陌 陌陌是一款基于地理位置的移动社交应用，是中国领先的开放式社交平台之一。用户在陌陌 APP 可以通过字符，文字，语音，图片等来展示自己，基于地理位置来发现附近的人，并且加入附近的群组，我们希望能够建立一种真实、有效和健康的社交关系。 这里展示了陌陌的主要发展历程：陌陌公司在 2011 年成立，2014 年在美国上市，在 2018 年月活已经过亿，并全资收购了探探，进一步巩固了陌陌在开放式社交领域中的地位。 2.
- 陌陌社交主场景 陌陌的社交推荐主场景为附近动态和附近的人。接下来，我们简单介绍下这两个场景的基本特点。 附近动态场景处于陌陌 APP 首页的首帧，附近动态场景强调的是以内容为载体的用户社交匹配。用户发布的动态，充当了一个桥梁作用，将用户和动态发布者连接起来。在动态场景本身，用户可以对动态进行点赞、评论和对话的操作。在动态下方，存在这种点赞、评论和对话的这种按钮。如果用户点击左上角的头像，可以进入发布者的个人页面，如最左侧这个图，我们可以看到发布者的一些高清头像，个人资料和过往动态信息等，并且可以在这里进行一些对话和关注等操作。另外点击动态本身，我们会进入动态详情页，可以看到动态的评论情况。在动态底部还有一个相似动态推荐的上拉按钮，如果你喜欢相似推荐的动态，可以拉起浏览到和当前动态相似的一些其他动态情况。 附近的人场景在陌陌 APP 首页的第二帧，在这个场景下，我们强调的是以地理位置为依托的用户社交匹配，通过点击该场景下的用户展示图像，可以进入展示用户的个人主页，看到用户更丰富的一些高清头像、个人资料、或者是一些过往动态，并进行对话或关注等操作。我们一直致力于提高附近动态和附近的人场景的社交推荐效果，提高用户的浏览体验。 模型化召回技术简介 1.
- 模型化召回 接下来，我们简单介绍一下模型化召回技术。在推荐系统中，召回模块是非常重要的一环。召回策略可以简单的分为功能性召回、热门召回、业务召回和个性化召回等。个性化召回能够有效的把握用户的兴趣偏好，在整个召回系统中处于十分重要的位置。 传统的个性化召回主要包括重定向召回、协同过滤类召回、内容偏好类召回等。这类召回算法一般实现简单、表征能力有限、泛化能力相对不足。近年来崛起的模型化 Embedding 检索类召回，比如图表征召回、浅层模型化召回、深度匹配模型化召回、内容语义模型化召回等，则具有更好的表征能力和更强的泛化能力，在推荐系统中受到了越来越多的重视。 2.

### Objective — indexed-source evidence

Not specified in source.

### Labels, horizon, delay, sparsity, and censoring — indexed-source evidence

Not specified in source.

### Architecture — indexed-source evidence

Not specified in source.

### Credit assignment — indexed-source evidence

Not specified in source.

### Training data, baselines, and counterfactual evidence

Not specified in source.

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- 首页 AI会议 hot AI课程 hot AI应用 hot 报告 HarmonyOS Snowflake new 更多    写点什么  创作场景  记录自己日常工作的实践、心得 发表对生活和职场的感悟 针对感兴趣的事件发表随笔或者杂谈 从 0 到 1 详细介绍你掌握的一门语言、一个技术，或者一个兴趣、爱好…

### Reported gains — indexed-source evidence

Not specified in source.

### Limitations, failure modes, and negative results — indexed-source evidence

Not specified in source.

**Statistical validity:** Not specified in source beyond the indexed evidence above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** Not specified in source.  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** Not specified in source.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** See §1 source evidence.  
**Prior work comparison:** Not specified in source. Indexed content does not provide a defensible top-5–7 ranking by citation frequency.  
**Verification:** No independent novelty verification was performed in this fallback batch.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Dataset or production logs described by the source | Not specified in source. | Not specified in source. | Indexed evidence is summarized in §1 where available. |

**Offline experiment reproducibility:** Not specified in source.

---

## 6. Community Reaction

Not specified in source.

---

## Project Relevance

**Source-grounded facts:** The evidence snippets above summarize only material present in the indexed source.

**Survey inference:** This source is relevant to reciprocal or two-sided ranking, marketplace interference, congestion, or bilateral experimentation. For dating, any transfer must be tested with 7–30 day retention and weeks-long subscription/à-la-carte revenue labels while keeping like, match, and conversation heads as migration auxiliaries.

**Prediction vs. incrementality:** Not specified in source. Indexed evidence does not establish exposure-effect identification; treat the method as prediction or optimization unless validated experimentally.

**Reciprocity and congestion:** This direction directly targets two-sided or reciprocal concerns where the evidence above supports them; dating still needs candidate-capacity and bilateral-acceptance checks.

**Cascade and low base rates:** Map the method to impression → like → match → conversation → retention/revenue only as a survey hypothesis; validate calibration and rare-event behavior.

**Success paradox:** Not specified in source. Protect match quality and successful off-platform outcomes so retention/revenue optimization does not penalize successful matching.

**Evaluation implication:** Add bilateral outcome metrics, candidate exposure concentration, delayed-label backtests, and randomized incrementality checks to any source protocol.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** Momo / InfoQ China (individual authors not taken from selected-source metadata)  
**Affiliations:** Momo / InfoQ China  
**Venue:** InfoQ-China  
**Year:** 2021  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 2
