# Project Ideas for a Computer Network and Security Final Research Project

## 1. Main Finding After Research

You are right to question the earlier idea.

A simple awareness app is too weak for a Computer Network and Security project. The project needs a technical artifact, even if it is only a demo/prototype. The artifact should detect, score, classify, or analyze scam-related cyber threats.

The research connection is this:

- Malaysia has a real cyber fraud problem, with fraud, phishing, impersonation, fraudulent websites, and malicious APKs repeatedly appearing in current incident reports.
- Recent papers show that online fraud victimization is connected to measurable factors such as overconfidence, social influence, risky behavior, and weak safe practice.
- Recent phishing and malware research is moving toward AI/ML detection, small language models, explainable phishing analysis, Android APK static analysis, and scenario-based testing.
- Recent anti-phishing training research shows that normal training alone often does not reduce phishing clicks enough, so a final project should not be only awareness/training.

So the best direction is:

> Build a small cybersecurity detection and analysis system that connects scam behavior factors with technical scam indicators.

## 2. Best Overall Idea

## ScamShield-MY: Hybrid Scam Detection and Revictimization Risk Analysis System

### Simple idea

A web-based demo where users or researchers can test suspicious scam content such as:

- SMS text,
- WhatsApp-style messages,
- suspicious URLs,
- investment scam messages,
- fake authority messages,
- fake APK/app permission details.

The system classifies the content as:

- likely safe,
- suspicious,
- high-risk scam.

It also explains what scam cues were detected:

- urgency,
- authority impersonation,
- financial pressure,
- emotional manipulation,
- suspicious link,
- request for APK installation,
- request for OTP/password/banking information,
- fake investment/clone firm pattern.

### Why this is useful

This is not an awareness project. It becomes a cybersecurity detection project.

The useful output is:

- a scam detection demo,
- a feature extraction method,
- a risk scoring engine,
- a small Malaysian scam scenario dataset,
- a dashboard showing detected scam cues,
- testing results using public datasets and sample Malaysian-style scam scenarios.

### Why it fits Computer Network and Security

It includes:

- phishing/smishing detection,
- URL analysis,
- social engineering cue detection,
- optional Android APK risk analysis,
- machine learning or small language model comparison,
- cybersecurity evaluation metrics.

### How it connects to the current report

The existing seven factors can become detection/risk categories:

| Research factor | Technical detection angle |
|---|---|
| Overconfidence | user ignores warnings or chooses risky response in scenario testing |
| Social influence | messages mention group proof, friends, testimonials, Telegram/WhatsApp groups |
| Authority impersonation | fake bank, PDRM, LHDN, court, customs, NSRC, SC, delivery company |
| Urgency and fear | "act now", "account blocked", "warrant", "last chance", "within 24 hours" |
| Emotional grooming | romance, sympathy, trust-building, shame, recovery scam |
| Financial pressure | high return, guaranteed profit, loan approval, debt/fine threat |
| Protective capability | whether user checks URL, Semak Mule, SC Investor Alert, bank hotline, NSRC |

### Demo scope

The demo does not need to be huge.

Minimum demo:

1. Text input for suspicious message.
2. Optional URL input.
3. Rule-based cue extractor.
4. ML classifier for SMS phishing/smishing.
5. Risk score output.
6. Explanation panel.
7. Researcher test table with accuracy, precision, recall, F1-score.

Better demo:

1. Add URL feature extraction.
2. Add Malay/English scam cue dictionary.
3. Add fake investment/clone firm indicator.
4. Add simple scenario test where users choose an action.
5. Add dashboard showing which factor caused the risk score.

Advanced demo:

1. Compare classical ML vs small language model.
2. Add Android APK static permission risk analysis.
3. Add local threat intelligence links such as SC Investor Alert and Semak Mule as manual-check references.

### Suggested title

**ScamShield-MY: A Hybrid Scam Detection and Revictimization Risk Analysis System for Malaysian Online Fraud Prevention**

