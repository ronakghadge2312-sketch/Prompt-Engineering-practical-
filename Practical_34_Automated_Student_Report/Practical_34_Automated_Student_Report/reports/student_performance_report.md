# Automated Student Performance Report

**Dataset:** `data/sample_student_marks.csv`  
**Subjects:** Maths, English, Computer  
**Maximum marks per subject:** 100  
**Records received:** 8  
**Complete records included in calculations:** 7  
**Incomplete records flagged:** 1

## 1. Calculation Method
For complete records only:
- **Total** = Maths + English + Computer
- **Percentage** = Total ÷ 300 × 100
- **Average mark** = Total ÷ 3

Incomplete records are not included in totals, percentages, or subject averages. They are flagged for manual checking to avoid misleading calculations.

## 2. Key Findings
- Average percentage across the 7 complete records: **76.14%**.
- Average mark across all subject scores in complete records: **76.14/100**.
- Highest overall percentage: **Diya Shah (91.67%)**.
- Strongest average subject: **Computer (80.71/100)**.
- Lowest average subject: **Maths (71.86/100)**.
- One record requires manual checking because a subject mark is missing.

## 3. Subject Averages
| Subject | Average mark (complete records only) |
|---|---:|
| Maths | 71.86/100 |
| English | 75.86/100 |
| Computer | 80.71/100 |

## 4. Student Results
| Student ID | Student Name | Maths | English | Computer | Total / 300 | Percentage | Status |
|---|---|---:|---:|---:|---:|---:|---|
| S001 | Aarav Patel | 78 | 84 | 91 | 253 | 84.33% | Complete |
| S002 | Diya Shah | 92 | 88 | 95 | 275 | 91.67% | Complete |
| S003 | Kabir Mehta | 65 | 72 | 70 | 207 | 69.00% | Complete |
| S004 | Riya Desai | 55 | 61 | 68 | 184 | 61.33% | Complete |
| S005 | Neel Joshi | 81 | 77 | 86 | 244 | 81.33% | Complete |
| S006 | Meera Trivedi | — | 73 | 80 | — | — | **Incomplete — manual check** |
| S007 | Vivaan Shah | 44 | 58 | 62 | 164 | 54.67% | Complete |
| S008 | Anaya Patel | 88 | 91 | 93 | 272 | 90.67% | Complete |

## 5. AI-Generated Performance Summary
The complete records show varied student performance across the three subjects. Computer has the highest subject average in this sample, while Maths has the lowest average and may deserve additional review or support. Anaya Patel has the highest overall percentage among complete records. These observations describe this sample only and should not be treated as a judgment about students beyond the available marks.

## 6. Incomplete Record Requiring Manual Checking
- **Student ID:** S006
- **Student name:** Meera Trivedi
- **Issue:** Maths mark is missing.
- **Action:** Confirm the original mark sheet with the authorized teacher and update the dataset before calculating this student's total or percentage.

## 7. Validation and Error Handling
- Blank marks are treated as missing, not as zero.
- Incomplete rows are excluded from aggregate calculations.
- Calculations use fixed arithmetic formulas, not AI-generated estimates.
- The source dataset is preserved separately from calculated results.
- Any corrected value should be checked against the authorized original record and recalculated.

## 8. Security and Privacy
- The dataset uses fictional sample student records.
- Do not upload real student marks or identifiers to a public repository.
- Restrict access to actual student reports to authorized staff.
- Avoid placing personal data in screenshots or public issue trackers.

## 9. Conclusion
This workflow reads a sample marks dataset, calculates totals and percentages using deterministic arithmetic, uses AI to summarize aggregate performance, and flags incomplete records for human review. Separating calculation from AI summarization improves reliability and makes the report easier to verify.

## 10. Learning Outcomes
- Processed structured student data from CSV.
- Calculated totals, averages, and percentages using reliable formulas.
- Summarized overall performance in plain language.
- Identified incomplete data and flagged it for manual checking.
- Practised validation, privacy, and human oversight.
