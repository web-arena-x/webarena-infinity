import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify default pharmacy changed to UCSF hospital pharmacy."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    pharmacies = state.get("pharmacies", [])
    settings = state.get("settings", {})

    # Find pharmacy with name containing 'UCSF'
    ucsf_pharmacies = [
        p for p in pharmacies
        if "UCSF" in p.get("name", "")
    ]

    if not ucsf_pharmacies:
        pharmacy_names = [p.get("name", "") for p in pharmacies]
        return False, (
            f"No pharmacy with name containing 'UCSF' found in state.pharmacies. "
            f"Available pharmacies: {pharmacy_names}"
        )

    ucsf_pharmacy = ucsf_pharmacies[0]
    ucsf_id = ucsf_pharmacy.get("id")

    # Check settings.defaultPharmacyId matches UCSF pharmacy
    actual_default = settings.get("defaultPharmacyId")
    if actual_default != ucsf_id:
        return False, (
            f"settings.defaultPharmacyId is '{actual_default}', expected '{ucsf_id}' "
            f"(UCSF: '{ucsf_pharmacy.get('name')}')"
        )

    return True, (
        f"Default pharmacy successfully changed to UCSF. "
        f"settings.defaultPharmacyId='{actual_default}', "
        f"pharmacy name='{ucsf_pharmacy.get('name')}'."
    )
