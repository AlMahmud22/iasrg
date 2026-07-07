from __future__ import annotations

import re
import zipfile
import os
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[2]
WORKING = ROOT / "02_working_record"
ACTIVE_DIR = WORKING / "current_from_2026-06-27"
PROJECT_DIR = WORKING / "03_cyber_fraud_research_report_2026-04_to_2026-06"
FINAL_MD = ACTIVE_DIR / "cyber_fraud_research_report_final.md"
FINAL_DIR = PROJECT_DIR / "final_outputs"
FINAL_DOCX = FINAL_DIR / "Cyber_Fraud_Research_Report_Final.docx"
TEMPLATE = PROJECT_DIR / "research_report_guidelines" / "Template_Tesis_UTM_PSM_UG_SC_Research.docx"

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


def rel(path: Path) -> str:
    return os.path.relpath(path, ACTIVE_DIR).replace("\\", "/")


FIG1 = rel(PROJECT_DIR / "figures_conceptual" / "fig1.png")
FIG8 = rel(PROJECT_DIR / "figures_conceptual" / "fig8.png")
FIG9 = rel(PROJECT_DIR / "figures_conceptual" / "fig9.png")
PROOF2 = rel(PROJECT_DIR / "proofs_live" / "proof2.png")
PROOF3 = rel(PROJECT_DIR / "proofs_live" / "proof3.png")
PROOF5 = rel(PROJECT_DIR / "proofs_live" / "proof5.png")
PROOF6 = rel(PROJECT_DIR / "proofs_live" / "proof6.png")
CHART_TREND = rel(PROJECT_DIR / "source_library" / "analysis_outputs" / "cyber999_total_vs_fraud_trend.svg")
CHART_Q2 = rel(PROJECT_DIR / "source_library" / "analysis_outputs" / "cyber999_top_fraud_categories_q2_2025.svg")
CHART_COVERAGE = rel(PROJECT_DIR / "source_library" / "analysis_outputs" / "seven_factor_evidence_coverage.svg")
CHART_TOOLS = rel(PROJECT_DIR / "source_library" / "analysis_outputs" / "malaysia_scam_response_tool_map.svg")


