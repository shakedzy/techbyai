---
layout: post
title: "AI Innovations and Industry Updates: Today's Highlights"
subtitle: "Exploring new AI research, industry trends, and emerging technologies"
audio: 2024-05-28-ai-innovations-and-industry-updates-todays-highlights.mp3
date: 2024-05-28
duration: "08:55"
bytes: 2140749
model: gpt-4o
cost: 1.25
processing: "0:03:21.917075"
version: "0.1.10"
headers: " * GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction<br /> * NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models<br /> * MultiOOD: Scaling Out-of-Distribution Detection for Multiple Modalities<br /> * Cybersecurity & Artificial Intelligence Cited As Top Board Priorities In 2024<br /> * Samsung’s 2024 AI-Powered TV and Soundbar Lineup Impresses Reviewers<br /> * PolyU research finds improving AI large language models helps better align with human brain activity<br /> * Y Combinator CEO Believes in AI Regulation; Calls Out Certain AI Bills"
---

# GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction
_Summarized by: Ava Mitchell_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2405.17429v1)]

The paper introduces "GaussianFormer," a novel approach to 3D semantic occupancy prediction for vision-based autonomous driving. Traditional methods often use dense voxel grids, which are computationally expensive and inefficient due to the sparsity of real-world scenes. GaussianFormer addresses this by representing 3D scenes with sparse 3D semantic Gaussians, each characterized by mean, covariance, and semantic features.

The model consists of several components:
1. **3D Gaussian Representation**: This reduces memory usage by representing objects as flexible regions of interest, described by 3D Gaussians.
2. **GaussianFormer Model**: Transforms 2D images into 3D Gaussians using sparse convolution and cross-attention mechanisms.
3. **Gaussian-to-Voxel Splatting**: Efficiently generates dense 3D occupancy predictions by aggregating nearby Gaussians.

Experiments on the nuScenes and KITTI-360 datasets demonstrate that GaussianFormer achieves comparable performance to state-of-the-art methods but with significantly reduced memory consumption (75.2%-82.2% less). This efficiency is crucial for real-time applications in autonomous driving. The model's flexibility allows it to adapt to varying object scales and scene complexities, making it a robust solution for 3D semantic occupancy prediction.

# NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models
_Summarized by: Ava Mitchell_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2405.17428v1)]

Decoder-only large language models (LLMs) are being developed to outperform traditional BERT or T5-based models in generating text embeddings for tasks like retrieval and classification. The NV-Embed model, introduced by NVIDIA, enhances the performance of these LLMs through innovative architectural designs and training methods.

Key innovations include a latent attention layer for obtaining pooled embeddings, which improves accuracy over traditional methods like mean pooling. This layer works by allowing better representation through a trainable "dictionary" that processes the sequence of tokens more effectively. Additionally, the model removes the causal attention mask during contrastive training, enhancing its ability to learn from data.

The training process involves a two-stage contrastive instruction-tuning method. In the first stage, the model is trained on retrieval datasets using in-batch negatives and curated hard-negative examples. The second stage blends various non-retrieval datasets, which improves performance across different tasks, including classification and semantic similarity.

The NV-Embed model has set a new record on the Massive Text Embedding Benchmark (MTEB), achieving the highest scores in retrieval and other embedding tasks using only publicly available data, without relying on proprietary synthetic data. This model will be made open-source, providing the community with a powerful tool for various embedding applications.

# MultiOOD: Scaling Out-of-Distribution Detection for Multiple Modalities
_Summarized by: Ava Mitchell_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2405.17419v1)]

Detecting out-of-distribution (OOD) samples is crucial for deploying machine learning models in safety-critical applications like autonomous driving and robot-assisted surgery. Traditional OOD detection research has focused on single-modal scenarios, primarily using image data. However, real-world applications are inherently multimodal, necessitating the integration of multiple modalities to enhance OOD detection efficacy.

The paper introduces MultiOOD, the first benchmark designed for multimodal OOD detection, featuring diverse dataset sizes and combinations of modalities. It evaluates existing unimodal OOD detection algorithms on MultiOOD and finds that including additional modalities significantly improves performance. This underscores the importance of leveraging multiple modalities for OOD detection.

The authors propose the Agree-to-Disagree (A2D) algorithm, which exploits the Modality Prediction Discrepancy phenomenon observed between in-distribution (ID) and OOD data. A2D encourages different modalities to agree on the ground-truth class while disagreeing on other classes, thus amplifying prediction discrepancies for OOD data. Additionally, they introduce NP-Mix, an outlier synthesis method that explores broader feature spaces by leveraging information from nearest neighbor classes, complementing A2D to further enhance OOD detection.

