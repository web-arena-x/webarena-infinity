import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prescriptions = state.get("prescriptions", [])

    rx = next((p for p in prescriptions if p["id"] == "rx_004"), None)
    if not rx:
        return False, "Prescription rx_004 (Amlodipine) not found."

    quantity = rx.get("quantity")
    if quantity != 90:
        return False, f"Prescription rx_004 quantity is {quantity}, expected 90."

    return True, "Prescription rx_004 (Amlodipine) quantity is 90."
