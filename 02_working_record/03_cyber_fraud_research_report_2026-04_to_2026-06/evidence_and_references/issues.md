# Final Audit Synthesis: Malaysia-Centric Cyber Scam Revictimization Report

Audit cutoff: 20 May 2026  
Files audited as frozen input: `table_of_contents.md`, `chapter1.md` to `chapter6.md`, `reference.md`, `paper writing guidelines/thesis_guide.md`, and `paper writing guidelines/template_demo_breakdown.md`.  
Support files created for this audit: `task_2.md`, `reference_new_live.md`, and `research_evidence_matrix.md`.

## Verdict

The report has a defensible research direction but is not yet research-valid for submission. Its strongest feature is the integration of TPB, PMT, and Cognitive Appraisal Theory to explain scam response behaviour. Its weakest feature is that many Malaysia-specific claims are either uncited, only generally cited, or supported by placeholder references. The report also uses "revictimization" as the central outcome before defining how repeat victimization will be measured.

Overall judgement:

| Criterion | Verdict | Reason |
| --- | --- | --- |
| Research-valid | Conditionally valid | The theory direction is coherent, but the revictimization construct and factor model need operational sharpening. |
| Evidence-backed | Not yet | Current `reference.md` is incomplete and Chapter 2 contains statistics marked for verification. |
| Malaysia-specific | Promising but uneven | Scam examples are local, but many claims need official Malaysian source IDs and exact checked URLs. |
| Methodologically workable | Partly | Quantitative survey plus scenarios is workable, but prior-victim sampling, repeat-victim measurement, and intervention evaluation need more detail. |
| Formatting/template fit | Secondary issue | Structure follows the template broadly but has chapter-count mismatch and incomplete Chapter 6. |

## Severity-Ranked Issues

### Critical 1: `reference.md` is not a valid reference list

The current reference list is too incomplete for the level of factual and methodological claims made in the report. It includes placeholder entries such as "BNM (2024) National Fraud Portal launch and online fraud prevention materials" and "MyCERT (2024-2025) Cyber incident quarterly summary reports and advisories" without exact titles, URLs, dates, authors/institutions, or access dates.

Why it matters: A literature review and Malaysia trend table cannot be considered evidence-backed if the reader cannot trace the sources.

Fix later:

- Replace placeholder references with checked entries from `reference_new_live.md`.
- Keep official/regulatory sources separate from academic sources and secondary news/vendor sources.
- Do not cite BusinessToday, Fortinet, or Bernama as primary national statistics unless the claim is clearly attributed and caveated.

### Critical 2: The 2019-2025 trend table is not submission-safe

Chapter 2 Table 2.1 includes major case and loss figures but the table note already admits that losses for 2023 and full-year 2025 should be verified. The 2025 RM2.7 billion figure has secondary support from Bernama/Fortinet, but the audit did not confirm it from a primary PDRM or BNM source.

Why it matters: This is a central Malaysia-specific evidence table. If figures are inaccurate or unevenly sourced, the report's credibility drops sharply.

Fix later:

- Rebuild Table 2.1 only from official PDRM, BNM, NSRC/MOF, MyCERT/Cyber999, SC, and MCMC sources where possible.
- Separate incident reports, police cases, calls to NSRC, Cyber999 reports, blocked transactions, and financial losses because they measure different things.
- Add caveats beside any vendor/news-derived 2025 figure.

### Critical 3: Revictimization is central but underdefined

The report repeatedly states "revictimization tendency" and "repeated victimization", but it does not yet define whether revictimization means repeat financial loss, repeat scam exposure, repeated risky compliance after a previous scam, recovery-scam targeting, or psychological vulnerability after prior victimization.

Why it matters: Without an operational definition, the questionnaire, sampling, analysis, and module evaluation cannot validly answer the research aim.

Fix later:

