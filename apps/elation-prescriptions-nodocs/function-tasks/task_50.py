import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check current patient is Aisha Rahman
    current_patient = state.get("currentPatientId")
    if current_patient != "pat_003":
        return False, f"currentPatientId is '{current_patient}', expected 'pat_003' (Aisha Rahman)."

    # Find prescription rx_021
    prescriptions = state.get("prescriptions", [])
    rx = next((p for p in prescriptions if p.get("id") == "rx_021"), None)
    if rx is None:
        return False, "Prescription 'rx_021' not found in state."

    # Check status is discontinued
    status = rx.get("status")
    if status != "discontinued":
        return False, f"Prescription rx_021 status is '{status}', expected 'discontinued'."

    # Check discontinuedReason contains 'Course completed'
    reason = rx.get("discontinuedReason", "")
    if "Course completed" not in reason:
        return False, f"Prescription rx_021 discontinuedReason is '{reason}', expected it to contain 'Course completed'."

    return True, "Patient switched to Aisha Rahman (pat_003) and rx_021 (Escitalopram) is discontinued with reason 'Course completed'."
