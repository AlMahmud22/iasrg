from __future__ import annotations

import csv
import html
import json
import math
import ssl
import textwrap
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path


WORKING_DIR = Path(__file__).resolve().parents[1]
CYBER_DIR = WORKING_DIR / "03_cyber_fraud_research_report_2026-04_to_2026-06"
LIB_DIR = CYBER_DIR / "source_library"
OFFICIAL_DIR = LIB_DIR / "official_reports"
ACADEMIC_DIR = LIB_DIR / "academic_papers"
NOTES_DIR = LIB_DIR / "source_notes"
RAW_DIR = LIB_DIR / "datasets_raw"
CLEAN_DIR = LIB_DIR / "datasets_clean"
OUTPUT_DIR = LIB_DIR / "analysis_outputs"
EVIDENCE_DIR = CYBER_DIR / "evidence_and_references"


TODAY = date.today().isoformat()


SOURCE_ENTRIES = [
    {
        "id": "OFF-01",
        "title": "Bank Negara Malaysia Annual Report 2025",
        "url": "https://www.bnm.gov.my/documents/20124/21185005/ar2025_en_book.pdf",
        "filename": "OFF-01_bnm_annual_report_2025.pdf",
        "folder": "official",
        "type": "Official annual report",
        "reliability": "High - central bank official publication.",
        "citation": "Bank Negara Malaysia. (2026). Annual Report 2025.",
        "used_for": "National scam-response background, fraud-resolution ecosystem, National Fraud Portal context, and banking-sector response indicators.",
        "chapters": "1, 2, 5, Appendix",
        "factors": "F1, F2, F7",
        "caveats": "Banking-sector indicators should not be merged with Cyber999 incident counts or PDRM police case totals.",
    },
    {
        "id": "OFF-02",
        "title": "Bank Negara Malaysia Fraud Resolution Box 2025",
        "url": "https://bnm.gov.my/publications/ar2025/box4",
        "filename": "OFF-02_bnm_fraud_resolution_box_2025.html",
        "folder": "official",
        "type": "Official web page",
        "reliability": "High - central bank official web publication.",
        "citation": "Bank Negara Malaysia. (2026). Enhancing the financial scam resolution process.",
        "used_for": "Fraud-resolution process, scam impact framing, and institutional response flow.",
        "chapters": "1, 2, 5",
        "factors": "F1, F7",
        "caveats": "The page may use web protection; the PDF annual report is a backup source for the same official context.",
    },
    {
        "id": "OFF-03",
        "title": "Bank Negara Malaysia National Fraud Portal Launch",
        "url": "https://www.bnm.gov.my/-/nfp-launch",
        "filename": "OFF-03_bnm_national_fraud_portal_launch.html",
        "folder": "official",
        "type": "Official media release",
        "reliability": "High - central bank official media release.",
        "citation": "Bank Negara Malaysia. (2024). Launch of the National Fraud Portal.",
        "used_for": "National reporting and bank-coordination flow after scam incidents.",
        "chapters": "1, 2, 4, 5",
        "factors": "F1, F7",
        "caveats": "Use only for process and institutional response, not victim psychology claims.",
    },
    {
        "id": "OFF-04",
        "title": "BNM Governor Speech at IFCTF 2025",
        "url": "https://www.bnm.gov.my/-/spch-g-ifctf25",
        "filename": "OFF-04_bnm_ifctf_2025_speech.html",
        "folder": "official",
        "type": "Official speech",
        "reliability": "High - official speech with national fraud figures quoted.",
        "citation": "Bank Negara Malaysia. (2025). Governor's remarks at IFCTF 2025.",
        "used_for": "Officially quoted PDRM online financial fraud cases and losses for Q1 2025.",
        "chapters": "1, 5",
        "factors": "F1, F6, F7",
        "caveats": "PDRM figures quoted here should be kept separate from Cyber999 incident data.",
    },
    {
        "id": "OFF-05",
        "title": "Royal Malaysia Police Scam Alert",
        "url": "https://www.rmp.gov.my/scam-alert",
        "filename": "OFF-05_pdrm_scam_alert.html",
        "folder": "official",
        "type": "Official warning page",
        "reliability": "High - police public scam-warning page.",
        "citation": "Royal Malaysia Police. (2026). Scam Alert.",
        "used_for": "Current scam warnings, NSRC reminder, job-scam statistics, impersonation and AI voice scam examples.",
        "chapters": "1, 2, 4, 5",
        "factors": "F2, F3, F4, F5, F6, F7",
        "caveats": "The page is a rolling alert page, so screenshots or local copies should be dated.",
    },
    {
        "id": "OFF-06",
        "title": "PDRM Semak Mule Portal",
        "url": "https://semakmule.rmp.gov.my/",
        "filename": "OFF-06_pdrm_semak_mule.html",
        "folder": "official",
        "type": "Official verification portal",
        "reliability": "High - police portal.",
        "citation": "Royal Malaysia Police. (n.d.). Semak Mule.",
        "used_for": "Reporting/checking tool mapping and protective self-efficacy intervention component.",
        "chapters": "2, 4, Appendix",
        "factors": "F1, F7",
        "caveats": "Use for tool workflow, not for national trend statistics unless a dated official statistic is available.",
    },
    {
        "id": "OFF-07",
        "title": "National Scam Response Centre Information",
        "url": "https://nfcc.jpm.gov.my/index.php/en/about-nsrc",
        "filename": "OFF-07_nfcc_nsrc_information.html",
        "folder": "official",
        "type": "Official agency information page",
        "reliability": "High - official government information page.",
        "citation": "National Anti-Financial Crime Centre. (n.d.). National Scam Response Centre.",
        "used_for": "NSRC 997 reporting flow and victim response mapping.",
        "chapters": "2, 4, Appendix",
        "factors": "F7",
        "caveats": "Operational details may change; check again before final DOCX submission.",
    },
    {
        "id": "OFF-08",
        "title": "MyCERT Cyber999 Q4 2024 Cyber Incident Quarterly Summary",
        "url": "https://www.mycert.org.my/portal/advisory?id=SR-029.022025",
        "filename": "OFF-08_mycert_cyber999_q4_2024.html",
        "folder": "official",
        "type": "Official incident report",
        "reliability": "High - CyberSecurity Malaysia/MyCERT advisory.",
        "citation": "MyCERT. (2025). Cyber Incident Quarterly Summary Report, Q4 2024.",
        "used_for": "Cyber999 incident baseline and fraud-category trend.",
        "chapters": "1, 2, 5",
        "factors": "F1, F3, F4, F7",
        "caveats": "Cyber999 incidents are reports handled by Cyber999, not all national police cases.",
    },
    {
        "id": "OFF-09",
        "title": "MyCERT Cyber999 Q1 2025 Cyber Incident Quarterly Summary",
        "url": "https://www.mycert.org.my/portal/advisory?id=SR-030.062025",
        "filename": "OFF-09_mycert_cyber999_q1_2025.html",
        "folder": "official",
        "type": "Official incident report",
        "reliability": "High - CyberSecurity Malaysia/MyCERT advisory.",
        "citation": "MyCERT. (2025). Cyber Incident Quarterly Summary Report, Q1 2025.",
        "used_for": "Cyber999 incident trend and fraud-category split.",
        "chapters": "1, 2, 5",
        "factors": "F1, F3, F4, F7",
        "caveats": "Do not merge with PDRM case totals.",
    },
    {
        "id": "OFF-10",
        "title": "MyCERT Cyber999 Q2 2025 Cyber Incident Quarterly Summary",
        "url": "https://www.mycert.org.my/portal/advisory?id=SR-031.082025",
        "filename": "OFF-10_mycert_cyber999_q2_2025.html",
        "folder": "official",
        "type": "Official incident report",
        "reliability": "High - CyberSecurity Malaysia/MyCERT advisory.",
        "citation": "MyCERT. (2025). Cyber Incident Quarterly Summary Report, Q2 2025.",
        "used_for": "Fraud share, monthly fraud counts, phishing and impersonation category figures.",
        "chapters": "1, 2, 5",
        "factors": "F1, F3, F4, F7",
        "caveats": "The report itself warns that Cyber999 statistics do not include monetary value or aftermath.",
    },
    {
        "id": "OFF-11",
        "title": "MyCERT Cyber999 Q3 2025 Cyber Incident Quarterly Summary",
        "url": "https://www.mycert.org.my/portal/advisory?id=SR-032.012026",
        "filename": "OFF-11_mycert_cyber999_q3_2025.html",
        "folder": "official",
        "type": "Official incident report",
        "reliability": "High - CyberSecurity Malaysia/MyCERT advisory.",
        "citation": "MyCERT. (2026). Cyber Incident Quarterly Summary Report, Q3 2025.",
        "used_for": "Fraud trend, category figures, and official quotation of PDRM Jan-Nov 2025 online crime figures.",
        "chapters": "1, 2, 5",
        "factors": "F1, F3, F4, F6, F7",
        "caveats": "The PDRM figure is quoted in MyCERT; cite carefully and avoid mixing with Cyber999 totals.",
    },
    {
        "id": "OFF-12",
        "title": "MyCERT Cyber999 Q4 2025 Cyber Incident Quarterly Summary",
        "url": "https://www.mycert.org.my/portal/advisory?id=SR-033.042026",
        "filename": "OFF-12_mycert_cyber999_q4_2025.html",
        "folder": "official",
        "type": "Official incident report",
        "reliability": "High - CyberSecurity Malaysia/MyCERT advisory.",
        "citation": "MyCERT. (2026). Cyber Incident Quarterly Summary Report, Q4 2025.",
        "used_for": "Latest Cyber999 fraud incident point for trend continuation.",
        "chapters": "1, 2, 5",
        "factors": "F1, F3, F4, F7",
        "caveats": "Only extracted fields should be used unless the table is fully verified from the local copy.",
    },
    {
        "id": "OFF-13",
        "title": "Securities Commission Malaysia - Beware of Scams",
        "url": "https://www.sc.com.my/investor-empowerment/scam",
        "filename": "OFF-13_sc_beware_of_scams.html",
        "folder": "official",
        "type": "Official investor guidance page",
        "reliability": "High - securities regulator official guidance.",
        "citation": "Securities Commission Malaysia. (n.d.). Beware of scams.",
        "used_for": "Investment scam characteristics, urgency, fake authority materials, unrelated bank accounts, and verification advice.",
        "chapters": "2, 4, Appendix",
        "factors": "F1, F2, F3, F4, F6, F7",
        "caveats": "The page is guidance, not a statistical dataset.",
    },
    {
        "id": "OFF-14",
        "title": "Securities Commission Malaysia Investment Checker",
        "url": "https://www.sc.com.my/investment-checker",
        "filename": "OFF-14_sc_investment_checker.html",
        "folder": "official",
        "type": "Official verification page",
        "reliability": "High - securities regulator official tool page.",
        "citation": "Securities Commission Malaysia. (n.d.). Investment Checker.",
        "used_for": "Protective self-efficacy tool-use mapping.",
        "chapters": "4, Appendix",
        "factors": "F7",
        "caveats": "Use for tool verification workflow, not prevalence statistics.",
    },
    {
        "id": "OFF-15",
        "title": "Securities Commission Malaysia Investor Alert Updates",
        "url": "https://www.sc.com.my/resources/media/investor-alert-updates",
        "filename": "OFF-15_sc_investor_alert_updates.html",
        "folder": "official",
        "type": "Official alert list page",
        "reliability": "High - securities regulator public alert page.",
        "citation": "Securities Commission Malaysia. (n.d.). Investor Alert Updates.",
        "used_for": "Source family for investment-scam warning examples and possible appendix reference.",
        "chapters": "2, 5, Appendix",
        "factors": "F1, F3, F6, F7",
        "caveats": "Alert-list counts need careful scraping and date filters before being used quantitatively.",
    },
    {
        "id": "OFF-16",
        "title": "SC and MCMC Enhanced Oversight Media Release",
        "url": "https://www.sc.com.my/resources/media/media-release/sc-and-mcmc-to-combat-scams-via-enhanced-regulatory-oversight",
        "filename": "OFF-16_sc_mcmc_enhanced_oversight.html",
        "folder": "official",
        "type": "Official media release",
        "reliability": "High - regulator media release.",
        "citation": "Securities Commission Malaysia. (2025). SC and MCMC to combat scams via enhanced regulatory oversight.",
        "used_for": "Regulatory response and scam platform/channel discussion.",
        "chapters": "1, 2, 5",
        "factors": "F1, F3, F7",
        "caveats": "Use as regulatory context, not as proof of intervention effectiveness.",
    },
    {
        "id": "OFF-17",
        "title": "DOSM Crime Statistics Malaysia 2025",
        "url": "https://www.dosm.gov.my/portal-main/release-content/crime-statistics-malaysia-2025",
        "filename": "OFF-17_dosm_crime_statistics_2025.html",
        "folder": "official",
        "type": "Official statistics page",
        "reliability": "High - national statistics department publication.",
        "citation": "Department of Statistics Malaysia. (2025). Crime Statistics Malaysia 2025.",
        "used_for": "National crime-statistics context if cybercrime categories are relevant.",
        "chapters": "1, 5, Appendix",
        "factors": "F1",
        "caveats": "Use only if the indicator matches the report scope; broad crime statistics may not equal cyber fraud.",
    },
    {
        "id": "OFF-18",
        "title": "CyberSecurity Malaysia Cyber999 Q2 2024 Summary",
        "url": "https://www.cybersecurity.my/portal-main/advisories-details/47317289-8a00-11ef-b9ea-005056812d51",
        "filename": "OFF-18_csm_cyber999_q2_2024.html",
        "folder": "official",
        "type": "Official incident report",
        "reliability": "High - CyberSecurity Malaysia advisory.",
        "citation": "CyberSecurity Malaysia. (2024). Cyber Incident Quarterly Summary Report, Q2 2024.",
        "used_for": "Earlier Cyber999 baseline for fraud-share trend.",
        "chapters": "1, 2, 5",
        "factors": "F1, F7",
        "caveats": "Keep Cyber999 report data separate from police case/loss figures.",
    },
    {
        "id": "ACA-01",
        "title": "Personal, environmental and behavioral predictors associated with online fraud victimization among adults",
        "url": "https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0317232",
        "filename": "ACA-01_balakrishnan_online_fraud_predictors_plos.html",
        "folder": "academic",
        "type": "Open-access journal article page",
        "reliability": "High - peer-reviewed open-access journal article.",
        "citation": "Balakrishnan, V., et al. (2025). Personal, environmental and behavioral predictors associated with online fraud victimization among adults. PLOS ONE, 20(1), e0317232.",
        "used_for": "Behavioral predictors including overconfidence and social influence, and survey-design support.",
        "chapters": "2, 3, 5",
        "factors": "F1, F2, F7",
        "caveats": "Study population and measures must be compared carefully before direct adoption.",
    },
    {
        "id": "ACA-02",
        "title": "PLOS ONE printable PDF for online fraud predictors article",
        "url": "https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0317232&type=printable",
        "filename": "ACA-02_balakrishnan_online_fraud_predictors_plos.pdf",
        "folder": "academic",
        "type": "Open-access PDF",
        "reliability": "High - peer-reviewed open-access PDF.",
        "citation": "Balakrishnan, V., et al. (2025). Personal, environmental and behavioral predictors associated with online fraud victimization among adults. PLOS ONE, 20(1), e0317232.",
        "used_for": "Local archived PDF copy for behavioral predictor evidence and questionnaire framing.",
        "chapters": "2, 3, 5",
        "factors": "F1, F2, F7",
        "caveats": "Use the article's actual constructs; avoid stretching findings into unsupported revictimization claims.",
    },
    {
        "id": "ACA-03",
        "title": "A systematic literature review of profiling victims of cyber scam",
        "url": "https://research.monash.edu/en/publications/a-systematic-literature-review-of-profiling-victims-of-cyber-scam/",
        "filename": "ACA-03_whitty_cyber_scam_victim_profiling.html",
        "folder": "academic",
        "type": "Academic publication page",
        "reliability": "Medium-high - academic record; full text may depend on publisher access.",
        "citation": "Whitty, M. T. (2025). A systematic literature review of profiling victims of cyber scam. Cogent Social Sciences.",
        "used_for": "Victim-profiling gaps, theoretical framing, and need for stronger behavioral models.",
        "chapters": "2, 3",
        "factors": "F1, F2, F5, F7",
        "caveats": "Use abstract and available metadata unless a legal full text is available.",
    },
    {
        "id": "ACA-04",
        "title": "Fraud victimization and psychosocial impact review",
        "url": "https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1805536/full",
        "filename": "ACA-04_frontiers_fraud_psychosocial_impact.html",
        "folder": "academic",
        "type": "Open-access journal article page",
        "reliability": "High - peer-reviewed open-access journal article.",
        "citation": "Frontiers in Psychology. (2026). Fraud victimization and psychosocial impacts.",
        "used_for": "Shame, distress, self-blame, delayed disclosure, and recovery-support framing.",
        "chapters": "2, 4, 5",
        "factors": "F4, F5, F7",
        "caveats": "Use for psychosocial impact, not Malaysia-specific prevalence.",
    },
    {
        "id": "ACA-05",
        "title": "Systematic literature review on anti-phishing training",
        "url": "https://www.sciencedirect.com/science/article/pii/S0167404823006053",
        "filename": "ACA-05_anti_phishing_training_review.html",
        "folder": "academic",
        "type": "Publisher article page",
        "reliability": "Medium-high - peer-reviewed publisher page; full text availability depends on access.",
        "citation": "Computer & Security. (2024). Anti-phishing training: A systematic literature review.",
        "used_for": "Scenario-based training, feedback, and limits of short-term awareness interventions.",
        "chapters": "2, 4",
        "factors": "F1, F7",
        "caveats": "Do not download paywalled PDF. Use accessible abstract/metadata unless legal open access exists.",
    },
    {
        "id": "ACA-06",
        "title": "Protection Motivation Theory and phishing email behaviour",
        "url": "https://www.iieta.org/download/file/fid/166612",
        "filename": "ACA-06_pmt_phishing_behaviour.pdf",
        "folder": "academic",
        "type": "Open PDF",
        "reliability": "Medium-high - academic PDF source.",
        "citation": "IIETA. (n.d.). Protection Motivation Theory and phishing email behaviour.",
        "used_for": "PMT construct support: threat appraisal, coping appraisal, response efficacy, self-efficacy.",
        "chapters": "2, 3, 4",
        "factors": "F1, F4, F7",
        "caveats": "Check bibliographic details from the PDF before final references.",
    },
    {
        "id": "ACA-07",
        "title": "FTC Review of Scam Prevention Messaging Research",
        "url": "https://consumer.ftc.gov/system/files/consumer_ftc_gov/pdf/A%20Review%20of%20Scam%20Prevention%20Messaging%20Research.pdf",
        "filename": "ACA-07_ftc_scam_prevention_messaging_review.pdf",
        "folder": "academic",
        "type": "Government research review PDF",
        "reliability": "High - government consumer-protection research review.",
        "citation": "Federal Trade Commission. (2022). A review of scam prevention messaging research.",
        "used_for": "Message design, consumer warning limits, and intervention-development evidence.",
        "chapters": "2, 4",
        "factors": "F1, F4, F7",
        "caveats": "US-focused source; use for intervention theory, not Malaysia prevalence.",
    },
    {
        "id": "ACA-08",
        "title": "Mental health impacts of internet scams",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12192844/",
        "filename": "ACA-08_pmc_internet_scams_mental_health.html",
        "folder": "academic",
        "type": "Open-access article page",
        "reliability": "High - open article hosted by PubMed Central.",
        "citation": "PubMed Central. (2025). Mental health impacts of internet scams.",
        "used_for": "Psychological harm, shame, distress, and post-scam recovery discussion.",
        "chapters": "2, 4, 5",
        "factors": "F5, F7",
        "caveats": "Use for impact framing; verify exact article title/authors before final reference list.",
    },
    {
        "id": "ACA-09",
        "title": "Cybercrime Through Love Scams: What Women Should Know",
        "url": "https://jcis.uitm.edu.my/journal/volume8/issue2/3_Cybercrime_Through_Love_Scams_What_Women_Should_Know.pdf",
        "filename": "ACA-09_love_scam_women_uitm.pdf",
        "folder": "academic",
        "type": "Open academic PDF",
        "reliability": "Medium-high - open journal PDF from UiTM journal site.",
        "citation": "Journal of Contemporary Islamic Studies. (2022). Cybercrime through love scams: What women should know.",
        "used_for": "Local/contextual romance-scam and emotional grooming discussion.",
        "chapters": "2, 4",
        "factors": "F2, F5",
        "caveats": "Use as contextual literature, not as national prevalence evidence.",
    },
]


