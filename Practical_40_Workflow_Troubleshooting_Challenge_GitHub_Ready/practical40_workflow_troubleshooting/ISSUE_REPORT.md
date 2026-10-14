# Troubleshooting Report — Practical 40

**Student Name:** `[Enter your full name]`  
**GRID Number:** `[Enter your GRID number]`

| No. | Failure observed | Cause | Implemented correction | Evidence / test |
|---:|---|---|---|---|
| 1 | Missing email address | Contact field absent/invalid | Email validation before processing | `test_missing_email` |
| 2 | Incorrect JSON format | AI output is not valid JSON | Guarded JSON parsing | `test_malformed_json_rejected` |
| 3 | Invalid API key | Missing/placeholder key | Stop at configuration check; keep real keys secret | `test_invalid_key` |
| 4 | Duplicate form submission | Same ID processed twice | Check unique submission ID | `test_duplicate_submission` |
| 5 | Failed network request | Request fails transiently or repeatedly | Retry up to three times | `test_network_retry_then_success`, `test_network_failure_after_retries` |
| 6 | Unexpected AI category | Model output outside allowlist | Reject unsupported category | `test_unexpected_category` |

Add your own observations and screenshot filenames after executing the program and tests.
