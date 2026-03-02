import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    cpt_codes = state.get("practiceSettings", {}).get("cptCodes", [])
    entry = None
    for c in cpt_codes:
        if c.get("code") == "99215":
            entry = c
            break

    if entry is None:
        return False, "CPT code 99215 not found in practice settings."

    description = entry.get("description")
    if not description:
        return False, "CPT code 99215 exists but has no description."

    return True, "CPT code 99215 has been added."
