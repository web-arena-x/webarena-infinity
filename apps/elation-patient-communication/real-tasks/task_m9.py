import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    patients = state.get("patients", [])
    patient = None
    for p in patients:
        if p.get("firstName") == "Raymond" and p.get("lastName") == "Copeland":
            patient = p
            break

    if patient is None:
        return False, "Patient Raymond Copeland not found."

    tags = patient.get("tags", [])

    if "Chronic Care" not in tags:
        return False, f"'Chronic Care' tag not found on Raymond Copeland. Current tags: {tags}."

    if "Diabetes Management" not in tags:
        return False, f"'Diabetes Management' tag not found on Raymond Copeland. Current tags: {tags}."

    return True, "Raymond Copeland tagged with Chronic Care and Diabetes Management."