- Define revictimization in Chapter 1 and Chapter 3 as measurable categories:
  - previous confirmed victimization with loss,
  - repeated scam exposure after prior victimization,
  - repeated risky compliance in scenarios,
  - recovery scam or fake support targeting after loss,
  - delayed/non-reporting caused by shame or low self-efficacy.
- Use prior-victim subgroup analysis rather than treating all respondents the same.

### Critical 4: Prior-victim sampling is not strong enough

Chapter 3 says prior victims should be intentionally included, but it does not specify how many prior victims are needed, how repeat victims will be identified, or how sensitive victim data will be protected.

Why it matters: A study about revictimization must include enough prior victims or repeat-exposure respondents to test the actual outcome.

Fix later:

- Add inclusion logic for prior cyber scam victims and attempted-scam targets.
- Set a minimum prior-victim subgroup target or justify feasibility if using purposive/convenience sampling.
- Add ethics safeguards: no bank credentials, no account numbers, no raw scam screenshots with personal data, and referral information for reporting/support.

### High 5: The seven factors need to become the report's measurement spine

Chapter 2 currently lists behavioural factors, but Chapter 3 and Chapter 4 do not yet make them a stable seven-factor model. The upgraded taxonomy in `task_2.md` should become the later chapter backbone.

Why it matters: Without a stable factor model, constructs, survey sections, scenarios, module content, and evaluation indicators will feel loosely connected.

Fix later:

- Use the seven categories from `task_2.md`.
- Add a factor-to-theory-to-measurement table in Chapter 3.
- Add a factor-to-module mapping in Chapter 4.
- Keep all categories Malaysia-specific through local scam cues.

### High 6: Chapter 6 is effectively missing and the table of contents is inconsistent

`chapter6.md` contains almost no substantive content, while `table_of_contents.md` lists only five main chapters and the guide/template expects a six-chapter structure. Chapter 5 is currently titled "Conclusion and Recommendations", which overlaps with what the template expects in Chapter 6.

Why it matters: The report may fail structural expectations even if the research argument improves.

Fix later:

- Decide whether the final report uses five or six chapters.
- If following the UTM template, make Chapter 5 "Results, Analysis and Discussion" or expected findings/evaluation if no final data exists, and Chapter 6 "Conclusion".
- If staying with five chapters, update the table of contents and justify the structure according to supervisor expectations.

### High 7: Intervention evaluation is plausible but not yet rigorous

The report proposes pre-test/post-test evaluation, but it does not specify exact outcome measures, scoring, comparison group options, delayed follow-up, or what counts as practical improvement.

Why it matters: The module development claim requires a measurable evaluation design, not only content descriptions.

Fix later:

- Add pre/post outcomes for scam cue detection, safe scenario response, self-efficacy, response efficacy, reporting intention, reporting speed, and recovery-scam resistance.
- Include scenario scoring rules: safe, partially safe, risky compliance.
- Add a delayed follow-up as optional but recommended.
- If no control group is feasible, say so and frame the evaluation as quasi-experimental or pre-experimental.

### Medium 8: Malaysia specificity is strong in examples but weak in citation mechanics

The report names PDRM, BNM, LHDN, MCMC, JPJ, SC, NSRC, Semak Mule, and Malaysian scam types, but many statements are not tied to precise source entries.

Why it matters: Local naming helps authenticity, but research validity requires traceable citations.

Fix later:

- Use `research_evidence_matrix.md` to attach evidence IDs to claims before rewriting.
- Keep Cyber999 counts separate from PDRM crime statistics.
- Use SC sources for investment scam claims, Cyber999/MyCERT for phishing/APK/cyber incident claims, NSRC/MOF/BNM for reporting and blocked transaction claims, and PDRM for Semak Mule/mule accounts.

### Medium 9: Official response tools are listed but not operationalized

The report mentions NSRC, Semak Mule, Cyber999, and SC checks, but the methodology does not yet test whether respondents can choose and use the right tool.

Why it matters: A person may know a tool exists but fail to use it under pressure, which is exactly the behavioural gap this study claims to address.

