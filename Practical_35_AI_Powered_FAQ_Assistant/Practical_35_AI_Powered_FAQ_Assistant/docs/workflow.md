# Workflow Diagram

```mermaid
flowchart TD
    A[Start] --> B[Load supplied FAQ JSON]
    B --> C[Accept user question]
    C --> D{Question empty?}
    D -- Yes --> E[Ask user to enter a question]
    E --> C
    D -- No --> F[Compare question with FAQ questions and keywords]
    F --> G{Relevant FAQ above threshold?}
    G -- Yes --> H[Return answer from matched FAQ]
    G -- No --> I[Say information is unavailable; do not guess]
    H --> J{User typed exit?}
    I --> J
    J -- No --> C
    J -- Yes --> K[End]
```

## Workflow Explanation
1. The application loads the FAQ list from `data/faqs.json`.
2. The user types a question.
3. The program compares words in the question with each FAQ question and its keywords.
4. If the best match reaches the configured threshold, it returns that FAQ's stored answer.
5. If no relevant match is found, it returns a safe fallback and directs the user to verify with the institute office.
6. The program does not create new institute rules or policies.
