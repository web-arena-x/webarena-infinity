import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    # Check page
    page = next((p for p in state["pages"] if p["name"] == "Loyalty Program"), None)
    if not page:
        return False, "Page 'Loyalty Program' not found."
    if page.get("path") != "/pages/loyalty-program":
        return False, f"Expected path '/pages/loyalty-program', got '{page.get('path')}'."
    if page.get("type") != "page":
        return False, f"Expected type 'page', got '{page.get('type')}'."
    if page.get("priority") != "high":
        return False, f"Expected priority 'high', got '{page.get('priority')}'."
    # Check event
    event = next((e for e in state["events"] if e["title"] == "Launched loyalty program page"), None)
    if not event:
        return False, "Event 'Launched loyalty program page' not found."
    if event.get("type") != "custom":
        return False, f"Expected event type 'custom', got '{event.get('type')}'."
    if event.get("metric") != "all":
        return False, f"Expected metric 'all', got '{event.get('metric')}'."
    if event.get("impact") != "neutral":
        return False, f"Expected impact 'neutral', got '{event.get('impact')}'."
    return True, "Page and event created correctly."
