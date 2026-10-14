# Practical 33: Customer Feedback Classifier

**Student Name:** [Enter Your Name]  
**GRID Number:** [Enter Your GRID Number]  
**Module:** AI Automation & Workflow Integration  
**Practical:** 33 — Customer Feedback Classifier

## 1. Problem Statement
Customer feedback can describe delivery problems, technical problems, or billing issues. Sorting each message manually takes time and can result in inconsistent labels. This practical defines a simple workflow that classifies feedback into one of three categories: **Delivery**, **Technical Support**, or **Billing**. The workflow is tested with both the examples supplied in the practical and new examples, and incorrect or uncertain classifications are flagged for human review.

## 2. Objectives
- Categorize customer feedback into the three required labels.
- Use a consistent prompt and structured output.
- Test the classifier using new examples.
- Identify incorrect or uncertain classifications.
- Apply human review and document limitations.

## 3. Tools Used
- **ChatGPT or another approved AI tool:** classifies each feedback message.
- **Markdown / text editor:** stores the prompt and sample results.
- **CSV files:** store test cases and expected labels.
- **GitHub:** stores project documentation and evidence.

This repository documents a prompt-based classifier. It does not connect to a live customer support platform or automatically route real customer messages.

## 4. Workflow Diagram
See [`docs/workflow_diagram.mmd`](docs/workflow_diagram.mmd).

**Workflow:** Receive feedback → Check that the message is not blank → Ask AI to choose exactly one category → Compare output with allowed labels → Review uncertain or mismatched results → Record the final label.

## 5. Category Definitions
- **Delivery:** Order not arrived, shipping delay, package tracking, or delivery damage.
- **Technical Support:** Application errors, crashes, login problems, or product/software malfunction.
- **Billing:** Duplicate charges, incorrect amount, refunds related to payment, or invoice/payment issues.

If a message clearly covers multiple issues or does not fit these categories, mark it **Needs Human Review** rather than inventing a fourth final category. The required classifier labels remain Delivery, Technical Support, and Billing.

## 6. Prompt Used
The full reusable prompt is in [`docs/classifier_prompt.md`](docs/classifier_prompt.md). It instructs the AI to return one allowed category and a short reason. For practical grading, the category must be one of the three required labels.

## 7. Supplied Examples
| Customer feedback | Expected category |
|---|---|
| My order has not arrived. | Delivery |
| The application crashes when I log in. | Technical Support |
| I was charged twice. | Billing |

## 8. New Examples and Test Results
See [`data/test_cases.csv`](data/test_cases.csv). It contains new messages for all three categories, plus ambiguous and empty-message checks. The expected categories are documented so that the AI output can be compared against them.

The example classifications in this repository are **illustrative expected results**, not proof that an external AI run has occurred. Run the prompt yourself and record any differences in the `Actual AI Output` and `Pass/Fail` columns.

## 9. Error Handling
- **Blank message:** do not classify; request feedback text.
- **Unexpected category:** normalize only if the intended category is clear; otherwise flag for review.
- **Wrong category:** compare the message with the category definitions, correct the label after review, and record the mismatch.
- **Ambiguous / multiple issues:** flag for human review instead of forcing an unreliable label.
- **AI response not in requested format:** ask the AI to return only the required structured fields.
- **AI unavailable:** keep the feedback in a pending state and retry later; do not lose the original message.

## 10. Security and Privacy
- Use fictional sample messages in the public repository.
- Remove names, phone numbers, order IDs, addresses, and other personal information before using real feedback in an AI tool.
- Do not upload private customer conversations to public GitHub.
- Do not include passwords, API keys, or support-platform credentials.
- Have a human review uncertain or high-impact cases before taking action.

## 11. Evidence / Demonstration Checklist
Add genuine screenshots after running the prompt:
- `screenshots/01_classifier_prompt.png` — prompt used.
- `screenshots/02_classification_results.png` — AI output for sample messages.
- `screenshots/03_error_review.png` — an incorrect, ambiguous, or invalid output and how it was reviewed.

Do not fabricate screenshots. Hide personal or confidential information before uploading evidence.

## 12. Conclusion
This practical demonstrates how AI can categorize customer feedback into Delivery, Technical Support, and Billing. Testing with new examples helps evaluate consistency, while comparison with expected labels reveals incorrect classifications. Input checks, structured output, and human review improve reliability; AI classifications should not be treated as infallible.

## 13. Learning Outcomes
- Learned to define categories and a reusable classification prompt.
- Tested the supplied examples and new customer feedback.
- Compared actual output with expected labels.
- Identified how to handle blank, ambiguous, and incorrectly classified messages.
- Understood the importance of privacy and human oversight.

---
**Before submission:** Replace student placeholders, run the prompt with the test messages, record actual results, add real screenshots, and upload the project folder to GitHub.
