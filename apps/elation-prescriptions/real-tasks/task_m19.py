import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Find the Amlodipine 5mg template (tpl_012)
    rx_templates = state.get("rxTemplates", [])
    amlodipine_template = None
    for tpl in rx_templates:
        if tpl.get("medicationName") == "Amlodipine 5mg tablet":
            amlodipine_template = tpl
            break

    if amlodipine_template is None:
        return False, "Amlodipine 5mg tablet template not found in rxTemplates"

    # Check sig is exactly "Take 1 tablet by mouth twice daily"
    sig = amlodipine_template.get("sig", "")
    if sig != "Take 1 tablet by mouth twice daily":
        return False, f"Amlodipine 5mg template sig is '{sig}', expected 'Take 1 tablet by mouth twice daily'"

    return True, "Amlodipine 5mg Rx template sig updated to 'Take 1 tablet by mouth twice daily'"
