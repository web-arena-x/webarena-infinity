import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target = next((i for i in issues if i["title"] == "Upgrade vulnerable dependencies identified in audit"), None)
    if not target:
        return False, "Issue 'Upgrade vulnerable dependencies identified in audit' not found."

    labels = target.get("labels", [])
    if "lbl_1" not in labels:
        return False, f"'lbl_1' (priority::critical) not in labels: {labels}."
    if "lbl_2" in labels:
        return False, f"'lbl_2' (priority::high) is still in labels: {labels}. Expected it to be removed."

    return True, "Issue 'Upgrade vulnerable dependencies identified in audit' has 'priority::critical' (lbl_1) and no longer has 'priority::high' (lbl_2)."
