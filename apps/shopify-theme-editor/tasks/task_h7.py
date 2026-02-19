import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify 'Sale announcement' block removed and 'Subheading' block hidden."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Block id 2 = 'Sale announcement' in section 2 (Announcement bar)
    sale_block = next((b for b in state["blocks"] if b.get("id") == 2), None)
    if sale_block:
        return False, "Block 'Sale announcement' (id 2) still exists."

    # Block id 4 = 'Subheading' in section 3 (Image banner)
    sub_block = next((b for b in state["blocks"] if b.get("id") == 4), None)
    if not sub_block:
        return False, "Block 'Subheading' (id 4) not found."

    if sub_block.get("hidden") is not True:
        return False, f"Block 'Subheading' is not hidden (hidden={sub_block.get('hidden')})."

    return True, "'Sale announcement' removed and 'Subheading' hidden."
