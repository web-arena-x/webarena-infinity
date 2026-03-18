import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prescriptions = state.get("prescriptions", [])

    rx = next((p for p in prescriptions if p.get("id") == "rx_004"), None)

    if rx is None:
        return False, "Prescription rx_004 not found in state."

    if rx.get("status") != "on-hold":
        return False, f"rx_004 status should be 'on-hold', got '{rx.get('status')}'."

    return True, "Prescription rx_004 is on hold."
