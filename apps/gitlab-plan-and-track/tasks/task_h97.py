import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Find labels
    api_label = backend_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "component::api":
            api_label = lbl
        elif lbl.get("title") == "component::backend":
            backend_label = lbl
    if api_label is None:
        return False, "Could not find 'component::api' label."
    if backend_label is None:
        return False, "Could not find 'component::backend' label."

    # Find API v3 Migration epic
    api_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "API v3 Migration":
            api_epic = e
            break
    if api_epic is None:
        return False, "Could not find epic 'API v3 Migration'."

    # Check open issues in this epic
    expected_titles = [
        "Implement GraphQL gateway for v3 API",
        "Migrate projects API to v3",
        "Add rate limiting to v3 endpoints",
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
        if api_label["id"] in issue.get("labels", []):
            errors.append(f"Issue '{title}' still has 'component::api' label.")
        if backend_label["id"] not in issue.get("labels", []):
            errors.append(f"Issue '{title}' missing 'component::backend' label.")

    if errors:
        return False, " ".join(errors)

    return True, (
        "All open API v3 Migration issues: "
        "component::api replaced with component::backend."
    )
