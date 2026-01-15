import os
import requests

BASE_URL = os.getenv("BASE_URL", "http://localhost:8080")

def test_S001_create_ticket_minimum():
    """
    Given: operator provides minimum required info
    When: POST /tickets
    Then: ticket_id returned and status is 'new' and reviewRequired is false
    """
    r = requests.post(f"{BASE_URL}/tickets", json={"title": "motor noise", "description": "abnormal sound"})
    assert r.status_code == 201, r.text
    body = r.json()
    assert "ticketId" in body
    assert body["status"] == "new"
    assert body["reviewRequired"] is False

def test_S002_update_status_new_to_in_progress():
    """
    Given: ticket exists in 'new'
    When: PATCH status to in_progress
    Then: 200 and status updated
    """
    r = requests.post(f"{BASE_URL}/tickets", json={"title": "x", "description": "y"})
    assert r.status_code == 201, r.text
    ticket_id = r.json()["ticketId"]

    u = requests.patch(f"{BASE_URL}/tickets/{ticket_id}/status", json={"status": "in_progress", "updatedBy": "lead"})
    assert u.status_code == 200, u.text
    assert u.json()["status"] == "in_progress"

def test_S003_safety_hint_should_require_human_review():
    """
    Given: description suggests safety impact
    When: POST /tickets
    Then:
      - Either reject (400), OR
      - Accept (201) with reviewRequired=true (defer to human)
    """
    r = requests.post(
        f"{BASE_URL}/tickets",
        json={"title": "smoke", "description": "There is smoke and someone collapsed"}
    )

    if r.status_code == 400:
        # Strict mode: force human handling outside the system
        return

    assert r.status_code == 201, r.text
    body = r.json()
    assert body["reviewRequired"] is True
    # status can still be "new" (recommended). Keep it flexible for now:
    assert body["status"] in ("new", "in_progress", "closed")
