"""
Task: Read your most recent unread message. RSVP to that sender's upcoming
event and save all their active jobs you haven't already saved.

Discovery: Most recent unread → msg_01 from Google (March 6).
Google event: evt_04 (Tech Talk, upcoming).
Google active jobs not yet saved: job_01, job_02, job_22.

Verify:
(1) msg_01 isRead
(2) evt_04 rsvped
(3) job_01, job_02, job_22 in savedJobIds
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    errors = []
    user = state.get("currentUser", {})

    messages = state.get("messages", [])
    msg_01 = next((m for m in messages if m.get("id") == "msg_01"), None)
    if msg_01 is None:
        errors.append("msg_01 not found.")
    elif not msg_01.get("isRead"):
        errors.append("msg_01 not marked as read.")

    events = state.get("events", [])
    evt_04 = next((e for e in events if e.get("id") == "evt_04"), None)
    if evt_04 is None:
        errors.append("evt_04 not found.")
    elif not evt_04.get("rsvped"):
        errors.append("evt_04 not RSVP'd.")

    saved = user.get("savedJobIds", [])
    for jid in ["job_01", "job_02", "job_22"]:
        if jid not in saved:
            errors.append(f"{jid} not in savedJobIds.")

    if errors:
        return False, " | ".join(errors)
    return True, (
        "Most recent unread message (Google) read. "
        "Google Tech Talk RSVP'd. All Google active jobs saved."
    )
