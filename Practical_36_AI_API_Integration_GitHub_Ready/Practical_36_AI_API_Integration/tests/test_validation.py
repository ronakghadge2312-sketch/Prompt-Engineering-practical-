import unittest
from validation import validate_prompt, MAX_PROMPT_LENGTH


class PromptValidationTests(unittest.TestCase):
    def test_valid_prompt_is_trimmed(self):
        self.assertEqual(validate_prompt("  Explain APIs simply  "), "Explain APIs simply")

    def test_empty_prompt_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_prompt("   ")

    def test_too_long_prompt_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_prompt("x" * (MAX_PROMPT_LENGTH + 1))


if __name__ == "__main__":
    unittest.main()
