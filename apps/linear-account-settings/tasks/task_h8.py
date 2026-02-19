import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify name='Jordan Rivera-Chen', username='jordan.rc', home view='inbox'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    cu = state.get("currentUser", {})
    prefs = state.get("preferences", {})

    name = cu.get("name")
    username = cu.get("username")
    home_view = prefs.get("defaultHomeView")

    if name != "Jordan Rivera-Chen":
        return False, f"Expected name='Jordan Rivera-Chen', got '{name}'."
    if username != "jordan.rc":
        return False, f"Expected username='jordan.rc', got '{username}'."
    if home_view != "inbox":
        return False, f"Expected defaultHomeView='inbox', got '{home_view}'."

    # Verify sync to workspaceMembers
    members = state.get("workspaceMembers", [])
    member = next((m for m in members if m["id"] == cu["id"]), None)
    if member:
        if member.get("name") != "Jordan Rivera-Chen":
            return False, f"Name not synced to workspaceMembers: got '{member.get('name')}'."
        if member.get("username") != "jordan.rc":
            return False, f"Username not synced to workspaceMembers: got '{member.get('username')}'."

    return True, "Name, username, and home view all updated correctly."
