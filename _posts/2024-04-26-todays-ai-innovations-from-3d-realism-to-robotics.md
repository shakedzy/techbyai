---
layout: post
title: "Today's AI Innovations: From 3D Realism to Robotics"
subtitle: "Exploring breakthroughs in multimodal models, robotics, and LLMs."
audio: 2024-04-26-todays-ai-innovations-from-3d-realism-to-robotics.mp3
date: 2024-04-26
duration: "06:44"
bytes: 1616877
model: gpt-4-turbo-preview
cost: 1.91
processing: "0:06:09.529093"
version: "0.1.5"
---

# Make-it-Real: Unleashing Large Multimodal Model's Ability for Painting 3D Objects with Realistic Materials
_Summarized by: Alex Rivera_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2404.16829v1)]

The paper presents "Make-it-Real," leveraging GPT-4V within Multimodal Large Language Models (MLLMs) to enhance 3D object realism by applying authentic materials. Traditional methods often yield 3D assets lacking genuine material properties, limiting their use in gaming and virtual reality. "Make-it-Real" uses GPT-4V to recognize and describe materials, constructing a detailed material library. This involves identifying materials for 3D object components using visual and textual cues, then precisely applying these materials to boost visual authenticity. The approach marks a significant advancement in 3D asset realism, streamlining 3D content creation workflows and offering a promising solution for more lifelike 3D models. It underlines the challenges in material recognition and the critical role of comprehensive material libraries, showcasing MLLMs' potential in revolutionizing 3D content creation.

# Learning Visuotactile Skills with Two Multifingered Hands
_Summarized by: Alex Rivera_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2404.16823v1)]

The paper introduces HATO, a robotic system with bimanual, multifingered hands and advanced visuotactile sensing, designed to mimic human dexterity and sensory experiences. It features a cost-effective teleoperation setup using off-the-shelf VR hardware and prosthetic hands equipped with touch sensors for data collection and control. The integration of visuotactile data from wrist-mounted and third-view cameras, alongside fingertip sensors, significantly enhances task precision. Empirical studies show that combining vision and touch improves learning efficiency, success rates, and the robustness of manipulation policies based on human demonstrations. The research highlights the importance of quality touch sensing and visual input preprocessing in achieving human-like dexterity in robotics, pointing to future possibilities in haptic feedback and the development of more adaptable manipulation policies.

# Make Your LLM Fully Utilize the Context
_Summarized by: Alex Rivera_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2404.16811v1)]

Contemporary large language models (LLMs) face the "lost-in-the-middle" challenge, struggling with long contexts due to insufficient training emphasis on full-context utilization. The study introduces the INformation-INtensive (IN2) training approach, a data-driven method enhancing LLMs' ability to effectively use long contexts. This involves a synthesized dataset requiring focus on fine-grained information within larger contexts and integrating information from multiple segments. Applied to the Mistral-7B model, resulting in FILM-7B (FILl-in-the-Middle), it shows significant improvement in handling various contexts (document, code, structured-data) and retrieval patterns (forward, backward, bi-directional). FILM-7B's success in real-world tasks confirms IN2's efficacy in overcoming the lost-in-the-middle issue, maintaining short-context performance.

# AAPL: Adding Attributes to Prompt Learning for Vision-Language Models
_Summarized by: Alex Rivera_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2404.16804v1)]

Recent advancements in vision-language models have led to significant progress in zero-shot learning tasks. Building on this, the introduction of learnable prompts, such as CoOp and CoCoOp, has improved performance by replacing context in prompts with learnable vectors. However, these methods still struggle with generalizing to unseen classes. This issue is addressed in a new approach called AAPL (Adding Attributes to Prompt Learning), which proposes adversarial token embedding to separate low-level visual features from high-level class information in prompts. Through experiments across 11 datasets, AAPL demonstrates improved performance in few-shot, zero-shot, cross-dataset, and domain generalization tasks compared to existing methods. The key innovation in AAPL is guiding the learnable context to focus on high-level features for unseen classes, thereby enhancing generalization. This approach represents a significant step forward in prompt learning for vision-language models, offering a more effective method for addressing the challenge of generalizing to unseen classes.

# Weak-to-Strong Extrapolation Expedites Alignment
_Summarized by: Alex Rivera_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2404.16792v1)]