REPORT_MD = f"""# Study on Identification of Factors and Development of Modules for Methods to Prevent Cyber Fraud Revictimization Problems Among Public in Malaysia

**Final Research Report**

**Prepared as a data-honest research framework and secondary-source analysis report**

**Date:** July 2026

[[PAGE_BREAK]]

## Abstract

Cyber fraud remains a serious public-facing cybersecurity and financial safety problem. In Malaysia, the public receives scam messages, calls, investment offers, impersonation attempts, phishing links, malicious application prompts, fake support messages and fraudulent payment requests through familiar digital channels. Existing awareness messages are useful, but awareness alone does not fully explain why some people continue to respond to scams, delay reporting, trust false authority cues or become exposed again after an earlier victimization experience. This report studies cyber fraud revictimization as a behavioural, social, emotional and practical protection problem.

The study integrates the Theory of Planned Behavior, Protection Motivation Theory and Cognitive Appraisal Theory. From these theories and the evidence reviewed, the report develops a seven-factor backbone: awareness gap; social influence and trust transfer; authority impersonation; urgency and fear; emotional grooming, shame and recovery; financial need and fear of missing out; and protective self-efficacy and reporting. The report also proposes a five-module intervention framework that focuses on scam awareness, cue detection, threat and coping appraisal, verification and reporting routines, and recovery support.

This final version is deliberately data-honest. It includes official secondary analysis from Cyber999/MyCERT incident reports, PDRM public warnings, Securities Commission Malaysia guidance, NSRC/Semak Mule/Cyber999 tool information and open-access academic literature. It does not claim survey findings or intervention effectiveness because no primary survey or module-testing dataset is available for this report. Instead, it provides a complete research design, measurement plan, scenario scoring method, module framework, appendices and secondary-source analysis that can support later empirical data collection.

**Keywords:** cyber fraud, revictimization, scam prevention, Malaysia, behavioural cybersecurity, Theory of Planned Behavior, Protection Motivation Theory, Cognitive Appraisal Theory, Cyber999, Semak Mule.

[[PAGE_BREAK]]

## Table of Contents

[[TOC]]

[[PAGE_BREAK]]

# CHAPTER 1: INTRODUCTION

## 1.1 Introduction

Cyber fraud has become part of everyday digital risk. The public now uses mobile banking, e-wallets, social media, messaging applications, online marketplaces and digital investment platforms as normal parts of daily life. These same channels are also used by scammers to create false trust, urgency and pressure. A scam may appear as an investment opportunity, a delivery message, a fake authority warning, a job offer, a romance approach, a payment instruction, a malicious application prompt or a support-channel impersonation.

This report focuses on cyber fraud revictimization among the public in Malaysia. Revictimization is treated as more than simply being exposed to scams many times. In this study, revictimization refers to repeated victimization, repeated risky compliance after previous exposure, recovery-scam targeting after an earlier loss, delayed reporting caused by shame or low confidence, and continued vulnerability where a person does not know how to verify, refuse or report suspicious contact.

## 1.2 Problem Background

Official and regulatory sources show that scam activity is not limited to one channel. Cyber999/MyCERT quarterly reports identify fraud as a major category of handled cyber incidents, with phishing and impersonation/spoofing appearing repeatedly as high-volume fraud types [OFF-09; OFF-10; OFF-11]. PDRM public warnings also describe job scams, impersonation, urgent borrowing, AI voice misuse and reminders to use NSRC 997 quickly after financial scam incidents [OFF-05]. Securities Commission Malaysia guidance identifies common investment scam warning signs such as unrealistic returns, pressure, unrelated bank accounts, fake documents, fake testimonials and clone entities [OFF-13; OFF-14; OFF-15].

These sources point to a practical research problem. The public is not only facing a lack of information. People may know that scams exist but still respond when the scam feels urgent, socially supported, emotionally convincing, financially attractive or officially legitimate. After victimization, shame, self-blame and confusion may delay help-seeking, which can increase exposure to recovery scams or further manipulation [ACA-04; ACA-08]. Therefore, a prevention approach needs to address awareness, judgement, emotion, verification skill and reporting confidence together.

## 1.3 Research Gap

Many prevention efforts focus on warning the public about scam types. This is necessary, but it does not fully explain behavioural response under pressure. The literature on online fraud victimization shows that behavioural predictors such as social influence and overconfidence can affect victimization risk [ACA-01; ACA-02]. Wider phishing-mitigation literature also shows that technical controls and human-centred training must work together, because technology-only approaches cannot remove all human-facing scam pressure [ACA-10].

The specific gap addressed by this report is the connection between cyber fraud revictimization factors and measurable intervention content. The report does not stop at listing scam types. It organizes the factors into a seven-factor backbone, links them to behavioural theories, translates them into questionnaire constructs and scenario tasks, and maps them to intervention modules that can later be evaluated.

## 1.4 Research Aim

The aim of this study is to identify key factors associated with cyber fraud revictimization among the public in Malaysia and to develop a theory-based module framework that can strengthen scam recognition, verification behaviour, reporting capability and recovery resistance.

## 1.5 Research Questions

1. What behavioural, social, emotional and practical protection factors are associated with cyber fraud revictimization tendency among the public?
2. How can TPB, PMT and Cognitive Appraisal Theory explain public response to scam cues under pressure?
3. How can official Malaysian scam evidence and academic literature be organized into a seven-factor revictimization framework?
4. What intervention modules can be designed to improve scam cue detection, verification, reporting and recovery support?
5. How should the proposed modules be evaluated without claiming unsupported results before primary data is collected?

## 1.6 Research Objectives

1. To define cyber fraud revictimization as a measurable behavioural and protection problem.
2. To identify factors that contribute to revictimization tendency using official sources and academic literature.
3. To develop a seven-factor framework grounded in TPB, PMT and Cognitive Appraisal Theory.
4. To design intervention modules that address awareness, cue detection, coping appraisal, verification and recovery support.
5. To prepare a data-honest analysis framework using official secondary data and a future-ready primary research design.

## 1.7 Research Scope

The study focuses on cyber fraud affecting the public, especially scams involving phishing, impersonation, investment deception, job scams, malicious application prompts, urgent payment requests, social proof manipulation and fake support or recovery channels. The scope is behavioural and preventive. It does not perform malware reverse engineering, syndicate investigation, financial forensics or production-system development.

The evidence base prioritizes official Malaysian sources and open-access academic literature. Cyber999, PDRM, NSRC, Semak Mule and Securities Commission Malaysia sources are used for local context. Academic sources are used for behavioural factors, victim impact, theory and intervention design. News or vendor sources are not used as primary national statistics unless clearly identified as secondary context.

## 1.8 Research Contribution

The report contributes a structured revictimization framework and module design that can be used for later empirical testing. It separates awareness from protective capability, and it separates official secondary indicators from future survey or intervention data. This distinction is important because research credibility depends on not mixing incompatible datasets or reporting findings before the data exists.

## 1.9 Chapter Summary

This chapter introduced cyber fraud revictimization as a behavioural and protection problem. It explained the problem background, research gap, aim, questions, objectives, scope and contribution. The next chapter reviews the literature and evidence that support the seven-factor framework.

[[PAGE_BREAK]]

# CHAPTER 2: LITERATURE REVIEW

## 2.1 Introduction

This chapter reviews official and academic evidence related to cyber fraud, revictimization and prevention. The review is organized around the Malaysian cyber fraud context, major scam techniques, theoretical foundations, the seven-factor backbone and gaps in existing prevention approaches.

## 2.2 Malaysian Cyber Fraud Context

Cyber999/MyCERT quarterly reports show that fraud is a major category in handled cyber incident reports. In Q1 2025, Cyber999 recorded 1,657 total incidents, with 1,126 fraud incidents. In Q2 2025, total incidents increased to 2,058, with 1,633 fraud incidents. In Q3 2025, total incidents remained high at 2,020, with 1,521 fraud incidents [OFF-09; OFF-10; OFF-11]. These figures should be interpreted as Cyber999-handled incidents, not as all national police cases.

![Figure 2.1: Cyber999 total incidents and fraud incidents by quarter. Source: OFF-09, OFF-10, OFF-11, OFF-18.]({CHART_TREND})

The available Cyber999 data also shows that phishing and impersonation/spoofing are important fraud categories. In Q2 2025, Cyber999 recorded 1,127 phishing incidents and 341 impersonation/spoofing incidents within its fraud category [OFF-10]. This supports the need for prevention modules that focus on cue detection, authority verification, and safe response routines.

![Figure 2.2: Cyber999 fraud categories in Q2 2025. Source: OFF-10.]({CHART_Q2})

## 2.3 Scam Types and Techniques

The report groups cyber fraud techniques into several practical categories. Phishing involves messages, links or websites that attempt to obtain credentials or trigger unsafe action. Impersonation scams involve false authority, fake institutions, familiar contacts or trusted-looking representatives. Investment scams use high returns, urgency, limited-time pressure, fake testimonials, clone entities and unrelated payment accounts [OFF-13]. Job scams may ask victims to pay fees, perform task-based transfers or provide personal information [OFF-05].

Scams also use emotional and social manipulation. Romance or love scams can create trust and dependency before requesting money or personal assistance [ACA-09]. Recovery or support-channel impersonation can target victims after they have already suffered loss, especially when they are ashamed, confused or desperate for help [OFF-05; PROOF-06]. This makes post-victim support and safe reporting channels important parts of revictimization prevention.

## 2.4 Theoretical Foundation

The Theory of Planned Behavior explains how attitude, subjective norms and perceived behavioural control influence intention and behaviour. In this study, attitude refers to whether verification and reporting are viewed as necessary and worthwhile. Subjective norms refer to whether family, peers and institutions support safe action. Perceived behavioural control refers to whether a person believes protective steps can actually be performed [Ajzen, 1991].

Protection Motivation Theory explains why threat awareness alone is insufficient. A person must see the threat as serious and personally relevant, but must also believe that safe action is effective and possible. If fear is high but coping ability is low, the person may panic, avoid reporting or comply with scam instructions instead of protecting themselves [Rogers, 1975; Rogers, 1983; ACA-06].

Cognitive Appraisal Theory helps explain the moment of decision. Under time pressure, a person appraises whether the event is dangerous, urgent, legitimate and manageable. This appraisal can be shaped by authority cues, social proof, emotional grooming, shame or financial pressure. The intervention framework therefore needs to train calm appraisal, not just factual knowledge.

## 2.5 Seven-Factor Revictimization Framework

The seven-factor backbone is the central structure of this report. It translates theory and evidence into measurable constructs and module design.

| Factor | Meaning | Main theory link | Example measurement focus |
|---|---|---|---|
| F1 | Awareness gap | TPB, PMT | Recognizing scam cues and avoiding overconfidence |
| F2 | Social influence and trust transfer | TPB | Resistance to fake testimonials, group pressure and familiar-contact misuse |
| F3 | Authority impersonation | Cognitive appraisal, TPB | Independent verification of official-sounding requests |
| F4 | Urgency and fear | PMT, cognitive appraisal | Pause-before-action and refusal of rushed instructions |
| F5 | Emotional grooming, shame and recovery | Cognitive appraisal | Help-seeking, non-blaming recovery and recovery-scam resistance |
| F6 | Financial need and FOMO | Cognitive appraisal, TPB | Identifying unrealistic returns, task fees and reward pressure |
| F7 | Protective self-efficacy and reporting | PMT, TPB | Use of NSRC, Semak Mule, Cyber999, SC Investment Checker and bank hotlines |

![Figure 2.3: Seven-factor framework for cyber fraud revictimization.]({FIG1})

## 2.6 Factor Evidence

F1 covers the awareness-behaviour gap. People may know scams exist but still click, reply, transfer, install or delay checking because the message appears familiar. The PLOS ONE online fraud victimization study supports the importance of behavioural predictors, including overconfidence and social influence [ACA-01; ACA-02].

F2 covers social influence and trust transfer. Scammers may create false credibility through group chats, fake testimonials, agents, celebrity misuse, familiar contacts or peer approval. SC scam guidance specifically warns about fake testimonials, social media promotion and clone entities in investment scams [OFF-13].

F3 covers authority impersonation. Scammers misuse institutional language and false official identity. PDRM warnings and SC guidance show how impersonation can appear through fake contacts, fake documents, clone entities and misleading official-looking claims [OFF-05; OFF-13].

F4 covers urgency and fear. Scam messages often demand immediate action, threatening loss, account blocking, arrest, deadline expiry or missed opportunity. PMT helps explain why fear must be paired with coping steps; otherwise fear can lead to panic compliance rather than protection [ACA-06].

F5 covers emotional grooming, shame and recovery vulnerability. Fraud victimization can create distress, shame, self-blame and delayed disclosure [ACA-04; ACA-08]. This matters because a person who delays reporting or feels isolated may be more vulnerable to fake support, recovery-fee requests or renewed manipulation.

F6 covers financial need and opportunity pressure. Investment scams and job scams often use reward framing, task payments, unrealistic returns, fees, taxes or urgent payment steps. SC and PDRM sources provide practical examples of these cues [OFF-05; OFF-13].

F7 covers protective self-efficacy and reporting capability. Knowing that scams exist is not enough if a person does not know which channel to use. The report therefore includes NSRC, Semak Mule, Cyber999, SC Investment Checker, bank hotlines and PDRM reporting as practical response channels [OFF-06; OFF-07; OFF-14; OFF-18].

![Figure 2.4: Verification and reporting capability for cyber fraud prevention.]({FIG8})

## 2.7 Prevention and Intervention Literature

Prevention literature suggests that phishing and scam mitigation cannot depend only on one method. Naqvi et al. (2023) classify mitigation strategies across technical and human-centred approaches and argue that human users must be considered in mitigation design [ACA-10]. The FTC scam-prevention messaging review also supports careful message design and warns against assuming that awareness messages automatically change behaviour [ACA-07].

For this report, the practical implication is direct: the intervention should include scenario practice, safe response routines, independent verification and reporting confidence. The module should not only tell people what scams are. It should help them practise what to do when pressure is present.

## 2.8 Literature Gap

The reviewed evidence supports the need for a module that connects scam types, behavioural factors, theory and practical tools. Existing public warnings are valuable, but the research gap lies in how the public appraises scam situations under pressure, how prior victims recover safely, and how reporting and verification skills can be measured. This report addresses that gap through a seven-factor framework, questionnaire constructs, scenario tasks and module design.

## 2.9 Chapter Summary

This chapter reviewed the Malaysian cyber fraud context, scam techniques, behavioural theories and seven-factor framework. It established the evidence base for the methodology and intervention design developed in the next chapters.

[[PAGE_BREAK]]

# CHAPTER 3: RESEARCH METHODOLOGY

## 3.1 Introduction

This chapter explains the proposed methodology. Because no primary survey or intervention dataset is currently available, the methodology is written as a complete research design that can be used for later data collection and analysis.

## 3.2 Research Design

The study uses a quantitative design supported by scenario-based assessment and a proposed pre-test/post-test intervention evaluation. The quantitative survey measures the seven factors and theory constructs. The scenario assessment measures practical scam cue detection and response choice. The intervention evaluation measures whether the module improves safe response outcomes after training.

The current final report includes official secondary analysis only. Primary survey findings, factor analysis, regression results and intervention effectiveness claims must be inserted only after real data collection.

## 3.3 Respondent Groups

The study should separate respondents into groups instead of treating the public as one uniform category.

| Respondent group | Definition | Reason for inclusion |
|---|---|---|
| Prior victims | Respondents who previously lost money, data or access because of a scam | Needed to study post-victim behaviour and recovery vulnerability |
| Repeat victims | Respondents with more than one confirmed victimization or repeated risky compliance | Central group for revictimization analysis |
| Attempted-scam exposed non-victims | Respondents who received scam attempts but avoided loss | Useful comparison group for protective behaviour |
| No known exposure | Respondents with no clear scam exposure | Baseline comparison for awareness and tool-use capability |

## 3.4 Sampling Strategy

Purposive and convenience sampling are suitable for the first empirical phase. Purposive sampling is needed because the study requires prior victims and attempted-scam exposed respondents. Convenience sampling can be used through university networks, public online channels, community groups and professional contacts. If the number of repeat victims is small, analysis for that subgroup should remain descriptive or exploratory.

The survey must avoid collecting sensitive financial information. Respondents should not be asked to provide account numbers, identity card numbers, passwords, screenshots containing personal data or scammer contact details that could expose them to risk.

## 3.5 Variables and Constructs

The independent constructs are the seven revictimization factors. The theory constructs include attitude, subjective norm, perceived behavioural control, threat appraisal, coping appraisal, self-efficacy and emotional appraisal. The outcome constructs include protective intention, safe scenario response, tool-use capability, reporting intention, recovery-scam resistance and revictimization tendency.

| Construct group | Example variables | Linked factors |
|---|---|---|
| Awareness and confidence | scam cue recognition, overconfidence, familiar-message trust | F1 |
| Social and authority pressure | group influence, fake endorsement, official-sounding pressure | F2, F3 |
| Emotional and urgency response | fear, shame, panic, delayed disclosure | F4, F5 |
| Financial pressure | opportunity pressure, unrealistic-return tolerance, task-fee acceptance | F6 |
| Protective capability | verification skill, reporting channel selection, refusal confidence | F7 |

## 3.6 Questionnaire Design

The questionnaire should use Likert-scale items, multiple-choice tool-use questions and scenario tasks. The Likert scale can use five points from strongly disagree to strongly agree. Items should be written in plain language and avoid blaming victims.

Example item areas are listed in Appendix A. The final survey should be piloted with a small group to check clarity, sensitivity and response time before wider distribution.

## 3.7 Scenario Design and Scoring

Scenario tasks are important because scams are contextual. A respondent may answer awareness questions correctly but still choose unsafe action in a realistic scenario. Each scenario should present a short scam-like situation and ask the respondent to choose a response.

Scoring should classify responses into three levels: safe, partially safe and risky. A safe response involves pausing, refusing unsafe requests, independently verifying and reporting through the correct channel. A partially safe response shows some caution but misses an important step. A risky response involves clicking, paying, installing, sharing credentials, continuing communication or delaying help when immediate reporting is needed.

## 3.8 Data Collection and Ethics

Participants should receive an information sheet explaining the study purpose, voluntary participation, anonymity, sensitive-topic nature and right to withdraw. The survey should avoid collecting unnecessary personal identifiers. If a respondent reports current scam harm, the survey should provide reporting guidance such as NSRC 997, bank hotline, PDRM, Semak Mule, Cyber999 and SC Investment Checker, depending on the situation.

## 3.9 Analysis Method

Descriptive analysis should summarize respondent profile, prior exposure, scam-type exposure, reporting behaviour and tool familiarity. Reliability can be assessed using Cronbach's alpha where constructs have multiple items. Relationship testing can use regression or PLS-SEM depending on final sample size and data quality. Scenario scores can be compared across respondent groups to examine whether prior victims, attempted-scam exposed non-victims and low-exposure respondents respond differently.

## 3.10 Chapter Summary

This chapter presented a complete methodology for later empirical testing. It defined respondent groups, constructs, questionnaire design, scenario scoring, ethics and analysis methods. The next chapter translates the framework into intervention modules.

[[PAGE_BREAK]]

# CHAPTER 4: RESEARCH DESIGN AND INTERVENTION MODULE

## 4.1 Introduction

This chapter presents the proposed intervention module framework. The module is designed to help the public move from awareness to practical protective action. It is not presented as a completed deployed application or proven intervention because no module-testing dataset is available.

## 4.2 Module Design Principles

The module follows five design principles. First, it must be non-blaming because shame and self-blame can delay reporting. Second, it must be practical because users need to know what to do under pressure. Third, it must be local enough to include Malaysian reporting and verification channels. Fourth, it must be scenario-based because scam decisions happen in context. Fifth, it must be measurable so that later evaluation can test improvement.

## 4.3 Module Structure

| Module | Focus | Factor mapping | Example outcome |
|---|---|---|---|
| Module 1 | Scam awareness and familiar-message risk | F1 | Recognize common scam cues without overconfidence |
| Module 2 | Social proof, trust transfer and authority cues | F2, F3 | Verify group claims, official-sounding requests and clone entities |
| Module 3 | Urgency, fear and coping appraisal | F4 | Pause before action and refuse rushed instructions |
| Module 4 | Verification and reporting routines | F7 | Match the right tool to the right situation |
| Module 5 | Recovery support and revictimization resistance | F5, F6, F7 | Seek help safely and avoid recovery-fee scams |

![Figure 4.1: Suggested conceptual flow for the seven-factor revictimization model.]({FIG9})

## 4.4 Verification and Reporting Routine

The reporting routine should teach users to choose channels based on the situation. If money has just been transferred, fast contact with the bank and NSRC 997 is important. If an account, phone number or company name is suspicious, Semak Mule can support checking. If the issue involves investment offers or licensed entities, SC Investment Checker and Investor Alert materials are relevant. If the issue is a cyber incident such as phishing, compromised access or malicious application activity, Cyber999/MyCERT can be used. PDRM reporting remains important for crime records and investigation.

![Figure 4.2: Malaysia scam response tool map. Source: OFF-06, OFF-07, OFF-14, OFF-18.]({CHART_TOOLS})

## 4.5 Use of Official Proofs

The module should use selected live-source screenshots only as supporting evidence. The screenshots must not replace references or be treated as datasets.

![Figure 4.3: SC investor guidance showing investment scam warning signs. Source: OFF-13, proof2.]({PROOF2})

![Figure 4.4: SC clone-firm scam evidence supporting authority impersonation and fake credibility discussion. Source: proof3.]({PROOF3})

![Figure 4.5: Semak Mule verification evidence supporting practical checking routines. Source: proof5.]({PROOF5})

![Figure 4.6: Fake NSRC account warning supporting recovery-scam and fake support-channel risk. Source: proof6.]({PROOF6})

## 4.6 Evaluation Framework

The module should be evaluated through pre-test/post-test measurement. The pre-test measures baseline awareness, scenario response, self-efficacy and tool-use capability. The post-test measures immediate improvement after module exposure. A delayed follow-up after two to four weeks is recommended if possible. If a comparison group is not available, the design should be described as pre-experimental and its limitations should be stated.

Outcome measures should include scam cue detection, safe response selection, reporting-channel matching, refusal confidence, recovery-scam resistance, reporting intention and help-seeking confidence. Effectiveness must not be claimed until real intervention data exists.

## 4.7 Chapter Summary

This chapter developed the intervention module framework and linked it to the seven-factor backbone. It also defined how official tools, proof screenshots and evaluation outcomes should be used. The next chapter presents official secondary analysis and data-honest discussion.

[[PAGE_BREAK]]

# CHAPTER 5: RESULTS, ANALYSIS AND DISCUSSION

## 5.1 Introduction

This chapter presents descriptive secondary-source analysis. It does not present survey findings, factor-analysis output, model testing or intervention effectiveness because no primary dataset is available. The purpose of this chapter is to show what can be concluded from official sources and what must wait for future empirical data.

## 5.2 Secondary Data Sources

The secondary analysis uses Cyber999/MyCERT incident reports, PDRM public scam warnings, SC investor guidance, official reporting-tool pages and open-access academic sources. The analysis keeps measurement families separate. Cyber999 incident counts are not the same as PDRM police cases. PDRM case/loss indicators are not the same as BNM banking response indicators. SC alert guidance is not a national prevalence dataset.

## 5.3 Cyber999 Trend Analysis

The cleaned Cyber999 dataset shows that fraud remained a large share of handled incident reports. Fraud incidents rose from 1,126 in Q1 2025 to 1,633 in Q2 2025, then remained high at 1,521 in Q3 2025. Q4 2025 currently has a partial extracted fraud value of 1,471 but lacks complete verified table fields in the local dataset, so it is not used as a full-quarter comparison.

| Period | Total incidents | Fraud incidents | Stated fraud share | Computed fraud share |
|---|---:|---:|---:|---:|
| 2024 Q2 | 1,481 | 947 | 63.94% | 63.94% |
| 2024 Q4 | 1,550 | 1,108 | 71% | 71.48% |
| 2025 Q1 | 1,657 | 1,126 | 68% | 67.95% |
| 2025 Q2 | 2,058 | 1,633 | 80% | 79.35% |
| 2025 Q3 | 2,020 | 1,521 | 75% | 75.30% |

The trend supports the relevance of cyber fraud prevention, but it does not prove revictimization by itself. Cyber999 data measures handled reports, not repeated victimization at the individual level. Therefore, it supports the problem context while the revictimization construct still requires primary data.

## 5.4 Fraud Category Analysis

Q2 2025 Cyber999 data shows phishing and impersonation/spoofing as high-count categories within fraud. This aligns with the report's focus on awareness gaps, authority impersonation, urgency and tool-use capability. It also supports scenario design because respondents should practise identifying suspicious links, fake contact, false authority and urgent instructions.

## 5.5 Seven-Factor Evidence Coverage

The evidence matrix maps official and academic sources to the seven-factor backbone. The strongest coverage is for awareness, authority impersonation, urgency/fear and protective self-efficacy. Emotional recovery and financial pressure are supported but should be strengthened further through primary data, especially from prior victims or attempted-scam exposed respondents.

![Figure 5.1: Evidence coverage by seven-factor backbone.]({CHART_COVERAGE})

## 5.6 Discussion

The secondary evidence supports the report's main argument that cyber fraud prevention must be practical and behavioural. Official sources show active scam warnings, fraud incident reports and verification tools. Academic literature shows that social influence, overconfidence, emotional harm and human-centred mitigation matter. The combined evidence supports a module framework that teaches cue detection, calm appraisal, independent verification and safe reporting.

At the same time, the secondary evidence cannot answer all research questions. It cannot show which factor is the strongest predictor among the Malaysian public. It cannot show whether prior victims respond differently from non-victims. It cannot prove that the proposed module improves behaviour. Those claims require survey and intervention data.

## 5.7 Chapter Summary

This chapter presented official secondary analysis and discussion boundaries. It showed that cyber fraud is a strong and current problem area, but it avoided unsupported empirical claims. The final chapter concludes the report and explains the next steps for proper empirical validation.

[[PAGE_BREAK]]

# CHAPTER 6: CONCLUSION AND FUTURE WORK

## 6.1 Introduction

This chapter concludes the report. It summarizes the study contribution, explains objective achievement, states limitations and identifies future work.

## 6.2 Achievement of Objectives

The first objective was to define cyber fraud revictimization as a measurable behavioural and protection problem. This was achieved by separating repeated victimization, repeated risky compliance, recovery-scam targeting, delayed reporting and low protective capability.

The second objective was to identify factors that contribute to revictimization tendency. This was achieved through the seven-factor backbone supported by official and academic evidence.

The third objective was to develop a theory-based framework. This was achieved by integrating TPB, PMT and Cognitive Appraisal Theory with the seven factors.

The fourth objective was to design intervention modules. This was achieved through the five-module framework covering awareness, cue detection, coping appraisal, verification, reporting and recovery support.

The fifth objective was to prepare a data-honest analysis framework. This was achieved by including official secondary analysis and clearly separating it from future primary survey or intervention results.

## 6.3 Contribution

The main contribution is a structured, evidence-backed framework for studying and preventing cyber fraud revictimization among the public. The report turns scattered scam warnings and behavioural ideas into a measurable model, questionnaire plan, scenario scoring method and module framework.

The report also contributes by protecting research honesty. It avoids invented findings, separates incompatible statistics and provides appendices that can support later data collection.

## 6.4 Limitations

The main limitation is the absence of primary survey and intervention data. As a result, the report cannot claim factor strength, causal relationships or module effectiveness. Another limitation is that some official BNM sources were blocked during automated local archiving, although their public URLs remain identified for manual verification. A further limitation is that revictimization is sensitive, and prior victims may be difficult to recruit.

## 6.5 Future Work

Future work should collect primary survey data with enough prior-victim and attempted-scam exposed respondents. The questionnaire should be piloted first, then improved for clarity and sensitivity. The intervention module should be tested using pre-test/post-test measurement and, if possible, delayed follow-up. A comparison group would strengthen the evaluation.

Future work should also improve the secondary dataset by extracting complete Q4 2025 Cyber999 values and adding any later official reports. BNM sources should be manually archived through a browser for local record completeness.

## 6.6 Final Conclusion

Cyber fraud revictimization cannot be treated only as a lack of awareness. It is shaped by trust, pressure, fear, shame, opportunity, authority cues and practical ability to verify and report. A useful prevention approach must therefore help people recognize cues, pause under pressure, verify independently, report quickly and recover without blame. This report provides a complete evidence-based framework for that purpose while keeping the analysis honest about what has and has not yet been empirically tested.

[[PAGE_BREAK]]

# References

Ajzen, I. (1991). The theory of planned behavior. *Organizational Behavior and Human Decision Processes, 50*(2), 179-211.

Bank Negara Malaysia. (2024). *National Fraud Portal to solidify coordinated efforts in curbing financial scams*. https://www.bnm.gov.my/-/nfp-launch

Bank Negara Malaysia. (2025). *Governor's opening remarks at the 15th International Conference on Financial Crime and Terrorism Financing*. https://www.bnm.gov.my/-/spch-g-ifctf25

Bank Negara Malaysia. (2026). *Annual Report 2025*. https://www.bnm.gov.my/documents/20124/21185005/ar2025_en_book.pdf

Balakrishnan, V., Ahhmed, S., & Basheer, A. (2025). Personal, environmental and behavioral predictors associated with online fraud victimization among adults. *PLOS ONE, 20*(1), e0317232. https://doi.org/10.1371/journal.pone.0317232

CyberSecurity Malaysia. (2024). *Cyber Incident Quarterly Summary Report Q2 2024*. https://www.cybersecurity.my/portal-main/advisories-details/47317289-8a00-11ef-b9ea-005056812d51

Federal Trade Commission. (2022). *A review of scam prevention messaging research*. https://consumer.ftc.gov/system/files/consumer_ftc_gov/pdf/A%20Review%20of%20Scam%20Prevention%20Messaging%20Research.pdf

MyCERT. (2025). *Cyber Incident Quarterly Summary Report Q4 2024*. https://www.mycert.org.my/portal/advisory?id=SR-029.022025

MyCERT. (2025). *Cyber Incident Quarterly Summary Report Q1 2025*. https://www.mycert.org.my/portal/advisory?id=SR-030.062025

MyCERT. (2025). *Cyber Incident Quarterly Summary Report Q2 2025*. https://www.mycert.org.my/portal/advisory?id=SR-031.082025

MyCERT. (2026). *Cyber Incident Quarterly Summary Report Q3 2025*. https://www.mycert.org.my/portal/advisory?id=SR-032.012026

MyCERT. (2026). *Cyber Incident Quarterly Summary Report Q4 2025*. https://www.mycert.org.my/portal/advisory?id=SR-033.042026

Naqvi, B., Perova, K., Farooq, A., Makhdoom, I., Oyedeji, S., & Porras, J. (2023). Mitigation strategies against the phishing attacks: A systematic literature review. *Computers & Security, 132*, 103387. https://doi.org/10.1016/j.cose.2023.103387

National Anti-Financial Crime Centre. (n.d.). *National Scam Response Centre*. https://nfcc.jpm.gov.my/index.php/en/about-nsrc

Royal Malaysia Police. (n.d.). *Semak Mule*. https://semakmule.rmp.gov.my/

Royal Malaysia Police. (2026). *Scam Alert*. https://www.rmp.gov.my/scam-alert

Rogers, R. W. (1975). A protection motivation theory of fear appeals and attitude change. *Journal of Psychology, 91*(1), 93-114.

Rogers, R. W. (1983). Cognitive and physiological processes in fear appeals and attitude change: A revised theory of protection motivation.

Securities Commission Malaysia. (n.d.). *Beware of scams*. https://www.sc.com.my/investor-empowerment/scam

Securities Commission Malaysia. (n.d.). *Investment Checker*. https://www.sc.com.my/investment-checker

Securities Commission Malaysia. (n.d.). *Investor Alert Updates*. https://www.sc.com.my/resources/media/investor-alert-updates

Whitty, M. T. (2025). A systematic literature review of profiling victims of cyber scam. *Cogent Social Sciences*. https://doi.org/10.1080/23311886.2025.2563781

[[PAGE_BREAK]]

# Appendix A: Questionnaire Draft

## A.1 Screening Questions

1. Have you ever received a suspicious online message, call, investment offer, job offer or payment request?
2. Have you ever lost money, data or account access because of a scam?
3. Have you ever experienced more than one scam incident or repeated scam contact after an earlier incident?
4. Did you report the incident or attempt to verify it through any official or trusted channel?

## A.2 Likert-Scale Constructs

| Construct | Example item |
|---|---|
| Awareness gap | I can usually identify suspicious links or payment requests before acting. |
| Social influence | I may trust an offer more if many people in a group appear to support it. |
| Authority impersonation | I know how to verify an official-sounding call or message independently. |
| Urgency and fear | I can pause and check even when a message says immediate action is required. |
| Emotional recovery | I would seek help after a scam without feeling too ashamed to report. |
| Financial pressure | I can reject offers that promise high returns with little or no risk. |
| Protective self-efficacy | I know which reporting or checking channel to use for different scam situations. |

## A.3 Tool-Use Questions

Respondents should match the scenario to the most suitable action: bank hotline, NSRC 997, Semak Mule, Cyber999, SC Investment Checker, PDRM report or platform reporting.

[[PAGE_BREAK]]

# Appendix B: Scenario Tasks

| Scenario | Main cue | Safe response |
|---|---|---|
| A message says a bank account will be blocked unless a link is opened immediately | urgency, phishing, authority cue | do not click; contact bank through official channel |
| An online investment group shows repeated profit testimonials and asks for transfer to a personal account | social proof, financial pressure, unrelated account | verify through SC tools; do not transfer |
| A caller claims to be from an enforcement agency and demands immediate payment | authority impersonation, fear | end call; verify independently; report if needed |
| A victim receives a message claiming money can be recovered after paying a processing fee | recovery scam, shame, financial pressure | do not pay; seek official support/reporting |
| A job offer requires task payments before salary can be withdrawn | job scam, reward pressure | refuse payment; save evidence; report/check |

# Appendix C: Scoring Rubric

| Score | Meaning | Example response |
|---|---|---|
| 2 | Safe | pauses, refuses unsafe request, verifies independently and reports through correct channel |
| 1 | Partially safe | recognizes risk but misses reporting or uses an incomplete checking step |
| 0 | Risky | clicks, pays, installs, shares credentials, continues contact or delays urgent reporting |

# Appendix D: Source and Evidence Package

The source library contains official reports, academic papers, source notes, raw datasets, cleaned datasets, analysis outputs and the evidence matrix. The main working files are:

- `source_library/source_inventory.md`
- `source_library/manual_followup_sources.md`
- `source_library/source_notes/`
- `source_library/datasets_raw/`
- `source_library/datasets_clean/`
- `source_library/analysis_outputs/`
- `evidence_and_references/evidence_matrix_v2.md`

BNM source files remain listed for manual browser saving because automated requests returned protected empty responses. The final report avoids using unverified BNM-specific numerical claims as core analysis values.
"""


