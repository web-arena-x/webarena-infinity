import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target = next((i for i in issues if i["title"] == "Security audit: XSS in comment parser"), None)
    if not target:
        return False, "Issue with title 'Security audit: XSS in comment parser' not found."

    if target.get("confidential") is not True:
        return False, f"Issue confidential is {target.get('confidential')}, expected True."

    labels = target.get("labels", [])
    if "lbl_21" not in labels:
        return False, f"'lbl_21' (security) not in labels: {labels}."
    if "lbl_1" not in labels:
        return False, f"'lbl_1' (priority::critical) not in labels: {labels}."

    return True, "Issue 'Security audit: XSS in comment parser' exists with confidential=True and labels security (lbl_21) and priority::critical (lbl_1)."
