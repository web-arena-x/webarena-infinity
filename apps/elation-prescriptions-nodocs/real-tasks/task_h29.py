import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Hold Family Medicine doctor's rx, renew cardiologist's rx with 6."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rx_004: prescribed by prov_002 (Dr. Okafor, Family Medicine) -> on-hold
    rx_004 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_004"), None)
    if not rx_004:
        errors.append("Prescription rx_004 (Levothyroxine) not found.")
    elif rx_004.get("status") != "on-hold":
        errors.append(f"Expected rx_004 (Family Med doctor's rx) status 'on-hold', got '{rx_004.get('status')}'.")

    # rx_014: prescribed by prov_006 (Dr. Tanaka, Cardiology) -> renewed with 6
    rx_014 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_014"), None)
    if not rx_014:
        errors.append("Prescription rx_014 (Apixaban) not found.")
    else:
        if rx_014.get("refillsRemaining", 0) < 6:
            errors.append(f"Expected rx_014 (cardiologist's rx) refillsRemaining >= 6, got {rx_014.get('refillsRemaining')}.")

    if errors:
        return False, " ".join(errors)
    return True, "Family Medicine doctor's prescription on hold, cardiologist's prescription renewed with 6 refills."
