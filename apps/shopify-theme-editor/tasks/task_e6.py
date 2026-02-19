import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the 'Related products' section is now visible (unhidden)."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find template 1 (Default product, Dawn theme)
    section = next((s for s in state["sections"]
                    if s.get("templateId") == 1 and s.get("name") == "Related products"), None)
    if not section:
        return False, "Section 'Related products' not found in Default product template."

    if section.get("hidden") != False:
        return False, f"Section 'Related products' is still hidden."

    return True, "Section 'Related products' is now visible."