## 3. Other Legit Project Ideas

## Idea 1: Smishing and Scam Message Classifier for Malaysian Users

### What it does

Classifies SMS/WhatsApp-style messages as legitimate, spam, or scam/smishing.

### Technical method

- Use public SMS phishing dataset.
- Train machine learning models:
  - Logistic Regression
  - SVM
  - Random Forest
  - Naive Bayes
  - LSTM or BERT if possible
- Add Malaysian scam cue dictionary:
  - bank account frozen,
  - LHDN tax issue,
  - PDRM case,
  - parcel/customs fee,
  - fake loan,
  - investment group,
  - APK file request.

### Output

- classifier,
- confusion matrix,
- accuracy/precision/recall/F1,
- explanation of detected cues.

### Strength

Very doable and clearly technical.

### Weakness

If it only detects text, it may feel slightly narrow unless connected to Malaysia and revictimization.

## Idea 2: Phishing URL Detection Using ML and Small Language Models

### What it does

Detects whether a suspicious URL is likely phishing.

### Technical method

- Extract URL features:
  - length,
  - number of dots,
  - IP address use,
  - suspicious words,
  - HTTPS,
  - domain age if available,
  - URL entropy,
  - brand impersonation words.
- Compare ML classifiers and an LLM/SLM prompt-based classifier.

### Output

- URL risk score,
- explanation of features,
- benchmark table.

### Strength

Very Computer Network and Security friendly.

### Weakness

It may drift away from the original revictimization topic unless combined with scenario/user-risk analysis.

## Idea 3: Malicious APK Risk Analyzer for Scam Apps

### What it does

Analyzes Android APK permission and manifest information to detect suspicious scam app behavior.

### Technical method

- Extract static APK features:
  - permissions,
  - services,
  - receivers,
  - suspicious API calls,
  - SMS access,
  - overlay permission,
  - accessibility service usage,
  - package metadata.
- Train or simulate a rule-based/ML risk score.

### Output

- APK risk level,
- suspicious permission list,
- explanation of why an APK is risky.

### Strength

Very strong CNS direction because Malaysia has malicious APK scam problems.

### Weakness

Handling real malware samples can be risky. Safer path is to use static sample manifests or public datasets, not live malicious APK execution.

## Idea 4: Scam Threat Intelligence Dashboard for Malaysia

### What it does

Creates a dashboard of scam indicators from public sources:

- suspicious URLs,
- clone investment entities,
- mule account checking references,
- scam phone/account patterns,
- scam categories.

### Technical method

- OSINT collection from public alerts.
- Store indicators in a simple database.
- Build graph relationships:
  - phone number,
  - bank account,
  - domain,
  - company name,
  - scam type,
  - source.
- Risk-rank indicators.

### Output

- searchable dashboard,
- scam graph,
- risk scoring,
- evidence/source links.

### Strength

Useful for faculty because it creates a reusable local cyber threat intelligence resource.

### Weakness

Some public sources may block automated scraping, so the project may need manual dataset creation.

## Idea 5: AI-Generated Scam Message Detection and Defense

### What it does

Tests whether AI-generated scam messages are harder to detect than normal scam messages, then builds a detector.

### Technical method

- Create safe synthetic scam messages in English and Malay.
- Label scam cues.
- Compare:
  - traditional ML,
  - BERT/transformer,
  - small LLM prompt classification.
- Test adversarial examples:
  - polite scam,
  - no spelling mistakes,
  - authority tone,
  - multilingual messages.

### Output

- dataset,
- detector,
- benchmark results,
- explanation of AI-enabled scam risks.

### Strength

Very current and research-worthy.

### Weakness

Needs careful ethics so it does not become a guide for writing better scam messages.

## Idea 6: Just-in-Time Scam Warning Browser Extension

### What it does

Warns users when they visit or type suspicious scam content.

### Technical method

- Browser extension reads page text/URL locally.
- Detects scam cues:
  - fake login,
  - investment promises,
  - urgency,
  - payment request,
  - suspicious domain.
