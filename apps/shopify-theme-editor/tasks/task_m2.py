import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify 'Image banner' section renamed to 'Hero Section'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Section id 3 was 'Image banner' in template 1
    section = next((s for s in state["sections"] if s.get("id") == 3), None)
    if not section:
        return False, "Section id 3 not found."

    if section.get("name") != "Hero Section":
        return False, f"Section name is '{section.get('name')}', expected 'Hero Section'."

    return True, "Section 'Image banner' renamed to 'Hero Section'."
