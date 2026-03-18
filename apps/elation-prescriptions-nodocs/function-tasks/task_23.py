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

    if rx.get("dosage") != "100mg":
        return False, f"Prescription rx_013 dosage is '{rx.get('dosage')}', expected '100mg'."

    return True, "Prescription rx_013 (Sertraline) dosage is '100mg'."
