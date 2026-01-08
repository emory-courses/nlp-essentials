---
title: Ideas 2025
---

# Project Ideas 2025

## Project Groups by Theme

### A. Career Development & Professional Tools

#### Resume & Cover Letter Analysis

* **Amoakohene, Humphrey**: NLP system to analyze and rank resumes based on job descriptions
* **Kansal, Rhea**: System to extract key skills from resumes and match with job descriptions
* **Wen, Yuanhuizi**: AI-powered resume-to-job matching system using neural networks
* **Zahid, Zeshan**: Web app for resume editing and optimization
* **Ambrose, Daniel**: Smart cover letter generator using job description keywords

#### Job Application Tracking

* **Arshavsky, Mark**: Email-based internship application tracking system

### B. Content Analysis & Verification

#### Media Bias & Fake News Detection

* **Dattatreya, Maya**: Sentiment analysis for detecting tone and bias in media
* **Jerry Xing**: Program to evaluate media bias levels
* **Kansal, Rhea**: Fake news detection system
* **King, Marisa**: Analysis of media word choices based on demographic factors
* **Suh, EunGyul**: Fake news detector for social media
* **Yoon, James**: Tool for identifying bias in journalism using sentiment analysis

#### Academic & Research Analysis

* **Ahn, Eric**: Academic paper simplifier for general audiences
* **Xu, Jack**: Sentiment analysis tool for evaluating research paper quality
* **Xinyuan, Hu**: Tool to evaluate research paper credibility
* **Okumura, Harutoshi**: LLM-based contradiction detection in political speeches

#### Review & Sentiment Analysis

* **Chen, Angelina**: Bot detection in Amazon product reviews
* **Coulanges, Charlington**: Sentiment analysis chatbot for platform reviews
* **Gyul Kim**: Analysis of healthcare system and doctor reviews
* **Hou, Carol**: Sentiment analysis for social media posts
* **Sezgin, Alas**: Dogwhistle detector for social media
* **Yeruva, Sujith**: Stock sentiment analysis from financial discussion platforms

### C. Content Generation & Processing

#### Text Simplification & Accessibility

* **Pham, Chloe**: Translation of academic text to accessible language
* **Yirdaw, Elshaday**: Readability analysis tool with improvement suggestions
* **Yuxuan, Shi**: Medical text simplification for patient education

#### Creative Writing & Story Generation

* **Zhang, Jingzhi**: Interactive life story generator
* **Wu, Junting**: Poetry style analysis and classification
* **Sixing, Wu**: Context-aware reply generator for various scenarios

### D. Educational Tools

#### Course Selection & Academic Planning

* **Hu, Yutong & Shah, Jiya**: Natural language-based course recommendation system

#### Study Aids

* **Jarman, Robert**: Pocket Teaching Assistant for lecture note processing
* **Yirdaw, Elshaday**: Vocabulary building tool

### E. Language & Translation

#### Language Understanding

* **Chang, Ridge**: Idiomatic expression translator across languages
* **Dahiya, Rishita**: Context-based word definition tool
* **Kim, Olivia**: Hand gesture and NLP integration system

### F. Content Classification

#### Genre & Style Analysis

* **Correa-Perez, Nicholas**: Music genre and lyrics analysis
* **Jennings, Caleb**: Author style prediction model
* **Jitngamplang, Varakorn**: Music mood and theme analyzer
* **Mi, Renzhi & Xiaotong, Liu**: Book genre classifier based on word patterns

### G. Code Analysis & Documentation

#### Code Quality

* **Carrier, Emma**: Code syntax analysis and improvement tool
* **Shah, Riyan**: Automated code documentation generator

### H. Data Processing & Analysis

#### Financial Analysis

* **Jiang, Jenny**: Financial news summarizer
* **Reicin, Noah**: Financial document analyzer
* **Suh, EunGyul**: Accounting fraud detector

#### Data Cleaning & Structure

* **Guan, Yifei**: Police report information extractor
* **Yang, Junhyeok**: Web-scraped data cleaner for LLMs
* **Tolmochow, Gregory**: Natural language query interface for structured data

### I. Health & Fitness

#### Fitness Planning

* **Chen, Xinmo**: Personalized fitness recommendation system
* **Arularasu, Akhil**: AI-powered meal planning assistant
* **Jarman, Robert**: Gym companion app

