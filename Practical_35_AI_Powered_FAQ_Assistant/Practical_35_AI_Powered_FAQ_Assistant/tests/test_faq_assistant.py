import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from app import answer_question, load_faqs, FALLBACK

class FAQAssistantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.faqs = load_faqs()

    def test_contact_question(self):
        answer = answer_question("How do I contact the institute?", self.faqs)
        self.assertIn("official contact details", answer)

    def test_timetable_question(self):
        answer = answer_question("Where can I find the course timetable?", self.faqs)
        self.assertIn("timetable", answer.lower())

    def test_assignment_question(self):
        answer = answer_question("Where do I get assignment instructions?", self.faqs)
        self.assertIn("assignment instructions", answer.lower())

    def test_unknown_policy_not_invented(self):
        answer = answer_question("Is attendance below 60 percent allowed?", self.faqs)
        self.assertEqual(answer, FALLBACK)

    def test_empty_input(self):
        answer = answer_question("   ", self.faqs)
        self.assertIn("Please enter a question", answer)

if __name__ == "__main__":
    unittest.main()
