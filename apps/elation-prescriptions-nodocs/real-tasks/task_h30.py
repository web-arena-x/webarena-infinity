import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Cross-patient antibiotics: Cipro for Margaret, Amoxicillin for Aisha."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []
    seed_ids = {f"rx_{str(i).zfill(3)}" for i in range(1, 31)}

    # New Ciprofloxacin for Margaret (pat_001)
    cipro = [
        rx for rx in state["prescriptions"]
        if rx["id"] not in seed_ids
        and rx.get("patientId") == "pat_001"
        and "ciprofloxacin" in rx.get("drugName", "").lower()
    ]
    if not cipro:
        errors.append("No new Ciprofloxacin prescription found for Margaret (pat_001).")
    else:
        rx = cipro[0]
        if "500mg" not in rx.get("formStrength", "").lower().replace(" ", ""):
            errors.append(f"Expected Cipro formStrength containing '500mg', got '{rx.get('formStrength')}'.")
        if rx.get("frequency") != "Twice daily":
            errors.append(f"Expected Cipro frequency 'Twice daily', got '{rx.get('frequency')}'.")
        if rx.get("quantity") != 14:
            errors.append(f"Expected Cipro quantity 14, got {rx.get('quantity')}.")
        if rx.get("refillsTotal") != 0:
            errors.append(f"Expected Cipro refillsTotal 0, got {rx.get('refillsTotal')}.")
        if rx.get("pharmacyId") != "pharm_001":
            errors.append(f"Expected Cipro pharmacyId 'pharm_001' (CVS), got '{rx.get('pharmacyId')}'.")

    # New Amoxicillin for Aisha (pat_003)
    amox = [
        rx for rx in state["prescriptions"]
        if rx["id"] not in seed_ids
        and rx.get("patientId") == "pat_003"
        and "amoxicillin" in rx.get("drugName", "").lower()
    ]
    if not amox:
        errors.append("No new Amoxicillin prescription found for Aisha (pat_003).")
    else:
        rx = amox[0]
        if "500mg" not in rx.get("formStrength", "").lower().replace(" ", ""):
            errors.append(f"Expected Amoxicillin formStrength containing '500mg', got '{rx.get('formStrength')}'.")
        if rx.get("frequency") != "Three times daily":
            errors.append(f"Expected Amoxicillin frequency 'Three times daily', got '{rx.get('frequency')}'.")
        if rx.get("quantity") != 30:
            errors.append(f"Expected Amoxicillin quantity 30, got {rx.get('quantity')}.")
        if rx.get("refillsTotal") != 0:
            errors.append(f"Expected Amoxicillin refillsTotal 0, got {rx.get('refillsTotal')}.")
        if rx.get("pharmacyId") != "pharm_002":
            errors.append(f"Expected Amoxicillin pharmacyId 'pharm_002' (Walgreens), got '{rx.get('pharmacyId')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "Ciprofloxacin prescribed for Margaret and Amoxicillin prescribed for Aisha."
