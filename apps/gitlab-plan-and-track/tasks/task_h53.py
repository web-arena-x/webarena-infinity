import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # The top-level epic with latest due date is Mobile App v2 (2026-11-30)
    mobile_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Mobile App v2":
            mobile_epic = e
            break
    if mobile_epic is None:
        return False, "Could not find epic 'Mobile App v2'."

    # Find needs-discussion label
    nd_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "needs-discussion":
            nd_label = lbl
            break
    if nd_label is None:
        return False, "Could not find label 'needs-discussion'."

    errors = []

    if mobile_epic.get("healthStatus") != "needs_attention":
        errors.append(f"Epic health is '{mobile_epic.get('healthStatus')}', expected 'needs_attention'.")

    if nd_label["id"] not in mobile_epic.get("labels", []):
        errors.append("Epic missing 'needs-discussion' label.")

    if errors:
        return False, " ".join(errors)

    return True, "Mobile App v2 epic (latest due date) updated with 'needs attention' health and 'needs-discussion' label."
