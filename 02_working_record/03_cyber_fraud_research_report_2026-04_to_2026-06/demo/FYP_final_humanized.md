🔍-
100%
🔍+
⚊
◨
🔄
🔍
✕
⚙️
📋 Document Outline
DECLARATION
DEDICATION
ACKNOWLEDGEMENT
ABSTRACT
ABSTRAK
TABLE OF CONTENTS
LIST OF TABLES
LIST OF FIGURES
LIST OF ABBREVIATIONS
INTRODUCTION
Introduction
Problem Background
Research Aim
Research Question
Research Objectives
Research Scope
Importance of This Research
Report Organization
LITERATURE REVIEW
Introduction
Intelligent Chatbot for Booking System
Table 2.1 Previous Paper study
Intent Classification for Chatbot
Figure 2.1 Intent Classification of Chatbot
Categories
Table 2.2 Categories of Intent Classification
Table 2.3 FAQs Classification
Machine Learning Algorithms in Chatbot
Figure 2.2 Machine Learning
Table 2.4 Existing Algorithms
Machine Learning for Intent Classification
Naïve Bayes
Support Vector Machine
Summary
RESEARCH METHODOLOGY
Introduction
Research Framework
Figure 3.1 Research Framework
Phase-1 - Literature Review and Problem Formulation
Phase 2 - Data Pre-processing
Phase 3 - Algorithm Model Implementation
Evaluation Metrics
Phase 4 - Result Analysis and Discussion
Chapter Summary
RESEARCH DESIGN AND IMPLEMENTATION
Introduction
Research Implementation
Figure 4.1: Research Implementation
Data Preparation
Figure 4.2: Raw Dataset
4.3.1 Steps of Data Preprocessing
6. Displaying Preprocessed Queries
Figure 4.3 : Pre-processed Dataset
Figure 4.4: Code of Data Pre-Processing
Figure 4.5: Data Pre-Processing Output
Parameters
4.4.1 Testing Method
Table 4.1 Example of Testing Method
Model Implementation
4.5.1 Model Architecture
4.5.1.1 Naive Bayes
Figure 4.6 Code for Naive Bayes Performance Metrics
4.5.1.2 Support Vector Machine
Figure 4.7 Code for SVM Performance Metrics
4.6 Model Efficiency
4.6.1 Naive Bayes
Figure 4.8 Naïve Bayes Classification Report
Figure 4.9 Naive Bayes Performance Metrics Output
4.6.2 Support Vector Machine
Figure 4.10 SVM Classification Report
Figure 4.11 SVM Performance Metrics Output
4.7 Chapter Summary
CHAPTER 5
RESULTS, ANALYSIS AND DISCUSSION
5.1 Introduction
5.2 Research Results and Analysis
5.2.1 Comparison of Algorithms
Figure 5.1 Comparative Classification Report
Figure 5.2 Naïve Bayes Vs SVM performance comparison
Figure 5.3 Naïve Bayes Vs SVM performance metrics
Figure 5.4 Naïve Bayes Confusion Matrix
5.2.1.1 Accuracy
5.2.1.2 Precision
5.2.1.3 Recall
5.2.1.4 F1 Score
Figure 5.5 SVM Confusion Matrix
5.2.1.1 Accuracy
5.2.1.2 Precision
5.2.1.3 Recall
5.2.1.4 F1 Score
Table 5.1: Metric Results
5.2.2 Algorithms Efficiency
5.3 Future Works
CHAPTER 6
CONCLUSION
6.1 Summary
6.2 Achievement of Project Objectives
6.3 Future Work
REFERENCES
A COMPARATIVE STUDY ON CHATBOT INTENT CLASSIFICATION

USING MACHINE LEARNING FOR HOMESTAY BOOKING

QUERIES

TANSHIBA NAORIN PRAPTI

UNIVERSITI TEKNOLOGI MALAYSIA

PSZ 19:16 (Pind. 1/13)

UNIVERSITI TEKNOLOGI MALAYSIA

DECLARATION OF THESIS / UNDERGRADUATE PROJECT REPORT AND COPYRIGHT

Author’s full name : TANSHIBA NAORIN PRAPTI

Date of Birth : 1 FEBRUARY 2000

Title : A COMPARATIVE STUDYON CHATBOT INTENT

CLASSIFICATION USING MACHINE LEARNING FOR

HOMESTAY BOOKING QUERIES

Academic Session : 2023-2024/1

I declare that this thesis is classified as:

CONFIDENTIAL

(Contains confidential information under the Official Secret Act 1972)*

RESTRICTED

(Contains restricted information as specified by the organization where research was done)*

✓

OPEN ACCESS

I agree that my thesis to be published as online open access (full text)

I acknowledged that Universiti Teknologi Malaysia reserves the right as follows:
The thesis is the property of Universiti Teknologi Malaysia
The Library of Universiti Teknologi Malaysia has the right to make copies for the purpose of research only.
The Library has the right to make copies of the thesis for academic exchange.
Certified by:





SIGNATURE OF STUDENT

SIGNATURE OF SUPERVISOR

A20EC4051

Ts. DR ROHAYANTI BINTI HASSAN

MATRIX NUMBER

NAME OF SUPERVISOR

Date: 14 JANUARY 2024

Date: 14 JANUARY 2024

NOTES : If the thesis is CONFIDENTIAL or RESTRICTED, please attach with the letter from the organization with period and reasons for confidentiality or restriction

“I hereby declare that we have read this thesis and in my

opinion this thesis is sufficient in term of scope and quality for the

award of the degree of Bachelor of Computer Science (Software Engineering)”



Signature

:

________________________________

Name of Supervisor

:

DR. ROHAYANTI BINTI HASSAN

Date

:

14 January 2024

A COMPARATIVE STUDY ON CHATBOT INTENT CLASSIFICATION

USING MACHINE LEARNING FOR HOMESTAY BOOKING

QUERIES

TANSHIBA NAORIN PRAPTI

A thesis submitted in fulfilment of the

requirements for the award of the degree of

Bachelor of Computer Science (Software Engineering)

Faculty of Computing

Universiti Teknologi Malaysia

JANUARY 2024

DECLARATION
I declare that this thesis entitled “A Comparative Study on Chatbot Intent Classification Using Machine Learning for Homestay Booking Queries” is the result of my own research except as cited in the references. The thesis has not been accepted for any degree and is not concurrently submitted in candidature of any other degree. 

Signature

:

....................................................

Name

:

TANSHIBA NAORIN PRAPTI

Date

:

14 JANUARY 2024

DEDICATION
I dedicate this paper to myself, as a testament to my unwavering dedication, hard work, and determination in pursuing knowledge. I have overcome obstacles and seized chances, through innumerable hours of research, analysis, and learning. The journey of self-improvement and self-discovery that has led me to this point is symbolised by this paper, which reflects my devotion to academic and personal growth. May this act as a prompt to keep aiming for greatness in all that I do, serving as a reminder of the potential that exists inside.

ACKNOWLEDGEMENT
I would like to express my sincere gratitude to everyone who has assisted me in completing my thesis. Throughout this journey, I have had the privilege of collaborating with a diverse group of individuals, including esteemed researchers, seasoned practitioners, and prominent academics. My understanding and perspectives have been greatly expanded by their priceless ideas and contributions.

In particular, I would like to express my deepest appreciation to my primary thesis supervisor, Dr. Rohayanti Binti Hassan. Her unwavering support, invaluable guidance, constructive critiques, and the genuine friendship she extended to me have been instrumental in shaping this thesis. Without her continuous encouragement and keen interest in my work, this thesis would not have reached its present form. Dr. Rohayanti's mentorship has been an invaluable asset, and I am profoundly grateful for her dedication to my academic journey.

ABSTRACT
The effectiveness of machine learning algorithms, specifically Naive Bayes and Support Vector Machine (SVM), in classifying user intents for homestay booking chatbots in the context of Malaysia's booming tourism industry. Existing chatbots in this domain face significant challenges in accurately understanding and responding to user queries. In this work, web scraping techniques are used for data collecting and preprocessing. Then, machine learning models are implemented and evaluated. In order to guarantee robustness and generalizability, performance will be evaluated using accepted measures including accuracy, precision, recall, and F1-score in addition to cross-validation. The research aims to enhance the capabilities of homestay booking chatbots, ultimately improving user satisfaction and streamlining the booking process in Malaysia's tourism sector.

