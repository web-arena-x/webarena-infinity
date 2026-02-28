import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])
    milestones = state.get("milestones", [])

    target = next((i for i in issues if i["title"] == "Add mobile dark mode toggle"), None)
    if not target:
        return False, "Issue with title 'Add mobile dark mode toggle' not found."

    if target.get("description") != "Allow users to toggle dark mode on mobile devices":
        return False, f"Issue description is '{target.get('description')}', expected 'Allow users to toggle dark mode on mobile devices'."

    assignees = target.get("assignees", [])
    if "usr_2" not in assignees:
        return False, f"'usr_2' (Marcus Johnson) not in assignees: {assignees}."
    if "usr_3" not in assignees:
        return False, f"'usr_3' (Priya Patel) not in assignees: {assignees}."

    labels = target.get("labels", [])
    if "lbl_10" not in labels:
        return False, f"'lbl_10' (type::feature) not in labels: {labels}."

    mobile_ms = next((m for m in milestones if m["title"] == "v4.3 - Mobile Optimization"), None)
    if not mobile_ms:
        return False, "Milestone 'v4.3 - Mobile Optimization' not found in state."

    if target.get("milestoneId") != mobile_ms["id"]:
        return False, f"Issue milestoneId is '{target.get('milestoneId')}', expected '{mobile_ms['id']}' (v4.3 - Mobile Optimization)."

    return True, "Issue 'Add mobile dark mode toggle' exists with correct description, assignees (usr_2, usr_3), label (lbl_10), and milestone (v4.3 - Mobile Optimization)."
