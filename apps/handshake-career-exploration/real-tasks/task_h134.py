"""
Task: Read all your unread top-match messages. For each sender, save their
most recently posted active internship.

Discovery:
  Unread top-match messages:
    msg_01 → Google (emp_01)
    msg_03 → Meta (emp_07)
    msg_08 → Apple (emp_05)
  Most recently posted active internship per sender:
    Google: job_22 (Feb 23)
    Meta: job_26 (Feb 26)
    Apple: job_25 (Mar 1)

Verify:
(1) msg_01, msg_03, msg_08 isRead
(2) job_22, job_26, job_25 in savedJobIds
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
    for msg_id in ["msg_01", "msg_03", "msg_08"]:
        msg = next((m for m in messages if m.get("id") == msg_id), None)
        if msg is None:
            errors.append(f"{msg_id} not found.")
        elif not msg.get("isRead"):
            errors.append(f"{msg_id} not marked as read.")

    saved = user.get("savedJobIds", [])
    for jid in ["job_22", "job_26", "job_25"]:
        if jid not in saved:
            errors.append(f"{jid} not in savedJobIds.")

    if errors:
        return False, " | ".join(errors)
    return True, (
        "All unread top-match messages read. "
        "Most recently posted internship from each sender saved."
    )
