import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Resume HCTZ + 50mg, renew Albuterol 4, discontinue Flonase."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rx_012: HCTZ resumed and dose changed to 50mg
    rx_012 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_012"), None)
    if not rx_012:
        errors.append("Prescription rx_012 (HCTZ) not found.")
    else:
        if rx_012.get("status") != "active":
            errors.append(f"Expected rx_012 status 'active', got '{rx_012.get('status')}'.")
        if "50" not in str(rx_012.get("dosage", "")):
            errors.append(f"Expected rx_012 dosage to contain '50', got '{rx_012.get('dosage')}'.")

    # rx_006: Albuterol renewed with 4
    rx_006 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_006"), None)
    if not rx_006:
        errors.append("Prescription rx_006 (Albuterol) not found.")
    else:
        if rx_006.get("refillsRemaining", 0) < 4:
            errors.append(f"Expected rx_006 refillsRemaining >= 4, got {rx_006.get('refillsRemaining')}.")

    # rx_008: Flonase discontinued
    rx_008 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_008"), None)
    if not rx_008:
        errors.append("Prescription rx_008 (Flonase) not found.")
    elif rx_008.get("status") != "discontinued":
        errors.append(f"Expected rx_008 status 'discontinued', got '{rx_008.get('status')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "HCTZ resumed at 50mg, Albuterol renewed with 4 refills, Flonase discontinued."
