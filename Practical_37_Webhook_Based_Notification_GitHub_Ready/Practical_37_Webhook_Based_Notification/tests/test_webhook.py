import unittest
import app as webhook_app


class WebhookTests(unittest.TestCase):
    def setUp(self):
        webhook_app.app.config["TESTING"] = True
        self.client = webhook_app.app.test_client()
        webhook_app.processed_event_ids.clear()
        webhook_app.notifications.clear()

    def valid_event(self, event_id="test-event-001"):
        return {
            "event_id": event_id,
            "event": "student.registration.created",
            "student_name": "Aarav Patel",
            "course": "Generative AI",
        }

    def test_valid_event_creates_notification(self):
        response = self.client.post("/webhook/registration", json=self.valid_event())
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.get_json()["notification_created"])
        self.assertEqual(len(webhook_app.notifications), 1)

    def test_missing_student_name_is_rejected(self):
        event = self.valid_event()
        event["student_name"] = " "
        response = self.client.post("/webhook/registration", json=event)
        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.get_json()["notification_created"])
        self.assertEqual(len(webhook_app.notifications), 0)

    def test_duplicate_event_does_not_create_second_notification(self):
        event = self.valid_event()
        first = self.client.post("/webhook/registration", json=event)
        second = self.client.post("/webhook/registration", json=event)
        self.assertEqual(first.status_code, 201)
        self.assertEqual(second.status_code, 200)
        self.assertEqual(second.get_json()["status"], "duplicate_ignored")
        self.assertEqual(len(webhook_app.notifications), 1)

    def test_unsupported_event_is_rejected(self):
        event = self.valid_event()
        event["event"] = "student.deleted"
        response = self.client.post("/webhook/registration", json=event)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(webhook_app.notifications), 0)

    def test_non_json_request_is_rejected(self):
        response = self.client.post(
            "/webhook/registration",
            data="not json",
            content_type="text/plain",
        )
        self.assertEqual(response.status_code, 415)
        self.assertEqual(len(webhook_app.notifications), 0)


if __name__ == "__main__":
    unittest.main()
