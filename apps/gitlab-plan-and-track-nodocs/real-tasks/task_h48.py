import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Issue #1 blocks #2 — agent must discover this
    issue1 = next((i for i in state["issues"] if i["id"] == 1), None)
    if issue1 is None:
        return False, "Issue #1 not found."

    # 20 hours = 72000 seconds added; original was 14400
    if issue1.get("timeSpent", 0) < 86400:
        return False, f"Issue #1 timeSpent is {issue1.get('timeSpent')}, expected at least 86400 (original 14400 + 72000)."

    # Priority should be critical (11), not high (12)
    if 11 not in issue1.get("labelIds", []):
        return False, f"Issue #1 does not have priority::critical (id 11). Labels: {issue1.get('labelIds')}."
    if 12 in issue1.get("labelIds", []):
        return False, f"Issue #1 still has priority::high (id 12). Labels: {issue1.get('labelIds')}."

    return True, "Issue #1 (blocker of #2) has 20h time spent logged and priority changed to critical."
