import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    if state.get("currentPatientId") != "pat_006":
        return False, f"currentPatientId is '{state.get('currentPatientId')}', expected 'pat_006'."

    prescriptions = state.get("prescriptions", [])

    rx = next((p for p in prescriptions if p["id"] == "rx_028"), None)
    if not rx:
        return False, "Prescription rx_028 (Carvedilol) not found."

    if rx.get("dosage") != "25mg":
        return False, f"Prescription rx_028 dosage is '{rx.get('dosage')}', expected '25mg'."

    return True, "Patient is pat_006 and prescription rx_028 (Carvedilol) dosage is '25mg'."
