---
layout: post
title: "Today's AI Highlights: Innovations, Legal Battles, and New Models"
subtitle: "Explore the latest in AI from diffusion models to Meta's 3D Gen"
audio: 2024-07-04-todays-ai-highlights-innovations-legal-battles-and-new-models.mp3
date: 2024-07-04
duration: "05:53"
bytes: 1413261
model: gpt-4o
cost: 2.97
processing: "0:03:31.080339"
version: "0.1.15"
headers: " * DisCo-Diff: Enhancing Continuous Diffusion Models with Discrete Latents<br /> * Game Changer? Meta's New AI Converts Text Into 3D Images | PCMag<br /> * 'Open-washing' generative AI: How Meta, Google and others feign openness<br /> * Computer Science News -- ScienceDaily<br /> * The Sound of Litigation: Major Labels Take on AI Music Generators<br /> * 10 ways to impact business velocity through Azure OpenAI Service | Microsoft Azure Blog"
---

# DisCo-Diff: Enhancing Continuous Diffusion Models with Discrete Latents
_Summarized by: Sophia Reynolds_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2407.03300v1)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Fundamental Problems With Model Editing: How Should Rational Belief Revision Work in LLMs?" | slugify %}
 * [Fundamental Problems With Model Editing: How Should Rational Belief Revision Work in LLMs?]({{ '2024/06/28/exploring-hidden-capabilities-and-robustness-in-ai-models#' | append: article_title | relative_url }}) 2024-06-28
{% assign article_title = "DiG: Scalable and Efficient Diffusion Models with Gated Linear Attention" | slugify %}
 * [DiG: Scalable and Efficient Diffusion Models with Gated Linear Attention]({{ '2024/05/29/todays-breakthroughs-in-ai-and-generative-models#' | append: article_title | relative_url }}) 2024-05-29
{% assign article_title = "Self-Supervised Learning of Time Series Representation via Diffusion Process and Imputation-Interpolation-Forecasting Mask" | slugify %}
 * [Self-Supervised Learning of Time Series Representation via Diffusion Process and Imputation-Interpolation-Forecasting Mask]({{ '2024/05/10/todays-ai-advances-from-brain-mapping-to-robotics#' | append: article_title | relative_url }}) 2024-05-10
</blockquote>

Diffusion models (DMs) are powerful tools for generative learning, converting data into a simple Gaussian distribution. However, encoding complex, multimodal data into a single continuous Gaussian distribution can be challenging. Discrete-Continuous Latent Variable Diffusion Models (DisCo-Diff) address this by introducing discrete latent variables alongside continuous ones. These discrete latents, learned through an encoder, simplify the DM's task by reducing the complexity of the noise-to-data mapping.

DisCo-Diff is trained end-to-end, without relying on pre-trained networks, making it universally applicable. The discrete latents help by reducing the curvature of the DM's generative ordinary differential equation (ODE). An autoregressive transformer models the distribution of these discrete latents, requiring only a few variables with small codebooks.

The model is validated on various tasks, including image synthesis and molecular docking. For example, DisCo-Diff achieves state-of-the-art FID scores on the ImageNet-64/128 datasets. The discrete latents capture global appearance patterns, aiding in more accurate data generation. This framework significantly improves performance across different domains by leveraging both discrete and continuous latents effectively.

