"""
Practical 38: AI Meeting Summary Workflow
A small command-line workflow that summarizes a supplied meeting transcript
using the official OpenAI API and displays structured output.
"""

import json
import os
import sys
from dotenv import load_dotenv
from openai import (
    OpenAI,
    AuthenticationError,
    RateLimitError,
    APIConnectionError,
    APIStatusError,
    BadRequestError,
)

MAX_TRANSCRIPT_LENGTH = 12000

SYSTEM_PROMPT = """
Summarize the meeting transcript provided by the user.
Return valid JSON with exactly these keys:
- main_discussion_points: an array of short strings
- decisions: an array of short strings
- action_items: an array of objects with task and responsible_role
- missing_information: an array of short strings for information not specified
Do not invent deadlines, decisions, names, or action items that are not in the transcript.
If a section has no supported items, return an empty array.
Use only the transcript as the source of meeting facts.
"""


def validate_transcript(transcript: str) -> str:
    cleaned = transcript.strip()
    if not cleaned:
        raise ValueError("Transcript cannot be empty. Paste a meeting transcript first.")
    if len(cleaned) > MAX_TRANSCRIPT_LENGTH:
        raise ValueError(
            f"Transcript is too long ({len(cleaned)} characters). "
            f"Please keep it under {MAX_TRANSCRIPT_LENGTH} characters."
        )
    return cleaned


def summarize_transcript(transcript: str) -> dict:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "OPENAI_API_KEY was not found. Copy .env.example to .env and configure your key."
        )

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=model,
        instructions=SYSTEM_PROMPT,
        input=transcript,
    )

    output_text = (response.output_text or "").strip()
    if not output_text:
        raise RuntimeError("The AI returned an empty response. Please try again.")

    try:
        data = json.loads(output_text)
    except json.JSONDecodeError as error:
        raise RuntimeError(
            "The AI response was not valid JSON. Try again or inspect the output."
        ) from error

    expected_keys = {
        "main_discussion_points",
        "decisions",
        "action_items",
        "missing_information",
    }
    if not isinstance(data, dict) or set(data.keys()) != expected_keys:
        raise RuntimeError("The AI response did not match the required JSON structure.")
    if not isinstance(data["main_discussion_points"], list):
        raise RuntimeError("Invalid output: main_discussion_points must be an array.")
    if not isinstance(data["decisions"], list):
        raise RuntimeError("Invalid output: decisions must be an array.")
    if not isinstance(data["action_items"], list):
        raise RuntimeError("Invalid output: action_items must be an array.")
    if not isinstance(data["missing_information"], list):
        raise RuntimeError("Invalid output: missing_information must be an array.")

    for item in data["action_items"]:
        if not isinstance(item, dict) or not isinstance(item.get("task"), str) or not isinstance(item.get("responsible_role"), str):
            raise RuntimeError("Invalid action item: each item must include task and responsible_role.")
    return data


def main() -> int:
    load_dotenv()
    print("=" * 58)
    print("PRACTICAL 38: AI MEETING SUMMARY WORKFLOW")
    print("=" * 58)
    print("Paste a meeting transcript. Enter a line containing only END when finished.")
    print("Type EXIT on the first line to close the app.\n")

    lines = []
    while True:
        try:
            line = input()
        except (EOFError, KeyboardInterrupt):
            print("\nApplication closed.")
            return 0

        if not lines and line.strip().upper() == "EXIT":
            print("Goodbye!")
            return 0
        if line.strip() == "END":
            break
        lines.append(line)

    try:
        transcript = validate_transcript("\n".join(lines))
    except ValueError as error:
        print(f"\nInput error: {error}")
        return 1

    print("\nSummarizing transcript... Please wait.")
    try:
        summary = summarize_transcript(transcript)
        print("\n--- STRUCTURED MEETING SUMMARY ---")
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        output_path = "meeting_summary.json"
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(summary, file, indent=2, ensure_ascii=False)
        print(f"\nSummary saved to: {output_path}")
        print("Review the summary for accuracy before sharing it.")
        return 0
    except EnvironmentError as error:
        print(f"\nConfiguration error: {error}")
        return 1
    except AuthenticationError:
        print("\nAuthentication error: check your API key in the local .env file.")
    except RateLimitError:
        print("\nRate limit or quota error: check API usage and account limits.")
    except APIConnectionError:
        print("\nConnection error: check your internet connection and try again.")
    except BadRequestError:
        print("\nThe API rejected the request. Check the model and input, then try again.")
    except APIStatusError as error:
        print(f"\nAPI error: service returned HTTP status {error.status_code}.")
    except RuntimeError as error:
        print(f"\nOutput error: {error}")
    except Exception as error:
        print(f"\nUnexpected error. Error type: {type(error).__name__}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