- Shows a warning panel before the user clicks risky links.

### Output

- browser extension demo,
- scam cue detection,
- warning logic,
- user testing with sample pages.

### Strength

More useful than awareness because it intervenes at the risky moment.

### Weakness

Browser extension development may take more time.

## 4. Comparison of Ideas

| Idea | Technical value | Research value | Demo difficulty | Fit with current topic | Recommendation |
|---|---:|---:|---:|---:|---|
| ScamShield-MY hybrid system | High | High | Medium | Very high | Best |
| Smishing classifier | Medium-high | Medium | Low-medium | High | Good fallback |
| Phishing URL detector | High | Medium | Medium | Medium | Good technical add-on |
| Malicious APK analyzer | Very high | High | Medium-high | High | Strong but needs care |
| Scam threat intelligence dashboard | High | High | Medium | High | Useful if data collection is possible |
| AI-generated scam detection | High | High | Medium | Medium-high | Good modern research angle |
| Browser warning extension | High | Medium | Medium-high | Medium | Good if implementation time exists |

## 5. My Recommended Final Direction

The strongest and most balanced option is:

> **ScamShield-MY: A Hybrid Scam Detection and Revictimization Risk Analysis System**

It should combine three parts:

1. **Scam Content Detection**
   - Detect phishing/smishing/scam cues in messages and URLs.

2. **Victim/Revictimization Risk Scoring**
   - Use the seven-factor model to score why a user may be vulnerable.

3. **Scenario-Based Evaluation**
   - Test whether users choose safe, partial, or risky responses in Malaysian scam scenarios.

This gives the project a real artifact and measurable output. It also keeps the existing research useful instead of throwing it away.

## 6. What Chapter 4 and Chapter 5 Can Become

### Chapter 4: Research Design and Implementation

This chapter can explain:

- system architecture,
- dataset preparation,
- scam cue feature extraction,
- ML/LLM classifier design,
- seven-factor scoring model,
- scenario simulator,
- prototype interface,
- privacy and ethical safeguards.

### Chapter 5: Results, Analysis and Discussion

This chapter can include:

- classifier performance,
- confusion matrix,
- precision/recall/F1-score,
- examples of correctly detected scam messages,
- examples of false positives/false negatives,
- scenario response scoring,
- discussion of which scam cues were hardest to detect,
- discussion of how the system supports revictimization prevention.

## 7. Possible Dataset and Testing Plan

### Dataset 1: SMS phishing/smishing dataset

Use a public SMS phishing dataset for baseline model training/testing.

Possible use:

- classify ham/spam/smishing,
- test ML models,
- report accuracy, precision, recall, F1-score.

### Dataset 2: URL phishing dataset

Use a public phishing URL dataset or manually collected phishing/legitimate URLs.

Possible use:

- extract URL features,
- classify URL risk,
- compare ML vs rule-based detection.

### Dataset 3: Malaysian-style scam scenario set

Create a small dataset of fictional but realistic Malaysian scam messages:

- Macau scam,
- fake bank warning,
- fake NSRC recovery scam,
- fake LHDN/tax message,
- fake parcel/customs payment,
- fake job offer,
- fake investment Telegram group,
- malicious APK delivery scam.

Important: these should be fictional and safe, not copied from active scam operations.

### Dataset 4: Optional APK static feature set

Use only safe static APK metadata or public malware-feature datasets.

Do not run live malware.

## 8. Why This Benefits the Faculty

This project gives the faculty something useful:

- a Malaysia-focused cyber fraud detection prototype,
- a reusable scenario dataset,
- a risk scoring model,
- a technical benchmark,
- a local cybersecurity case study,
- a foundation for future students to improve with better datasets or models.

It also fits Computer Network and Security because it covers:

- phishing,
- smishing,
- malicious URLs,
- Android scam APK risk,
- social engineering,
- cyber threat intelligence,
- security analytics,
- ML/AI-based detection.

