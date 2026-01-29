---
title: Ideas 2026
slug: current-ideas
---

# Project Ideas (2026)

## Table of Contents

1. [Complete Student Directory](#section-1-complete-student-directory)
2. [Thematic Groups & Potential Teams](#section-2-thematic-groups--potential-teams)

---

## Section 1: Complete Student Directory

Below is a complete listing of all 55 students and their project ideas in numerical order.

### 1. Oliver Kumar {#student-1}

I am interested in exploring natural language processing techniques that have to do with the faithfulness of summaries (whether those are produced by blogs, news articles, or LLMs). Essentially, I would build something that could detect if the summary is actually representing the source text. I think it would be interesting to add a feature that highlights components of the summary that are not supported by anything (essentially a hallucination or simply a factually incorrect statement made by a human). It would go even beyond something that is simply a hallucination by also highlighting contradictions, the omission of key constraints or stipulations, or overgeneralization. This would be a great project to explore the world of natural language processing and computational linguistics.

---

### 2. Pranav Balaji {#student-2}

A team project concept idea I had was a multi-perspective news neutralizer and synthesizer. We live in an era of extremely high media polarization and different viewpoints on global topics. Because of this, understanding an "objective" truth and considering different perspectives is hard especially if you just read one article that is somewhat opinionated. I want to propose a tool that can ingest multiple articles that cover the same topic or event and can output a single, fact-verified, bias-neutral summary that explicitly highlights differences in framing. 

In theory, this could be accomplished by using vector space models to group topically related articles and seeing where in the article the semantic meaning differs through identifying differences in contextual framing. By then leveraging this information, we could use some sort of RAG pipeline to generate a report that can identify and flag potential bias. 

---

### 3. Wang Ruiyu {#student-3}

I propose building two lightweight natural language processing tools to support student learning and academic communication. The first is an Automatic Quiz Generator that helps students test their understanding of course material. By feeding in past quizzes and specifying a current lecture or topic range, the system will generate new practice questions that resemble real assessments in both style and difficulty. 

Another idea I find interesting is an Email Tone Classifier and Rewriter. This tool will allow students to target emails to predefined tone categories (e.g., PhD application emails to professors, interview requests, professional outreach, or casual messages to friends) and provide one-click rewrites to adjust tone while preserving meaning. 

---

### 4. James Broderick {#student-4}

My project idea would be a program that knows a wide variety of texts, either poems and/or novels and/or non-fiction, and could suggest specific books or perhaps authors that relate to a user based on their input. For example, somebody grieving could indicate that to the system and be recommended certain poetry. Another user could indicate that they want something lighthearted and be recommended a comedic novel. A third use case might be a user that read a book they enjoyed and wants to discover similar works. This system could be achieved either by having an LLM actually read many texts, by passing in smaller snippets of many texts, or by learning about texts through reviews or other metadata.

---

### 5. Cao Wenxuan {#student-5}

i am a beginner for cooking and when I tried to cook something, the recipe online is sometimes confusing or missing some details. It assume I know the cooking terms but actually I don’t. So I want to create a cooking assistant that reads any recipe and explains it in simpler terms, fills in the gaps, and warns people about tricky parts before they start cooking.
For example, if a recipe says "caramelize the onions" but doesn't explain how long that takes or what it should look like, the assistant would add: "This takes about 20 minutes on medium heat - keep stirring until onions turn golden brown and sweet." It would catch when recipes skip steps  without saying how long or where, and give practical tips. I want to make cooking less intimidating and prevent kitchen disasters by explaining recipes in plain language, especially for beginners who might not know cooking terminology or hidden steps.


---

### 6. Mandy Sun {#student-6}

(Idea: Sustainability detector for retail fashion companies) My concept involves developing a tool that can assess the credibility of sustainable claims made by fashion retail companies. In today’s current market, many retail companies engage in “green-washing,” where companies tag their products with superfluous or false claims of environmentally friendly production materials or techniques, and it’s become harder for consumers to evaluate if a product has been produced through sustainable means. This tool could determine the level of sustainable credibility through individual product descriptions and company mission statements. Additionally, it would utilize external sources, like news articles on a company’s new clothing trends, production processes, or even negative articles related to scandals or controversies.

---

### 7. Yuxuan Yang {#student-7}

As a lot of services now, in the era of technology, are digitalized, a large proportion of elderly people are left behind and have little idea how to deal with different apps or websites when they are not with their children. Appointment scheduling, checking lab test results, and viewing electronic medical records are all done online, and my grandma, as an example, has not been able to do any of these through her phone without help from my parents. General conversational AI often fails to give accurate instruction due to unfamiliarity with those interfaces. Therefore, I want to design an extension embedded into commonly used healthcare websites or apps to accept text-based function-related questions from users and then give step-by-step instructions to users. It is similar to Cursor for healthcare apps. Due to time limitations, one major patient portal or appointment system will be selected to build the extension.

---

### 8. Jiawen Ren {#student-8}

Project Idea: “Legal Similarity Search” for Precedents & Arguments
This project builds a legal tool where user pastes a paragraph from a motion or brief, and the system retrieves the most relevant similar arguments or case summaries, then highlights the key differences (for example: "their facts involve X, but yours doesn’t"). The pipeline uses embedding-based similarity search over a vector database to find candidate matches, then reranks those candidates using a stronger model such as a cross-encoder or an LLM-based reranker. Optionally, the system generates short grounded summaries explaining why each result is similar and how it differs from the user’s text. Data can come from open legal corpora (case summaries, judicial opinions, public briefs) or from a smaller curated dataset if one wants a tighter scope. This can help not only attorneys but individuals who don’t have legal training but need to understand whether their situation resembles existing cases or common arguments, such as tenants reviewing housing disputes, employees dealing with contract issues, or small business owners responding to a demand letter, by quickly surfacing relevant precedents and clearly explaining the key similarities and differences in plain language

---

### 9. Xu Yida {#student-9}

Using NLP to Identify Disease Related Signals from Social Media
Many people post about feeling sick or missing school or work because of illness on social media. At the same time, there are also many posts that shares news, jokes or random things. This makes it difficult to directly use social media data to understand health trends. In this project, I am looking forward to use NLP techniques to identify health-related posts from social media text. I will also try to look at how the number of health-related posts change over time to identify if there is a trend or what. This analysis could be useful for future research on health-related signals in social media.

---

### 10. Lucas Stein {#student-10}

Initial team project idea: Creating an AI detector.

 Uncover the text patterns (and potentially different ones) that LLMs such as Claude, Gemini, GPT, and Groq output. Determine what makes a sentence, paragraph, or essay AI-generated and how to assign a percentage to it. Very similar to https://quillbot.com/ai-content-detector. I hope that doing this project will help me learn about the biases and patterns of AI and how to avoid writing like AI so individual work can clearly stand out.

---

### 11. Hanyang Sun {#student-11}

I have two ideas about the project. 
The first idea is an LLM Answer Reliability Checker. Users paste an answer generated by a language model, and the system analyzes it for signals like vague wording, hedging, or claims that sound confident but lack support. The tool highlights parts of the response that may need fact-checking and suggests follow-up questions, helping users better judge whether an answer is trustworthy instead of blindly accepting it.
The second idea is an Explanation Gap Detector designed for learning support. Users input explanations from lecture notes, textbooks, or AI responses, and the system looks for skipped steps or hidden assumptions that could confuse learners. It then points out where the explanation jumps too quickly and provides short clarifications. Both ideas aim to create practical, easy-to-use tools that make LLM outputs more reliable and easier to learn from.

---

### 12. Ethan Hsiung {#student-12}

I am thinking of something that can quickly describe a brand or specific product in as many adjectives as the user sets based on online reviews.

When a user buys a product from a brand they are not familiar with, they could use this bot to scrape all reviews online, both text-based (ie, from product reviews or forum discourse) and in video form. The analysis would return the words most commonly used to describe the brand or product, or synonyms for similar words.

Once the analysis is finished, the user could input the number of adjectives to describe the brand or product, and the bot could return the adjectives and strength scores based on the % of reviewers describing it as such. If the user wants more elaboration, the bot could give a quick summary, and if the user wants more specific words, they could increase the input.

---

### 13. Kyra Bauer {#student-13}

I don’t have strong attachments to any ideas, and I am open to most things at this point. One idea that I had that I think could be pretty interesting is to make something to do spam detection using NLP techniques, whether that is emails, text messages, reviews, etc. It could be something that you put the text into to check, or if it’s something more contained like email it could be an automatic filter. I am not super familiar with computational linguistics and NLP, so I am absolutely open to other thoughts.

---

### 14. Srijon Sarkar {#student-14}

Do vision models 'understand' prompts the same way language models do? I want to understand the correlation or dependence between the image generation by prompt and the segmentation of the objects in the same image, achieved using the same prompt via SAM3. This could be replicated across different image generation models and used to understand memory coordination between SAM3 and the corresponding models. Also, measure if segmentation remains consistent across paraphrases. A rank-based system measuring putting numerals on the distance between synonyms or words could further be analyzed to see how certain groupings correspond to better segmentation or image generation as opposed to others.

---

### 15. Andrew Jaffe-Berkowitz {#student-15}

A research project to investigate whether LLMs can identify their own writing. We would test various LLMs to see if they can distinguish between their output and human responses or even another LLM’s response. We would generate paired sets of answers to the same prompts from the target model itself, humans, and other LLMs, then ask the target model to label which responses are its own. We would measure accuracy against calibrated baselines such as random guessing, always predicting "not me," and simple statistical classifiers to determine whether the model is doing more than exploiting priors. The outcome would be empirical results showing when correct identification exceeds random chance, which transformations prevent correct identification, and whether any apparent self-recognition generalizes across topics and sampling settings.

---

### 16. Ramlah Amer {#student-16}


The International Phonetic Alphabet (IPA) is a system of symbols used to represent virtually any sound across human languages. It aims to document/reproduce speech with consistency and precision. While IPA is widely used in sociolinguistics, language learning, and speech-language pathology, manual transcription is deeply time-consuming and requires expertise, making it largely inaccessible to most users. This project aims to leverage large LLMs and speech-to-text models to automatically generate accurate IPA transcriptions from spoken English datasets. By making IPA more accessible, this project can support linguistic research, improve pronunciation modeling, and enable phonetic analysis across diverse disciplines. Moreover, it facilitates understanding of speech variation in an increasingly multicultural world, providing a tool for both practical language learning applications and advanced phonetic study.


---

### 17. Esther Fu {#student-17}

As students, we have always been asked to fact-check by cross-referencing information from multiple reliable sources, a process that can feel inconvenient. My project idea is to create a tool that can compare two or more articles or passages of a user's choice, and output features such as word token overlap, unique word types, semantic similarity and differences, tone differences, and more. Furthermore, to help users focus on relevant content, a keyword search feature can be implemented so that only text related to the keyword is compared. The tool can be in the form of a browser extension or an external webpage, and hopefully, it can help students streamline the process of fact-checking.

---

### 18. Charles Cook {#student-18}

Much of the rhetoric used by politicians carry covert meanings with a specific goal, such as promoting fear or evoking a certain image. I would like for a tool to exist that would analyze speeches delivered by politicians to understand how they are using certain words to convey a message. Through frequency and sentiment analyses, this tool would be given various speeches and their dates and be able to model how the frequency of certain words or phrases have changed and the semantic meanings associated with words or phrases as they are used in a speech. The goal of the tool would be to understand how the meanings and tonality of certain words used by politicians has changed over various years, which will give us insight as to the power of words in promoting an agenda.

---

### 19. Zou Chengru {#student-19}

Cosine similarity is widely used to measure proximity between word embeddings, but it implicitly assumes a Euclidean geometry. In modern NLP, contextual embeddings often exhibit complex, irregular structure—better described by manifolds or non-Euclidean geometries (e.g., hyperbolic spaces)—so cosine proximity can be misleading: two tokens may appear close by cosine distance yet differ substantially in meaning.

To address this, we propose a geometry-informed post-processing step that maps embeddings from an irregular latent space into a representation where Euclidean similarity is more faithful. We consider both graph-based Laplacian mappings and learned metric transformations (e.g., Mahalanobis distances) to better align geometric proximity with semantic similarity. We then evaluate the resulting embeddings on downstream tasks to quantify improvements in performance and robustness.

---

### 20. Coralynn Yang {#student-20}

A project concept related to computational linguistics is investigating how semantic meaning differs across languages and whether or not words that are understood as 'identical' across languages truly are: ie. honorific pronouns in East Asian languages vs. static ones in English and how much denotation / connotation play into linguistic difference. 

These results could be at the macro level of language or specific components of a language such as syntactic structure, grammar, types of words or certain phrases, potentially providing insights into meaningful cultural or linguistic differences in communication. 

The project could also compare different NLP techniques: ie. contextual embeddings and determine whether or not one is more effective at capturing semantic meaning. This could also raise interesting questions related to LLMs and how they are being used for cross-language translation.

---

### 21. Sumaya Abdi {#student-21}

This project examines how biological research abstracts use hedging language to express uncertainty and avoid strong scientific claims. In biology, researchers often rely on cautious language when evidence is incomplete or probabilistic, making hedging an importing feature of scientific communication. This study focuses on identifying common linguistic markers of speculation, such as modal verbs and hedging phrases, and examining how frequently they appear in biology abstracts. By comparing patterns of hedging across texts, the project aims to show how uncertainty is systematically encoded in biological scientific discourse. Overall, the project highlights how linguistic choices reflect scientific caution and help researchers balance explanation with responsible interpretation of results. 

---

### 22. Anushka Basu {#student-22}

I want to build an LLM-based translation pipeline for short strings where context is limited and tiny word choices matter, like UI labels, system messages, or scientific terms. The workflow would begin with consistent text processing to preserve punctuation, placeholders, and token boundaries across runs. For each string, the model would generate candidate translations and create a terminology glossary so key terms remain consistent across the entire dataset. We’d compare this glossary-aware pipeline to a baseline translation approach, and evaluate using a mix of automatic checks and human review when possible. We’d flag recurring linguistic issues, such as inconsistent terminology, awkward register, and mismatches in formality. The project would ideally test at least two language pairs on a small curated dataset (and find native speakers to review our progress) and document what kinds of errors persist when the source text is short and underspecified. I’ve previously built a similar workflow, so I can provide the initial prompts and setup while teammates help with data curation, evaluation design, and analysis tied to course topics.


---

### 23. Claire Burkhardt {#student-23}

Writing style/personality detector: this would use textual linguistic profiling to analyze and correlate writing styles. What makes writing styles sound distinctive? How do writing styles correlate to social groups (ie age) or context (ie business, academia, social media, etc.). It could look at communication styles on different text-based social media platforms (reddit vs. Stack Overflow vs. X vs. Quora). It could become a fun generator/Spotify-wrapped type application (your writing style is closer to Hemingway than Orwell!). Or it could be used to examine hallmarks/characteristics of writing in different contexts with an eye towards social profiling and analysis — ie. Do reddit users sound more like business folks or academics?


---

### 24. Zhe Jin {#student-24}

I‘d like to make a web tool,which will compare the writing styles of two texts, determine if they are likely written by the same author, and provide an explanation of "why." The user will input two paragragh of text, eg. two short articles, two emails or two comments. The system will auto abstract some easily understandable stylistic features, eg. average sentense length, distrubution, variaty of words(vocab, such as type-token ratio), function-word usage (e.g., “and”, “but”, “the”), punctuation patterns, and common word/character n-grams. A simple classifier (e.g., logistic regression or SVM) produces a similarity score, and the interface visualizes which features contribute most to the decision so the result is interpretable, not a “black box.” Our goal is to make authorship-style analysis approachable for students while demonstrating core NLP ideas like feature engineering and text classification. We will evaluate the tool using small benchmark datasets and basic accuracy plus user feedback on clarity of explanations.

---

### 25. Shuyan Zheng {#student-25}

I want to build an AI-powered research assistant that helps scholars quickly find relevant academic papers and discover new research directions. Users can input keywords, research questions, or short descriptions of their topic, and the system will search across paper databases (PubMed, Semantic Scholar, etc.) by analyzing abstracts, titles, keywords, and key sections using NLP. Instead of returning only a long list of papers, the tool will rank results by relevance, summarize main contributions, and also highlight why each paper is useful. Beyond paper retrieval, the system will analyze the user’s research area and suggest related or adjacent topics, emerging trends, and other interdisciplinary connections. This feature aims to inspire creativity, broaden perspectives, and help users generate novel research ideas. The platform could also include citation mapping, topic clustering, and personalized recommendations based on the user’s reading history.

---

### 26. Yuigo Ueyama {#student-26}

Perhaps comparing language and grammar features between modern and historical English texts by investigating how NLP models may be designed to parse either. Errors may be introduced by different or less standardised spellings, as well as the presence of different structures like genders and certain cases. If an NLP approach is successful on, say, modern English, it could also be applied to earlier texts to see what errors it makes and test if these errors are similar to what a human might make. It may also be interesting if incorporating sister languages like some sister languages in model construction could yield better results.

---

### 27. Hsin-Yu Chen {#student-27}

I would like to analyze emotional tone and sentiment across music genres using NLP applied to the song lyrics. It will collect lyrics from multiple genres such as pop, hip-hop, and R&B, and use tokenization, sentiment analysis, and lexical emotion dictionaries to classify words as positive, negative, or emotion-specific (e.g., happiness, sadness, anger, or confidence). The goal is to examine whether certain genres consistently express distinct emotional profiles, such as hip-hop may show stronger expressions of anger or confidence, while R&B may emphasize themes of heartbreak or vulnerability. By comparing sentiment patterns across genres, I would like to explore how musical genres are reflected through emotional language, and whether genre labels align with the emotional content of lyrics.

---

### 28. Qingyang Liu {#student-28}

The project I am going for is news related. The world is changing rapidly around us, and it is difficult to keep up with everything that is happening. To make this matter worse, different news agents around the globe could report the same incidence from very different prospective. I want to develop an app that help individuals filter news and extract the ground truth by collecting the same news from different new websites. They could be American, European, Asian, or just any press. The news are first processed by NLP, extracting important information from the whole text. Then, we could use LLM API to generate response for the user and tell them what information that these news are truly revealing. 

---

### 29. Jaeyeon Lee {#student-29}

I am open to other ideas but here are a couple:

1. Sentiment Analysis for E-commerce (Amazon) Reviews : A goal is to analyze customer reviews beyond star ratings (common feature in Amazon but extent to in which it helps decide is limited). Given a product link, the model aggregates review text to generate both a numerical score and short advice indicating whether the product is worth purchasing.

2. Detecting Sponsored or Fake Reviews: Similarly to the idea above, this aims to investigate whether online reviews are genuine or sponsored. The model estimates the likelihood that a review was written for promotional purposes rather than real user experience.

3. AI Hallucination: This goal of this idea is to study AI hallucinations—confident but incorrect model outputs. Analyzing when hallucinations occur across different prompts and tasks (if too broad, I’m open to narrow it down to a certain topic/area), aiming to identify reliability signals and explore ways to assess and communicate AI trustworthiness to users.

4. Spam SMS Classification: Classify SMS messages as spam or legitimate.


---

### 30. Qile Rao {#student-30}

I would like to make a tool that improves user experience in in-car voice assistants by accurately interpreting driver intent, context, and emotional state. Using a dataset of simulated or real-world voice commands (e.g., navigation requests, climate control, media selection, or complaints), the project analyzes how linguistic features such as intent phrasing, ambiguity, politeness, urgency, and sentiment affect system responses. The project aims to model how different language choices reflect user expectations and how adaptive, context-aware responses can lead to a smoother and more intuitive in-car interaction experience.

---

### 31. Carl Yu {#student-31}

I am interested in a project that focuses on understanding the biases and prejudices associated with a piece of text, such as in media publications. This could potentially be done using sentiment analysis to identify the opinion of an article, as well as keyword analysis to identify what particular phrases coincide with particular sentiments. Articles' sentiments/keywords can also be compared with either other works by the same author or other works of the same topic. Additionally, if within the scope of this course, this could also be expanded to apply to not only written text, but also spoken word to assess how certain linguistic features of speech (e.g., suprasegmentals, accents, dialects, tone) could be linked to particular biases.

---

### 32. Kenneth Hou {#student-32}

I am proposing a project to build an AI-driven agent that **automates the job application process**. The system will use an LLM-powered backend to parse my resume and analyze job descriptions to ensure a high semantic match.

The core functionality includes a RAG pipeline for resume tailoring and a browser automation component using Selenium to navigate job boards and auto-fill application forms. My goal is to create a tool that handles everything from "finding a fit" to "clicking submit" with minimal human intervention. I plan to use Python for the backend, database not sure yet, and a React-based dashboard to track the agent’s progress.

---

### 33. Timothy Lim {#student-33}

I would want to try to use large language models to constantly detect changes in writing patterns over time, scouring over data gathered from specific users. This would be built for long term or analyzing large amounts of such data, in particular gaining an understanding of the characteristics that the user would have in language (e.g., tone, sentence structure, grammaticality, formality). With LLMs able to draw upon sentiment in data and find features well, this would be a challenging expansion of that purpose. This could help in certain research paths, analyzing changes from different writing environments, or as a good measure of aptitude and improvement measures for some of these changes. 

---

### 34. Li Mingyang {#student-34}

I want to build a AI agent framework which enables ReAct Agent, Tool-Calling Agent, Plan-and-Solve Agent, and Multi-Agent Communication and Collaboration. Based on this framework, We could easily develop multiple AI applications such as Workflow, Deep ReSearch, Agentic Coder, CharacterAgent. This project will not use existing framework such as langchain, langgraph, or crawai, etc. This project will based on google's white book of developing AI agent via 5 days (which can be easily found in gaggle), where it includes multiple principles and architectural standards for building ai agent application. The tool calling functionality will follow the same paradigm in MCP, and Multi-Agent Communication will follow the paradigm of A2A. 

---

### 35. Jianing Fu {#student-35}

I want to build an analysis tool that compares how the same historical event is narrated across different sources. This tool will help historians summarize general characteristics of the historical event while demonstrating bias and different perspectives of the authors. It may look at the style, tone, word choice, grammatical correctness, similarities/differences, among other factors. Some key tasks to be implemented by NLP include looking for text similarity, keyword and framing divergence, and possibly classification sentiment analysis. Possible sources may include travel accounts describing the same city written by Western and Eastern travelers, foreign/local accounts reporting the same event, newspaper articles, biographies, etc. 

---

### 36. Heewon Jin {#student-36}

A project idea I have utilizing NLP is to determine whether faster publication correlates with lower factual reliability in early news coverage. Modern news organizations operate under intense pressure to publish quickly, especially during breaking events like mass shootings, elections, natural disasters, etc. While speed helps outlets stay competitive and to spread important information quickly, premature reporting risks spreading misinformation that can shape public perception before corrections are issued. Through this project, it may be useful to analyze linguistic features including hedging language, modal verbs, and explicit correction markers to evaluate if those articles are more likely to be revised or corrected over time.

---

### 37. Huang Benjamin {#student-37}

As I’m majoring in biology, I often find it difficult to quickly extract useful information from the large volume of biomedical literature. In particular, it can be time-consuming to identify which other proteins or biological pathways are frequently mentioned if our protein or gene of interest is changed.
For this project, I am interested in using natural language processing techniques to analyze the provided scientific papers and identify patterns of co-occurrence between a target protein/gene and other related proteins or biological pathways. The goal is to summarize and highlight commonly associated proteins or pathways from the text, which could help researchers more efficiently narrow down potentially meaningful candidates for further investigation.


---

### 38. Kevin Cho {#student-38}

I am interested in building a simple NLP-based system that processes written natural disaster reports, such as descriptions of hurricanes, wildfires, and floods, and extracts important information from the text. The system would identify key details like the type of disaster, the location where it occurred, and the date of the event. This project would focus on basic NLP techniques such as tokenization, keyword matching, and pattern recognition rather than advanced models. The goal is to explore how unstructured environmental text can be converted into structured data that is easier to analyze, which could help support basic disaster monitoring and response efforts.

---

### 39. Chloe Peyrebrune {#student-39}

I would be open to any project ideas but one idea that seemed interesting to me was a model that recommends movies. It could use plot summaries from different websites to recommend movies that are similar to a given movie. It could use sentiment analysis of movie reviews to either recommend a movie or not, or to recommend movies with similar reviews. I am not sure yet which exact data sets could be used for something like this but IMDb or MovieLens could be good options. Another idea would be to take a review of a movie and find users who gave similar reviews and recommend movies that those users have rated highly. 


---

### 40. Yiyun Chen {#student-40}

I want to build an instruction parser that converts school assignment or homework instruction PDFs into a clear, step-by-step checklist. The input to the system is the text extracted from an assignment or homework handout, where requirements are often written in long paragraphs. Using techniques from the course, I will tokenize and lemmatize the text, analyze word frequencies to identify action verbs and sequencing cues, and represent sentences using bag-of-words and TF–IDF vectors. The system will classify sentences as actions or conditions and infer ordering using temporal language such as “before” and “after.” The output is an ordered checklist that explicitly states what steps must be completed and in what order. For example, given the instruction “Before submitting, create the required files and run the program to verify the output,” the system outputs two ordered steps with a dependency indicating that file creation must occur before running the program.

---

### 41. Zichen Wang {#student-41}

For this project, I propose to investigate semantic drift by examining how the meanings of words change over time using distributional semantic models. Using large text corpora such as news articles, political speeches, or social media collected from different historical periods, we construct word and sentence embeddings for each time slice and analyze shifts in semantic neighborhoods using cosine similarity. By tracking changes in nearest neighbors and vector distances, we quantitatively measure how concepts such as technology and identity evolve in response to social, political, and cultural contexts. The project compares classical vector space models, including TF-IDF and Word2Vec, with contextual embedding models to evaluate their effectiveness in capturing semantic change. Results are visualized using dimensionality reduction techniques to provide interpretable insights into language evolution over time.

---

### 42. Olivia Joyner {#student-42}

I am open to any project ideas for this class. I hope to be able to collaborate with people in class. I would like to do something geared towards job selection. 
An idea I have is a tool that can analyze job descriptions and pick if it is a good pick for a user based on resume and work experience. With this tool and its extraction capabilities, I hope to create a useful tool for those who need help finding jobs that fit their skills and interests. I am also interested in adding a feature that can help with researching a job opportunity. If a user is interested in what goes into a certain career, maybe the tool can give the person suggestions based on extracted information.

---

### 43. Shaun Baek {#student-43}

Ever wonder why some posts explode with thousands of upvotes while others just vanish into nothing? I think about this probably more than I should. This project explores the linguistic patterns behind Reddit virality: what words, phrases, and structures actually get people to engage.

We will collect posts from various subreddits and analyze stuff like title phrasing, sentiment, emotional triggers, and readability. The end goal is building a model that predicts upvote potential before you even post. I want to know if it's the wording, the timing, or just random luck.

We want to understand online engagement, content recommendation systems, maybe even detecting rage bait designed to manipulate people. This could be applicable to other platforms.

---

### 44. Brady Westergren {#student-44}

One project idea I have is to detect emotional distress markers in patient messages to healthcare providers. Patients may use these chat tools to express anxiety, confusion, or frustration. These messages may often go unnoticed in busy clinical settings or when providers aren't working. The project would analyze short written messages  and classify them based on emotional tone (high distress, low distress, etc). The model would be intended as an assistive, non-diagnostic tool that is for ethical use rather than clinical decision-making. By flagging these messages, this tool can help providers prioritize responses and quickly give relevant resources. The project focuses on simplicity to address a meaningful healthcare communication challenge.

---

### 45. Alan Wei {#student-45}

This project can be about how natural language processing can be used to analyze language sentiment and risk signals cross crypto-currency related text, from sources such as X, Reddit, and crypto news, we can classify text in different ways. There are many implications with crypto since it can change very fast, so transformers with different text embeddings as an example can provide more insight towards crypto movements. Catching the major market crashes before they might happen could be crucial in succeeding in such an innovative space with everything run on decentralized applications. The goal is also to understand how collective language can reflect market psychology and informational risk's role in decentralized finance.

---

### 46. Mohamed Ali {#student-46}

Networking tool -
A browser extension that analyzes your LinkedIn profile and suggests meaningful connections based on shared interests, skills, career trajectories, and educational backgrounds. Unlike LinkedIn's basic "People You May Know" feature, this tool uses machine learning to identify professionals with complementary expertise, similar career goals, or overlapping project interests.

The extension scans profile data including job titles, skills, industries, and post engagement patterns to calculate similarity scores. It then surfaces high-potential connections with personalized conversation starters based on shared interests. Users receive weekly digests of top matches and can filter by criteria like location, seniority level, or specific skills.

The tool addresses a critical pain point: LinkedIn has over 900 million users, making it overwhelming to find genuinely relevant connections. By leveraging NLP and similarity algorithms, Smart Connect transforms networking from spray-and-pray to strategic relationship building, helping users build valuable professional networks efficiently. 

---

### 47. Samuel Besley {#student-47}

My project idea is a system that detects real-time quality degradation (or writing fatigue) during document composition. It would establish a document specific baseline from the opening section, and then evaluate the text to produce a fatigue score using various signals. It would have some sort of a tiered rating for your writing quality, and make sure to not give early false alarms based on just a few sentences. The overall goal would be to just help avoid burnout. Ideally it could work with different writing types(email, academic, creative, etc), and have another model to detect which it is working with to have more specific feedback. 

---

### 48. Nicholas Melamed {#student-48}

My idea consists of using word processing identifiers in relation to the financial sector. This entails using company quaterly announcements or any extra information and running through a word processor to assign each word an impact score. this can be  used to make predictions in the markets based off of what is being announced. 

---

### 49. Zhixiang Wu {#student-49}

1. Build a sequence labeling model that identifies how bilingual speakers switch languages in sentences, so we can analyze why the switches happen, whether it is because of grammatical boundaries or struggling the the hybrid meaning of words. This project to better help us understand the differences between languages. 
2. Fine tuning a model for domain adaptation. For example, companies release annual sustainability reports and sometimes some of them will try to use vague or misleading languages to sound more environmental friendly than they are, so we can build a classification model for labeling the vague sentences in pdf reports. 
3. Another example to fine tune a model for domain adaptation is finding potential risks in legal contract. The legal contracts nowadays are usually long and boring for reading. However, we can fine tun models for more finding clauses related to risks such as liability and termination conditions or policies.

---

### 50. Zhang Jinghao {#student-50}

I’m interested in building an NLP-based application where users can either type text or record short audio messages, which are automatically transcribed and analyzed to infer emotional or stress-related states. Beyond basic sentiment analysis, the application would identify richer linguistic signals such as emotional intensity, variability in language use, semantic coherence, and shifts in temporal orientation (e.g., past- vs. future-focused language). These features would be combined to generate interpretable feedback, such as a stress score, emotional profile, or visual summary of language patterns over time.

---

### 51. Mingke Tian {#student-51}

I'd like to explore ideas on understanding the reasoning behavior of multimodal large language models. While these models perform well on many vision–language tasks, it is unclear how stable their reasoning is when the textual input changes but the meaning stays the same. We can keep the visual input fixed and rewrite the accompanying text using different linguistic formulations, such as alternative sentence structures or phrasing. Then analyze whether the model produces consistent reasoning and final answers across these variations. Instead of trying to improve model performance, we can study how sensitive multimodal reasoning is to linguistic form and where failures occur. Through systematic comparison and analysis, we aim to better understand how multimodal models integrate language and vision during reasoning, and to explore limitations of current multimodal reasoning systems.

---

### 52. Chloe Zhao {#student-52}

An idea for an NLP project is a sentiment analysis for news articles and similar media to detect biases. The model would analyze specific words, as well as tone and framing, to decide if works of media are more facts- or opinions-based. There can be analyses on objectivity vs subjectivity and emotional language. One could input an article, or maybe even just a headline, to receive a report assessing how reliable the source is. 

---

### 53. Sharon Li {#student-53}

I am interested in building an NLP system that automatically extracts PICO (Population, Intervention, Comparison, Outcome) elements from clinical trial abstracts. PICO is commonly used in medical research and biostatistics, especially for systematic reviews and meta analyses, but identifying these elements manually is time consuming and labor intensive. Therefore, the idea of this project is to first classify sentences in an abstract by what role they play (for example, whether a sentence is talking about the population or the outcome), and then try to extract the exact text that matches each PICO category. By turning unstructured medical text into more structured data, this tool could help make medical literature review more efficient.

---

### 54. Jonathan Velazquez {#student-54}

Im not too sure about the feasibility of this project, but I think an interesting project could be to look at some popular wikipedia pages, and then look at how in different languages the emphasis/meaning of the article changes, due to certain limitations like language constraints. We could use NLP techniques to identify thing such as frequency and use LLMs to actually translate the content of the words and through that get a better understanding of how language can change the meaning of articles. We can also measure which facts are omitted in each language to quantify differences in knowledge representation.

---

### 55. Riyaa Randhawa {#student-55}

Project Concept: Error Analysis of Tokenization and Offset Alignment in Modern NLP Pipelines
This project will explore how modern English tokenizers handle real world text and where they fail from a computational linguistics perspective. Rather than focusing on overall performance, we will conduct a comparative error analysis of multiple widely used tokenizers across different text domains, including academic writing, informal social media text, and proper nouns such as person/place names. We will specifically examine token fragmentation patterns and character offset alignment to analyze how tokenization decisions affect downstream tasks like named entity recognition and span based annotation. By quantifying tokenizer disagreement and identifying recurring linguistic failure modes, this project will aim to highlight limitations in current tokenization approaches. Our goal is to better understand how low level linguistic processing choices influence higher level NLP behavior, with implications for robustness, interpretability, and fairness in language technologies.

---

## Section 2: Thematic Groups & Potential Teams

Students are organized by thematic interests to help identify potential teammates. If you're interested in a particular theme, consider reaching out to others in that group.

### Text Analysis & Verification (7 students)

*Projects focused on fact-checking, faithfulness, reliability, and detecting AI-generated content*

**Students in this group:**

- [1. Oliver Kumar](#student-1)
- [10. Lucas Stein](#student-10)
- [11. Hanyang Sun](#student-11)
- [13. Kyra Bauer](#student-13)
- [15. Andrew Jaffe-Berkowitz](#student-15)
- [17. Esther Fu](#student-17)
- [29. Jaeyeon Lee](#student-29)

---

### News & Media Analysis (7 students)

*Projects analyzing news bias, multi-perspective synthesis, and media polarization*

**Students in this group:**

- [2. Pranav Balaji](#student-2)
- [18. Charles Cook](#student-18)
- [28. Qingyang Liu](#student-28)
- [31. Carl Yu](#student-31)
- [35. Jianing Fu](#student-35)
- [36. Heewon Jin](#student-36)
- [52. Chloe Zhao](#student-52)

---

### Domain-Specific NLP (7 students)

*Projects focused on specialized domains like finance, biology, or disaster response*

**Students in this group:**

- [21. Sumaya Abdi](#student-21)
- [30. Qile Rao](#student-30)
- [37. Huang Benjamin](#student-37)
- [38. Kevin Cho](#student-38)
- [45. Alan Wei](#student-45)
- [48. Nicholas Melamed](#student-48)
- [49. Zhixiang Wu](#student-49)

---

### Advanced NLP Research (7 students)

*Projects exploring theoretical aspects like embeddings, semantic drift, and model reasoning*

**Students in this group:**

- [14. Srijon Sarkar](#student-14)
- [19. Zou Chengru](#student-19)
- [26. Yuigo Ueyama](#student-26)
- [34. Li Mingyang](#student-34)
- [41. Zichen Wang](#student-41)
- [51. Mingke Tian](#student-51)
- [55. Riyaa Randhawa](#student-55)

---

### Sentiment & Emotion Analysis (6 students)

*Projects analyzing emotional content, sentiment, and psychological signals*

**Students in this group:**

- [18. Charles Cook](#student-18)
- [27. Hsin-Yu Chen](#student-27)
- [31. Carl Yu](#student-31)
- [44. Brady Westergren](#student-44)
- [50. Zhang Jinghao](#student-50)
- [52. Chloe Zhao](#student-52)

---

### Content Recommendation (6 students)

*Projects building recommendation systems for books, movies, jobs, or research papers*

**Students in this group:**

- [4. James Broderick](#student-4)
- [25. Shuyan Zheng](#student-25)
- [32. Kenneth Hou](#student-32)
- [39. Chloe Peyrebrune](#student-39)
- [42. Olivia Joyner](#student-42)
- [46. Mohamed Ali](#student-46)

---

### Healthcare & Medical NLP (4 students)

*Projects focused on healthcare communication, medical literature, and patient support*

**Students in this group:**

- [7. Yuxuan Yang](#student-7)
- [9. Xu Yida](#student-9)
- [44. Brady Westergren](#student-44)
- [53. Sharon Li](#student-53)

---

### Writing Style & Authorship (4 students)

*Projects focused on writing style analysis, authorship detection, and personality profiling*

**Students in this group:**

- [23. Claire Burkhardt](#student-23)
- [24. Zhe Jin](#student-24)
- [33. Timothy Lim](#student-33)
- [47. Samuel Besley](#student-47)

---

### Translation & Cross-Language (4 students)

*Projects exploring translation, cross-language comparison, and multilingual analysis*

**Students in this group:**

- [20. Coralynn Yang](#student-20)
- [22. Anushka Basu](#student-22)
- [49. Zhixiang Wu](#student-49)
- [54. Jonathan Velazquez](#student-54)

---

### Consumer & Product Analysis (3 students)

*Projects analyzing reviews, products, sustainability claims, and e-commerce*

**Students in this group:**

- [6. Mandy Sun](#student-6)
- [12. Ethan Hsiung](#student-12)
- [29. Jaeyeon Lee](#student-29)

---

### Educational Tools (3 students)

*Projects creating learning aids, quiz generators, assignment parsers, and explanation tools*

**Students in this group:**

- [3. Wang Ruiyu](#student-3)
- [11. Hanyang Sun](#student-11)
- [40. Yiyun Chen](#student-40)

---

### Legal & Professional Applications (1 student)

*Projects focused on legal text analysis, professional communication, and contract analysis*

**Students in this group:**

- [8. Jiawen Ren](#student-8)

---

### Social Media & Online Content (1 student)

*Projects analyzing social media patterns, virality, and online engagement*

**Students in this group:**

- [43. Shaun Baek](#student-43)

---

### Cooking & Recipe Assistant (1 student)

*Projects focused on cooking assistance and recipe understanding*

**Students in this group:**

- [5. Cao Wenxuan](#student-5)

---

### Speech & Phonetics (1 student)

*Projects involving speech-to-text, IPA transcription, and voice analysis*

**Students in this group:**

- [16. Ramlah Amer](#student-16)
