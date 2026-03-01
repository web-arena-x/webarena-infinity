import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Backlog milestone
    backlog = None
    for m in state.get("milestones", []):
        if m.get("title") == "Backlog":
            backlog = m
            break
    if backlog is None:
        return False, "Could not find milestone 'Backlog'."

    # Find Documentation Overhaul epic
    doc_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Documentation Overhaul":
            doc_epic = e
            break
    if doc_epic is None:
        return False, "Could not find epic 'Documentation Overhaul'."

    backlog_id = backlog["id"]
    doc_id = doc_epic["id"]

    # These are the issues that should have been moved (open, no epic, no milestone in seed)
    expected_titles = [
        "File upload fails silently for files > 50MB",
        "Implement retry mechanism for failed API calls",
        "Fix dropdown menu position clipping at viewport edges",
        "Fix typo in 404 error page message",
        "Add tooltip to truncated sidebar labels",
    ]

    errors = []
    for title in expected_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if issue.get("milestoneId") != backlog_id:
            errors.append(f"Issue '{title}' not in Backlog milestone.")
        if issue.get("epicId") != doc_id:
            errors.append(f"Issue '{title}' not in Documentation Overhaul epic.")

    if errors:
        return False, " ".join(errors)

    return True, f"All {len(expected_titles)} orphaned issues moved to Backlog milestone and Documentation Overhaul epic."
