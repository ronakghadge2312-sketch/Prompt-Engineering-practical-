"""
Practical 39: AI Workflow with Conditions
Categorizes support requests and applies conditional rules:
Urgent -> flag for human review
General -> prepare a standard response
Unclear -> ask for clarification
Invalid input -> return an error
"""
import json
import os
import sys
from dotenv import load_dotenv
from openai import (
    OpenAI, AuthenticationError, RateLimitError,
    APIConnectionError, APIStatusError, BadRequestError,
)

MAX_MESSAGE_LENGTH = 3000
ALLOWED_CATEGORIES = {"urgent", "general", "unclear"}

SYSTEM_PROMPT = """
You classify customer/student support messages.
Return only valid JSON with exactly these keys:
category: one of "urgent", "general", or "unclear"
summary: a brief summary based only on the message
reason: a short explanation of the classification
Do not invent facts. Use "urgent" only when the message clearly indicates a
time-sensitive problem, safety concern, service outage, or serious blockage
needing immediate human review. Use "general" for understandable ordinary
questions or requests. Use "unclear" when the message lacks enough information.
Do not make consequential decisions. A human must review urgent requests.
"""

def validate_message(message: str) -> str:
    cleaned = message.strip()
    if not cleaned:
        raise ValueError("Invalid input: message cannot be empty.")
    if len(cleaned) > MAX_MESSAGE_LENGTH:
        raise ValueError(f"Invalid input: message must be {MAX_MESSAGE_LENGTH} characters or fewer.")
    return cleaned

def classify_with_ai(message: str) -> dict:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY is missing. Configure it in your local .env file.")
    client = OpenAI(api_key=api_key)
    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    response = client.responses.create(model=model, instructions=SYSTEM_PROMPT, input=message)
    output = (response.output_text or "").strip()
    if not output:
        raise RuntimeError("The AI returned an empty response.")
    try:
        result = json.loads(output)
    except json.JSONDecodeError as error:
        raise RuntimeError("The AI returned invalid JSON. Please try again.") from error
    expected = {"category", "summary", "reason"}
    if not isinstance(result, dict) or set(result.keys()) != expected:
        raise RuntimeError("The AI response did not match the required JSON structure.")
    if result["category"] not in ALLOWED_CATEGORIES:
        raise RuntimeError("The AI returned an unexpected category.")
    if not all(isinstance(result[key], str) for key in expected):
        raise RuntimeError("The AI response contains invalid field types.")
    if not result["summary"].strip() or not result["reason"].strip():
        raise RuntimeError("The AI response has an empty summary or reason.")
    return result

def apply_rules(result: dict) -> dict:
    category = result["category"]
    if category == "urgent":
        return {
            "route": "human_review",
            "priority": "urgent",
            "action": "Flag for immediate human review. Do not send an automatic final answer.",
            "response": None,
        }
    if category == "general":
        return {
            "route": "standard_response",
            "priority": "normal",
            "action": "Prepare a standard response for the user.",
            "response": (
                "Thank you for contacting support. We have received your request. "
                "Please share any additional details if needed."
            ),
        }
    return {
        "route": "clarification",
        "priority": "needs_clarification",
        "action": "Ask the user to clarify the request.",
        "response": "Could you please provide a little more detail about your issue so we can help you?",
    }

def process_request(message: str) -> dict:
    valid_message = validate_message(message)
    classification = classify_with_ai(valid_message)
    decision = apply_rules(classification)
    return {
        "input": valid_message,
        "classification": classification,
        "workflow_decision": decision,
        "human_review_required": classification["category"] == "urgent",
    }

def main() -> int:
    load_dotenv()
    print("=" * 58)
    print("PRACTICAL 39: AI WORKFLOW WITH CONDITIONS")
    print("=" * 58)
    print("Enter a support request. Type EXIT to close.\n")
    while True:
        try:
            message = input("Support request: ")
        except (EOFError, KeyboardInterrupt):
            print("\nApplication closed.")
            return 0
        if message.strip().upper() == "EXIT":
            print("Goodbye!")
            return 0
        try:
            valid_message = validate_message(message)
        except ValueError as error:
            print(json.dumps({"status": "error", "message": str(error)}, indent=2))
            print()
            continue
        print("\nProcessing request...")
        try:
            result = process_request(valid_message)
            print("\n--- WORKFLOW RESULT ---")
            print(json.dumps(result, indent=2, ensure_ascii=False))
            print("\nA human should verify AI classification before acting on important requests.\n")
        except EnvironmentError as error:
            print(f"\nConfiguration error: {error}\n")
            return 1
        except AuthenticationError:
            print("\nAuthentication error: check the API key in your local .env file.\n")
        except RateLimitError:
            print("\nRate limit or quota error: check API usage and account limits.\n")
        except APIConnectionError:
            print("\nConnection error: check internet access and try again.\n")
        except BadRequestError:
            print("\nThe API rejected the request. Check the model and input.\n")
        except APIStatusError as error:
            print(f"\nAPI error: service returned HTTP status {error.status_code}.\n")
        except RuntimeError as error:
            print(f"\nOutput error: {error}\n")
        except Exception as error:
            print(f"\nUnexpected error. Error type: {type(error).__name__}\n")

if __name__ == "__main__":
    sys.exit(main())
