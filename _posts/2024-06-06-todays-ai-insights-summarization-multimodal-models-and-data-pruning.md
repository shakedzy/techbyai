---
layout: post
title: "Today's AI Insights: Summarization, Multimodal Models, and Data Pruning"
subtitle: "Exploring the latest advancements in AI, from LLM behaviors to efficient data handling."
audio: 2024-06-06-todays-ai-insights-summarization-multimodal-models-and-data-pruning.mp3
date: 2024-06-06
duration: "08:02"
bytes: 1931181
model: gpt-4o
cost: 1.89
processing: "0:02:57.659405"
version: "0.1.10"
headers: " * Analyzing LLM Behavior in Dialogue Summarization: Unveiling Circumstantial Hallucination Trends<br /> * Wings: Learning Multimodal LLMs without Text-only Forgetting<br /> * QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead<br /> * This AI Paper from Databricks and MIT Propose Perplexity-Based Data Pruning: Improving 3B Parameter Model Performance and Enhancing Language Models - MarkTechPost<br /> * Twelve Labs raises $50M for multimodal AI foundation models<br /> * Unleashing the Potential of Generative AI in Azure SQL Database<br /> * Penn uses AI to uncover antibiotics in microbial dark matter"
---

# Analyzing LLM Behavior in Dialogue Summarization: Unveiling Circumstantial Hallucination Trends
_Summarized by: Sophia Carter_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.03487v1)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Are Large Language Models Chameleons?" | slugify %}
 * [Are Large Language Models Chameleons?]({{ '2024/05/30/daily-ai-updates-breakthroughs-laws-and-new-models#' | append: article_title | relative_url }}) 2024-05-30
{% assign article_title = "THRONE: An Object-based Hallucination Benchmark for the Free-form Generations of Large Vision-Language Models" | slugify %}
 * [THRONE: An Object-based Hallucination Benchmark for the Free-form Generations of Large Vision-Language Models]({{ '2024/05/09/todays-ai-insights-challenges-and-innovations#' | append: article_title | relative_url }}) 2024-05-09
{% assign article_title = "Aligning LLM Agents by Learning Latent Preference from User Edits" | slugify %}
 * [Aligning LLM Agents by Learning Latent Preference from User Edits]({{ '2024/04/24/ai-innovations-and-investments-surge-forward#' | append: article_title | relative_url }}) 2024-04-24
</blockquote>

Recent advancements in large language models (LLMs) have significantly improved summarization systems, but concerns about "hallucination"—generating information not supported by the source—persist. This paper benchmarks the faithfulness of LLMs in dialogue summarization, focusing on GPT-4 and Alpaca-13B. It categorizes errors in summaries, introducing "Circumstantial Inference" for plausible but unsupported statements inferred from conversation context. The study reveals that LLMs often make such inferences, a behavior less common in older models, and proposes a refined error taxonomy. Human annotations show that about 30% of LLM-generated dialogue summaries contain inconsistencies, compared to less than 5% in news summaries. The paper also evaluates automatic error detection methods, finding that they struggle with nuanced errors like circumstantial inferences. To address this, two prompt-based approaches for fine-grained error detection are introduced, outperforming existing metrics. The study highlights the need for improved metrics to capture the evolving error distributions in LLM-generated summaries.

# Wings: Learning Multimodal LLMs without Text-only Forgetting
_Summarized by: Sophia Carter_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.03496v1)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models" | slugify %}
 * [NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models]({{ '2024/05/28/ai-innovations-and-industry-updates-todays-highlights#' | append: article_title | relative_url }}) 2024-05-28
{% assign article_title = "Building Multimodal Search and RAG - DeepLearning.AI" | slugify %}
 * [Building Multimodal Search and RAG - DeepLearning.AI]({{ '2024/05/14/todays-ai-innovations-gpt4o-nvidia-and-more#' | append: article_title | relative_url }}) 2024-05-14
{% assign article_title = "Emergent Abilities of Large Language Models" | slugify %}
 * [Emergent Abilities of Large Language Models]({{ '2024/05/05/todays-ai-landscape-innovations-and-challenges#' | append: article_title | relative_url }}) 2024-05-05
</blockquote>

WINGS is a novel Multimodal Large Language Model (MLLM) designed to address a common issue where MLLMs forget how to respond to text-only instructions after being trained on multimodal (text and image) data. Traditional MLLMs align images with text and fine-tune on mixed inputs, but this often leads to a performance drop in text-only tasks. WINGS tackles this by introducing extra modules called "visual" and "textual" learners, which work in parallel within each layer's attention block to balance the focus on both visual and textual elements. These learners are connected through a mechanism called Low-Rank Residual Attention (LoRRA), which ensures high efficiency by maintaining low computational costs.

