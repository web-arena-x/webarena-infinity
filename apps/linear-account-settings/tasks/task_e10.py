import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that subscription to NEX-987 was removed."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    subs = state.get("issueSubscriptions", [])

    nex987 = [s for s in subs if s.get("issueId") == "NEX-987"]
    if nex987:
        return False, "Subscription to NEX-987 still exists."

    return True, "Successfully unsubscribed from NEX-987."
