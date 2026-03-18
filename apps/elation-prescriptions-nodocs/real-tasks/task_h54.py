import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Robert: diabetes med to 25mg, beta blocker to once daily, diuretic qty to 60."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    if state.get("currentPatientId") != "pat_006":
        errors.append(f"Expected currentPatientId 'pat_006' (Robert Fitzgerald), got '{state.get('currentPatientId')}'.")

    # rx_027 Empagliflozin (diabetes med) dosage -> 25mg
    rx_027 = next((r for r in state["prescriptions"] if r["id"] == "rx_027"), None)
    if not rx_027:
        errors.append("Prescription rx_027 (Empagliflozin) not found.")
    else:
        if rx_027.get("dosage") != "25mg":
            errors.append(f"Expected rx_027 (Empagliflozin) dosage '25mg', got '{rx_027.get('dosage')}'.")

    # rx_028 Carvedilol (beta blocker) frequency -> Once daily
    rx_028 = next((r for r in state["prescriptions"] if r["id"] == "rx_028"), None)
    if not rx_028:
        errors.append("Prescription rx_028 (Carvedilol) not found.")
    else:
        if rx_028.get("frequency") != "Once daily":
            errors.append(f"Expected rx_028 (Carvedilol) frequency 'Once daily', got '{rx_028.get('frequency')}'.")

    # rx_029 Spironolactone (potassium-sparing diuretic) quantity -> 60
    rx_029 = next((r for r in state["prescriptions"] if r["id"] == "rx_029"), None)
    if not rx_029:
        errors.append("Prescription rx_029 (Spironolactone) not found.")
    else:
        if rx_029.get("quantity") != 60:
            errors.append(f"Expected rx_029 (Spironolactone) quantity 60, got {rx_029.get('quantity')}.")

    if errors:
        return False, " ".join(errors)
    return True, "Robert's Empagliflozin 25mg, Carvedilol once daily, Spironolactone qty 60."
