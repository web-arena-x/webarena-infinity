import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Find blocked label
    blocked_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "blocked":
            blocked_label = lbl
            break
    if blocked_label is None:
        return False, "Could not find 'blocked' label."

    # The two highest-weight issues in Sprint 26 are weight 13:
    # GraphQL gateway and dark mode
    expected_titles = [
        "Implement GraphQL gateway for v3 API",
        "Add dark mode support for the entire application",
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
        if blocked_label["id"] not in issue.get("labels", []):
            errors.append(f"Issue '{title}' missing 'blocked' label.")

    if errors:
        return False, " ".join(errors)

    return True, (
        "'blocked' label added to the two heaviest issues in Sprint 26 "
        "(GraphQL gateway and dark mode, both weight 13)."
    )
