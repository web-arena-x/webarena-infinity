import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that a drug allergy for Ibuprofen was added with the correct details."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Get allergies from currentPatient
    current_patient = state.get("currentPatient", {})
    allergies = current_patient.get("allergies", [])

    # Find allergy with allergen='Ibuprofen'
    ibuprofen_allergy = None
    for allergy in allergies:
        if allergy.get("allergen") == "Ibuprofen":
            ibuprofen_allergy = allergy
            break

    if ibuprofen_allergy is None:
        allergen_names = [a.get("allergen") for a in allergies]
        return False, f"No allergy found with allergen='Ibuprofen'. Current allergens: {allergen_names}"

    # Check type is 'drug'
    allergy_type = ibuprofen_allergy.get("type")
    if allergy_type != "drug":
        return False, f"Ibuprofen allergy type is '{allergy_type}', expected 'drug'"

    # Check severity is 'Moderate'
    severity = ibuprofen_allergy.get("severity")
    if severity != "Moderate":
        return False, f"Ibuprofen allergy severity is '{severity}', expected 'Moderate'"

    # Check reaction contains 'Stomach upset' or 'GI bleeding'
    reaction = ibuprofen_allergy.get("reaction", "")
    has_stomach_upset = "Stomach upset" in reaction
    has_gi_bleeding = "GI bleeding" in reaction
    if not has_stomach_upset and not has_gi_bleeding:
        return False, f"Ibuprofen allergy reaction is '{reaction}', expected it to contain 'Stomach upset' or 'GI bleeding'"

    return True, (
        f"Ibuprofen drug allergy added successfully. "
        f"type='{allergy_type}', severity='{severity}', reaction='{reaction}'"
    )
