import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify blocks in 'Our story' section of About template were updated."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Section 23 = 'Our story' in About template (template 6)
    # Block 18 = Heading block, Block 19 = Content block
    heading_block = next((b for b in state["blocks"]
                          if b.get("sectionId") == 23 and b.get("type") == "heading"), None)
    if not heading_block:
        return False, "Heading block not found in 'Our story' section."

    heading_text = heading_block.get("settings", {}).get("text")
    if heading_text != "Our Values":
        return False, f"Heading text is '{heading_text}', expected 'Our Values'."

    content_block = next((b for b in state["blocks"]
                          if b.get("sectionId") == 23 and b.get("type") == "text"), None)
    if not content_block:
        return False, "Content block not found in 'Our story' section."

    content_text = content_block.get("settings", {}).get("text")
    expected = "We are committed to sustainability and ethical sourcing in everything we do."
    if content_text != expected:
        return False, f"Content text does not match expected value."

    return True, "Both blocks in 'Our story' section updated correctly."
