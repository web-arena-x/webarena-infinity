import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify a new Rich text section was added to Dawn's Default product template."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Template 1 = Default product for Dawn (theme 1)
    rich_text_sections = [s for s in state["sections"]
                          if s.get("templateId") == 1 and s.get("type") == "rich-text"
                          and s.get("area") == "template"]

    # Seed has one rich-text section (id 4) in template 1
    if len(rich_text_sections) < 2:
        return False, f"Expected at least 2 Rich text sections in template, found {len(rich_text_sections)}."

    new_sections = [s for s in rich_text_sections if s.get("id") != 4]
    if not new_sections:
        return False, "No new Rich text section found."

    return True, "New Rich text section added to Default product template."
