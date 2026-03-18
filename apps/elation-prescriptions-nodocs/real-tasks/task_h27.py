import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Jessica: renew Fluoxetine with 6. Robert: hold Empagliflozin."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rx_026: Jessica's Fluoxetine renewed with 6
    rx_026 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_026"), None)
    if not rx_026:
        errors.append("Prescription rx_026 (Fluoxetine) not found.")
    else:
        if rx_026.get("refillsRemaining", 0) < 6:
            errors.append(f"Expected rx_026 refillsRemaining >= 6, got {rx_026.get('refillsRemaining')}.")

    # rx_027: Robert's Empagliflozin on hold
    rx_027 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_027"), None)
    if not rx_027:
        errors.append("Prescription rx_027 (Empagliflozin) not found.")
    else:
        if rx_027.get("status") != "on-hold":
            errors.append(f"Expected rx_027 status 'on-hold', got '{rx_027.get('status')}'.")

    if state.get("currentPatientId") != "pat_006":
        errors.append(f"Expected currentPatientId 'pat_006' (Robert Fitzgerald), got '{state.get('currentPatientId')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "Jessica's Fluoxetine renewed with 6 refills, Robert's Empagliflozin placed on hold."
