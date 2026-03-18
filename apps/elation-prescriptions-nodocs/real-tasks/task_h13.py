import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    errors = []

    # Settings checks
    if settings.get("defaultPharmacy") != "pharm_006":
        errors.append(f"Expected defaultPharmacy 'pharm_006' (Costco), got '{settings.get('defaultPharmacy')}'.")
    if settings.get("defaultDaysSupply") != 90:
        errors.append(f"Expected defaultDaysSupply 90, got {settings.get('defaultDaysSupply')}.")
    if settings.get("defaultRefills") != 3:
        errors.append(f"Expected defaultRefills 3, got {settings.get('defaultRefills')}.")
    if settings.get("requireAllergyReview") is not False:
        errors.append(f"Expected requireAllergyReview False, got {settings.get('requireAllergyReview')}.")

    # New Omeprazole prescription for pat_001
    prescriptions = state.get("prescriptions", [])
    seed_ids = {f"rx_{str(i).zfill(3)}" for i in range(1, 31)}
    matches = [
        rx for rx in prescriptions
        if rx["id"] not in seed_ids
        and rx.get("patientId") == "pat_001"
        and "omeprazole" in rx.get("drugName", "").lower()
    ]

    if not matches:
        errors.append("No new Omeprazole prescription found for Margaret Chen (pat_001).")
    else:
        new_rx = matches[0]
        if "20mg" not in new_rx.get("formStrength", "").lower().replace(" ", ""):
            errors.append(f"Omeprazole: expected formStrength containing '20mg', got '{new_rx.get('formStrength')}'.")
        if new_rx.get("quantity") != 30:
            errors.append(f"Omeprazole: expected quantity 30, got {new_rx.get('quantity')}.")
        if new_rx.get("refillsTotal") != 2:
            errors.append(f"Omeprazole: expected refillsTotal 2, got {new_rx.get('refillsTotal')}.")
        if new_rx.get("pharmacyId") != "pharm_006":
            errors.append(f"Omeprazole: expected pharmacyId 'pharm_006' (Costco), got '{new_rx.get('pharmacyId')}'.")

    if errors:
        return False, " ".join(errors)

    return True, "Settings configured and Omeprazole 20mg prescribed for Margaret at Costco."
