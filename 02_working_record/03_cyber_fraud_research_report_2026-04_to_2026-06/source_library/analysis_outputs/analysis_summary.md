# Secondary Data And Chart Analysis Summary

Generated: 2026-07-04

## Files Created

- `datasets_raw/cyber999_quarterly_indicators_raw.csv`
- `datasets_clean/cyber999_quarterly_indicators_clean.csv`
- `datasets_raw/pdrm_officially_quoted_online_fraud_indicators_raw.csv`
- `datasets_clean/seven_factor_evidence_coverage.csv`
- `analysis_outputs/cyber999_total_vs_fraud_trend.svg`
- `analysis_outputs/cyber999_top_fraud_categories_q2_2025.svg`
- `analysis_outputs/seven_factor_evidence_coverage.svg`
- `analysis_outputs/malaysia_scam_response_tool_map.svg`

## Data Integrity Notes

- Cyber999 figures are handled incident reports, not all Malaysian police cases.
- PDRM case/loss figures are stored separately because the measurement unit is different.
- Q4 2025 Cyber999 currently contains a partial extracted fraud value and should be checked before full trend interpretation.
- The generated charts are descriptive secondary-data visuals. They are not survey or intervention results.

## Fraud Share Checks

| Period | Total | Fraud | Stated % | Computed % | Check |
|---|---:|---:|---:|---:|---|
| 2024 Q2 | 1481 | 947 | 63.94 | 63.94 | share check ok |
| 2024 Q4 | 1550 | 1108 | 71 | 71.48 | share check ok |
| 2025 Q1 | 1657 | 1126 | 68 | 67.95 | share check ok |
| 2025 Q2 | 2058 | 1633 | 80 | 79.35 | share check ok |
| 2025 Q3 | 2020 | 1521 | 75 | 75.30 | share check ok |
| 2025 Q4 | NA | 1471 | NA | NA | partial |
