import unittest
from unittest.mock import patch
from app import validate_message, apply_rules, process_request

class InputValidationTests(unittest.TestCase):
    def test_valid_message_is_trimmed(self):
        self.assertEqual(validate_message("  Need help with timetable  "), "Need help with timetable")

    def test_empty_message_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_message("   ")

    def test_overlong_message_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_message("x" * 3001)

class ConditionalRuleTests(unittest.TestCase):
    def test_urgent_goes_to_human_review(self):
        result = apply_rules({"category":"urgent","summary":"Portal is down","reason":"Time-sensitive outage"})
        self.assertEqual(result["route"], "human_review")
        self.assertIsNone(result["response"])

    def test_general_prepares_standard_response(self):
        result = apply_rules({"category":"general","summary":"Asks for timetable","reason":"Ordinary request"})
        self.assertEqual(result["route"], "standard_response")
        self.assertIsInstance(result["response"], str)

    def test_unclear_asks_for_clarification(self):
        result = apply_rules({"category":"unclear","summary":"Insufficient details","reason":"Issue is not explained"})
        self.assertEqual(result["route"], "clarification")
        self.assertIn("detail", result["response"].lower())

    @patch("app.classify_with_ai")
    def test_invalid_input_does_not_call_ai(self, mock_classifier):
        with self.assertRaises(ValueError):
            process_request(" ")
        mock_classifier.assert_not_called()

if __name__ == "__main__":
    unittest.main()
