import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Backlog milestone and needs-discussion label
    backlog = None
    for m in state.get("milestones", []):
        if m.get("title") == "Backlog":
            backlog = m
            break
    if backlog is None:
        return False, "Could not find 'Backlog' milestone."

    nd_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "needs-discussion":
            nd_label = lbl
            break
    if nd_label is None:
        return False, "Could not find 'needs-discussion' label."

    errors = []

    # Issues with no assignees that originally had a milestone -> just add label
    with_ms_titles = [
        "Implement CSRF token rotation",
        "Markdown preview renders incorrectly with nested code blocks",
        "Build real-time collaborative editing for issue descriptions",
        "Add custom fields support for issues",
        "Add webhook support for issue state changes",
        "Implement GitLab Pages custom domain support",
        "Add merge request approval rules engine",
        "Add inline code suggestions in merge request reviews",
    ]
    for title in with_ms_titles:
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

    # Issues with no assignees AND no milestone -> add to Backlog + add label
    no_ms_titles = [
        "Fix typo in 404 error page message",
        "Add tooltip to truncated sidebar labels",
    ]
    for title in no_ms_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if issue.get("milestoneId") != backlog["id"]:
            errors.append(f"Issue '{title}' should be in Backlog milestone.")
        if nd_label["id"] not in issue.get("labels", []):
            errors.append(f"Issue '{title}' missing 'needs-discussion' label.")

    if errors:
        return False, " ".join(errors)

    return True, (
        f"Unassigned issues updated: {len(with_ms_titles)} got needs-discussion label, "
        f"{len(no_ms_titles)} also moved to Backlog."
    )
