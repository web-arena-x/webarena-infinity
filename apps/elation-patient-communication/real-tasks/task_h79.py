import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify online digital E/M codes removed and two new codes added."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    cpt_codes = state.get("practiceSettings", {}).get("cptCodes", [])
    code_values = [str(c.get("code", "")) for c in cpt_codes]

    errors = []

    # Check removed codes
    removed_codes = ["99421", "99422", "99423"]
    for code in removed_codes:
        if code in code_values:
            errors.append(f"Online digital E/M code '{code}' still present")

    # Check added codes
    if "99024" not in code_values:
        errors.append("CPT code '99024' not found in billing codes")
    if "99050" not in code_values:
        errors.append("CPT code '99050' not found in billing codes")

    if errors:
        return False, "; ".join(errors)
    return True, "Online digital E/M codes removed and codes 99024, 99050 added"
