import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Margaret's DAW prescription: quantity to 90, days supply to 90."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rx_004 Levothyroxine is the only DAW prescription
    rx_004 = next((r for r in state["prescriptions"] if r["id"] == "rx_004"), None)
    if not rx_004:
        errors.append("Prescription rx_004 (Levothyroxine) not found.")
    else:
        if rx_004.get("quantity") != 90:
            errors.append(f"Expected rx_004 quantity 90, got {rx_004.get('quantity')}.")
        if rx_004.get("daysSupply") != 90:
            errors.append(f"Expected rx_004 daysSupply 90, got {rx_004.get('daysSupply')}.")

    if errors:
        return False, " ".join(errors)
    return True, "Levothyroxine (DAW) quantity and days supply updated to 90."