### J. AI & Machine Learning Research

#### AI Development

* **Gao Henry**: AI text detection and human-like text generation
* **Jung, Seungwon**: Zero-shot vs few-shot learning comparison
* **Hakam, Brian**: AI debate simulator using persona-based LLMs

## Detailed Individual Ideas

### Ahn, Eric

The team project idea I had in mind was an academic paper simplifier that would aim to bridge the gap between complex academic research and general audiences. Lots of scholarly papers today are filled with technical jargon, which makes them difficult to understand for non-experts. In this way, by using NLTK for text preprocessing followed by NLP (using pre-trained models like GPT or BERT) for summarization to analyze research articles, we could preserve key information and provide plain-language summarizes, highlight essential points, and offer explanations for complex terms. Users, such as students or the general public, can input an academic paper and receive an easy-to-read summary via input from the following potential options: (1) web scraping from URLs (like PubMed), (2) uploading .txt/.docx/.pdf file, (3) and/or direct text input in the UI.

### Ambrose, Daniel

Cover letters are definitely the most annoying and time consuming part about applying to jobs. There are methods to make a cover letter quicker like using ChatGPT, but the result is usually too general and recruiters could easily tell it's AI-generated. I want to create a project where you can input a job’s description and your general cover letter and it outputs a tailored cover letter that incorporates keywords from the job description. To create this project, I will need to use a mix of AI-generation and keyword matching through text processing. This project will mostly focus on computer science jobs to limit the variety of keywords. Keywords extracted from job descriptions will prioritize certain groups of keywords such as programming languages and the requirements section in the job description. Additionally, there could be functionality to rate how well the job's keywords match your cover letter's keywords.

### Amoakohene, Humphrey

Building an NLP system to analyze and rank resumes based on job descriptions to make it easy to apply to spam apply for jobs without having to manually create new resumes

### Arshavsky, Mark

In Data Science and CS, it’s quite normal for students to apply to tons of internships. From personal experience, it gets really hard to keep track of all the applications. Sometimes you might even miss an important status update that gets buried in your email. My project idea is to create a product that simplifies the internship application process for students by handling the “tracking” and “monitoring” step for them. My vision is for it to work by students connecting the product to their emails (as when you apply to an internship you usually get an email), but I am open to other interpretations! Then, the product will use NLP to parse the relevant emails, extracting data such as company name, date of application, position name, etc. and put it in an Excel sheet. The product will also track for updates to students’ applications and color-code accordingly. Perhaps red would be “Rejected”, yellow would be “Status Update”, and green would be “Offered”. I have been thinking of this idea for some time now, and I think it can make a real-world impact!

### Arularasu, Akhil

I want to implement an AI-powered meal planning assistant that dynamically generates personalized meal plans based on user inputted dietary preferences, allergies, fitness goals, and daily caloric needs. By processing natural language inputs (eg: "I need a high-protein vegetarian meal plan with 2500 calories per day"), the system will create meals from one or many extensive recipe datasets, ensuring nutritional balance while considering restrictions like keto, vegan, vegetarian, gluten-free, etc.

Key Features include leveraging NLP for text generation, calory and nutrient optimization, dynamic recipe recommendations, grocery list generator, and more. Users can describe their dietary needs in natural language (eg: "low-carb, high-protein meals under 2000 calories"), and the system will parse these requests into structured data to generate meal plans. I feel that there is a lot of places the group can take this idea and run with it while utilizing NLP.

### Carrier, Emma

An application that identifies poor coding syntax practices and gives suggestions to fix it. For example, if there isn't any commenting found throughout the code, it will suggest to add more comments in specific places (before functions, etc.). The user would input a file / code chunk to be analyzed and it can either return the code chunk accepting the suggestions or just give a list of suggestions for the user to change themselves. There could be an option for multiple programming languages because they all have different syntax and standards that programmers should follow. Could market it as a way to help new programmers or programmers learning a new language as a way to help them identify areas in which their code could improve. Would likely need to implement a parser to achieve this goal.

### Chang, Ridge

