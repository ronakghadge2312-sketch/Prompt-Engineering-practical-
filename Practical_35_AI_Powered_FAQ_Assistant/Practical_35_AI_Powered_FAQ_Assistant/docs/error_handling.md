# Error-Handling Approach

- **Empty question:** ask the user to enter a question.
- **Unsupported question:** return the fixed fallback and recommend confirmation with the institute office.
- **Missing FAQ file:** show a clear setup error and stop safely.
- **Invalid JSON:** explain that the FAQ file format must be corrected.
- **Malformed FAQ entry:** validate required `question`, `answer`, and `keywords` fields.
- **Weak or ambiguous match:** use the fallback rather than guessing. The keyword matching is a simple demo, so results should be manually checked.
- **Incorrect answer found:** correct the source FAQ and rerun the test cases; do not patch in an unsupported policy.
