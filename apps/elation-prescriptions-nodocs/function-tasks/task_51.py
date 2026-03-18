import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check current patient is William Thornton
    current_patient = state.get("currentPatientId")
    if current_patient != "pat_004":
        return False, f"currentPatientId is '{current_patient}', expected 'pat_004' (William Thornton)."

    # Find prescription rx_023
    prescriptions = state.get("prescriptions", [])
    rx = next((p for p in prescriptions if p.get("id") == "rx_023"), None)
    if rx is None:
        return False, "Prescription 'rx_023' not found in state."

    # Check refillsRemaining
    refills_remaining = rx.get("refillsRemaining")
    if refills_remaining != 5:
        return False, f"Prescription rx_023 refillsRemaining is {refills_remaining}, expected 5."

    # Check refillsTotal
    refills_total = rx.get("refillsTotal")
    if refills_total != 5:
        return False, f"Prescription rx_023 refillsTotal is {refills_total}, expected 5."

    # Check status is active
    status = rx.get("status")
    if status != "active":
        return False, f"Prescription rx_023 status is '{status}', expected 'active'."

    return True, "Patient switched to William Thornton (pat_004) and rx_023 (Insulin Glargine) renewed with 5 refills, status active."
