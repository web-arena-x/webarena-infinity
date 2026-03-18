import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    current_patient = state.get("currentPatientId")
    if current_patient != "pat_003":
        return False, f"currentPatientId is '{current_patient}', expected 'pat_003' (Aisha Rahman)."

    return True, "Current patient switched to Aisha Rahman (pat_003)."
