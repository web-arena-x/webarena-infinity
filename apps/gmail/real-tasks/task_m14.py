"""Add the Projects label to the office renovation email from Daniel Thompson."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()

    emails = state.get("emails", [])
    target = next((e for e in emails if e.get("id") == 17), None)
    if target is None:
        return False, "Email with id=17 (Office Renovation Plans) not found."

    labels = target.get("labels", [])
    if "label_9" in labels:
        return True, "Email 17 (Office Renovation Plans) has the Projects label (label_9)."
    return False, f"Expected 'label_9' (Projects) in labels, got {labels!r}."
