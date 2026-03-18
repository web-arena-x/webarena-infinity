import requests


def verify(server_url: str) -> tuple[bool, str]:
    """The patient allergic to NSAIDs needs beta blocker dose 100mg and statin qty 90."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Must have switched to David Kowalski (NSAID allergy patient)
    if state.get("currentPatientId") != "pat_002":
        errors.append(f"Expected currentPatientId 'pat_002' (David Kowalski), got '{state.get('currentPatientId')}'.")

    # Beta blocker: rx_016 Metoprolol ER dosage -> 100mg
    rx_016 = next((r for r in state["prescriptions"] if r["id"] == "rx_016"), None)
    if not rx_016:
        errors.append("Prescription rx_016 (Metoprolol) not found.")
    else:
        if rx_016.get("dosage") != "100mg":
            errors.append(f"Expected rx_016 (Metoprolol) dosage '100mg', got '{rx_016.get('dosage')}'.")

    # Statin: rx_017 Atorvastatin quantity -> 90
    rx_017 = next((r for r in state["prescriptions"] if r["id"] == "rx_017"), None)
    if not rx_017:
        errors.append("Prescription rx_017 (Atorvastatin) not found.")
    else:
        if rx_017.get("quantity") != 90:
            errors.append(f"Expected rx_017 (Atorvastatin) quantity 90, got {rx_017.get('quantity')}.")

    if errors:
        return False, " ".join(errors)
    return True, "David Kowalski's Metoprolol increased to 100mg and Atorvastatin quantity changed to 90."
