import unittest
from app import validate_transcript, MAX_TRANSCRIPT_LENGTH


class TranscriptValidationTests(unittest.TestCase):
    def test_valid_transcript_is_trimmed(self):
        self.assertEqual(validate_transcript("  Discuss project status  "), "Discuss project status")

    def test_empty_transcript_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_transcript("   ")

    def test_oversized_transcript_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_transcript("x" * (MAX_TRANSCRIPT_LENGTH + 1))


if __name__ == "__main__":
    unittest.main()
