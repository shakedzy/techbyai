---
layout: post
title: "Today's Breakthroughs in AI and Robotics"
subtitle: "From Molecular Learning to Warehouse Automation and Ethical AI Challenges"
audio: 2024-06-25-todays-breakthroughs-in-ai-and-robotics.mp3
date: 2024-06-25
duration: "08:10"
bytes: 1964301
model: gpt-4o
cost: 2.18
processing: "0:03:41.902785"
version: "0.1.14"
headers: " * GeoMFormer: A General Architecture for Geometric Molecular Representation Learning<br /> * Understanding and Mitigating Tokenization Bias in Language Models<br /> * General Binding Affinity Guidance for Diffusion Models in Structure-Based Drug Design<br /> * New UNESCO report warns that Generative AI threatens Holocaust memory | UNESCO<br /> * Record Companies Bring Landmark Cases for Responsible AI AgainstSuno and Udio in Boston and New York Federal Courts, Respectively<br /> * Humanoid Robots Being Tested for Warehouse Automation"
---

# GeoMFormer: A General Architecture for Geometric Molecular Representation Learning
_Summarized by: Sophia Reynolds_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.16864v1)]

StableNormal is a novel approach for estimating high-quality surface normals from monocular colored inputs (images and videos). This method addresses the inherent stochasticity in diffusion-based models, which previously led to unstable and incorrect normal estimates. StableNormal reduces this stochasticity by minimizing inference variance, resulting in stable and sharp normal maps without the need for ensembling.

The process begins with a coarse but reliable initial normal estimate using a one-step estimator called YOSO (You-Only-Sample-Once). This is followed by a semantic-guided refinement step (SG-DRN) that enhances geometric details. SG-DRN leverages semantic features from a pre-trained DINO model to provide global context, which helps in accurately refining the normals.

StableNormal performs robustly under challenging conditions such as extreme lighting, blurring, and cluttered scenes. It has shown superior performance on standard datasets like DIODE-indoor, iBims, ScannetV2, and NYUv2, outperforming existing methods in both accuracy and stability.

The method's effectiveness is demonstrated in various applications, including surface reconstruction and normal enhancement. StableNormal represents a significant step forward in repurposing diffusion priors for deterministic estimation tasks, offering a reliable and efficient solution for high-quality normal estimation.

# Understanding and Mitigating Tokenization Bias in Language Models
_Summarized by: Sophia Reynolds_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.16833v1)]

The paper introduces the USDC dataset, which stands for User Stance and Dogmatism in Conversations. This dataset is designed to help understand user opinions and dogmatism in long Reddit conversations. The authors highlight the importance of identifying user stances for applications like personalized marketing, political campaigns, and content moderation. However, manually annotating these stances is challenging due to the length and complexity of conversations.

To address this, the researchers used two large language models (LLMs), Mistral Large and GPT-4, to automate the annotation process. They focused on two tasks: User Stance classification, which labels a user's stance in a conversation on a five-point scale, and User Dogmatism classification, which assesses the overall opinion of a user on a four-point scale. The dataset includes 764 multi-user Reddit conversations, resulting in 9,618 stance samples and 1,528 dogmatism samples.

The paper discusses the challenges of manual annotation and the advantages of using LLMs, such as their ability to handle long-range dependencies in text. The authors experimented with various models and found that instruction-tuned models generally performed better for stance detection, while fine-tuned models were more effective for dogmatism detection. The dataset and code are publicly available, providing a valuable resource for future research in understanding user opinions and dogmatism in online conversations.

# General Binding Affinity Guidance for Diffusion Models in Structure-Based Drug Design
_Summarized by: Sophia Reynolds_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.16828v1)]

Retrieval-Augmented Generation (RAG) is a technique that enhances large language models (LLMs) by incorporating real-time data to provide more accurate and contextually relevant answers. Traditional search engines display a list of ranked documents, but RAG systems generate a concise, attributed summary by retrieving and integrating information from multiple sources.

The paper introduces Ragnarök, a reusable RAG framework designed to foster innovation and standardize RAG system evaluation. Ragnarök integrates with existing Python frameworks like Pyserini and rank_llm, offering customizable retrievers, rerankers, and generation models. It supports REST APIs and a Web-based user interface for interactive benchmarking.