CYBER999_ROWS = [
    {
        "period": "2024 Q2",
        "total_incidents": "1481",
        "fraud_incidents": "947",
        "fraud_share_pct": "63.94",
        "phishing": "",
        "impersonation_spoofing": "",
        "bogus_email": "",
        "fraudulent_website": "",
        "job_scam": "",
        "business_email_compromise": "",
        "love_parcel_scam": "",
        "source_id": "OFF-18",
        "measurement_note": "Cyber999 handled incidents only.",
    },
    {
        "period": "2024 Q4",
        "total_incidents": "1550",
        "fraud_incidents": "1108",
        "fraud_share_pct": "71",
        "phishing": "810",
        "impersonation_spoofing": "252",
        "bogus_email": "",
        "fraudulent_website": "",
        "job_scam": "",
        "business_email_compromise": "",
        "love_parcel_scam": "",
        "source_id": "OFF-08",
        "measurement_note": "Cyber999 handled incidents only.",
    },
    {
        "period": "2025 Q1",
        "total_incidents": "1657",
        "fraud_incidents": "1126",
        "fraud_share_pct": "68",
        "phishing": "719",
        "impersonation_spoofing": "342",
        "bogus_email": "28",
        "fraudulent_website": "8",
        "job_scam": "20",
        "business_email_compromise": "6",
        "love_parcel_scam": "3",
        "source_id": "OFF-09",
        "measurement_note": "Cyber999 handled incidents only.",
    },
    {
        "period": "2025 Q2",
        "total_incidents": "2058",
        "fraud_incidents": "1633",
        "fraud_share_pct": "80",
        "phishing": "1127",
        "impersonation_spoofing": "341",
        "bogus_email": "56",
        "fraudulent_website": "40",
        "job_scam": "57",
        "business_email_compromise": "3",
        "love_parcel_scam": "9",
        "source_id": "OFF-10",
        "measurement_note": "Cyber999 handled incidents only.",
    },
    {
        "period": "2025 Q3",
        "total_incidents": "2020",
        "fraud_incidents": "1521",
        "fraud_share_pct": "75",
        "phishing": "1160",
        "impersonation_spoofing": "352",
        "bogus_email": "26",
        "fraudulent_website": "38",
        "job_scam": "25",
        "business_email_compromise": "8",
        "love_parcel_scam": "5",
        "source_id": "OFF-11",
        "measurement_note": "Cyber999 handled incidents only.",
    },
    {
        "period": "2025 Q4",
        "total_incidents": "",
        "fraud_incidents": "1471",
        "fraud_share_pct": "",
        "phishing": "",
        "impersonation_spoofing": "",
        "bogus_email": "",
        "fraudulent_website": "",
        "job_scam": "",
        "business_email_compromise": "",
        "love_parcel_scam": "",
        "source_id": "OFF-12",
        "measurement_note": "Partial extracted point. Full table should be checked before using as a complete quarter.",
    },
]