def xml_escape(text: str) -> str:
    return escape(text, {"'": "&apos;", '"': "&quot;"})


def emu(inches: float) -> int:
    return int(inches * 914400)


def image_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")
    if data[:5].lower().startswith(b"<svg") or b"<svg" in data[:300].lower():
        text = data[:1000].decode("utf-8", errors="ignore")
        w = re.search(r'width="([0-9.]+)', text)
        h = re.search(r'height="([0-9.]+)', text)
        return int(float(w.group(1))) if w else 980, int(float(h.group(1))) if h else 560
    return 1200, 800


def rpr(size=24, bold=False, italic=False):
    parts = [
        "<w:rPr>",
        '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>',
        f'<w:sz w:val="{size}"/>',
        f'<w:szCs w:val="{size}"/>',
    ]
    if bold:
        parts.append("<w:b/><w:bCs/>")
    if italic:
        parts.append("<w:i/><w:iCs/>")
    parts.append("</w:rPr>")
    return "".join(parts)


def ppr(style=None, align=None, before=0, after=120, line=360, first_line=False,
        keep_next=False, keep_lines=False, page_break_before=False, left=0, hanging=0):
    parts = ["<w:pPr>"]
    if style:
        parts.append(f'<w:pStyle w:val="{style}"/>')
    if keep_next:
        parts.append("<w:keepNext/>")
    if keep_lines:
        parts.append("<w:keepLines/>")
    if page_break_before:
        parts.append("<w:pageBreakBefore/>")
    if align:
        parts.append(f'<w:jc w:val="{align}"/>')
    parts.append(f'<w:spacing w:before="{before}" w:after="{after}" w:line="{line}" w:lineRule="auto"/>')
    if first_line:
        parts.append('<w:ind w:firstLine="720"/>')
    elif left or hanging:
        hang = f' w:hanging="{hanging}"' if hanging else ""
        parts.append(f'<w:ind w:left="{left}"{hang}/>')
    parts.append("</w:pPr>")
    return "".join(parts)


