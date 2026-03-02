import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    patients = state.get("patients", [])
    for patient in patients:
        if patient.get("id") == "pat_2":
            tags = patient.get("tags", [])
            if "New Patient" not in tags:
                return True, "'New Patient' tag removed from Emily Thompson."
            else:
                return False, f"Patient pat_2 still has 'New Patient' in tags: {tags}."

    return False, "Patient with id 'pat_2' not found in patients."
