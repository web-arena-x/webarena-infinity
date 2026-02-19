import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    rule = next((a for a in state["alertRules"] if a["name"] == "LCP Budget Exceeded"), None)
    if not rule:
        return False, "Alert rule 'LCP Budget Exceeded' not found."
    if rule.get("enabled") != False:
        return False, f"Alert rule is still enabled (enabled={rule.get('enabled')})."
    return True, "Alert rule 'LCP Budget Exceeded' disabled."
