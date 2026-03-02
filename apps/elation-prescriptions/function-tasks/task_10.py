import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the Codeine allergy was removed from the patient's allergies."""
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

    # Check that no allergy with allergen='Codeine' exists
    for allergy in allergies:
        if allergy.get("allergen") == "Codeine":
            return False, "Codeine allergy still exists in currentPatient.allergies"

    return True, "Codeine allergy removed successfully. No allergy with allergen='Codeine' found."
