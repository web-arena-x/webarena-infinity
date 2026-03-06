import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that CPT code 99205 has been added to the billing codes."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    practice_settings = state.get("practiceSettings")
    if practice_settings is None:
        return False, "practiceSettings not found in state"

    cpt_codes = practice_settings.get("cptCodes", [])
    found = False
    for cpt in cpt_codes:
        if str(cpt.get("code", "")) == "99205":
            found = True
            break

    if not found:
        existing_codes = [str(c.get("code", "")) for c in cpt_codes]
        return False, f"CPT code '99205' not found in billing codes. Existing codes: {existing_codes}"

    return True, "CPT code 99205 has been added to the billing codes"
