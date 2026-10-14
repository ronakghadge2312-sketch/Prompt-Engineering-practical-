# Practical 32: AI Email Draft Generator

**Student Name:** [Enter Your Name]  
**GRID Number:** [Enter Your GRID Number]  
**Module:** AI Automation & Workflow Integration  
**Practical:** 32 — AI Email Draft Generator

## 1. Problem Statement
Students sometimes miss project submission deadlines because they overlook reminders or are unsure about the next steps. This practical uses an AI tool to prepare a polite reminder email from a supplied situation. The AI must include a subject, a deadline placeholder, and clear next steps. The email must **not** be sent automatically; a person must review it first.

## 2. Objectives
- Use a structured prompt to generate a professional email draft.
- Include a subject line, deadline placeholder, and clear next steps.
- Review the draft for tone, accuracy, missing information, and invented details.
- Keep the final sending decision with a human reviewer.

## 3. Tools and Integrations
- **ChatGPT or another approved AI tool:** generates the email draft.
- **Text editor / Markdown:** stores the prompt, draft, and review notes.
- **GitHub:** stores the practical documentation and test cases.

This is a prompt-based AI exercise. It does not connect to an email account and does not send messages.

## 4. Workflow Diagram
See [`docs/workflow_diagram.mmd`](docs/workflow_diagram.mmd).

**Workflow:** Situation provided → Check required information → Submit approved prompt to AI → Generate draft → Human reviews subject, deadline placeholder, tone, and next steps → Revise if needed → Approve draft for manual use. No automatic sending step is included.

## 5. Required Prompt
Use the prompt supplied in the practical:

> Act as a professional communication assistant. Draft a polite email to a student reminding them to submit their project. Include a subject, deadline placeholder, and clear next steps. Do not send the email.

The prompt is saved in [`docs/prompt_and_sample.md`](docs/prompt_and_sample.md).

## 6. Sample Situation and AI Draft
A sample situation and example output are included in [`docs/prompt_and_sample.md`](docs/prompt_and_sample.md). The deadline is deliberately shown as `[Insert Deadline]`; do not replace it with an invented date. The example is a demonstration draft, not a sent email.

## 7. Human Review Checklist
Before using the draft, the reviewer should check:
- [ ] Subject clearly states that this is a project submission reminder.
- [ ] Greeting and tone are polite and professional.
- [ ] Deadline remains a placeholder until the correct deadline is confirmed.
- [ ] Next steps are clear (complete the project, review requirements, submit through the specified channel).
- [ ] No unsupported policies, penalties, dates, links, or claims were invented.
- [ ] Student name, project name, and submission method are correct if added.
- [ ] The message has not been sent automatically.
- [ ] A teacher or authorized person approves it before manual sending.

## 8. Test Cases and Results
See [`data/test_cases.csv`](data/test_cases.csv). The tests check the required subject, deadline placeholder, next steps, polite tone, unsupported details, and the no-send rule.

## 9. Error Handling
- **Missing deadline:** keep `[Insert Deadline]` and ask the human reviewer to confirm it.
- **Missing project or student details:** use neutral wording or visible placeholders; do not guess.
- **Incorrect or invented information:** remove it and regenerate or edit the draft.
- **Unprofessional tone:** revise the prompt or edit the draft before approval.
- **Accidental sending risk:** do not connect an email-sending action; copy the reviewed draft manually only after authorization.
- **AI output misses a requirement:** compare it against the checklist and regenerate or edit it.

## 10. Security and Privacy
- Use fictional names and sample details in this public repository.
- Do not paste private student records or confidential institute information into an AI tool unless approved.
- Do not include passwords, access tokens, or private email addresses in the repository.
- Keep human review before sending; the AI draft is a suggestion, not an automatically approved communication.
- Share the repository without private email account credentials or message links.

## 11. Evidence / Demonstration Checklist
Create genuine screenshots after running the prompt in your chosen AI tool:
- `screenshots/01_prompt.png` — the prompt entered into the AI tool.
- `screenshots/02_generated_draft.png` — the generated email draft.
- `screenshots/03_human_review.png` — the checklist showing what you verified or corrected.

Do not fabricate screenshots. Hide private information before uploading evidence.

## 12. Conclusion
This practical demonstrates how AI can assist with routine communication by preparing a polite project reminder. A structured prompt helps produce a consistent draft, while a human reviewer checks facts, tone, placeholders, and next steps. The workflow intentionally stops before sending the email, ensuring that a person retains control over the final communication.

## 13. Learning Outcomes
- Learned to write and use a task-specific AI prompt.
- Generated an email draft with a subject, deadline placeholder, and next steps.
- Practised verifying AI-generated text.
- Understood why human approval and privacy matter in AI-assisted communication.

---
**Before submission:** Replace the student placeholders, run the prompt, review the output, add real screenshots, and upload the project folder to GitHub.
