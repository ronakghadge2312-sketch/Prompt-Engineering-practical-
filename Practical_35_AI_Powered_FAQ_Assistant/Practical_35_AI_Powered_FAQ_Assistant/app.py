"""Practical 35: FAQ assistant grounded in a local JSON knowledge base."""
import json
import re
from difflib import SequenceMatcher
from pathlib import Path

FAQ_PATH = Path(__file__).parent / "data" / "faqs.json"
FALLBACK = (
    "I couldn't find this information in the supplied FAQs. "
    "Please confirm with the institute office. I won't guess institute policy."
)

STOP_WORDS = {
    "a", "an", "the", "is", "are", "do", "does", "can", "i", "we", "you",
    "how", "what", "when", "where", "which", "to", "of", "for", "my", "your",
    "please", "tell", "me", "about", "could", "would", "be", "get", "in", "at"
}

def normalize(text):
    """Lowercase text and retain alphanumeric words."""
    return re.findall(r"[a-z0-9]+", text.lower())

def load_faqs(path=FAQ_PATH):
    """Load and validate FAQ entries from JSON."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("FAQ data must be a list.")
        for item in data:
            if not all(key in item for key in ("question", "answer", "keywords")):
                raise ValueError("Each FAQ must contain question, answer, and keywords.")
            if not isinstance(item["answer"], str) or not item["answer"].strip():
                raise ValueError("FAQ answers cannot be empty.")
        return data
    except FileNotFoundError as exc:
        raise RuntimeError(f"FAQ file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError("FAQ file is not valid JSON. Check commas and quotation marks.") from exc

def score_question(user_question, faq):
    """Score a question using keyword overlap and wording similarity."""
    user_words = {w for w in normalize(user_question) if w not in STOP_WORDS}
    faq_text = " ".join([faq["question"], *faq.get("keywords", [])])
    faq_words = {w for w in normalize(faq_text) if w not in STOP_WORDS}
    overlap = len(user_words & faq_words) / max(1, len(user_words))
    similarity = SequenceMatcher(None, " ".join(sorted(user_words)),
                                  " ".join(sorted(faq_words))).ratio()
    return max(overlap, similarity * 0.75)

def answer_question(user_question, faqs=None, threshold=0.28):
    """Return a verified FAQ answer or a safe fallback."""
    if not user_question or not user_question.strip():
        return "Please enter a question so I can check the supplied FAQs."
    if faqs is None:
        faqs = load_faqs()

    scored = [(score_question(user_question, faq), faq) for faq in faqs]
    if not scored:
        return FALLBACK
    best_score, best_faq = max(scored, key=lambda pair: pair[0])
    if best_score < threshold:
        return FALLBACK
    return f"According to the supplied FAQs: {best_faq['answer']}"

def main():
    print("=" * 54)
    print("WELCOME TO THE AI-POWERED FAQ ASSISTANT (DEMO)")
    print("Answers are limited to the supplied FAQ information.")
    print("Type 'exit' to close.")
    print("=" * 54)
    try:
        faqs = load_faqs()
    except RuntimeError as error:
        print(f"Setup error: {error}")
        return

    while True:
        try:
            question = input("\nYour question: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAssistant closed.")
            break
        if question.lower() == "exit":
            print("Goodbye!")
            break
        print("\nAssistant:", answer_question(question, faqs))

if __name__ == "__main__":
    main()