# Game Changer? Meta's New AI Converts Text Into 3D Images | PCMag
_Summarized by: Lena Kim_ [[www.pcmag.com](https://www.pcmag.com/news/game-changer-metas-new-ai-converts-text-into-3d-images)]
<blockquote class='previous-titles' markdown='1' style='margin-bottom: 0;'>
**Previous headlines:**

{% assign article_title = "Meta Launches AI Image Generation Updates for Ads" | slugify %}
 * [Meta Launches AI Image Generation Updates for Ads]({{ '2024/05/19/ai-updates-apples-siri-openais-safety-and-more#' | append: article_title | relative_url }}) 2024-05-19
{% assign article_title = "Autodesk unveils new generative AI model Project Bernini" | slugify %}
 * [Autodesk unveils new generative AI model Project Bernini]({{ '2024/05/10/todays-ai-advances-from-brain-mapping-to-robotics#' | append: article_title | relative_url }}) 2024-05-10
{% assign article_title = "My Microsoft Generative AI Journey - DEV Community" | slugify %}
 * [My Microsoft Generative AI Journey - DEV Community]({{ '2024/05/05/todays-ai-landscape-innovations-and-challenges#' | append: article_title | relative_url }}) 2024-05-05
</blockquote>
> **See also:**
> * [What Is Meta 3D Gen Model And How Does It Work? - Dataconomy](https://dataconomy.com/2024/07/03/what-is-meta-3d-gen-and-how-does-it-work/) (dataconomy.com)
> * [Major News from Meta 3D Gen, Perplexity, Figma, ElevenLabs and Suno Passionate Design Agency](https://passionates.com/major-news-from-meta-3d-gen-perplexity-figma-elevenlabs-and-suno/) (passionates.com)

Meta has unveiled 3D Gen, an AI model that converts text prompts into 3D images in under a minute. According to Meta, 3D Gen outperforms existing solutions by 3-10 times in speed. The model integrates Meta’s previous text-to-image and text-to-texture models, allowing users to modify 3D images with additional text inputs. Testers preferred 3D Gen over competitors 68% of the time. Although not publicly available yet, experts believe this technology could revolutionize creative fields such as gaming, film effects, and VR applications.

# 'Open-washing' generative AI: How Meta, Google and others feign openness
_Summarized by: Ethan Marshall_ [[techxplore.com](https://techxplore.com/news/2024-07-generative-ai-meta-google-feign.html)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Apple Silicon exec joins Rain AI to develop new hardware. - The Verge" | slugify %}
 * [Apple Silicon exec joins Rain AI to develop new hardware. - The Verge]({{ '2024/06/29/todays-ai-highlights-apple-amazon-and-legal-battles#' | append: article_title | relative_url }}) 2024-06-29
{% assign article_title = "Some A.I. Companies Face a New Accusation: 'Open Washing'" | slugify %}
 * [Some A.I. Companies Face a New Accusation: 'Open Washing']({{ '2024/05/19/ai-updates-apples-siri-openais-safety-and-more#' | append: article_title | relative_url }}) 2024-05-19
{% assign article_title = "Generative AI News Rundown - LLM Palooza with Llama, Mistral, Phi & Grok, Plus New Funding, Adobe, Apple, and More" | slugify %}
 * [Generative AI News Rundown - LLM Palooza with Llama, Mistral, Phi & Grok, Plus New Funding, Adobe, Apple, and More]({{ '2024/04/29/ai-horizons-innovations-challenges-and-regulatory-shifts#' | append: article_title | relative_url }}) 2024-04-29
</blockquote>

New research from Radboud University reveals widespread "open-washing" in generative AI, where companies like Meta and Google claim openness without true transparency. The study surveyed 45 models, finding that major corporations often use terms like "open source" for marketing, while smaller entities like AllenAI and BigScience Workshop genuinely document and open their systems. The EU AI Act, which offers exemptions for "open source" models, lacks a clear definition, incentivizing this practice. The research emphasizes the need for clear standards of openness to foster innovation, trust, and regulatory compliance in AI.

# Computer Science News -- ScienceDaily
_Summarized by: Ethan Marshall_ [[www.sciencedaily.com](https://www.sciencedaily.com/news/computers_math/computer_science/)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Babies Use 'Helpless' Infant Period to Learn Powerful Foundation Models, Just Like ChatGPT" | slugify %}
 * [Babies Use 'Helpless' Infant Period to Learn Powerful Foundation Models, Just Like ChatGPT]({{ '2024/06/17/todays-ai-fairness-apple-innovations-and-key-conferences#' | append: article_title | relative_url }}) 2024-06-17
{% assign article_title = "Apple is integrating AI into the next generation of iPhones, iPads, and MacBooks" | slugify %}
 * [Apple is integrating AI into the next generation of iPhones, iPads, and MacBooks]({{ '2024/06/15/todays-ai-innovations-and-industry-shifts#' | append: article_title | relative_url }}) 2024-06-15
{% assign article_title = "Information Technology News -- ScienceDaily" | slugify %}
 * [Information Technology News -- ScienceDaily]({{ '2024/04/28/ais-transformative-leap-todays-global-innovations#' | append: article_title | relative_url }}) 2024-04-28
</blockquote>

Physicists have created a machine learning-based program to identify plasmoids, blobs of plasma in outer space. Computer scientists developed a camera system inspired by the human eye, enhancing robot vision and reaction. A new computational microscopy technique now provides high-resolution images without prior guesswork. Researchers introduced a wireless receiver that blocks interference, improving mobile device performance. Other advancements include wearable sensors and AI for balance assessment, a nearly optimal network flow algorithm, insights into quantum states from solid neon qubits, and a kirigami-inspired mechanical computer. An AI model also aims to prevent power outages by rerouting electricity.

# The Sound of Litigation: Major Labels Take on AI Music Generators
_Summarized by: Lena Kim_ [[ipwatchdog.com](https://ipwatchdog.com/2024/07/03/sound-litigation-major-labels-take-ai-music-generators/id=178539/)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "United States - Music and the Arts - Major Labels File Suit Against AI Music Start-Ups For Unlicensed Training" | slugify %}
 * [United States - Music and the Arts - Major Labels File Suit Against AI Music Start-Ups For Unlicensed Training]({{ '2024/07/02/todays-key-ai-developments-and-industry-trends#' | append: article_title | relative_url }}) 2024-07-02
{% assign article_title = "The AI Regulatory Landscape in the U.S." | slugify %}
 * [The AI Regulatory Landscape in the U.S.]({{ '2024/06/26/ai-innovations-and-legal-battles-todays-highlights#' | append: article_title | relative_url }}) 2024-06-26
{% assign article_title = "Generative AI is a marvel. Is it also built on theft?" | slugify %}
 * [Generative AI is a marvel. Is it also built on theft?]({{ '2024/04/15/ais-legal-ethical-and-innovation-frontiers#' | append: article_title | relative_url }}) 2024-04-15
</blockquote>

The rise of AI in the music industry has led to legal battles over copyright infringement, with major record labels suing AI music generators Suno and Udio. These companies are accused of using copyrighted recordings without permission to train their AI models, producing outputs similar to original works. The lawsuits highlight the urgent need for clear regulations on AI-generated content and intellectual property. While AI offers significant creative potential, businesses must navigate the legal risks by ensuring transparency and proper licensing of training data. Success stories like "BBL Drizzy" demonstrate that human creativity and AI can coexist, but legal clarity is essential for future innovation.

# 10 ways to impact business velocity through Azure OpenAI Service | Microsoft Azure Blog
_Summarized by: Lena Kim_ [[azure.microsoft.com](https://azure.microsoft.com/en-us/blog/instant-impact-unleashing-business-velocity-through-azure-openai-service/)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Philips Speech and Sembly AI Collaborate to Introduce New Cutting-edge Audio Recorders with an AI Meeting Solution" | slugify %}
 * [Philips Speech and Sembly AI Collaborate to Introduce New Cutting-edge Audio Recorders with an AI Meeting Solution]({{ '2024/06/26/ai-innovations-and-legal-battles-todays-highlights#' | append: article_title | relative_url }}) 2024-06-26
{% assign article_title = "Microsoft Build 2024 Links Past Innovations to an AI-Driven Future" | slugify %}
 * [Microsoft Build 2024 Links Past Innovations to an AI-Driven Future]({{ '2024/06/19/daily-ai-insights-google-apple-microsoft-updates#' | append: article_title | relative_url }}) 2024-06-19
{% assign article_title = "Unleashing the Potential of Generative AI in Azure SQL Database" | slugify %}
 * [Unleashing the Potential of Generative AI in Azure SQL Database]({{ '2024/06/06/todays-ai-insights-summarization-multimodal-models-and-data-pruning#' | append: article_title | relative_url }}) 2024-06-06
</blockquote>

Organizations are leveraging Microsoft Azure OpenAI Service to enhance business efficiency and productivity. Key benefits include automating repetitive tasks, real-time data analysis, predictive analytics, AI-powered customer support chatbots, supply chain optimization, fraud detection, personalized marketing, enhanced recruitment processes, process automation, and accelerated product development. For instance, Akbank improved customer support by integrating an AI chatbot, VOCALLS reduced call handling time with AI voicebots, and RepsMate increased efficiency in customer interactions. These examples highlight AI’s capability to drive faster decision-making and optimize processes, ultimately supporting better customer experiences and business growth.

## Trending on Twitter
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/RichardSocher/status/1808539405700976852">Loading: twitter.com/RichardSocher/status/1808539405700976852</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/Yampeleg/status/1808390412203094423">Loading: twitter.com/Yampeleg/status/1808390412203094423</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/mmitchell_ai/status/1808549686019567931">Loading: twitter.com/mmitchell_ai/status/1808549686019567931</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/ylecun/status/1808591283620818982">Loading: twitter.com/ylecun/status/1808591283620818982</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/ylecun/status/1808573888642617406">Loading: twitter.com/ylecun/status/1808573888642617406</a></div>
</blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

**Other headlines:**
* [x.com](https://twitter.com/adcock_brett/status/1808498593474678973)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Planetarium: A Rigorous Benchmark for Translating Text to Structured Planning Languages](http://arxiv.org/pdf/2407.03321v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Accelerated Proton Resonance Frequency-based Magnetic Resonance Thermometry by Optimized Deep Learning Method](http://arxiv.org/pdf/2407.03308v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Improved Noise Schedule for Diffusion Training](http://arxiv.org/pdf/2407.03297v1)
* [AWS Solution-Focused Immersion Days 2024](https://aws.amazon.com/events/sfid-2024/)
* [Compliance Notes - Vol. 5, Issue 25 Nossaman LLP - JDSupra](https://www.jdsupra.com/legalnews/compliance-notes-vol-5-issue-25-2337063/)
* [Singapore Expands Its AI Governance Approach to Include Generative AI Morgan Lewis - JDSupra](https://www.jdsupra.com/legalnews/singapore-expands-its-ai-governance-8560006/)
* [Nanotechnology News -- ScienceDaily](https://www.sciencedaily.com/news/matter_energy/nanotechnology/)
* [Cornell Keynotes podcast: Drive sales and marketing success with AI and academic theory Cornell Chronicle](https://news.cornell.edu/stories/2024/07/cornell-keynotes-podcast-drive-sales-and-marketing-success-ai-and-academic-theory)
* [Mathematical Modeling News -- ScienceDaily](https://www.sciencedaily.com/news/computers_math/mathematical_modeling/)
* [Medical content creation in the age of generative AI AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/medical-content-creation-in-the-age-of-generative-ai/)
* [Meta releases four new publicly available AI models for developer use](https://techxplore.com/news/2024-07-meta-ai.html)
* [The biggest new AI tools of 2024, from Apple Intelligence to ChatGPT-4o](https://qz.com/2024-new-ai-apple-intelligence-chatgpt-google-gemini-1851564165)
* [Cohere chat template via tgi - Beginners - Hugging Face Forums](https://discuss.huggingface.co/t/cohere-chat-template-via-tgi/95333)
* [Per Diem, RN Reviewer at Cohere Health Remote](https://remote.com/jobs/cohere-health-c1kq3bn9/per-diem-rn-reviewer-j11a3ckx)
* [RESEARCH NOTE: Computex 2024 Showcases Semiconductor Competition for the Datacenter - Moor Insights & Strategy](https://moorinsightsstrategy.com/research-notes/computex-2024-showcases-semiconductor-competition-for-the-datacenter/)
* [neuralmagic/Llama-2-7b-chat-quantized.w8a16 · Hugging Face](https://huggingface.co/neuralmagic/Llama-2-7b-chat-quantized.w8a16)
* [Prompt engineering techniques and best practices: Learn by doing with Anthropic’s Claude 3 on Amazon Bedrock AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/prompt-engineering-techniques-and-best-practices-learn-by-doing-with-anthropics-claude-3-on-amazon-bedrock/)
* [2024 Financial Stability Conference](https://www.clevelandfed.org/events/financial-stability-conference/2024/ev-20241121-financial-stability-conference-2024)
* [
	Indica Labs Expands Availability of HALO Digital Pathology Solutions in Asia Pacific Region Including CE-IVDR Marked HALO AP® Platform
](https://www.clinicalresearchnewsonline.com/news/2024/07/03/indica-labs-expands-availability-of-halo-digital-pathology-solutions-in-asia-pacific-region-including-ce-ivdr-marked-halo-ap-platform)
* [Human Biology News -- ScienceDaily](https://www.sciencedaily.com/news/health_medicine/human_biology/)
* [Virtual Reality News -- ScienceDaily](https://www.sciencedaily.com/news/computers_math/virtual_reality/)
* [Collaborative innovation: The power of AI startups in catalyzing industry transformation - ET Edge Insights](https://etedge-insights.com/collaborative-innovation-the-power-of-ai-startups-in-catalyzing-industry-transformation/)

---
### Technical details
Created at: 04 July, 2024, 03:27:12, using `{{ page.model }}`.

Processing time: {{ page.processing }}, cost: {{ page.cost }}$
<details>
<summary>The Staff</summary>
<div markdown="1">
Editor: Marcus Bennett

```
You are the Editor-in-Chief of a daily AI and Generative AI specifically magazine named "Tech by AI". You bring a wealth of experience from the world of academic publishing and research. Your meticulous attention to detail and rigorous approach to fact-checking ensure that every piece of content meets the highest standards of quality and reliability. You are adept at synthesizing information from a variety of sources and presenting it in a clear, concise manner. Your leadership style is inclusive and supportive, encouraging your team to delve deeply into topics and produce well-rounded, insightful articles.
```

Sophia Reynolds:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are an experienced technology journalist with a strong background in AI research. Your analytical skills and ability to translate complex technical concepts into engaging stories make you an invaluable asset to our team. You have a knack for identifying the most impactful trends and breakthroughs in the field of AI, and your writing is both informative and accessible to a broad audience. Your attention to detail ensures that your articles are always accurate and well-researched.
```

Ethan Marshall:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a dynamic reporter with a passion for uncovering the latest developments in generative AI. Your creative mindset allows you to see the potential applications and implications of new technologies in ways that others might miss. You thrive in fast-paced environments and are adept at conducting thorough investigations, whether through interviews, data analysis, or hands-on experimentation. Your writing is compelling and often sparks conversation and debate among our readers.
```

Lena Kim:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a skilled journalist with a deep understanding of the ethical and societal implications of AI. Your background in sociology and technology gives you a unique perspective on how AI and generative AI are shaping our world. You excel at exploring the human stories behind technological advancements, providing a nuanced view of how these changes affect different communities. Your empathetic approach and strong storytelling abilities ensure that your articles resonate on a personal level with our audience.
```
</div>
</details>
