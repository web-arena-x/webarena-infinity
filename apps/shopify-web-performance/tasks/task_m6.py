import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    budgets = state.get("performanceBudgets", {})
    lcp = budgets.get("lcp", {})
    if lcp.get("target") != 2000:
        return False, f"Expected LCP target 2000, got {lcp.get('target')}."
    if lcp.get("warning") != 3000:
        return False, f"Expected LCP warning 3000, got {lcp.get('warning')}."
    return True, "LCP performance budget updated: target=2000, warning=3000."