PDRM_ROWS = [
    {
        "period": "2025 Q1",
        "indicator": "Online financial fraud cases",
        "cases": "12110",
        "loss_rm_million": "573.7",
        "source_id": "OFF-04",
        "measurement_note": "PDRM figure quoted by BNM speech. Police case/loss figures, not Cyber999 incidents.",
    },
    {
        "period": "2025 Jan-Nov",
        "indicator": "Online crime cases",
        "cases": "67735",
        "loss_rm_million": ">2700",
        "source_id": "OFF-11",
        "measurement_note": "PDRM figure quoted by MyCERT Q3 2025. Do not merge with Cyber999 handled incidents.",
    },
    {
        "period": "2026 Jan-Mar",
        "indicator": "Job scam cases",
        "cases": "1537",
        "loss_rm_million": "31.8",
        "source_id": "OFF-05",
        "measurement_note": "PDRM Scam Alert job-scam warning. Specific scam type and period.",
    },
]


FACTOR_LABELS = {
    "F1": "Awareness gap",
    "F2": "Social influence and trust transfer",
    "F3": "Authority impersonation",
    "F4": "Urgency and fear",
    "F5": "Emotional grooming, shame and recovery",
    "F6": "Financial need and FOMO",
    "F7": "Protective self-efficacy and reporting",
}