def parse_inline(text: str, size=24):
    runs = []
    pattern = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)")
    pos = 0
    for match in pattern.finditer(text):
        if match.start() > pos:
            runs.append((text[pos:match.start()], False, False))
        token = match.group(0)
        if token.startswith("**"):
            runs.append((token[2:-2], True, False))
        elif token.startswith("*"):
            runs.append((token[1:-1], False, True))
        else:
            runs.append((token[1:-1], False, False))
        pos = match.end()
    if pos < len(text):
        runs.append((text[pos:], False, False))
    return "".join(
        f'<w:r>{rpr(size, bold, italic)}<w:t xml:space="preserve">{xml_escape(t)}</w:t></w:r>'
        for t, bold, italic in runs
        if t
    )


def paragraph(text="", style=None, align=None, before=0, after=120, line=360,
              first_line=False, keep_next=False, keep_lines=False, bold=False,
              italic=False, size=24, left=0, hanging=0, page_break_before=False):
    runs = (
        f'<w:r>{rpr(size, bold, italic)}<w:t xml:space="preserve">{xml_escape(text)}</w:t></w:r>'
        if bold or italic
        else parse_inline(text, size)
    )
    return (
        "<w:p>"
        + ppr(style, align, before, after, line, first_line, keep_next, keep_lines, page_break_before, left, hanging)
        + runs
        + "</w:p>"
    )


