import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    templates = state.get("rxTemplates", [])

    target_name = "Metformin 500mg tablet"
    template = next((t for t in templates if t.get("medicationName") == target_name), None)

    if template is None:
        return False, f"No rxTemplate found with medicationName='{target_name}'."

    actual_qty = template.get("qty")

    if actual_qty != 90:
        return False, f"Template '{target_name}' qty is {actual_qty}, expected 90."

    return True, f"Template '{target_name}' has correct qty: 90."
