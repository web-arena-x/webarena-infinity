import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    match = [s for s in state["textStyles"] if s["name"] == "Heading/H4"]
    if not match:
        return False, "Text style 'Heading/H4' not found."

    style = match[0]
    if style.get("description") != "Quaternary heading":
        return False, f"Expected description 'Quaternary heading', got '{style.get('description')}'."

    return True, "Text style 'Heading/H4' created with correct description."