I want to build a system that translates idiomatic expressions across languages in a way that actually makes sense, rather than just converting words literally. Expressions like “break the ice” don’t mean much if translated directly, but most language has its own way of saying the same thing or similar things. I want to create a tool that captures these nuances, ensuring that meaning—not just words—is preserved to the best of its ability. I’m interested in how idioms reflect cultural perspectives, and I want to explore how this project can improve communication between languages while keeping translations natural, authentic, and pragmatic.

### Chen, Angelina

I think it would be interesting to look into Amazon product reviews and use NLP to detect whether a bot is responding or an actual human; this is due to the increased number of bot action on Amazon. Often bots will give fake positive reviews to help boost a particular item or to show that a user is active if they are a paid reviewer. Another idea is to analyze the most popular companies and the kinds of words that are used in advertisements/website/customer interaction to understand how they have good customer retention. There could be a analysis of popular and dying companies.

### Chen, Xinmo

I want to analyze user input and provide personalized fitness recommendations. It will allow users to log their workouts in natural language, such as "I lifted 50 lbs for 3 sets of 8 reps today," and extract key data points using NLP. By analyzing past workout logs, the system will identify trends, detect plateaus, and suggest progressive overload strategies, such as increasing weight, reps, or intensity. Additionally, I also want to do/incorporate sentiment analysis to give user motivation and provide encouraging feedback. This model will probabaly rely on outside fitness-related datasets and integrating them in order to offer actionable insights for optimizing workout routines.

### Correa-Perez, Nicholas

My idea for the team project would be an analysis between lyrics and music genre. It would take a list of songs from a list of different genres and see if common themes or even words come up in the search. Perhaps maybe even an ambitious goal could be to see if we can tie the type of music to its words (i.e. bubbly music has positive words). Genre would be described as the musical aspects of songs to have a consistent definition, and the lyrics would be analysis for overall theme and tone of the lyrics as a whole.

### Coulanges, Charlington

I would like to build a sentiment analysis chatbot to distinguish reviews on given platforms (Yelp, Amazon, Rotten Tomatoes, etc.). By giving the data either a positive, neutral, or negative label, the majority of the labels will either recommend or not recommend the product using excerpts from the reviews analyzed. There are often times when a review site will have a decent amount of bot reviews to either tank or boost the rating. Thus, the chatbot will also be able to detect whether any review appears to be written by bots or a any non-human source.

### Dahiya, Rishita

I've often been fascinated by the intricacies of the English language which may not be intuitive if English is not someone's first language. An example of such is how certain words change in definition by their context, for example the word "set", which means something different in each of these phrases: set the table, the sun set, to set the record, and so on. My goal in this project would be to develop a tool which is able to decipher the definition of the ambiguous words depending on the context it is used and as a result make machine language processing more precise and intuitive. This would make machines understand the human language better and would have practical applications in machine translations and search engines.

### Dattatreya, Maya

My project idea would be to create a model that can perform sentiment analysis to detect the tone and bias in media and the news. I want to see how levels of emotional language used in different kinds of articles affect the engagement metrics of popular media and news sources. My goal is to understand how sentiment influences public perception and how media literacy can be improved.

### Forbes, Alexander

I get spam emails daily, and I think it'd be an interesting final project to create a straightforward spam detection tool that flags suspicious emails or messages by using NLP techniques to identify spammy keywords, suspicious links, or recurring patterns. A feedback loop will let users confirm or override the model’s decisions, which could potentially improve accuracy over time. This project would combine classification algorithms with a user-friendly interface for simple adoption. Ultimately, I want to produce a packaged, practical tool that addresses an actual, real-world communication problem.

### Gelb, Jake

Hi! I am open to all sorts of various projects and am not attached to any specific idea. Some areas of interest include spam bot detection, phishing and scam prevention, recipes tailored to dietary needs, sentiment analysis, and chat bot development. One specific idea is aa chatbot geared toward fantasy football users that analyzes trades and decision-making, helping users optimize their teams based on player performance, matchups, and trends. I am very excited for this course and am eager to collaborate on some impactful project.

### Guan, Yifei

I'm currently working with a professor to aggregate data from the police department. Some department has organized data that we can use directly, but most of them only have individual reports that we have to fetch information manually. I want to use linguistic model and text processing technique to extract information efficiently from individual police report, including incident, date, victims, information officer, information, and so on. This would largely shorten the time we need on processing the reports.

