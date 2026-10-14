"""Input validation helpers for Practical 36."""

MAX_PROMPT_LENGTH = 4000


def validate_prompt(prompt: str) -> str:
    """Trim and validate user input before any API request."""
    cleaned = prompt.strip()
    if not cleaned:
        raise ValueError("Prompt cannot be empty. Please type a question or task.")
    if len(cleaned) > MAX_PROMPT_LENGTH:
        raise ValueError(
            f"Prompt is too long ({len(cleaned)} characters). "
            f"Please keep it under {MAX_PROMPT_LENGTH} characters."
        )
    return cleaned
