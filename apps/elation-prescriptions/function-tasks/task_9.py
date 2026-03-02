import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the Latex allergy was removed from the patient's allergies."""
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

    # Check that no allergy with allergen='Latex' exists
    for allergy in allergies:
        if allergy.get("allergen") == "Latex":
            return False, "Latex allergy still exists in currentPatient.allergies"

    # Verify count is 3 (was 4 in seed: Penicillin, Sulfonamides, Codeine, Latex)
    allergy_count = len(allergies)
    if allergy_count != 3:
        return False, f"Expected 3 allergies after removing Latex (seed had 4), but found {allergy_count}"

    return True, "Latex allergy removed successfully. Allergy count is now 3."
