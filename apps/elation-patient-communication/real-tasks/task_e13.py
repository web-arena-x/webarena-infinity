import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that CPT code 99201 has been removed from the billing codes list."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    practice_settings = state.get("practiceSettings", {})
    cpt_codes = practice_settings.get("cptCodes", [])

    for cpt in cpt_codes:
        if cpt.get("code") == "99201":
            return False, "CPT code 99201 still exists in practiceSettings.cptCodes"

    return True, "CPT code 99201 has been removed from the billing codes list"
