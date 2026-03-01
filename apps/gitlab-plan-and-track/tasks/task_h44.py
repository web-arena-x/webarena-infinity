import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the new review::pending label
    rp_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "review::pending":
            rp_label = lbl
            break
    if rp_label is None:
        return False, "Could not find label 'review::pending'."

    if rp_label.get("color") != "#7b68ee":
        return False, f"Label 'review::pending' color is '{rp_label.get('color')}', expected '#7b68ee'."

    if rp_label.get("scoped") is not True:
        return False, "Label 'review::pending' should be scoped."

    rp_id = rp_label["id"]

    # Find workflow::ready label
    ready_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "workflow::ready":
            ready_label = lbl
            break
    if ready_label is None:
        return False, "Could not find label 'workflow::ready'."

    ready_id = ready_label["id"]

    # Find all open issues with workflow::ready
    ready_issues = [i for i in state.get("issues", [])
                    if i.get("status") == "open" and ready_id in i.get("labels", [])]

    if len(ready_issues) < 2:
        return False, f"Expected at least 2 open issues with 'workflow::ready', found {len(ready_issues)}."

    errors = []
    for issue in ready_issues:
        if rp_id not in issue.get("labels", []):
            errors.append(f"Issue '{issue.get('title')}' with workflow::ready is missing 'review::pending' label.")

    if errors:
        return False, " ".join(errors)

    return True, f"Label 'review::pending' created and applied to {len(ready_issues)} workflow::ready issues."
