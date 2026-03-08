"""
Task: Find the only employer in the 'Media & Entertainment' industry.
Save their active job, follow them, and RSVP to the upcoming virtual
career fair.

Discovery: Media & Entertainment → Spotify (emp_13).
Active job: job_15 (Data Science Intern).
Virtual career fair: evt_07 (Virtual Career Fair - Technology Focus).

Verify:
(1) job_15 in savedJobIds
(2) emp_13 in followedEmployerIds
(3) evt_07 rsvped
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    errors = []
    user = state.get("currentUser", {})

    saved = user.get("savedJobIds", [])
    if "job_15" not in saved:
        errors.append("job_15 not in savedJobIds.")

    followed = user.get("followedEmployerIds", [])
    if "emp_13" not in followed:
        errors.append("emp_13 (Spotify) not followed.")

    events = state.get("events", [])
    evt_07 = next((e for e in events if e.get("id") == "evt_07"), None)
    if evt_07 is None:
        errors.append("evt_07 not found.")
    elif not evt_07.get("rsvped"):
        errors.append("evt_07 not RSVP'd.")

    if errors:
        return False, " | ".join(errors)
    return True, (
        "Spotify identified (Media & Entertainment). "
        "job_15 saved, employer followed, virtual career fair RSVP'd."
    )
