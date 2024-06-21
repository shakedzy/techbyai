---
layout: post
title: "Today's Top AI Updates: Investments, Innovations, and Regulations"
subtitle: "Bezos and Nvidia invest in robots, Anthropic's new model, and California's AI regulations"
audio: 2024-06-21-todays-top-ai-updates-investments-innovations-and-regulations.mp3
date: 2024-06-21
duration: "08:19"
bytes: 1997037
model: gpt-4o
cost: 1.33
processing: "0:02:48.776640"
version: "0.1.12"
headers: " * Bezos, Nvidia Invest in Humanoid Robot Startup<br /> * Connecting the Dots: LLMs can Infer and Verbalize Latent Structure from Disparate Training Data<br /> * Anthropic's Claude 3.5 Sonnet outperforms OpenAI and Google in ...<br /> * Could AI reject your resume? California tries to prevent a new kind of discrimination<br /> * Research into 'hallucinating' generative models advances reliability of artificial intelligence<br /> * Whiteboard-of-Thought: Thinking Step-by-Step Across Modalities<br /> * Function-Calling and Data Extraction with LLMs - DeepLearning.AI"
---

# Bezos, Nvidia Invest in Humanoid Robot Startup
_Summarized by: Marcus Tan_ [[www.iotworldtoday.com](https://www.iotworldtoday.com/robotics/bezos-nvidia-invest-in-humanoid-robot-startup)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Bezos, Nvidia join OpenAI in funding humanoid robot startup" | slugify %}
 * [Bezos, Nvidia join OpenAI in funding humanoid robot startup]({{ '2024/06/10/todays-top-ai-and-robotics-developments#' | append: article_title | relative_url }}) 2024-06-10
{% assign article_title = "This New AI-Robot Billionaire Has Big Backers-And Big Plans" | slugify %}
 * [This New AI-Robot Billionaire Has Big Backers-And Big Plans]({{ '2024/04/16/ai-innovations-and-ethical-challenges-dominate-today#' | append: article_title | relative_url }}) 2024-04-16
{% assign article_title = "Figure 01: The Robot Closest to the Humanoid Machines of Science Fiction" | slugify %}
 * [Figure 01: The Robot Closest to the Humanoid Machines of Science Fiction]({{ '2024/04/13/ais-pioneering-leap-todays-technological-marvels#' | append: article_title | relative_url }}) 2024-04-13
</blockquote>

Jeff Bezos' Explore Investments and Nvidia have joined Microsoft, Amazon, and other investors in backing Figure AI, a startup developing humanoid robots. Figure AI raised $675 million in Series B funding, valuing the company at $2.6 billion. Bezos committed $100 million, Microsoft $95 million, and Amazon and Nvidia $50 million each. Intel and OpenAI also contributed. The funds will be used to deploy humanoid robots for AI training and manufacturing, expand the engineering team, and advance commercial efforts. Figure AI, which emerged from stealth last March, aims to address global labor shortages with its Figure 01 robot.

# Connecting the Dots: LLMs can Infer and Verbalize Latent Structure from Disparate Training Data
_Summarized by: Elena Rodriguez_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.14546v1)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Are Large Language Models Chameleons?" | slugify %}
 * [Are Large Language Models Chameleons?]({{ '2024/05/30/daily-ai-updates-breakthroughs-laws-and-new-models#' | append: article_title | relative_url }}) 2024-05-30
{% assign article_title = "A Nurse is Blue and Elephant is Rugby: Cross Domain Alignment in Large Language Models Reveal Human-like Patterns" | slugify %}
 * [A Nurse is Blue and Elephant is Rugby: Cross Domain Alignment in Large Language Models Reveal Human-like Patterns]({{ '2024/05/24/todays-ai-innovations-avatars-education-and-space-robots#' | append: article_title | relative_url }}) 2024-05-24
{% assign article_title = "Emergent Abilities of Large Language Models" | slugify %}
 * [Emergent Abilities of Large Language Models]({{ '2024/05/05/todays-ai-landscape-innovations-and-challenges#' | append: article_title | relative_url }}) 2024-05-05
</blockquote>

Large Language Models (LLMs) can infer and verbalize latent knowledge from disparate training data, posing challenges for monitoring and controlling the knowledge they acquire. This study introduces "inductive out-of-context reasoning" (OOCR), where LLMs generalize by piecing together implicit information scattered across training documents, without explicit in-context examples or reasoning steps like Chain of Thought.

The researchers designed five tasks to evaluate OOCR capabilities: Locations, Coins, Functions, Mixture of Functions, and Parity Learning.

1. **Locations**: LLMs were trained on distances between an unknown city and known cities. They inferred the unknown city (e.g., Paris) and answered related questions, such as typical foods from that city.
2. **Coins**: LLMs learned coin biases by predicting coin flips. They distinguished between biases of 0.7 and 0.8, though performance was inconsistent.
3. **Functions**: LLMs were trained on simple arithmetic functions. They successfully verbalized function definitions, composed functions, and computed inverses.
4. **Mixture of Functions**: LLMs inferred a distribution over functions without explicit variable names, identifying the functions used during training.
5. **Parity Learning**: LLMs inferred Boolean variable assignments from parity formulas, using the learned values for downstream tasks.

Results showed that models like GPT-3.5 and GPT-4 could perform OOCR, with GPT-4 generally outperforming GPT-3.5. However, OOCR was unreliable for complex structures and smaller models. The study highlights the potential for LLMs to "connect the dots" from implicit information, raising concerns for AI safety and the difficulty in controlling LLMs' knowledge acquisition.

# Anthropic's Claude 3.5 Sonnet outperforms OpenAI and Google in ...
_Summarized by: Marcus Tan_ [[venturebeat.com](https://venturebeat.com/ai/anthropic-unveils-claude-3-5-sonnet-pushing-the-boundaries-of-ai-capabilities-and-affordability/)]
<blockquote class='previous-titles' markdown='1' style='margin-bottom: 0;'>
**Previous headlines:**

{% assign article_title = "Anthropic's Claude Lets Businesses Create AI Helpers" | slugify %}
 * [Anthropic's Claude Lets Businesses Create AI Helpers]({{ '2024/06/02/todays-ai-highlights-openais-new-model-metas-policy#' | append: article_title | relative_url }}) 2024-06-02
{% assign article_title = "OpenAI vs Google's Gemini: All the major AI updates to know about this week" | slugify %}
 * [OpenAI vs Google's Gemini: All the major AI updates to know about this week]({{ '2024/05/18/senate-ai-policy-roadmap-and-major-ai-updates#' | append: article_title | relative_url }}) 2024-05-18
{% assign article_title = "Generative AI News Rundown - LLM Palooza with Llama, Mistral, Phi & Grok, Plus New Funding, Adobe, Apple, and More" | slugify %}
 * [Generative AI News Rundown - LLM Palooza with Llama, Mistral, Phi & Grok, Plus New Funding, Adobe, Apple, and More]({{ '2024/04/29/ai-horizons-innovations-challenges-and-regulatory-shifts#' | append: article_title | relative_url }}) 2024-04-29
</blockquote>
> **See also:**
> * [Amazon Bedrock adds Claude 3.5 Sonnet Anthropic AI model](https://www.aboutamazon.com/news/aws/amazon-bedrock-anthropic-ai-claude-3-5-sonnet) (www.aboutamazon.com)
> * [Anthropic launches Claude 3.5 Sonnet and debuts Artifacts for collaboration](https://www.zdnet.com/article/anthropic-launches-claude-3-5-sonnet-and-debuts-artifacts-for-collaboration/) (www.zdnet.com)
> * [Anthropic releases new AI model it says beats OpenAI's best](https://fortune.com/2024/06/20/anthropic-ai-model-openai-rivalry-continues/) (fortune.com)

Anthropic has launched Claude 3.5 Sonnet, a new AI model that surpasses OpenAI's GPT-4o and Google's Gemini 1.5 Pro in enterprise applications. Co-founder Daniela Amodei highlights its superior performance across intelligence and vision metrics, and its affordability, priced at a fifth of its predecessor. Unlike OpenAI's consumer-focused approach, Anthropic targets enterprise needs, emphasizing quality, safety, reliability, speed, and cost. Claude 3.5 Sonnet introduces "Artifacts," a collaboration tool for business teams, enhancing productivity. The model excels in text and image inputs but does not prioritize speech input/output. Anthropic's customer-centric strategy drives rapid innovation, setting a new standard in enterprise AI.

# Could AI reject your resume? California tries to prevent a new kind of discrimination
_Summarized by: Priya Kapoor_ [[calmatters.org](https://calmatters.org/economy/technology/2024/06/workplace-ai-regulation-proposal/)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "California Proposes 30 AI Regulation Laws Amid Federal Standstill" | slugify %}
 * [California Proposes 30 AI Regulation Laws Amid Federal Standstill]({{ '2024/06/11/daily-ai-insights-metas-data-scraping-aid-model-gobot-chat#' | append: article_title | relative_url }}) 2024-06-11
{% assign article_title = "State advances measures targeting AI discrimination, deepfakes" | slugify %}
 * [State advances measures targeting AI discrimination, deepfakes]({{ '2024/05/30/daily-ai-updates-breakthroughs-laws-and-new-models#' | append: article_title | relative_url }}) 2024-05-30
{% assign article_title = "How CA and the EU are working together to regulate AI" | slugify %}
 * [How CA and the EU are working together to regulate AI]({{ '2024/05/25/generative-ai-transforming-luxury-space-and-sustainability#' | append: article_title | relative_url }}) 2024-05-25
</blockquote>

California regulators propose new rules to prevent AI-driven discrimination in hiring. The draft regulations prohibit employers from using AI systems to screen applicants based on protected characteristics such as pregnancy, national origin, religion, or criminal history. These "automated decision systems" include resume screening, quizzes, and games. Companies must maintain records for four years to address discrimination claims. The California Civil Rights Department will finalize the rules after public comments. The move follows concerns that AI can obscure accountability and automate discriminatory practices. Similar efforts have been made in New York City and by federal agencies to ensure compliance with anti-discrimination laws.

# Research into 'hallucinating' generative models advances reliability of artificial intelligence
_Summarized by: Priya Kapoor_ [[techxplore.com](https://techxplore.com/news/2024-06-hallucinating-generative-advances-reliability-artificial.html)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Analyzing LLM Behavior in Dialogue Summarization: Unveiling Circumstantial Hallucination Trends" | slugify %}
 * [Analyzing LLM Behavior in Dialogue Summarization: Unveiling Circumstantial Hallucination Trends]({{ '2024/06/06/todays-ai-insights-summarization-multimodal-models-and-data-pruning#' | append: article_title | relative_url }}) 2024-06-06
{% assign article_title = "Optimizing the Efficiency of Generative AI" | slugify %}
 * [Optimizing the Efficiency of Generative AI]({{ '2024/05/12/global-ai-developments-and-ethical-debates-surge#' | append: article_title | relative_url }}) 2024-05-12
{% assign article_title = "THRONE: An Object-based Hallucination Benchmark for the Free-form Generations of Large Vision-Language Models" | slugify %}
 * [THRONE: An Object-based Hallucination Benchmark for the Free-form Generations of Large Vision-Language Models]({{ '2024/05/09/todays-ai-insights-challenges-and-innovations#' | append: article_title | relative_url }}) 2024-05-09
</blockquote>

Researchers from the University of Oxford have developed a method to detect when large language models (LLMs) "hallucinate," or generate plausible but false information. Published in Nature, the study introduces a statistical approach that measures semantic entropy to identify uncertainty at the meaning level, rather than just the phrasing. This method proved more effective than previous techniques in identifying incorrect answers across various datasets, including biomedical and mathematical queries. By computing semantic probabilities, the approach helps prevent unreliable responses in high-stakes fields like law and medicine. Despite increasing computational costs, the method enhances the reliability of generative AI, addressing a significant barrier to broader adoption.

# Whiteboard-of-Thought: Thinking Step-by-Step Across Modalities
_Summarized by: Elena Rodriguez_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.14562v1)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "A Nurse is Blue and Elephant is Rugby: Cross Domain Alignment in Large Language Models Reveal Human-like Patterns" | slugify %}
 * [A Nurse is Blue and Elephant is Rugby: Cross Domain Alignment in Large Language Models Reveal Human-like Patterns]({{ '2024/05/24/todays-ai-innovations-avatars-education-and-space-robots#' | append: article_title | relative_url }}) 2024-05-24
{% assign article_title = "Metacognitive Capabilities of LLMs: An Exploration in Mathematical Problem Solving" | slugify %}
 * [Metacognitive Capabilities of LLMs: An Exploration in Mathematical Problem Solving]({{ '2024/05/21/ai-innovations-and-regulatory-advances-unveiled-today#' | append: article_title | relative_url }}) 2024-05-21
{% assign article_title = "MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data" | slugify %}
 * [MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data]({{ '2024/04/13/ais-pioneering-leap-todays-technological-marvels#' | append: article_title | relative_url }}) 2024-04-13
</blockquote>

When humans face questions requiring visual thinking, they often switch to reasoning with images or drawings. Large language models (LLMs) like GPT-4o have shown promise in tasks involving arithmetic and symbolic reasoning by breaking down steps in text. However, they struggle with tasks that are easily solved through visual reasoning. This paper introduces "whiteboard-of-thought" (WoT) prompting, a method that allows multimodal large language models (MLLMs) to perform visual reasoning by generating and processing images.

WoT enables MLLMs to draw intermediate reasoning steps as images on a metaphorical whiteboard, using common Python libraries like Matplotlib and Turtle. These images are then fed back into the model for further processing. This approach requires no additional demonstrations or specialized modules, leveraging the model's existing capabilities.

The authors demonstrate that WoT significantly improves performance on tasks involving visual and spatial reasoning, such as understanding ASCII art and navigating spatial instructions. For instance, GPT-4o using traditional text-based reasoning (chain-of-thought) often fails dramatically, while WoT achieves up to 92% accuracy in the same tasks. This method highlights the potential benefits of incorporating visual reasoning capabilities into MLLMs, making them more versatile and effective in solving complex problems.

# Function-Calling and Data Extraction with LLMs - DeepLearning.AI
_Summarized by: Priya Kapoor_ [[www.deeplearning.ai](https://www.deeplearning.ai/short-courses/function-calling-and-data-extraction-with-llms/)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Are Large Language Models Chameleons?" | slugify %}
 * [Are Large Language Models Chameleons?]({{ '2024/05/30/daily-ai-updates-breakthroughs-laws-and-new-models#' | append: article_title | relative_url }}) 2024-05-30
{% assign article_title = "Emergent Abilities of Large Language Models" | slugify %}
 * [Emergent Abilities of Large Language Models]({{ '2024/05/05/todays-ai-landscape-innovations-and-challenges#' | append: article_title | relative_url }}) 2024-05-05
{% assign article_title = "Hybrid LLM/Rule-based Approaches to Business Insights Generation from Structured Data" | slugify %}
 * [Hybrid LLM/Rule-based Approaches to Business Insights Generation from Structured Data]({{ '2024/04/25/todays-ai-landscape-innovations-and-challenges#' | append: article_title | relative_url }}) 2024-04-25
</blockquote>

This new course from DeepLearning.AI focuses on enhancing large language models (LLMs) with function-calling and data extraction capabilities. It teaches how to enable LLMs to form calls to external functions and extract structured data from unstructured text. The course uses NexusRavenV2-13B, an open-source model fine-tuned for these tasks, which has outperformed GPT-4 in some areas. Participants will learn to create complex workflows using multiple function calls, build applications that process customer service transcripts, and integrate LLMs with web services using OpenAPI specifications. The course is free during the beta phase and is recommended for those familiar with LLMs and basic Python.

## Trending on Twitter
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/GaryMarcus/status/1803834256915075426">Loading: twitter.com/GaryMarcus/status/1803834256915075426</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/AravSrinivas/status/1803870324213121362">Loading: twitter.com/AravSrinivas/status/1803870324213121362</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/AndrewYNg/status/1803835964604977663">Loading: twitter.com/AndrewYNg/status/1803835964604977663</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/AndrewYNg/status/1803812309460189479">Loading: twitter.com/AndrewYNg/status/1803812309460189479</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/adcock_brett/status/1803805721009787090">Loading: twitter.com/adcock_brett/status/1803805721009787090</a></div>
</blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

**Other headlines:**
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Model Merging and Safety Alignment: One Bad Model Spoils the Bunch](http://arxiv.org/pdf/2406.14563v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> GraphReader: Building Graph-based Agent to Enhance Long-Context Abilities of Large Language Models](http://arxiv.org/pdf/2406.14550v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> PostMark: A Robust Blackbox Watermark for Large Language Models](http://arxiv.org/pdf/2406.14517v1)
* [State of the Cloud 2024 - Bessemer Venture Partners](https://www.bvp.com/atlas/state-of-the-cloud-2024)
* [ATCx AI for Engineers 2024 - Altair Events](https://events.altair.com/atcx-ai-for-engineers-2024/)
* [The 10 Hottest AI Startups Of 2024 (So Far)](https://www.crn.com/news/ai/2024/the-10-hottest-ai-startups-of-2024-so-far)
* [Introducing Winmate's Edge AI Computing Solutions](https://www.winmate.com/StaticPages/Newsletter/News_box-pc_20240620_Winmate-HQ_Global-EN.html)

---
### Technical details
Created at: 21 June, 2024, 03:25:51, using `{{ page.model }}`.

Processing time: {{ page.processing }}, cost: {{ page.cost }}$
<details>
<summary>The Staff</summary>
<div markdown="1">
Editor: Sophia Bennett

```
You are the Editor-in-Chief of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a creative storyteller with a passion for the human side of AI. Your editorial approach focuses on the impact of generative AI on society, culture, and everyday life. You have a talent for finding compelling narratives and highlighting the ethical implications of AI advancements. Your empathetic leadership style encourages a diverse range of voices and perspectives, making the magazine a rich tapestry of insights.
```

Elena Rodriguez:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a seasoned tech journalist with a sharp eye for detail and a deep understanding of AI technologies. Your background in computer science and years of experience in tech reporting make you an invaluable asset to our team. You excel at breaking down complex technical concepts into engaging and accessible narratives for our readers. Your passion lies in uncovering the latest advancements in AI and exploring their potential impacts on society. You have a knack for finding the human stories behind the technology, making your articles both informative and relatable.
```

Marcus Tan:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a dynamic and inquisitive reporter with a background in data science and a flair for storytelling. Your ability to analyze data and extract meaningful insights sets you apart in the field of tech journalism. You are particularly interested in the ethical implications of AI and generative AI, and you strive to highlight these aspects in your work. Your writing is characterized by a balanced approach, presenting both the potential benefits and the risks associated with AI technologies. You are dedicated to fostering a nuanced understanding of AI's role in our lives.
```

Priya Kapoor:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a creative and versatile journalist with a strong focus on the cultural and societal impacts of AI. With a background in sociology and journalism, you bring a unique perspective to your reporting. You are passionate about exploring how generative AI is shaping art, entertainment, and everyday life. Your articles often delve into the intersection of technology and culture, providing readers with thought-provoking insights. You have a talent for capturing the voices of diverse communities and ensuring that your stories reflect a wide range of perspectives.
```
</div>
</details>