EVIDENCE_ROWS = [
    {
        "claim_id": "EV-01",
        "claim": "Cyber fraud is a continuing national financial and social problem, but different agencies measure different parts of it.",
        "source_ids": "OFF-01; OFF-04; OFF-10; OFF-11",
        "chapter": "1.1, 1.2, 5.2",
        "factors": "F1, F7",
        "citation_status": "Partial - Cyber999 local copies ready; BNM local copy blocked",
        "notes": "Separate BNM/PDRM financial figures from Cyber999 incident counts. Manually archive BNM source before final citation.",
    },
    {
        "claim_id": "EV-02",
        "claim": "Cyber999 fraud incidents increased strongly from Q1 2025 to Q2 2025 and remained high in Q3 2025.",
        "source_ids": "OFF-09; OFF-10; OFF-11",
        "chapter": "1.2, 5.2",
        "factors": "F1, F3, F7",
        "citation_status": "Ready - official Cyber999 reports",
        "notes": "Use as incident-report trend, not national police case trend.",
    },
    {
        "claim_id": "EV-03",
        "claim": "Phishing and impersonation/spoofing are major fraud categories in Cyber999 quarterly reporting.",
        "source_ids": "OFF-09; OFF-10; OFF-11",
        "chapter": "2.2, 5.2",
        "factors": "F1, F3, F4",
        "citation_status": "Ready - official Cyber999 reports",
        "notes": "Supports scenario design and authority-impersonation factor.",
    },
    {
        "claim_id": "EV-04",
        "claim": "PDRM public warnings include job scams, impersonation of acquaintances, urgent borrowing, AI voice misuse and NSRC 997 reminders.",
        "source_ids": "OFF-05",
        "chapter": "2.2, 4.2",
        "factors": "F2, F3, F4, F5, F6, F7",
        "citation_status": "Ready - official warning page",
        "notes": "Use dated warning examples carefully because page content changes.",
    },
    {
        "claim_id": "EV-05",
        "claim": "Investment scam warnings commonly involve unrealistic returns, low-risk promises, pressure, fake documents and unrelated bank accounts.",
        "source_ids": "OFF-13; OFF-14; OFF-15",
        "chapter": "2.2, 4.3",
        "factors": "F1, F3, F4, F6, F7",
        "citation_status": "Ready - SC guidance",
        "notes": "Useful for scenario red flags and tool-checking module.",
    },
    {
        "claim_id": "EV-06",
        "claim": "Verification tools such as Semak Mule, NSRC, SC Investment Checker and Cyber999 can support protective action after exposure to scams.",
        "source_ids": "OFF-06; OFF-07; OFF-13; OFF-14; OFF-18",
        "chapter": "4.3, Appendix",
        "factors": "F7",
        "citation_status": "Ready - official tool pages",
        "notes": "Use as protective self-efficacy action map, not proof that all victims will report.",
    },
    {
        "claim_id": "EV-07",
        "claim": "Online fraud victimization research has found behavioral predictors such as overconfidence and social influence.",
        "source_ids": "ACA-01; ACA-02",
        "chapter": "2.3, 3.4",
        "factors": "F1, F2, F7",
        "citation_status": "Ready - peer-reviewed open access",
        "notes": "Good support for questionnaire and conceptual framework.",
    },
    {
        "claim_id": "EV-08",
        "claim": "Cyber scam victim profiling literature still has gaps in behavioral theory use and intervention-oriented measurement.",
        "source_ids": "ACA-03",
        "chapter": "2.4, 3.1",
        "factors": "F1, F2, F5, F7",
        "citation_status": "Partial - metadata and abstract unless full text is legally available",
        "notes": "Use conservatively unless full open text is confirmed.",
    },
    {
        "claim_id": "EV-09",
        "claim": "Fraud victimization can cause distress, shame, self-blame and delayed help-seeking, which matters for revictimization prevention.",
        "source_ids": "ACA-04; ACA-08",
        "chapter": "2.5, 4.4",
        "factors": "F5, F7",
        "citation_status": "Ready - open literature",
        "notes": "Use for recovery and non-blaming intervention language.",
    },
    {
        "claim_id": "EV-10",
        "claim": "Short awareness or phishing training may improve near-term identification, but sustained behavior change requires design and evaluation.",
        "source_ids": "ACA-05; ACA-07",
        "chapter": "2.6, 4.5",
        "factors": "F1, F7",
        "citation_status": "Partial - FTC local copy ready; ScienceDirect page blocked",
        "notes": "Use FTC review now. Locate legal open access for ACA-05 before relying on the publisher article.",
    },
    {
        "claim_id": "EV-11",
        "claim": "Protection Motivation Theory helps structure scam-prevention content around threat appraisal, coping appraisal and self-efficacy.",
        "source_ids": "ACA-06",
        "chapter": "2.7, 3.3, 4.2",
        "factors": "F1, F4, F7",
        "citation_status": "Needs final bibliographic check",
        "notes": "Verify title/authors from PDF before final reference list.",
    },
    {
        "claim_id": "EV-12",
        "claim": "Romance/love scam literature helps explain emotional grooming, trust transfer and delayed disclosure.",
        "source_ids": "ACA-09",
        "chapter": "2.5, 4.4",
        "factors": "F2, F5",
        "citation_status": "Ready - open academic PDF with context caveat",
        "notes": "Use as local contextual literature, not broad prevalence.",
    },
]


