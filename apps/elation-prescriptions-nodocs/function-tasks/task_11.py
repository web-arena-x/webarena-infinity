import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prescriptions = state.get("prescriptions", [])

    rx = next((p for p in prescriptions if p.get("id") == "rx_012"), None)

    if rx is None:
        return False, "Prescription rx_012 not found in state."

    if rx.get("status") != "active":
        return False, f"rx_012 status should be 'active' (resumed), got '{rx.get('status')}'."

    return True, "Prescription rx_012 (Hydrochlorothiazide) has been resumed to active."
