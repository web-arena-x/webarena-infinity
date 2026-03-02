import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that an environmental allergy for Bee stings was added with the correct details."""
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

    # Find allergy with allergen='Bee stings'
    bee_allergy = None
    for allergy in allergies:
        if allergy.get("allergen") == "Bee stings":
            bee_allergy = allergy
            break

    if bee_allergy is None:
        allergen_names = [a.get("allergen") for a in allergies]
        return False, f"No allergy found with allergen='Bee stings'. Current allergens: {allergen_names}"

    # Check type is 'environmental'
    allergy_type = bee_allergy.get("type")
    if allergy_type != "environmental":
        return False, f"Bee stings allergy type is '{allergy_type}', expected 'environmental'"

    # Check severity is 'Severe'
    severity = bee_allergy.get("severity")
    if severity != "Severe":
        return False, f"Bee stings allergy severity is '{severity}', expected 'Severe'"

    return True, (
        f"Bee stings environmental allergy added successfully. "
        f"type='{allergy_type}', severity='{severity}'"
    )