def ensure_dirs() -> None:
    for directory in [
        OFFICIAL_DIR,
        ACADEMIC_DIR,
        NOTES_DIR,
        RAW_DIR,
        CLEAN_DIR,
        OUTPUT_DIR,
        EVIDENCE_DIR,
    ]:
        directory.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def download_source(entry: dict[str, str]) -> dict[str, str]:
    target_dir = OFFICIAL_DIR if entry["folder"] == "official" else ACADEMIC_DIR
    target = target_dir / entry["filename"]
    req = urllib.request.Request(
        entry["url"],
        headers={
            "User-Agent": "Mozilla/5.0 research-source-archiver/1.0",
            "Accept": "*/*",
        },
    )
    context = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=45, context=context) as response:
            data = response.read()
            if len(data) == 0:
                error_path = target.with_suffix(target.suffix + ".download_error.txt")
                if target.exists():
                    target.unlink()
                write_text(
                    error_path,
                    f"Download failed on {TODAY}\nURL: {entry['url']}\nError: Empty response body with HTTP {getattr(response, 'status', '')}\n",
                )
                return {
                    "id": entry["id"],
                    "url": entry["url"],
                    "path": str(error_path.relative_to(CYBER_DIR)),
                    "status": "failed",
                    "http_status": str(getattr(response, "status", "")),
                    "bytes": "0",
                    "error": "Empty response body",
                }
            target.write_bytes(data)
            return {
                "id": entry["id"],
                "url": entry["url"],
                "path": str(target.relative_to(CYBER_DIR)),
                "status": "downloaded",
                "http_status": str(getattr(response, "status", "")),
                "bytes": str(len(data)),
                "error": "",
            }
    except Exception as exc:
        if "CERTIFICATE_VERIFY_FAILED" in repr(exc):
            try:
                with urllib.request.urlopen(
                    req, timeout=45, context=ssl._create_unverified_context()
                ) as response:
                    data = response.read()
                    if len(data) > 0:
                        target.write_bytes(data)
                        error_path = target.with_suffix(target.suffix + ".download_warning.txt")
                        write_text(
                            error_path,
                            f"Download warning on {TODAY}\nURL: {entry['url']}\nWarning: Saved using SSL verification fallback after certificate-chain verification failed.\n",
                        )
                        return {
                            "id": entry["id"],
                            "url": entry["url"],
                            "path": str(target.relative_to(CYBER_DIR)),
                            "status": "downloaded_ssl_unverified",
                            "http_status": str(getattr(response, "status", "")),
                            "bytes": str(len(data)),
                            "error": "Saved with SSL verification fallback",
                        }
            except Exception as fallback_exc:
                exc = fallback_exc
        if target.exists() and target.stat().st_size > 1000:
            error_path = target.with_suffix(target.suffix + ".download_error.txt")
            write_text(
                error_path,
                f"Download warning on {TODAY}\nURL: {entry['url']}\nError: {exc}\nExisting cached file kept: {target.name}\n",
            )
            return {
                "id": entry["id"],
                "url": entry["url"],
                "path": str(target.relative_to(CYBER_DIR)),
                "status": "cached_after_download_error",
                "http_status": "",
                "bytes": str(target.stat().st_size),
                "error": repr(exc),
            }
        error_path = target.with_suffix(target.suffix + ".download_error.txt")
        write_text(error_path, f"Download failed on {TODAY}\nURL: {entry['url']}\nError: {exc}\n")
        return {
            "id": entry["id"],
            "url": entry["url"],
            "path": str(error_path.relative_to(CYBER_DIR)),
            "status": "failed",
            "http_status": "",
            "bytes": "0",
            "error": repr(exc),
        }


