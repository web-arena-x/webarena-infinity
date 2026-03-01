import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Find labels
    bug_label = nd_label = high_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "type::bug":
            bug_label = lbl
        elif lbl.get("title") == "needs-discussion":
            nd_label = lbl
        elif lbl.get("title") == "priority::high":
            high_label = lbl
    if bug_label is None:
        return False, "Could not find 'type::bug' label."
    if nd_label is None:
        return False, "Could not find 'needs-discussion' label."
    if high_label is None:
        return False, "Could not find 'priority::high' label."

    # Find all open issues with both type::bug and priority::high
    expected_titles = [
        "Email notifications sent with wrong timezone offset",
        "File upload fails silently for files > 50MB",
        "Database connection pool exhaustion under load",
        "Fix race condition in concurrent issue updates",
    ]

    for title in expected_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if nd_label["id"] not in issue.get("labels", []):
            errors.append(f"Issue '{title}' missing 'needs-discussion' label.")

    if errors:
        return False, " ".join(errors)

    return True, (
        f"'needs-discussion' label added to all {len(expected_titles)} open issues "
        f"with both type::bug and priority::high."
    )
