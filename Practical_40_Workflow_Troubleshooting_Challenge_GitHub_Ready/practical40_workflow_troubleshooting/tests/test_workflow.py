import unittest
from app import parse_ai_json, process_submission, send_with_retry, valid_email


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.payload = {"submission_id": "FORM-1", "email": "learner@example.com", "message": "Help"}

    def test_valid_email(self):
        self.assertTrue(valid_email("learner@example.com"))
        self.assertFalse(valid_email(""))
        self.assertFalse(valid_email("not-an-email"))

    def test_malformed_json_rejected(self):
        with self.assertRaisesRegex(ValueError, "Incorrect JSON"):
            parse_ai_json("{category: urgent}")

    def test_unexpected_category_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unexpected AI category"):
            parse_ai_json('{"category":"maybe"}')

    def test_missing_email(self):
        payload = dict(self.payload, email="")
        result = process_submission(payload, "demo-key", '{"category":"general"}')
        self.assertEqual(result["stage"], "validation")

    def test_invalid_key(self):
        result = process_submission(self.payload, "invalid", '{"category":"general"}')
        self.assertEqual(result["stage"], "authentication")

    def test_duplicate_submission(self):
        seen = set()
        first = process_submission(self.payload, "demo-key", '{"category":"general"}', seen_ids=seen)
        second = process_submission(self.payload, "demo-key", '{"category":"general"}', seen_ids=seen)
        self.assertTrue(first["ok"])
        self.assertEqual(second["stage"], "deduplication")

    def test_network_retry_then_success(self):
        calls = {"count": 0}
        def request():
            calls["count"] += 1
            return calls["count"] >= 2
        self.assertTrue(send_with_retry(request, attempts=3))
        self.assertEqual(calls["count"], 2)

    def test_network_failure_after_retries(self):
        calls = {"count": 0}
        def request():
            calls["count"] += 1
            return False
        result = process_submission(self.payload, "demo-key", '{"category":"general"}', send_request=request)
        self.assertFalse(result["ok"])
        self.assertEqual(result["stage"], "delivery")
        self.assertEqual(calls["count"], 3)

    def test_correct_routing(self):
        result = process_submission(self.payload, "demo-key", '{"category":"urgent"}')
        self.assertEqual(result["route"], "human_review")


if __name__ == "__main__":
    unittest.main()