### Hakam, Brian

AI Debate Simulator-Using persona based LLMs(Similar to Character AI) This project would fine tune LLMs to answer like specific people, using scraped transcripts and a tone analysis of the person(funny, serious). Then attach the person’s history and debate relevant events to the context window. For example, to do Abraham Lincoln, an LLM would first be fine tuned on speech of that time, then specifically tuning on his transcripts and text. Then another LLM would be trained in this fashion on another person. The 2 or more LLMs would then debate a chosen topic with an intermediately and neutral LLM asking questions, then ultimately deciding the winner. This process would be fully automated, where you type in a name and it would web scrape and train all on its own.

### Henry, Gao

I have two ideas:

1. Create an AI model that will identify text written by AI. It would be difficult because AIs are becoming more and more human-like. Some ideas would be to look for some “errors” that AIs won't make, or check the cosine similarities between sentences. The “errors” should be something that is grammatically correct but not often used. By checking cosine similarities, we can see if the sentences use similar words, or have similar structures.
2. Use human-written text to train an AGI agent that writes like a real human. Instead of always choosing the token with the highest probability, choose a random token based on the probability assigned. In this way AI will have a larger vocabulary set. Another possible approach is to analyze the sentence structures and let each sentence structure appear in a probability similar to that in reality.

* Henry Gao

### Hou, Carol

I'm interested in a project focusing on sentiment analysis or an email spam detector. I am interested in researching machine learning models that can be used for the classification tasks (classifying a social media post as positive, negative, or neutral, or for emails as spam or not spam.) I haven't narrowed down the main social media website I want to use as a data source for sentiment analysis, but I'm currently thinking of X (twitter), Yelp, etc. The goal of the project would be to determine what customers are thinking about certain products, restaurants, etc. Or, to detect if an email is spam or not.

### Hu, Yutong

I would like to build a natural language-based course recommendation system that helps students find relevant courses based on their preferences and academic history. The system will process natural language inputs from users to understand their course requirements and generate personalized recommendations. The system will accept free-form text descriptions of desired courses, parsing key information such as: subject area/discipline, course topics and content, instructor preferences, credit hour requirements, and etc. Besides, we would like to add more advanced filtering based on students' personal information: their majors and the course they've already taken. We might need to use named entity recognition and some filtering engine.

### Jarman, Robert

I have a few ideas.

Online Multiplayer Game: Create a simple multiplayer game (e.g., trivia like charades, word games like Wordle, or strategy-based optimization such as collecting coins on a map within a limited number of steps or time). The game would feature real-time interaction and leaderboards to engage players.

Pocket Teaching Assistant (Pocket-TA): Develop an app that uses natural language processing to summarize lecture notes, create flashcards, organize notes collaboratively in real-time (with features like version history, tags, and search), and answer questions from uploaded documents. This tool aims to make studying for exams more efficient.

Gym Companion App: Build an app to personalize fitness journeys with tailored exercise, diet, and sleep plans based on a user’s current build and desired physique. The app also fosters community by helping users find nearby sports partners for games like basketball or tennis, promoting health and social connection.

### Jennings, Caleb

Create a model using machine learning combined with computational linguistics that learns the writing style of a list of classic authors from a database of many classic literature books, and the model tries to predict an author based on a sample text that was left out of the database for testing. Finding the database should be easy since much of classic literature is public domain (though it would take some time to collect it all). A number of machine learning techniques could be applied such as Stochastic Gradient Descent, Random Forests, Neural Networks, and Clustering. The challenge would be to determine how to parse the data, what learning technique to use, and how to use the data in learning the model.

### Jiang, Jenny

An idea I had using NLP is a tool that processes hundreds of news articles that are released daily regarding markets, finance, and the economy (from Wall Street Journal, New York Times, CNBC, MarketWatch, etc.) that then provides a summary of what happened. As someone that likes to keep up with the news and markets myself, it can be exhausting reading multiple articles a day from different platforms to get an accurate grasp of current events. An NLP tool could process all these news articles using big data to then generate daily summaries of the news. This can help make keeping up with the economy more accessible for those that don’t follow the news.

### Jitngamplang, Varakorn