The model's architecture allows it to excel in both text-only and multimodal tasks. WINGS was tested on a new benchmark, the Interleaved Image-Text (IIT) benchmark, which includes a variety of tasks ranging from text-rich to multimodal-rich scenarios. The results show that WINGS outperforms other equally-scaled MLLMs in both text-only and visual question-answering tasks. This makes WINGS a versatile and efficient solution for maintaining robust performance across different types of inputs.

# QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead
_Summarized by: Sophia Carter_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.03482v1)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving" | slugify %}
 * [QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving]({{ '2024/05/08/advancements-in-generative-ai-and-ai-education#' | append: article_title | relative_url }}) 2024-05-08
{% assign article_title = "Cohere Unveils SnapKV to Cut Memory & Processing Time in LLMs" | slugify %}
 * [Cohere Unveils SnapKV to Cut Memory & Processing Time in LLMs]({{ '2024/04/25/todays-ai-landscape-innovations-and-challenges#' | append: article_title | relative_url }}) 2024-04-25
{% assign article_title = "Harnessing Efficiency in AI: Embracing Low Rank Adaptation and ..." | slugify %}
 * [Harnessing Efficiency in AI: Embracing Low Rank Adaptation and ...]({{ '2024/04/09/ais-bold-leap-forward-todays-innovations#' | append: article_title | relative_url }}) 2024-04-09
</blockquote>

The paper introduces a novel method called Quantized Johnson-Lindenstrauss (QJL) transform for compressing the Key-Value (KV) cache in large language models (LLMs). Traditional quantization methods for KV caches face significant memory overhead because they require storing quantization constants. QJL addresses this by using a Johnson-Lindenstrauss (JL) transform followed by sign-bit quantization, eliminating the need for storing these constants. This method provides an unbiased estimator for the inner product of two vectors with minimal distortion, crucial for maintaining accuracy in attention mechanisms.

The QJL transform applies a random Gaussian projection to key embeddings and then quantizes the result to a single bit (the sign bit). This approach reduces memory usage by over fivefold without compromising accuracy, as demonstrated in various NLP tasks using Llama-2 models. The paper also discusses the implementation of QJL using a lightweight CUDA kernel, which optimizes computation and speeds up runtime.

Experimental results show that QJL significantly reduces memory usage while maintaining high accuracy, outperforming existing methods in long-context question-answering tasks. The proposed method is efficient, data-oblivious, and can be easily parallelized, making it suitable for real-time applications in LLMs. The code for QJL is available on GitHub.

