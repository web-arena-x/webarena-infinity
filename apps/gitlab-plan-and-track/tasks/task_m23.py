import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the database connection pool issue
    target_issue = None
    for issue in state.get("issues", []):
        if issue.get("title") == "Database connection pool exhaustion under load":
            target_issue = issue
            break
    if target_issue is None:
        return False, "Could not find issue 'Database connection pool exhaustion under load'."

    # Find Chen Wei and Yuki Tanaka
    chen_wei = None
    yuki = None
    for user in state.get("users", []):
        if user.get("name") == "Chen Wei":
            chen_wei = user
        elif user.get("name") == "Yuki Tanaka":
            yuki = user

    if chen_wei is None:
        return False, "Could not find user 'Chen Wei'."
    if yuki is None:
        return False, "Could not find user 'Yuki Tanaka'."

    assignees = target_issue.get("assignees", [])

    if chen_wei["id"] not in assignees:
        return False, "Chen Wei is not assigned to the database connection pool issue."
    if yuki["id"] not in assignees:
        return False, "Yuki Tanaka is not assigned to the database connection pool issue."

    return True, "Chen Wei and Yuki Tanaka are assigned to the database connection pool issue."
