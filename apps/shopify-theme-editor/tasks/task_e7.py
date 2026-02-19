import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the 'Email signup' section was removed from the Default product template."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Section id 7 was 'Email signup' in template 1
    email_section = [s for s in state["sections"]
                     if s.get("templateId") == 1 and s.get("type") == "newsletter"
                     and s.get("name") == "Email signup"]
    if email_section:
        return False, "Section 'Email signup' still exists in the Default product template."

    # Also check blocks were cleaned up
    blocks_for_7 = [b for b in state["blocks"] if b.get("sectionId") == 7]
    if blocks_for_7:
        return False, f"Found {len(blocks_for_7)} orphaned blocks for removed section."

    return True, "Section 'Email signup' successfully removed from Default product template."
