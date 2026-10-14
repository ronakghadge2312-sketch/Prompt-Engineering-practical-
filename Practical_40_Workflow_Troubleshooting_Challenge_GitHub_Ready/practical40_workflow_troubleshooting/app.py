"""Practical 40: Workflow Troubleshooting Challenge.

A deterministic, offline-friendly workflow that diagnoses common automation failures
and demonstrates corrected handling. No real email or external API calls are made.
"""
from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, asdict
from typing import Any, Callable

ALLOWED_CATEGORIES = {"urgent", "general", "unclear"}


@dataclass
class Issue:
    name: str
    status: str
    cause: str
    correction: str


def valid_email(email: Any) -> bool:
    """Basic practical-level email validation; not a full RFC validator."""
    if not isinstance(email, str):
        return False
    email = email.strip()
    return bool(re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email))


def parse_ai_json(raw: str) -> dict[str, Any]:
    """Parse AI output and reject malformed JSON or unsupported categories."""
    try:
        value = json.loads(raw)
    except (json.JSONDecodeError, TypeError) as exc:
        raise ValueError("Incorrect JSON format from AI step") from exc
    if not isinstance(value, dict):
        raise ValueError("AI output must be a JSON object")
    category = value.get("category")
    if category not in ALLOWED_CATEGORIES:
        raise ValueError(f"Unexpected AI category: {category!r}")
    return value


def send_with_retry(request: Callable[[], bool], attempts: int = 3, delay: float = 0.0) -> bool:
    """Retry a transient network request a limited number of times."""
    if attempts < 1:
        raise ValueError("attempts must be at least 1")
    for attempt in range(attempts):
        try:
            if request():
                return True
        except (ConnectionError, TimeoutError):
            pass
        if attempt < attempts - 1 and delay > 0:
            time.sleep(delay)
    return False


def process_submission(payload: dict[str, Any], api_key: str | None,
                       ai_response: str, send_request: Callable[[], bool] | None = None,
                       seen_ids: set[str] | None = None) -> dict[str, Any]:
    """Run the corrected workflow on one submitted support request.

    This project simulates AI and delivery. It never sends an actual email or request.
    """
    if not isinstance(payload, dict):
        return {"ok": False, "stage": "input", "error": "Input must be a JSON object"}

    email = payload.get("email")
    if not valid_email(email):
        return {"ok": False, "stage": "validation", "error": "Missing or invalid email address"}

    request_id = payload.get("submission_id")
    if not isinstance(request_id, str) or not request_id.strip():
        return {"ok": False, "stage": "validation", "error": "submission_id is required"}
    if seen_ids is None:
        seen_ids = set()
    if request_id in seen_ids:
        return {"ok": False, "stage": "deduplication", "error": "Duplicate form submission ignored"}

    message = payload.get("message")
    if not isinstance(message, str) or not message.strip():
        return {"ok": False, "stage": "validation", "error": "Message is required"}

    if not isinstance(api_key, str) or not api_key.strip() or api_key.strip() in {"YOUR_API_KEY", "invalid", "INVALID_API_KEY"}:
        return {"ok": False, "stage": "authentication", "error": "Missing or invalid API key (simulated check)"}

    try:
        classification = parse_ai_json(ai_response)
    except ValueError as exc:
        return {"ok": False, "stage": "ai_output", "error": str(exc)}

    if send_request is None:
        send_request = lambda: True
    if not send_with_retry(send_request, attempts=3):
        return {"ok": False, "stage": "delivery", "error": "Network request failed after 3 attempts"}

    seen_ids.add(request_id)
    category = classification["category"]
    if category == "urgent":
        route = "human_review"
    elif category == "general":
        route = "standard_response"
    else:
        route = "clarification_required"
    return {"ok": True, "submission_id": request_id, "category": category,
            "route": route, "message": "Workflow completed (delivery simulated)"}


def run_challenge() -> list[Issue]:
    """Show deliberate fault examples, then the corrected diagnosis and fix."""
    return [
        Issue("Missing email address", "FIXED", "The form payload has no usable email, so a notification cannot be addressed.",
              "Validate the email before processing and return a clear validation error."),
        Issue("Incorrect JSON format", "FIXED", "The AI step returned text that cannot be parsed as JSON.",
              "Parse inside a guarded block; reject malformed output and log a safe error."),
        Issue("Invalid API key", "FIXED", "The configured key is missing or a placeholder/invalid value.",
              "Read the key from an environment variable, validate configuration, and never commit secrets."),
        Issue("Duplicate form submission", "FIXED", "The same submission ID is processed more than once.",
              "Track a unique submission ID and ignore duplicates; use persistent storage in production."),
        Issue("Failed network request", "FIXED", "A temporary network failure prevents delivery.",
              "Retry a limited number of times, then fail clearly instead of looping forever."),
        Issue("Unexpected AI category", "FIXED", "The model returned a category outside the allowed set.",
              "Validate against an allowlist (urgent/general/unclear) and route only validated values."),
    ]


def main() -> None:
    print("PRACTICAL 40 — WORKFLOW TROUBLESHOOTING CHALLENGE")
    print("Offline demo: failures are simulated; no external calls or emails are sent.\n")
    for issue in run_challenge():
        print(f"[{issue.status}] {issue.name}\n  Cause: {issue.cause}\n  Fix:   {issue.correction}\n")
    sample = {"submission_id": "FORM-1001", "email": "student@example.com",
              "message": "My account is locked and I need help."}
    result = process_submission(sample, "demo-key", '{"category":"urgent"}')
    print("Corrected workflow sample result:")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
