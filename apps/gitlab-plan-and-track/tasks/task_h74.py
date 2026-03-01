import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Chen Wei and Alex Thompson
    chen = alex = None
    for u in state.get("users", []):
        if u.get("name") == "Chen Wei":
            chen = u
        elif u.get("name") == "Alex Thompson":
            alex = u
    if chen is None:
        return False, "Could not find user 'Chen Wei'."
    if alex is None:
        return False, "Could not find user 'Alex Thompson'."

    # Find v4.0 milestone
    ms_v40 = None
    for m in state.get("milestones", []):
        if m.get("title") == "v4.0 - Platform Redesign":
            ms_v40 = m
            break
    if ms_v40 is None:
        return False, "Could not find milestone 'v4.0 - Platform Redesign'."

    errors = []

    # Issues in v4.0 should still have Chen Wei
    v40_titles = [
        "Implement GraphQL gateway for v3 API",
        "Email notifications sent with wrong timezone offset",
    ]
    for title in v40_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if chen["id"] not in issue.get("assignees", []):
            errors.append(f"Issue '{title}' should still have Chen Wei assigned.")

    # Non-v4.0 issues should be reassigned to Alex Thompson
    reassigned_titles = [
        "Add bulk operations for issue management",
        "Refactor notification service to use event-driven architecture",
        "Implement retry mechanism for failed API calls",
        "Fix race condition in concurrent issue updates",
    ]
    for title in reassigned_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if alex["id"] not in issue.get("assignees", []):
            errors.append(f"Issue '{title}' should have Alex Thompson assigned.")
        if chen["id"] in issue.get("assignees", []):
            errors.append(f"Issue '{title}' should no longer have Chen Wei assigned.")

    if errors:
        return False, " ".join(errors)

    return True, (
        f"Chen Wei's issues reassigned: {len(reassigned_titles)} to Alex Thompson, "
        f"{len(v40_titles)} in v4.0 unchanged."
    )