ABSTRAK
Keberkesanan algoritma pembelajaran mesin, khususnya Naive Bayes dan Support Vector Machine (SVM), dalam mengklasifikasikan niat pengguna untuk chatbot tempahan homestay dalam konteks industri pelancongan Malaysia yang pesat. Chatbot sedia ada dalam domain ini menghadapi cabaran penting dalam memahami dan memberikan respons yang tepat kepada pertanyaan pengguna. Kajian ini melibatkan pengumpulan data dan pra pemprosesan menggunakan teknik web scraping, diikuti oleh pelaksanaan dan penilaian model pembelajaran mesin. Prestasi akan dinilai menggunakan metrik yang sudah mapan seperti ketepatan, ketepatan presisi, ingatan, dan skor F1, bersama dengan pengecaman silang untuk memastikan kekuatan dan generalisasi. Penyelidikan ini bertujuan untuk meningkatkan keupayaan chatbot tempahan homestay, dengan harapan meningkatkan kepuasan pengguna dan menyelaraskan proses tempahan dalam sektor pelancongan Malaysia.

TABLE OF CONTENTS
TITLE

PAGE

DECLARATION iii

DEDICATION iv

ACKNOWLEDGEMENT v

ABSTRACT vi

ABSTRAK vii

TABLE OF CONTENTS viii

LIST OF TABLES xi

LIST OF FIGURES xii

LIST OF ABBREVIATIONS xiii

CHAPTER 1 INTRODUCTION 1

1.1 Introduction 1

1.2 Problem Background 3

1.3 Research Aim 4

1.4 Research Question 4

1.5 Research Objectives 5

1.6 Research Scope 6

1.7 Importance of This Research 6

1.8 Report Organization 7

CHAPTER 2 LITERATURE REVIEW 8

2.1 Introduction 8

2.2 Intelligent Chatbot for Booking System 8

2.3 Intent Classification for Chatbot 12

2.3.1 Categories 13

2.4 Machine Learning Algorithms in Chatbot 15

2.5 Machine Learning for Intent Classification 22

2.5.1 Naïve Bayes 22

2.5.2 Support Vector Machine 23

2.6 Summary 24

CHAPTER 3 RESEARCH METHODOLOGY 25

3.1 Introduction 25

3.2 Research Framework 25

3.2.1 Phase-1 - Literature Review and Problem Formulation 26

3.2.2 Phase 2 - Data Pre-processing 27

3.2.3 Phase 3 - Algorithm Model Implementation 28

3.2.4 Phase 4 - Result Analysis and Discussion 30

3.3 Chapter Summary 30

CHAPTER 4 RESEARCH DESIGN AND IMPLEMENTATION 32

4.1 Introduction 32

4.2 Research Implementation 32

4.3 Data Preparation 35

4.3.1 Steps of Data Preprocessing 37

4.4 Parameters 44

4.4.1 Testing Method 45

4.5 Model Implementation 46

4.5.1 Model Architecture 46

4.6 Model Efficiency 51

4.6.1 Naive Bayes 51

4.6.2 Support Vector Machine 52

4.7 Chapter Summary 54

CHAPTER 5 RESULTS, ANALYSIS AND DISCUSSION 55

5.1 Introduction 55

5.2 Research Results and Analysis 55

5.2.1 Comparison of Algorithms 56

5.2.2 Algorithms Efficiency 61

5.3 Future Works 61

CHAPTER 6 CONCLUSION 63

6.1 Summary 63

6.2 Achievement of Project Objectives 63

6.3 Future Work 64

