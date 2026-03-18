import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Settings: brand first, 5 refills, no sig. Then Jessica's Fluoxetine renewed with 5."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []
    settings = state.get("settings", {})

    # showGenericFirst -> False
    if settings.get("showGenericFirst") is not False:
        errors.append(f"Expected showGenericFirst False, got {settings.get('showGenericFirst')}.")

    # defaultRefills -> 5
    if settings.get("defaultRefills") != 5:
        errors.append(f"Expected defaultRefills 5, got {settings.get('defaultRefills')}.")

    # signatureRequired -> False
    if settings.get("signatureRequired") is not False:
        errors.append(f"Expected signatureRequired False, got {settings.get('signatureRequired')}.")

    # Current patient -> Jessica Morales
    if state.get("currentPatientId") != "pat_005":
        errors.append(f"Expected currentPatientId 'pat_005' (Jessica Morales), got '{state.get('currentPatientId')}'.")

    # rx_026 Fluoxetine renewed with 5 refills
    rx_026 = next((r for r in state["prescriptions"] if r["id"] == "rx_026"), None)
    if not rx_026:
        errors.append("Prescription rx_026 (Fluoxetine) not found.")
    else:
        if rx_026.get("refillsRemaining") != 5:
            errors.append(f"Expected rx_026 (Fluoxetine) refillsRemaining 5, got {rx_026.get('refillsRemaining')}.")

    if errors:
        return False, " ".join(errors)
    return True, "Settings updated and Jessica's Fluoxetine renewed with 5 refills."
