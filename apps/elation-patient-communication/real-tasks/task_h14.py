import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    practice_settings = state.get("practiceSettings", {})
    cpt_codes = practice_settings.get("cptCodes", [])

    codes_to_remove = {"99421", "99422", "99423"}
    code_to_add = "99458"

    # Check removed codes are gone
    remaining_removed = []
    for entry in cpt_codes:
        code = str(entry.get("code", ""))
        if code in codes_to_remove:
            remaining_removed.append(code)

    if remaining_removed:
        return False, (
            f"Online digital E/M codes still present: {', '.join(remaining_removed)}."
        )

    # Check 99458 was added
    code_values = [str(entry.get("code", "")) for entry in cpt_codes]
    if code_to_add not in code_values:
        return False, f"CPT code {code_to_add} was not added."

    # Check at least 10 codes remain (13 - 3 + 1 = 11, but allow some margin)
    if len(cpt_codes) < 10:
        return False, (
            f"Only {len(cpt_codes)} CPT codes remain, expected at least 10. "
            f"Other codes may have been incorrectly removed."
        )

    return True, "Online digital E/M codes replaced with telehealth code 99458."
