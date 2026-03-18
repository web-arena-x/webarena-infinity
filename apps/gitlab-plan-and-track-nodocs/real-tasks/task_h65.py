import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # #57 (confidential SAML issue) -> non-confidential, milestoneId 3 (v2.0)
    issue57 = next((i for i in state["issues"] if i["id"] == 57), None)
    if issue57 is None:
        return False, "Issue #57 not found."
    if issue57.get("confidential") is True:
        return False, "Issue #57 is still confidential."
    if issue57.get("milestoneId") != 3:
        return False, f"Issue #57 milestoneId is {issue57.get('milestoneId')}, expected 3 (v2.0)."

    # #2 (non-confidential SAML issue) -> iterationId 8 (Sprint 8), weight 8
    issue2 = next((i for i in state["issues"] if i["id"] == 2), None)
    if issue2 is None:
        return False, "Issue #2 not found."
    if issue2.get("iterationId") != 8:
        return False, f"Issue #2 iterationId is {issue2.get('iterationId')}, expected 8 (Sprint 8)."
    if issue2.get("weight") != 8:
        return False, f"Issue #2 weight is {issue2.get('weight')}, expected 8."

    return True, "SAML issues updated: #57 non-confidential in v2.0, #2 in Sprint 8 with weight 8."
