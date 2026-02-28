import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    labels = state.get("labels", [])

    old_label = next((l for l in labels if l.get("title") == "good-first-issue"), None)
    if old_label is not None:
        return False, "Label 'good-first-issue' still exists; it should have been renamed."

    new_label = next((l for l in labels if l.get("title") == "beginner-friendly"), None)
    if new_label is None:
        return False, "Label 'beginner-friendly' not found."

    return True, "Label 'good-first-issue' no longer exists and label 'beginner-friendly' exists."