REFERENCES ` 65

LIST OF TABLES
TABLE NO.

TITLE

PAGE

Table 2.1 Previous Paper study 10

Table 2.2 Categories of Intent Classification 13

Table 2.3 FAQs Classification 15

Table 2.4 Existing Algorithms 18

Table 4.1 Example of Testing Method 45

Table 5.1 Metric Results 61

LIST OF FIGURES
FIGURE NO.

TITLE

PAGE

Figure 2.1 Intent Classification of Chatbot 13

Figure 2.2 Machine Learning 16

Figure 3.1 Research Framework 26

Figure 4.1 Research Implementation 34

Figure 4.2 Raw Dataset 36

Figure 4.3 Pre-processed Dataset 39

Figure 4.4 Code of Data Pre-Processing 42

Figure 4.5 Data Pre-Processing Output 43

Figure 4.6 Code for Naive Bayes Performance Metrics 48

Figure 4.7 Code for SVM Performance Metrics 50

Figure 4.8 Naïve Bayes Classification Report 51

Figure 4.9 Naive Bayes Performance Metrics Output 52

Figure 4.10 SVM Classification Report 53

Figure 4.11 SVM Performance Metrics Output 53

Figure 5.1 Comparative Classification Report 57

Figure 5.2 Naïve Bayes Vs SVM performance comparison 57

Figure 5.3 Naïve Bayes Vs SVM performance metrics 58

Figure 5.4 Naïve Bayes Confusion Matrix 59

Figure 5.5 SVM Confusion Matrix 60

LIST OF ABBREVIATIONS
NLP

ML

-

Natural Language Processing

Machine Learning

SVM

-

Support Vector Machine

NB

-

Naïve Bayes




INTRODUCTION
Introduction
A homestay is basically a place where people can spend their holiday period in a destination which offers a homely comfort and relaxing environment. The renting of these kinds of homestay places are getting into the trend to provide the travellers with real experience of culture and lifestyle. The rising tourism industry of Malaysia are focusing and giving more emphasis on the online platforms for homestay bookings. Because of this advancement in the digital booking system, the tourism industry is progressing to maintain the digital ecosystem and getting more engagements of bigger customer crowd. This digital system needs a highly configured chatbot to keep up with the customer base, manage the user queries and provide a seamless service in the booking process. Although the system of online technology is launched, but the chatbot system is still behind the vail. Their ability to understand user’s intent in homestay booking has become highly questionable, and it’s also a matter of serious concern.

With the advancement of technology in the fourth industrial revolution, Malaysia has managed to transform from the manual lifestyle to a digital life. The booking system is designated to redefine the customer engagement through the involvement of chatbot and instrumental tools. This helps to manage the adequate user queries and provide them with relevant suggestions as per their searches [3]. Despite having these chatbots, the current situation of the chatbots lack with the functionalities of detecting accurate user intents and thus shows low efficacy in the performance to meet the requirements of the user. This study has its own value to provide with thorough investigation using machine learning algorithms and uncover the complexity of classifying the user intents for homestay booking queries. This study takes place to over lead Malaysia’s trendy rule-based chatbots in booking systems. The tourism industry is evolving into the digital platform with a rising number of populations on its own demand.

The popularity of the chatbots is emerging day-by-day, they have become the one of the most essential tools in the technological industry. Along with the involvement of the artificial intelligence in every sector, the significance of chatbots has raised its value after the invention of chatbot tools and applications like Bing AI, Blender Bot, Kuki, Meena, Rose AI, ChatGPT and so on. Besides all these influence in the digital sector to make human life easier and impactful, it has now become important and concerning fact to design and initiate an efficient and better performer Chatbot system in order to classify the user queries [5]. This research aims to bring a new advancement in the performance of chatbots by improvising the machine learning algorithms to classify intents. By doing a thorough study on the previous articles and literatures [1],[4], the evidence of ongoing obstacles is noticed in the homestay booking process. The challenges of the past research papers are not negligible, whereas the amazing research done by Ukpabi et al [2] takes the limelight of the rising problem, it demonstrates the efficiency and user contentment of the current chatbot system.

One of the major challenges includes the misunderstanding and classifying wrong user intentions, which leads to misinterpretations and unsuitable predictions or suggestions. Because of this, the user loses interest to use the application and finds difficulty in getting response to their required queries. Another reason of having this situation raised into a gross problem for the user is the current rule-based system used in the chatbots, which is ineffective to provide dynamic solutions and cannot help with providing accurate destination suggestion as per the user’s necessity. Not only this, the chatbot lacks with necessary flexibility and individualization in managing various user inputs. For this reason, the chatbot fails to provide personalized responses and suggestions, this situation hampers the existing inadequate Natural Language Processing (NLP) capabilities, failing to handle complex conversations, slang and non-standard language with the user. As a result, response time becomes slow and causes user’s dissatisfaction. The slow time response frustrates the user and user the loses interest to use the digital platform. The economic growth of the owner is also compromised. Thus, these persistent concerning issues shows the necessity for the improvement of the existing chatbot models.

This research is performed focusing on three major objectives. The first objective is to analyze and examine the previous research papers on utilizing machine learning algorithms to determine intent classification of chatbots in homestay booking queries. Then second objectives involve the implementation of Naïve Bayes and Support Vector Machine (SVM). And lastly, the third objective is to assess the efficacy of the two chosen algorithms when applied to the dataset from homestay booking queries. These goals focus on the comprehensive investigation and delve into solving the complexities of intent classification of the chatbots. Additionally, in the following sections of this research, a thorough analysis of the previous research is done in support of the statement and put strong points to detail the selected approach of this paper. This study defines the significant scopes and necessary findings to improvise the effectiveness and user experience in using homestay booking chatbots.

Problem Background
Despite the considerable advancements in the field of homestay booking, numerous ongoing issues can be observed in current research articles. Specifically, existing chatbots are plagued by a variety of challenges and constraints [1] [4]. Ukpabi et al [2] hinder their effectiveness and user satisfaction. Some of the common problems include:

Chatbots struggle to accurately understand and classify user intents, leading to misinterpretations of user queries and inappropriate responses.
Existing chatbots mostly are rule-based, they lack efficacy in more complex and dynamic scenarios where user inputs vary widely and where contextual understanding, personalization and adaptation are crucial.
The chatbots provide generic responses and recommendations and fail to personalize their interactions based on user preferences or past behavior.
Ineffective Natural Language Processing (NLP) in the existing chatbots results in difficulty in handling complex conversations, slang or non-standard language.
Slow response time in the current booking chatbot frustrates users.
Chatbots struggles to scale effectively to handle a growing user base when the user demand increases.
The current chatbot lacks a mechanism for continual learning and adaptation to changing user behaviour patterns or emerging trends in the tourism industry.
Research Aim
Against this backdrop, the primary aim of this research is to conduct a comprehensive comparative study that goes beyond the surface-level examination of chatbot functionalities. Instead, the focus will be on evaluating various machine learning algorithms specifically tailored for intent classification within the unique context of homestay booking queries in Malaysia.

Research Question
Some of the major research questions of this thesis are:

How can natural language understanding be improved to handle a wide range of user queries, including complex and nuanced requests related to homestay accommodations?
What are the key metrics and methods for evaluating the effectiveness of the chatbot system in terms of personalization, user satisfaction, and overall performance compared to existing booking systems?
What personalized recommendation algorithms can be employed to suggest homestay accommodations that align with individual user preferences and requirements?
To what extent do chatbots effectively provide accurate and relevant information about homestay options and availability, and how does their performance compare to traditional booking platforms?
How can user feedback be collected and utilized to iteratively improve the chatbot's performance and enhance the user experience in homestay booking?
Research Objectives
This research assesses the latest studies that have not been previously covered in earlier publications.

The study will specifically focus on the utilization of machine learning techniques to tackle the challenges related to homestay booking chatbot. Therefore, our objectives are as follows:

To explore the existing works on machine learning algorithms in classifying the chatbot intent
To propose the implementation of machine learning algorithm, specifically Naive Bayes and Support Vector Machine (SVM), for intent classification in Malaysia’s homestay booking chatbot queries.
To evaluate the performance of machine learning algorithm in (b) for intent classification in Malaysia’s homestay booking chatbot queries.
Research Scope
The study aims to address the challenges in homestay booking by improving intent classification using machine learning and enhancing the overall user experience in the booking process.

This work intends to perform preprocessing by using potential query datasets on homestay booking. This data will be processed to identify the inquiries and their intents. It will emphasize functionality-wise investigation to streamline booking processes.
To address the limitations of rule-based chatbots and enhance intent classification, we will leverage machine learning algorithms, specifically using Naive Bayesian and Support Vector Machine.
A set of well-established evaluation metrics, e.g. accuracy, precision, F1-score and recall will be employed to examine the performance of ML models.
Cross-validation technique includes splitting dataset into multiple subsets and model evaluation on different subsets. This helps to ensure the model’s performance on data distributions.
Importance of This Research
The significance of this research transcends the immediate concerns of the homestay booking ecosystem in Malaysia. By addressing the persistent challenges faced by existing chatbots, this project aspires to contribute to the broader landscape of customer service within the tourism industry.

By refining and advancing chatbot capabilities, particularly in a domain as nuanced as homestay bookings, the research aligns with the trajectory of machine learning algorithms aimed at creating more intelligent, adaptable, and user-centric systems.

In the subsequent sections of this extended proposal, we will delve deeper into each research objective, outlining the methodology, detailing the specific algorithms, and expounding on the potential impact of the findings on both academia and industry.

Report Organization
The rest of the report is organized as per the following:

Chapter 1 shows the Introduction of the thesis which includes the problem background, research scopes, research questions, objectives, aim and the importance of this research.
Chapter 2 represents the literature review on chatbot intent classification, machine learning algorithms for intent classification, context and a brief analysis of the previous researches.
Chapter 3 provides the research methodology, which includes data collection, analysis of the model development.
Chapter 4 describes the design and implementation of the research study.
Chapter 5 shows the complete research results and a comparative analysis of the chosen model performance.
Chapter 6 provides the summary of the research work, achievements and the future works.
The organization of this report is easily understandable and the precise information of each finding enables the reader to quickly access the need of this thesis.




LITERATURE REVIEW
Introduction
The chapter of this research delves into the technological advancements of the homestay booking system. This chapter represents the analytical discussion on the pre-existing chatbots and their challenges in the system. The chapter shows the discussion on the proposed algorithms and their role in classifying the user intents. The chapter begins with the intelligent chatbot for booking system, which shows a comparative study on the pre-existing chatbots and their challenges. Then the chapter continues describing about the intent classification and their categories. Furthermore, the study represents the existing machine learning algorithms for chatbot and the analysis of the proposed algorithms, Naïve Bayes and Support Vector Machine for intent classification in chatbot. This study focuses on the improvement of the existing system and initializing the intent classification of user queries in homestay booking chatbots.

Intelligent Chatbot for Booking System
An intelligent chatbot for booking system involves the application of Artificial Intelligence (AI) and Natural Language Processing (NLP) technologies. After the fourth industrial revolution, [3] chatbots have become prominent in various industries and their interaction into booking systems have revolutionized the approach of business interactions alongside streamline operations with the customers.

The previous studies explore the impact and the benefits of chatbot in a system. Nowadays, chatbots plays a significant role in the financial growth of the tourism business industry. Chatbots provides some key facilities like 24/7 availability, by which user can express his query anytime from anywhere. Following up with the necessary steps to complete the booking process, chatbot assists the user to complete the reservation and supports with personalized recommendations. As a result, through the involvement of intelligent chatbot system, the user experience can be upgraded. Furthermore, the business owners can get idea of the customer preferences, tastes and trends by evaluating the input data. Thus, the intelligent chatbot system reduces the time-taking manual entry in booking process, confusion in legitimacy of the homestay selection, inaccurate information lowers the customer satisfaction levels.

Chatbots are very good at doing repetitive and routine jobs by freeing up human agents to work on more complex projects. This lowers costs for enterprises and improves operational effectiveness. As such, chatbots are adept at answering query questions on room availability, pricing and amenities when it comes to chores like making hotel reservations. The employees can then concentrate on providing guests with outstanding in-person service [7].

The need for digital booking system is growing rapidly to run business with high profits and building more engagements. Every chatbot has a wealth of data, booking patterns, user preferences, and some common queries. Businesses can make wise decisions and acquire insightful knowledge about consumer behaviour by utilizing this data. Based on the knowledge extracted from chatbot interactions, homestay or hotel chain might pinpoint to keep record of the booking times, adjust pricing strategies and tailor marketing campaigns. [9]

A preview of the challenges faced in the previous study:

Table 2.1 Previous Paper study
System

Challenges

Ticketing Chatbot Service using Serverless NLP Technology [10]

Challenges in accurately processing complex queries and adapting various languages
Slang, dialects, and idioms complicate understanding across different cultures and languages.
Concerns over data security arise due to the inefficiency in handling of user information.
Integrating with ticketing systems can also be challenging and results in compatibility issue.
Careful attention is needed in managing unexpected queries or out-of-scope requests
Consistent updates are necessary for better performance and relevance.
Some users might prefer human interactions over chatbot assistance.
Ensuring optimal performance and scalability during peak times can be challenging.
Designing Intelligent Personalized Chatbot for Hotel Services [3]

Accurately capturing nuances in Indonesian language and culture to improve interactions.
Ensuring user data security collected during bookings.
Efficiently connecting the chatbot with hotel systems.
Continuous improvements to maintain accuracy and relevance in responses.
Establishing reliability to gain user acceptance and trust.
Effectively managing complexity to intricate user requests.
Ensuring scalability without sacrificing performance.
Finding the perfect balance between automated responses and human assistance.
Ensuring cost-effectiveness in both development and maintenance.
AI chatbot for Tourism Recommendations [1]

Challenges faced in ensuring accurate and comprehensive local knowledge
AI Chatbot for Hospital Management System [11]

Creates hospital management system with a chatbot, faces various problems like guaranteeing the reliability and confidentiality of the data
Inefficiency to indicate medical queries and precision of system diagnosis.
Integrates system in multiple platforms and lack of trust in the chatbot recommendations, which violates strict regulatory standards.
By delving into the previous research works, the challenges are prominent and their proposal of improvements to the system has made an impactful change. The study of this project is also co-related with the challenges, and it assures to make a useful solution to improvise and cope up with the weaknesses of the existing system.

Intent Classification for Chatbot
Intent classification as basically the conductor of an orchestra, guiding the chatbot's interactions Intent classification as basically the conductor of an orchestra, guiding the chatbot's interactions with users. This vital process utilizes the power of Natural Language Processing (NLP) and Machine Learning (ML) to decipher the users' intentions. The goal of this study is to determine the appropriate intents of the user query in homestay chatbot system.

For example, a human is asks question to a chatbot and expresses his query. [7],[9] Intent classification helps the chatbot understand the real reason behind your question. An appropriate answer is to be found that fits in with the user query. For getting this sort of appropriate results, algorithms like Naive Bayes and Support Vector Machines are used. These algorithms are like expert dancers who have been trained with lots of examples to understand how people talk and what they mean. They can figure out different ways people might ask the same thing.

So, intent classification is not just a technical thing. It's the heart of how chatbots work. It helps them understand what you want, so they can have better, more personal conversations with you.



Figure 2.1 Intent Classification of Chatbot
Categories
The categories of Intent classification are:

Table 2.2 Categories of Intent Classification
Categories

Function

Greeting

Recognizing when a user is saying hello or starting a conversation.

Farewell

Identifying when a user is ending a conversation or saying goodbye.

Information Request

Recognizing when a user is asking for information, such as asking about the weather, news, or a specific fact.

Booking/Reservation

Identifying when a user wants to make a booking or reservation, such as for a hotel room, restaurant table, or flight.

Navigation/Directions

Recognizing when a user needs directions or help with navigation, like finding a route or locating a specific place.

Product/Service Inquiry

Identifying when a user is asking about a product or service, including its features, pricing, or availability.

Support/Help

Recognizing when a user needs assistance or support with a particular issue or problem.

Feedback/Suggestions

Identifying when a user is providing feedback or making suggestions for improvement.

Small Talk/Chitchat

Recognizing when a user engages in casual conversation or makes general comments without a specific request.

From the study of the existing systems, this paper will review some of the questions as a sample. Let us assume the intent class in alphabetical order for a better understanding.

Information
Booking
Availability
The table shows a brief analytical intent classification of the FAQs.

Table 2.3 FAQs Classification
Question

Intent Class

I want to book a homestay in Paris

B

Find me accommodation in London

B

Tell me about homestays in Bali

A

Check availability in Rome for the weekend

C

From the above intent classification, the study shows a brief idea how to classify the data as per the intents. For further implementation, NB and SVM algorithms are initiated to prove the accuracy and efficacy rates of the classification.

Machine Learning Algorithms in Chatbot
The immense influence of Machine Learning knows no bounds in the transformation of rule-based chatbot into intelligent and user-centric conversation chatbots. These chatbots are in high demands in tourism business, e-commerce business, homestay booking and many other applications where human interactions are necessary.

Intent recognition is at the core of this transformation, as machine learning models excel at intent classification. Chatbots can be made much more useful and effective by classifying user questions into specified intents and then responding with accurate and contextually aware responses. Furthermore, it extends to personalization. Chatbots may provide a highly personalized and engaging user experience by customizing their responses, recommendations, and content based on the analysis of user data and preferences.




Figure 2.2 Machine Learning
Chatbots rely heavily on Machine Learning algorithms to comprehend user input, generate coherent responses, and continuously enhance their capabilities. The selection of appropriate algorithms for each chatbot depends on its designated tasks and objectives. Some widely used algorithms and techniques in chatbots include:

Natural Language Processing (NLP):
Backbone of the chatbots
Determine and interpret user-generated text
Uses tokenization, stemming, lemmatization techniques
Enables bots to understand intent, sentiment and syntax of input data
Intent Recognition: Intent recognition is important for understanding the user’s queries and input. Chatbots use several algorithms for intent recognition, including:
Rule-based Systems:

Depends on the predefined rules and patterns to identify user’s intents.
Machine Learning Models:

Supervised learning algorithms like, Support Vector Machine or neural networks used to classify user intent data
Sentiment and detecting spam:
Categorize text using Naive Bayes, Logistic Regression, Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs)
Sequence-to-Sequence Models:
Transformer architecture, are employed for language translation and generate coherent responses in chatbots
Reinforcement Learning (RL):
Used to optimize chatbot responses through interaction
Chatbots learn by trial and error and receive rewards for providing appropriate responses
Dialogue Management:
Often based on RL or Finite State Machines (FSMs)
Determine how the chatbot response to user inputs
Anomaly Detection:
Help chatbots to identify unusual or unexpected user inputs or system behaviour.
Crucial for security and error prevention.
Contextual Understanding:
Chatbots use these techniques to keep track of previous user inputs
The system responses and allows more context-aware interactions
Speech Recognition:
Voice-based chatbots use Hidden Markov Models (HMMs) or Connectionist Temporal Classification (CTC) to convert spoken language into text.
Machine Translation:
Neural Machine Translation (NMT) are used in cross-language communication.
Clustering and Recommendations:
Help chatbots provide personalized suggestions or recommendations basing on user behaviour and preferences.
An analysis on the existing Machine Learning Algorithms:

Table 2.4 Existing Algorithms
Articles

System

ML algorithms

Pros/Cons

[3]

AIML (Artificial Intelligence Markup Language) for building conversational logic and Google Flutter as a framework for developing the cross-platform mobile application.

Finite-State Transducers (FSTs), Hidden Markov Models (HMMs), Conditional Random Fields (CRFs), Recurrent Neural Networks (RNNs) or Transformers

Pros:

Convenience: Offers

24/7 accessibility for

users to access hotel

services, make

bookings, and

receive personalized

assistance at any

time.

Cost Reduction:

Reduces operational

costs by automating

customer service,

sales, and support,

potentially

decreasing staffing

needs.

Personalization:

Provides tailored

services based on

user preferences,

enhancing customer

experience and

loyalty.

Data Collection:

Gathers valuable

data on user

preferences,

behaviours, and

booking patterns,

aiding in targeted

marketing

strategies.

Cross-Platform

Capability: Utilizes

Google Flutter,

Enabling

development across

multiple platforms,

improving

accessibility for a

wider user base.

Cons:

Initial Development

Complexity:

Developing an

effective chatbot

hotel requires significant initial setup and training of the system.

Language and

Cultural Sensitivity:

Ensuring the

chatbot's

understanding of

Indonesian language

nuances and cultural

aspects might pose

challenges.

Dependency on Internet Connectivity: Relies on stable internet connections for seamless interactions, which might hinder accessibility in certain areas.

[12]

AI-powered chatbot

JSON knowledge base Speech and text communication

Bag of Words

preprocessing

Symptom diagnosis prediction

Pros:

Improved healthcare accessibility

Organic conversation

capability

Knowledge base

integration

Symptom diagnosis

Doctor

recommendation

Cons:

Dependency on data

accuracy

Ethical considerations in healthcare data handling

[10]

Chatbot routing agent

Messenger bot

Machine Learning

Morphological analysis

Part-of-Speech (POS) tagging

Pros:

24/7 service availability

Time efficiency

Natural Language Processing (NLP)

Contextual analysis

Cons:

Language-specific rules

Dependency on internet connectivity

[1]

Chatbot with intent classification

Naive Bayes

Logistic Regression

Pros:

Natural language understanding

Intent classification

Accuracy assessment

Comparison of

classification methods

Cons:

Model comparison

complexity

Dependency on training data quality

Basing on the analysis from the previous research works, it is understood that there was only one study which is maximum relevant with this study analysis. So, this research is done to bring a new advancement to the chatbot technology to initiate the trend of more precise and efficient chatbots.

Machine Learning for Intent Classification
As per the current study analysis, the existing homestay booking system are mostly rule-based systems. It lacks the feature of intent recognition using supervised learning algorithms. So, this study focuses on the intent recognition using the two appropriate ML algorithms to get the maximum accurate and efficient outputs.

Naïve Bayes and Support Vector Machine (SVM) are both machine learning algorithms used for classification task. These two algorithms are chosen for this study to emphasize the rule-based features into supervised learning. [1]

Naïve Bayes
Naïve Bayes is a probabilistic classification algorithm. It operates under the assumption so that data are conditionally independent as per the given class label. Despite its seeming oversimplification, Naïve Bayes can be useful in a variety of applications, especially sentiment analysis and text classification. [9]

Intent categorization is one component of chatbot development that needs careful consideration, and Naïve Bayes is a strong decision-maker in this domain. Naïve Bayes utilizes the concept of probability and sorts user inputs into predetermined intents. By examining particular input that fall under each intent category, Naïve Bayes effectively assigns the input to the most probable category. As a result, this probabilistic approach enables chatbots to make well-informed decisions that consider the nuanced complexities of language. The utilization of Naive Bayes algorithm provides several benefits, which include:

Simplicity: Naive Bayes gives a simple and straightforward result for intent classification tasks.
Good Performance: Naive Bayes does independent assumptions but sometimes outperforms expectations, particularly in tasks involving the classification of textual data.
Requires Less Training Data: Naive Bayes is resilient and performs well even with less training datasets.
Support Vector Machine
Support Vector Machine (SVM) is a technique to perform in problems related to regression and classification. It performs best in high-dimensional domains, ensuring strong impact in picture and text categorization. SVM plays a vital role in intent classification of chatbots. It splits the classes of intent in terms of their feature so that it can provide more specified and distinct characteristics to discriminate the accurate intentions.

The following are some advantages of applying the SVM algorithm:

Effective in High-Dimensional Spaces: SVM has higher efficiency in managing large data inputs.
Versatility: SVM has the ability to effortlessly tackle both linear and non-linear classification problems by utilizing a variety of kernel functions.
Robust to Overfitting: In complex intent classification, SVM can avoid the common pitfall of overfitting. This is particularly true in the intricate world of high-dimensional spaces, where achieving a delicate equilibrium is essential.
Summary
This chapter analysed the influence of AI and ML in enhancing the chatbot functionality to detect and classify the intents of user queries using Naïve Bayes and SVM algorithms. This study specifically focuses on the existing homestay booking chatbots of Malaysia. The comprehensive examination and development of the algorithms to classify maximum accurate intents and provide with better user experience. The prime emphasis of this research is to digitalize the chatbots, involving the most advanced AI and ML technology.

Throughout the analysis, Naïve Bayes performs great in handling textual data and uncomplicated methodology, whereas SVM handles complex datasets. The classification of complex inputs is carried out to ease the booking of performances, deliver data-driven insights and boost user experience.



RESEARCH METHODOLOGY
Introduction
In this chapter, machine learning algorithms are evaluated for intent classification. The study conducted in four phases: Literature Review and Problem formulation, Data Preparing and Pre-processing, Algorithm Model Implementation and Result analysis and Discussion. The study starts with the review of existing literature and analysing the problems. Then the paper proceeds with the analytical discussion of the preparation of the existing data and pre-processing them with a comparative study onwards with the next step which is based on the algorithms model implementation. This phase is one of the core sections of this paper. Lastly, the chapter ends with the result analysis and discussion.

Research Framework
The research framework provides a structured approach to the study, ensuring a systematic investigation into enhancing chatbot functionalities for homestay booking systems in Malaysia. This research framework focuses on four phases: Phase-1-Literature Review and problem Formulation, Phase-2- Data Preparing and pre-processing, Phase-3- Algorithm Model Implementation, Phase-4- Result Analysis and Discussion.




Figure 3.1 Research Framework
Phase-1 - Literature Review and Problem Formulation
This phase involves an extensive review of existing literature in the field. The goal here is to gain a comprehensive understanding of the current state of chatbot technologies, specifically focusing on their application in homestay booking systems and the role of machine learning in intent classification. This review will help in identifying gaps in the existing research and formulating the specific problem statement that the study aims to address. A systematic study was done to identify relevant research from several electronic database sites, like, IEEE Xplore, ScienceDirect, Google Scholar and ACM Digital Library. The focus of this search relies on some specific contents and phrases like, “Machine Learning”, “Intent Classification”, “Chatbot”, “SVM”, “Naïve Bayes” and “Homestay Booking system”. This paper used an existing system’s potential user queries as a sample reference for classifying the intents.

Following up with the insights of the literature review, the most relatable and common algorithms are chosen to implement in this project. The selection is done by going through the preliminary studies [3]-[9] and by the relevance and requirement of the existing chatbot booking system compatible with the research objectives. By incorporating the findings from the literature reviews, a solid theoretical analysis has been made in all the phases subsequently. The algorithms “Naïve Bayes” and “SVM” are chosen and these will enable a comprehensive implementation of intent classification in the existing homestay booking systems.

The search was done by going through the English articles, journals that are peer-reviewed, papers of the conference and books between past nine years. The literature review shows the insights about past researches’ algorithms, methodologies, workflows, datasets, and findings. The selected algorithms and datasets are widely used for the purpose of intent classification and detection. The implementation of this project will benefit the existing system and contribute to the advancing knowledge of the research of Chatbot technologies.

Phase 2 - Data Pre-processing
This phase covers the methods used for collecting and preparing data for analysis.

This article will emphasize on real valuable potential user feedback and inquiries from major platforms such as TripAdvisor, Kaggle with a focus on homestay bookings. The pre-processing techniques used, including meticulous cleaning, strategic tokenization, and thorough normalization, ensure the quality and dependability of the system.

The data for this study was obtained from various platforms which relates with the homestay booking. Through an assessment of both frequently asked questions and review question and answers, this research aims to classify and analyses intentions, ultimately validating the purpose of the study.

Phase 3 - Algorithm Model Implementation
In this research paper, the practical implementation of the Naïve Bayes and SVM algorithms are done to calculate efficacy and new findings in order to meet the purpose of this study. A preliminary dataset sample is used to investigate the findings. This investigation is done through distinct phases like coding, model training using pre-processed data and fine-tuning parameters for effective results.

Evaluation Metrics
Machine learning models are thoroughly assessed to using four well-known evaluation metrics-accuracy, precision, recall and F1-score. This stage of the study helps in better understanding of cross-validation, where datasets are divided into subsets to evaluate and examine the model’s effectiveness, consistency and accuracy in data distribution as per the requirements. The comprehensive finding of this study helps us to investigate model’s performance and identify the potential weaknesses. Here’s the four key metrics used to evaluate the result of this investigation.

Precision:
Evaluates algorithm’s positive detection
Measures the proportion of the total correct-positives and incorrect-positives and makes a comparative analysis.
Precision = TP / (TP + FP)

Here, TP: True Positive; FP: False Positive.

Recall:
Measures algorithm’s accurate ability to detect positive instances.
Recall = TP / (TP + FN)

Here, TP: True Positive; FN: False Negative.

F1 Score:
Does comprehensive performance measure by involving both precision and recall.
F1 Score = 2 * (Precision * Recall) / (Precision + Recall)

Accuracy:
Prediction is appropriate or not, it can be measure by accuracy percent.
Determined by evaluating overall correctness.
Accuracy = (TP + TN) / (TP + TN + FP + FN)

Here, TP: True Positive; FP: False Positive; TN: True Negative; FN: False Negative.

Through the evaluation metrics, the comprehensive study is investigated by supervised algorithms utilized for intent classification. This helps us to analyse the result and draw an insightful conclusion in support of the goal of this research.

Phase 4 - Result Analysis and Discussion
This is one of the critical stages of this research methodology. In this phase, the results of the model evaluations are out to do a comparative and comprehensive analysis. These findings are to be examined so that the investigation does not violate the major objective of this proposal. Machine learning models are implemented to determine and justify the intent classification in the chatbot system. User queries in homestay booking are used as practical dataset for the preliminary use in this research.

In the evaluation process, resilient-related user query datasets are collected from various platforms randomly and implemented. The datasets are pre-processed for use in the code while using the two chosen algorithms. The evaluation metrics are processed and examined to perform an analytical study and assess the strengths and weaknesses of each algorithm and their capabilities compared to the existing system. The ultimate result and expected result are analysed. The study supports the upcoming future improvements to strengthen the accuracy and applicability of the outcomes of this testing.

This phase implements the two most relevant and best-chosen algorithms NB and SVM to determine the intent classification of the homestay booking chatbots. User’s intent is being classified and generated insights to contribute to the scopes and objectives of this research.

Chapter Summary
In this chapter, a comprehensive planning and study of the machine learning algorithms is initiated for intent classification for homestay booking system. The research is strategically designed into four phases to be more precise with the understanding. The phases start with the literature review and problem formulation to brief on the preliminary study to specify and identify the current system algorithms and the proposed algorithms that need to be tested. In the second phase, the data chosen to test is being processed by web scrapping technique. In the third phase, the implementation of the algorithms will be conducted and, in this phase, the most appropriate algorithm can be analysed. Lastly, in the fourth step, the study proceeds with the result analysis and a comparative discussion are initiated.


RESEARCH DESIGN AND IMPLEMENTATION
Introduction
The chapter involves the data preparation process through selecting potential necessary datasets, implementing machine learning algorithms, and result analysis for intent classification for homestay booking queries. The work begins with preparing required input data from potentially relevant booking queries by the user and initiating the data as a sample to test through the implementation of several machine learning algorithms. Detecting and classifying intent through the two proposed algorithms and preprocessing the required input to transform into a compatible format following some necessary steps.

This chapter shows how the algorithm models are implemented for the intent classification of chatbots. Naïve Bayes and SVM algorithms are initiated to evaluate the outcomes to allow a comprehensive analysis of each algorithm’s effectiveness and performance. Through various experiments and comparisons, this chapter provides valuable insights on the obtained results of each algorithm.

Research Implementation
In this part of the thesis, the research aims to show and compare the efficiency of the Naïve Bayes and Support Vector Machine algorithms for intent classification of the selected potential datasets.


The goal of this comparative analysis is to evaluate the performance of these two algorithms and understand the best one to classify the intents. This comparison will help to identify the strengths and weaknesses of the algorithms in classification of intents. The study provides required information for selecting the best algorithm.

Naive Bayes is a well-known and widely used algorithm for its simplicity, effectiveness and efficiency in handling text classification tasks, making it particularly well-suited for intent classification. The probabilistic approach of this algorithm calculates the classification feature of the intents. This model allows processing large datasets rapidly and efficiently.

Support Vector Machine (SVM) is suitable for intent classification since it offers robustness in operating high-dimensional data and complex decision boundaries. It has the ability to feed the labelled data, create optimal hyperplane and analyse the results using evaluation metrics: accuracy or precision.



Figure 4.1: Research Implementation

Data Preparation
The process of data preparation involves various steps to carefully pre-process and clean the dataset. About 100 raw datasets consisting of homestay booking queries are used in this research. Each dataset consists of user inquiry related to accommodations, like booking, information, specific facilities or recommendations. The dataset is organized into two parts: the query text (e.g., "How do I book accommodation in Penang?") and the associated intent (e.g., "Booking"). These queries contain various type of intents related to homestay accommodations in Malaysia, using 80% datasets for training classification models and 20% datasets for testing. These raw datasets will be pre-processed and transform into csv format. Now these files can be used for model training and performance assessments. Then, after model training is completed, the model is ready to use the test datasets and show the results. Moving onto the algorithm implementation, Python and Scikit-learn library is used.



Figure 4.2: Raw Dataset
4.3.1 Steps of Data Preprocessing
1. Importing Necessary Modules and Libraries

nltk library is oriented to works with datas which are going to be text type.
stopwords module within NLTK contains a list of common stop words.
word_tokenize is a function which splits text into individual words aka tokens.
WordNetLemmatizer class is used for the purpose lemmatizing words, meaning reducing words to their base or root form hence it simplifies it for application in various linguistic uses.
string and re - python’s standard libraries for string operations and regular expressions.
2. Downloading NLTK Data Files

nltk.download('punkt') is initiates the command to download the tokenizer models.
nltk.download('stopwords') the one downloads list of stop words .
nltk.download('wordnet') is used to download the WordNet data for lemmatization.
3. Defining Queries

queries - list of text strings represent various user queries.
4. Initializing the Lemmatizer and Stop Words

lemmatizer = WordNetLemmatizer(): initializes the WordNet lemmatizer.
stop_words = set(stopwords.words('english')): retrieves and stores the English stop words in a set.
5. Preprocessing Function

Lowercasing: query = query.lower()
Converts the entire query to lowercase to ensure uniformity and avoid case-sensitive issues.

Removing Punctuation: query = re.sub(r'[^\w\s]', '', query)
Uses a regular expression to remove all characters that are not word characters or whitespace. This step helps in removing punctuation marks from the query.

Tokenization: tokens = word_tokenize(query)
Splits the cleaned, lowercase string into individual tokens (words).

Removing Stop Words and Lemmatization: tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
Removing Stop Words: Filters out common words that don't contribute much to the meaning of the sentence (e.g., "is", "in", "at").
Lemmatization:Reduces each word to its base or root form (e.g., "running" becomes "run").
Return Tokens: Returns the processed list of tokens.
6. Displaying Preprocessed Queries
The preprocessing function is applied to each query in the list: preprocessed_queries = [preprocess(query) for query in queries]
Displays all the preprocessed queries.


Figure 4.3 : Pre-processed Dataset
7. Splitting data into Training and Testing sets

The text data (text_data) and their respective labels (Y) are shuffled using the shuffle function from sklearn.utils.
After shuffling, the text data is divided into training and testing sets using the train_test_split function from sklearn.model_selection.
The size of the testing set is defined using test_size=0.2; meaning 20% of all text data will go to the test set, and the rest, 80%, to the training set.
The resulting arrays:
X_train: Text data to be used for training.
X_test: Text data to be held out for testing.
y_train: Labels corresponding to the text data for training.
y_test: Labels corresponding to the text data for testing.
The experiment is done to clean the raw data and preprocess them making the data more uniform. The process assures that the model learns the given set of data samples and finally the selected dataset for testing is used to evaluate the performance of the model.





Figure 4.4: Code of Data Pre-Processing


Figure 4.5: Data Pre-Processing Output
Parameters
In this part of the experiment, various parameters and testing methods of Naïve Bayes and SVM classifiers is elaborated for a better understanding of the model implementation.

SVM:

Kernel: In this thesis, the SVM uses a linear kernel to map the input data into high-dimensional spaces to conduct classification.
Regularization Parameter (C): This is a parameter that controls the tradeoff between achieving a low error on the training set and minimizing model complexity to avoid overfitting. The linear kernel is a default choice for this set.
Testing Procedure: The cross-validation techniques, such as splitting the dataset into training and test sets, are used-80% training and 20% for testing-to ensure generalization.
Metrics of Evaluation:
Accuracy: Measures the percentage of correct predictions.
Precision: Measures the accuracy of positive predictions.
Recall: Assesses the model’s ability to find all relevant instances in the dataset.
F1-Score: Balances precision and recall in a single metric.
Naive Bayes:

Smoothing: The Laplace Smoothing technique ensures none of the features has zero probability during classification.
Text Feature Representation: Text data are first vectorized using the Bag of Words method represented with CountVectorizer. This will convert the textual data into numerical data.
Testing Techniques: As like SVM, Naive Bayes uses an 80-20 split for training and testing based on the smoothing parameter.
Metrics for Evaluation: All the metrics that were used for SVM are the same for this model: Accuracy, Precision, Recall, and F1-Score.
4.4.1 Testing Method
The testing process includes splitting the dataset into training and testing subsets. Once trained, both models predict the labels of the testing data, which are compared against the actual labels to determine the model's performance. The following categories are used-

True Positive (TP): The model correctly classifies a booking query as the actual intent.
False Negative (FN): The model incorrectly predicts a query as a different intent.
False Positive (FP): The model mistakenly classifies a non-relevant query as a target intent.
True Negative (TN): The model correctly identifies irrelevant queries.
Table 4.1 Example of Testing Method
Actual Class

Predicted Class

Output

Booking

Booking

True Positive (TP)

Booking

Information

False Negative (FN)

Information

Booking

False Positive (FP)

Information

Information

True Negative (TN)

These results help assess the classification performance of the model using the classification metrics.

Model Implementation
The model implementation gives a brief idea of the two selected models for classifying intents of homestay booking queries in chatbot. The experiment ensures the comparative analysis and provides justification to the improvement and performance accuracy in this current rule-based chatbot system. The detailed understanding on the proposed solution to detect and classify intents for the homestay booking queries brings a new evolution in the chatbot industry.

4.5.1 Model Architecture
4.5.1.1 Naive Bayes
The following code describes a simple Naive Bayes classifier to categorize homestay booking queries into predefined intents. This code choses dataset of labeled queries, vectorizes the text using CountVectorizer, and trains the model using MultinomialNB. Also, the following code evaluates the performance of the model through metrics such as accuracy, precision, recall, and F1-score, providing a classification report reviewing the effectiveness of the model.





Figure 4.6 Code for Naive Bayes Performance Metrics
4.5.1.2 Support Vector Machine
SVM classifier is used to classify the intents of homestay booking queries. This code works on a labeled dataset of queries, creates feature vectors using the `CountVectorizer`, and encodes labels using `LabelEncoder`. Then it splits data into training and testing sets and uses a support vector machine (SVM) with a linear kernel to train the model. The four-performance metrics accuracy, precision, recall, and F1-score is shown using a bar chart and confusion matrix.





Figure 4.7 Code for SVM Performance Metrics
4.6 Model Efficiency
4.6.1 Naive Bayes
The classification report of Naïve Bayes model shows a strong performance giving 69% accuracy, 80% precision, 69% recall and &1% F1-score. The report demonstrates that among the four types of intents, such as availability, booking, information and recommendations, “booking” query intents give more accurate results compared to other intents.



Figure 4.8 Naïve Bayes Classification Report


Figure 4.9 Naive Bayes Performance Metrics Output
4.6.2 Support Vector Machine
The prepared dataset was used to train the SVM classifier and test it, which resulted in an accuracy of about 56%. Model precision is approximately 73%, the recall is around 56%, and the F1-score is approximately 57%. From the classification report below, it is clear that "Booking" queries were predicted best of all while "Recommendations" were the poorest, with zero recall hence difficulty in detecting this class. Availability and Information classes are standing more or less on equal grounds, as the precision and recall values show greater room for improvement while training.



Figure 4.10 SVM Classification Report


Figure 4.11 SVM Performance Metrics Output
4.7 Chapter Summary
This chapter describes the design and implementation of the machine learning algorithms, Naive Bayes and Support Vector Machine, for intent classification in homestay booking queries of chatbot. It outlines the data preparation process consisting of text preprocessing and dataset splitting, and describes the implementation of the research for both algorithms. While Naive Bayes showed higher accuracy with a more balanced performance between all intent categories, SVM showed strengths in precision but struggled with certain intent categories, especially "Recommendation." The chapter also added information about parameters used by each model, evaluation metrics, and results provide a full overview of the algorithm's effectiveness and the efficiency.

CHAPTER 5
RESULTS, ANALYSIS AND DISCUSSION
5.1 Introduction
This chapter describes the results that are found from the intent classification models and analyse their performance. It also compares the following two algorithms which are Naïve Bayes and Support Vector Mechanism (SVM), by examining the key metrics like accuracy, precision, recall and F1-score. The paper also explores how efficient each of the model is when it comes to classifying user intents based on a dataset of homestay booking queries,

5.2 Research Results and Analysis
In this section, we focus on the results from the intent classification models that were used in the study. We relied on two well-known machine learning algorithms to classify user queries related to homestay bookings. To evaluate how well these models performed, we looked at four key metrics: accuracy, precision, recall, and F1-score—each playing a critical role in understanding the strengths and weaknesses of the models. We also present a comparative visual analysis of the results.

What we found is that both classifiers have their own strengths and areas for improvement. By analysing the confusion matrices, we were able to get a better sense of where each model struggled with misclassifications—whether false positives or false negatives. This gave us deeper insights into the effectiveness of each model.

In the end, both Naive Bayes and SVM proved to be useful for intent classification. Naive Bayes had a slight edge in terms of accuracy and precision, but SVM showed more balanced results across recall and F1-score.

5.2.1 Comparison of Algorithms
The comparison of the two models is done through a graphical representation for a better understanding in their performance metrics on the provided dataset. In this analysis, Naïve Bayes model achieved 69% accuracy, 80% precision, 69% recall and 71% F1-score. It shows great performance identifying “Booking” and “Recommendation”. On the other side, SVM model shows 56% accuracy, 73% precision, 56% recall and 57% F1-scores. SVM also struggled with “Recommendation” category having zero recall which indicates it low performance in comparison to Naïve Bayes. But SVM showed better performance in precision for “Booking” category. Thus, the Naïve Bayes provided better results compared to SVM in classifying user intents.



Figure 5.1 Comparative Classification Report


Figure 5.2 Naïve Bayes Vs SVM performance comparison


Figure 5.3 Naïve Bayes Vs SVM performance metrics
Naive Bayes:



Figure 5.4 Naïve Bayes Confusion Matrix
5.2.1.1 Accuracy
Naive Bayes indicates a strong overall performance having 69% accuracy.
5.2.1.2 Precision
Precision is high with 80%, particularly for "Booking" and "Recommendations."
5.2.1.3 Recall
69% recall indicate its ability to detect relevant instances of various categories.
5.2.1.4 F1 Score
F1-score shows good overall classification performance having 71% rate.
Support Vector Machine:



Figure 5.5 SVM Confusion Matrix
5.2.1.1 Accuracy
SVM shows low accuracy of 56%, showing struggles with certain categories.
5.2.1.2 Precision
73% precision shows strong performance in "Booking" but weaknesses in other categories.
5.2.1.3 Recall
Low recall rate of 56%, fails in the "Recommendations" category.
5.2.1.4 F1 Score
57% f1 score suggests inconsistency in balancing precision and recall.

Table 5.1: Metric Results
Metric

Naive Bayes

SVM

Accuracy

69%

56%

Precision

80%

73%

Recall

69%

56%

F1 Score

71%

57%

5.2.2 Algorithms Efficiency
Naïve Bayes is more effective for text-based datasets which resulted it to provide excellent performance in classifying user intentions. Because of its simplicity it can handle very efficiently and deliver better accuracy and recall. Even though SVM is a bit complex, it performed quite well in precision for “Booking” category. SVM’s weaker performance in recall for “Recommendations” category affected its overall model efficiency. Thus, for this research Naïve Bayes is more suitable and efficient model.

5.3 Future Works
Future research can take guidance from this research study to improvise the model’s generalizability using diverse datasets to classify more complex intents. Additionally, deep learning or hybrid approach to combine multiple algorithms can provide better performance and accuracy. Furthermore, the future approaches can expand to explore classifications in other fields and provide an advanced practical application. Finally, integrating models to identify difficult human intents can bring valuable change in dynamic environments.

CHAPTER 6
CONCLUSION
6.1 Summary
The study involves two machine learning techniques for the intention classification of user queries in homestay booking chatbots. For this research different types of query datasets are used to show the comparative performance of the proposed machine learning algorithms. The model performances are being evaluated where the Naive Bayes classifier with an accuracy of 69% outperforms the SVM’s accuracy of 56%. Naive Bayes classifier excelled in detecting “Recommendations” and also showed a balanced F1 score of 71%. On the other hand, better precision is shown by SVM in the “Booking” category, whereas SVM's recall performance struggled for “Recommendations”. Thus, the analysed results shows that Naive Bayes’ effectiveness is best fit in intent classification for booking queries.

6.2 Achievement of Project Objectives
The thesis successfully fulfilled its objectives by providing a thorough comparative investigation of the machine learning algorithms for intent classification of homestay booking queries. Several experimental steps were taken to find the best selection for the classification. Finally comparing all the performance analysis between the two models, Naïve Bayes classifier has performed better than SVM. The superior performance of Naïve Bayes demonstrates it suitability for intent classification tasks in this context.

The work has evaluated the valuable performance metrics and given noteworthy insights on the algorithm’s strengths and weaknesses, which will act as a practical guidance for the future researches.

6.3 Future Work
The future research works should put emphasis on the expansion of datasets so that a larger and more diverse sample of queries can help to improvise the generalizability of the model. Initiating and exploring advanced text preprocessing techniques and using hybrid models that combines Naïve Bayes and SVM can bring more accuracy and improve efficiency to the system. The scopes should be expanded to include various query types in other advanced fields to provide more comprehensive analysis.


REFERENCES
Alotaibi, R., Ali, A., Alharthi, H., & Almehamdi, R. (2020). AI Chatbot for Tourist Recommendations: A Case Study in the City of Jeddah, Saudi Arabia. International Journal of Interactive Mobile Technologies, 14(19), 18. https://doi.org/10.3991/ijim.v14i19.17201
Ukpabi, D. C., Aslam, B., & Karjaluoto, H. (2019). Chatbot adoption in Tourism Services: A Conceptual Exploration. In Emerald Publishing Limited eBooks (pp. 105–121). https://doi.org/10.1108/978-1-78756-687- 320191006
Putri, F. P., Meidia, H., & Gunawan, D. (2019). Designing Intelligent Personalized Chatbot for Hotel Services. Designing Intelligent Personalized Chatbot for Hotel Services. https://doi.org/10.1145/3377713.3377791
Иванов, С. (2020b). The first chatbot of a tourism/hospitality journal: Editor’s impressions. European Journal of Tourism Research, 24, 2401. https://doi.org/10.54055/ejtr.v24i.403
Dilshan, K. K. D. N., et al. “JESSY: An Intelligence Travel Assistant.” IEEE Xplore, 1 Dec. 2021, ieeexplore.ieee.org/document/9671229
A. T. Al-Tuama and D. A. Nasrawi, "Intent Classification Using Machine Learning Algorithms and Augmented Data," 2022 International Conference on Data Science and Intelligent Computing (ICDSIC), Karbala, Iraq, 2022, pp. 234-239, doi: 10.1109/ICDSIC56987.2022.10075794.
W. M. A. F. W. Hamzah, M. K. Yusof, I. Ismail, M. Makhtar, H. Nawang and A. A. Aziz, "Multiclass Intent Classification for Chatbot Based on Machine Learning Algorithm," 2022 Seventh International Conference on Informatics and Computing (ICIC), Denpasar, Bali, Indonesia, 2022, pp. 01-06, doi: 10.1109/ICIC56845.2022.10006979.
B. Li, N. Jiang, J. Sham, H. Shi and H. Fazal, "Real-World Conversational AI for Hotel Bookings," 2019 Second International Conference on Artificial Intelligence for Industries (AI4I), Laguna Hills, CA, USA, 2019, pp. 58-62, doi: 10.1109/AI4I46381.2019.00022.
M. Y. Helmi Setyawan, R. M. Awangga and S. R. Efendi, "Comparison Of Multinomial Naive Bayes Algorithm And Logistic Regression For Intent Classification In Chatbot," 2018 International Conference on Applied Engineering (ICAE), Batam, Indonesia, 2018, pp. 1-5, doi: 10.1109/INCAE.2018.8579372
E. Handoyo, M. Arfan, Y. A. A. Soetrisno, M. Somantri, A. Sofwan and E. W. Sinuraya, "Ticketing Chatbot Service using Serverless NLP Technology," 2018 5th International Conference on Information Technology, Computer, and Electrical Engineering (ICITACEE), Semarang, Indonesia, 2018, pp. 325-330, doi: 10.1109/ICITACEE.2018.8576921.https://ieeexplore.ieee.org/document/8576921/.
S. R. Dammavalam, N. Chandana, T. R. Rao, A. Lahari and B. Aparna, "AI Based Chatbot for Hospital Management System," 2022 3rd International Conference on Computing, Analytics and Networks (ICAN), Rajpura, Punjab, India, 2022, pp. 1-5, doi:10.1109/ICAN56228.2022.10007105. https://ieeexplore.ieee.org/document/10007105.
Gunawan, Dennis & Putri, Farica & Meidia, Hira. (2020). Bershca: bringing chatbot into hotel industry in Indonesia. TELKOMNIKA (Telecommunication Computing Electronics and Control). 18. 839. 10.12928/telkomnika.v18i2.14841.
Friedman, N., Geiger, D., & Goldszmidt, M. (1997). Bayesian Network Classifiers. Machine Learning, 29(2/3), 131–163. https://doi.org/10.1023/a:1007465528199
Hsu, C., Chang, C., & Lin, C. (2003). A Practical guide to support vector Classification Chih-Wei Hsu, Chih-Chung Chang, and Chih-Jen Lin. ResearchGate. https://www.researchgate.net/publication/2926909_A_Practical_Guide_to_Support_Vector_Classification_Chih-Wei_Hsu_Chih-Chung_Chang_and_Chih-Jen_Lin
Vannala, R., Swathi, S., & Puranam, Y. (2022). AI chatbot for answering FAQ’s. 2022 IEEE 2nd International Conference on Sustainable Energy and Future Electric Transportation (SeFeT). https://doi.org/10.1109/sefet55524.2022.9908774
Zhirui, Y., & Li, C. (2020). Analysis of Sentiment Classification of Hotel Reviews Based on Multinomial Naive Bayes. Analysis of Sentiment Classification of Hotel Reviews Based on Multinomial Naive Bayes. https://doi.org/10.1145/3414752.3414796
Setyawan, M. Y. H., Awangga, R. M., & Efendi, S. R. (2018). Comparison Of Multinomial Naive Bayes Algorithm And Logistic Regression For Intent Classification In Chatbot. Comparison of Multinomial Naive Bayes Algorithm and Logistic Regression for Intent Classification in Chatbot. https://doi.org/10.1109/incae.2018.8579372
Gowda, C. P. M., Srivastava, A., Chakraborty, S., Ghosh, A., & Raj, H. (2021). Development of Information Technology Telecom Chatbot: an artificial intelligence and machine learning approach. 2021 2nd International Conference on Intelligent Engineering and Management (ICIEM). https://doi.org/10.1109/iciem51511.2021.9445354
A. H. Hefny, G. A. Dafoulas and M. A. Ismail, "Intent Classification for a Management Conversational Assistant," 2020 15th International Conference on Computer Engineering and Systems (ICCES), Cairo, Egypt, 2020, pp. 1-6, doi: 10.1109/ICCES51560.2020.9334685.
W. M. A. F. W. Hamzah, M. K. Yusof, I. Ismail, M. Makhtar, H. Nawang and A. A. Aziz, "Multiclass Intent Classification for Chatbot Based on Machine Learning Algorithm," 2022 Seventh International Conference on Informatics and Computing (ICIC), Denpasar, Bali, Indonesia, 2022, pp. 01-06, doi:10.1109/ICIC56845.2022.10006979.
Sang-Bum Kim, Hee-Cheol Seo, and Hae-Chang Rim. 2003. Poisson naive Bayes for text classification with feature weighting. In Proceedings of the sixth international workshop on Information retrieval with Asian languages - Volume 11 (AsianIR '03). Association for Computational Linguistics, USA, 33–40. https://doi.org/10.3115/1118935.1118940
A. Souha, C. Ouaddi, L. Benaddi and A. Jakimi, "Pre-Trained Models for Intent Classification in Chatbot: A Comparative Study and Critical Analysis," 2023 6th International Conference on Advanced Communication Technologies and Networking (CommNet), Rabat, Morocco, 2023, pp. 1-6, doi: 10.1109/CommNet60167.2023.10365312.
Y. Liu, X. Li and Z. Xiang, "The Effect of Chatbot-customer Interaction on Consumer Brand Advocacy: Exploring the Role of Chatbots," 2022 IEEE 12th International Conference on Electronics Information and Emergency Communication (ICEIEC), Beijing, China, 2022, pp. 185-190, doi: 10.1109/ICEIEC54567.2022.9835050.