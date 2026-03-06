import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify telephone E/M CPT codes removed and 99205 added."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    practice_settings = state.get("practiceSettings")
    if practice_settings is None:
        return False, "practiceSettings not found in state"

    cpt_codes = practice_settings.get("cptCodes", [])
    code_values = [str(c.get("code", "")) for c in cpt_codes]

    # Telephone E/M codes that should be removed: 99441, 99442, 99443
    telephone_codes = {"99441", "99442", "99443"}
    still_present = telephone_codes.intersection(set(code_values))

    if still_present:
        return False, (
            f"Telephone E/M CPT codes still present: {', '.join(sorted(still_present))}. "
            f"These should have been removed."
        )

    # Check that 99205 was added
    if "99205" not in code_values:
        return False, (
            f"CPT code '99205' not found in billing codes. "
            f"Current codes: {code_values}"
        )

    return True, (
        "Telephone E/M CPT codes (99441, 99442, 99443) removed and "
        "code 99205 (high-complexity new patient office visit) added"
    )
