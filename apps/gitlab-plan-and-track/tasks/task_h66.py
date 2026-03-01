import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the 'sprint-focus' label
    sf_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "sprint-focus":
            sf_label = lbl
            break
    if sf_label is None:
        return False, "Could not find label 'sprint-focus'."

    errors = []
    if sf_label.get("color") != "#0891b2":
        errors.append(
            f"Label color is '{sf_label.get('color')}', expected '#0891b2'."
        )

    # Sprint 26 has the most open issues (10)
    sprint26 = None
    for it in state.get("iterations", []):
        if it.get("title") == "Sprint 26":
            sprint26 = it
            break
    if sprint26 is None:
        return False, "Could not find iteration 'Sprint 26'."

    sf_id = sf_label["id"]
    sprint26_issues = [i for i in state.get("issues", [])
                       if i.get("iterationId") == sprint26["id"]
                       and i.get("status") == "open"]

    labeled_count = 0
    for issue in sprint26_issues:
        if sf_id in issue.get("labels", []):
            labeled_count += 1
        else:
            errors.append(
                f"Issue '{issue.get('title')}' in Sprint 26 missing 'sprint-focus' label."
            )

    if len(sprint26_issues) < 10:
        errors.append(
            f"Expected at least 10 open issues in Sprint 26, found {len(sprint26_issues)}."
        )

    if errors:
        return False, " ".join(errors)

    return True, f"Label 'sprint-focus' created and applied to {labeled_count} Sprint 26 issues."
