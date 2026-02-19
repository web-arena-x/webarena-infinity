import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the user's username was changed to 'j.rivera'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    cu = state.get("currentUser", {})
    username = cu.get("username", "")

    if username != "j.rivera":
        return False, f"Expected username 'j.rivera', got '{username}'."

    # Verify sync to workspaceMembers
    members = state.get("workspaceMembers", [])
    member = next((m for m in members if m["id"] == cu["id"]), None)
    if member and member.get("username") != "j.rivera":
        return False, f"Username not synced to workspaceMembers: got '{member.get('username')}'."

    return True, "User's username successfully changed to 'j.rivera'."
