import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Performance Initiative epic
    perf_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Performance Initiative":
            perf_epic = e
            break
    if perf_epic is None:
        return False, "Could not find epic 'Performance Initiative'."

    # Find child epics
    db_epic = None
    cache_epic = None
    for e in state.get("epics", []):
        if e.get("parentEpicId") == perf_epic["id"]:
            if e.get("title") == "Database Optimization":
                db_epic = e
            elif e.get("title") == "Caching Layer Implementation":
                cache_epic = e

    if db_epic is None:
        return False, "Could not find child epic 'Database Optimization'."
    if cache_epic is None:
        return False, "Could not find child epic 'Caching Layer Implementation'."

    errors = []

    # Database Optimization has more issues (5 vs 2) -> set weight to 13
    db_issues = [i for i in state.get("issues", []) if i.get("epicId") == db_epic["id"]]
    for issue in db_issues:
        if issue.get("weight") != 13:
            errors.append(f"Issue '{issue.get('title')}' (DB Optimization) weight is {issue.get('weight')}, expected 13.")

    # Caching Layer has fewer issues (2) -> close all open
    cache_issues = [i for i in state.get("issues", []) if i.get("epicId") == cache_epic["id"]]
    for issue in cache_issues:
        if issue.get("status") != "closed":
            errors.append(f"Issue '{issue.get('title')}' (Caching Layer) should be closed, got '{issue.get('status')}'.")

    if errors:
        return False, " ".join(errors)

    return True, f"DB Optimization issues ({len(db_issues)}) set to weight 13; Caching Layer issues ({len(cache_issues)}) closed."
