import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Dawn was duplicated (a new copy exists)."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Seed already has 'Copy of Dawn' (id 7). A new duplicate would be an additional theme.
    dawn_copies = [t for t in state["themes"] if t["name"].startswith("Copy of") and "Dawn" in t["name"]]
    if len(dawn_copies) < 2:
        return False, f"Expected at least 2 'Copy of Dawn' themes, found {len(dawn_copies)}."

    # The new copy should be a draft
    new_copies = [t for t in dawn_copies if t["id"] != 7]
    if not new_copies:
        return False, "No new copy of Dawn found (only the pre-existing copy)."

    new_copy = new_copies[0]
    if new_copy.get("status") != "draft":
        return False, f"New copy status is '{new_copy.get('status')}', expected 'draft'."

    return True, "Theme 'Dawn' successfully duplicated."
