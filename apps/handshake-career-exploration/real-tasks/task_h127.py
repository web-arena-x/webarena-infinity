"""
Task: Three employers are in the Consulting industry, but only one hosts
an upcoming event. RSVP to that event and save that employer's active job.

Discovery: Consulting employers: McKinsey (emp_04), Deloitte (emp_08),
Bain (emp_11). McKinsey hosts evt_01 (Campus Presentation, upcoming).
McKinsey active job: job_05.

Verify:
(1) evt_01 rsvped
(2) job_05 in savedJobIds
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
    evt_01 = next((e for e in events if e.get("id") == "evt_01"), None)
    if evt_01 is None:
        errors.append("evt_01 not found.")
    elif not evt_01.get("rsvped"):
        errors.append("evt_01 not RSVP'd.")

    saved = user.get("savedJobIds", [])
    if "job_05" not in saved:
        errors.append("job_05 not in savedJobIds.")

    if errors:
        return False, " | ".join(errors)
    return True, (
        "McKinsey identified as the only consulting employer with an "
        "upcoming event. evt_01 RSVP'd and job_05 saved."
    )
