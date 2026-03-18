import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rr_002 (Metformin refill) should be denied with reason containing "lab"
    refill_requests = state.get("refillRequests", [])
    rr_002 = None
    for rr in refill_requests:
        if rr.get("id") == "rr_002":
            rr_002 = rr
            break

    if rr_002 is None:
        errors.append("Refill request rr_002 (Metformin) not found.")
    else:
        if rr_002.get("status") != "denied":
            errors.append(f"Expected rr_002 status 'denied', got '{rr_002.get('status')}'.")
        deny_reason = str(rr_002.get("denyReason", ""))
        if "lab" not in deny_reason.lower():
            errors.append(f"Expected rr_002 denyReason to contain 'lab', got '{deny_reason}'.")

    # rx_003 (Metformin 1000mg) should be discontinued
    prescriptions = state.get("prescriptions", [])
    rx_003 = None
    for rx in prescriptions:
        if rx.get("id") == "rx_003":
            rx_003 = rx
            break

    if rx_003 is None:
        errors.append("Prescription rx_003 (Metformin 1000mg) not found.")
    elif rx_003.get("status") != "discontinued":
        errors.append(f"Expected rx_003 status 'discontinued', got '{rx_003.get('status')}'.")

    # New Metformin ER prescription for pat_001
    seed_ids = {f"rx_{str(i).zfill(3)}" for i in range(1, 31)}
    matches = [
        rx for rx in prescriptions
        if rx["id"] not in seed_ids
        and rx.get("patientId") == "pat_001"
        and "metformin" in rx.get("drugName", "").lower()
    ]

    if not matches:
        errors.append("No new Metformin ER prescription found for Margaret Chen (pat_001).")
    else:
        new_rx = matches[0]
        if "500mg" not in new_rx.get("formStrength", "").lower().replace(" ", ""):
            errors.append(f"Metformin ER: expected formStrength containing '500mg', got '{new_rx.get('formStrength')}'.")
        if new_rx.get("frequency") != "Once daily":
            errors.append(f"Metformin ER: expected frequency 'Once daily', got '{new_rx.get('frequency')}'.")
        if new_rx.get("quantity") != 30:
            errors.append(f"Metformin ER: expected quantity 30, got {new_rx.get('quantity')}.")
        if new_rx.get("refillsTotal") != 5:
            errors.append(f"Metformin ER: expected refillsTotal 5, got {new_rx.get('refillsTotal')}.")
        if new_rx.get("pharmacyId") != "pharm_001":
            errors.append(f"Metformin ER: expected pharmacyId 'pharm_001' (CVS), got '{new_rx.get('pharmacyId')}'.")

    if errors:
        return False, " ".join(errors)

    return True, "Metformin refill denied, old Metformin discontinued, new Metformin ER 500mg prescribed."
