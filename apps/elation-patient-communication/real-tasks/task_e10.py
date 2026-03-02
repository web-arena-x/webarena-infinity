import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    practice_settings = state.get("practiceSettings", {})
    cpt_codes = practice_settings.get("cptCodes", [])

    for entry in cpt_codes:
        if entry.get("code") == "99423":
            return False, "CPT code 99423 still exists in practiceSettings.cptCodes."

    return True, "CPT code 99423 has been removed."
