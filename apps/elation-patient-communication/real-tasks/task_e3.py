import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    patients = state.get("patients", [])
    for patient in patients:
        if patient.get("id") == "pat_1":
            tags = patient.get("tags", [])
            if "VIP" in tags:
                return True, "James Rodriguez has been tagged as VIP."
            else:
                return False, f"Patient pat_1 found but tags are {tags}, expected 'VIP' to be present."

    return False, "Patient with id 'pat_1' not found in patients."