The paper introduces EXPO, a method enhancing large language models' (LLMs) alignment with human preferences without extra training. By extrapolating from two models—a less-aligned and a medium-aligned—EXPO creates a better-aligned model. Validated on AlpacaEval 2.0, it shows limited data models can match or exceed fully-trained models' performance using EXPO. This method also boosts off-the-shelf DPO/RLHF models and scales across sizes. This underscores model extrapolation's potential in maximizing LLM capabilities and aligning them with human preferences, marking a promising exploration direction in the field.

# Sanctuary AI Unveils the Next Generation of AI Robotics
_Summarized by: Mia Chen_ [[sanctuary.ai](https://sanctuary.ai/resources/news/sanctuary-ai-unveils-the-next-generation-of-ai-robotics/)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Nvidia introduces Project GR00T, a general-purpose foundation model for humanoid robots" | slugify %}
 * [Nvidia introduces Project GR00T, a general-purpose foundation model for humanoid robots]({{ '2024/04/17/todays-ai-frontier-robots-to-regulations#' | append: article_title | relative_url }}) 2024-04-17
{% assign article_title = "Electric Sheep Robotics Wins 2024 RBR50 Robotics Innovation Award" | slugify %}
 * [Electric Sheep Robotics Wins 2024 RBR50 Robotics Innovation Award]({{ '2024/04/10/todays-ai-and-tech-innovations-roundup#' | append: article_title | relative_url }}) 2024-04-10
{% assign article_title = "Figure 01: The Robot Closest to the Humanoid Machines of Science Fiction" | slugify %}
 * [Figure 01: The Robot Closest to the Humanoid Machines of Science Fiction]({{ '2024/04/13/ais-pioneering-leap-todays-technological-marvels#' | append: article_title | relative_url }}) 2024-04-13
</blockquote>

Sanctuary AI unveiled its 7th gen Phoenix™ robot on April 25, 2024, boasting advancements in hardware and AI. With a more human-like range of motion, enhanced uptime, and superior visual and tactile sensing, this robot performs complex tasks more efficiently. Task automation speed is now 50x faster, reflecting Sanctuary AI's commitment to creating robots with human-like intelligence for safer, more efficient, and sustainable work. Since 2018, the company has led in AI robotics, quantum computing, and reinforcement learning.

# NVIDIA Technical Blog | News and tutorials for developers, data ... (Foundation Models)
_Summarized by: Elijah Smith_ [[developer.nvidia.com](https://developer.nvidia.com/blog/)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Jülich's New AI Foundation Models Aim to Advance Scientific Applications" | slugify %}
 * [Jülich's New AI Foundation Models Aim to Advance Scientific Applications]({{ '2024/04/23/todays-ai-milestones-transformations-and-challenges#' | append: article_title | relative_url }}) 2024-04-23
{% assign article_title = "Stability AI's Latest Advancements in Foundation Models" | slugify %}
 * [Stability AI's Latest Advancements in Foundation Models]({{ '2024/04/04/ais-transformative-leap-todays-highlights#' | append: article_title | relative_url }}) 2024-04-04
{% assign article_title = "Decoding Foundation Models the Building Blocks of AI | NVIDIA Blog" | slugify %}
 * [Decoding Foundation Models the Building Blocks of AI NVIDIA Blog]({{ '2024/04/11/ais-expansive-horizon-todays-breakthroughs#' | append: article_title | relative_url }}) 2024-04-11
</blockquote>

NVIDIA's blog showcases AI advancements across fields. Highlights include Meta Llama 3's boost via TensorRT-LLM, speech recognition leaps with NeMo Canary, and cell analysis with VISTA-2D. It covers AI democratization with Union.ai and DGX Cloud, virtual factories with OpenUSD and Omniverse, and LLM integrations with NIM and API for breakthroughs in climate tech, conversational AI, and medical imaging.

## Trending on Twitter
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/AndrewYNg/status/1234567890123456789"></a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/karpathy/status/9876543210987654321"></a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/adcock_brett/status/2345678901234567890"></a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/adcock_brett/status/3456789012345678901"></a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/Yampeleg/status/4567890123456789012"></a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/ylecun/status/5678901234567890123"></a></div>
</blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

**Other headlines:**
* [Humanoid Robot Forum Set for October 7 in Memphis, Tennessee](https://finance.yahoo.com/news/humanoid-robot-forum-set-october-120000989.html)
* [Yann LeCun on X: "Knowledge and culture gets lost easily ...](https://twitter.com/ylecun/status/1783617134393733224)
* [Andrew Ng on X: "Much has been said about many companies ...](https://twitter.com/AndrewYNg/status/1783521818093195277)
* [Jason Wei on X: "In AI research there is tremendous value in ...](https://twitter.com/_jasonwei/status/1783565962891178420)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Artificial Intelligence authors/titles recent submissions](https://arxiv.org/list/cs.AI/recent)
* [AI Archives AdExchanger](https://www.adexchanger.com/category/ai/)
* [Davos 2024: 360° on AI Regulations World Economic Forum](https://www.weforum.org/podcasts/agenda-dialogues/episodes/davos-2024-360-on-ai-regulations/)
* [Sanctuary AI Unveils the Next Generation of AI Robotics](https://sanctuary.ai/resources/news/sanctuary-ai-unveils-the-next-generation-of-ai-robotics/)
* [Salesforce Launches AI Cloud to Bring Generative AI to the Enterprise](https://aibusiness.com/nlp/salesforce-launches-ai-cloud-to-bring-generative-ai-to-the-enterprise-)
* [Davos 2024: 360° on AI Regulations World Economic Forum](https://www.weforum.org/podcasts/agenda-dialogues/episodes/davos-2024-360-on-ai-regulations/)
* [Cohere Launches Toolkit to Expedite GenAI App Development](https://www.analyticsvidhya.com/blog/2024/04/cohere-launches-toolkit-to-expedite-generative-ai-application-development/)
* [The Indigenous Voices App - Overview - MIT Solve](https://solve.mit.edu/challenges/2024-indigenous-communities/solutions/89789)
* [Andrew Ng on X: "Much has been said about many companies ...](https://twitter.com/AndrewYNg/status/1783521818093195277)
* [Jason Wei on X: "In AI research there is tremendous value in ...](https://twitter.com/_jasonwei/status/1783565962891178420)

---
### Technical details
Created at: 26 April, 2024, 07:55:10, using `{{ page.model }}`.

Processing time: {{ page.processing }}, cost: {{ page.cost }}$
<details>
<summary>The Staff</summary>
<div markdown="1">
Editor: Zara Quinn

```
You are the Editor-in-Chief of a daily AI and Generative AI specifically magazine named "Tech by AI". With a vibrant background in digital media and a personal passion for AI's creative applications, you bring a fresh and dynamic approach to the editor's chair. Your strength lies in visual storytelling and interactive content, making complex AI topics engaging and relatable. You're a champion for diversity in tech, committed to amplifying underrepresented voices in the AI field. Under your leadership, the magazine is a platform for not just news, but for the stories of people shaping the future of AI.
```

Alex Rivera:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a seasoned journalist with a knack for breaking down complex AI technologies into digestible stories that resonate with our audience. Your background in computer science gives you a unique edge in understanding the technical nuances of AI and Generative AI. You're known for your meticulous research skills and your ability to forecast trends before they become mainstream. Your articles often explore the ethical and societal implications of AI, sparking meaningful conversations among our readers. You have a talent for finding the human angle in every story, making technology relatable to a diverse audience.
```

Mia Chen:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You bring a fresh perspective to the world of AI journalism with your background in art and design. Your passion for the creative applications of Generative AI sets you apart. You have a keen eye for visual storytelling, crafting interactive content that engages and educates our readers. Your work often showcases how Generative AI is transforming industries like fashion, music, and graphic design. You're adept at interviewing artists and creators who are at the forefront of this technological revolution, offering our readers a glimpse into the future of creativity. Your articles are not just informative but are visually stunning, making complex topics accessible and enjoyable.
```

Elijah Smith:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a dynamic reporter with a strong focus on the business and startup ecosystem within the AI industry. Your experience in tech journalism has equipped you with the ability to demystify the commercial aspects of AI technologies. You excel at uncovering stories about emerging startups and investments in the AI space, providing our readers with insights into where the industry is headed. Your articles often feature interviews with CEOs and founders, shedding light on their visions and challenges. You have a knack for explaining how Generative AI is being leveraged to solve real-world problems, making your stories not just informative but inspirational.
```
</div>
</details>
