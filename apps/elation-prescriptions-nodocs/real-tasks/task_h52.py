import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Margaret: resume HCTZ, cancel Albuterol, change Metformin to once daily qty 30."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rx_012 Hydrochlorothiazide -> resumed (active)
    rx_012 = next((r for r in state["prescriptions"] if r["id"] == "rx_012"), None)
    if not rx_012:
        errors.append("Prescription rx_012 (Hydrochlorothiazide) not found.")
    else:
        if rx_012.get("status") != "active":
            errors.append(f"Expected rx_012 (HCTZ) status 'active', got '{rx_012.get('status')}'.")

    # rx_006 Albuterol -> cancelled
    rx_006 = next((r for r in state["prescriptions"] if r["id"] == "rx_006"), None)
    if not rx_006:
        errors.append("Prescription rx_006 (Albuterol) not found.")
    else:
        if rx_006.get("status") != "cancelled":
            errors.append(f"Expected rx_006 (Albuterol) status 'cancelled', got '{rx_006.get('status')}'.")

    # rx_003 Metformin -> frequency Once daily, quantity 30
    rx_003 = next((r for r in state["prescriptions"] if r["id"] == "rx_003"), None)
    if not rx_003:
        errors.append("Prescription rx_003 (Metformin) not found.")
    else:
        if rx_003.get("frequency") != "Once daily":
            errors.append(f"Expected rx_003 (Metformin) frequency 'Once daily', got '{rx_003.get('frequency')}'.")
        if rx_003.get("quantity") != 30:
            errors.append(f"Expected rx_003 (Metformin) quantity 30, got {rx_003.get('quantity')}.")

    if errors:
        return False, " ".join(errors)
    return True, "Margaret's HCTZ resumed, Albuterol cancelled, Metformin changed to once daily qty 30."
