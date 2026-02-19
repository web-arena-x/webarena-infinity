import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that theme 'Craft' was renamed to 'Artisan'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    craft = [t for t in state["themes"] if t["name"] == "Craft"]
    if craft:
        return False, "Theme 'Craft' still exists (not renamed)."

    artisan = [t for t in state["themes"] if t["name"] == "Artisan"]
    if not artisan:
        return False, "Theme 'Artisan' not found."

    return True, "Theme 'Craft' successfully renamed to 'Artisan'."
