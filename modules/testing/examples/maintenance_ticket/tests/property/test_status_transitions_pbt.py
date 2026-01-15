import os
import requests
from hypothesis import given, settings, strategies as st

BASE_URL = os.getenv("BASE_URL", "http://localhost:8080")

STATUSES = ["new", "in_progress", "closed"]
ALLOWED = {
    ("new", "in_progress"),
    ("in_progress", "closed"),
    # keep minimal; if you want, allow idempotent updates:
    ("new", "new"),
    ("in_progress", "in_progress"),
    ("closed", "closed"),
}

def create_ticket():
    r = requests.post(
        f"{BASE_URL}/tickets",
        json={"title": "t", "description": "d"}
    )
    assert r.status_code == 201, r.text
    data = r.json()
    return data["ticketId"], data["status"]

def patch_status(ticket_id: str, status: str):
    return requests.patch(
        f"{BASE_URL}/tickets/{ticket_id}/status",
        json={"status": status, "updatedBy": "pbt"}
    )

@settings(max_examples=30, deadline=None)
@given(st.lists(st.sampled_from(STATUSES), min_size=1, max_size=6))
def test_status_transition_property(sequence):
    """
    Property:
    - Only allowed transitions should be accepted (200).
    - Disallowed transitions should be rejected (400).
    """
    ticket_id, current = create_ticket()

    for nxt in sequence:
        resp = patch_status(ticket_id, nxt)
        if (current, nxt) in ALLOWED:
            assert resp.status_code == 200, resp.text
            current = resp.json()["status"]
        else:
            assert resp.status_code in (400, 409), resp.text  # allow either choice
            # current state should remain unchanged; we don't assert GET endpoint here
