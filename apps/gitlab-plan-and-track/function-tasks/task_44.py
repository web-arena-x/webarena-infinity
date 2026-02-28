import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    epics = state.get("epics", [])

    target = next((e for e in epics if e["title"] == "Caching Layer Implementation"), None)
    if not target:
        return False, "Epic with title 'Caching Layer Implementation' not found."

    labels = target.get("labels", [])
    if "lbl_21" not in labels:
        return False, f"Label 'lbl_21' (security) not found in epic labels: {labels}."

    return True, "Epic 'Caching Layer Implementation' has label 'lbl_21' (security) in its labels."
