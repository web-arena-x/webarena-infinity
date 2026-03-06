import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check that Codeine allergy has been removed
    current_patient = state.get("currentPatient", {})
    allergies = current_patient.get("allergies", [])

    for allergy in allergies:
        if allergy.get("allergen") == "Codeine":
            return False, "Codeine allergy still present in currentPatient.allergies"

    if len(allergies) != 3:
        return False, f"Expected 3 allergies after removing Codeine, found {len(allergies)}"

    return True, "Codeine allergy removed successfully; 3 allergies remain"
