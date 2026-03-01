import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find label type::bug
    bug_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "type::bug":
            bug_label = lbl
            break
    if bug_label is None:
        return False, "Could not find label 'type::bug'."

    # Find v4.1 - Performance milestone
    ms = None
    for m in state.get("milestones", []):
        if m.get("title") == "v4.1 - Performance":
            ms = m
            break
    if ms is None:
        return False, "Could not find milestone 'v4.1 - Performance'."

    # Expected bug issues in this milestone (by title)
    expected_closed = [
        "Database connection pool exhaustion under load",
        "Fix race condition in concurrent issue updates",
    ]

    errors = []
    for title in expected_closed:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if issue.get("status") != "closed":
            errors.append(f"Issue '{title}' is still open, expected closed.")

    # Also verify no open bug issues remain in this milestone
    for issue in state.get("issues", []):
        if (issue.get("milestoneId") == ms["id"]
                and bug_label["id"] in issue.get("labels", [])
                and issue.get("status") == "open"):
            errors.append(f"Issue '{issue.get('title')}' is still open with type::bug in v4.1.")

    if errors:
        return False, " ".join(errors)

    return True, "All type::bug issues in v4.1 - Performance milestone are now closed."
