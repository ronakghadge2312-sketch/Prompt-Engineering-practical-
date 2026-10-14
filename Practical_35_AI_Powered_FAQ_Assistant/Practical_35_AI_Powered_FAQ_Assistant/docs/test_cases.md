# Test Cases and Results

These are expected results based on the illustrative FAQ entries in `data/faqs.json`. Run the program to confirm the actual output on your machine.

| ID | Input | Expected result | Status |
|---|---|---|---|
| TC01 | `How do I contact the institute?` | Returns the stored institute-contact answer | To verify |
| TC02 | `I need the office phone or email` | Returns contact answer if matching threshold is reached | To verify |
| TC03 | `Where is the course timetable?` | Returns timetable guidance | To verify |
| TC04 | `Where are my assignment instructions?` | Returns assignment guidance | To verify |
| TC05 | `How can I access notes and PDFs?` | Returns learning-material guidance | To verify |
| TC06 | `I cannot log in to the learning platform` | Returns login troubleshooting guidance | To verify |
| TC07 | Empty input | Asks the user to enter a question | To verify |
| TC08 | `Is attendance below 60 percent allowed?` | Safe fallback; no policy invented | To verify |
| TC09 | `Can I get a fee refund?` | Safe fallback; no refund policy invented | To verify |
| TC10 | `What is the institute's exam rechecking fee?` | Safe fallback; no fee invented | To verify |

## Result Recording
After running each test, replace `To verify` with `Pass` or `Fail` based on the actual output. If a paraphrased supported question is not matched, adjust the relevant keywords in `data/faqs.json` and rerun the tests. Never mark a test as passed without checking it.
