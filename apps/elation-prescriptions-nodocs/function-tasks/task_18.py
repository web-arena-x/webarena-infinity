import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    if state.get("currentPatientId") != "pat_004":
        return False, f"currentPatientId is '{state.get('currentPatientId')}', expected 'pat_004'."

    prescriptions = state.get("prescriptions", [])

    rx = next((p for p in prescriptions if p["id"] == "rx_024"), None)
    if not rx:
        return False, "Prescription rx_024 (Furosemide) not found."

    if rx.get("status") != "discontinued":
        return False, f"Prescription rx_024 status is '{rx.get('status')}', expected 'discontinued'."

    reason = rx.get("discontinuedReason") or ""
    if "Resolved peripheral edema" not in reason:
        return False, f"Prescription rx_024 discontinuedReason is '{reason}', expected it to contain 'Resolved peripheral edema'."

    return True, "Patient is pat_004 and prescription rx_024 (Furosemide) is discontinued with reason containing 'Resolved peripheral edema'."
