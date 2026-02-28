import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find label "accessibility" by title
    accessibility_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "accessibility":
            accessibility_label = lbl
            break
    if accessibility_label is None:
        return False, "Could not find label 'accessibility' in state."
    accessibility_label_id = accessibility_label["id"]

    # Find the epic "Accessibility Initiative"
    target_epic = None
    for epic in state.get("epics", []):
        if epic.get("title") == "Accessibility Initiative":
            target_epic = epic
            break
    if target_epic is None:
        return False, "Could not find epic 'Accessibility Initiative'."

    # Check that the accessibility label is applied to this epic
    epic_labels = target_epic.get("labels", [])
    if accessibility_label_id not in epic_labels:
        return False, f"Epic 'Accessibility Initiative' does not have the 'accessibility' label."

    # Find ALL issues that have the accessibility label
    issues_with_label = []
    for issue in state.get("issues", []):
        if accessibility_label_id in issue.get("labels", []):
            issues_with_label.append(issue)

    if len(issues_with_label) < 2:
        return False, f"Expected at least 2 issues with the 'accessibility' label, found {len(issues_with_label)}."

    # Check each such issue has epicId == the new epic's id
    epic_id = target_epic["id"]
    for issue in issues_with_label:
        if issue.get("epicId") != epic_id:
            return False, f"Issue '{issue.get('title')}' with accessibility label does not belong to the 'Accessibility Initiative' epic."

    return True, f"Epic 'Accessibility Initiative' created with accessibility label, and {len(issues_with_label)} accessibility issues added to it."
