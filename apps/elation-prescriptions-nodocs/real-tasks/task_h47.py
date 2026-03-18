import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Erythromycin allergy patient (Jessica): discontinue antibiotic, increase SSRI to 40mg."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    if state.get("currentPatientId") != "pat_005":
        errors.append(f"Expected currentPatientId 'pat_005' (Jessica Morales), got '{state.get('currentPatientId')}'.")

    # rx_025 Cephalexin -> discontinued
    rx_025 = next((r for r in state["prescriptions"] if r["id"] == "rx_025"), None)
    if not rx_025:
        errors.append("Prescription rx_025 (Cephalexin) not found.")
    else:
        if rx_025.get("status") != "discontinued":
            errors.append(f"Expected rx_025 (Cephalexin) status 'discontinued', got '{rx_025.get('status')}'.")

    # rx_026 Fluoxetine dosage -> 40mg
    rx_026 = next((r for r in state["prescriptions"] if r["id"] == "rx_026"), None)
    if not rx_026:
        errors.append("Prescription rx_026 (Fluoxetine) not found.")
    else:
        if rx_026.get("dosage") != "40mg":
            errors.append(f"Expected rx_026 (Fluoxetine) dosage '40mg', got '{rx_026.get('dosage')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "Jessica's Cephalexin discontinued and Fluoxetine increased to 40mg."
