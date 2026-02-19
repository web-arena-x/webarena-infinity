import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    event = next((e for e in state["events"] if e["title"] == "Migrated to new image CDN"), None)
    if not event:
        return False, "Event 'Migrated to new image CDN' not found."
    if event.get("type") != "code_change":
        return False, f"Expected type 'code_change', got '{event.get('type')}'."
    if event.get("metric") != "lcp":
        return False, f"Expected metric 'lcp', got '{event.get('metric')}'."
    if event.get("impact") != "positive":
        return False, f"Expected impact 'positive', got '{event.get('impact')}'."
    return True, "Event 'Migrated to new image CDN' added correctly."
