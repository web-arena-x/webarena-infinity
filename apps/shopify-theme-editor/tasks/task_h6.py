import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify new Image banner section with Heading block and Button block."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    # Seed has one image_banner (section_6)
    ib_sections = [s for s in state["sections"]
                   if s["type"] == "image_banner" and s["templateId"] == "home" and s["group"] == "template"]

    if len(ib_sections) < 2:
        return False, f"Expected at least 2 image_banner sections, found {len(ib_sections)}."

    # Find the new one
    new_ib = [s for s in ib_sections if s["id"] != "section_6"]
    if not new_ib:
        return False, "No new image banner section found."

    blocks = new_ib[0]["blocks"]
    heading_blocks = [b for b in blocks if b["type"] == "heading"]
    button_blocks = [b for b in blocks if b["type"] == "button"]

    if not heading_blocks:
        return False, "New image banner section has no Heading block."
    if not button_blocks:
        return False, "New image banner section has no Button block."

    return True, "New Image banner section with Heading and Button blocks found."
