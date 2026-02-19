import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    craft = next((t for t in state["themes"] if t["name"] == "Craft"), None)
    if not craft:
        return False, "Theme 'Craft' not found."
    if not craft.get("active"):
        return False, "Theme 'Craft' is not active."
    settings = craft.get("settings", {})
    if settings.get("lazyLoading") != True:
        return False, f"Lazy loading should be enabled (got {settings.get('lazyLoading')})."
    if settings.get("paginationLimit") != 32:
        return False, f"Expected pagination limit 32, got {settings.get('paginationLimit')}."
    # Dawn should no longer be active
    dawn = next((t for t in state["themes"] if t["name"] == "Dawn"), None)
    if dawn and dawn.get("active"):
        return False, "Theme 'Dawn' is still active."
    return True, "Theme 'Craft' activated with lazy loading enabled and pagination=32."
