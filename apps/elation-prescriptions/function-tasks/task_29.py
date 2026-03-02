import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    templates = state.get("rxTemplates", [])

    target_name = "Azithromycin 250mg tablet (Z-Pack)"
    match = [t for t in templates if t.get("medicationName") == target_name]

    if match:
        return False, f"Template with medicationName='{target_name}' still exists. Expected it to be deleted."

    if len(templates) != 11:
        return False, f"Expected 11 rxTemplates after deletion, found {len(templates)}."

    return True, f"Template '{target_name}' was successfully deleted. rxTemplates count is 11."