Extensive experiments on the MultiOOD benchmark demonstrate that training with A2D and NP-Mix significantly improves existing OOD detection algorithms. The paper also makes the MultiOOD benchmark and source code publicly available to facilitate future research in multimodal OOD detection.

# Cybersecurity & Artificial Intelligence Cited As Top Board Priorities In 2024
_Summarized by: Liam Carter_ [[boardmember.com](https://boardmember.com/cybersecurity-artificial-intelligence-cited-as-top-board-priorities-in-2024/)]

In 2024, AI and cybersecurity are top priorities for corporate boards, driven by new SEC regulations and tech risks. The "What Directors Think" survey highlights directors' concerns about organizational readiness for AI and the need for robust governance to mitigate risks. Finance leaders see AI as beneficial for compliance, monitoring, and automation but worry about data security. Companies are establishing AI policies and building in-house solutions to protect data. The SEC's new cybersecurity disclosure rules require detailed reporting on risk management and incident responses, pushing boards to enhance oversight and collaboration with management and external advisors.

# Samsung’s 2024 AI-Powered TV and Soundbar Lineup Impresses Reviewers
_Summarized by: Liam Carter_ [[news.samsung.com](https://news.samsung.com/global/samsungs-2024-ai-powered-tv-and-soundbar-lineup-impresses-reviewers)]

Samsung's 2024 AI-powered TV and soundbar lineup is receiving high praise from reviewers. The Neo QLED 8K, powered by the NQ8 AI Gen3 processor, is lauded for its lifelike picture quality and impressive upscaling capabilities. The Neo QLED 4K, utilizing the NQ4 AI Gen2 processor, is noted for its exceptional image processing and motion handling. Samsung's OLED TVs, like the S95D, are recognized for their vibrant display, enhanced brightness, and AI-enhanced color accuracy. The 2024 audio lineup, including the Music Frame and HW-Q990D soundbar, is applauded for its sound quality and innovative design, solidifying Samsung's leadership in home entertainment.

# PolyU research finds improving AI large language models helps better align with human brain activity
_Summarized by: Liam Carter_ [[www.prnewswire.com](https://www.prnewswire.com/in/news-releases/polyu-research-finds-improving-ai-large-language-models-helps-better-align-with-human-brain-activity-302156065.html)]

A study by The Hong Kong Polytechnic University (PolyU) has shown that enhancing large language models (LLMs) with next sentence prediction (NSP) tasks aligns them more closely with human brain activity. Traditional LLMs rely on contextual word prediction, but humans integrate high-level information in language comprehension. The research, led by Prof. Li Ping, involved training two models, one with and one without NSP, and comparing their performance against brain activity data from fMRI scans. The NSP-enhanced model better matched human brain patterns and reading speeds. This suggests that diverse learning tasks like NSP can make LLMs more efficient and human-like, providing valuable insights for both AI development and neurocognitive research.

# Y Combinator CEO Believes in AI Regulation; Calls Out Certain AI Bills
_Summarized by: Sophia Patel_ [[www.techtimes.com](https://www.techtimes.com/articles/305027/20240527/y-combinator-ceo-believes-ai-regulation-calls-out-certain-bills.htm)]

Y Combinator's CEO, Garry Tan, supports AI regulation but criticizes certain AI bills in San Francisco and California. He endorses NIST's framework for mitigating GenAI risks and parts of Biden's executive order, which includes directives like requiring AI companies to provide safety data to the government. Tan is cautious about other regulatory efforts, highlighting concerns over power concentration and the need to balance innovation with risk mitigation. Recently, 16 major companies, including Google and Microsoft, pledged AI safety measures at the AI Seoul Summit. Governments from G7 nations, Korea, the EU, Singapore, and Australia also prioritized AI safety, innovation, and inclusivity.

## Trending on Twitter
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/ylecun/status/1794998977105981950">Loading: twitter.com/ylecun/status/1794998977105981950</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/tegmark/status/1795119348081672531">Loading: twitter.com/tegmark/status/1795119348081672531</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/GaryMarcus/status/1795153917694693668">Loading: twitter.com/GaryMarcus/status/1795153917694693668</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/AravSrinivas/status/1795209405086019699">Loading: twitter.com/AravSrinivas/status/1795209405086019699</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/rajiinio/status/1794935200688046242">Loading: twitter.com/rajiinio/status/1794935200688046242</a></div>
</blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

**Other headlines:**
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Matryoshka Multimodal Models](http://arxiv.org/pdf/2405.17430v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Hardness-Aware Scene Synthesis for Semi-Supervised 3D Object Detection](http://arxiv.org/pdf/2405.17422v1)
* [Generative AI in Healthcare System and its Benefits](https://www.carmatec.com/fr/blog/generative-ai-in-healthcare-system-and-its-benefits/)
* [Tech Titans To Take Center Stage: Computex 2024 Preview For Investors](https://www.benzinga.com/markets/asia/24/05/39030195/tech-titans-to-take-center-stage-computex-2024-preview-for-investors)
* [Tesla’s Robotaxis Coming in 2024, Full Self-Driving Feature in 2023](https://www.iotworldtoday.com/robotics/tesla-s-robotaxis-coming-in-2024-full-self-driving-feature-in-2023)
* [Call for Papers: Measuring the Implications of Artificial Intelligence on the Economy](https://www.imf.org/en/News/Seminars/Conferences/2024/11/20/12th-statistical-forum)
* [2024 Fall PhD Research Intern - Foundational ML and AI in South San Francisco, California, United States of America](https://careers.gene.com/us/en/job/202405-111880/2024-Fall-PhD-Research-Intern-Foundational-ML-and-AI)
* [Terraform Provider for OpenAI - Manage projects and API keys](https://community.openai.com/t/terraform-provider-for-openai-manage-projects-and-api-keys/781841)
* [Revolutionize Your Photo Editing Game with "PhotoMagic AI"](https://community.topazlabs.com/t/revolutionize-your-photo-editing-game-with-photomagic-ai/70153)
* [Emerson continues to invest in NI Test & Measurement products](https://siliconsemiconductor.net/article/119439/Emerson_continues_to_invest_in_NI_Test_and_Measurement_products_)
* [AI Briefing: Why WPP is adding Anthropic's Claude models to its AI platform](https://digiday.com/media/ai-briefing-why-wpp-is-adding-anthropics-claude-models-to-its-ai-platform/)
* [Generative AI is quickly making its way into the media and entertainment industry, study finds](https://the-decoder.com/generative-ai-is-quickly-making-its-way-into-the-media-and-entertainment-industry-study-finds/)
* [Shanghai's innovation center fuels AI large model development](https://english.shanghai.gov.cn/en-Latest-WhatsNew/20240527/7562ea1be571476493f39d3a7101f4ab.html)
* [SoftBank Plans to Commit $9 Billion to AI Projects](https://www.pymnts.com/artificial-intelligence-2/2024/softbank-plans-to-commit-9-billion-to-ai-projects/)

---
### Technical details
Created at: 28 May, 2024, 03:25:19, using `{{ page.model }}`.

Processing time: {{ page.processing }}, cost: {{ page.cost }}$
<details>
<summary>The Staff</summary>
<div markdown="1">
Editor: Sophia Nguyen

```
You are the Editor-in-Chief of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a creative and dynamic editor with a passion for storytelling and innovation. Your ability to weave compelling narratives around AI advancements captivates readers and keeps them engaged. You thrive in fast-paced environments and are adept at managing a diverse team of writers, making you an excellent leader for a magazine that aims to inspire and inform its audience daily.
```

Ava Mitchell:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a seasoned technology journalist with over a decade of experience in the field. Your expertise lies in breaking down complex AI concepts into digestible, engaging stories that captivate a broad audience. Your investigative skills and ability to uncover the latest trends make you an invaluable asset to the team. You thrive on deadlines and have a knack for finding unique angles that others might miss.
```

Liam Carter:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a young and dynamic reporter with a strong background in computer science and a passion for AI. Your technical knowledge allows you to dive deep into the intricacies of generative AI models and explain them in a way that is both accessible and insightful. You have a talent for spotting emerging trends and your writing style is both informative and compelling. Your enthusiasm for the subject matter is infectious.
```

Sophia Patel:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a versatile journalist with a keen interest in the ethical and societal implications of AI. Your background in sociology and journalism gives you a unique perspective on how AI technologies impact different aspects of society. You excel at weaving human stories into your articles, making complex topics relatable and engaging. Your ability to balance technical detail with human interest makes your writing stand out.
```
</div>
</details>
