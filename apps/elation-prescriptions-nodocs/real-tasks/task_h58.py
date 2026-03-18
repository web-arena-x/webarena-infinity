import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Latex allergy patient (William): renew Valsartan 5, insulin to 30 units, Furosemide qty 60."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    if state.get("currentPatientId") != "pat_004":
        errors.append(f"Expected currentPatientId 'pat_004' (William Thornton), got '{state.get('currentPatientId')}'.")

    # rx_022 Valsartan -> renewed with 5 refills
    rx_022 = next((r for r in state["prescriptions"] if r["id"] == "rx_022"), None)
    if not rx_022:
        errors.append("Prescription rx_022 (Valsartan) not found.")
    else:
        if rx_022.get("refillsRemaining") != 5:
            errors.append(f"Expected rx_022 (Valsartan) refillsRemaining 5, got {rx_022.get('refillsRemaining')}.")

    # rx_023 Insulin Glargine -> dosage 30 units
    rx_023 = next((r for r in state["prescriptions"] if r["id"] == "rx_023"), None)
    if not rx_023:
        errors.append("Prescription rx_023 (Insulin Glargine) not found.")
    else:
        if rx_023.get("dosage") != "30 units":
            errors.append(f"Expected rx_023 (Insulin) dosage '30 units', got '{rx_023.get('dosage')}'.")

    # rx_024 Furosemide -> quantity 60
    rx_024 = next((r for r in state["prescriptions"] if r["id"] == "rx_024"), None)
    if not rx_024:
        errors.append("Prescription rx_024 (Furosemide) not found.")
    else:
        if rx_024.get("quantity") != 60:
            errors.append(f"Expected rx_024 (Furosemide) quantity 60, got {rx_024.get('quantity')}.")

    if errors:
        return False, " ".join(errors)
    return True, "William's Valsartan renewed, insulin 30 units, Furosemide qty 60."