def source_note(entry: dict[str, str], log: dict[str, str]) -> str:
    wrapped_used = textwrap.fill(entry["used_for"], width=92)
    wrapped_caveat = textwrap.fill(entry["caveats"], width=92)
    return f"""# {entry['id']} - {entry['title']}

## Citation
{entry['citation']}

## Source Type And Reliability
- Type: {entry['type']}
- Reliability: {entry['reliability']}
- Accessed: {TODAY}
- URL: {entry['url']}
- Local file/status: `{log['path']}` ({log['status']})

## Information Used
{wrapped_used}

## Report Placement
- Chapters supported: {entry['chapters']}
- Seven-factor mapping: {entry['factors']}

## Caveats And Limits
{wrapped_caveat}

## Implementation Note
Use this source only for the claim types listed above. If a numerical indicator comes from
this source, keep the original measurement family intact and do not combine it with other
agency datasets unless the units and collection method match.
"""


def build_inventory(logs: list[dict[str, str]]) -> str:
    lines = [
        "# Cyber Fraud Source Library Inventory",
        "",
        f"Generated: {TODAY}",
        "",
        "This inventory records the public sources prepared for the cyber fraud research report.",
        "Downloaded files are stored under `source_library/official_reports/` or",
        "`source_library/academic_papers/`. Failed downloads are still recorded with an error file",
        "so the missing item can be manually checked later.",
        "",
        "| Source ID | Source | Type | Local Status | Chapters | Factors |",
        "|---|---|---|---|---|---|",
    ]
    log_by_id = {log["id"]: log for log in logs}
    for entry in SOURCE_ENTRIES:
        log = log_by_id.get(entry["id"], {"status": "not attempted", "path": ""})
        lines.append(
            f"| {entry['id']} | {entry['title']} | {entry['type']} | {log['status']} | {entry['chapters']} | {entry['factors']} |"
        )
    lines.extend(
        [
            "",
            "## Dataset Separation Rule",
            "",
            "- Cyber999 incident data is treated as handled incident reports.",
            "- PDRM figures are police case/loss indicators.",
            "- BNM/NFP indicators are banking and response-system indicators.",
            "- SC data is regulatory warning and verification context unless a dated numeric alert dataset is extracted separately.",
        ]
    )
    return "\n".join(lines) + "\n"


def build_manual_followup(logs: list[dict[str, str]]) -> str:
    log_by_id = {log["id"]: log for log in logs}
    lines = [
        "# Manual Follow-Up Sources",
        "",
        f"Generated: {TODAY}",
        "",
        "These sources were identified as useful but could not be archived as normal local copies",
        "during the automated build. They should be checked manually before final report citation.",
        "",
        "| Source ID | Title | URL | Current Status | Required Action |",
        "|---|---|---|---|---|",
    ]
    for entry in SOURCE_ENTRIES:
        log = log_by_id.get(entry["id"])
        if not log or log["status"] not in {"failed", "downloaded_ssl_unverified"}:
            continue
        if log["status"] == "downloaded_ssl_unverified":
            action = "Open the page in a browser and confirm the captured file is the expected public page; keep the SSL-warning note."
        elif entry["id"].startswith("OFF-01") or entry["id"].startswith("OFF-02") or entry["id"].startswith("OFF-03") or entry["id"].startswith("OFF-04"):
            action = "Manually download or save the official BNM page/PDF from a browser because the automated request returned an empty protected response."
        elif entry["id"] == "ACA-05":
            action = "Do not download a paywalled copy. Use accessible metadata only or locate a legal open-access author copy."
        else:
            action = "Retry in browser or confirm whether the source is still needed."
        lines.append(
            f"| {entry['id']} | {entry['title']} | {entry['url']} | {log['status']} ({log['error']}) | {action} |"
        )
    lines.extend(
        [
            "",
            "## Priority",
            "",
            "1. BNM Annual Report 2025 / Fraud Resolution materials are high priority because they support national scam-response framing.",
            "2. ScienceDirect anti-phishing review is useful but replaceable with an open-access review if no legal full text is available.",
            "3. SSL-fallback pages are usable as working copies but should be visually checked in a normal browser before final submission.",
        ]
    )
    return "\n".join(lines) + "\n"


def parse_float(value: str) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(str(value).replace(">", ""))
    except ValueError:
        return None


def clean_cyber999_rows() -> list[dict[str, str]]:
    cleaned = []
    for row in CYBER999_ROWS:
        total = parse_float(row["total_incidents"])
        fraud = parse_float(row["fraud_incidents"])
        stated_share = parse_float(row["fraud_share_pct"])
        computed_share = ""
        check_note = "partial"
        if total and fraud:
            computed = fraud / total * 100
            computed_share = f"{computed:.2f}"
            if stated_share is None:
                check_note = "computed only"
            elif abs(computed - stated_share) <= 1.0:
                check_note = "share check ok"
            else:
                check_note = "share differs from stated source"
        cleaned.append(
            {
                **row,
                "computed_fraud_share_pct": computed_share,
                "data_check_note": check_note,
            }
        )
    return cleaned


def factor_coverage_rows() -> list[dict[str, str]]:
    rows = []
    for factor, label in FACTOR_LABELS.items():
        evidence_count = 0
        official_count = 0
        academic_count = 0
        for ev in EVIDENCE_ROWS:
            factors = [item.strip() for item in ev["factors"].split(",")]
            if factor in factors:
                evidence_count += 1
                ids = [item.strip() for item in ev["source_ids"].split(";")]
                official_count += sum(1 for sid in ids if sid.startswith("OFF-"))
                academic_count += sum(1 for sid in ids if sid.startswith("ACA-"))
        rows.append(
            {
                "factor_id": factor,
                "factor": label,
                "evidence_claim_count": str(evidence_count),
                "official_source_mentions": str(official_count),
                "academic_source_mentions": str(academic_count),
            }
        )
    return rows


def svg_escape(value: str) -> str:
    return html.escape(str(value), quote=True)


