import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    labels = state.get("labels", [])

    testing_label = next((l for l in labels if l.get("title") == "testing"), None)
    if testing_label is not None:
        return False, "Label 'testing' still exists; it should have been deleted."

    return True, "Label 'testing' has been deleted."
