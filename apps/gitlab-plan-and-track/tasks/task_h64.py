import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find James O'Brien
    james = None
    for u in state.get("users", []):
        if u.get("name") == "James O'Brien":
            james = u
            break
    if james is None:
        return False, "Could not find user 'James O'Brien'."

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
    # Issues that originally had milestones should have health on_track
    with_milestone_titles = [
        "Migrate projects API to v3",
        "Implement Content Security Policy headers",
        "Implement audit logging for admin actions",
        "Add project archival functionality",
        "Implement two-factor authentication with TOTP",
        "Migrate user authentication from sessions to JWT",
    ]
    for title in with_milestone_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if issue.get("healthStatus") != "on_track":
            errors.append(
                f"Issue '{title}' health is '{issue.get('healthStatus')}', expected 'on_track'."
            )

    # The issue without a milestone should now be in Backlog with needs-discussion
    no_ms_title = "File upload fails silently for files > 50MB"
    issue = None
    for i in state.get("issues", []):
        if i.get("title") == no_ms_title:
            issue = i
            break
    if issue is None:
        errors.append(f"Could not find issue '{no_ms_title}'.")
    else:
        if issue.get("milestoneId") != backlog["id"]:
            errors.append(
                f"Issue '{no_ms_title}' should be in Backlog milestone."
            )
        if nd_label["id"] not in issue.get("labels", []):
            errors.append(
                f"Issue '{no_ms_title}' missing 'needs-discussion' label."
            )

    if errors:
        return False, " ".join(errors)

    return True, "All James O'Brien issues updated: 6 set to on_track, 1 moved to Backlog with needs-discussion."
