import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    target_pharmacy_name = "Walgreens #7892"

    # Look up the pharmacy by name to get its id
    pharmacies = state.get("pharmacies", [])
    pharmacy = next((p for p in pharmacies if p.get("name") == target_pharmacy_name), None)
    if pharmacy is None:
        return False, f"Could not find pharmacy with name '{target_pharmacy_name}' in pharmacies list."

    expected_id = pharmacy.get("id")

    # Check settings
    settings = state.get("settings", {})
    actual_id = settings.get("defaultPharmacyId")

    if actual_id != expected_id:
        return False, f"defaultPharmacyId is '{actual_id}', expected '{expected_id}' (for '{target_pharmacy_name}')."

    return True, f"defaultPharmacyId successfully changed to '{expected_id}' ({target_pharmacy_name})."
