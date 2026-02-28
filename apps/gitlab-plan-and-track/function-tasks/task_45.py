import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    epics = state.get("epics", [])

    target = next((e for e in epics if e["title"] == "Platform Redesign"), None)
    if not target:
        return False, "Epic with title 'Platform Redesign' not found."

    labels = target.get("labels", [])

    if "lbl_14" in labels:
        return False, f"Label 'lbl_14' (component::frontend) should NOT be in epic labels, but found: {labels}."

    if "lbl_10" not in labels:
        return False, f"Label 'lbl_10' should still be in epic labels, but not found: {labels}."

    if "lbl_23" not in labels:
        return False, f"Label 'lbl_23' should still be in epic labels, but not found: {labels}."

    return True, "Epic 'Platform Redesign' has 'lbl_14' removed and still contains 'lbl_10' and 'lbl_23'."
