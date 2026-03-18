import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prescriptions = state.get("prescriptions", [])

    rx = next((p for p in prescriptions if p.get("id") == "rx_008"), None)

    if rx is None:
        return False, "Prescription rx_008 not found in state."

    if rx.get("status") != "cancelled":
        return False, f"rx_008 status should be 'cancelled', got '{rx.get('status')}'."

    return True, "Prescription rx_008 has been cancelled."
