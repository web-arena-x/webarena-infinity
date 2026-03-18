import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    templates = state.get("templates", [])
    for t in templates:
        if t.get("name") == "Three Cards Layout":
            return True, "Template 'Three Cards Layout' exists in state templates."

    template_names = [t.get("name", "") for t in templates]
    return False, f"Template 'Three Cards Layout' not found. Existing templates: {template_names}"
