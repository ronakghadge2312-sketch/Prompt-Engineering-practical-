# Error Handling and Verification

## 1. Blank input
**Problem:** No customer feedback was provided.  
**Correction:** Stop the workflow and request the message text. Do not guess a category.

## 2. Incorrect category
**Problem:** The AI label does not match the meaning of the message.  
**Correction:** Compare the message with category definitions, flag it for human review, and record the corrected label.

## 3. Unexpected category name
**Problem:** The AI returns a label such as `Shipping`, which is not one of the three allowed categories.  
**Correction:** If the meaning is clearly delivery-related, a reviewer may map it to `Delivery`. If unclear, flag it for review. Keep final labels within the required categories.

## 4. Ambiguous message
**Problem:** A message contains two different issues, such as a late package and an application crash.  
**Correction:** Mark `Review needed: Yes`; a human can split the feedback into separate issues or choose the appropriate handling.

## 5. Invalid response format
**Problem:** The AI gives a paragraph instead of the requested fields.  
**Correction:** Ask it to return `Category`, `Reason`, and `Review needed` in the required format.

## 6. Verification method
For each test:
1. Paste the feedback into the prompt.
2. Record the actual AI output in `data/test_cases.csv`.
3. Compare it to the expected category.
4. Mark Pass or Fail.
5. For failures, note the cause and the correction.
