import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    practice_settings = state.get("practiceSettings", {})
    cpt_codes = practice_settings.get("cptCodes", [])

    telephone_codes = {"99441", "99442", "99443"}

    # Check that no telephone E/M codes remain
    remaining_telephone = []
    for entry in cpt_codes:
        code = str(entry.get("code", ""))
        if code in telephone_codes:
            remaining_telephone.append(code)

    if remaining_telephone:
        return False, (
            f"Telephone E/M codes still present: {', '.join(remaining_telephone)}."
        )

    # Check that other CPT codes still exist (originally 13, minus 3 = 10, at least 8)
    if len(cpt_codes) < 8:
        return False, (
            f"Only {len(cpt_codes)} CPT codes remain, expected at least 8. "
            f"Other codes may have been incorrectly removed."
        )

    return True, "All telephone E/M billing codes have been removed."
