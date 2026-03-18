import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    templates = state.get("templates", [])
    for t in templates:
        if t.get("name") == "Metrics Dashboard":
            return True, "Template 'Metrics Dashboard' exists in state templates."

    template_names = [t.get("name", "") for t in templates]
    return False, f"Template 'Metrics Dashboard' not found. Existing templates: {template_names}"