Ragnarök's retrieval module retrieves and reranks relevant segments for a given topic, while the augmented generation module uses these segments to produce a detailed answer with citations. The framework is open-source and provides industrial baselines like OpenAI's GPT-4o and Cohere's Command R+.

The paper also discusses the MS MARCO V2.1 collection, a deduplicated dataset used for the TREC 2024 RAG Track, and introduces two sets of development topics: TREC-RAGgy 2024 and TREC-Researchy 2024. These topics are designed to require long-form answers and information aggregation, providing a robust evaluation for RAG systems.

Overall, Ragnarök aims to standardize RAG applications and promote their wider adoption by providing a comprehensive, user-friendly framework for building and evaluating RAG systems.

# New UNESCO report warns that Generative AI threatens Holocaust memory | UNESCO
_Summarized by: Ava Martinez_ [[www.unesco.org](https://www.unesco.org/en/articles/new-unesco-report-warns-generative-ai-threatens-holocaust-memory)]

A UNESCO report warns that generative AI poses a significant threat to Holocaust memory by potentially distorting historical records and spreading antisemitism. The report highlights the risk of AI-generated disinformation and the inadvertent creation of false content about the Holocaust. It emphasizes the urgent need for ethical principles to guide AI development to prevent the dilution of historical facts. The report also notes that AI can amplify societal biases, leading to the misrepresentation of events and reinforcing prejudices. UNESCO calls for the implementation of its ethical AI guidelines and collaboration with tech companies, educators, and the Jewish community to safeguard historical accuracy and promote digital literacy among young people.

# Record Companies Bring Landmark Cases for Responsible AI AgainstSuno and Udio in Boston and New York Federal Courts, Respectively
_Summarized by: Liam O'Connor_ [[www.morningstar.com](https://www.morningstar.com/news/accesswire/879837msn/leveraging-twitter-with-generative-ai-enhancing-us-equity-investments)]
> **See also:**
> * [Record Companies Bring Landmark Cases for Responsible AI AgainstSuno and Udio in Boston and New York Federal Courts, Respectively - RIAA](https://www.riaa.com/record-companies-bring-landmark-cases-for-responsible-ai-againstsuno-and-udio-in-boston-and-new-york-federal-courts-respectively/) (www.riaa.com)

Context Analytics (CA) has introduced a Generative AI application for US equity investments, leveraging Twitter data to provide real-time insights and summaries. This tool captures and analyzes millions of tweets to offer investors a comprehensive view of market sentiment, identifying key trends and conversation topics. The AI-generated summaries help investors quickly digest large volumes of data, highlighting potential red flags and positive signals. The application integrates seamlessly via API, ensuring continuous monitoring and real-time data updates. Additionally, the Active Trader platform provides a user-friendly interface with sentiment metrics and real-time Twitter feeds. Daily refreshed summaries and email alerts keep investors informed of the latest market conversations, enabling better-informed decisions and risk assessments.

# Humanoid Robots Being Tested for Warehouse Automation
_Summarized by: Liam O'Connor_ [[www.iotworldtoday.com](https://www.iotworldtoday.com/robotics/humanoid-robots-being-tested-for-warehouse-automation)]
> **See also:**
> * [Humanoid Robots Being Tested for Warehouse Automation](https://www.billboard.com/pro/riaa-mitch-glazier-generative-ai-guest-column-suno-udio-lawsuit/) (www.billboard.com)

GXO, a leading logistics firm, is collaborating with Apptronik to test Apollo, an AI-powered humanoid robot, for warehouse automation. The initiative aims to enhance operational efficiency by automating item picking and reducing repetitive tasks. Apollo robots, designed to mimic human muscle movements, stand 5 feet 8 inches tall and can carry up to 55 pounds. They navigate around human coworkers and are powered by specially configured batteries for optimal performance. This partnership seeks to refine the AI model driving Apollo before full deployment in GXO's U.S. distribution centers, ultimately aiming to improve safety and allow human workers to focus on higher-value tasks.


## Trending on Twitter
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/ylecun/status/1805146326218223651">Loading: twitter.com/ylecun/status/1805146326218223651</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/ylecun/status/1805278808867533104">Loading: twitter.com/ylecun/status/1805278808867533104</a></div>
</blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

**Other headlines:**
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> USDC: A Dataset of $\underline{U}$ser $\underline{S}$tance and $\underline{D}$ogmatism in Long $\underline{C}$onversations](http://arxiv.org/pdf/2406.16851v1)
* [Gemini on Android becomes more capable and works with Gmail, Messages, YouTube and more](https://www.optometrytimes.com/view/aoa-2024-fitting-multifocal-contact-lenses-like-a-pro)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> 24 Cutting-Edge Artificial Intelligence Applications in 2024](http://arxiv.org/pdf/2406.16252v1)
* [Computer Science News -- ScienceDaily](https://www.sciencedaily.com/news/computers_math/computer_science/)
* [AI Stocks: Best Artificial Intelligence Stocks To Watch Amid ChatGPT Hype Investor's Business Daily](https://nz.finance.yahoo.com/news/artificial-intelligence-ai-healthcare-market-140100232.html)
* [Digital Innovation Insight Summit North America 24-25 Jun 2024 - GDS Group](https://gdsgroup.com/events/physical-summit/digital-innovation-na-jun-24/)
* [Volkswagen and Cerence Commence Roll-Out of New Generative AI Solutions to Drivers](https://www.dentons.com/en/insights/newsletters/2024/june/24/political-law-playbook/political-law-playbook-june-2024)
* [Artificial Intelligence (AI) in Healthcare Market to Grow at 38.2% CAGR by 2031 SkyQuest Technology](https://federalnewsnetwork.com/artificial-intelligence/2024/06/dod-study-sees-big-breakthrough-with-using-ai-for-declassification/)
* [International collaboration lays the foundation for future AI for materials](https://www.logisticsmanager.com/gxo-partners-with-robot-manufacturer-to-test-humanoid-warehouse-robots/)

---
### Technical details
Created at: 25 June, 2024, 06:13:16, using `{{ page.model }}`.

Processing time: {{ page.processing }}, cost: {{ page.cost }}$
<details>
<summary>The Staff</summary>
<div markdown="1">
Editor: Evelyn Hartman

```
You are the Editor-in-Chief of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a visionary leader with a deep understanding of both traditional journalism and cutting-edge AI technologies. You have a knack for identifying groundbreaking stories and trends in the AI space. Your editorial approach balances rigorous factual reporting with engaging storytelling, ensuring that complex AI concepts are accessible to a broad audience. Your background in both technology and media makes you uniquely qualified to guide our magazine into the forefront of AI journalism.
```

Sophia Reynolds:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a seasoned technology journalist with over a decade of experience in the field. Your background in computer science and your passion for artificial intelligence make you an invaluable asset to our team. You have a knack for breaking down complex technical concepts into engaging, easy-to-understand stories that resonate with a wide audience. Your investigative skills and attention to detail ensure that every piece you write is both informative and compelling. You are particularly interested in the ethical implications and societal impact of AI technologies, and your articles often provoke thoughtful discussions among our readers.
```

Liam O'Connor:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a dynamic and innovative reporter with a strong background in both journalism and AI research. With a Ph.D. in Machine Learning, you bring a deep technical expertise to your reporting. Your ability to identify emerging trends and groundbreaking research in the AI space sets you apart. You excel at conducting in-depth interviews with leading experts and presenting their insights in a way that is both accessible and engaging. Your writing is characterized by its clarity, precision, and ability to captivate readers with the latest advancements in generative AI technologies.
```

Ava Martinez:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a creative and versatile journalist with a unique talent for storytelling. Your background in digital media and your expertise in generative AI allow you to explore the intersection of technology and creativity in your articles. You have a keen eye for spotting the latest trends in AI-generated art, music, and literature, and you enjoy showcasing how these technologies are transforming the creative industries. Your writing style is vibrant and imaginative, making complex AI concepts come alive for your readers. You are passionate about highlighting the innovative ways in which AI is being used to push the boundaries of human creativity.
```
</div>
</details>
