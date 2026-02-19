import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    rule = next((a for a in state["alertRules"] if a["name"] == "Collection Page LCP"), None)
    if not rule:
        return False, "Alert rule 'Collection Page LCP' not found."
    if rule.get("metric") != "lcp":
        return False, f"Expected metric 'lcp', got '{rule.get('metric')}'."
    if rule.get("threshold") != 3000:
        return False, f"Expected threshold 3000, got {rule.get('threshold')}."
    if rule.get("pageType") != "collection":
        return False, f"Expected pageType 'collection', got '{rule.get('pageType')}'."
    return True, "Alert rule 'Collection Page LCP' created correctly."
