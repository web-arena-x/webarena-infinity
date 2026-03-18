import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prescriptions = state.get("prescriptions", [])

    rx = next((p for p in prescriptions if p["id"] == "rx_002"), None)
    if not rx:
        return False, "Prescription rx_002 (Lisinopril) not found."

    if rx.get("status") != "cancelled":
        return False, f"Prescription rx_002 status is '{rx.get('status')}', expected 'cancelled'."

    return True, "Prescription rx_002 has status 'cancelled'."
