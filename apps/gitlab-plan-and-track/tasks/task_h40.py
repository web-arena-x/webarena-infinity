import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the new label
    review_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "needs-review":
            review_label = lbl
            break
    if review_label is None:
        return False, "Could not find label 'needs-review'."

    # Check color
    if review_label.get("color") != "#fbca04":
        return False, f"Label color is '{review_label.get('color')}', expected '#fbca04'."

    review_id = review_label["id"]

    # Find Marcus Johnson
    marcus = None
    for user in state.get("users", []):
        if user.get("name") == "Marcus Johnson":
            marcus = user
            break
    if marcus is None:
        return False, "Could not find user 'Marcus Johnson'."

    # Find all open issues assigned to Marcus
    marcus_issues = [i for i in state.get("issues", [])
                     if marcus["id"] in i.get("assignees", []) and i.get("status") == "open"]
    if len(marcus_issues) < 2:
        return False, f"Expected at least 2 open issues assigned to Marcus Johnson, found {len(marcus_issues)}."

    # Check each has the needs-review label
    errors = []
    for issue in marcus_issues:
        if review_id not in issue.get("labels", []):
            errors.append(f"Issue '{issue.get('title')}' missing 'needs-review' label.")

    if errors:
        return False, " ".join(errors)

    return True, f"Label 'needs-review' created with color #fbca04 and applied to {len(marcus_issues)} of Marcus Johnson's issues."
