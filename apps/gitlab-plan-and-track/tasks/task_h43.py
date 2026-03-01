import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # The issue with the highest weight is "Build real-time collaborative editing" (weight 21)
    target = None
    for i in state.get("issues", []):
        if i.get("title") == "Build real-time collaborative editing for issue descriptions":
            target = i
            break
    if target is None:
        return False, "Could not find issue 'Build real-time collaborative editing for issue descriptions'."

    # Find Sprint 27
    sprint27 = None
    for it in state.get("iterations", []):
        if it.get("title") == "Sprint 27":
            sprint27 = it
            break
    if sprint27 is None:
        return False, "Could not find iteration 'Sprint 27'."

    # Find needs-discussion label
    nd_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "needs-discussion":
            nd_label = lbl
            break
    if nd_label is None:
        return False, "Could not find label 'needs-discussion'."

    errors = []

    if target.get("iterationId") != sprint27["id"]:
        errors.append(f"Issue iteration is '{target.get('iterationId')}', expected '{sprint27['id']}'.")

    if nd_label["id"] not in target.get("labels", []):
        errors.append("Issue is missing the 'needs-discussion' label.")

    if errors:
        return False, " ".join(errors)

    return True, "Highest-weight issue assigned to Sprint 27 with 'needs-discussion' label."
