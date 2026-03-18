import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Deny Margaret's Metformin refill, hold David's Metformin, increase Robert's Jardiance to 25mg."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rr_002 Margaret's Metformin refill -> denied
    rr_002 = next((r for r in state["refillRequests"] if r["id"] == "rr_002"), None)
    if not rr_002:
        errors.append("Refill request rr_002 not found.")
    else:
        if rr_002.get("status") != "denied":
            errors.append(f"Expected rr_002 (Metformin refill) status 'denied', got '{rr_002.get('status')}'.")
        elif "lab" not in rr_002.get("denyReason", "").lower():
            errors.append(f"Expected rr_002 denyReason to mention 'lab', got '{rr_002.get('denyReason')}'.")

    # rx_019 David's Metformin -> on-hold
    rx_019 = next((r for r in state["prescriptions"] if r["id"] == "rx_019"), None)
    if not rx_019:
        errors.append("Prescription rx_019 (David's Metformin) not found.")
    else:
        if rx_019.get("status") != "on-hold":
            errors.append(f"Expected rx_019 (David's Metformin) status 'on-hold', got '{rx_019.get('status')}'.")

    # Final patient should be Robert Fitzgerald
    if state.get("currentPatientId") != "pat_006":
        errors.append(f"Expected currentPatientId 'pat_006' (Robert Fitzgerald), got '{state.get('currentPatientId')}'.")

    # rx_027 Robert's Empagliflozin (Jardiance) -> dosage 25mg
    rx_027 = next((r for r in state["prescriptions"] if r["id"] == "rx_027"), None)
    if not rx_027:
        errors.append("Prescription rx_027 (Empagliflozin) not found.")
    else:
        if rx_027.get("dosage") != "25mg":
            errors.append(f"Expected rx_027 (Empagliflozin) dosage '25mg', got '{rx_027.get('dosage')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "Metformin refill denied, David's Metformin on hold, Robert's Jardiance increased to 25mg."
