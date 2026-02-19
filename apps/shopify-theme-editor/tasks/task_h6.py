import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify new Announcement block added to Announcement bar in Default product template."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Section 2 = Announcement bar in template 1
    announcement_blocks = [b for b in state["blocks"]
                           if b.get("sectionId") == 2 and b.get("type") == "announcement"]

    # Seed has 2 announcement blocks (ids 1, 2)
    if len(announcement_blocks) < 3:
        return False, f"Expected at least 3 Announcement blocks, found {len(announcement_blocks)}."

    new_blocks = [b for b in announcement_blocks if b.get("id") not in [1, 2]]
    if not new_blocks:
        return False, "No new Announcement block found."

    return True, f"New Announcement block added. Total announcements: {len(announcement_blocks)}."