def write_line_svg(path: Path, labels: list[str], series: dict[str, list[float | None]], title: str) -> None:
    width, height = 980, 540
    margin_left, margin_right, margin_top, margin_bottom = 88, 40, 72, 92
    plot_w = width - margin_left - margin_right
    plot_h = height - margin_top - margin_bottom
    values = [v for vals in series.values() for v in vals if v is not None]
    max_val = max(values) if values else 1
    max_axis = math.ceil(max_val / 250) * 250
    x_positions = [
        margin_left + (plot_w * i / max(1, len(labels) - 1)) for i in range(len(labels))
    ]

    def y(value: float) -> float:
        return margin_top + plot_h - (value / max_axis) * plot_h

    colors = ["#1f5f99", "#c25b2c", "#4c7c3f"]
    chunks = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<text x="{width/2}" y="34" text-anchor="middle" font-family="Times New Roman, serif" font-size="22" font-weight="bold">{svg_escape(title)}</text>',
        f'<line x1="{margin_left}" y1="{margin_top + plot_h}" x2="{width - margin_right}" y2="{margin_top + plot_h}" stroke="#222"/>',
        f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{margin_top + plot_h}" stroke="#222"/>',
    ]
    for step in range(0, 6):
        val = max_axis * step / 5
        y_pos = y(val)
        chunks.append(f'<line x1="{margin_left}" y1="{y_pos:.1f}" x2="{width - margin_right}" y2="{y_pos:.1f}" stroke="#e5e8ef"/>')
        chunks.append(f'<text x="{margin_left - 12}" y="{y_pos + 4:.1f}" text-anchor="end" font-family="Times New Roman, serif" font-size="13">{int(val)}</text>')
    for i, label in enumerate(labels):
        chunks.append(f'<text x="{x_positions[i]:.1f}" y="{height - 54}" text-anchor="middle" font-family="Times New Roman, serif" font-size="13">{svg_escape(label)}</text>')
    for idx, (name, vals) in enumerate(series.items()):
        color = colors[idx % len(colors)]
        points = []
        for i, value in enumerate(vals):
            if value is None:
                continue
            points.append(f"{x_positions[i]:.1f},{y(value):.1f}")
            chunks.append(f'<circle cx="{x_positions[i]:.1f}" cy="{y(value):.1f}" r="4" fill="{color}"/>')
            chunks.append(f'<text x="{x_positions[i]:.1f}" y="{y(value) - 10:.1f}" text-anchor="middle" font-family="Times New Roman, serif" font-size="12" fill="{color}">{int(value)}</text>')
        if len(points) >= 2:
            chunks.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{color}" stroke-width="3"/>')
        chunks.append(f'<rect x="{margin_left + idx * 220}" y="{height - 28}" width="16" height="10" fill="{color}"/>')
        chunks.append(f'<text x="{margin_left + 22 + idx * 220}" y="{height - 19}" font-family="Times New Roman, serif" font-size="13">{svg_escape(name)}</text>')
    chunks.append("</svg>")
    write_text(path, "\n".join(chunks))


def write_bar_svg(path: Path, labels: list[str], values: list[float], title: str, subtitle: str = "") -> None:
    width, height = 980, 560
    margin_left, margin_right, margin_top, margin_bottom = 96, 40, 80, 126
    plot_w = width - margin_left - margin_right
    plot_h = height - margin_top - margin_bottom
    max_val = max(values) if values else 1
    max_axis = math.ceil(max_val / 100) * 100
    bar_gap = 18
    bar_w = max(28, (plot_w - bar_gap * (len(labels) - 1)) / max(1, len(labels)))

    def y(value: float) -> float:
        return margin_top + plot_h - (value / max_axis) * plot_h

    chunks = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<text x="{width/2}" y="34" text-anchor="middle" font-family="Times New Roman, serif" font-size="22" font-weight="bold">{svg_escape(title)}</text>',
    ]
    if subtitle:
        chunks.append(f'<text x="{width/2}" y="58" text-anchor="middle" font-family="Times New Roman, serif" font-size="14">{svg_escape(subtitle)}</text>')
    chunks.append(f'<line x1="{margin_left}" y1="{margin_top + plot_h}" x2="{width - margin_right}" y2="{margin_top + plot_h}" stroke="#222"/>')
    chunks.append(f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{margin_top + plot_h}" stroke="#222"/>')
    for step in range(0, 6):
        val = max_axis * step / 5
        y_pos = y(val)
        chunks.append(f'<line x1="{margin_left}" y1="{y_pos:.1f}" x2="{width - margin_right}" y2="{y_pos:.1f}" stroke="#e5e8ef"/>')
        chunks.append(f'<text x="{margin_left - 12}" y="{y_pos + 4:.1f}" text-anchor="end" font-family="Times New Roman, serif" font-size="13">{int(val)}</text>')
    for i, (label, value) in enumerate(zip(labels, values)):
        x = margin_left + i * (bar_w + bar_gap)
        y_pos = y(value)
        chunks.append(f'<rect x="{x:.1f}" y="{y_pos:.1f}" width="{bar_w:.1f}" height="{margin_top + plot_h - y_pos:.1f}" fill="#2e6f9e"/>')
        chunks.append(f'<text x="{x + bar_w/2:.1f}" y="{y_pos - 8:.1f}" text-anchor="middle" font-family="Times New Roman, serif" font-size="13">{int(value)}</text>')
        label_lines = textwrap.wrap(label, width=12)
        for line_index, line in enumerate(label_lines[:3]):
            chunks.append(f'<text x="{x + bar_w/2:.1f}" y="{height - 84 + line_index * 15}" text-anchor="middle" font-family="Times New Roman, serif" font-size="13">{svg_escape(line)}</text>')
    chunks.append("</svg>")
    write_text(path, "\n".join(chunks))


def write_timeline_svg(path: Path) -> None:
    events = [
        ("Semak Mule", "Police checking tool for mule-account risk."),
        ("NSRC 997", "Rapid scam response channel for financial scam victims."),
        ("Cyber999", "Cyber incident reporting and response channel."),
        ("SC tools", "Investment Checker and investor alert guidance."),
        ("NFP", "Banking-sector fraud-response coordination."),
    ]
    width, height = 980, 420
    x0, y0 = 90, 190
    spacing = 190
    chunks = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<text x="{width/2}" y="42" text-anchor="middle" font-family="Times New Roman, serif" font-size="22" font-weight="bold">Malaysia Scam Response Tool Map</text>',
        f'<line x1="{x0}" y1="{y0}" x2="{x0 + spacing * (len(events) - 1)}" y2="{y0}" stroke="#25364a" stroke-width="3"/>',
    ]
    for i, (title, desc) in enumerate(events):
        x = x0 + spacing * i
        chunks.append(f'<circle cx="{x}" cy="{y0}" r="14" fill="#2e6f9e"/>')
        chunks.append(f'<text x="{x}" y="{y0 - 34}" text-anchor="middle" font-family="Times New Roman, serif" font-size="16" font-weight="bold">{svg_escape(title)}</text>')
        for line_idx, line in enumerate(textwrap.wrap(desc, width=22)[:3]):
            chunks.append(f'<text x="{x}" y="{y0 + 46 + line_idx * 16}" text-anchor="middle" font-family="Times New Roman, serif" font-size="13">{svg_escape(line)}</text>')
    chunks.append("</svg>")
    write_text(path, "\n".join(chunks))


