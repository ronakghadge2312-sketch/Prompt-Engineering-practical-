"""
Practical 37: Webhook-Based Notification
A small Flask demo that accepts sample student-registration events.

Run locally:
    python -m venv .venv
    .venv\Scripts\activate        # Windows
    pip install -r requirements.txt
    python app.py

Then send a sample event from another terminal:
    python send_sample_event.py
"""

import os
import json
import hashlib
from datetime import datetime, timezone
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024  # Limit request size.

# Demo-only in-memory store. Data resets when the app restarts.
processed_event_ids = set()
notifications = []

PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Practical 37 - Webhook Notification</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 900px; margin: 36px auto; padding: 0 16px; line-height: 1.5; color: #202124; }
    .card { border: 1px solid #ddd; border-radius: 12px; padding: 18px; margin: 16px 0; }
    code, pre { background: #f4f4f4; border-radius: 6px; padding: 3px 6px; }
    pre { padding: 12px; overflow-x: auto; }
    .muted { color: #555; }
  </style>
</head>
<body>
  <h1>Practical 37: Webhook-Based Notification</h1>
  <p class="muted">Local demonstration — new student registration events.</p>
  <div class="card">
    <h2>Webhook endpoint</h2>
    <p><code>POST /webhook/registration</code></p>
    <p>Send JSON containing <code>event_id</code>, <code>event</code>, <code>student_name</code>, and <code>course</code>.</p>
    <p>Use <code>python send_sample_event.py</code> in a second terminal to submit a sample event.</p>
  </div>
  <div class="card">
    <h2>Latest notifications (this run only)</h2>
    {% if notifications %}
      {% for item in notifications|reverse %}
        <div>
          <strong>{{ item["title"] }}</strong>
          <p>{{ item["message"] }}</p>
          <small>{{ item["created_at"] }} · Event ID: {{ item["event_id"] }}</small>
          <hr>
        </div>
      {% endfor %}
    {% else %}
      <p>No notifications yet. Send a sample event to test the webhook.</p>
    {% endif %}
  </div>
  <div class="card">
    <h2>Safety notes</h2>
    <ul>
      <li>Invalid events are rejected and do not create notifications.</li>
      <li>Duplicate event IDs are ignored.</li>
      <li>This is a local classroom demo; data is stored in memory and resets on restart.</li>
    </ul>
  </div>
</body>
</html>
"""


def make_event_fingerprint(event_id: str) -> str:
    """Create a stable digest for an event ID before storing it in the demo set."""
    return hashlib.sha256(event_id.encode("utf-8")).hexdigest()


def validate_event(payload):
    """Return (cleaned_event, error_message)."""
    if not isinstance(payload, dict):
        return None, "Request body must be a JSON object."

    required = ["event_id", "event", "student_name", "course"]
    missing = [key for key in required if not isinstance(payload.get(key), str) or not payload[key].strip()]
    if missing:
        return None, "Missing or invalid required field(s): " + ", ".join(missing)

    cleaned = {key: payload[key].strip() for key in required}
    if cleaned["event"] != "student.registration.created":
        return None, "Unsupported event type. Expected 'student.registration.created'."
    if len(cleaned["event_id"]) > 120:
        return None, "event_id must be 120 characters or fewer."
    if len(cleaned["student_name"]) > 100:
        return None, "student_name must be 100 characters or fewer."
    if len(cleaned["course"]) > 100:
        return None, "course must be 100 characters or fewer."
    return cleaned, None


@app.get("/")
def home():
    return render_template_string(PAGE, notifications=notifications)


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "student-registration-webhook-demo"}), 200


@app.post("/webhook/registration")
def registration_webhook():
    if not request.is_json:
        return jsonify({"status": "error", "message": "Content-Type must be application/json."}), 415

    payload = request.get_json(silent=True)
    event, error = validate_event(payload)
    if error:
        return jsonify({"status": "rejected", "message": error, "notification_created": False}), 400

    fingerprint = make_event_fingerprint(event["event_id"])
    if fingerprint in processed_event_ids:
        return jsonify({
            "status": "duplicate_ignored",
            "message": "This event ID has already been processed.",
            "notification_created": False,
            "event_id": event["event_id"],
        }), 200

    # Mark as processed only after validation, then prepare the notification.
    processed_event_ids.add(fingerprint)
    notification = {
        "title": "New Student Registration",
        "message": f'{event["student_name"]} registered for {event["course"]}.',
        "event_id": event["event_id"],
        "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
    }
    notifications.append(notification)

    return jsonify({
        "status": "success",
        "message": "Registration notification prepared.",
        "notification_created": True,
        "notification": notification,
    }), 201


if __name__ == "__main__":
    # Debug mode is disabled by default for safer demonstration.
    port = int(os.getenv("PORT", "5000"))
    app.run(host="127.0.0.1", port=port, debug=False)
