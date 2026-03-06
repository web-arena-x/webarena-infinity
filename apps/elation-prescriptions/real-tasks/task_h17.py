import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check Peanut allergy added
    allergies = state.get("currentPatient", {}).get("allergies", [])
    peanut_allergy = None
    for allergy in allergies:
        if allergy.get("allergen", "").lower() == "peanut":
            peanut_allergy = allergy
            break

    if peanut_allergy is None:
        # Also check plural form
        for allergy in allergies:
            if "peanut" in allergy.get("allergen", "").lower():
                peanut_allergy = allergy
                break

    if peanut_allergy is None:
        return False, "No Peanut allergy found in currentPatient.allergies"

    severity = peanut_allergy.get("severity", "")
    if severity != "Severe":
        return False, f"Peanut allergy severity is '{severity}', expected 'Severe'"

    allergy_type = peanut_allergy.get("type", "")
    if allergy_type != "food":
        return False, f"Peanut allergy type is '{allergy_type}', expected 'food'"

    # Check Doxycycline 100mg in temporaryMeds
    temporary_meds = state.get("temporaryMeds", [])
    doxycycline = None
    for med in temporary_meds:
        name = med.get("medicationName", "").lower()
        if "doxycycline" in name and "100mg" in name:
            doxycycline = med
            break

    if doxycycline is None:
        return False, "No Doxycycline 100mg found in temporaryMeds"

    classification = doxycycline.get("classification", "")
    if classification != "temporary":
        return False, f"Doxycycline classification is '{classification}', expected 'temporary'"

    pharmacy_id = doxycycline.get("pharmacyId", "")
    pharmacy_name = doxycycline.get("pharmacyName", "")
    if pharmacy_id != "pharm_001" and "cvs" not in pharmacy_name.lower():
        return False, f"Doxycycline pharmacy is '{pharmacy_name}' ({pharmacy_id}), expected CVS Pharmacy #4521 (pharm_001)"

    return True, "Peanut allergy added (Severe, food) and Doxycycline 100mg prescribed as temporary at CVS #4521"
