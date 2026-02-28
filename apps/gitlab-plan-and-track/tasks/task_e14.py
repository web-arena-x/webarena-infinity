import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    labels = state.get("labels", [])

    old_label = next((l for l in labels if l.get("title") == "good-first-issue"), None)
    if old_label is not None:
        return False, "Label 'good-first-issue' still exists but should have been renamed."

    new_label = next((l for l in labels if l.get("title") == "starter-issue"), None)
    if new_label is None:
        return False, "Label 'starter-issue' does not exist. The rename did not complete successfully."

    return True, "Label 'good-first-issue' has been renamed to 'starter-issue'."
