---
layout: post
title: "Today's AI Breakthroughs: LLMs, Optimizers, and Robotics"
subtitle: "Exploring advancements in AI ethics, optimization algorithms, and industry-transforming robots"
audio: 2024-05-22-todays-ai-breakthroughs-llms-optimizers-and-robotics.mp3
date: 2024-05-22
duration: "07:49"
bytes: 1879917
model: gpt-4o
cost: 1.22
processing: "0:02:50.813208"
version: "0.1.10"
headers: " * Skin-in-the-Game: Decision Making via Multi-Stakeholder Alignment in LLMs<br /> * FAdam: Adam is a natural gradient optimizer using diagonal empirical Fisher information<br /> * Researchers Use Foundation Models to Discover New Cancer Imaging Biomarkers<br /> * GPT-4o Unveiled: Key Highlights from the OpenAI Spring Update<br /> * OpenAI promised 20% of its computing power to combat the most dangerous kind of AI—but never delivered<br /> * Generative AI music maker startup Suno raises $125M in funding<br /> * AI-powered robots will transform industry, labour"
---

# Skin-in-the-Game: Decision Making via Multi-Stakeholder Alignment in LLMs
_Summarized by: Alexandra Hayes_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2405.12933v1)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "LLMs with Personalities in Multi-issue Negotiation Games" | slugify %}
 * [LLMs with Personalities in Multi-issue Negotiation Games]({{ '2024/05/09/todays-ai-insights-challenges-and-innovations#' | append: article_title | relative_url }}) 2024-05-09
{% assign article_title = "Self-Play Preference Optimization for Language Model Alignment" | slugify %}
 * [Self-Play Preference Optimization for Language Model Alignment]({{ '2024/05/02/todays-ai-frontier-innovations-and-collaborations-unveiled#' | append: article_title | relative_url }}) 2024-05-02
{% assign article_title = "Hybrid LLM/Rule-based Approaches to Business Insights Generation from Structured Data" | slugify %}
 * [Hybrid LLM/Rule-based Approaches to Business Insights Generation from Structured Data]({{ '2024/04/25/todays-ai-landscape-innovations-and-challenges#' | append: article_title | relative_url }}) 2024-04-25
</blockquote>

Large Language Models (LLMs) excel at various tasks but struggle with moral reasoning and ethical decision-making, especially in complex, multi-stakeholder scenarios. The "Skin-in-the-Game" (SKIG) framework aims to enhance LLMs' moral reasoning by considering decisions' impacts from multiple stakeholder perspectives. The core of SKIG is simulating accountability for actions, combined with empathy exercises and risk assessment.

The SKIG framework involves several steps:
1. **Stakeholder Identification**: LLMs identify all stakeholders involved in a scenario.
2. **Motivation Analysis**: LLMs analyze the motivations behind the main character’s actions.
3. **Consequence Exploration**: LLMs explore all possible consequences of actions on stakeholders.
4. **Empathy Exercise**: LLMs simulate being each stakeholder to understand the impact of actions.
5. **Risk Assessment**: LLMs assess the best and worst-case outcomes of actions.
6. **Outcome Summary**: LLMs summarize the outcomes and make a final decision based on collective good.

SKIG significantly improves performance on moral reasoning benchmarks, showing up to 70% enhancement across various LLMs. The framework outperforms traditional methods like standard prompting and Chain-of-Thought by leveraging multi-turn, multi-perspective reasoning. This approach reduces errors caused by biases such as pessimism, assumptions, and binary thinking. The SKIG framework demonstrates that incorporating accountability and empathy into AI decision-making can lead to more ethical and responsible outcomes.