def page_break():
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


def toc_field():
    entries = [
        ("Abstract", 2, 1),
        ("CHAPTER 1: INTRODUCTION", 4, 1),
        ("1.1 Introduction", 4, 2),
        ("1.2 Problem Background", 4, 2),
        ("1.3 Research Gap", 5, 2),
        ("1.4 Research Aim", 5, 2),
        ("1.5 Research Questions", 5, 2),
        ("1.6 Research Objectives", 5, 2),
        ("1.7 Research Scope", 6, 2),
        ("1.8 Research Contribution", 6, 2),
        ("1.9 Chapter Summary", 6, 2),
        ("CHAPTER 2: LITERATURE REVIEW", 7, 1),
        ("CHAPTER 3: RESEARCH METHODOLOGY", 13, 1),
        ("CHAPTER 4: RESEARCH DESIGN AND INTERVENTION MODULE", 16, 1),
        ("CHAPTER 5: RESULTS, ANALYSIS AND DISCUSSION", 23, 1),
        ("CHAPTER 6: CONCLUSION AND FUTURE WORK", 26, 1),
        ("References", 28, 1),
        ("Appendix A: Questionnaire Draft", 30, 1),
        ("Appendix B: Scenario Tasks", 31, 1),
        ("Appendix C: Scoring Rubric", 31, 1),
        ("Appendix D: Source and Evidence Package", 31, 1),
    ]
    parts = [
        '<w:p><w:r><w:fldChar w:fldCharType="begin"/></w:r>'
        '<w:r><w:instrText xml:space="preserve"> TOC \\o "1-3" \\h \\z \\u </w:instrText></w:r>'
        '<w:r><w:fldChar w:fldCharType="separate"/></w:r></w:p>'
    ]
    for title, page, level in entries:
        indent = 0 if level == 1 else 360
        size = 22 if level == 1 else 20
        bold = level == 1
        parts.append(
            "<w:p>"
            + ppr(before=0, after=55, line=276, left=indent)
            + f'<w:r>{rpr(size, bold)}<w:t xml:space="preserve">{xml_escape(title)}</w:t></w:r>'
            + f'<w:r>{rpr(size)}<w:tab/><w:t>{page}</w:t></w:r>'
            + "</w:p>"
        )
    parts.append('<w:p><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>')
    return "".join(parts)


