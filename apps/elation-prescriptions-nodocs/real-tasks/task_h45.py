import requests


def verify(server_url: str) -> tuple[bool, str]:
    """NKDA patient (Aisha): increase SSRI dosage to 10mg, quantity to 60."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    if state.get("currentPatientId") != "pat_003":
        errors.append(f"Expected currentPatientId 'pat_003' (Aisha Rahman), got '{state.get('currentPatientId')}'.")

    rx_021 = next((r for r in state["prescriptions"] if r["id"] == "rx_021"), None)
    if not rx_021:
        errors.append("Prescription rx_021 (Escitalopram) not found.")
    else:
        if rx_021.get("dosage") != "10mg":
            errors.append(f"Expected rx_021 dosage '10mg', got '{rx_021.get('dosage')}'.")
        if rx_021.get("quantity") != 60:
            errors.append(f"Expected rx_021 quantity 60, got {rx_021.get('quantity')}.")

    if errors:
        return False, " ".join(errors)
    return True, "Aisha Rahman's Escitalopram increased to 10mg with quantity 60."
