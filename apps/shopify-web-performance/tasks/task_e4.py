import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    match = [a for a in state["alertRules"] if a["name"] == "CLS Regression Alert"]
    if match:
        return False, "Alert rule 'CLS Regression Alert' still exists."
    return True, "Alert rule 'CLS Regression Alert' deleted."
