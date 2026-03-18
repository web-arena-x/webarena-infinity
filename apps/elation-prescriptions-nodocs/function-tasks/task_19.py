import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prescriptions = state.get("prescriptions", [])

    rx = next((p for p in prescriptions if p["id"] == "rx_001"), None)
    if not rx:
        return False, "Prescription rx_001 (Atorvastatin) not found."

    if rx.get("dosage") != "40mg":
        return False, f"Prescription rx_001 dosage is '{rx.get('dosage')}', expected '40mg'."

    return True, "Prescription rx_001 (Atorvastatin) dosage is '40mg'."
