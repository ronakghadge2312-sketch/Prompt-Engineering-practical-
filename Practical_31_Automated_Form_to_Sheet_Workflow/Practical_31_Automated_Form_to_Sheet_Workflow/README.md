# Practical 31: Automated Form-to-Sheet Workflow

**Student Name:** [Enter Your Name]  
**GRID Number:** [Enter Your GRID Number]  
**Module:** AI Automation & Workflow Integration  
**Practical:** 31 — Automated Form-to-Sheet Workflow

## 1. Problem Statement
Student registration details are often collected manually, which can lead to missing information, typing mistakes, and duplicate entries. This workflow collects each student's name, email address, and course through Google Forms and automatically stores each submission in a linked Google Sheet. The sheet is then checked for missing fields and duplicate email addresses.

## 2. Objectives
- Create a registration form with **Name**, **Email**, and **Course** fields.
- Collect sample student submissions.
- Verify that form responses appear correctly in Google Sheets.
- Identify missing information and duplicate email addresses.
- Document validation, error handling, privacy, and test results.

## 3. Tools and Integrations
- **Google Forms:** collects registration information.
- **Google Sheets:** stores form responses in rows.
- **Google Forms → Google Sheets integration:** sends each submitted response to the linked spreadsheet.
- **GitHub:** stores the practical documentation, sample data, test cases, and workflow diagram.

> This repository includes a ready-to-follow implementation guide and sample test data. The live Google Form and Sheet must be created in your own Google account; no account connection is created by this repository.

## 4. Workflow Diagram
See [`docs/workflow_diagram.mmd`](docs/workflow_diagram.mmd).

**Workflow:**  
Student opens form → Enters details → Required-field/email validation → Submits form → Google Sheets records response → Check missing/duplicate entries → Correct or flag exceptions → Verify results.

## 5. Implementation
Follow [`docs/setup_guide.md`](docs/setup_guide.md) to create the Google Form and link it to a spreadsheet.

Recommended form fields:
1. **Name** — Short answer, required.
2. **Email** — Short answer, required; enable email validation if available.
3. **Course** — Dropdown, required; add the courses offered by your institute.

## 6. Sample Inputs and Expected Data
Sample records are provided in [`data/sample_submissions.csv`](data/sample_submissions.csv). They include valid examples plus records intentionally used to test duplicate detection and missing-field handling. Do not treat this sample CSV as proof of a live Google Sheets connection.

## 7. Test Cases and Results
See [`data/test_cases.csv`](data/test_cases.csv) for test inputs, expected behavior, and demonstration results.

Summary:
- Valid registration: should be accepted and appear as a new row.
- Missing name/email/course: should be blocked by required-field validation; if a row is imported or entered manually, flag it during sheet review.
- Invalid email: should be rejected by email validation where configured.
- Duplicate email: Google Forms does not automatically guarantee unique email addresses in every setup. Detect duplicates in Google Sheets and flag them for manual review.
- Sheet/link failure: verify the response destination and retry after restoring access; do not claim success until the row is visible.

## 8. Error Handling
- **Missing fields:** mark each field as required in Google Forms; check the sheet for blank cells.
- **Invalid email:** enable response validation for an email format where available; manually review suspicious entries.
- **Duplicate submissions:** use a duplicate-check formula or conditional formatting in Google Sheets; flag duplicates rather than silently deleting records.
- **Response not saved:** confirm the form is accepting responses and the linked response sheet is correct; submit a test record and verify the row.
- **Unexpected course value:** use a dropdown rather than free text to limit inconsistent course names.

## 9. Security and Privacy
- Collect only information needed for registration.
- Use fictional sample data in the public GitHub repository; do not upload real student personal information.
- Restrict Google Form and Sheet access to authorized people.
- Do not publish the live spreadsheet or expose private response links in this repository.
- Review and remove test records before using the workflow for real registrations.
- Use institutional guidance for data retention and consent.

## 10. Evidence / Demonstration Checklist
Before submitting, add your own screenshots to `screenshots/` (create this folder if needed):
- `01_google_form.png` — the form showing Name, Email, and Course.
- `02_sample_submission.png` — a successful test submission (hide any personal details).
- `03_google_sheet_responses.png` — the response row visible in Google Sheets.
- `04_duplicate_missing_check.png` — the sheet showing how duplicates or missing values are flagged.

**Important:** Screenshots are intentionally not fabricated. Capture them after you create and test your own Google Form and Sheet.

## 11. Conclusion
This practical demonstrates how Google Forms and Google Sheets can automate data collection. The linked sheet provides a central place to review submissions, while required fields, email validation, dropdown choices, and duplicate checks improve data quality. Verification and human review remain important because form-to-sheet automation does not by itself guarantee that every record is complete or unique.

## 12. Learning Outcomes
- Understood a trigger-and-action workflow.
- Created a form for structured data collection.
- Connected a form to a spreadsheet.
- Practised checking missing fields and duplicate email addresses.
- Learned the importance of verification, error handling, and privacy.

---
**Submission reminder:** Replace the student placeholders, create the live form and sheet, run the test cases, and add real screenshots before submitting.
