import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Frontend Modernization epic
    fe_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Frontend Modernization":
            fe_epic = e
            break
    if fe_epic is None:
        return False, "Could not find epic 'Frontend Modernization'."

    errors = []

    # Epic health should be at_risk
    if fe_epic.get("healthStatus") != "at_risk":
        errors.append(
            f"Frontend Modernization health is '{fe_epic.get('healthStatus')}', "
            f"expected 'at_risk'."
        )

    # All open issues in epic should have timeEstimate = 86400 (24h)
    expected_titles = [
        "Migrate user settings page to React",
        "Build component library documentation site",
        "Add dark mode support for the entire application",
        "Add accessibility labels to all form inputs",
        "Create reusable data table component with sorting and filtering",
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
        if issue.get("timeEstimate") != 86400:
            errors.append(
                f"Issue '{title}' time estimate is {issue.get('timeEstimate')}s, "
                f"expected 86400s (24h)."
            )

    if errors:
        return False, " ".join(errors)

    return True, (
        f"Time estimate set to 24h on {len(expected_titles)} Frontend Modernization issues; "
        f"epic health set to at_risk."
    )
