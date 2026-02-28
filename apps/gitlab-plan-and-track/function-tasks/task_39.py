import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    epics = state.get("epics", [])

    target = next((e for e in epics if e.get("title") == "CI/CD Pipeline Modernization"), None)
    if not target:
        return False, "Epic with title 'CI/CD Pipeline Modernization' not found."

    status = target.get("status", "")
    if status != "open":
        return False, f"Epic status is '{status}', expected 'open'."

    labels = target.get("labels", [])
    if "lbl_18" not in labels:
        return False, f"Epic labels {labels} do not contain 'lbl_18' (component::infrastructure)."

    description = target.get("description", "")
    if "Modernize" not in description:
        return False, f"Epic description does not contain 'Modernize'. Got: '{description}'."

    return True, "Epic 'CI/CD Pipeline Modernization' exists with status 'open', label 'lbl_18', and description containing 'Modernize'."
