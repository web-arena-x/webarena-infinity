import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    event = next((e for e in state["events"] if e["title"] == "Installed PageFly Landing Page Builder"), None)
    if not event:
        return False, "Event with title 'Installed PageFly Landing Page Builder' not found."
    if event.get("impact") != "neutral":
        return False, f"Expected impact 'neutral', got '{event.get('impact')}'."
    # Make sure old title is gone
    old = [e for e in state["events"] if e["title"] == "Installed PageFly Builder"]
    if old:
        return False, "Old event title 'Installed PageFly Builder' still exists."
    return True, "Event updated: title and impact changed."
