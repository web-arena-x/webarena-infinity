import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Security Hardening epic
    sec_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Security Hardening":
            sec_epic = e
            break
    if sec_epic is None:
        return False, "Could not find epic 'Security Hardening'."

    # Find Enterprise SSO Integration epic
    sso_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Enterprise SSO Integration":
            sso_epic = e
            break
    if sso_epic is None:
        return False, "Could not find epic 'Enterprise SSO Integration'."

    errors = []

    # Check parent
    if sso_epic.get("parentEpicId") != sec_epic["id"]:
        errors.append(f"Enterprise SSO Integration parentEpicId is '{sso_epic.get('parentEpicId')}', expected '{sec_epic['id']}'.")

    # Check health status
    if sso_epic.get("healthStatus") != "on_track":
        errors.append(f"Health status is '{sso_epic.get('healthStatus')}', expected 'on_track'.")

    if errors:
        return False, " ".join(errors)

    return True, "Enterprise SSO Integration is a child of Security Hardening with health status on_track."