def table_xml(rows: list[list[str]]):
    if not rows:
        return ""
    cols = max(len(r) for r in rows)
    width = int(9000 / cols)
    parts = [
        '<w:tbl><w:tblPr><w:tblStyle w:val="TableGrid"/><w:tblW w:w="9000" w:type="dxa"/>'
        '<w:tblBorders><w:top w:val="single" w:sz="4" w:color="666666"/>'
        '<w:left w:val="single" w:sz="4" w:color="666666"/>'
        '<w:bottom w:val="single" w:sz="4" w:color="666666"/>'
        '<w:right w:val="single" w:sz="4" w:color="666666"/>'
        '<w:insideH w:val="single" w:sz="4" w:color="999999"/>'
        '<w:insideV w:val="single" w:sz="4" w:color="999999"/></w:tblBorders>'
        '<w:tblCellMar><w:top w:w="100" w:type="dxa"/><w:left w:w="120" w:type="dxa"/>'
        '<w:bottom w:w="100" w:type="dxa"/><w:right w:w="120" w:type="dxa"/></w:tblCellMar></w:tblPr>',
        "<w:tblGrid>" + "".join(f'<w:gridCol w:w="{width}"/>' for _ in range(cols)) + "</w:tblGrid>",
    ]
    for ridx, row in enumerate(rows):
        parts.append("<w:tr>")
        for cell in row + [""] * (cols - len(row)):
            shade = '<w:shd w:fill="D9EAF7"/>' if ridx == 0 else ""
            bold = ridx == 0
            parts.append(
                f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{shade}</w:tcPr>'
                + paragraph(cell.strip(), before=0, after=0, line=276, size=20, bold=bold)
                + "</w:tc>"
            )
        parts.append("</w:tr>")
    parts.append("</w:tbl>")
    return "".join(parts) + paragraph("", after=120)


