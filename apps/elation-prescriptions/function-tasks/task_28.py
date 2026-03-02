import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    template_name = "Prednisone 10mg tablet (taper)"

    rx_templates = state.get("rxTemplates", [])

    # Check that the template no longer exists
    match = [t for t in rx_templates if t.get("medicationName") == template_name]
    if match:
        return False, f"Template '{template_name}' still exists in rxTemplates. Expected it to be deleted."

    # Verify count is 11 (was 12 in seed)
    count = len(rx_templates)
    if count != 11:
        return False, f"rxTemplates count is {count}, expected 11 (was 12 in seed, minus 1 deleted)."

    return True, f"Template '{template_name}' successfully deleted. rxTemplates count is 11."
