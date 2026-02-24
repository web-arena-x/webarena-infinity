import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify a new 'Image with text' section exists in the template area."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    # The seed already has one image_with_text section (section_7)
    iwt_sections = [s for s in state["sections"]
                    if s["type"] == "image_with_text" and s["templateId"] == "home" and s["group"] == "template"]

    if len(iwt_sections) < 2:
        return False, f"Expected at least 2 'Image with text' sections in template area, found {len(iwt_sections)}."

    return True, "New 'Image with text' section added to template area."
