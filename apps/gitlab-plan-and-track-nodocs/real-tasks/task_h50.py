import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Label 'release-blocker' must exist
    label = next((l for l in state["labels"] if l["name"] == "release-blocker"), None)
    if label is None:
        return False, "Label 'release-blocker' not found."
    if label.get("color", "").lower() != "#cc0000":
        return False, f"Label 'release-blocker' color is '{label.get('color')}', expected '#cc0000'."
    label_id = label["id"]

    # Milestone 'v2.0.1 — Hotfix' must exist
    ms = next((m for m in state["milestones"] if "v2.0.1" in m.get("title", "")), None)
    if ms is None:
        return False, "Milestone 'v2.0.1 — Hotfix' not found."
    if ms.get("dueDate") != "2026-04-10":
        return False, f"Milestone dueDate is '{ms.get('dueDate')}', expected '2026-04-10'."
    ms_id = ms["id"]

    # Issues #33 and #41 must have the label and be in the new milestone
    for issue_id in [33, 41]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if label_id not in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} missing 'release-blocker' label (id {label_id}). Labels: {issue.get('labelIds')}."
        if issue.get("milestoneId") != ms_id:
            return False, f"Issue #{issue_id} milestoneId is {issue.get('milestoneId')}, expected {ms_id}."

    return True, "Label 'release-blocker' and milestone 'v2.0.1 — Hotfix' created; #33 and #41 updated."
