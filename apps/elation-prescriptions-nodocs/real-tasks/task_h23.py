import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Two Atorvastatin patients: renew lower-dose with 5, increase higher-dose qty to 90."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rx_001: Margaret's Atorvastatin 20mg (lower dose) -> renew with 5
    rx_001 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_001"), None)
    if not rx_001:
        errors.append("Prescription rx_001 (Margaret's Atorvastatin) not found.")
    else:
        if rx_001.get("refillsRemaining", 0) < 5:
            errors.append(f"Expected rx_001 refillsRemaining >= 5, got {rx_001.get('refillsRemaining')}.")

    # rx_017: David's Atorvastatin 40mg (higher dose) -> qty 90
    rx_017 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_017"), None)
    if not rx_017:
        errors.append("Prescription rx_017 (David's Atorvastatin) not found.")
    else:
        if rx_017.get("quantity") != 90:
            errors.append(f"Expected rx_017 quantity 90, got {rx_017.get('quantity')}.")

    if errors:
        return False, " ".join(errors)
    return True, "Lower-dose Atorvastatin renewed with 5 refills, higher-dose quantity set to 90."
