import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    labels = state.get("labels", [])

    target = next((l for l in labels if l.get("title") == "needs-discussion"), None)
    if not target:
        return False, "Label with title 'needs-discussion' not found."

    color = target.get("color", "")
    if color.lower() != "#0075ca":
        return False, f"Label color is '{color}', expected '#0075ca'."

    return True, "Label 'needs-discussion' has color '#0075ca'."
