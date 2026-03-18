import requests


def verify(server_url: str) -> tuple[bool, str]:
    """David: deny Metoprolol refill, discontinue Metoprolol, prescribe Carvedilol."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    if state.get("currentPatientId") != "pat_002":
        errors.append(f"Expected currentPatientId 'pat_002' (David Kowalski), got '{state.get('currentPatientId')}'.")

    # rr_005 denied
    rr_005 = next((r for r in state["refillRequests"] if r["id"] == "rr_005"), None)
    if not rr_005:
        errors.append("Refill request rr_005 not found.")
    elif rr_005.get("status") != "denied":
        errors.append(f"Expected rr_005 status 'denied', got '{rr_005.get('status')}'.")

    # rx_016 discontinued
    rx_016 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_016"), None)
    if not rx_016:
        errors.append("Prescription rx_016 (Metoprolol) not found.")
    elif rx_016.get("status") != "discontinued":
        errors.append(f"Expected rx_016 status 'discontinued', got '{rx_016.get('status')}'.")

    # New Carvedilol prescription
    seed_ids = {f"rx_{str(i).zfill(3)}" for i in range(1, 31)}
    matches = [
        rx for rx in state["prescriptions"]
        if rx["id"] not in seed_ids
        and rx.get("patientId") == "pat_002"
        and "carvedilol" in rx.get("drugName", "").lower()
    ]

    if not matches:
        errors.append("No new Carvedilol prescription found for David (pat_002).")
    else:
        new_rx = matches[0]
        if "12.5mg" not in new_rx.get("formStrength", "").lower().replace(" ", ""):
            errors.append(f"Expected formStrength containing '12.5mg', got '{new_rx.get('formStrength')}'.")
        if new_rx.get("frequency") != "Twice daily":
            errors.append(f"Expected frequency 'Twice daily', got '{new_rx.get('frequency')}'.")
        if new_rx.get("quantity") != 60:
            errors.append(f"Expected quantity 60, got {new_rx.get('quantity')}.")
        if new_rx.get("refillsTotal") != 3:
            errors.append(f"Expected refillsTotal 3, got {new_rx.get('refillsTotal')}.")
        if new_rx.get("pharmacyId") != "pharm_003":
            errors.append(f"Expected pharmacyId 'pharm_003' (Rite Aid), got '{new_rx.get('pharmacyId')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "Metoprolol refill denied, Metoprolol discontinued, Carvedilol prescribed for David."
