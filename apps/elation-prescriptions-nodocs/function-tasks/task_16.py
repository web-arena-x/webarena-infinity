import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prescriptions = state.get("prescriptions", [])

    rx = next((p for p in prescriptions if p["id"] == "rx_006"), None)
    if not rx:
        return False, "Prescription rx_006 (Levothyroxine) not found."

    if rx.get("status") != "on-hold":
        return False, f"Prescription rx_006 status is '{rx.get('status')}', expected 'on-hold'."

    return True, "Prescription rx_006 has status 'on-hold'."
