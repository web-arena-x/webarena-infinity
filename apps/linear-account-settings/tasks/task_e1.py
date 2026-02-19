import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the user's full name was changed to 'Jordan R. Rivera'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    cu = state.get("currentUser", {})
    name = cu.get("name", "")

    if name != "Jordan R. Rivera":
        return False, f"Expected name 'Jordan R. Rivera', got '{name}'."

    # Verify sync to workspaceMembers
    members = state.get("workspaceMembers", [])
    member = next((m for m in members if m["id"] == cu["id"]), None)
    if member and member.get("name") != "Jordan R. Rivera":
        return False, f"Name not synced to workspaceMembers: got '{member.get('name')}'."

    return True, "User's name successfully changed to 'Jordan R. Rivera'."