def image_paragraph(rel_id: str, name: str, width_px: int, height_px: int, max_width=5.8, max_height=6.8):
    ratio = height_px / max(width_px, 1)
    width = max_width
    height = width * ratio
    if height > max_height:
        height = max_height
        width = height / ratio
    cx = emu(width)
    cy = emu(height)
    safe_name = xml_escape(name)
    return f"""
<w:p>
  {ppr(align="center", before=160, after=80, line=240, keep_next=True, keep_lines=True)}
  <w:r>
    {rpr(22)}
    <w:drawing>
      <wp:inline xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" distT="0" distB="0" distL="0" distR="0">
        <wp:extent cx="{cx}" cy="{cy}"/>
        <wp:docPr id="1" name="{safe_name}"/>
        <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
          <a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
            <pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
              <pic:nvPicPr><pic:cNvPr id="0" name="{safe_name}"/><pic:cNvPicPr/></pic:nvPicPr>
              <pic:blipFill><a:blip r:embed="{rel_id}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>
              <pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>
            </pic:pic>
          </a:graphicData>
        </a:graphic>
      </wp:inline>
    </w:drawing>
  </w:r>
</w:p>
"""


def parse_markdown(md: str):
    lines = md.splitlines()
    body = []
    image_paths: list[Path] = []
    image_map: dict[Path, str] = {}
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line:
            i += 1
            continue
        if line == "[[PAGE_BREAK]]":
            body.append(page_break())
            i += 1
            continue
        if line == "[[TOC]]":
            body.append(toc_field())
            i += 1
            continue
        img = re.match(r"!\[(.*?)\]\((.*?)\)", line)
        if img:
            caption, link = img.groups()
            path = (ACTIVE_DIR / link).resolve()
            if path.exists():
                if path not in image_map:
                    image_map[path] = f"rImg{len(image_map) + 1}"
                    image_paths.append(path)
                w, h = image_size(path)
                body.append(image_paragraph(image_map[path], path.name, w, h))
                body.append(paragraph(caption, style="Caption", align="center", size=20, italic=True, before=0, after=180, line=276, keep_lines=True))
            else:
                body.append(paragraph(f"[Missing image: {caption}]", italic=True))
            i += 1
            continue
        if line.startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            rows = []
            for tline in table_lines:
                cells = [c.strip() for c in tline.strip("|").split("|")]
                if all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells):
                    continue
                rows.append(cells)
            body.append(table_xml(rows))
            continue
        if line.startswith("# "):
            title = line[2:].strip()
            if title.startswith("CHAPTER"):
                body.append(paragraph(title, style="Heading1", align="center", bold=True, size=28, before=0, after=240, line=360, keep_next=True, page_break_before=False))
            elif title.startswith("Appendix") or title == "References":
                body.append(paragraph(title, style="Heading1", bold=True, size=26, before=240, after=180, keep_next=True))
            else:
                body.append(paragraph(title, style="Title", align="center", bold=True, size=30, before=240, after=240, line=360, keep_next=True))
            i += 1
            continue
        if line.startswith("## "):
            body.append(paragraph(line[3:].strip(), style="Heading2", bold=True, size=24, before=180, after=120, keep_next=True))
            i += 1
            continue
        if line.startswith("### "):
            body.append(paragraph(line[4:].strip(), style="Heading3", bold=True, size=23, before=120, after=80, keep_next=True))
            i += 1
            continue
        if re.match(r"^\d+\. ", line):
            body.append(paragraph(line, size=24, left=720, hanging=360, before=0, after=80))
            i += 1
            continue
        if line.startswith("- "):
            body.append(paragraph(line[2:].strip(), size=24, left=720, hanging=360, before=0, after=80))
            i += 1
            continue

        para_lines = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|!\[|\||\[\[PAGE_BREAK\]\]|\[\[TOC\]\]|\d+\. |- )", lines[i].strip()):
            para_lines.append(lines[i].strip())
            i += 1
        text = " ".join(para_lines)
        if text.startswith("**") and text.endswith("**") and len(text) < 160:
            body.append(paragraph(text.strip("*"), align="center", bold=True, size=24, before=80, after=80, keep_next=True))
        else:
            body.append(paragraph(text, first_line=True, size=24, before=0, after=120, line=360, keep_lines=True))
    return body, image_paths, image_map


