import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check default pharmacy changed to Walgreens #7892 (pharm_003)
    settings = state.get("settings", {})
    default_pharmacy_id = settings.get("defaultPharmacyId")

    if default_pharmacy_id != "pharm_003":
        return False, f"settings.defaultPharmacyId is '{default_pharmacy_id}', expected 'pharm_003' (Walgreens #7892)"

    return True, "Default pharmacy changed to Walgreens #7892 successfully"
