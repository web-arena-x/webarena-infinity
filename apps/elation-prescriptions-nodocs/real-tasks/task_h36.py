import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Robert: renew Carvedilol 6, increase Spironolactone 50mg, increase Empagliflozin 25mg."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    if state.get("currentPatientId") != "pat_006":
        errors.append(f"Expected currentPatientId 'pat_006' (Robert Fitzgerald), got '{state.get('currentPatientId')}'.")

    # rx_028: Carvedilol renewed with 6
    rx_028 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_028"), None)
    if not rx_028:
        errors.append("Prescription rx_028 (Carvedilol) not found.")
    else:
        if rx_028.get("refillsRemaining", 0) < 6:
            errors.append(f"Expected rx_028 refillsRemaining >= 6, got {rx_028.get('refillsRemaining')}.")

    # rx_029: Spironolactone dosage to 50mg
    rx_029 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_029"), None)
    if not rx_029:
        errors.append("Prescription rx_029 (Spironolactone) not found.")
    else:
        if "50" not in str(rx_029.get("dosage", "")):
            errors.append(f"Expected rx_029 dosage to contain '50', got '{rx_029.get('dosage')}'.")

    # rx_027: Empagliflozin dosage to 25mg
    rx_027 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_027"), None)
    if not rx_027:
        errors.append("Prescription rx_027 (Empagliflozin) not found.")
    else:
        if "25" not in str(rx_027.get("dosage", "")):
            errors.append(f"Expected rx_027 dosage to contain '25', got '{rx_027.get('dosage')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "Robert's heart failure regimen adjusted: Carvedilol renewed, Spironolactone and Empagliflozin increased."
