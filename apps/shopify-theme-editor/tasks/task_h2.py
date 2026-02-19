import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify new Rich text section with Heading block added to Contact template."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Template 5 = Contact template for Dawn
    # Check for a new rich-text section
    rt_sections = [s for s in state["sections"]
                   if s.get("templateId") == 5 and s.get("type") == "rich-text"
                   and s.get("area") == "template"]

    if not rt_sections:
        return False, "No Rich text section found in Contact template."

    # Check that at least one of those sections has a heading block
    found_heading = False
    for section in rt_sections:
        heading_blocks = [b for b in state["blocks"]
                          if b.get("sectionId") == section["id"] and b.get("type") == "heading"]
        if heading_blocks:
            found_heading = True
            break

    if not found_heading:
        return False, "No Heading block found in the new Rich text section."

    return True, "Rich text section with Heading block added to Contact template."