def build_analysis_outputs() -> None:
    clean_rows = clean_cyber999_rows()
    write_csv(RAW_DIR / "cyber999_quarterly_indicators_raw.csv", CYBER999_ROWS)
    write_csv(CLEAN_DIR / "cyber999_quarterly_indicators_clean.csv", clean_rows)
    write_csv(RAW_DIR / "pdrm_officially_quoted_online_fraud_indicators_raw.csv", PDRM_ROWS)

    coverage = factor_coverage_rows()
    write_csv(CLEAN_DIR / "seven_factor_evidence_coverage.csv", coverage)

    labels = [row["period"] for row in clean_rows]
    total_values = [parse_float(row["total_incidents"]) for row in clean_rows]
    fraud_values = [parse_float(row["fraud_incidents"]) for row in clean_rows]
    write_line_svg(
        OUTPUT_DIR / "cyber999_total_vs_fraud_trend.svg",
        labels,
        {"Total incidents": total_values, "Fraud incidents": fraud_values},
        "Cyber999 Total Incidents and Fraud Incidents by Quarter",
    )

    q2_2025 = next(row for row in clean_rows if row["period"] == "2025 Q2")
    category_labels = [
        "Phishing",
        "Impersonation",
        "Bogus email",
        "Fraud website",
        "Job scam",
        "BEC",
        "Love/parcel",
    ]
    category_values = [
        float(q2_2025["phishing"]),
        float(q2_2025["impersonation_spoofing"]),
        float(q2_2025["bogus_email"]),
        float(q2_2025["fraudulent_website"]),
        float(q2_2025["job_scam"]),
        float(q2_2025["business_email_compromise"]),
        float(q2_2025["love_parcel_scam"]),
    ]
    write_bar_svg(
        OUTPUT_DIR / "cyber999_top_fraud_categories_q2_2025.svg",
        category_labels,
        category_values,
        "Cyber999 Fraud Categories, Q2 2025",
        "Source family: MyCERT/Cyber999 handled incidents",
    )

    write_bar_svg(
        OUTPUT_DIR / "seven_factor_evidence_coverage.svg",
        [row["factor_id"] for row in coverage],
        [float(row["evidence_claim_count"]) for row in coverage],
        "Evidence Coverage by Seven-Factor Backbone",
        "Count of evidence-matrix claims mapped to each factor",
    )

    write_timeline_svg(OUTPUT_DIR / "malaysia_scam_response_tool_map.svg")

    summary = [
        "# Secondary Data And Chart Analysis Summary",
        "",
        f"Generated: {TODAY}",
        "",
        "## Files Created",
        "",
        "- `datasets_raw/cyber999_quarterly_indicators_raw.csv`",
        "- `datasets_clean/cyber999_quarterly_indicators_clean.csv`",
        "- `datasets_raw/pdrm_officially_quoted_online_fraud_indicators_raw.csv`",
        "- `datasets_clean/seven_factor_evidence_coverage.csv`",
        "- `analysis_outputs/cyber999_total_vs_fraud_trend.svg`",
        "- `analysis_outputs/cyber999_top_fraud_categories_q2_2025.svg`",
        "- `analysis_outputs/seven_factor_evidence_coverage.svg`",
        "- `analysis_outputs/malaysia_scam_response_tool_map.svg`",
        "",
        "## Data Integrity Notes",
        "",
        "- Cyber999 figures are handled incident reports, not all Malaysian police cases.",
        "- PDRM case/loss figures are stored separately because the measurement unit is different.",
        "- Q4 2025 Cyber999 currently contains a partial extracted fraud value and should be checked before full trend interpretation.",
        "- The generated charts are descriptive secondary-data visuals. They are not survey or intervention results.",
        "",
        "## Fraud Share Checks",
        "",
        "| Period | Total | Fraud | Stated % | Computed % | Check |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for row in clean_rows:
        summary.append(
            f"| {row['period']} | {row['total_incidents'] or 'NA'} | {row['fraud_incidents'] or 'NA'} | {row['fraud_share_pct'] or 'NA'} | {row['computed_fraud_share_pct'] or 'NA'} | {row['data_check_note']} |"
        )
    write_text(OUTPUT_DIR / "analysis_summary.md", "\n".join(summary) + "\n")


def build_evidence_matrix() -> str:
    lines = [
        "# Evidence Matrix V2",
        "",
        f"Generated: {TODAY}",
        "",
        "This matrix links report claims to source IDs, chapter placement, seven-factor mapping,",
        "and citation status. It is designed to prevent unsupported claims and to keep official",
        "statistics separated by measurement type.",
        "",
        "| Claim ID | Report Claim | Source ID(s) | Chapter Section | Seven-Factor Mapping | Citation Status | Notes |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in EVIDENCE_ROWS:
        lines.append(
            f"| {row['claim_id']} | {row['claim']} | {row['source_ids']} | {row['chapter']} | {row['factors']} | {row['citation_status']} | {row['notes']} |"
        )
    lines.extend(
        [
            "",
            "## Seven-Factor Backbone",
            "",
            "| Factor | Meaning |",
            "|---|---|",
        ]
    )
    for factor, label in FACTOR_LABELS.items():
        lines.append(f"| {factor} | {label} |")
    lines.extend(
        [
            "",
            "## Rules For Chapter 5",
            "",
            "- These sources can support descriptive secondary analysis.",
            "- They cannot be written as survey findings or intervention results.",
            "- PDRM police case/loss figures, Cyber999 handled incidents, BNM banking response figures,",
            "  and SC regulatory warnings must remain separate unless a compatible measurement basis is documented.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    ensure_dirs()

    logs = []
    for entry in SOURCE_ENTRIES:
        log = download_source(entry)
        logs.append(log)
        write_text(NOTES_DIR / f"{entry['id']}_source_note.md", source_note(entry, log))

    write_csv(
        LIB_DIR / "download_log.csv",
        logs,
        ["id", "url", "path", "status", "http_status", "bytes", "error"],
    )
    write_text(LIB_DIR / "source_inventory.md", build_inventory(logs))
    write_text(LIB_DIR / "manual_followup_sources.md", build_manual_followup(logs))

    build_analysis_outputs()
    matrix = build_evidence_matrix()
    write_text(EVIDENCE_DIR / "evidence_matrix_v2.md", matrix)
    write_text(LIB_DIR / "evidence_matrix_v2.md", matrix)

    manifest = {
        "generated": TODAY,
        "source_count": len(SOURCE_ENTRIES),
        "downloaded": sum(1 for log in logs if log["status"] == "downloaded"),
        "downloaded_ssl_unverified": sum(
            1 for log in logs if log["status"] == "downloaded_ssl_unverified"
        ),
        "cached_after_download_error": sum(
            1 for log in logs if log["status"] == "cached_after_download_error"
        ),
        "hard_failed": sum(1 for log in logs if log["status"] == "failed"),
        "usable_local_sources": sum(
            1
            for log in logs
            if log["status"] in {"downloaded", "downloaded_ssl_unverified", "cached_after_download_error"}
        ),
        "source_library": str(LIB_DIR.relative_to(WORKING_DIR.parent)),
        "evidence_matrix": str((EVIDENCE_DIR / "evidence_matrix_v2.md").relative_to(WORKING_DIR.parent)),
        "note": "The main cyber fraud report draft was not edited by this script.",
    }
    write_text(LIB_DIR / "build_manifest.json", json.dumps(manifest, indent=2))
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
