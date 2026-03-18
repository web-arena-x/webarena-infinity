import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check current patient is Jessica Morales
    current_patient = state.get("currentPatientId")
    if current_patient != "pat_005":
        return False, f"currentPatientId is '{current_patient}', expected 'pat_005' (Jessica Morales)."

    # Find prescription rx_025
    prescriptions = state.get("prescriptions", [])
    rx = next((p for p in prescriptions if p.get("id") == "rx_025"), None)
    if rx is None:
        return False, "Prescription 'rx_025' not found in state."

    # Check status is on-hold
    status = rx.get("status")
    if status != "on-hold":
        return False, f"Prescription rx_025 status is '{status}', expected 'on-hold'."

    return True, "Patient switched to Jessica Morales (pat_005) and rx_025 (Cephalexin) placed on hold."
