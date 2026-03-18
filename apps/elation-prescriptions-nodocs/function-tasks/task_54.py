import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check current patient is Robert Fitzgerald
    current_patient = state.get("currentPatientId")
    if current_patient != "pat_006":
        return False, f"currentPatientId is '{current_patient}', expected 'pat_006' (Robert Fitzgerald)."

    # Find prescription rx_029
    prescriptions = state.get("prescriptions", [])
    rx = next((p for p in prescriptions if p.get("id") == "rx_029"), None)
    if rx is None:
        return False, "Prescription 'rx_029' not found in state."

    # Check quantity is 60
    quantity = rx.get("quantity")
    if quantity != 60:
        return False, f"Prescription rx_029 quantity is {quantity}, expected 60."

    return True, "Patient switched to Robert Fitzgerald (pat_006) and rx_029 (Spironolactone) quantity changed to 60."
