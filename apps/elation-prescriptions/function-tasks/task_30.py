import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    templates = state.get("rxTemplates", [])

    match = [
        t for t in templates
        if "Levothyroxine" in t.get("medicationName", "")
        and "50mcg" in t.get("medicationName", "")
    ]

    if not match:
        return False, "No rxTemplate found with medicationName containing 'Levothyroxine' and '50mcg'."

    template = match[0]
    expected_sig = "Take 1 tablet by mouth once daily on empty stomach"
    errors = []

    if template.get("sig") != expected_sig:
        errors.append(f"sig: expected '{expected_sig}', got '{template.get('sig')}'")

    if template.get("qty") != 30:
        errors.append(f"qty: expected 30, got {template.get('qty')}")

    if template.get("refills") != 5:
        errors.append(f"refills: expected 5, got {template.get('refills')}")

    if template.get("daysSupply") != 30:
        errors.append(f"daysSupply: expected 30, got {template.get('daysSupply')}")

    if errors:
        return False, f"Levothyroxine 50mcg template found but has incorrect fields: {'; '.join(errors)}"

    return True, "Levothyroxine 50mcg template exists with correct sig, qty=30, refills=5, daysSupply=30."
