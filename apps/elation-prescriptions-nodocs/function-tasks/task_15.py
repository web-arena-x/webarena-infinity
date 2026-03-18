import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prescriptions = state.get("prescriptions", [])

    rx = next((p for p in prescriptions if p["id"] == "rx_013"), None)
    if not rx:
        return False, "Prescription rx_013 (Sertraline) not found."

    if rx.get("status") != "discontinued":
        return False, f"Prescription rx_013 status is '{rx.get('status')}', expected 'discontinued'."

    reason = rx.get("discontinuedReason") or ""
    if "Patient request" not in reason:
        return False, f"Prescription rx_013 discontinuedReason is '{reason}', expected it to contain 'Patient request'."

    return True, "Prescription rx_013 (Sertraline) is discontinued with reason containing 'Patient request'."
