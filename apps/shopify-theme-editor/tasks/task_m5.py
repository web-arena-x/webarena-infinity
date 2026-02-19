import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify block 'Aisha Patel' removed from 'Team members' section in About template."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Section 24 = 'Team members' in About template (template 6)
    # Block id 22 = 'Aisha Patel' column block
    block = next((b for b in state["blocks"] if b.get("id") == 22), None)
    if block:
        return False, "Block 'Aisha Patel' still exists."

    # Also check by name in section 24 blocks
    aisha_blocks = [b for b in state["blocks"]
                    if b.get("sectionId") == 24 and b.get("name") == "Aisha Patel"]
    if aisha_blocks:
        return False, "Block 'Aisha Patel' still found in Team members section."

    return True, "Block 'Aisha Patel' removed from Team members section."
