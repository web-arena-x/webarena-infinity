import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Settings for mail-order + prescribe Montelukast."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []
    settings = state.get("settings", {})

    # Check settings
    if settings.get("defaultPharmacy") != "pharm_007":
        errors.append(f"Expected defaultPharmacy 'pharm_007' (Alto), got '{settings.get('defaultPharmacy')}'.")
    if settings.get("defaultDaysSupply") != 90:
        errors.append(f"Expected defaultDaysSupply 90, got {settings.get('defaultDaysSupply')}.")
    if settings.get("defaultRefills") != 3:
        errors.append(f"Expected defaultRefills 3, got {settings.get('defaultRefills')}.")

    # Check new Montelukast prescription
    seed_ids = {f"rx_{str(i).zfill(3)}" for i in range(1, 31)}
    matches = [
        rx for rx in state["prescriptions"]
        if rx["id"] not in seed_ids
        and rx.get("patientId") == "pat_001"
        and "montelukast" in rx.get("drugName", "").lower()
    ]

    if not matches:
        errors.append("No new Montelukast prescription found for Margaret (pat_001).")
    else:
        new_rx = matches[0]
        if "10mg" not in new_rx.get("formStrength", "").lower().replace(" ", ""):
            errors.append(f"Expected formStrength containing '10mg', got '{new_rx.get('formStrength')}'.")
        if new_rx.get("frequency") != "Once daily":
            errors.append(f"Expected frequency 'Once daily', got '{new_rx.get('frequency')}'.")
        if new_rx.get("quantity") != 90:
            errors.append(f"Expected quantity 90, got {new_rx.get('quantity')}.")
        if new_rx.get("refillsTotal") != 3:
            errors.append(f"Expected refillsTotal 3, got {new_rx.get('refillsTotal')}.")
        if new_rx.get("pharmacyId") != "pharm_007":
            errors.append(f"Expected pharmacyId 'pharm_007' (Alto), got '{new_rx.get('pharmacyId')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "Mail-order settings configured and Montelukast prescribed correctly."
