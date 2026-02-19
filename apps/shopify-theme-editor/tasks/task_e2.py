import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that theme 'Crave' was deleted."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    crave = [t for t in state["themes"] if t["name"] == "Crave"]
    if crave:
        return False, "Theme 'Crave' still exists."

    # Also check no templates/sections/blocks left for this theme
    crave_templates = [t for t in state["templates"] if t.get("themeId") == 6]
    if crave_templates:
        return False, f"Found {len(crave_templates)} orphaned templates for deleted theme."

    return True, "Theme 'Crave' successfully deleted."
