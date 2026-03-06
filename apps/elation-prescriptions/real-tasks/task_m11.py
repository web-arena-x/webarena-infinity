import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check currentPatient.allergies for Shellfish allergy
    allergies = state.get("currentPatient", {}).get("allergies", [])
    shellfish_allergy = None
    for allergy in allergies:
        if "shellfish" in allergy.get("allergen", "").lower():
            shellfish_allergy = allergy
            break

    if shellfish_allergy is None:
        return False, "No Shellfish allergy found in currentPatient.allergies"

    # Check reaction contains "hives"
    reaction = shellfish_allergy.get("reaction", "")
    if "hives" not in reaction.lower():
        return False, f"Shellfish allergy reaction is '{reaction}', expected it to contain 'hives'"

    # Check severity is Severe
    severity = shellfish_allergy.get("severity", "")
    if severity != "Severe":
        return False, f"Shellfish allergy severity is '{severity}', expected 'Severe'"

    # Check type is food
    allergy_type = shellfish_allergy.get("type", "")
    if allergy_type != "food":
        return False, f"Shellfish allergy type is '{allergy_type}', expected 'food'"

    return True, "Shellfish allergy added with hives and swelling reaction, Severe severity, food type"
