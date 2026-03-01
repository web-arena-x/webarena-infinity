import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find users
    aisha = None
    nina = None
    for u in state.get("users", []):
        if u.get("name") == "Aisha Mohammed":
            aisha = u
        elif u.get("name") == "Nina Kowalski":
            nina = u

    if aisha is None:
        return False, "Could not find user 'Aisha Mohammed'."
    if nina is None:
        return False, "Could not find user 'Nina Kowalski'."

    aisha_id = aisha["id"]
    nina_id = nina["id"]

    # Find v4.0 milestone
    ms_v40 = None
    for m in state.get("milestones", []):
        if m.get("title") == "v4.0 - Platform Redesign":
            ms_v40 = m
            break
    if ms_v40 is None:
        return False, "Could not find milestone 'v4.0 - Platform Redesign'."

    # Find Sprint 28
    sprint28 = None
    for it in state.get("iterations", []):
        if it.get("title") == "Sprint 28":
            sprint28 = it
            break
    if sprint28 is None:
        return False, "Could not find iteration 'Sprint 28'."

    sprint28_id = sprint28["id"]

    # Expected issues (Aisha's open issues in v4.0 in seed)
    expected_titles = [
        "Build component library documentation site",
        "Dashboard widget layout breaks at 1440px viewport",
        "Add dark mode support for the entire application",
        "Add accessibility labels to all form inputs",
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
        if aisha_id in issue.get("assignees", []):
            errors.append(f"Issue '{title}' still assigned to Aisha Mohammed.")
        if nina_id not in issue.get("assignees", []):
            errors.append(f"Issue '{title}' not assigned to Nina Kowalski.")
        if issue.get("iterationId") != sprint28_id:
            errors.append(f"Issue '{title}' not in Sprint 28.")

    if errors:
        return False, " ".join(errors)

    return True, f"All {len(expected_titles)} of Aisha's v4.0 issues reassigned to Nina and moved to Sprint 28."
