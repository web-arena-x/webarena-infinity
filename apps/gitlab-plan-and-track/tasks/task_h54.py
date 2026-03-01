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

    # Find labels
    lbl_high = None
    lbl_nd = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "priority::high":
            lbl_high = lbl
        elif lbl.get("title") == "needs-discussion":
            lbl_nd = lbl

    if lbl_high is None:
        return False, "Could not find label 'priority::high'."
    if lbl_nd is None:
        return False, "Could not find label 'needs-discussion'."

    errors = []

    # Check epic labels contain exactly priority::high and needs-discussion
    epic_labels = perf_epic.get("labels", [])
    if lbl_high["id"] not in epic_labels:
        errors.append("Epic missing 'priority::high' label.")
    if lbl_nd["id"] not in epic_labels:
        errors.append("Epic missing 'needs-discussion' label.")
    # Check old labels removed
    old_label_titles = {"performance", "component::backend"}
    for lbl in state.get("labels", []):
        if lbl.get("title") in old_label_titles and lbl["id"] in epic_labels:
            errors.append(f"Epic still has old label '{lbl.get('title')}'.")

    # Check child epics have at_risk health
    children = [e for e in state.get("epics", []) if e.get("parentEpicId") == perf_epic["id"]]
    if len(children) < 2:
        errors.append(f"Expected 2 child epics, found {len(children)}.")

    for child in children:
        if child.get("healthStatus") != "at_risk":
            errors.append(f"Child epic '{child.get('title')}' health is '{child.get('healthStatus')}', expected 'at_risk'.")

    if errors:
        return False, " ".join(errors)

    return True, "Performance Initiative labels replaced and both child epics set to 'at risk'."
