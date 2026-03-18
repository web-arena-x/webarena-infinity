import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Settings changes + David Atorvastatin 80mg + switch back to Margaret."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []
    settings = state.get("settings", {})

    # Settings
    if settings.get("signatureRequired") is not False:
        errors.append(f"Expected signatureRequired False, got {settings.get('signatureRequired')}.")
    if settings.get("printFormat") != "detailed":
        errors.append(f"Expected printFormat 'detailed', got '{settings.get('printFormat')}'.")

    # rx_017: David's Atorvastatin to 80mg
    rx_017 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_017"), None)
    if not rx_017:
        errors.append("Prescription rx_017 (David's Atorvastatin) not found.")
    else:
        if "80" not in str(rx_017.get("dosage", "")):
            errors.append(f"Expected rx_017 dosage to contain '80', got '{rx_017.get('dosage')}'.")

    # Should be back on Margaret
    if state.get("currentPatientId") != "pat_001":
        errors.append(f"Expected currentPatientId 'pat_001' (Margaret Chen), got '{state.get('currentPatientId')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "Settings updated, David's Atorvastatin increased to 80mg, switched back to Margaret."