## 9. Research Sources That Support This Direction

1. Balakrishnan, Ahhmed and Basheer, 2025, PLOS ONE.
   - Malaysian adult study found overconfidence and social influence significantly predicted online fraud victimization.
   - Link: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0317232

2. MyCERT Cyber Incident Quarterly Summary Report Q4 2025.
   - Fraud remained the largest reported incident category, with phishing campaigns, impersonation scams, fraudulent websites, and scam APK patterns.
   - Link: https://www.mycert.org.my/portal/advisory?id=SR-033.042026

3. NSRC official guidance.
   - Confirms Malaysia's online financial fraud response flow and reporting route through bank hotline/NSRC 997/police report.
   - Link: https://nfcc.jpm.gov.my/index.php/en/about-nsrc

4. Goldenits et al., 2025, Small Language Models for Phishing Website Detection.
   - Shows SLMs can be used for phishing website detection while balancing cost, privacy, and deployability.
   - Link: https://arxiv.org/abs/2511.15434

5. Nasution et al., 2025, Benchmarking 21 Open-Source LLMs for Phishing Link Detection.
   - Shows open-source LLMs can reach strong phishing URL detection performance with proper prompting.
   - Link: https://www.mdpi.com/2078-2489/16/5/366

6. Lin, Liu and Fan, 2025, Improving Phishing Email Detection Performance of Small LLMs.
   - Shows prompt engineering, explanation-augmented fine-tuning, and ensembles can improve small LLM phishing detection.
   - Link: https://arxiv.org/abs/2505.00034

7. Anti-Phishing Training Does Not Work, 2025.
   - Large-scale study found conventional training did not significantly reduce phishing clicks or improve reporting, supporting the need for technical controls and measurement.
   - Link: https://arxiv.org/html/2506.19899v1

8. Understanding Influences on SMS Phishing Detection, USEC 2025.
   - Shows users struggle with smishing detection, especially identifying real messages correctly, supporting scenario-based testing.
   - Link: https://www.ndss-symposium.org/wp-content/uploads/usec25-27.pdf

9. SMS Phishing Dataset for Machine Learning and Pattern Recognition, Mendeley Data.
   - Provides 5,971 labelled messages for ham/spam/smishing classification.
   - Link: https://data.mendeley.com/datasets/f45bkkt8pr/1

10. LAMD, 2025.
   - Shows context-driven LLM-based Android malware detection using static analysis and explainable reasoning.
   - Link: https://arxiv.org/html/2502.13055v2

11. Enhancing Android Malware Detection with Retrieval-Augmented Generation, 2025.
   - Uses static features, LLM-generated functional descriptions, and transformer-based classification for Android malware detection.
   - Link: https://arxiv.org/html/2506.22750v1

12. Routine activities and fraud re-victimization among older adults, 2026.
   - Shows prior fraud victimization increases later fraud exposure/loss, supporting the revictimization angle.
   - Link: https://journals.sagepub.com/doi/abs/10.1177/17488958241257860

13. Patterns and Predictors of Cyber Fraud Victimization, 2025.
   - Shows attempted fraud and actual victimization should be separated, and that only a few victims changed preventive behavior after victimization.
   - Link: https://www.researchgate.net/publication/394891842_Patterns_and_Predictors_of_Cyber_Fraud_Victimization_Testing_Routine_Activity_Theory_and_General_Theory_of_Crime_in_Japan

## 10. Final Answer

The project should become a technical CNS project, not a humanities-style awareness paper.

Best final concept:

> **ScamShield-MY: Hybrid Scam Detection and Revictimization Risk Analysis System**

The final report can then legitimately say:

- a cybersecurity problem was studied,
- current research and Malaysian incident data were analyzed,
- a detection/risk scoring model was designed,
- a prototype/demo was implemented,
- public datasets and Malaysian-style scenarios were used for testing,
- the system gives measurable outputs and can support future cyber fraud prevention work.

