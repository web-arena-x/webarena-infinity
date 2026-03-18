import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Switch to ACE-inhibitor-allergy patient, modify Valsartan to 320mg, renew with 5."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    if state.get("currentPatientId") != "pat_004":
        errors.append(f"Expected currentPatientId 'pat_004' (William Thornton), got '{state.get('currentPatientId')}'.")

    rx_022 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_022"), None)
    if not rx_022:
        errors.append("Prescription rx_022 (Valsartan) not found.")
    else:
        if "320" not in str(rx_022.get("dosage", "")):
            errors.append(f"Expected rx_022 dosage to contain '320', got '{rx_022.get('dosage')}'.")
        if rx_022.get("refillsRemaining", 0) < 5:
            errors.append(f"Expected rx_022 refillsRemaining >= 5, got {rx_022.get('refillsRemaining')}.")

    if errors:
        return False, " ".join(errors)
    return True, "William Thornton selected, Valsartan increased to 320mg and renewed with 5 refills."