I like the idea of a tool that helps find music that precisely matches a desired mood or theme. I want to develop a tool that uses natural language processing techniques to analyze song lyrics and facilitate music discovery based on a specified lyrical characteristics. Ideally, it would searches for songs based on themes (e.g., romance, travel), sentiment (e.g., melancholic, upbeat), and other lyrical features. By extracting keywords, analyzing sentiment, and employing other NLP processes, I hope it will recommend songs that resonate with given preferences. This goes beyond a simple sentiment analysis tools or aggregator as this would require analyzing music rhetoric.

### Jung, Seungwon

I am open to any topic to research. I am open to topics like sentiment analysis, news fraud detection, text-to-speech tools that add emotional expressiveness, and even poetry-generating writing editor. Also, research related to bias detection and ethical language generation can be done. My idea at the moment is to research the effectiveness of zero-shot vs. few-shot learning on dynamic gaming(or just a normal life if sufficient datasets are not found) NPCs. Although it is well-known few-shot learning will be more effective than zero-shot, I would like to research its limitations using BLEU, ROUGE, or BERTScore to evaluate the quality of a generated text using few-shot learning.

### Kansal, Rhea

I am open to any project ideas, but one that I think could be interesting is using NLP to detect fake news. In this project, we would develop a system that can classify news articles or social media posts as either fake or real. The system could analyze linguistic patterns, stylistic features, and content to identify misinformation and provide users with a confidence score for the classification. The prevalence of misinformation in today’s society makes this a highly relevant topic.

Another idea I have is a system that identifies and extracts key skills, qualifications, and experiences from resumes. This tool can be used to match resumes with specific job descriptions, streamlining the recruitment process. It could also rank resumes based on how closely they align with the job requirements, helping recruiters quickly find the best candidates.

### Kim, Gyul

I would like to analyze patient reviews on healthcare systems and doctors to identify key topics such as wait time, doctor empathy, quality of care, misdiagnosis, and facility conditions. Through topic modeling, the project can identify recurring themes to provide a summarized review on a facility, service, doctor/ any other patient feedback. The project will involve collecting and preprocessing patient reviews from platforms such as Healthgrades, Zocdoc, or Reddit, followed by implementing unsupervised learning models to extract meaningful topics. Sentiment analysis can also be integrated to assess whether patient sentiments about specific topics are positive, negative, or neutral.

### Kim, Olivia

Embedding hand gestures with NLP. As LLMs expand out to voice recognition, there has been significant more researches about tone, but to my short knowledge hand gesture research hasn't been done as extensively. By recording the hand movements made when speaking a certain text and analyzing it, nuances will be able to be captured more effectively. This could also be implemented to turn a written text into ai-generated videos of sign language. However, I strongly believe this is too good of an idea to not have been made already.

### King, Marisa

I would enjoy developing a project that examines the different words and terms used by the media to describe events (both global and internal), and how their specific word choices differ based on factors such as race, gender, sexuality, politics, religion, etc.

### Lin, Ryan

My team project concept is a some kind of text-message/DM chatbot that can mimic slang or like styles of texting. People speak differently over text whether in content, style, or length of messages. I think its pretty interesting how language over text can be so different than using proper grammar, and in a sense it is its own kind of dialect of language. I'm open to doing other stuff cuz I'm also interested in using different types of data including video, audio, and picture data but I'm not really certain how yet.

### Mi, Renzhi

I'm thinking about developing a program that classifies books and novels into their respective genres based on word frequency patterns and word types, which can potentially help to build the page suggestions for readers. This might involve processing volumes of text, extracting frequently occurring terms and utilizing them as key indicators to infer the overarching theme and genre. By leveraging NLP techniques, the program will identify genre-specific linguistic patterns and compare them against predefined datasets corresponding to various literary genres such as mystery, fantasy, science fiction, and romance. This automated classification framework enhances genre identification by analyzing textual content directly, so it can provide a more objective and data-driven approach to literary categorization.

### Okumura, Harutoshi

Political Science Research Paper on using LLMs to detect explicit contradictions from presidential debate speech candidates.

Can LLM rely solely on Natural Language Structure to find explicit contradictions on candidates' past speeches (public, tweets, websties, e.t.c), and use it against them to solidify an argument of contradiction, and thereby lack of credibility in certain topics?

