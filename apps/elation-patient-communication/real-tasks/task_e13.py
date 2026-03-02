import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    patients = state.get("patients", [])
    for patient in patients:
        if patient.get("id") == "pat_30":
            tags = patient.get("tags", [])
            if "High Risk" in tags:
                return True, "Janet Okonkwo has been tagged as High Risk."
            else:
                return False, f"Patient pat_30 found but tags are {tags}, expected 'High Risk' to be present."

    return False, "Patient with id 'pat_30' not found in patients."
