import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Favorites cleanup + prescribe Duloxetine 60mg."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []
    favs = state.get("settings", {}).get("favoritesDrugIds", [])

    # Ibuprofen (drug_043) removed
    if "drug_043" in favs:
        errors.append("Ibuprofen (drug_043) is still in favorites.")
    # Prednisone (drug_045) removed
    if "drug_045" in favs:
        errors.append("Prednisone (drug_045) is still in favorites.")
    # Gabapentin (drug_036) added
    if "drug_036" not in favs:
        errors.append("Gabapentin (drug_036) not found in favorites.")
    # Duloxetine (drug_035) added
    if "drug_035" not in favs:
        errors.append("Duloxetine (drug_035) not found in favorites.")

    # New Duloxetine prescription for Margaret
    seed_ids = {f"rx_{str(i).zfill(3)}" for i in range(1, 31)}
    matches = [
        rx for rx in state["prescriptions"]
        if rx["id"] not in seed_ids
        and rx.get("patientId") == "pat_001"
        and "duloxetine" in rx.get("drugName", "").lower()
    ]
    if not matches:
        errors.append("No new Duloxetine prescription found for Margaret (pat_001).")
    else:
        new_rx = matches[0]
        if "60mg" not in new_rx.get("formStrength", "").lower().replace(" ", ""):
            errors.append(f"Expected formStrength containing '60mg', got '{new_rx.get('formStrength')}'.")
        if new_rx.get("frequency") != "Once daily":
            errors.append(f"Expected frequency 'Once daily', got '{new_rx.get('frequency')}'.")
        if new_rx.get("quantity") != 30:
            errors.append(f"Expected quantity 30, got {new_rx.get('quantity')}.")
        if new_rx.get("refillsTotal") != 3:
            errors.append(f"Expected refillsTotal 3, got {new_rx.get('refillsTotal')}.")
        if new_rx.get("pharmacyId") != "pharm_001":
            errors.append(f"Expected pharmacyId 'pharm_001' (CVS), got '{new_rx.get('pharmacyId')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "Favorites updated and Duloxetine 60mg prescribed correctly."
