import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Remove antibiotics from favorites, add Duloxetine + Pregabalin, Amazon Pharmacy, disable eRx."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []
    settings = state.get("settings", {})
    favs = settings.get("favoritesDrugIds", [])

    # Amoxicillin (drug_025) removed from favorites
    if "drug_025" in favs:
        errors.append("Amoxicillin (drug_025) is still in the favorites list.")

    # Azithromycin (drug_028) removed from favorites
    if "drug_028" in favs:
        errors.append("Azithromycin (drug_028) is still in the favorites list.")

    # Duloxetine (drug_035) added to favorites
    if "drug_035" not in favs:
        errors.append("Duloxetine (drug_035) was not added to the favorites list.")

    # Pregabalin (drug_037) added to favorites
    if "drug_037" not in favs:
        errors.append("Pregabalin (drug_037) was not added to the favorites list.")

    # Default pharmacy -> Amazon Pharmacy (pharm_013)
    if settings.get("defaultPharmacy") != "pharm_013":
        errors.append(f"Expected defaultPharmacy 'pharm_013' (Amazon Pharmacy), got '{settings.get('defaultPharmacy')}'.")

    # eRx disabled
    if settings.get("eRxEnabled") is not False:
        errors.append(f"Expected eRxEnabled False, got {settings.get('eRxEnabled')}.")

    if errors:
        return False, " ".join(errors)
    return True, "Antibiotics removed from favorites, Duloxetine and Pregabalin added, Amazon Pharmacy set, eRx disabled."
