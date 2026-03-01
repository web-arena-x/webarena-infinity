import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Platform Redesign epic
    pr_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Platform Redesign":
            pr_epic = e
            break
    if pr_epic is None:
        return False, "Could not find epic 'Platform Redesign'."

    # Find child epics
    children = [e for e in state.get("epics", []) if e.get("parentEpicId") == pr_epic["id"]]
    if len(children) < 2:
        return False, f"Expected 2 child epics of Platform Redesign, found {len(children)}."

    # API v3 Migration has fewer open issues (3) vs Frontend Modernization (5)
    api_epic = None
    fe_epic = None
    for c in children:
        if c.get("title") == "API v3 Migration":
            api_epic = c
        elif c.get("title") == "Frontend Modernization":
            fe_epic = c

    if api_epic is None:
        return False, "Could not find child epic 'API v3 Migration'."
    if fe_epic is None:
        return False, "Could not find child epic 'Frontend Modernization'."

    errors = []

    # API v3 Migration should be closed (fewer open issues)
    if api_epic.get("status") != "closed":
        errors.append(f"Epic 'API v3 Migration' should be closed, got '{api_epic.get('status')}'.")

    # Frontend Modernization should remain open
    if fe_epic.get("status") != "open":
        errors.append(f"Epic 'Frontend Modernization' should remain open, got '{fe_epic.get('status')}'.")

    if errors:
        return False, " ".join(errors)

    return True, "API v3 Migration epic (fewer open issues) closed; Frontend Modernization remains open."
