import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    templates = state.get("rxTemplates", [])

    target_name = "Lisinopril 10mg tablet"
    template = next((t for t in templates if t.get("medicationName") == target_name), None)

    if template is None:
        return False, f"No rxTemplate found with medicationName='{target_name}'."

    expected_sig = "Take 1 tablet by mouth once daily in the morning"
    actual_sig = template.get("sig")

    if actual_sig != expected_sig:
        return False, f"Template '{target_name}' sig is '{actual_sig}', expected '{expected_sig}'."

    return True, f"Template '{target_name}' has correct sig: '{expected_sig}'."
