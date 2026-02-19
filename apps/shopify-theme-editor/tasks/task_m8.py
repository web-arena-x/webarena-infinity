import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify 'Featured collection' section was duplicated in Default product template."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Template 1 = Default product
    fc_sections = [s for s in state["sections"]
                   if s.get("templateId") == 1 and s.get("type") == "featured-collection"]

    # Seed has 1 featured-collection (id 5)
    if len(fc_sections) < 2:
        return False, f"Expected at least 2 Featured collection sections, found {len(fc_sections)}."

    copy_sections = [s for s in fc_sections if s.get("id") != 5]
    if not copy_sections:
        return False, "No duplicate of Featured collection found."

    return True, "Featured collection section duplicated successfully."