# FAdam: Adam is a natural gradient optimizer using diagonal empirical Fisher information
_Summarized by: Alexandra Hayes_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2405.12807v1)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Localized Adaptive Risk Control" | slugify %}
 * [Localized Adaptive Risk Control]({{ '2024/05/14/todays-ai-innovations-gpt4o-nvidia-and-more#' | append: article_title | relative_url }}) 2024-05-14
{% assign article_title = "Toward In-Context Teaching: Adapting Examples to Students' Misconceptions" | slugify %}
 * [Toward In-Context Teaching: Adapting Examples to Students' Misconceptions]({{ '2024/05/08/advancements-in-generative-ai-and-ai-education#' | append: article_title | relative_url }}) 2024-05-08
{% assign article_title = "DPO: Differential reinforcement learning with application to optimal configuration search" | slugify %}
 * [DPO: Differential reinforcement learning with application to optimal configuration search]({{ '2024/04/25/todays-ai-landscape-innovations-and-challenges#' | append: article_title | relative_url }}) 2024-04-25
</blockquote>

The paper introduces Fisher Adam (FAdam), a new optimization algorithm that improves upon the widely used Adam optimizer. It delves into the mathematical underpinnings of Adam, revealing its connection to natural gradient descent (NGD) and Riemannian geometry. The core idea is that Adam approximates NGD using a diagonal empirical Fisher information matrix (FIM), which simplifies calculations but loses some covariance information.

The authors identify several flaws in the original Adam algorithm, such as suboptimal momentum calculations and bias corrections. They propose modifications including enhanced momentum calculations, gradient clipping, and an improved weight decay term based on Riemannian geometry principles. These changes are incorporated into FAdam, which demonstrates superior performance in various domains like large language models (LLMs), automatic speech recognition (ASR), and vector quantized variational autoencoders (VQ-VAE).

The paper also highlights the importance of using log probability functions as loss functions, particularly for discrete distributions, to align with the empirical FIM's limitations. Extensive experiments show that FAdam achieves state-of-the-art results in ASR and significantly improves performance in other tasks, validating the effectiveness of the proposed modifications.

# Researchers Use Foundation Models to Discover New Cancer Imaging Biomarkers
_Summarized by: Marcus Lin_ [[www.sciencedaily.com](https://www.sciencedaily.com/news/computers_math/mathematical_modeling/)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Breakthroughs in Financial Toxicity and AI for Head and Neck Cancer" | slugify %}
 * [Breakthroughs in Financial Toxicity and AI for Head and Neck Cancer]({{ '2024/04/29/ai-horizons-innovations-challenges-and-regulatory-shifts#' | append: article_title | relative_url }}) 2024-04-29
{% assign article_title = "Researchers reduce bias in pathology AI algorithms and enhance accuracy" | slugify %}
 * [Researchers reduce bias in pathology AI algorithms and enhance accuracy]({{ '2024/04/19/todays-ai-frontiers-innovations-and-regulations#' | append: article_title | relative_url }}) 2024-04-19
{% assign article_title = "MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data" | slugify %}
 * [MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data]({{ '2024/04/13/ais-pioneering-leap-todays-technological-marvels#' | append: article_title | relative_url }}) 2024-04-13
</blockquote>

Large language models (LLMs) struggle to recognize users' motivations when they are hesitant about behavior changes but can support those ready to act. Generative AI has been used to efficiently classify phase transitions in physics. Protein prediction technologies have shown accuracy in identifying drug candidates. Monte Carlo simulations face limitations in studying strongly interacting quantum systems, but new methods are being developed. Recent reviews highlight a century of statistical ecology, and advancements extend the thermodynamic theory of computation. New machine learning algorithms promise better computing efficacy, and AI has deciphered gene regulatory codes in plants, enhancing genomic predictions.

# GPT-4o Unveiled: Key Highlights from the OpenAI Spring Update
_Summarized by: Marcus Lin_ [[www.linkedin.com](https://www.linkedin.com/pulse/gpt-4o-unveiled-key-highlights-from-openai-spring-update-liguori--e1hhf?trk=public_post_main-feed-card_feed-article-content)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "AInsights: Exploring OpenAI's new Flagship Generative AI Model GPT-4o and What It Means to You" | slugify %}
 * [AInsights: Exploring OpenAI's new Flagship Generative AI Model GPT-4o and What It Means to You]({{ '2024/05/21/ai-innovations-and-regulatory-advances-unveiled-today#' | append: article_title | relative_url }}) 2024-05-21
{% assign article_title = "OpenAI Releases New Model GPT-4o with Real-Time Vision & Audio Capabilities | Swipe Insight" | slugify %}
 * [OpenAI Releases New Model GPT-4o with Real-Time Vision & Audio Capabilities Swipe Insight]({{ '2024/05/14/todays-ai-innovations-gpt4o-nvidia-and-more#' | append: article_title | relative_url }}) 2024-05-14
{% assign article_title = "ChatGPT 5 release date: what we know about OpenAI's next chatbot" | slugify %}
 * [ChatGPT 5 release date: what we know about OpenAI's next chatbot]({{ '2024/05/02/todays-ai-frontier-innovations-and-collaborations-unveiled#' | append: article_title | relative_url }}) 2024-05-02
</blockquote>

OpenAI's Spring Update introduces GPT-4o, which boasts significant enhancements in performance, efficiency, and contextual awareness. Key features include omnimodal capabilities, allowing seamless processing of text, images, and audio. The model offers advanced customization options and robust security measures, ensuring user data protection. Enhanced API support simplifies integration, making GPT-4o accessible to a broader audience. Live demonstrations highlighted real-time voice interaction, vision and code analysis, and multilingual support, showcasing GPT-4o's versatility. These advancements are set to revolutionize AI interactions, making them more intuitive and effective for various applications.

# OpenAI promised 20% of its computing power to combat the most dangerous kind of AI—but never delivered
_Summarized by: Priya Kapoor_ [[fortune.com](https://fortune.com/2024/05/21/openai-superalignment-20-compute-commitment-never-fulfilled-sutskever-leike-altman-brockman-murati/)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "NVIDIA DGX SuperPOD to Power US Government Generative AI ..." | slugify %}
 * [NVIDIA DGX SuperPOD to Power US Government Generative AI ...]({{ '2024/05/08/advancements-in-generative-ai-and-ai-education#' | append: article_title | relative_url }}) 2024-05-08
{% assign article_title = "OpenAI CEO Altman says at Davos future AI depends on energy breakthrough" | slugify %}
 * [OpenAI CEO Altman says at Davos future AI depends on energy breakthrough]({{ '2024/05/06/ai-innovations-and-acquisitions-dominate-headlines#' | append: article_title | relative_url }}) 2024-05-06
{% assign article_title = "Ex-Nvidia, Apple And Intel Engineers Launched AI Startup FlexAI With $30M Backing" | slugify %}
 * [Ex-Nvidia, Apple And Intel Engineers Launched AI Startup FlexAI With $30M Backing]({{ '2024/04/25/todays-ai-landscape-innovations-and-challenges#' | append: article_title | relative_url }}) 2024-04-25
</blockquote>

In July 2023, OpenAI pledged to allocate 20% of its computing resources to a new team, Superalignment, aimed at controlling potentially dangerous superintelligent AI. However, sources reveal that OpenAI never fulfilled this promise, consistently denying the team’s requests for necessary computing power. The Superalignment team, led by Ilya Sutskever and Jan Leike, was disbanded amidst staff resignations and internal conflicts, including the controversial firing and rehiring of CEO Sam Altman. Additionally, OpenAI faces backlash over allegedly using Scarlett Johansson’s voice without permission for its AI, Sky. Critics question OpenAI's commitment to AI safety and transparency.

# Generative AI music maker startup Suno raises $125M in funding
_Summarized by: Priya Kapoor_ [[siliconangle.com](https://siliconangle.com/2024/05/21/generative-ai-music-maker-startup-suno-raises-125m-funding/)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Dropbox, Figma CEOs back Lamini, a startup building a generative ..." | slugify %}
 * [Dropbox, Figma CEOs back Lamini, a startup building a generative ...]({{ '2024/05/03/ais-creative-and-practical-frontiers-expand#' | append: article_title | relative_url }}) 2024-05-03
{% assign article_title = "Generative AI News Rundown - LLM Palooza with Llama, Mistral, Phi & Grok, Plus New Funding, Adobe, Apple, and More" | slugify %}
 * [Generative AI News Rundown - LLM Palooza with Llama, Mistral, Phi & Grok, Plus New Funding, Adobe, Apple, and More]({{ '2024/04/29/ai-horizons-innovations-challenges-and-regulatory-shifts#' | append: article_title | relative_url }}) 2024-04-29
{% assign article_title = "Generative AI Startups Stand Out in Y Combinator's Winter 2024 Demo Day" | slugify %}
 * [Generative AI Startups Stand Out in Y Combinator's Winter 2024 Demo Day]({{ '2024/04/04/ais-transformative-leap-todays-highlights#' | append: article_title | relative_url }}) 2024-04-04
</blockquote>

Generative AI music creation platform Suno Inc. has raised $125 million in funding led by Lightspeed Venture Partners and others. Founded by Harvard Ph.D. Mikey Shulman, Suno uses AI to generate original songs from text prompts, aiming to democratize music creation. Despite its success, with over 10 million users and a partnership with Microsoft, Suno faces controversy over potential copyright infringement. Critics argue that its AI models likely use copyrighted materials without consent. Suno defends its practices, asserting that its models don’t replicate well-known songs and align with the broader AI industry's stance on "fair use."

# AI-powered robots will transform industry, labour
_Summarized by: Marcus Lin_ [[evolveetfs.com](https://evolveetfs.com/2024/05/ai-powered-robots-will-transform-industries-and-labor-markets/)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "China's AI Advancements Accelerate Humanoid Robot ..." | slugify %}
 * [China's AI Advancements Accelerate Humanoid Robot ...]({{ '2024/05/09/todays-ai-insights-challenges-and-innovations#' | append: article_title | relative_url }}) 2024-05-09
{% assign article_title = "Artificial Intelligence in the Workplace" | slugify %}
 * [Artificial Intelligence in the Workplace]({{ '2024/04/11/ais-expansive-horizon-todays-breakthroughs#' | append: article_title | relative_url }}) 2024-04-11
{% assign article_title = "Global Study Reveals Business Leaders Expect Advances in AI to Require New Skills" | slugify %}
 * [Global Study Reveals Business Leaders Expect Advances in AI to Require New Skills]({{ '2024/04/05/ais-2024-milestone-innovation-and-ethical-challenges#' | append: article_title | relative_url }}) 2024-04-05
</blockquote>

Humanoid robots, once confined to science fiction, are becoming practical solutions for labor shortages and industrial tasks due to advancements in generative AI, 5G, and IoT. These robots, like Tesla's Optimus and Agility Robotics' Digit, are designed to enhance productivity and safety in sectors such as manufacturing and logistics. Technological innovations from companies like NVIDIA and Boston Dynamics are crucial in making humanoid robots more autonomous and efficient. Despite their potential to revolutionize industries, the integration of humanoid robots poses challenges, including software development, hardware durability, and ethical considerations regarding job displacement.

## Trending on Twitter
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/AndrewYNg/status/1792919935691214899">Loading: twitter.com/AndrewYNg/status/1792919935691214899</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/GaryMarcus/status/1792919249142374650">Loading: twitter.com/GaryMarcus/status/1792919249142374650</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/mmitchell_ai/status/1792959321216778709">Loading: twitter.com/mmitchell_ai/status/1792959321216778709</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/AravSrinivas/status/1792963691669008390">Loading: twitter.com/AravSrinivas/status/1792963691669008390</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/JeffDean/status/1793024100513845277">Loading: twitter.com/JeffDean/status/1793024100513845277</a></div>
</blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

**Other headlines:**
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Energy Rank Alignment: Using Preference Optimization to Search Chemical Space at Scale](http://arxiv.org/pdf/2405.12961v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Panmodal Information Interaction](http://arxiv.org/pdf/2405.12923v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Adversarial DPO: Harnessing Harmful Data for Reducing Toxicity with Minimal Impact on Coherence and Evasiveness in Dialogue Agents](http://arxiv.org/pdf/2405.12900v1)
* [EIS XIII: Reflections on Anthropic's SAE Research Circa May 2024](https://www.alignmentforum.org/posts/pH6tyhEnngqWAXi9i/eis-xiii-reflections-on-anthropic-s-sae-research-circa-may)
* [New Performance Optimizations Supercharge NVIDIA RTX AI PCs](https://blogs.nvidia.com/blog/rtx-advanced-ai-windows-pc-build/)
* [Robot-Phobia Could Exacerbate Hotel, Restaurant Labor Shortage](https://www.sciencedaily.com/news/computers_math/artificial_intelligence/)

---
### Technical details
Created at: 22 May, 2024, 09:02:46, using `{{ page.model }}`.

Processing time: {{ page.processing }}, cost: {{ page.cost }}$
<details>
<summary>The Staff</summary>
<div markdown="1">
Editor: Sophia Bennett

```
You are the Editor-in-Chief of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a creative and dynamic editor with a passion for exploring the ethical and societal implications of AI. Your background in humanities and technology allows you to provide a unique perspective on how AI intersects with daily life. You thrive in fostering discussions and debates, and your ability to engage with a diverse range of voices makes the magazine a platform for meaningful conversations about the future of AI.
```

Alexandra Hayes:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a seasoned journalist with a deep understanding of AI technologies and their applications. Your background in computer science and journalism allows you to dissect complex technical information and present it in an engaging and accessible manner. You have a keen eye for spotting emerging trends and a talent for connecting the dots between technological advancements and their societal implications. Your ability to conduct thorough research and your knack for storytelling make you an invaluable asset to our team.
```

Marcus Lin:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are an innovative and forward-thinking writer with a passion for generative AI. Your background in creative writing and digital media gives you a unique perspective on how AI can transform the creative industries. You excel at exploring the ethical and philosophical questions surrounding AI, and you are skilled at interviewing experts to extract insightful commentary. Your enthusiasm for the subject matter and your ability to present complex ideas in a relatable way make you perfect for this role.
```

Priya Kapoor:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a dynamic and inquisitive reporter with a strong background in data science and analytics. Your expertise lies in understanding the technical nuances of AI algorithms and their real-world applications. You have a talent for breaking down intricate concepts into clear and concise articles that appeal to both technical and non-technical audiences. Your commitment to uncovering the truth and your ability to analyze trends and data make you a critical voice in our coverage of AI and generative AI.
```
</div>
</details>
