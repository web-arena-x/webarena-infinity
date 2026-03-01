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

    perf_id = perf_epic["id"]

    # Find child epics
    child_epics = [e for e in state.get("epics", []) if e.get("parentEpicId") == perf_id]
    if len(child_epics) < 2:
        return False, f"Expected at least 2 child epics of Performance Initiative, found {len(child_epics)}."

    # Check health status on parent and children
    errors = []
    if perf_epic.get("healthStatus") != "needs_attention":
        errors.append(f"Performance Initiative health status is '{perf_epic.get('healthStatus')}', expected 'needs_attention'.")

    for child in child_epics:
        if child.get("healthStatus") != "needs_attention":
            errors.append(f"Child epic '{child.get('title')}' health status is '{child.get('healthStatus')}', expected 'needs_attention'.")

    if errors:
        return False, " ".join(errors)

    return True, "Performance Initiative and both child epics have health status set to needs_attention."