Are there certain semantical features and law of contradiction, that we can adapt reliably for a consistent system that detects contradictions (no matter how fundamental it may be), and apply to large corpus of past speeches.

### Pham, Chloe

I'm potentially interested in the idea of "translating" texts written in a highly elevated/academic/obscure tone to language that may be more accessible to the average person. While there is an argument for "flowery" and "smart" writing, I think there is an elitist undertone to conveying ideas in a way that is inaccessible to many, especially if the text's purpose is education. There is a large set of existing source texts to draw from, along with some existing SparkNotes-type "translations" of classics and other foundational texts.

### Reicin, Noah

Develop a Natural Language Processing (NLP) system that analyzes financial documents to perform two main tasks:

1. Sentiment Analysis: Identify and categorize the document's tone—positive, neutral, or negative—based on relevant keywords' frequency and contextual usage.
2. Key Focus Extraction: Detect the frequency and distribution of specific domain-relevant terms to determine the company’s primary areas of emphasis (e.g., sustainability initiatives, R\&D, and shareholder returns).

### Sezgin, Alas

I would like to work on a dogwhistle detector, specifically for Twitter (or, reluctantly, now named "X") as with the new administration of the website, far right rhetoric (like fascism) has become less and less censored and perhaps even more common, albeit hidden behind a veil of dogwhistles and plausible deniability which make it hard for the average person to determine if what they are consuming is a joke or far right rhetoric. This has the effect of familiarizing users to unkowingly become familiarized with harmful rhetoric through humor, the selective lack of censorship towards which can sway user opinions on a supposedly neutral website. This is why it's important to detect dogwhistles or general far right rhetoric, which may be difficult for the average person. It would be nice to implement this as a browser add-on but that might be outside the scope of this class. This would likely involve a lot of hard-coding or feeding labeled data into a model, so I am open to new ideas.

### Shah, Jiya

This idea was made in collaboration with Yutong Hu. Although I don’t have any concrete ideas on implementation currently, we were thinking of something that helps students choose courses based on information inputted in natural language. It would use their description of the course (i.e., which academic discipline, professors they’d like, how many hours they want/need, which major/general education requirements they still need to fulfill, general subjects they would like to explore, etc.) in addition to information about what courses they have already taken and their major(s) and/or minor(s). This would all be to provide suggestions of what courses they could take based on the course atlas of that semester.

### Shah, Riyan

My idea is to process pieces of code and using an NLP algorithm, generate meaningful comments for it so other people looking at the code can better understand it.

* create a list of variables used with their purpose
* comment long lines of code to explain what they are trying to do (eg. long mathematical expressions, or lines involving lots of variables and packages)
* create comments for blocks of code that are trying to perform a task (eg. this for loop is meant to do blah blah blah)

### Sixing, Wu

My idea is to make a Brilliant Reply model. I hope the model can work to assist people in replying in various scenarios. 1. email writing assistant: helps to formulate emails for different occasions, including networking, job applications, announcements, etc.); 2. text message reply: helps to generate an appropriate and engaging response for personal and business usage, being able to handle slangs and emojis.); 3. scenarios based replies: eg: helps to generate a hook-up message or flirting replies in ins, a coffee chat invitation in LinkedIn, appropriate complaints message to customers services, etc; 4. tries to tailor the users' tone and learn from the previous text.

### Suh, EunGyul

Project Concept 1: Accounting Fraud Detector. I assume that the SEC filings of companies involved in accounting fraud may contain exaggerated or magnified language and tone. I would like to develop a classification or anomaly detection model that identifies accounting fraud by analyzing companies' SEC filings. However, I anticipate that datasets containing SEC filings from fraudulent companies would not be available enough to train the model effectively.

Project Concept 2: Fake News Detector. Fake news on social media has become a significant concern in recent times. Similar to the first concept, I aim to develop a detection model that identifies potential fake news by analyzing social media posts, such as those on platforms like X. I would collect dataset from X with API or use existing dataset on fake news on social media. Additionally, I am interested in exploring which components of a social media post—such as whether the account is verified, whether the post contains images, the post's length, etc.—serve as indicators of potential fake news via extracting meta features from posts

### Tolmochow, Gregory

