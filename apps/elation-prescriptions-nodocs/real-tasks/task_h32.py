import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Two Metformin patients: Margaret dosage 1500mg, David renew 5."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rx_003: Margaret's Metformin -> dosage 1500mg
    rx_003 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_003"), None)
    if not rx_003:
        errors.append("Prescription rx_003 (Margaret's Metformin) not found.")
    else:
        if "1500" not in str(rx_003.get("dosage", "")):
            errors.append(f"Expected rx_003 dosage to contain '1500', got '{rx_003.get('dosage')}'.")

    # rx_019: David's Metformin ER -> renewed with 5
    rx_019 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_019"), None)
    if not rx_019:
        errors.append("Prescription rx_019 (David's Metformin ER) not found.")
    else:
        if rx_019.get("refillsRemaining", 0) < 5:
            errors.append(f"Expected rx_019 refillsRemaining >= 5, got {rx_019.get('refillsRemaining')}.")

    if errors:
        return False, " ".join(errors)
    return True, "Margaret's Metformin increased to 1500mg, David's Metformin ER renewed with 5 refills."