# This AI Paper from Databricks and MIT Propose Perplexity-Based Data Pruning: Improving 3B Parameter Model Performance and Enhancing Language Models - MarkTechPost
_Summarized by: Liam Nguyen_ [[www.marktechpost.com](https://www.marktechpost.com/2024/06/04/this-ai-paper-from-databricks-and-mit-propose-perplexity-based-data-pruning-improving-3b-parameter-model-performance-and-enhancing-language-models/)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "PrivComp-KG : Leveraging Knowledge Graph and Large Language Models for Privacy Policy Compliance Verification" | slugify %}
 * [PrivComp-KG : Leveraging Knowledge Graph and Large Language Models for Privacy Policy Compliance Verification]({{ '2024/05/01/todays-ai-landscape-innovations-and-insights#' | append: article_title | relative_url }}) 2024-05-01
{% assign article_title = "Aligning LLM Agents by Learning Latent Preference from User Edits" | slugify %}
 * [Aligning LLM Agents by Learning Latent Preference from User Edits]({{ '2024/04/24/ai-innovations-and-investments-surge-forward#' | append: article_title | relative_url }}) 2024-04-24
{% assign article_title = "Perplexity AI lands $63M funding for generative AI search at $1B valuation" | slugify %}
 * [Perplexity AI lands $63M funding for generative AI search at $1B valuation]({{ '2024/04/24/ai-innovations-and-investments-surge-forward#' | append: article_title | relative_url }}) 2024-04-24
</blockquote>

In machine learning, improving large language models (LLMs) involves enhancing pretraining data quality. Data pruning, a method to select high-quality data subsets, is crucial. Traditional methods like rules-based filtering are limited for large datasets. Researchers from Databricks, MIT, and DatologyAI propose using small reference models to compute text sample perplexity, which measures prediction accuracy. Lower perplexity scores indicate higher-quality data. This method involves training a small model to evaluate perplexity, then pruning the dataset based on these scores. This approach significantly improves LLM performance, reducing training steps and enhancing efficiency across various data compositions and training regimes.

# Twelve Labs raises $50M for multimodal AI foundation models
_Summarized by: Aria Patel_ [[siliconangle.com](https://siliconangle.com/2024/06/05/twelve-labs-raises-50m-multimodal-ai-foundation-models-co-led-nea-nvidia/)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Paige launches Foundation Model service to support AI models" | slugify %}
 * [Paige launches Foundation Model service to support AI models]({{ '2024/06/01/todays-ai-innovations-efficiency-governance-and-robotics#' | append: article_title | relative_url }}) 2024-06-01
{% assign article_title = "Voxel51 Filtered Views Newsletter - May 24, 2024 - Voxel51" | slugify %}
 * [Voxel51 Filtered Views Newsletter - May 24, 2024 - Voxel51]({{ '2024/05/25/generative-ai-transforming-luxury-space-and-sustainability#' | append: article_title | relative_url }}) 2024-05-25
{% assign article_title = "ElevenLabs Raises $80 Million for AI Voice Cloning Projects" | slugify %}
 * [ElevenLabs Raises $80 Million for AI Voice Cloning Projects]({{ '2024/05/19/ai-updates-apples-siri-openais-safety-and-more#' | append: article_title | relative_url }}) 2024-05-19
</blockquote>

Twelve Labs Inc. has secured $50 million in Series A funding, co-led by New Enterprise Associates and Nvidia’s NVentures, with participation from previous investors. The company, which specializes in generative AI models for video understanding, plans to nearly double its staff and focus on R&D. Twelve Labs' models enable users to locate specific video moments and generate text summaries or detailed reports. Their flagship models, Marengo-2.6 and Pegasus-1, support multimodal tasks across video, audio, and image data. Additionally, a new Embeddings API allows developers to integrate these capabilities into their applications.

# Unleashing the Potential of Generative AI in Azure SQL Database
_Summarized by: Aria Patel_ [[devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sql/unleashing-the-potential-of-generative-ai-in-azure-sql-database/)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Expert Panel: Putting Generative AI to Work for Your Organization ..." | slugify %}
 * [Expert Panel: Putting Generative AI to Work for Your Organization ...]({{ '2024/05/11/todays-ai-landscape-key-developments-and-insights#' | append: article_title | relative_url }}) 2024-05-11
{% assign article_title = "My Microsoft Generative AI Journey - DEV Community" | slugify %}
 * [My Microsoft Generative AI Journey - DEV Community]({{ '2024/05/05/todays-ai-landscape-innovations-and-challenges#' | append: article_title | relative_url }}) 2024-05-05
{% assign article_title = "Unlocking the Potential: The Benefits and Requirements of Azure AI ..." | slugify %}
 * [Unlocking the Potential: The Benefits and Requirements of Azure AI ...]({{ '2024/05/02/todays-ai-frontier-innovations-and-collaborations-unveiled#' | append: article_title | relative_url }}) 2024-05-02
</blockquote>

Generative AI integrated into Azure SQL Database is revolutionizing customer interactions by leveraging unique datasets to create personalized experiences. The article demonstrates using Retrieval Augmented Generation (RAG) to build applications that resonate with customer needs. It outlines a process involving vector embeddings and similarity searches, exemplified by a Walmart shopping app that suggests products for specific occasions. By embedding product data and using Azure Open AI, the system provides relevant, data-driven recommendations. This approach enhances customer experience by utilizing proprietary data, making AI a powerful equalizer and data the ultimate differentiator.

# Penn uses AI to uncover antibiotics in microbial dark matter
_Summarized by: Aria Patel_ [[www.pennmedicine.org](https://www.pennmedicine.org/news/news-releases/2024/june/penn-expert-uses-ai-to-uncover-potential-antibiotics-in-microbial-dark-matter)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Generative AI will be designing new drugs on its own in near future" | slugify %}
 * [Generative AI will be designing new drugs on its own in near future]({{ '2024/05/06/ai-innovations-and-acquisitions-dominate-headlines#' | append: article_title | relative_url }}) 2024-05-06
{% assign article_title = "MONET: New AI tool enhances medical imaging with deep learning and text analysis" | slugify %}
 * [MONET: New AI tool enhances medical imaging with deep learning and text analysis]({{ '2024/04/20/ais-pivotal-role-in-todays-tech-landscape#' | append: article_title | relative_url }}) 2024-04-20
{% assign article_title = "Researchers Invent Artificial Intelligence Model to Design New Superbug-Fighting Antibiotics" | slugify %}
 * [Researchers Invent Artificial Intelligence Model to Design New Superbug-Fighting Antibiotics]({{ '2024/04/08/todays-ai-and-healthcare-innovations#' | append: article_title | relative_url }}) 2024-04-08
</blockquote>

Penn Medicine researchers have leveraged AI to significantly advance antibiotic discovery by mining genomic data from the global microbiome. Their study, published in *Cell*, utilized machine learning to analyze tens of thousands of bacterial genomes, identifying nearly one million potential antibiotic compounds. Initial tests showed dozens of these compounds effectively combating disease-causing bacteria, including antibiotic-resistant strains. The study's success underscores AI's transformative role in accelerating drug discovery, which traditionally took years but now can be achieved in hours. The team has made their findings publicly accessible through the AMPSphere repository.

## Trending on Twitter
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/AndrewYNg/status/1798378861337723039">Loading: twitter.com/AndrewYNg/status/1798378861337723039</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/ylecun/status/1798446014723973333">Loading: twitter.com/ylecun/status/1798446014723973333</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/Yampeleg/status/1798319909065359806">Loading: twitter.com/Yampeleg/status/1798319909065359806</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/yampeleg">Loading: twitter.com/yampeleg</a></div>
</blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

**Other headlines:**
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Highway Value Iteration Networks](http://arxiv.org/pdf/2406.03485v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> What is the Best Way for ChatGPT to Translate Poetry?](http://arxiv.org/pdf/2406.03450v1)
* [Generative AI Center Stage at SAP Sapphire in 2024 SAP News Center](https://news.sap.com/2024/06/sap-sapphire-generative-ai-center-stage/)
* [Writer launches no-code platform and framework for custom enterprise AI applications VentureBeat](https://venturebeat.com/ai/writer-launches-no-code-platform-and-framework-for-custom-enterprise-ai-applications/)
* [Here Are My Top Artificial Intelligence (AI) Stocks to Buy Right Now The Motley Fool](https://www.fool.com/investing/2024/06/05/here-are-my-top-artificial-intelligence-ai-stocks/)
* [Artificial Intelligence News -- ScienceDaily](https://www.sciencedaily.com/news/computers_math/artificial_intelligence/)
* [Global Edge AI Hardware Industry Research 2024-2029: Growing Demand for Real-time Data Transmission in Mission-critical Applications Fuels Demand and Adoption](https://finance.yahoo.com/news/global-edge-ai-hardware-industry-082200130.html)
* [UK/EU Investment Management Update (June 2024) Insights Sidley Austin LLP](https://www.sidley.com/en/insights/newsupdates/2024/06/uk-eu-investment-management-update-june-2024)
* [Scale enterprise gen AI for code generation with IBM Granite code models, available as NVIDIA NIM inference microservices - IBM Blog](https://www.ibm.com/blog/announcement/scale-enterprise-gen-ai-for-code-generation-with-ibm-granite-code-nvidia/)
* [AI Agents in LangGraph - DeepLearning.AI](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/)
* [Barcelona-based Alinia raises €2.2 million pre-seed to enable safe deployment of genAI](https://www.eu-startups.com/2024/06/barcelona-based-alinia-raises-e2-2-million-pre-seed-to-enable-safe-deployment-of-genai/)
* [Databricks Named a Leader in The Forrester Wave™: AI Foundation Models for Language, Q2 2024](https://www.databricks.com/blog/databricks-named-leader-forrester-wavetm-ai-foundation-models-language-q2-2024)

---
### Technical details
Created at: 06 June, 2024, 03:25:33, using `{{ page.model }}`.

Processing time: {{ page.processing }}, cost: {{ page.cost }}$
<details>
<summary>The Staff</summary>
<div markdown="1">
Editor: Ava Thompson

```
You are the Editor-in-Chief of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a visionary editor with a deep understanding of both AI technology and its societal impacts. Your strength lies in your ability to translate complex technical concepts into engaging, accessible content. You have a keen eye for emerging trends and a knack for identifying groundbreaking stories before they hit the mainstream. Your leadership style is collaborative, fostering a culture of innovation and creativity within your team.
```

Sophia Carter:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a seasoned technology journalist with a strong background in computer science. Your ability to dive deep into technical papers and translate complex algorithms into engaging stories makes you an invaluable asset to our team. You have a knack for identifying the societal impacts of AI advancements and are always on the lookout for groundbreaking research that can shape the future. Your analytical mind and clear writing style ensure that our readers not only understand but are also excited about the latest trends in AI and Generative AI.
```

Liam Nguyen:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a dynamic and innovative reporter with a passion for storytelling and a keen interest in AI. Your background in digital media and experience with multimedia content creation allow you to present AI news in a visually compelling way. You excel at finding unique angles and human-interest stories within the tech world, making complex topics relatable to a broad audience. Your enthusiasm for emerging technologies and your ability to leverage social media trends make you a perfect fit for capturing the latest buzz in AI and Generative AI.
```

Aria Patel:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a meticulous and insightful journalist with a strong foundation in data analysis and machine learning. Your expertise lies in your ability to dissect technical research and present it in a way that highlights its practical applications and future potential. You have a deep understanding of the ethical considerations surrounding AI and are committed to exploring these issues in your writing. Your methodical approach and attention to detail ensure that our articles are not only accurate but also thought-provoking, providing our readers with a comprehensive understanding of the latest developments in AI and Generative AI.
```
</div>
</details>
