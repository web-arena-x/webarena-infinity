import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find relevant labels
    label_map = {}
    for lbl in state.get("labels", []):
        label_map[lbl["title"]] = lbl["id"]

    perf_id = label_map.get("performance")
    db_id = label_map.get("component::database")
    fe_id = label_map.get("component::frontend")
    crit_id = label_map.get("priority::critical")
    high_id = label_map.get("priority::high")
    med_id = label_map.get("priority::medium")

    if not all([perf_id, db_id, fe_id, crit_id, high_id, med_id]):
        return False, "Could not find all required labels."

    errors = []

    # Issues with performance label -> check priority based on component
    # Database issues -> critical
    db_titles = [
        "Analyze and optimize slow queries from APM logs",
        "Add composite indexes for frequently joined tables",
        "Optimize issue list query to use keyset pagination",
        "Database connection pool exhaustion under load",
    ]
    for title in db_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if crit_id not in issue.get("labels", []):
            errors.append(f"Issue '{title}' missing priority::critical label.")

    # Frontend issues -> high
    fe_titles = [
        "Reduce JavaScript bundle size by 40%",
        "Implement lazy loading for images and avatars",
    ]
    for title in fe_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if high_id not in issue.get("labels", []):
            errors.append(f"Issue '{title}' missing priority::high label.")

    # Others (no database or frontend component) -> medium
    other_title = "Configure CDN for static asset delivery"
    issue = None
    for i in state.get("issues", []):
        if i.get("title") == other_title:
            issue = i
            break
    if issue is None:
        errors.append(f"Could not find issue '{other_title}'.")
    else:
        if med_id not in issue.get("labels", []):
            errors.append(f"Issue '{other_title}' missing priority::medium label.")

    if errors:
        return False, " ".join(errors)

    return True, "Performance issues prioritized: 4 critical (database), 2 high (frontend), 1 medium (other)."