Natural Language Query Interface for Structured Data This project aims to develop an NLP-powered interface that allows users to query structured databases (CSV or SQL) using natural language. Instead of writing complex SQL queries or manually filtering data, users can ask questions conversationally, and the system will break down their queries into structured filters. For example, given a housing dataset, a user might ask, "How many homes built in 2023 have 2 or more residents within 5 miles of a school?" The model would extract relevant columns such as year\_built = 2023, # of ppl > 2, and dist\_to\_school < 5. These filters would be put into blocks that users can then refine these filters before and after applying them, or even pick which ones to remove. This project combines natural language understanding with data retrieval, making database interaction more intuitive and user-friendly.

### Ukpong, Imeikan

One idea that hopefully will call on knowledge learned in this course is a tool that is able to take in prompts like conversations or simple sentences and returns whether that input is either positive or negative, (depending on the difficulty maybe neutral or more nuanced statements can be considered and categorized as well). To figure out what to produce as an output, the tool could observe certain keywords based on a certain heuristic (like words or symbols that tend to generally be important when people use them, like “I just got a new job!” has “new job” - positive and exclamation point further helps model be sure that the statement is positive).The sign of the output (Either positive or negative) is solely based on whether the input elicits positive emotions like happiness, laughter, etc. or negative emotions like sadness, pain, etc.

### Wen, Yuanhuizi

This project aims to develop an AI-powered resume-to-job matching system using a dataset containing candidate resumes, the job positions they are applying for, and a numerically labeled match score. We will train a neural network-based regression model to predict the match score between a given resume and job position (already found the dataset from Kaggle). The model's performance will be evaluated using appropriate metrics such as Mean Squared Error (MSE) or R² score (We will do more research on this). This system has two key applications: (1) Automating resume screening to help recruiters efficiently rank candidates, reducing manual effort, and (2) Assisting job seekers in evaluating how well their resume aligns with different job positions before applying. By streamlining the hiring process, this project saves time for both candidates and recruiters, increasing overall efficiency in job matching.

### Wu, Junting

Different poets have different styles. People who read enough poems can know the author of a poem through its style. But what is the style? Is it the use of words (some poets would use certain words repeatedly, some poets have characteristic ways of arranging the sequence of words, etc.)? Is it the meaning? Is it the way of starting or ending a poem? Or is it just a feeling? I wonder whether AI can classify poems according to their authors just based on their style. The result may shed light on the understanding of a poet's style. Only English poets would be chosen to avoid issues with translation.

### Xiaotong, Liu

My project aims to develop a program for analyzing text in books and novels to determine their genre based on word frequency patterns. The program will skim through a large amount of text, identify the most frequently occurring words, and use them as key indicators to make inferences about the overall theme or genre. Using Natural Language Processing (NLP) techniques, the program will identify genre-specific words and compare them to predefined datasets of literary genres such as suspense, fantasy, science fiction, or romance. This automated classification system helps readers to effectively categorize novels based on textual content rather than metadata.

### Xing, Jerry

My team project concept is a program that evaluates media and determines the level of bias. It would specifically evaluate news articles and transcripts of news videos. While all media has the same goal of informing the viewer or reader, often there is a certain level of bias from the person who wrote the article or script. I believe that natural language processing could be very applicable for analyzing media and gauging the amount of bias. In terms of deliverables, the end product would aggregate various sources of media on a topic, and compare the degrees of bias between the content that is written on a singular subject.

### Xinyuan, Hu

I'm planning to build a tool that uses natural language processing to analyze and evaluate research paper credibility on platforms like arXiv and Google Scholar. Given the massive volume of papers being published today, having an automated way to assess paper quality would be incredibly helpful. The project will use well-established papers from top journals as training data to identify what makes research credible. The analysis will focus on some key aspects such as: methodology robustness (how well research methods are described and justified), citation patterns (how the work connects with existing research), and overall writing quality, etc. The process might be retrieving papers from websites, extracting the paper contents, and hen developing a scoring method.

### Xu, Jack

I'm interested in making a sentiment analysis tool for studies/papers that can classify the overall quality, or to see if there are patterns that can be found in papers that are considered low-quality in meta-research. Given the text of a paper, it should predict the quality of the evidence and overall methodology. Also, maybe it could highlight some common patterns that are indicative of high quality, etc.

### Yang, Junhyeok

Idea: Making web-scraped data readable for LLM

