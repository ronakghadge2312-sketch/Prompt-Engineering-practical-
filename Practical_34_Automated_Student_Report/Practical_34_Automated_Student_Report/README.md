# Practical 34: Automated Student Report

**Student Name:** [Enter Your Name]  
**GRID Number:** [Enter Your GRID Number]  
**Module:** AI Automation & Workflow Integration  
**Practical:** 34 — Automated Student Report

## 1. Problem Statement
Preparing student performance reports manually can take time and lead to calculation mistakes. This practical uses a sample dataset containing student names and marks, calculates totals and percentages using reliable arithmetic, prepares a summary of overall performance, and flags incomplete records for manual checking.

## 2. Objectives
- Read student names and subject marks from a CSV dataset.
- Calculate totals, averages, and percentages with fixed formulas.
- Summarize aggregate performance with AI-assisted language.
- Generate a report with key findings and student results.
- Flag missing or incomplete records rather than guessing missing marks.

## 3. Tools and Integrations
- **CSV dataset:** sample student names and marks.
- **Spreadsheet / CSV reader:** structured data input and review.
- **Python or spreadsheet formulas:** deterministic calculations.
- **ChatGPT or another approved AI tool:** summarize calculated findings in plain language.
- **GitHub:** version-control and submission of project documentation.

This repository includes a sample dataset, calculated output, report, workflow diagram, and test cases. The records are fictional. The arithmetic results are calculated from the included dataset; if you use a separate AI tool to generate a summary, capture genuine evidence and compare it with these calculations.

## 4. Workflow Diagram
See [`docs/workflow_diagram.mmd`](docs/workflow_diagram.mmd).

**Workflow:** Read dataset → Validate required fields and marks → Calculate totals and percentages using formulas → Exclude and flag incomplete records → Summarize complete-record results → Generate report → Human verifies findings.

## 5. Dataset and Calculation Rules
Input file: [`data/sample_student_marks.csv`](data/sample_student_marks.csv)

Subjects: Maths, English, Computer. Each subject is out of 100.

- **Total** = Maths + English + Computer
- **Percentage** = Total ÷ 300 × 100
- **Average mark** = Total ÷ 3

A blank mark is treated as missing, not zero. Incomplete records are flagged and excluded from aggregate calculations until the source value is verified.

## 6. Outputs
- [`data/calculated_results.csv`](data/calculated_results.csv) — totals, percentages, averages, and record status.
- [`reports/student_performance_report.md`](reports/student_performance_report.md) — key findings, subject averages, student results, AI-style summary, and incomplete-record notes.
- [`data/test_cases.csv`](data/test_cases.csv) — test cases and expected behavior.
- [`docs/ai_summary_prompt.md`](docs/ai_summary_prompt.md) — prompt for summarizing verified calculations.

## 7. Test Cases and Results
See [`data/test_cases.csv`](data/test_cases.csv). The tests cover valid records, missing marks, arithmetic checks, and whether incomplete records are excluded from the aggregate summary.

## 8. Error Handling
- **Missing marks:** flag for manual checking; never assume zero.
- **Invalid marks:** check that each provided mark is numeric and between 0 and 100.
- **Missing student name or ID:** flag the record as incomplete.
- **Calculation mismatch:** recalculate with fixed formulas and compare with the source data.
- **AI summary conflicts with figures:** trust verified calculations, correct the summary, and document the correction.
- **Incomplete report:** do not finalize until required fields and calculations have been reviewed.

## 9. Security and Privacy
- Use fictional sample student records in the public repository.
- Do not publish real student marks, IDs, or identifying details.
- Restrict real datasets and reports to authorized people.
- Share aggregate findings where possible rather than personal records.
- Do not rely on AI to invent missing marks or make consequential decisions about students.

## 10. Evidence / Demonstration Checklist
Add genuine screenshots after opening the dataset and reviewing the output:
- `screenshots/01_sample_dataset.png` — input marks dataset.
- `screenshots/02_calculated_results.png` — totals and percentages.
- `screenshots/03_performance_report.png` — generated report and key findings.
- `screenshots/04_incomplete_record_flag.png` — missing mark flagged for manual checking.

Do not fabricate screenshots. Hide personal information if you replace the fictional dataset with real data.

## 11. Conclusion
This practical demonstrates a reliable reporting workflow by separating numeric calculations from AI summarization. Complete records are calculated with fixed formulas, the report presents key findings, and incomplete records are flagged for manual verification. This supports accurate data processing and responsible use of AI.

## 12. Learning Outcomes
- Read and organize student data from CSV.
- Calculate totals, averages, and percentages reliably.
- Use AI to summarize verified performance statistics.
- Identify incomplete records and route them for manual checking.
- Apply validation, privacy, and human review.

---
**Before submission:** Replace student placeholders, inspect the included report and test cases, add genuine screenshots, and upload the complete folder to GitHub.
