"""
Task: You received a message about a 'Futureforce' program. RSVP to that
employer's upcoming event, follow them, and save their active software
engineering position.

Discovery: 'Futureforce' → msg_10 from Salesforce (emp_19).
Salesforce event: evt_10 (Futureforce virtual info session).
Salesforce active SE job: job_17 (Software Engineer, New Grad).

Verify:
(1) evt_10 rsvped
(2) emp_19 in followedEmployerIds
(3) job_17 in savedJobIds
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    errors = []
    user = state.get("currentUser", {})

    events = state.get("events", [])
    evt_10 = next((e for e in events if e.get("id") == "evt_10"), None)
    if evt_10 is None:
        errors.append("evt_10 not found.")
    elif not evt_10.get("rsvped"):
        errors.append("evt_10 not RSVP'd.")

    followed = user.get("followedEmployerIds", [])
    if "emp_19" not in followed:
        errors.append("emp_19 (Salesforce) not followed.")

    saved = user.get("savedJobIds", [])
    if "job_17" not in saved:
        errors.append("job_17 not in savedJobIds.")

    if errors:
        return False, " | ".join(errors)
    return True, (
        "Salesforce identified via Futureforce message. "
        "Event RSVP'd, employer followed, SE job saved."
    )
