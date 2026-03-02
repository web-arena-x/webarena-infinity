import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    patients = state.get("patients", [])
    patient = None
    for p in patients:
        if p.get("firstName") == "Helen" and p.get("lastName") == "Matsumoto":
            patient = p
            break

    if patient is None:
        return False, "Patient Helen Matsumoto not found."

    sharing_level = patient.get("passportSharingLevel")
    if sharing_level != 4:
        return False, f"Helen Matsumoto's Passport sharing level is {sharing_level}, expected 4."

    return True, "Helen Matsumoto's Passport sharing level upgraded to Level 4."
