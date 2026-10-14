# Setup Guide: Google Forms → Google Sheets

## A. Create the registration form
1. Open Google Forms and create a blank form.
2. Title it **Student Registration Form — Practical 31**.
3. Add these fields:
   - **Name** — Short answer — Required.
   - **Email** — Short answer — Required. Open the question menu and configure response validation for an email address if the option is available.
   - **Course** — Dropdown — Required. Add suitable options, for example `BCA`, `B.Com`, and `B.Sc. IT`. Replace these with the courses relevant to your institute.
4. Add a short description explaining that the form is for a student registration workflow.
5. Keep access settings appropriate for your classroom. Do not collect unnecessary personal information.

## B. Link responses to Google Sheets
1. Open the form's **Responses** tab.
2. Select the green Google Sheets icon / **Link to Sheets** option.
3. Create a new spreadsheet named **Practical 31 — Student Registrations**.
4. Submit one test response.
5. Open the linked spreadsheet and confirm that the response appears as a new row with the Name, Email, and Course values.

## C. Check for missing values
Google Forms required fields should prevent most blank submissions. Still check the spreadsheet for imported, manually edited, or older records that have blanks.

If columns are:
- A = Timestamp
- B = Name
- C = Email
- D = Course

Add a helper column E named `Record Check`. In E2, enter:

```excel
=IF(OR(B2="",C2="",D2=""),"MISSING FIELD","Complete")
```

Fill the formula down the column.

## D. Check for duplicate email addresses
Add a helper column F named `Duplicate Check`. In F2, enter:

```excel
=IF(C2="","Missing email",IF(COUNTIF($C$2:C2,C2)>1,"DUPLICATE EMAIL","Unique"))
```

Fill the formula down. The first occurrence is marked `Unique`; later occurrences of the same email are flagged `DUPLICATE EMAIL`.

If your sheet uses different columns, adjust the formula references accordingly. Formula separators may differ by spreadsheet locale.

## E. Test the workflow
Use fictional test data from `../data/sample_submissions.csv`. Submit the valid cases through the form. For invalid cases, try submitting a blank required field or malformed email and confirm that validation blocks it. To test duplicate detection, submit the same email twice if your form settings allow it, then check the helper column.

If Google Forms blocks a test before submission, record the result as **Blocked by form validation** rather than expecting a row in Sheets.

## F. Capture evidence
Take screenshots of:
1. Form fields and required settings.
2. A successful submission confirmation.
3. The corresponding row in the linked Sheet.
4. The helper columns flagging duplicates or missing values.

Blur or replace real personal information before adding screenshots to a public repository.
