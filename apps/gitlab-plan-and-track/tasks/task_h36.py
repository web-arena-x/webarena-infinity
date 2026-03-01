import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Sprint 24
    sprint24 = None
    for i in state.get("iterations", []):
        if i.get("title") == "Sprint 24":
            sprint24 = i
            break
    if sprint24 is None:
        return False, "Could not find iteration 'Sprint 24'."

    # Find Sprint 28
    sprint28 = None
    for i in state.get("iterations", []):
        if i.get("title") == "Sprint 28":
            sprint28 = i
            break
    if sprint28 is None:
        return False, "Could not find iteration 'Sprint 28'."

    # Expected issues (were closed in Sprint 24)
    expected_titles = [
        "Implement sidebar navigation with collapsible sections",
        "Create reusable modal dialog system",
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
        if issue.get("status") != "open":
            errors.append(f"Issue '{title}' is still closed, expected open.")
        if issue.get("iterationId") != sprint28["id"]:
            errors.append(f"Issue '{title}' not moved to Sprint 28.")

    if errors:
        return False, " ".join(errors)

    return True, "Both Sprint 24 issues reopened and moved to Sprint 28."