Fix later:

- Add tool-use capability items.
- Add scenario decisions requiring the respondent to select the correct channel:
  - NSRC/bank hotline for active fund transfer,
  - Semak Mule for suspicious account/phone/company,
  - SC Investment Checker/Investor Alert List for investment entity,
  - Cyber999/MyCERT for cyber incident reporting,
  - PDRM report for crime record/investigation.

### Medium 10: Recovery scam and shame are under-supported in the current draft

Chapter 4 includes recovery, social support, and revictimization resistance, which is good, but the draft does not yet provide enough evidence or measurement items for shame, reporting reluctance, and fake recovery/support scams.

Why it matters: This is the most revictimization-specific part of the project. If weak, the project becomes a general scam-prevention study.

Fix later:

- Use SC clone-firm victim non-cooperation as evidence of reporting/cooperation friction without assuming motive.
- Use PDRM/Bernama fake NSRC account warning as evidence that recovery/help channels can be impersonated.
- Add direct items on embarrassment, self-blame, help-seeking, delayed reporting, repeated contact, and willingness to pay recovery fees.

## Evidence-Backed Strengths

The report should keep these elements:

- The topic is genuinely Malaysia-relevant because official and regulatory evidence shows active local scam infrastructure, localized phishing themes, NSRC/Semak Mule/NFP response tools, investment scam enforcement, and malicious APK patterns.
- The theory integration is appropriate. TPB explains intention and social norms; PMT explains threat/coping appraisal and self-efficacy; Cognitive Appraisal Theory explains real-time interpretation under pressure.
- Scenario-based assessment is a strong methodological choice because Malaysian scam cues are contextual and emotional.
- The proposed intervention modules are directionally sound, especially the move from awareness to cue detection, coping appraisal, reporting routines, and recovery resistance.

## Required Later Chapter Actions

Do not rewrite the chapters until these audit tasks are accepted. When rewriting begins, apply the following order:

1. Fix Chapter 1 definitions: cyber fraud, prior victim, repeat victimization, revictimization tendency, and intervention target.
2. Rebuild Chapter 2 evidence with source IDs from `reference_new_live.md` and raw evidence from `research_evidence_matrix.md`.
3. Replace generic behavioural-factor discussion with the seven-factor taxonomy in `task_2.md`.
4. Rebuild the Malaysia trend table using only verified, compatible statistics.
5. Update Chapter 3 with sampling quotas/subgroups, instrument constructs, scenario scoring, and ethical safeguards.
6. Update Chapter 4 module mapping so every module maps to the seven factors, Malaysian sources, and measurable outcomes.
7. Decide the five-chapter versus six-chapter structure and complete Chapter 6 if the UTM template is followed.
8. Rebuild the final reference list in one consistent author-date style.

## Minimum Acceptance Criteria Before Rewriting

The report should not be considered research-ready until all of the following are true:

- Every major Malaysia trend statistic has a checked source and a caveat if needed.
- Every in-text citation appears in the reference list and every reference is used.
- The seven-factor model is explicitly defined and appears consistently in literature review, methodology, and module design.
- Prior victimization and repeat victimization are measurable survey variables.
- Scenario tasks include local scams: PDRM/LHDN/MCMC/BNM/NSRC impersonation, phishing/smishing, traffic summons, government aid, delivery/e-wallet, investment Telegram/crypto, job/task scam, love/parcel scam, malicious APK, and recovery scam.
- The intervention evaluation distinguishes confidence, intention, scenario performance, reporting speed, and recovery-scam resistance.
- Chapter structure matches the selected thesis template.

## Final Audit Conclusion

This report can become a solid Malaysia-centric study, but it is not ready as a research-valid submission in its current state. The project should move forward by treating revictimization as the measurable research gap, not as an already-proven conclusion. The best next move is to rewrite the chapters around the seven-factor taxonomy, verified Malaysian evidence, and a methodology that can actually detect repeat-victim risk and intervention impact.

