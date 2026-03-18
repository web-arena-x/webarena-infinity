import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prescriptions = state.get("prescriptions", [])

    rx = next((p for p in prescriptions if p["id"] == "rx_007"), None)
    if not rx:
        return False, "Prescription rx_007 (Gabapentin) not found."

    if rx.get("frequency") != "Twice daily":
        return False, f"Prescription rx_007 frequency is '{rx.get('frequency')}', expected 'Twice daily'."

    return True, "Prescription rx_007 (Gabapentin) frequency is 'Twice daily'."
