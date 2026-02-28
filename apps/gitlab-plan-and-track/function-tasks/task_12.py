import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target = next((i for i in issues if i["title"] == "Add dark mode support for the entire application"), None)
    if not target:
        return False, "Issue 'Add dark mode support for the entire application' not found."

    labels = target.get("labels", [])
    if "lbl_23" in labels:
        return False, f"'lbl_23' (UX) is still in labels: {labels}. Expected it to be removed."

    return True, "Issue 'Add dark mode support for the entire application' no longer has the 'UX' label (lbl_23)."
