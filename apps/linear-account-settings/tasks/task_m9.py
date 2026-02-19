import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify email digest settings: SLA breach immediate=true, delay low priority=false."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    digest = state.get("emailDigestSettings", {})

    sla = digest.get("sendImmediatelyOnSLABreach")
    delay = digest.get("delayLowPriorityToWorkHours")

    if sla is not True:
        return False, f"Expected sendImmediatelyOnSLABreach=true, got {sla}."
    if delay is not False:
        return False, f"Expected delayLowPriorityToWorkHours=false, got {delay}."

    return True, "Email digest settings updated correctly."