def get_template_part(name: str) -> bytes:
    with zipfile.ZipFile(TEMPLATE, "r") as z:
        return z.read(name)


def get_template_sectpr() -> str:
    xml = get_template_part("word/document.xml").decode("utf-8", errors="ignore")
    matches = re.findall(r"<w:sectPr[\\s\\S]*?</w:sectPr>", xml)
    if matches:
        return matches[-1]
    return '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/></w:sectPr>'


def document_xml(body_parts: list[str]) -> str:
    sect = get_template_sectpr()
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{W_NS}" xmlns:r="{R_NS}" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
  <w:body>
    {''.join(body_parts)}
    {sect}
  </w:body>
</w:document>"""


def add_content_type_defaults(content: str, image_paths: list[Path]) -> str:
    additions = {
        ".png": '<Default Extension="png" ContentType="image/png"/>',
        ".jpg": '<Default Extension="jpg" ContentType="image/jpeg"/>',
        ".jpeg": '<Default Extension="jpeg" ContentType="image/jpeg"/>',
        ".svg": '<Default Extension="svg" ContentType="image/svg+xml"/>',
    }
    for suffix, default in additions.items():
        if any(p.suffix.lower() == suffix for p in image_paths) and f'Extension="{suffix[1:]}"' not in content:
            content = content.replace("</Types>", f"  {default}\n</Types>")
    return content


def update_settings(settings: str) -> str:
    if "<w:updateFields" not in settings:
        settings = settings.replace("</w:settings>", '<w:updateFields w:val="true"/></w:settings>')
    return settings


def update_rels(rels: str, image_paths: list[Path], image_map: dict[Path, str]) -> str:
    existing = [int(m.group(1)) for m in re.finditer(r'Id="rId(\\d+)"', rels)]
    next_id = max(existing, default=50) + 50
    for path in image_paths:
        rid = image_map[path]
        media_name = f"media/{path.stem}_{len(rid)}{path.suffix.lower()}"
        image_map[path] = (rid, media_name)  # type: ignore[assignment]
        rels = rels.replace(
            "</Relationships>",
            f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="{media_name}"/></Relationships>',
        )
        next_id += 1
    return rels


def build_docx(md: str) -> None:
    body, image_paths, image_map = parse_markdown(md)
    FINAL_DIR.mkdir(parents=True, exist_ok=True)
    if FINAL_DOCX.exists():
        FINAL_DOCX.unlink()

    original_rels = get_template_part("word/_rels/document.xml.rels").decode("utf-8", errors="ignore")
    rels_for_images = original_rels
    media_targets: dict[Path, str] = {}
    for idx, path in enumerate(image_paths, start=1):
        rid = image_map[path]
        media_name = f"media/final_cyber_{idx}{path.suffix.lower()}"
        media_targets[path] = media_name
        rels_for_images = rels_for_images.replace(
            "</Relationships>",
            f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="{media_name}"/></Relationships>',
        )

    with zipfile.ZipFile(TEMPLATE, "r") as zin, zipfile.ZipFile(FINAL_DOCX, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.filename in {"word/document.xml", "word/_rels/document.xml.rels"}:
                continue
            data = zin.read(item.filename)
            if item.filename == "[Content_Types].xml":
                data = add_content_type_defaults(data.decode("utf-8", errors="ignore"), image_paths).encode("utf-8")
            if item.filename == "word/settings.xml":
                data = update_settings(data.decode("utf-8", errors="ignore")).encode("utf-8")
            zout.writestr(item, data)
        zout.writestr("word/document.xml", document_xml(body))
        zout.writestr("word/_rels/document.xml.rels", rels_for_images)
        for path, media_name in media_targets.items():
            zout.writestr(f"word/{media_name}", path.read_bytes())


def main() -> None:
    FINAL_DIR.mkdir(parents=True, exist_ok=True)
    FINAL_MD.write_text(REPORT_MD, encoding="utf-8", newline="\n")
    build_docx(REPORT_MD)
    print(FINAL_MD)
    print(FINAL_DOCX)


if __name__ == "__main__":
    main()
