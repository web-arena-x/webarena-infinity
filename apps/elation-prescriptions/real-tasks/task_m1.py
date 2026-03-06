import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check currentPatient.allergies for an Ibuprofen allergy
    allergies = state.get("currentPatient", {}).get("allergies", [])
    ibuprofen_allergy = None
    for allergy in allergies:
        if allergy.get("allergen", "").lower() == "ibuprofen":
            ibuprofen_allergy = allergy
            break

    if ibuprofen_allergy is None:
        return False, "No Ibuprofen allergy found in currentPatient.allergies"

    # Check reaction contains "GI bleeding"
    reaction = ibuprofen_allergy.get("reaction", "")
    if "gi bleeding" not in reaction.lower():
        return False, f"Ibuprofen allergy reaction is '{reaction}', expected it to contain 'GI bleeding'"

    # Check severity is Moderate
    severity = ibuprofen_allergy.get("severity", "")
    if severity != "Moderate":
        return False, f"Ibuprofen allergy severity is '{severity}', expected 'Moderate'"

    # Check type is drug
    allergy_type = ibuprofen_allergy.get("type", "")
    if allergy_type != "drug":
        return False, f"Ibuprofen allergy type is '{allergy_type}', expected 'drug'"

    return True, "Ibuprofen allergy added successfully with GI bleeding reaction, Moderate severity, drug type"