Description: Web-scraped data from various websites often contain unstructured and irrelevant content, making it difficult for LLMs to process effectively. Issues include raw HTML tags, boilerplate text, headers, footers, advertisements, and redundant information. NLP techniques can be leveraged to clean, preprocess, and structure this data into a format optimized for LLMs. Methods such as text normalization, entity recognition, summarization, and noise filtering help remove unwanted elements while preserving meaningful content. By applying NLP-driven parsing and formatting, web-scraped data can be transformed into a structured, high-quality dataset for better comprehension and usability for LLMs.

### Yeruva, Sujith

I would like to do something involving sentiment analysis on stocks. There are sites like SeekingAlpha, ValueInvestorsClub, Yahoo Finance, and many others that analyze a stock and sometimes pitch it. There is also discussion on social media sites like Twitter and Reddit from individual retail investors. I would like to use this to potentially generate a "sentiment score" that shows what the public perception is on certain stocks (and how it might vary between different sources).

### Yirdaw, Elshaday

I mainly have two project ideas that I would like to work on throughout the semester. My first (and main) project idea involves creating a tool that can estimate the readability level of a text provided by a user. In addition, I would like for this tool to offer some kind of suggestions that can make the text more accessible. These suggestions could range from simple modification, like replacing difficult words with more commonly used words, to advanced modifications, such as restructuring sentences or paragraphs that may otherwise be unclear and hard to understand. Essentially, the goal of the project would be to estimate the current readability level of the given text and provide modification suggestions to improve the readability of the text (perhaps to some level of complexity that a user might want). The secondary idea I am considering is developing some kind of a vocabulary builder. This tool would take a text provided by a user and identify words (and phrases) that may be challenging to understand. Then, using these words (and phrases), it would generate a vocabulary list along with definitions so that users can use it to expand their understanding.

### Yoon, James

With the Information Age’s abundance of information, such an overwhelming sea of viewpoints and novel ideas may embolden more polarizing instances of media. Consequently, there remains an ever-urgent necessity to identify bias within journalism which may be obviated through utilizing NLP and subsequent sentiment analysis techniques. By leveraging sentiment analysis, named entity recognition, and topic modeling, one could assess the emotional tone, political leaning, and framing of articles from multiple sources. Users could input URLs or text to receive a breakdown of sentiment polarity, lexical bias, and comparative analysis against a diverse dataset of news sources. The tool could further employ machine learning models trained on labeled datasets to enhance accuracy, offering readers an objective lens through which to evaluate media narratives.

### Yuxuan, Shi

Text Simplification for Patient Education

The complexity of medical language has been a major barrier in consumer health informatics. For individuals untrained in medical field, the healthcare processes become a black box. Here are some potential directions that I aim to optimize through this project: lexical and contextual complexity; health literacy; language and cultural barriers; patient-centric communication tools.

Solution: a multi-agent environment that can do:

1. lexical simplification: replace complex medical jargon with simpler terms; syntactic simplification to shorten long, complex sentences.
2. context specific explanations. ("benign" as "not cancerous" in a pathology report)
3. dynamic summarization: highlight and prioritize most critical information, such as diagnoses, treatment plans, next steps.
4. user feedback loop: allow interaction with agent for further clarification or simplification
5. personalization: adjust output based on user’s patient literacy levels, language preference, and prior knowledge.

### Zahid, Zeshan

The project Im thinking about creating is a webapp or program that can make edits to your resume weather it be format or edits to your words in the way you describe certain stuff in your resumes. Im familiar with backend webapp creation with Python and think using some of the libraries along with possibly Ai like chatgpt 4 to be able to make those edits. This tool could be useful for students as well as job seekers by helping tailor their resumes. Using Ai would make it alot more robust to where once inputed we could use Ai to tailor the resume for certain jobs or purposes and make effective edits.

### Zhang, Jingzhi

Interactive Life Story Generator: Turn user-provided life details into a realistic, interactive, fictional story, where real-time user choices can adjust the plot (i.e., exploring future "what-if" scenarios). The project will allow users to specify the genre and ending type and use pre-trained models to dynamically generate realistic narratives based on the user's past experiences. The focus will likely be on prompt engineering to ensure coherence and immersion with a web-based UI for user interaction.
