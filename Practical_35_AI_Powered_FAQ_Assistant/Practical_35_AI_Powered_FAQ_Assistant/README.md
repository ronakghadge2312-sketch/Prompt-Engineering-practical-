# Practical 35: AI-Powered FAQ Assistant

**Student Name:** [Enter your name]  
**GRID Number:** [Enter your GRID number]  
**Subject/Journal:** AI Automation & Workflow Integration

## 1. Problem Statement
Create a simple FAQ assistant that accepts a user's question, finds a relevant answer from a supplied FAQ list, clearly says when the answer is unavailable, and does not invent institute policies.

## 2. Learning Outcomes
- Use a supplied knowledge base as context.
- Match questions to relevant FAQ entries.
- Handle unknown or unsupported questions safely.
- Verify answers against the source information.

## 3. Tools Used
- Python 3 (standard library)
- JSON for the FAQ knowledge base
- Terminal / IDLE / VS Code
- Optional: an AI model may be used with the grounding prompt in `docs/ai_prompt_template.md`. No API key or live AI integration is required for the included demo.

## 4. Project Structure
```text
Practical_35_AI_Powered_FAQ_Assistant/
├── README.md
├── app.py
├── data/
│   └── faqs.json
├── docs/
│   ├── workflow.md
│   ├── ai_prompt_template.md
│   ├── test_cases.md
│   ├── error_handling.md
│   └── security.md
├── tests/
│   └── test_faq_assistant.py
└── screenshots/
    └── README.md
```

## 5. How to Run
1. Install Python 3 if it is not already installed.
2. Extract the ZIP file.
3. Open a terminal in this project folder.
4. Run:
   ```bash
   python app.py
   ```
5. Ask one of the supplied questions, such as `How do I contact the institute?`.
6. Try an unsupported question, such as `Is attendance below 60% allowed?`. The assistant should say the information is not available instead of guessing.
7. Type `exit` to stop.

## 6. Sample Input and Output
**Input:** `How do I contact the institute?`  
**Expected output:** The supplied FAQ says: `Please contact the institute office using the official contact details provided by your department.`

**Input:** `Can I get a fee refund?`  
**Expected output:** `I couldn't find this information in the supplied FAQs. Please confirm with the institute office. I won't guess institute policy.`

## 7. Workflow Diagram
See [`docs/workflow.md`](docs/workflow.md).

## 8. Test Cases and Results
See [`docs/test_cases.md`](docs/test_cases.md). Run automated tests with:
```bash
python -m unittest discover -s tests -v
```
The tests check supported questions, paraphrased questions, and unsupported questions.

## 9. Error Handling
See [`docs/error_handling.md`](docs/error_handling.md). The program handles empty input, unknown questions, and a missing or invalid FAQ file with a clear message.

## 10. Security Considerations
See [`docs/security.md`](docs/security.md). Do not place passwords, private student data, or API keys in the FAQ file or public repository.

## 11. Screenshots / Demonstration
The `screenshots` folder contains instructions. Capture genuine screenshots on your own computer showing:
- The program starting.
- A supported question and answer.
- An unsupported question with the safe fallback.
- The test suite passing.

Screenshots are not fabricated or included as if a live system had been run.

## 12. Conclusion
This project demonstrates a context-based FAQ assistant. It uses only the supplied FAQ content, provides a fallback when the answer cannot be found, and avoids making up institute policies. The sample FAQs are illustrative and must be replaced with verified information supplied by the institute before real use.
