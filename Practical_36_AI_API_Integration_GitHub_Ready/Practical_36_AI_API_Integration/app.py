"""
Practical 36: API Integration with AI
A beginner-friendly command-line app using the official OpenAI Python SDK.
"""

import os
import sys
from dotenv import load_dotenv
from validation import validate_prompt, MAX_PROMPT_LENGTH
from openai import (
    OpenAI,
    AuthenticationError,
    RateLimitError,
    APIConnectionError,
    APIStatusError,
    BadRequestError,
)

def generate_response(prompt: str) -> str:
    """Send a validated prompt to the official OpenAI Responses API."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "OPENAI_API_KEY was not found. Create a local .env file and add your API key."
        )

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model=model,
        instructions=(
            "You are a helpful educational assistant. Give clear, concise answers. "
            "If a request is unclear, ask a clarifying question. Do not invent facts."
        ),
        input=prompt,
    )

    answer = (response.output_text or "").strip()
    if not answer:
        raise RuntimeError("The API returned no text. Please try again.")
    return answer


def main() -> int:
    load_dotenv()

    print("=" * 54)
    print("PRACTICAL 36: API INTEGRATION WITH AI")
    print("=" * 54)
    print("Enter a prompt for the AI. Type 'exit' to close the app.\n")

    while True:
        try:
            prompt = input("Your prompt: ")
        except (EOFError, KeyboardInterrupt):
            print("\nApplication closed.")
            return 0

        if prompt.strip().lower() in {"exit", "quit"}:
            print("Goodbye!")
            return 0

        try:
            valid_prompt = validate_prompt(prompt)
        except ValueError as error:
            print(f"\nInput error: {error}\n")
            continue

        print("\nGenerating response... Please wait.")
        try:
            answer = generate_response(valid_prompt)
            print("\n--- AI RESPONSE ---")
            print(answer)
            print("-------------------\n")
        except EnvironmentError as error:
            print(f"\nConfiguration error: {error}\n")
            return 1
        except AuthenticationError:
            print(
                "\nAuthentication error: The API key may be invalid or expired. "
                "Check your local .env file; never publish the key.\n"
            )
        except RateLimitError:
            print(
                "\nRate limit or quota error: Check your API usage and billing limits, "
                "then try again later.\n"
            )
        except APIConnectionError:
            print(
                "\nConnection error: Check your internet connection and try again.\n"
            )
        except BadRequestError as error:
            print(f"\nInvalid API request: {error}\n")
        except APIStatusError as error:
            print(
                f"\nAPI error: The service returned HTTP status {error.status_code}. "
                "Please try again later or check the API documentation.\n"
            )
        except RuntimeError as error:
            print(f"\nResponse error: {error}\n")
        except Exception as error:
            # Keep the app running for unexpected errors without printing secrets.
            print(
                "\nUnexpected error occurred. Please try again. "
                f"Error type: {type(error).__name__}\n"
            )


if __name__ == "__main__":
    sys.exit(main())
