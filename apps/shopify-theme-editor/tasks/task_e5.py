import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that theme 'Minimalist' was added."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    theme = next((t for t in state["themes"] if t["name"] == "Minimalist"), None)
    if not theme:
        return False, "Theme 'Minimalist' not found."

    if theme.get("source") != "shopify":
        return False, f"Expected source 'shopify', got '{theme.get('source')}'."

    if theme.get("architecture") != "online_store_2.0":
        return False, f"Expected architecture 'online_store_2.0', got '{theme.get('architecture')}'."

    if theme.get("status") != "draft":
        return False, f"Expected status 'draft', got '{theme.get('status')}'."

    return True, "Theme 'Minimalist' added with correct source and architecture."
