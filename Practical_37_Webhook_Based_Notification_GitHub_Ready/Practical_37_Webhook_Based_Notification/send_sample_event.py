"""Send a sample student-registration event to the local webhook."""

import json
import urllib.error
import urllib.request

URL = "http://127.0.0.1:5000/webhook/registration"

sample_event = {
    "event_id": "registration-demo-001",
    "event": "student.registration.created",
    "student_name": "Aarav Patel",
    "course": "Generative AI",
}


def send_event(payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            print(f"HTTP {response.status}")
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print(f"HTTP {error.code}")
        print(error.read().decode("utf-8"))
    except urllib.error.URLError as error:
        print("Could not connect to the app. Start app.py first.")
        print(f"Details: {error.reason}")


if __name__ == "__main__":
    send_event(sample_event)
    print("\nSending the same event again to test duplicate protection:")
    send_event(sample_event)
