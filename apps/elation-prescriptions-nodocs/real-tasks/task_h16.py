import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Robert's cardiologist-prescribed medications: both on hold."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    if state.get("currentPatientId") != "pat_006":
        errors.append(f"Expected currentPatientId 'pat_006' (Robert Fitzgerald), got '{state.get('currentPatientId')}'.")

    # rx_028 Carvedilol (prescribed by prov_006 Tanaka) -> on-hold
    rx_028 = next((r for r in state["prescriptions"] if r["id"] == "rx_028"), None)
    if not rx_028:
        errors.append("Prescription rx_028 (Carvedilol) not found.")
    else:
        if rx_028.get("status") != "on-hold":
            errors.append(f"Expected rx_028 (Carvedilol) status 'on-hold', got '{rx_028.get('status')}'.")

    # rx_029 Spironolactone (prescribed by prov_006 Tanaka) -> on-hold
    rx_029 = next((r for r in state["prescriptions"] if r["id"] == "rx_029"), None)
    if not rx_029:
        errors.append("Prescription rx_029 (Spironolactone) not found.")
    else:
        if rx_029.get("status") != "on-hold":
            errors.append(f"Expected rx_029 (Spironolactone) status 'on-hold', got '{rx_029.get('status')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "Robert's Carvedilol and Spironolactone (cardiologist-prescribed) both placed on hold."
